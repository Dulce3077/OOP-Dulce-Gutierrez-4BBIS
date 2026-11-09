class SuscripcionExpiradaError(Exception):
    pass

class PuntosInsuficientesError(Exception):
    pass

class PerfilMovil:

    def __init__(self, username, gemas=50, racha_dias=1,
                 notificaciones_activas=True):

        if not isinstance(gemas, int) or isinstance(gemas, bool) or gemas < 0:
            raise ValueError("Las gemas no pueden ser negativas.")

        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:

        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:

        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva.")

        if cantidad > self.gemas:
            raise PuntosInsuficientesError("No tienes suficientes gemas.")

        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):

    def __init__(self, username, meses_suscripcion, gemas=50,
                 racha_dias=1, notificaciones_activas=True):

        if not isinstance(meses_suscripcion, int) or isinstance(meses_suscripcion, bool) or meses_suscripcion <= 0:
            raise ValueError("La suscripcion debe ser mayor a cero.")

        super().__init__(username, gemas, racha_dias,
                         notificaciones_activas)

        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:

        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("Tu suscripcion ha expirado.")

        return "Descarga de contenido offline exitosa."
