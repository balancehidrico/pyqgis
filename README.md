# balancehidrico.py
El *script* `balancehidrico.py` genera un modelo de balance hídrico. Es un programa desarrollado en el lenguaje [Python](https://www.python.org/) para ejecutarse en el sistema de información geográfica [QGIS](https://qgis.org/).

## Entradas
1. 12 archivos raster con promedios mensuales de precipitación con nombres: `p_01.tif`, `p_02.tif`, `p_03.tif`, ..., `p_10.tif`, `p_11.tif`, `p_12.tif`.
2. 12 archivos raster con promedios mensuales de evapotranspiración potencial con nombres: `etp_01.tif`, `etp_02.tif`, `etp_03.tif`, ..., `etp_10.tif`, `etp_11.tif`, `etp_12.tif`.
3. 1 archivo de propiedades con valores de variables a utilizar en los cálculos. Este archivo debe llamarse `balancehidrico.ini`. Seguidamente se presenta un ejemplo de su contenido:

```
# Parámetros generales
[general]
llu_ret=0.2
fc=18.41
kp=0.06
kv=0.10
kfc=0.05191
i=1
hsi=860
cc_mm=1093.5
pm_mm=594.14
cc_pm_mm=499.37
```

## Salidas
1. Mapas raster del modelo de balance hídrico.

## Ejecución del script
1. Descargue en su computadora los siguientes archivos (se recomienda colocarlos en un directorio separado):
    - [balancehidrico.py](https://github.com/balancehidrico/pyqgis/blob/main/balancehidrico.py)
    - [balancehidrico.ini](https://github.com/balancehidrico/pyqgis/blob/main/balancehidrico.ini)
2. Coloque en el mismo directorio los 12 archivos raster de precipitación y de evapotranspiración potencial.
3. Abra en QGIS el *script* `balancehidrico.py` con la opción de menú *Plugins - Python Console* y el botón *Open Script...*. Luego ejecútelo con el botón *Run Script*.
