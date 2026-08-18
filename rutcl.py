def limpiar_rut(rut: str) -> str:
    return rut.replace(".", "").replace("-", "").replace(" ", "").upper()


def calcular_dv(rut: str) -> str:
    rut_limpio = limpiar_rut(rut)
    revertido = reversed(rut_limpio)
    multiplicador = 2
    suma = 0
    for digito in revertido:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    resto = 11 - (suma % 11)
    if resto == 11:
        return "0"
    elif resto == 10:
        return "K"
    else:
        return str(resto)


def formatear_rut(rut: str) -> str:
    rut_limpio = limpiar_rut(rut)
    cuerpo = rut_limpio[:-1]
    dv = rut_limpio[-1]
    cuerpo_formateado = ""
    for i, digito in enumerate(reversed(cuerpo)):
        if i > 0 and i % 3 == 0:
            cuerpo_formateado = "." + cuerpo_formateado
        cuerpo_formateado = digito + cuerpo_formateado
    return f"{cuerpo_formateado}-{dv}"


def validar_rut(rut: str) -> bool:
    rut_limpio = limpiar_rut(rut)
    if len(rut_limpio) < 2:
        return False
    cuerpo = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]
    dv_calculado = calcular_dv(cuerpo)
    return dv_ingresado == dv_calculado
