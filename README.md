# RUTCL

Libreria en Python para validar, formatear y calcular RUT chileno. Sin dependencias externas.

## Instalacion

```bash
pip install rutcl
```

## Funciones

### `validar_rut(rut)`

Valida si un RUT es correcto comparando el digito verificador.

```python
from rutcl import validar_rut

validar_rut("12.345.678-5")  # True
validar_rut("12.345.678-9")  # False
validar_rut("60803000-K")    # True (Ministerio de Hacienda)
```

### `calcular_dv(rut)`

Calcula el digito verificador de un RUT.

```python
from rutcl import calcular_dv

calcular_dv("12345678")   # "5"
calcular_dv("60803000")   # "K"
```

### `formatear_rut(rut)`

Formatea un RUT con puntos y guion.

```python
from rutcl import formatear_rut

formatear_rut("123456785")  # "12.345.678-5"
formatear_rut("12345678K")  # "12.345.678-K"
```

### `limpiar_rut(rut)`

Elimina puntos, guiones y espacios de un RUT.

```python
from rutcl import limpiar_rut

limpiar_rut("12.345.678-5")  # "123456785"
```

## Licencia

MIT
