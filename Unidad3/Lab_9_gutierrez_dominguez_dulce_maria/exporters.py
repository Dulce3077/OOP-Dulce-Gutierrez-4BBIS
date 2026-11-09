
import csv
import json
from fpdf import FPDF
from abc import ABC, abstractmethod


class Exporter(ABC):

    @abstractmethod
    def export(self, data, file_path):
        raise NotImplementedError


class CSVExporter(Exporter):

    def export(self, data, file_path):

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Product Name",
                "Price"
            ])

            for product in data:
                writer.writerow([
                    product["id_product"],
                    product["product_name"],
                    product["price"]
                ])


class TXTExporter(Exporter):

    def export(self, data, file_path):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write("PRODUCT INVENTORY REPORT\n")
            file.write("=" * 40 + "\n\n")

            for product in data:

                file.write(
                    f"ID: {product['id_product']}\n"
                    f"Product: {product['product_name']}\n"
                    f"Price: ${product['price']}\n"
                    + "-" * 30 + "\n"
                )


class JSONExporter(Exporter):

    def export(self, data, file_path):

        productos = []

        for product in data:

            productos.append({
                "id_product": product["id_product"],
                "product_name": product["product_name"],
                "price": float(product["price"])
            })

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                productos,
                file,
                indent=4,
                ensure_ascii=False
            )


class PDFExporter(Exporter):

    def export(self, data, file_path):

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", "B", 16)

        pdf.cell(
            190,
            10,
            "PRODUCT INVENTORY REPORT",
            ln=True,
            align="C"
        )

        pdf.ln(10)

        pdf.set_font("Arial", "B", 12)

        pdf.cell(25, 10, "ID", border=1)
        pdf.cell(100, 10, "Product Name", border=1)
        pdf.cell(65, 10, "Price", border=1, ln=True)

        pdf.set_font("Arial", size=11)

        for product in data:

            pdf.cell(
                25,
                10,
                str(product["id_product"]),
                border=1
            )

            pdf.cell(
                100,
                10,
                str(product["product_name"]),
                border=1
            )

            pdf.cell(
                65,
                10,
                f"${float(product['price']):.2f}",
                border=1,
                ln=True
            )

        pdf.output(file_path)
