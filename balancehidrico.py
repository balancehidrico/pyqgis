import os
import configparser

from qgis.PyQt import QtGui
from console.console import _console



#                                     #
#                                     #
# Modelo de balance hídrico de suelos #
#                                     #
#                                     #



#
#
# Lectura de archivo con valores
#
#

config = configparser.ConfigParser()
config.read('E:/balancehidrico/balancehidrico.ini')



#
#
# Constantes
#
#

print("Valores leídos de balancehidrico.ini:")
LLU_RET = float(config.get("general", "llu_ret"))
print("LLU_RET", LLU_RET)
FC = float(config.get("general", "fc"))
print("FC", FC)
KP = float(config.get("general", "kp"))
print("KP", KP)
KV = float(config.get("general", "kv"))
print("KV", KV)
KFC = float(config.get("general", "kfc"))
print("KFC", KFC)
I = float(config.get("general", "i"))
print("I", I)
HSI = float(config.get("general", "hsi"))
print("HSI", HSI)
CC_MM = float(config.get("general", "cc_mm"))
print("CC_MM", CC_MM)
PM_MM = float(config.get("general", "pm_mm"))
print("PM_MM", PM_MM)
CC_PM_MM = float(config.get("general", "cc_pm_mm"))
print("CC_PM_MM", CC_PM_MM)


#
#
# Archivos
#
#

# Directorio del script
dir_script = os.path.dirname(_console.console.tabEditorWidget.currentWidget().path) + "/"

# Directorios de datos de entrada
datos_entrada = dir_script
# datos_entrada = 'C:/Users/mfvargas/balancehidrico/datos/entrada/'
# datos_entrada = 'E:/balancehidrico/datos/entrada/'
# datos_entrada = '/home/mfvargas/balancehidrico/balancehidrico/datos/entrada/'

# Directorio de datos de salida
if not os.path.exists(dir_script + "salida"):
    os.makedirs(dir_script + "salida")
datos_salida = dir_script + "salida/"
# datos_salida = 'C:/Users/mfvargas/balancehidrico/datos/salida/'
# datos_salida = 'E:/balancehidrico/datos/salida/'
# datos_salida = '/home/mfvargas/balancehidrico/balancehidrico/datos/salida/'


# Precipitación media (p)
p_01_fn = datos_entrada + 'p_01.tif'
p_02_fn = datos_entrada + 'p_02.tif'
p_03_fn = datos_entrada + 'p_03.tif'
p_04_fn = datos_entrada + 'p_04.tif'
p_05_fn = datos_entrada + 'p_05.tif'
p_06_fn = datos_entrada + 'p_06.tif'
p_07_fn = datos_entrada + 'p_07.tif'
p_08_fn = datos_entrada + 'p_08.tif'
p_09_fn = datos_entrada + 'p_09.tif'
p_10_fn = datos_entrada + 'p_10.tif'
p_11_fn = datos_entrada + 'p_11.tif'
p_12_fn = datos_entrada + 'p_12.tif'
p_suma_fn = datos_salida + 'p_suma.tif'

# Evapotranspiración potencial (etp)
etp_01_fn = datos_entrada + 'etp_01.tif'
etp_02_fn = datos_entrada + 'etp_02.tif'
etp_03_fn = datos_entrada + 'etp_03.tif'
etp_04_fn = datos_entrada + 'etp_04.tif'
etp_05_fn = datos_entrada + 'etp_05.tif'
etp_06_fn = datos_entrada + 'etp_06.tif'
etp_07_fn = datos_entrada + 'etp_07.tif'
etp_08_fn = datos_entrada + 'etp_08.tif'
etp_09_fn = datos_entrada + 'etp_09.tif'
etp_10_fn = datos_entrada + 'etp_10.tif'
etp_11_fn = datos_entrada + 'etp_11.tif'
etp_12_fn = datos_entrada + 'etp_12.tif'
etp_suma_fn = datos_salida + 'etp_suma.tif'

# Precipitación retenida (ret)
ret_01_fn = datos_salida + 'ret_01.tif'
ret_02_fn = datos_salida + 'ret_02.tif'
ret_03_fn = datos_salida + 'ret_03.tif'
ret_04_fn = datos_salida + 'ret_04.tif'
ret_05_fn = datos_salida + 'ret_05.tif'
ret_06_fn = datos_salida + 'ret_06.tif'
ret_07_fn = datos_salida + 'ret_07.tif'
ret_08_fn = datos_salida + 'ret_08.tif'
ret_09_fn = datos_salida + 'ret_09.tif'
ret_10_fn = datos_salida + 'ret_10.tif'
ret_11_fn = datos_salida + 'ret_11.tif'
ret_12_fn = datos_salida + 'ret_12.tif'
ret_suma_fn = datos_salida + 'ret_suma.tif'

# Precipitación infiltrada (pi)
pi_01_fn = datos_salida + 'pi_01.tif'
pi_02_fn = datos_salida + 'pi_02.tif'
pi_03_fn = datos_salida + 'pi_03.tif'
pi_04_fn = datos_salida + 'pi_04.tif'
pi_05_fn = datos_salida + 'pi_05.tif'
pi_06_fn = datos_salida + 'pi_06.tif'
pi_07_fn = datos_salida + 'pi_07.tif'
pi_08_fn = datos_salida + 'pi_08.tif'
pi_09_fn = datos_salida + 'pi_09.tif'
pi_10_fn = datos_salida + 'pi_10.tif'
pi_11_fn = datos_salida + 'pi_11.tif'
pi_12_fn = datos_salida + 'pi_12.tif'
pi_suma_fn = datos_salida + 'pi_suma.tif'

# Escorrentía superficial (esc)
esc_01_fn = datos_salida + 'esc_01.tif'
esc_02_fn = datos_salida + 'esc_02.tif'
esc_03_fn = datos_salida + 'esc_03.tif'
esc_04_fn = datos_salida + 'esc_04.tif'
esc_05_fn = datos_salida + 'esc_05.tif'
esc_06_fn = datos_salida + 'esc_06.tif'
esc_07_fn = datos_salida + 'esc_07.tif'
esc_08_fn = datos_salida + 'esc_08.tif'
esc_09_fn = datos_salida + 'esc_09.tif'
esc_10_fn = datos_salida + 'esc_10.tif'
esc_11_fn = datos_salida + 'esc_11.tif'
esc_12_fn = datos_salida + 'esc_12.tif'
esc_suma_fn = datos_salida + 'esc_suma.tif'

# Humedad de suelo inicial (hsi)
hsi_01_fn = datos_salida + 'hsi_01.tif'
hsi_02_fn = datos_salida + 'hsi_02.tif'
hsi_03_fn = datos_salida + 'hsi_03.tif'
hsi_04_fn = datos_salida + 'hsi_04.tif'
hsi_05_fn = datos_salida + 'hsi_05.tif'
hsi_06_fn = datos_salida + 'hsi_06.tif'
hsi_07_fn = datos_salida + 'hsi_07.tif'
hsi_08_fn = datos_salida + 'hsi_08.tif'
hsi_09_fn = datos_salida + 'hsi_09.tif'
hsi_10_fn = datos_salida + 'hsi_10.tif'
hsi_11_fn = datos_salida + 'hsi_11.tif'
hsi_12_fn = datos_salida + 'hsi_12.tif'
hsi_suma_fn = datos_salida + 'hsi_suma.tif'

# Factor de ETP, por cierre de estomas, antes que ocurra ETR (c1)
c1_01_fn = datos_salida + 'c1_01.tif'
c1_02_fn = datos_salida + 'c1_02.tif'
c1_03_fn = datos_salida + 'c1_03.tif'
c1_04_fn = datos_salida + 'c1_04.tif'
c1_05_fn = datos_salida + 'c1_05.tif'
c1_06_fn = datos_salida + 'c1_06.tif'
c1_07_fn = datos_salida + 'c1_07.tif'
c1_08_fn = datos_salida + 'c1_08.tif'
c1_09_fn = datos_salida + 'c1_09.tif'
c1_10_fn = datos_salida + 'c1_10.tif'
c1_11_fn = datos_salida + 'c1_11.tif'
c1_12_fn = datos_salida + 'c1_12.tif'

# Factor de ETP, por cierre de estomas, después de que ocurra ETR (c2)
c2_01_fn = datos_salida + 'c2_01.tif'
c2_02_fn = datos_salida + 'c2_02.tif'
c2_03_fn = datos_salida + 'c2_03.tif'
c2_04_fn = datos_salida + 'c2_04.tif'
c2_05_fn = datos_salida + 'c2_05.tif'
c2_06_fn = datos_salida + 'c2_06.tif'
c2_07_fn = datos_salida + 'c2_07.tif'
c2_08_fn = datos_salida + 'c2_08.tif'
c2_09_fn = datos_salida + 'c2_09.tif'
c2_10_fn = datos_salida + 'c2_10.tif'
c2_11_fn = datos_salida + 'c2_11.tif'
c2_12_fn = datos_salida + 'c2_12.tif'

# Humedad disponible (hd)
hd_01_fn = datos_salida + 'hd_01.tif'
hd_02_fn = datos_salida + 'hd_02.tif'
hd_03_fn = datos_salida + 'hd_03.tif'
hd_04_fn = datos_salida + 'hd_04.tif'
hd_05_fn = datos_salida + 'hd_05.tif'
hd_06_fn = datos_salida + 'hd_06.tif'
hd_07_fn = datos_salida + 'hd_07.tif'
hd_08_fn = datos_salida + 'hd_08.tif'
hd_09_fn = datos_salida + 'hd_09.tif'
hd_10_fn = datos_salida + 'hd_10.tif'
hd_11_fn = datos_salida + 'hd_11.tif'
hd_12_fn = datos_salida + 'hd_12.tif'
hd_suma_fn = datos_salida + 'hd_suma.tif'

# Evapotranspiración real (etr)
etr_01_fn = datos_salida + 'etr_01.tif'
etr_02_fn = datos_salida + 'etr_02.tif'
etr_03_fn = datos_salida + 'etr_03.tif'
etr_04_fn = datos_salida + 'etr_04.tif'
etr_05_fn = datos_salida + 'etr_05.tif'
etr_06_fn = datos_salida + 'etr_06.tif'
etr_07_fn = datos_salida + 'etr_07.tif'
etr_08_fn = datos_salida + 'etr_08.tif'
etr_09_fn = datos_salida + 'etr_09.tif'
etr_10_fn = datos_salida + 'etr_10.tif'
etr_11_fn = datos_salida + 'etr_11.tif'
etr_12_fn = datos_salida + 'etr_12.tif'
etr_suma_fn = datos_salida + 'etr_suma.tif'

# Humedad de suelo final (hsf)
hsf_01_fn = datos_salida + 'hsf_01.tif'
hsf_02_fn = datos_salida + 'hsf_02.tif'
hsf_03_fn = datos_salida + 'hsf_03.tif'
hsf_04_fn = datos_salida + 'hsf_04.tif'
hsf_05_fn = datos_salida + 'hsf_05.tif'
hsf_06_fn = datos_salida + 'hsf_06.tif'
hsf_07_fn = datos_salida + 'hsf_07.tif'
hsf_08_fn = datos_salida + 'hsf_08.tif'
hsf_09_fn = datos_salida + 'hsf_09.tif'
hsf_10_fn = datos_salida + 'hsf_10.tif'
hsf_11_fn = datos_salida + 'hsf_11.tif'
hsf_12_fn = datos_salida + 'hsf_12.tif'
hsf_suma_fn = datos_salida + 'hsf_suma.tif'

# Déficit de capacidad de campo (dcc)
dcc_01_fn = datos_salida + 'dcc_01.tif'
dcc_02_fn = datos_salida + 'dcc_02.tif'
dcc_03_fn = datos_salida + 'dcc_03.tif'
dcc_04_fn = datos_salida + 'dcc_04.tif'
dcc_05_fn = datos_salida + 'dcc_05.tif'
dcc_06_fn = datos_salida + 'dcc_06.tif'
dcc_07_fn = datos_salida + 'dcc_07.tif'
dcc_08_fn = datos_salida + 'dcc_08.tif'
dcc_09_fn = datos_salida + 'dcc_09.tif'
dcc_10_fn = datos_salida + 'dcc_10.tif'
dcc_11_fn = datos_salida + 'dcc_11.tif'
dcc_12_fn = datos_salida + 'dcc_12.tif'
dcc_suma_fn = datos_salida + 'dcc_suma.tif'

# Recarga potencial (rp)
rp_01_fn = datos_salida + 'rp_01.tif'
rp_02_fn = datos_salida + 'rp_02.tif'
rp_03_fn = datos_salida + 'rp_03.tif'
rp_04_fn = datos_salida + 'rp_04.tif'
rp_05_fn = datos_salida + 'rp_05.tif'
rp_06_fn = datos_salida + 'rp_06.tif'
rp_07_fn = datos_salida + 'rp_07.tif'
rp_08_fn = datos_salida + 'rp_08.tif'
rp_09_fn = datos_salida + 'rp_09.tif'
rp_10_fn = datos_salida + 'rp_10.tif'
rp_11_fn = datos_salida + 'rp_11.tif'
rp_12_fn = datos_salida + 'rp_12.tif'
rp_suma_fn = datos_salida + 'rp_suma.tif'

# Necesidad de riego (nr)
nr_01_fn = datos_salida + 'nr_01.tif'
nr_02_fn = datos_salida + 'nr_02.tif'
nr_03_fn = datos_salida + 'nr_03.tif'
nr_04_fn = datos_salida + 'nr_04.tif'
nr_05_fn = datos_salida + 'nr_05.tif'
nr_06_fn = datos_salida + 'nr_06.tif'
nr_07_fn = datos_salida + 'nr_07.tif'
nr_08_fn = datos_salida + 'nr_08.tif'
nr_09_fn = datos_salida + 'nr_09.tif'
nr_10_fn = datos_salida + 'nr_10.tif'
nr_11_fn = datos_salida + 'nr_11.tif'
nr_12_fn = datos_salida + 'nr_12.tif'
nr_suma_fn = datos_salida + 'nr_suma.tif'



#
#
# Vector de entradas de la calculadora raster
#
#

entries = []



#
#
# Cálculos de p, etp, ret, pi y esc para todos los meses
#
#

#
# Precipitación mensual (p)
#

# Capas
p_01 = QgsRasterLayer(p_01_fn)
p_02 = QgsRasterLayer(p_02_fn)
p_03 = QgsRasterLayer(p_03_fn)
p_04 = QgsRasterLayer(p_04_fn)
p_05 = QgsRasterLayer(p_05_fn)
p_06 = QgsRasterLayer(p_06_fn)
p_07 = QgsRasterLayer(p_07_fn)
p_08 = QgsRasterLayer(p_08_fn)
p_09 = QgsRasterLayer(p_09_fn)
p_10 = QgsRasterLayer(p_10_fn)
p_11 = QgsRasterLayer(p_11_fn)
p_12 = QgsRasterLayer(p_12_fn)


# Entradas para la calculadora raster
entry_01 = QgsRasterCalculatorEntry()
entry_01.ref = 'p@1'
entry_01.raster = p_01
entry_01.bandNumber = 1
entries.append(entry_01)

entry_02 = QgsRasterCalculatorEntry()
entry_02.ref = 'p@2'
entry_02.raster = p_02
entry_02.bandNumber = 1
entries.append(entry_02)

entry_03 = QgsRasterCalculatorEntry()
entry_03.ref = 'p@3'
entry_03.raster = p_03
entry_03.bandNumber = 1
entries.append(entry_03)

entry_04 = QgsRasterCalculatorEntry()
entry_04.ref = 'p@4'
entry_04.raster = p_04
entry_04.bandNumber = 1
entries.append(entry_04)

entry_05 = QgsRasterCalculatorEntry()
entry_05.ref = 'p@5'
entry_05.raster = p_05
entry_05.bandNumber = 1
entries.append(entry_05)

entry_06 = QgsRasterCalculatorEntry()
entry_06.ref = 'p@6'
entry_06.raster = p_06
entry_06.bandNumber = 1
entries.append(entry_06)

entry_07 = QgsRasterCalculatorEntry()
entry_07.ref = 'p@7'
entry_07.raster = p_07
entry_07.bandNumber = 1
entries.append(entry_07)

entry_08 = QgsRasterCalculatorEntry()
entry_08.ref = 'p@8'
entry_08.raster = p_08
entry_08.bandNumber = 1
entries.append(entry_08)

entry_09 = QgsRasterCalculatorEntry()
entry_09.ref = 'p@9'
entry_09.raster = p_09
entry_09.bandNumber = 1
entries.append(entry_09)

entry_10 = QgsRasterCalculatorEntry()
entry_10.ref = 'p@10'
entry_10.raster = p_10
entry_10.bandNumber = 1
entries.append(entry_10)

entry_11 = QgsRasterCalculatorEntry()
entry_11.ref = 'p@11'
entry_11.raster = p_11
entry_11.bandNumber = 1
entries.append(entry_11)

entry_12 = QgsRasterCalculatorEntry()
entry_12.ref = 'p@12'
entry_12.raster = p_12
entry_12.bandNumber = 1
entries.append(entry_12)


# Cálculo de la suma anual
calc_sum = QgsRasterCalculator(f'p@1 + p@2 + p@3 + p@4 + p@5 + p@6 + p@7 + p@8 + p@9 + p@10 + p@11 + p@12',
                               p_suma_fn, 
                               'GTiff', 
                               p_01.extent(), 
                               p_01.width(), 
                               p_01.height(), 
                               entries)
calc_sum.processCalculation()



#
# Evapotranspiración potencial (etp)
#

# Capas
etp_01 = QgsRasterLayer(etp_01_fn)
etp_02 = QgsRasterLayer(etp_02_fn)
etp_03 = QgsRasterLayer(etp_03_fn)
etp_04 = QgsRasterLayer(etp_04_fn)
etp_05 = QgsRasterLayer(etp_05_fn)
etp_06 = QgsRasterLayer(etp_06_fn)
etp_07 = QgsRasterLayer(etp_07_fn)
etp_08 = QgsRasterLayer(etp_08_fn)
etp_09 = QgsRasterLayer(etp_09_fn)
etp_10 = QgsRasterLayer(etp_10_fn)
etp_11 = QgsRasterLayer(etp_11_fn)
etp_12 = QgsRasterLayer(etp_12_fn)


# Entradas para la calculadora raster
entry_13 = QgsRasterCalculatorEntry()
entry_13.ref = 'etp@1'
entry_13.raster = etp_01
entry_13.bandNumber = 1
entries.append(entry_13)

entry_14 = QgsRasterCalculatorEntry()
entry_14.ref = 'etp@2'
entry_14.raster = etp_02
entry_14.bandNumber = 1
entries.append(entry_14)

entry_15 = QgsRasterCalculatorEntry()
entry_15.ref = 'etp@3'
entry_15.raster = etp_03
entry_15.bandNumber = 1
entries.append(entry_15)

entry_16 = QgsRasterCalculatorEntry()
entry_16.ref = 'etp@4'
entry_16.raster = etp_04
entry_16.bandNumber = 1
entries.append(entry_16)

entry_17 = QgsRasterCalculatorEntry()
entry_17.ref = 'etp@5'
entry_17.raster = etp_05
entry_17.bandNumber = 1
entries.append(entry_17)

entry_18 = QgsRasterCalculatorEntry()
entry_18.ref = 'etp@6'
entry_18.raster = etp_06
entry_18.bandNumber = 1
entries.append(entry_18)

entry_19 = QgsRasterCalculatorEntry()
entry_19.ref = 'etp@7'
entry_19.raster = etp_07
entry_19.bandNumber = 1
entries.append(entry_19)

entry_20 = QgsRasterCalculatorEntry()
entry_20.ref = 'etp@8'
entry_20.raster = etp_08
entry_20.bandNumber = 1
entries.append(entry_20)

entry_21 = QgsRasterCalculatorEntry()
entry_21.ref = 'etp@9'
entry_21.raster = etp_09
entry_21.bandNumber = 1
entries.append(entry_21)

entry_22 = QgsRasterCalculatorEntry()
entry_22.ref = 'etp@10'
entry_22.raster = etp_10
entry_22.bandNumber = 1
entries.append(entry_22)

entry_23 = QgsRasterCalculatorEntry()
entry_23.ref = 'etp@11'
entry_23.raster = etp_11
entry_23.bandNumber = 1
entries.append(entry_23)

entry_24 = QgsRasterCalculatorEntry()
entry_24.ref = 'etp@12'
entry_24.raster = etp_12
entry_24.bandNumber = 1
entries.append(entry_24)


# Cálculo de la suma anual
calc_sum = QgsRasterCalculator(f'etp@1 + etp@2 + etp@3 + etp@4 + etp@5 + etp@6 + etp@7 + etp@8 + etp@9 + etp@10 + etp@11 + etp@12',
                               etp_suma_fn, 
                               'GTiff', 
                               p_01.extent(), 
                               p_01.width(), 
                               p_01.height(), 
                               entries)
calc_sum.processCalculation()



#
# Precipitación retenida (ret)
#


# Cálculos raster
calc_ret_01 = QgsRasterCalculator(f'(p@1 <= 5) * 5 + (p@1 > 5) * ( (p@1*{LLU_RET} > 5) * p@1*{LLU_RET} + (p@1*{LLU_RET} <= 5) * 5  )',
                                  ret_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_ret_01.processCalculation()

calc_ret_02 = QgsRasterCalculator(f'(p@2 <= 5) * 5 + (p@2 > 5) * ( (p@2*{LLU_RET} > 5) * p@2*{LLU_RET} + (p@2*{LLU_RET} <= 5) * 5  )',
                                  ret_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_ret_02.processCalculation()

calc_ret_03 = QgsRasterCalculator(f'(p@3 <= 5) * 5 + (p@3 > 5) * ( (p@3*{LLU_RET} > 5) * p@3*{LLU_RET} + (p@3*{LLU_RET} <= 5) * 5  )',
                                  ret_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_ret_03.processCalculation()

calc_ret_04 = QgsRasterCalculator(f'(p@4 <= 5) * 5 + (p@4 > 5) * ( (p@4*{LLU_RET} > 5) * p@4*{LLU_RET} + (p@4*{LLU_RET} <= 5) * 5  )',
                                  ret_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_ret_04.processCalculation()

calc_ret_05 = QgsRasterCalculator(f'(p@5 <= 5) * 5 + (p@5 > 5) * ( (p@5*{LLU_RET} > 5) * p@5*{LLU_RET} + (p@5*{LLU_RET} <= 5) * 5  )',
                                  ret_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_ret_05.processCalculation()

calc_ret_06 = QgsRasterCalculator(f'(p@6 <= 5) * 5 + (p@6 > 5) * ( (p@6*{LLU_RET} > 5) * p@6*{LLU_RET} + (p@6*{LLU_RET} <= 5) * 5  )',
                                  ret_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_ret_06.processCalculation()

calc_ret_07 = QgsRasterCalculator(f'(p@7 <= 5) * 5 + (p@7 > 5) * ( (p@7*{LLU_RET} > 5) * p@7*{LLU_RET} + (p@7*{LLU_RET} <= 5) * 5  )',
                                  ret_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_ret_07.processCalculation()

calc_ret_08 = QgsRasterCalculator(f'(p@8 <= 5) * 5 + (p@8 > 5) * ( (p@8*{LLU_RET} > 5) * p@8*{LLU_RET} + (p@8*{LLU_RET} <= 5) * 5  )',
                                  ret_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_ret_08.processCalculation()

calc_ret_09 = QgsRasterCalculator(f'(p@9 <= 5) * 5 + (p@9 > 5) * ( (p@9*{LLU_RET} > 5) * p@9*{LLU_RET} + (p@9*{LLU_RET} <= 5) * 5  )',
                                  ret_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_ret_09.processCalculation()

calc_ret_10 = QgsRasterCalculator(f'(p@10 <= 5) * 5 + (p@10 > 5) * ( (p@10*{LLU_RET} > 5) * p@10*{LLU_RET} + (p@10*{LLU_RET} <= 5) * 5  )',
                                  ret_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_ret_10.processCalculation()

calc_ret_11 = QgsRasterCalculator(f'(p@11 <= 5) * 5 + (p@11 > 5) * ( (p@11*{LLU_RET} > 5) * p@11*{LLU_RET} + (p@11*{LLU_RET} <= 5) * 5  )',
                                  ret_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_ret_11.processCalculation()

calc_ret_12 = QgsRasterCalculator(f'(p@12 <= 5) * 5 + (p@12 > 5) * ( (p@12*{LLU_RET} > 5) * p@12*{LLU_RET} + (p@12*{LLU_RET} <= 5) * 5  )',
                                  ret_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_ret_12.processCalculation()


# Capas
ret_01 = QgsRasterLayer(ret_01_fn)
ret_02 = QgsRasterLayer(ret_02_fn)
ret_03 = QgsRasterLayer(ret_03_fn)
ret_04 = QgsRasterLayer(ret_04_fn)
ret_05 = QgsRasterLayer(ret_05_fn)
ret_06 = QgsRasterLayer(ret_06_fn)
ret_07 = QgsRasterLayer(ret_07_fn)
ret_08 = QgsRasterLayer(ret_08_fn)
ret_09 = QgsRasterLayer(ret_09_fn)
ret_10 = QgsRasterLayer(ret_10_fn)
ret_11 = QgsRasterLayer(ret_11_fn)
ret_12 = QgsRasterLayer(ret_12_fn)


# Entradas para la calculadora raster
entry_25 = QgsRasterCalculatorEntry()
entry_25.ref = 'ret@1'
entry_25.raster = ret_01
entry_25.bandNumber = 1
entries.append(entry_25)

entry_26 = QgsRasterCalculatorEntry()
entry_26.ref = 'ret@2'
entry_26.raster = ret_02
entry_26.bandNumber = 1
entries.append(entry_26)

entry_27 = QgsRasterCalculatorEntry()
entry_27.ref = 'ret@3'
entry_27.raster = ret_03
entry_27.bandNumber = 1
entries.append(entry_27)

entry_28 = QgsRasterCalculatorEntry()
entry_28.ref = 'ret@4'
entry_28.raster = ret_04
entry_28.bandNumber = 1
entries.append(entry_28)

entry_29 = QgsRasterCalculatorEntry()
entry_29.ref = 'ret@5'
entry_29.raster = ret_05
entry_29.bandNumber = 1
entries.append(entry_29)

entry_30 = QgsRasterCalculatorEntry()
entry_30.ref = 'ret@6'
entry_30.raster = ret_06
entry_30.bandNumber = 1
entries.append(entry_30)

entry_31 = QgsRasterCalculatorEntry()
entry_31.ref = 'ret@7'
entry_31.raster = ret_07
entry_31.bandNumber = 1
entries.append(entry_31)

entry_32 = QgsRasterCalculatorEntry()
entry_32.ref = 'ret@8'
entry_32.raster = ret_08
entry_32.bandNumber = 1
entries.append(entry_32)

entry_33 = QgsRasterCalculatorEntry()
entry_33.ref = 'ret@9'
entry_33.raster = ret_09
entry_33.bandNumber = 1
entries.append(entry_33)

entry_34 = QgsRasterCalculatorEntry()
entry_34.ref = 'ret@10'
entry_34.raster = ret_10
entry_34.bandNumber = 1
entries.append(entry_34)

entry_35 = QgsRasterCalculatorEntry()
entry_35.ref = 'ret@11'
entry_35.raster = ret_11
entry_35.bandNumber = 1
entries.append(entry_35)

entry_36 = QgsRasterCalculatorEntry()
entry_36.ref = 'ret@12'
entry_36.raster = ret_12
entry_36.bandNumber = 1
entries.append(entry_36)


# Cálculo de la suma anual
calc_sum = QgsRasterCalculator(f'ret@1 + ret@2 + ret@3 + ret@4 + ret@5 + ret@6 + ret@7 + ret@8 + ret@9 + ret@10 + ret@11 + ret@12',
                               ret_suma_fn, 
                               'GTiff', 
                               p_01.extent(), 
                               p_01.width(), 
                               p_01.height(), 
                               entries)
calc_sum.processCalculation()



#
# Precipitación infiltrada (pi)
#

# Cálculos raster
calc_pi_01 = QgsRasterCalculator(f'(p@1 - ret@1) * {I}',
                                  pi_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_pi_01.processCalculation()

calc_pi_02 = QgsRasterCalculator(f'(p@2 - ret@2) * {I}',
                                  pi_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_pi_02.processCalculation()

calc_pi_03 = QgsRasterCalculator(f'(p@3 - ret@3) * {I}',
                                  pi_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_pi_03.processCalculation()

calc_pi_04 = QgsRasterCalculator(f'(p@4 - ret@4) * {I}',
                                  pi_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_pi_04.processCalculation()

calc_pi_05 = QgsRasterCalculator(f'(p@5 - ret@5) * {I}',
                                  pi_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_pi_05.processCalculation()

calc_pi_06 = QgsRasterCalculator(f'(p@6 - ret@6) * {I}',
                                  pi_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_pi_06.processCalculation()

calc_pi_07 = QgsRasterCalculator(f'(p@7 - ret@7) * {I}',
                                  pi_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_pi_07.processCalculation()

calc_pi_08 = QgsRasterCalculator(f'(p@8 - ret@8) * {I}',
                                  pi_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_pi_08.processCalculation()

calc_pi_09 = QgsRasterCalculator(f'(p@9 - ret@9) * {I}',
                                  pi_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_pi_09.processCalculation()

calc_pi_10 = QgsRasterCalculator(f'(p@10 - ret@10) * {I}',
                                  pi_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_pi_10.processCalculation()

calc_pi_11 = QgsRasterCalculator(f'(p@11 - ret@11) * {I}',
                                  pi_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_pi_11.processCalculation()

calc_pi_12 = QgsRasterCalculator(f'(p@12 - ret@12) * {I}',
                                  pi_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_pi_12.processCalculation()


# Capas
pi_01 = QgsRasterLayer(pi_01_fn)
pi_02 = QgsRasterLayer(pi_02_fn)
pi_03 = QgsRasterLayer(pi_03_fn)
pi_04 = QgsRasterLayer(pi_04_fn)
pi_05 = QgsRasterLayer(pi_05_fn)
pi_06 = QgsRasterLayer(pi_06_fn)
pi_07 = QgsRasterLayer(pi_07_fn)
pi_08 = QgsRasterLayer(pi_08_fn)
pi_09 = QgsRasterLayer(pi_09_fn)
pi_10 = QgsRasterLayer(pi_10_fn)
pi_11 = QgsRasterLayer(pi_11_fn)
pi_12 = QgsRasterLayer(pi_12_fn)


# Entradas para la calculadora raster
entry_37 = QgsRasterCalculatorEntry()
entry_37.ref = 'pi@1'
entry_37.raster = pi_01
entry_37.bandNumber = 1
entries.append(entry_37)

entry_38 = QgsRasterCalculatorEntry()
entry_38.ref = 'pi@2'
entry_38.raster = pi_02
entry_38.bandNumber = 1
entries.append(entry_38)

entry_39 = QgsRasterCalculatorEntry()
entry_39.ref = 'pi@3'
entry_39.raster = pi_03
entry_39.bandNumber = 1
entries.append(entry_39)

entry_40 = QgsRasterCalculatorEntry()
entry_40.ref = 'pi@4'
entry_40.raster = pi_04
entry_40.bandNumber = 1
entries.append(entry_40)

entry_41 = QgsRasterCalculatorEntry()
entry_41.ref = 'pi@5'
entry_41.raster = pi_05
entry_41.bandNumber = 1
entries.append(entry_41)

entry_42 = QgsRasterCalculatorEntry()
entry_42.ref = 'pi@6'
entry_42.raster = pi_06
entry_42.bandNumber = 1
entries.append(entry_42)

entry_43 = QgsRasterCalculatorEntry()
entry_43.ref = 'pi@7'
entry_43.raster = pi_07
entry_43.bandNumber = 1
entries.append(entry_43)

entry_44 = QgsRasterCalculatorEntry()
entry_44.ref = 'pi@8'
entry_44.raster = pi_08
entry_44.bandNumber = 1
entries.append(entry_44)

entry_45 = QgsRasterCalculatorEntry()
entry_45.ref = 'pi@9'
entry_45.raster = pi_09
entry_45.bandNumber = 1
entries.append(entry_45)

entry_46 = QgsRasterCalculatorEntry()
entry_46.ref = 'pi@10'
entry_46.raster = pi_10
entry_46.bandNumber = 1
entries.append(entry_46)

entry_47 = QgsRasterCalculatorEntry()
entry_47.ref = 'pi@11'
entry_47.raster = pi_11
entry_47.bandNumber = 1
entries.append(entry_47)

entry_48 = QgsRasterCalculatorEntry()
entry_48.ref = 'pi@12'
entry_48.raster = pi_12
entry_48.bandNumber = 1
entries.append(entry_48)


# Cálculo de la suma anual
calc_sum = QgsRasterCalculator('pi@1 + pi@2 + pi@3 + pi@4 + pi@5 + pi@6 + pi@7 + pi@8 + pi@9 + pi@10 + pi@11 + pi@12',
                               pi_suma_fn, 
                               'GTiff', 
                               p_01.extent(), 
                               p_01.width(), 
                               p_01.height(), 
                               entries)
calc_sum.processCalculation()



#
# Escorrentía superficial (esc)
#

# Cálculos raster
calc_esc_01 = QgsRasterCalculator('p@1 - ret@1 - pi@1',
                                  esc_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_esc_01.processCalculation()

calc_esc_02 = QgsRasterCalculator('p@2 - ret@2 - pi@2',
                                  esc_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_esc_02.processCalculation()

calc_esc_03 = QgsRasterCalculator('p@3 - ret@3 - pi@3',
                                  esc_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_esc_03.processCalculation()

calc_esc_04 = QgsRasterCalculator('p@4 - ret@4 - pi@4',
                                  esc_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_esc_04.processCalculation()

calc_esc_05 = QgsRasterCalculator('p@5 - ret@5 - pi@5',
                                  esc_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_esc_05.processCalculation()

calc_esc_06 = QgsRasterCalculator('p@6 - ret@6 - pi@6',
                                  esc_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_esc_06.processCalculation()

calc_esc_07 = QgsRasterCalculator('p@7 - ret@7 - pi@7',
                                  esc_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_esc_07.processCalculation()

calc_esc_08 = QgsRasterCalculator('p@8 - ret@8 - pi@8',
                                  esc_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_esc_08.processCalculation()

calc_esc_09 = QgsRasterCalculator('p@9 - ret@9 - pi@9',
                                  esc_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_esc_09.processCalculation()

calc_esc_10 = QgsRasterCalculator('p@10 - ret@10 - pi@10',
                                  esc_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_esc_10.processCalculation()

calc_esc_11 = QgsRasterCalculator('p@11 - ret@11 - pi@11',
                                  esc_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_esc_11.processCalculation()

calc_esc_12 = QgsRasterCalculator('p@12 - ret@12 - pi@12',
                                  esc_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_esc_12.processCalculation()


# Capas
esc_01 = QgsRasterLayer(esc_01_fn)
esc_02 = QgsRasterLayer(esc_02_fn)
esc_03 = QgsRasterLayer(esc_03_fn)
esc_04 = QgsRasterLayer(esc_04_fn)
esc_05 = QgsRasterLayer(esc_05_fn)
esc_06 = QgsRasterLayer(esc_06_fn)
esc_07 = QgsRasterLayer(esc_07_fn)
esc_08 = QgsRasterLayer(esc_08_fn)
esc_09 = QgsRasterLayer(esc_09_fn)
esc_10 = QgsRasterLayer(esc_10_fn)
esc_11 = QgsRasterLayer(esc_11_fn)
esc_12 = QgsRasterLayer(esc_12_fn)


# Entradas para la calculadora raster
entry_49 = QgsRasterCalculatorEntry()
entry_49.ref = 'esc@1'
entry_49.raster = esc_01
entry_49.bandNumber = 1
entries.append(entry_49)

entry_50 = QgsRasterCalculatorEntry()
entry_50.ref = 'esc@2'
entry_50.raster = esc_02
entry_50.bandNumber = 1
entries.append(entry_50)

entry_51 = QgsRasterCalculatorEntry()
entry_51.ref = 'esc@3'
entry_51.raster = esc_03
entry_51.bandNumber = 1
entries.append(entry_51)

entry_52 = QgsRasterCalculatorEntry()
entry_52.ref = 'esc@4'
entry_52.raster = esc_04
entry_52.bandNumber = 1
entries.append(entry_52)

entry_53 = QgsRasterCalculatorEntry()
entry_53.ref = 'esc@5'
entry_53.raster = esc_05
entry_53.bandNumber = 1
entries.append(entry_53)

entry_54 = QgsRasterCalculatorEntry()
entry_54.ref = 'esc@6'
entry_54.raster = esc_06
entry_54.bandNumber = 1
entries.append(entry_54)

entry_55 = QgsRasterCalculatorEntry()
entry_55.ref = 'esc@7'
entry_55.raster = esc_07
entry_55.bandNumber = 1
entries.append(entry_55)

entry_56 = QgsRasterCalculatorEntry()
entry_56.ref = 'esc@8'
entry_56.raster = esc_08
entry_56.bandNumber = 1
entries.append(entry_56)

entry_57 = QgsRasterCalculatorEntry()
entry_57.ref = 'esc@9'
entry_57.raster = esc_09
entry_57.bandNumber = 1
entries.append(entry_57)

entry_58 = QgsRasterCalculatorEntry()
entry_58.ref = 'esc@10'
entry_58.raster = esc_10
entry_58.bandNumber = 1
entries.append(entry_58)

entry_59 = QgsRasterCalculatorEntry()
entry_59.ref = 'esc@11'
entry_59.raster = esc_11
entry_59.bandNumber = 1
entries.append(entry_59)

entry_60 = QgsRasterCalculatorEntry()
entry_60.ref = 'esc@12'
entry_60.raster = esc_12
entry_60.bandNumber = 1
entries.append(entry_60)


# Cálculo de la suma anual
calc_sum = QgsRasterCalculator('esc@1 + esc@2 + esc@3 + esc@4 + esc@5 + esc@6 + esc@7 + esc@8 + esc@9 + esc@10 + esc@11 + esc@12',
                               esc_suma_fn, 
                               'GTiff', 
                               p_01.extent(), 
                               p_01.width(), 
                               p_01.height(), 
                               entries)
calc_sum.processCalculation()



#
# Mes inicial
#


# hsi
# Cálculos raster
calc_hsi_11 = QgsRasterCalculator(f'(p@11 * 0) + {HSI}',
                                  hsi_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_hsi_11.processCalculation()

# Capas
hsi_11 = QgsRasterLayer(hsi_11_fn)

# Entradas para la calculadora raster
entry_71 = QgsRasterCalculatorEntry()
entry_71.ref = 'hsi@11'
entry_71.raster = hsi_11
entry_71.bandNumber = 1
entries.append(entry_71)


# c1
# Cálculos raster
calc_c1_11 = QgsRasterCalculator(f'((hsi@11 - {PM_MM} + pi@11)/{CC_PM_MM} < 1) * (hsi@11 - {PM_MM} + pi@11)/{CC_PM_MM} + ((hsi@11 - {PM_MM} + pi@11)/{CC_PM_MM} >= 1) * 1',
                                  c1_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_c1_11.processCalculation()

# Capas
c1_11 = QgsRasterLayer(c1_11_fn)

# Entradas para la calculadora raster
entry_83 = QgsRasterCalculatorEntry()
entry_83.ref = 'c1@11'
entry_83.raster = c1_11
entry_83.bandNumber = 1
entries.append(entry_83)


# c2
# Cálculos raster
calc_c2_11 = QgsRasterCalculator(f'((hsi@11 - {PM_MM} + pi@11 - c1@11*etp@11)/{CC_PM_MM} > 1) * 1 + ((hsi@11 - {PM_MM} + pi@11 - c1@11*etp@11)/{CC_PM_MM} <= 1) * (  ((hsi@11 - {PM_MM} + pi@11 - c1@11*etp@11)/{CC_PM_MM} < 0) * 0 + ((hsi@11 - {PM_MM} + pi@11 - c1@11*etp@11)/{CC_PM_MM} >= 0) * (hsi@11 - {PM_MM} + pi@11 - c1@11*etp@11)/{CC_PM_MM}  )',
                                  c2_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_c2_11.processCalculation()

# Capas
c2_11 = QgsRasterLayer(c2_11_fn)

# Entradas para la calculadora raster
entry_95 = QgsRasterCalculatorEntry()
entry_95.ref = 'c2@11'
entry_95.raster = c2_11
entry_95.bandNumber = 1
entries.append(entry_95)


# hd
# Cálculos raster
calc_hd_11 = QgsRasterCalculator(f'hsi@11 - {PM_MM} + pi@11',
                                  hd_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_hd_11.processCalculation()

# Capas
hd_11 = QgsRasterLayer(hd_11_fn)

# Entradas para la calculadora raster
entry_107 = QgsRasterCalculatorEntry()
entry_107.ref = 'hd@11'
entry_107.raster = hd_11
entry_107.bandNumber = 1
entries.append(entry_107)


# etr
# Cálculos raster
calc_etr_11 = QgsRasterCalculator(f'(hd@11 >= (c1@11 + c2@11)/2*etp@11) * (c1@11 + c2@11)/2*etp@11 + (hd@11 < (c1@11 + c2@11)/2*etp@11) * hd@11',
                                  etr_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_etr_11.processCalculation()

# Capas
etr_11 = QgsRasterLayer(etr_11_fn)

# Entradas para la calculadora raster
entry_119 = QgsRasterCalculatorEntry()
entry_119.ref = 'etr@11'
entry_119.raster = etr_11
entry_119.bandNumber = 1
entries.append(entry_119)


# hsf
# Cálculos raster
calc_hsf_11 = QgsRasterCalculator(f'(hd@11 + {PM_MM} - etr@11 >= {CC_MM}) * {CC_MM} + (hd@11 + {PM_MM} - etr@11 < {CC_MM}) * (hd@11 + {PM_MM} - etr@11)',
                                  hsf_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_hsf_11.processCalculation()

# Capas
hsf_11 = QgsRasterLayer(hsf_11_fn)

# Entradas para la calculadora raster
entry_131 = QgsRasterCalculatorEntry()
entry_131.ref = 'hsf@11'
entry_131.raster = hsf_11
entry_131.bandNumber = 1
entries.append(entry_131)


# dcc
# Cálculos raster
calc_dcc_11 = QgsRasterCalculator(f'{CC_MM} - hsf@11',
                                  dcc_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_dcc_11.processCalculation()

# Capas
dcc_11 = QgsRasterLayer(dcc_11_fn)

# Entradas para la calculadora raster
entry_143 = QgsRasterCalculatorEntry()
entry_143.ref = 'dcc@11'
entry_143.raster = dcc_11
entry_143.bandNumber = 1
entries.append(entry_143)


# rp
# Cálculos raster
calc_rp_11 = QgsRasterCalculator(f'pi@11 + hsi@11 - hsf@11 - etr@11',
                                  rp_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_rp_11.processCalculation()

# Capas
rp_11 = QgsRasterLayer(rp_11_fn)

# Entradas para la calculadora raster
entry_155 = QgsRasterCalculatorEntry()
entry_155.ref = 'rp@11'
entry_155.raster = rp_11
entry_155.bandNumber = 1
entries.append(entry_155)


# nr
# Cálculos raster
calc_nr_11 = QgsRasterCalculator(f'dcc@11 - etr@11 + etp@11',
                                  nr_11_fn, 
                                  'GTiff', 
                                  p_11.extent(), 
                                  p_11.width(), 
                                  p_11.height(), 
                                  entries)
calc_nr_11.processCalculation()

# Capas
nr_11 = QgsRasterLayer(nr_11_fn)

# Entradas para la calculadora raster
entry_167 = QgsRasterCalculatorEntry()
entry_167.ref = 'nr@11'
entry_167.raster = nr_11
entry_167.bandNumber = 1
entries.append(entry_167)



#
# Meses posteriores al inicial
#


# hsi
# Cálculos raster
calc_hsi_12 = QgsRasterCalculator(f'hsf@11',
                                  hsi_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_hsi_12.processCalculation()

# Capas
hsi_12 = QgsRasterLayer(hsi_12_fn)

# Entradas para la calculadora raster
entry_72 = QgsRasterCalculatorEntry()
entry_72.ref = 'hsi@12'
entry_72.raster = hsi_12
entry_72.bandNumber = 1
entries.append(entry_72)


# c1
# Cálculos raster
calc_c1_12 = QgsRasterCalculator(f'((hsi@12 - {PM_MM} + pi@12)/{CC_PM_MM} < 1) * (hsi@12 - {PM_MM} + pi@12)/{CC_PM_MM} + ((hsi@12 - {PM_MM} + pi@12)/{CC_PM_MM} >= 1) * 1',
                                  c1_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_c1_12.processCalculation()

# Capas
c1_12 = QgsRasterLayer(c1_12_fn)

# Entradas para la calculadora raster
entry_84 = QgsRasterCalculatorEntry()
entry_84.ref = 'c1@12'
entry_84.raster = c1_12
entry_84.bandNumber = 1
entries.append(entry_84)


# c2
# Cálculos raster
calc_c2_12 = QgsRasterCalculator(f'((hsi@12 - {PM_MM} + pi@12 - c1@12*etp@12)/{CC_PM_MM} > 1) * 1 + ((hsi@12 - {PM_MM} + pi@12 - c1@12*etp@12)/{CC_PM_MM} <= 1) * (  ((hsi@12 - {PM_MM} + pi@12 - c1@12*etp@12)/{CC_PM_MM} < 0) * 0 + ((hsi@12 - {PM_MM} + pi@12 - c1@12*etp@12)/{CC_PM_MM} >= 0) * (hsi@12 - {PM_MM} + pi@12 - c1@12*etp@12)/{CC_PM_MM}  )',
                                  c2_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_c2_12.processCalculation()

# Capas
c2_12 = QgsRasterLayer(c2_12_fn)

# Entradas para la calculadora raster
entry_96 = QgsRasterCalculatorEntry()
entry_96.ref = 'c2@12'
entry_96.raster = c2_12
entry_96.bandNumber = 1
entries.append(entry_96)


# hd
# Cálculos raster
calc_hd_12 = QgsRasterCalculator(f'hsi@12 - {PM_MM} + pi@12',
                                  hd_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_hd_12.processCalculation()

# Capas
hd_12 = QgsRasterLayer(hd_12_fn)

# Entradas para la calculadora raster
entry_108 = QgsRasterCalculatorEntry()
entry_108.ref = 'hd@12'
entry_108.raster = hd_12
entry_108.bandNumber = 1
entries.append(entry_108)


# etr
# Cálculos raster
calc_etr_12 = QgsRasterCalculator(f'(hd@12 >= (c1@12 + c2@12)/2*etp@12) * (c1@12 + c2@12)/2*etp@12 + (hd@12 < (c1@12 + c2@12)/2*etp@12) * hd@12',
                                  etr_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_etr_12.processCalculation()

# Capas
etr_12 = QgsRasterLayer(etr_12_fn)

# Entradas para la calculadora raster
entry_120 = QgsRasterCalculatorEntry()
entry_120.ref = 'etr@12'
entry_120.raster = etr_12
entry_120.bandNumber = 1
entries.append(entry_120)


# hsf
# Cálculos raster
calc_hsf_12 = QgsRasterCalculator(f'(hd@12 + {PM_MM} - etr@12 >= {CC_MM}) * {CC_MM} + (hd@12 + {PM_MM} - etr@12 < {CC_MM}) * (hd@12 + {PM_MM} - etr@12)',
                                  hsf_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_hsf_12.processCalculation()

# Capas
hsf_12 = QgsRasterLayer(hsf_12_fn)

# Entradas para la calculadora raster
entry_132 = QgsRasterCalculatorEntry()
entry_132.ref = 'hsf@12'
entry_132.raster = hsf_12
entry_132.bandNumber = 1
entries.append(entry_132)


# dcc
# Cálculos raster
calc_dcc_12 = QgsRasterCalculator(f'{CC_MM} - hsf@12',
                                  dcc_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_dcc_12.processCalculation()

# Capas
dcc_12 = QgsRasterLayer(dcc_12_fn)

# Entradas para la calculadora raster
entry_144 = QgsRasterCalculatorEntry()
entry_144.ref = 'dcc@12'
entry_144.raster = dcc_12
entry_144.bandNumber = 1
entries.append(entry_144)


# rp
# Cálculos raster
calc_rp_12 = QgsRasterCalculator(f'pi@12 + hsi@12 - hsf@12 - etr@12',
                                  rp_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_rp_12.processCalculation()

# Capas
rp_12 = QgsRasterLayer(rp_12_fn)

# Entradas para la calculadora raster
entry_156 = QgsRasterCalculatorEntry()
entry_156.ref = 'rp@12'
entry_156.raster = rp_12
entry_156.bandNumber = 1
entries.append(entry_156)


# nr
# Cálculos raster
calc_nr_12 = QgsRasterCalculator(f'dcc@12 - etr@12 + etp@12',
                                  nr_12_fn, 
                                  'GTiff', 
                                  p_12.extent(), 
                                  p_12.width(), 
                                  p_12.height(), 
                                  entries)
calc_nr_12.processCalculation()

# Capas
nr_12 = QgsRasterLayer(nr_12_fn)

# Entradas para la calculadora raster
entry_168 = QgsRasterCalculatorEntry()
entry_168.ref = 'nr@12'
entry_168.raster = nr_12
entry_168.bandNumber = 1
entries.append(entry_168)



#
# Mes 1
#

# hsi
# Cálculos raster
calc_hsi_01 = QgsRasterCalculator(f'hsf@12',
                                  hsi_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_hsi_01.processCalculation()

# Capas
hsi_01 = QgsRasterLayer(hsi_01_fn)

# Entradas para la calculadora raster
entry_61 = QgsRasterCalculatorEntry()
entry_61.ref = 'hsi@1'
entry_61.raster = hsi_01
entry_61.bandNumber = 1
entries.append(entry_61)


# c1
# Cálculos raster
calc_c1_01 = QgsRasterCalculator(f'((hsi@1 - {PM_MM} + pi@1)/{CC_PM_MM} < 1) * (hsi@1 - {PM_MM} + pi@1)/{CC_PM_MM} + ((hsi@1 - {PM_MM} + pi@1)/{CC_PM_MM} >= 1) * 1',
                                  c1_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_c1_01.processCalculation()

# Capas
c1_01 = QgsRasterLayer(c1_01_fn)

# Entradas para la calculadora raster
entry_73 = QgsRasterCalculatorEntry()
entry_73.ref = 'c1@1'
entry_73.raster = c1_01
entry_73.bandNumber = 1
entries.append(entry_73)


# c2
# Cálculos raster
calc_c2_01 = QgsRasterCalculator(f'((hsi@1 - {PM_MM} + pi@1 - c1@1*etp@1)/{CC_PM_MM} > 1) * 1 + ((hsi@1 - {PM_MM} + pi@1 - c1@1*etp@1)/{CC_PM_MM} <= 1) * (  ((hsi@1 - {PM_MM} + pi@1 - c1@1*etp@1)/{CC_PM_MM} < 0) * 0 + ((hsi@1 - {PM_MM} + pi@1 - c1@1*etp@1)/{CC_PM_MM} >= 0) * (hsi@1 - {PM_MM} + pi@1 - c1@1*etp@1)/{CC_PM_MM}  )',
                                  c2_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_c2_01.processCalculation()

# Capas
c2_01 = QgsRasterLayer(c2_01_fn)

# Entradas para la calculadora raster
entry_85 = QgsRasterCalculatorEntry()
entry_85.ref = 'c2@1'
entry_85.raster = c2_01
entry_85.bandNumber = 1
entries.append(entry_85)


# hd
# Cálculos raster
calc_hd_01 = QgsRasterCalculator(f'hsi@1 - {PM_MM} + pi@1',
                                  hd_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_hd_01.processCalculation()

# Capas
hd_01 = QgsRasterLayer(hd_01_fn)

# Entradas para la calculadora raster
entry_97 = QgsRasterCalculatorEntry()
entry_97.ref = 'hd@1'
entry_97.raster = hd_01
entry_97.bandNumber = 1
entries.append(entry_97)


# etr
# Cálculos raster
calc_etr_01 = QgsRasterCalculator(f'(hd@1 >= (c1@1 + c2@1)/2*etp@1) * (c1@1 + c2@1)/2*etp@1 + (hd@1 < (c1@1 + c2@1)/2*etp@1) * hd@1',
                                  etr_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_etr_01.processCalculation()

# Capas
etr_01 = QgsRasterLayer(etr_01_fn)

# Entradas para la calculadora raster
entry_109 = QgsRasterCalculatorEntry()
entry_109.ref = 'etr@1'
entry_109.raster = etr_01
entry_109.bandNumber = 1
entries.append(entry_109)


# hsf
# Cálculos raster
calc_hsf_01 = QgsRasterCalculator(f'(hd@1 + {PM_MM} - etr@1 >= {CC_MM}) * {CC_MM} + (hd@1 + {PM_MM} - etr@1 < {CC_MM}) * (hd@1 + {PM_MM} - etr@1)',
                                  hsf_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_hsf_01.processCalculation()

# Capas
hsf_01 = QgsRasterLayer(hsf_01_fn)

# Entradas para la calculadora raster
entry_121 = QgsRasterCalculatorEntry()
entry_121.ref = 'hsf@1'
entry_121.raster = hsf_01
entry_121.bandNumber = 1
entries.append(entry_121)


# dcc
# Cálculos raster
calc_dcc_01 = QgsRasterCalculator(f'{CC_MM} - hsf@1',
                                  dcc_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_dcc_01.processCalculation()

# Capas
dcc_01 = QgsRasterLayer(dcc_01_fn)

# Entradas para la calculadora raster
entry_133 = QgsRasterCalculatorEntry()
entry_133.ref = 'dcc@1'
entry_133.raster = dcc_01
entry_133.bandNumber = 1
entries.append(entry_133)


# rp
# Cálculos raster
calc_rp_01 = QgsRasterCalculator(f'pi@1 + hsi@1 - hsf@1 - etr@1',
                                  rp_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_rp_01.processCalculation()

# Capas
rp_01 = QgsRasterLayer(rp_01_fn)

# Entradas para la calculadora raster
entry_145 = QgsRasterCalculatorEntry()
entry_145.ref = 'rp@1'
entry_145.raster = rp_01
entry_145.bandNumber = 1
entries.append(entry_145)


# nr
# Cálculos raster
calc_nr_01 = QgsRasterCalculator(f'dcc@1 - etr@1 + etp@1',
                                  nr_01_fn, 
                                  'GTiff', 
                                  p_01.extent(), 
                                  p_01.width(), 
                                  p_01.height(), 
                                  entries)
calc_nr_01.processCalculation()

# Capas
nr_01 = QgsRasterLayer(nr_01_fn)

# Entradas para la calculadora raster
entry_157 = QgsRasterCalculatorEntry()
entry_157.ref = 'nr@1'
entry_157.raster = nr_01
entry_157.bandNumber = 1
entries.append(entry_157)



#
# Mes 2
#

# hsi
# Cálculos raster
calc_hsi_02 = QgsRasterCalculator(f'hsf@1',
                                  hsi_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_hsi_02.processCalculation()

# Capas
hsi_02 = QgsRasterLayer(hsi_02_fn)

# Entradas para la calculadora raster
entry_62 = QgsRasterCalculatorEntry()
entry_62.ref = 'hsi@2'
entry_62.raster = hsi_02
entry_62.bandNumber = 1
entries.append(entry_62)


# c1
# Cálculos raster
calc_c1_02 = QgsRasterCalculator(f'((hsi@2 - {PM_MM} + pi@2)/{CC_PM_MM} < 1) * (hsi@2 - {PM_MM} + pi@2)/{CC_PM_MM} + ((hsi@2 - {PM_MM} + pi@2)/{CC_PM_MM} >= 1) * 1',
                                  c1_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_c1_02.processCalculation()

# Capas
c1_02 = QgsRasterLayer(c1_02_fn)

# Entradas para la calculadora raster
entry_74 = QgsRasterCalculatorEntry()
entry_74.ref = 'c1@2'
entry_74.raster = c1_02
entry_74.bandNumber = 1
entries.append(entry_74)


# c2
# Cálculos raster
calc_c2_02 = QgsRasterCalculator(f'((hsi@2 - {PM_MM} + pi@2 - c1@2*etp@2)/{CC_PM_MM} > 1) * 1 + ((hsi@2 - {PM_MM} + pi@2 - c1@2*etp@2)/{CC_PM_MM} <= 1) * (  ((hsi@2 - {PM_MM} + pi@2 - c1@2*etp@2)/{CC_PM_MM} < 0) * 0 + ((hsi@2 - {PM_MM} + pi@2 - c1@2*etp@2)/{CC_PM_MM} >= 0) * (hsi@2 - {PM_MM} + pi@2 - c1@2*etp@2)/{CC_PM_MM}  )',
                                  c2_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_c2_02.processCalculation()

# Capas
c2_02 = QgsRasterLayer(c2_02_fn)

# Entradas para la calculadora raster
entry_86 = QgsRasterCalculatorEntry()
entry_86.ref = 'c2@2'
entry_86.raster = c2_02
entry_86.bandNumber = 1
entries.append(entry_86)


# hd
# Cálculos raster
calc_hd_02 = QgsRasterCalculator(f'hsi@2 - {PM_MM} + pi@2',
                                  hd_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_hd_02.processCalculation()

# Capas
hd_02 = QgsRasterLayer(hd_02_fn)

# Entradas para la calculadora raster
entry_98 = QgsRasterCalculatorEntry()
entry_98.ref = 'hd@2'
entry_98.raster = hd_02
entry_98.bandNumber = 1
entries.append(entry_98)


# etr
# Cálculos raster
calc_etr_02 = QgsRasterCalculator(f'(hd@2 >= (c1@2 + c2@2)/2*etp@2) * (c1@2 + c2@2)/2*etp@2 + (hd@2 < (c1@2 + c2@2)/2*etp@2) * hd@2',
                                  etr_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_etr_02.processCalculation()

# Capas
etr_02 = QgsRasterLayer(etr_02_fn)

# Entradas para la calculadora raster
entry_110 = QgsRasterCalculatorEntry()
entry_110.ref = 'etr@2'
entry_110.raster = etr_02
entry_110.bandNumber = 1
entries.append(entry_110)


# hsf
# Cálculos raster
calc_hsf_02 = QgsRasterCalculator(f'(hd@2 + {PM_MM} - etr@2 >= {CC_MM}) * {CC_MM} + (hd@2 + {PM_MM} - etr@2 < {CC_MM}) * (hd@2 + {PM_MM} - etr@2)',
                                  hsf_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_hsf_02.processCalculation()

# Capas
hsf_02 = QgsRasterLayer(hsf_02_fn)

# Entradas para la calculadora raster
entry_122 = QgsRasterCalculatorEntry()
entry_122.ref = 'hsf@2'
entry_122.raster = hsf_02
entry_122.bandNumber = 1
entries.append(entry_122)


# dcc
# Cálculos raster
calc_dcc_02 = QgsRasterCalculator(f'{CC_MM} - hsf@2',
                                  dcc_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_dcc_02.processCalculation()

# Capas
dcc_02 = QgsRasterLayer(dcc_02_fn)

# Entradas para la calculadora raster
entry_134 = QgsRasterCalculatorEntry()
entry_134.ref = 'dcc@2'
entry_134.raster = dcc_02
entry_134.bandNumber = 1
entries.append(entry_134)


# rp
# Cálculos raster
calc_rp_02 = QgsRasterCalculator(f'pi@2 + hsi@2 - hsf@2 - etr@2',
                                  rp_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_rp_02.processCalculation()

# Capas
rp_02 = QgsRasterLayer(rp_02_fn)

# Entradas para la calculadora raster
entry_146 = QgsRasterCalculatorEntry()
entry_146.ref = 'rp@2'
entry_146.raster = rp_02
entry_146.bandNumber = 1
entries.append(entry_146)


# nr
# Cálculos raster
calc_nr_02 = QgsRasterCalculator(f'dcc@2 - etr@2 + etp@2',
                                  nr_02_fn, 
                                  'GTiff', 
                                  p_02.extent(), 
                                  p_02.width(), 
                                  p_02.height(), 
                                  entries)
calc_nr_02.processCalculation()

# Capas
nr_02 = QgsRasterLayer(nr_02_fn)

# Entradas para la calculadora raster
entry_158 = QgsRasterCalculatorEntry()
entry_158.ref = 'nr@2'
entry_158.raster = nr_02
entry_158.bandNumber = 1
entries.append(entry_158)



#
# Mes 3
#

# hsi
# Cálculos raster
calc_hsi_03 = QgsRasterCalculator(f'hsf@2',
                                  hsi_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_hsi_03.processCalculation()

# Capas
hsi_03 = QgsRasterLayer(hsi_03_fn)

# Entradas para la calculadora raster
entry_63 = QgsRasterCalculatorEntry()
entry_63.ref = 'hsi@3'
entry_63.raster = hsi_03
entry_63.bandNumber = 1
entries.append(entry_63)


# c1
# Cálculos raster
calc_c1_03 = QgsRasterCalculator(f'((hsi@3 - {PM_MM} + pi@3)/{CC_PM_MM} < 1) * (hsi@3 - {PM_MM} + pi@3)/{CC_PM_MM} + ((hsi@3 - {PM_MM} + pi@3)/{CC_PM_MM} >= 1) * 1',
                                  c1_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_c1_03.processCalculation()

# Capas
c1_03 = QgsRasterLayer(c1_03_fn)

# Entradas para la calculadora raster
entry_75 = QgsRasterCalculatorEntry()
entry_75.ref = 'c1@3'
entry_75.raster = c1_03
entry_75.bandNumber = 1
entries.append(entry_75)


# c2
# Cálculos raster
calc_c2_03 = QgsRasterCalculator(f'((hsi@3 - {PM_MM} + pi@3 - c1@3*etp@3)/{CC_PM_MM} > 1) * 1 + ((hsi@3 - {PM_MM} + pi@3 - c1@3*etp@3)/{CC_PM_MM} <= 1) * (  ((hsi@3 - {PM_MM} + pi@3 - c1@3*etp@3)/{CC_PM_MM} < 0) * 0 + ((hsi@3 - {PM_MM} + pi@3 - c1@3*etp@3)/{CC_PM_MM} >= 0) * (hsi@3 - {PM_MM} + pi@3 - c1@3*etp@3)/{CC_PM_MM}  )',
                                  c2_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_c2_03.processCalculation()

# Capas
c2_03 = QgsRasterLayer(c2_03_fn)

# Entradas para la calculadora raster
entry_87 = QgsRasterCalculatorEntry()
entry_87.ref = 'c2@3'
entry_87.raster = c2_03
entry_87.bandNumber = 1
entries.append(entry_87)


# hd
# Cálculos raster
calc_hd_03 = QgsRasterCalculator(f'hsi@3 - {PM_MM} + pi@3',
                                  hd_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_hd_03.processCalculation()

# Capas
hd_03 = QgsRasterLayer(hd_03_fn)

# Entradas para la calculadora raster
entry_99 = QgsRasterCalculatorEntry()
entry_99.ref = 'hd@3'
entry_99.raster = hd_03
entry_99.bandNumber = 1
entries.append(entry_99)


# etr
# Cálculos raster
calc_etr_03 = QgsRasterCalculator(f'(hd@3 >= (c1@3 + c2@3)/2*etp@3) * (c1@3 + c2@3)/2*etp@3 + (hd@3 < (c1@3 + c2@3)/2*etp@3) * hd@3',
                                  etr_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_etr_03.processCalculation()

# Capas
etr_03 = QgsRasterLayer(etr_03_fn)

# Entradas para la calculadora raster
entry_111 = QgsRasterCalculatorEntry()
entry_111.ref = 'etr@3'
entry_111.raster = etr_03
entry_111.bandNumber = 1
entries.append(entry_111)


# hsf
# Cálculos raster
calc_hsf_03 = QgsRasterCalculator(f'(hd@3 + {PM_MM} - etr@3 >= {CC_MM}) * {CC_MM} + (hd@3 + {PM_MM} - etr@3 < {CC_MM}) * (hd@3 + {PM_MM} - etr@3)',
                                  hsf_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_hsf_03.processCalculation()

# Capas
hsf_03 = QgsRasterLayer(hsf_03_fn)

# Entradas para la calculadora raster
entry_123 = QgsRasterCalculatorEntry()
entry_123.ref = 'hsf@3'
entry_123.raster = hsf_03
entry_123.bandNumber = 1
entries.append(entry_123)


# dcc
# Cálculos raster
calc_dcc_03 = QgsRasterCalculator(f'{CC_MM} - hsf@3',
                                  dcc_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_dcc_03.processCalculation()

# Capas
dcc_03 = QgsRasterLayer(dcc_03_fn)

# Entradas para la calculadora raster
entry_135 = QgsRasterCalculatorEntry()
entry_135.ref = 'dcc@3'
entry_135.raster = dcc_03
entry_135.bandNumber = 1
entries.append(entry_135)


# rp
# Cálculos raster
calc_rp_03 = QgsRasterCalculator(f'pi@3 + hsi@3 - hsf@3 - etr@3',
                                  rp_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_rp_03.processCalculation()

# Capas
rp_03 = QgsRasterLayer(rp_03_fn)

# Entradas para la calculadora raster
entry_147 = QgsRasterCalculatorEntry()
entry_147.ref = 'rp@3'
entry_147.raster = rp_03
entry_147.bandNumber = 1
entries.append(entry_147)


# nr
# Cálculos raster
calc_nr_03 = QgsRasterCalculator(f'dcc@3 - etr@3 + etp@3',
                                  nr_03_fn, 
                                  'GTiff', 
                                  p_03.extent(), 
                                  p_03.width(), 
                                  p_03.height(), 
                                  entries)
calc_nr_03.processCalculation()

# Capas
nr_03 = QgsRasterLayer(nr_03_fn)

# Entradas para la calculadora raster
entry_159 = QgsRasterCalculatorEntry()
entry_159.ref = 'nr@3'
entry_159.raster = nr_03
entry_159.bandNumber = 1
entries.append(entry_159)



#
# Mes 4
#

# hsi
# Cálculos raster
calc_hsi_04 = QgsRasterCalculator(f'hsf@3',
                                  hsi_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_hsi_04.processCalculation()

# Capas
hsi_04 = QgsRasterLayer(hsi_04_fn)

# Entradas para la calculadora raster
entry_64 = QgsRasterCalculatorEntry()
entry_64.ref = 'hsi@4'
entry_64.raster = hsi_04
entry_64.bandNumber = 1
entries.append(entry_64)


# c1
# Cálculos raster
calc_c1_04 = QgsRasterCalculator(f'((hsi@4 - {PM_MM} + pi@4)/{CC_PM_MM} < 1) * (hsi@4 - {PM_MM} + pi@4)/{CC_PM_MM} + ((hsi@4 - {PM_MM} + pi@4)/{CC_PM_MM} >= 1) * 1',
                                  c1_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_c1_04.processCalculation()

# Capas
c1_04 = QgsRasterLayer(c1_04_fn)

# Entradas para la calculadora raster
entry_76 = QgsRasterCalculatorEntry()
entry_76.ref = 'c1@4'
entry_76.raster = c1_04
entry_76.bandNumber = 1
entries.append(entry_76)


# c2
# Cálculos raster
calc_c2_04 = QgsRasterCalculator(f'((hsi@4 - {PM_MM} + pi@4 - c1@4*etp@4)/{CC_PM_MM} > 1) * 1 + ((hsi@4 - {PM_MM} + pi@4 - c1@4*etp@4)/{CC_PM_MM} <= 1) * (  ((hsi@4 - {PM_MM} + pi@4 - c1@4*etp@4)/{CC_PM_MM} < 0) * 0 + ((hsi@4 - {PM_MM} + pi@4 - c1@4*etp@4)/{CC_PM_MM} >= 0) * (hsi@4 - {PM_MM} + pi@4 - c1@4*etp@4)/{CC_PM_MM}  )',
                                  c2_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_c2_04.processCalculation()

# Capas
c2_04 = QgsRasterLayer(c2_04_fn)

# Entradas para la calculadora raster
entry_88 = QgsRasterCalculatorEntry()
entry_88.ref = 'c2@4'
entry_88.raster = c2_04
entry_88.bandNumber = 1
entries.append(entry_88)


# hd
# Cálculos raster
calc_hd_04 = QgsRasterCalculator(f'hsi@4 - {PM_MM} + pi@4',
                                  hd_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_hd_04.processCalculation()

# Capas
hd_04 = QgsRasterLayer(hd_04_fn)

# Entradas para la calculadora raster
entry_100 = QgsRasterCalculatorEntry()
entry_100.ref = 'hd@4'
entry_100.raster = hd_04
entry_100.bandNumber = 1
entries.append(entry_100)


# etr
# Cálculos raster
calc_etr_04 = QgsRasterCalculator(f'(hd@4 >= (c1@4 + c2@4)/2*etp@4) * (c1@4 + c2@4)/2*etp@4 + (hd@4 < (c1@4 + c2@4)/2*etp@4) * hd@4',
                                  etr_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_etr_04.processCalculation()

# Capas
etr_04 = QgsRasterLayer(etr_04_fn)

# Entradas para la calculadora raster
entry_112 = QgsRasterCalculatorEntry()
entry_112.ref = 'etr@4'
entry_112.raster = etr_04
entry_112.bandNumber = 1
entries.append(entry_112)


# hsf
# Cálculos raster
calc_hsf_04 = QgsRasterCalculator(f'(hd@4 + {PM_MM} - etr@4 >= {CC_MM}) * {CC_MM} + (hd@4 + {PM_MM} - etr@4 < {CC_MM}) * (hd@4 + {PM_MM} - etr@4)',
                                  hsf_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_hsf_04.processCalculation()

# Capas
hsf_04 = QgsRasterLayer(hsf_04_fn)

# Entradas para la calculadora raster
entry_124 = QgsRasterCalculatorEntry()
entry_124.ref = 'hsf@4'
entry_124.raster = hsf_04
entry_124.bandNumber = 1
entries.append(entry_124)


# dcc
# Cálculos raster
calc_dcc_04 = QgsRasterCalculator(f'{CC_MM} - hsf@4',
                                  dcc_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_dcc_04.processCalculation()

# Capas
dcc_04 = QgsRasterLayer(dcc_04_fn)

# Entradas para la calculadora raster
entry_136 = QgsRasterCalculatorEntry()
entry_136.ref = 'dcc@4'
entry_136.raster = dcc_04
entry_136.bandNumber = 1
entries.append(entry_136)


# rp
# Cálculos raster
calc_rp_04 = QgsRasterCalculator(f'pi@4 + hsi@4 - hsf@4 - etr@4',
                                  rp_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_rp_04.processCalculation()

# Capas
rp_04 = QgsRasterLayer(rp_04_fn)

# Entradas para la calculadora raster
entry_148 = QgsRasterCalculatorEntry()
entry_148.ref = 'rp@4'
entry_148.raster = rp_04
entry_148.bandNumber = 1
entries.append(entry_148)


# nr
# Cálculos raster
calc_nr_04 = QgsRasterCalculator(f'dcc@4 - etr@4 + etp@4',
                                  nr_04_fn, 
                                  'GTiff', 
                                  p_04.extent(), 
                                  p_04.width(), 
                                  p_04.height(), 
                                  entries)
calc_nr_04.processCalculation()

# Capas
nr_04 = QgsRasterLayer(nr_04_fn)

# Entradas para la calculadora raster
entry_160 = QgsRasterCalculatorEntry()
entry_160.ref = 'nr@4'
entry_160.raster = nr_04
entry_160.bandNumber = 1
entries.append(entry_160)



#
# Mes 5
#

# hsi
# Cálculos raster
calc_hsi_05 = QgsRasterCalculator(f'hsf@4',
                                  hsi_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_hsi_05.processCalculation()

# Capas
hsi_05 = QgsRasterLayer(hsi_05_fn)

# Entradas para la calculadora raster
entry_65 = QgsRasterCalculatorEntry()
entry_65.ref = 'hsi@5'
entry_65.raster = hsi_05
entry_65.bandNumber = 1
entries.append(entry_65)


# c1
# Cálculos raster
calc_c1_05 = QgsRasterCalculator(f'((hsi@5 - {PM_MM} + pi@5)/{CC_PM_MM} < 1) * (hsi@5 - {PM_MM} + pi@5)/{CC_PM_MM} + ((hsi@5 - {PM_MM} + pi@5)/{CC_PM_MM} >= 1) * 1',
                                  c1_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_c1_05.processCalculation()

# Capas
c1_05 = QgsRasterLayer(c1_05_fn)

# Entradas para la calculadora raster
entry_77 = QgsRasterCalculatorEntry()
entry_77.ref = 'c1@5'
entry_77.raster = c1_05
entry_77.bandNumber = 1
entries.append(entry_77)


# c2
# Cálculos raster
calc_c2_05 = QgsRasterCalculator(f'((hsi@5 - {PM_MM} + pi@5 - c1@5*etp@5)/{CC_PM_MM} > 1) * 1 + ((hsi@5 - {PM_MM} + pi@5 - c1@5*etp@5)/{CC_PM_MM} <= 1) * (  ((hsi@5 - {PM_MM} + pi@5 - c1@5*etp@5)/{CC_PM_MM} < 0) * 0 + ((hsi@5 - {PM_MM} + pi@5 - c1@5*etp@5)/{CC_PM_MM} >= 0) * (hsi@5 - {PM_MM} + pi@5 - c1@5*etp@5)/{CC_PM_MM}  )',
                                  c2_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_c2_05.processCalculation()

# Capas
c2_05 = QgsRasterLayer(c2_05_fn)

# Entradas para la calculadora raster
entry_89 = QgsRasterCalculatorEntry()
entry_89.ref = 'c2@5'
entry_89.raster = c2_05
entry_89.bandNumber = 1
entries.append(entry_89)


# hd
# Cálculos raster
calc_hd_05 = QgsRasterCalculator(f'hsi@5 - {PM_MM} + pi@5',
                                  hd_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_hd_05.processCalculation()

# Capas
hd_05 = QgsRasterLayer(hd_05_fn)

# Entradas para la calculadora raster
entry_101 = QgsRasterCalculatorEntry()
entry_101.ref = 'hd@5'
entry_101.raster = hd_05
entry_101.bandNumber = 1
entries.append(entry_101)


# etr
# Cálculos raster
calc_etr_05 = QgsRasterCalculator(f'(hd@5 >= (c1@5 + c2@5)/2*etp@5) * (c1@5 + c2@5)/2*etp@5 + (hd@5 < (c1@5 + c2@5)/2*etp@5) * hd@5',
                                  etr_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_etr_05.processCalculation()

# Capas
etr_05 = QgsRasterLayer(etr_05_fn)

# Entradas para la calculadora raster
entry_113 = QgsRasterCalculatorEntry()
entry_113.ref = 'etr@5'
entry_113.raster = etr_05
entry_113.bandNumber = 1
entries.append(entry_113)


# hsf
# Cálculos raster
calc_hsf_05 = QgsRasterCalculator(f'(hd@5 + {PM_MM} - etr@5 >= {CC_MM}) * {CC_MM} + (hd@5 + {PM_MM} - etr@5 < {CC_MM}) * (hd@5 + {PM_MM} - etr@5)',
                                  hsf_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_hsf_05.processCalculation()

# Capas
hsf_05 = QgsRasterLayer(hsf_05_fn)

# Entradas para la calculadora raster
entry_125 = QgsRasterCalculatorEntry()
entry_125.ref = 'hsf@5'
entry_125.raster = hsf_05
entry_125.bandNumber = 1
entries.append(entry_125)


# dcc
# Cálculos raster
calc_dcc_05 = QgsRasterCalculator(f'{CC_MM} - hsf@5',
                                  dcc_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_dcc_05.processCalculation()

# Capas
dcc_05 = QgsRasterLayer(dcc_05_fn)

# Entradas para la calculadora raster
entry_137 = QgsRasterCalculatorEntry()
entry_137.ref = 'dcc@5'
entry_137.raster = dcc_05
entry_137.bandNumber = 1
entries.append(entry_137)


# rp
# Cálculos raster
calc_rp_05 = QgsRasterCalculator(f'pi@5 + hsi@5 - hsf@5 - etr@5',
                                  rp_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_rp_05.processCalculation()

# Capas
rp_05 = QgsRasterLayer(rp_05_fn)

# Entradas para la calculadora raster
entry_149 = QgsRasterCalculatorEntry()
entry_149.ref = 'rp@5'
entry_149.raster = rp_05
entry_149.bandNumber = 1
entries.append(entry_149)


# nr
# Cálculos raster
calc_nr_05 = QgsRasterCalculator(f'dcc@5 - etr@5 + etp@5',
                                  nr_05_fn, 
                                  'GTiff', 
                                  p_05.extent(), 
                                  p_05.width(), 
                                  p_05.height(), 
                                  entries)
calc_nr_05.processCalculation()

# Capas
nr_05 = QgsRasterLayer(nr_05_fn)

# Entradas para la calculadora raster
entry_161 = QgsRasterCalculatorEntry()
entry_161.ref = 'nr@5'
entry_161.raster = nr_05
entry_161.bandNumber = 1
entries.append(entry_161)



#
# Mes 6
#

# hsi
# Cálculos raster
calc_hsi_06 = QgsRasterCalculator(f'hsf@5',
                                  hsi_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_hsi_06.processCalculation()

# Capas
hsi_06 = QgsRasterLayer(hsi_06_fn)

# Entradas para la calculadora raster
entry_66 = QgsRasterCalculatorEntry()
entry_66.ref = 'hsi@6'
entry_66.raster = hsi_06
entry_66.bandNumber = 1
entries.append(entry_66)


# c1
# Cálculos raster
calc_c1_06 = QgsRasterCalculator(f'((hsi@6 - {PM_MM} + pi@6)/{CC_PM_MM} < 1) * (hsi@6 - {PM_MM} + pi@6)/{CC_PM_MM} + ((hsi@6 - {PM_MM} + pi@6)/{CC_PM_MM} >= 1) * 1',
                                  c1_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_c1_06.processCalculation()

# Capas
c1_06 = QgsRasterLayer(c1_06_fn)

# Entradas para la calculadora raster
entry_78 = QgsRasterCalculatorEntry()
entry_78.ref = 'c1@6'
entry_78.raster = c1_06
entry_78.bandNumber = 1
entries.append(entry_78)


# c2
# Cálculos raster
calc_c2_06 = QgsRasterCalculator(f'((hsi@6 - {PM_MM} + pi@6 - c1@6*etp@6)/{CC_PM_MM} > 1) * 1 + ((hsi@6 - {PM_MM} + pi@6 - c1@6*etp@6)/{CC_PM_MM} <= 1) * (  ((hsi@6 - {PM_MM} + pi@6 - c1@6*etp@6)/{CC_PM_MM} < 0) * 0 + ((hsi@6 - {PM_MM} + pi@6 - c1@6*etp@6)/{CC_PM_MM} >= 0) * (hsi@6 - {PM_MM} + pi@6 - c1@6*etp@6)/{CC_PM_MM}  )',
                                  c2_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_c2_06.processCalculation()

# Capas
c2_06 = QgsRasterLayer(c2_06_fn)

# Entradas para la calculadora raster
entry_90 = QgsRasterCalculatorEntry()
entry_90.ref = 'c2@6'
entry_90.raster = c2_06
entry_90.bandNumber = 1
entries.append(entry_90)


# hd
# Cálculos raster
calc_hd_06 = QgsRasterCalculator(f'hsi@6 - {PM_MM} + pi@6',
                                  hd_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_hd_06.processCalculation()

# Capas
hd_06 = QgsRasterLayer(hd_06_fn)

# Entradas para la calculadora raster
entry_102 = QgsRasterCalculatorEntry()
entry_102.ref = 'hd@6'
entry_102.raster = hd_06
entry_102.bandNumber = 1
entries.append(entry_102)


# etr
# Cálculos raster
calc_etr_06 = QgsRasterCalculator(f'(hd@6 >= (c1@6 + c2@6)/2*etp@6) * (c1@6 + c2@6)/2*etp@6 + (hd@6 < (c1@6 + c2@6)/2*etp@6) * hd@6',
                                  etr_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_etr_06.processCalculation()

# Capas
etr_06 = QgsRasterLayer(etr_06_fn)

# Entradas para la calculadora raster
entry_114 = QgsRasterCalculatorEntry()
entry_114.ref = 'etr@6'
entry_114.raster = etr_06
entry_114.bandNumber = 1
entries.append(entry_114)


# hsf
# Cálculos raster
calc_hsf_06 = QgsRasterCalculator(f'(hd@6 + {PM_MM} - etr@6 >= {CC_MM}) * {CC_MM} + (hd@6 + {PM_MM} - etr@6 < {CC_MM}) * (hd@6 + {PM_MM} - etr@6)',
                                  hsf_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_hsf_06.processCalculation()

# Capas
hsf_06 = QgsRasterLayer(hsf_06_fn)

# Entradas para la calculadora raster
entry_126 = QgsRasterCalculatorEntry()
entry_126.ref = 'hsf@6'
entry_126.raster = hsf_06
entry_126.bandNumber = 1
entries.append(entry_126)


# dcc
# Cálculos raster
calc_dcc_06 = QgsRasterCalculator(f'{CC_MM} - hsf@6',
                                  dcc_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_dcc_06.processCalculation()

# Capas
dcc_06 = QgsRasterLayer(dcc_06_fn)

# Entradas para la calculadora raster
entry_138 = QgsRasterCalculatorEntry()
entry_138.ref = 'dcc@6'
entry_138.raster = dcc_06
entry_138.bandNumber = 1
entries.append(entry_138)


# rp
# Cálculos raster
calc_rp_06 = QgsRasterCalculator(f'pi@6 + hsi@6 - hsf@6 - etr@6',
                                  rp_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_rp_06.processCalculation()

# Capas
rp_06 = QgsRasterLayer(rp_06_fn)

# Entradas para la calculadora raster
entry_150 = QgsRasterCalculatorEntry()
entry_150.ref = 'rp@6'
entry_150.raster = rp_06
entry_150.bandNumber = 1
entries.append(entry_150)


# nr
# Cálculos raster
calc_nr_06 = QgsRasterCalculator(f'dcc@6 - etr@6 + etp@6',
                                  nr_06_fn, 
                                  'GTiff', 
                                  p_06.extent(), 
                                  p_06.width(), 
                                  p_06.height(), 
                                  entries)
calc_nr_06.processCalculation()

# Capas
nr_06 = QgsRasterLayer(nr_06_fn)

# Entradas para la calculadora raster
entry_162 = QgsRasterCalculatorEntry()
entry_162.ref = 'nr@6'
entry_162.raster = nr_06
entry_162.bandNumber = 1
entries.append(entry_162)



#
# Mes 7
#

# hsi
# Cálculos raster
calc_hsi_07 = QgsRasterCalculator(f'hsf@6',
                                  hsi_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_hsi_07.processCalculation()

# Capas
hsi_07 = QgsRasterLayer(hsi_07_fn)

# Entradas para la calculadora raster
entry_67 = QgsRasterCalculatorEntry()
entry_67.ref = 'hsi@7'
entry_67.raster = hsi_07
entry_67.bandNumber = 1
entries.append(entry_67)


# c1
# Cálculos raster
calc_c1_07 = QgsRasterCalculator(f'((hsi@7 - {PM_MM} + pi@7)/{CC_PM_MM} < 1) * (hsi@7 - {PM_MM} + pi@7)/{CC_PM_MM} + ((hsi@7 - {PM_MM} + pi@7)/{CC_PM_MM} >= 1) * 1',
                                  c1_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_c1_07.processCalculation()

# Capas
c1_07 = QgsRasterLayer(c1_07_fn)

# Entradas para la calculadora raster
entry_79 = QgsRasterCalculatorEntry()
entry_79.ref = 'c1@7'
entry_79.raster = c1_07
entry_79.bandNumber = 1
entries.append(entry_79)


# c2
# Cálculos raster
calc_c2_07 = QgsRasterCalculator(f'((hsi@7 - {PM_MM} + pi@7 - c1@7*etp@7)/{CC_PM_MM} > 1) * 1 + ((hsi@7 - {PM_MM} + pi@7 - c1@7*etp@7)/{CC_PM_MM} <= 1) * (  ((hsi@7 - {PM_MM} + pi@7 - c1@7*etp@7)/{CC_PM_MM} < 0) * 0 + ((hsi@7 - {PM_MM} + pi@7 - c1@7*etp@7)/{CC_PM_MM} >= 0) * (hsi@7 - {PM_MM} + pi@7 - c1@7*etp@7)/{CC_PM_MM}  )',
                                  c2_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_c2_07.processCalculation()

# Capas
c2_07 = QgsRasterLayer(c2_07_fn)

# Entradas para la calculadora raster
entry_91 = QgsRasterCalculatorEntry()
entry_91.ref = 'c2@7'
entry_91.raster = c2_07
entry_91.bandNumber = 1
entries.append(entry_91)


# hd
# Cálculos raster
calc_hd_07 = QgsRasterCalculator(f'hsi@7 - {PM_MM} + pi@7',
                                  hd_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_hd_07.processCalculation()

# Capas
hd_07 = QgsRasterLayer(hd_07_fn)

# Entradas para la calculadora raster
entry_103 = QgsRasterCalculatorEntry()
entry_103.ref = 'hd@7'
entry_103.raster = hd_07
entry_103.bandNumber = 1
entries.append(entry_103)


# etr
# Cálculos raster
calc_etr_07 = QgsRasterCalculator(f'(hd@7 >= (c1@7 + c2@7)/2*etp@7) * (c1@7 + c2@7)/2*etp@7 + (hd@7 < (c1@7 + c2@7)/2*etp@7) * hd@7',
                                  etr_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_etr_07.processCalculation()

# Capas
etr_07 = QgsRasterLayer(etr_07_fn)

# Entradas para la calculadora raster
entry_115 = QgsRasterCalculatorEntry()
entry_115.ref = 'etr@7'
entry_115.raster = etr_07
entry_115.bandNumber = 1
entries.append(entry_115)


# hsf
# Cálculos raster
calc_hsf_07 = QgsRasterCalculator(f'(hd@7 + {PM_MM} - etr@7 >= {CC_MM}) * {CC_MM} + (hd@7 + {PM_MM} - etr@7 < {CC_MM}) * (hd@7 + {PM_MM} - etr@7)',
                                  hsf_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_hsf_07.processCalculation()

# Capas
hsf_07 = QgsRasterLayer(hsf_07_fn)

# Entradas para la calculadora raster
entry_127 = QgsRasterCalculatorEntry()
entry_127.ref = 'hsf@7'
entry_127.raster = hsf_07
entry_127.bandNumber = 1
entries.append(entry_127)


# dcc
# Cálculos raster
calc_dcc_07 = QgsRasterCalculator(f'{CC_MM} - hsf@7',
                                  dcc_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_dcc_07.processCalculation()

# Capas
dcc_07 = QgsRasterLayer(dcc_07_fn)

# Entradas para la calculadora raster
entry_139 = QgsRasterCalculatorEntry()
entry_139.ref = 'dcc@7'
entry_139.raster = dcc_07
entry_139.bandNumber = 1
entries.append(entry_139)


# rp
# Cálculos raster
calc_rp_07 = QgsRasterCalculator(f'pi@7 + hsi@7 - hsf@7 - etr@7',
                                  rp_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_rp_07.processCalculation()

# Capas
rp_07 = QgsRasterLayer(rp_07_fn)

# Entradas para la calculadora raster
entry_151 = QgsRasterCalculatorEntry()
entry_151.ref = 'rp@7'
entry_151.raster = rp_07
entry_151.bandNumber = 1
entries.append(entry_151)


# nr
# Cálculos raster
calc_nr_07 = QgsRasterCalculator(f'dcc@7 - etr@7 + etp@7',
                                  nr_07_fn, 
                                  'GTiff', 
                                  p_07.extent(), 
                                  p_07.width(), 
                                  p_07.height(), 
                                  entries)
calc_nr_07.processCalculation()

# Capas
nr_07 = QgsRasterLayer(nr_07_fn)

# Entradas para la calculadora raster
entry_163 = QgsRasterCalculatorEntry()
entry_163.ref = 'nr@7'
entry_163.raster = nr_07
entry_163.bandNumber = 1
entries.append(entry_163)



#
# Mes 8
#

# hsi
# Cálculos raster
calc_hsi_08 = QgsRasterCalculator(f'hsf@7',
                                  hsi_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_hsi_08.processCalculation()

# Capas
hsi_08 = QgsRasterLayer(hsi_08_fn)

# Entradas para la calculadora raster
entry_68 = QgsRasterCalculatorEntry()
entry_68.ref = 'hsi@8'
entry_68.raster = hsi_08
entry_68.bandNumber = 1
entries.append(entry_68)


# c1
# Cálculos raster
calc_c1_08 = QgsRasterCalculator(f'((hsi@8 - {PM_MM} + pi@8)/{CC_PM_MM} < 1) * (hsi@8 - {PM_MM} + pi@8)/{CC_PM_MM} + ((hsi@8 - {PM_MM} + pi@8)/{CC_PM_MM} >= 1) * 1',
                                  c1_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_c1_08.processCalculation()

# Capas
c1_08 = QgsRasterLayer(c1_08_fn)

# Entradas para la calculadora raster
entry_80 = QgsRasterCalculatorEntry()
entry_80.ref = 'c1@8'
entry_80.raster = c1_08
entry_80.bandNumber = 1
entries.append(entry_80)


# c2
# Cálculos raster
calc_c2_08 = QgsRasterCalculator(f'((hsi@8 - {PM_MM} + pi@8 - c1@8*etp@8)/{CC_PM_MM} > 1) * 1 + ((hsi@8 - {PM_MM} + pi@8 - c1@8*etp@8)/{CC_PM_MM} <= 1) * (  ((hsi@8 - {PM_MM} + pi@8 - c1@8*etp@8)/{CC_PM_MM} < 0) * 0 + ((hsi@8 - {PM_MM} + pi@8 - c1@8*etp@8)/{CC_PM_MM} >= 0) * (hsi@8 - {PM_MM} + pi@8 - c1@8*etp@8)/{CC_PM_MM}  )',
                                  c2_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_c2_08.processCalculation()

# Capas
c2_08 = QgsRasterLayer(c2_08_fn)

# Entradas para la calculadora raster
entry_92 = QgsRasterCalculatorEntry()
entry_92.ref = 'c2@8'
entry_92.raster = c2_08
entry_92.bandNumber = 1
entries.append(entry_92)


# hd
# Cálculos raster
calc_hd_08 = QgsRasterCalculator(f'hsi@8 - {PM_MM} + pi@8',
                                  hd_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_hd_08.processCalculation()

# Capas
hd_08 = QgsRasterLayer(hd_08_fn)

# Entradas para la calculadora raster
entry_104 = QgsRasterCalculatorEntry()
entry_104.ref = 'hd@8'
entry_104.raster = hd_08
entry_104.bandNumber = 1
entries.append(entry_104)


# etr
# Cálculos raster
calc_etr_08 = QgsRasterCalculator(f'(hd@8 >= (c1@8 + c2@8)/2*etp@8) * (c1@8 + c2@8)/2*etp@8 + (hd@8 < (c1@8 + c2@8)/2*etp@8) * hd@8',
                                  etr_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_etr_08.processCalculation()

# Capas
etr_08 = QgsRasterLayer(etr_08_fn)

# Entradas para la calculadora raster
entry_116 = QgsRasterCalculatorEntry()
entry_116.ref = 'etr@8'
entry_116.raster = etr_08
entry_116.bandNumber = 1
entries.append(entry_116)


# hsf
# Cálculos raster
calc_hsf_08 = QgsRasterCalculator(f'(hd@8 + {PM_MM} - etr@8 >= {CC_MM}) * {CC_MM} + (hd@8 + {PM_MM} - etr@8 < {CC_MM}) * (hd@8 + {PM_MM} - etr@8)',
                                  hsf_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_hsf_08.processCalculation()

# Capas
hsf_08 = QgsRasterLayer(hsf_08_fn)

# Entradas para la calculadora raster
entry_128 = QgsRasterCalculatorEntry()
entry_128.ref = 'hsf@8'
entry_128.raster = hsf_08
entry_128.bandNumber = 1
entries.append(entry_128)


# dcc
# Cálculos raster
calc_dcc_08 = QgsRasterCalculator(f'{CC_MM} - hsf@8',
                                  dcc_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_dcc_08.processCalculation()

# Capas
dcc_08 = QgsRasterLayer(dcc_08_fn)

# Entradas para la calculadora raster
entry_140 = QgsRasterCalculatorEntry()
entry_140.ref = 'dcc@8'
entry_140.raster = dcc_08
entry_140.bandNumber = 1
entries.append(entry_140)


# rp
# Cálculos raster
calc_rp_08 = QgsRasterCalculator(f'pi@8 + hsi@8 - hsf@8 - etr@8',
                                  rp_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_rp_08.processCalculation()

# Capas
rp_08 = QgsRasterLayer(rp_08_fn)

# Entradas para la calculadora raster
entry_152 = QgsRasterCalculatorEntry()
entry_152.ref = 'rp@8'
entry_152.raster = rp_08
entry_152.bandNumber = 1
entries.append(entry_152)


# nr
# Cálculos raster
calc_nr_08 = QgsRasterCalculator(f'dcc@8 - etr@8 + etp@8',
                                  nr_08_fn, 
                                  'GTiff', 
                                  p_08.extent(), 
                                  p_08.width(), 
                                  p_08.height(), 
                                  entries)
calc_nr_08.processCalculation()

# Capas
nr_08 = QgsRasterLayer(nr_08_fn)

# Entradas para la calculadora raster
entry_164 = QgsRasterCalculatorEntry()
entry_164.ref = 'nr@8'
entry_164.raster = nr_08
entry_164.bandNumber = 1
entries.append(entry_164)



#
# Mes 9
#

# hsi
# Cálculos raster
calc_hsi_09 = QgsRasterCalculator(f'hsf@8',
                                  hsi_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_hsi_09.processCalculation()

# Capas
hsi_09 = QgsRasterLayer(hsi_09_fn)

# Entradas para la calculadora raster
entry_69 = QgsRasterCalculatorEntry()
entry_69.ref = 'hsi@9'
entry_69.raster = hsi_09
entry_69.bandNumber = 1
entries.append(entry_69)


# c1
# Cálculos raster
calc_c1_09 = QgsRasterCalculator(f'((hsi@9 - {PM_MM} + pi@9)/{CC_PM_MM} < 1) * (hsi@9 - {PM_MM} + pi@9)/{CC_PM_MM} + ((hsi@9 - {PM_MM} + pi@9)/{CC_PM_MM} >= 1) * 1',
                                  c1_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_c1_09.processCalculation()

# Capas
c1_09 = QgsRasterLayer(c1_09_fn)

# Entradas para la calculadora raster
entry_81 = QgsRasterCalculatorEntry()
entry_81.ref = 'c1@9'
entry_81.raster = c1_09
entry_81.bandNumber = 1
entries.append(entry_81)


# c2
# Cálculos raster
calc_c2_09 = QgsRasterCalculator(f'((hsi@9 - {PM_MM} + pi@9 - c1@9*etp@9)/{CC_PM_MM} > 1) * 1 + ((hsi@9 - {PM_MM} + pi@9 - c1@9*etp@9)/{CC_PM_MM} <= 1) * (  ((hsi@9 - {PM_MM} + pi@9 - c1@9*etp@9)/{CC_PM_MM} < 0) * 0 + ((hsi@9 - {PM_MM} + pi@9 - c1@9*etp@9)/{CC_PM_MM} >= 0) * (hsi@9 - {PM_MM} + pi@9 - c1@9*etp@9)/{CC_PM_MM}  )',
                                  c2_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_c2_09.processCalculation()

# Capas
c2_09 = QgsRasterLayer(c2_09_fn)

# Entradas para la calculadora raster
entry_93 = QgsRasterCalculatorEntry()
entry_93.ref = 'c2@9'
entry_93.raster = c2_09
entry_93.bandNumber = 1
entries.append(entry_93)


# hd
# Cálculos raster
calc_hd_09 = QgsRasterCalculator(f'hsi@9 - {PM_MM} + pi@9',
                                  hd_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_hd_09.processCalculation()

# Capas
hd_09 = QgsRasterLayer(hd_09_fn)

# Entradas para la calculadora raster
entry_105 = QgsRasterCalculatorEntry()
entry_105.ref = 'hd@9'
entry_105.raster = hd_09
entry_105.bandNumber = 1
entries.append(entry_105)


# etr
# Cálculos raster
calc_etr_09 = QgsRasterCalculator(f'(hd@9 >= (c1@9 + c2@9)/2*etp@9) * (c1@9 + c2@9)/2*etp@9 + (hd@9 < (c1@9 + c2@9)/2*etp@9) * hd@9',
                                  etr_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_etr_09.processCalculation()

# Capas
etr_09 = QgsRasterLayer(etr_09_fn)

# Entradas para la calculadora raster
entry_117 = QgsRasterCalculatorEntry()
entry_117.ref = 'etr@9'
entry_117.raster = etr_09
entry_117.bandNumber = 1
entries.append(entry_117)


# hsf
# Cálculos raster
calc_hsf_09 = QgsRasterCalculator(f'(hd@9 + {PM_MM} - etr@9 >= {CC_MM}) * {CC_MM} + (hd@9 + {PM_MM} - etr@9 < {CC_MM}) * (hd@9 + {PM_MM} - etr@9)',
                                  hsf_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_hsf_09.processCalculation()

# Capas
hsf_09 = QgsRasterLayer(hsf_09_fn)

# Entradas para la calculadora raster
entry_129 = QgsRasterCalculatorEntry()
entry_129.ref = 'hsf@9'
entry_129.raster = hsf_09
entry_129.bandNumber = 1
entries.append(entry_129)


# dcc
# Cálculos raster
calc_dcc_09 = QgsRasterCalculator(f'{CC_MM} - hsf@9',
                                  dcc_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_dcc_09.processCalculation()

# Capas
dcc_09 = QgsRasterLayer(dcc_09_fn)

# Entradas para la calculadora raster
entry_141 = QgsRasterCalculatorEntry()
entry_141.ref = 'dcc@9'
entry_141.raster = dcc_09
entry_141.bandNumber = 1
entries.append(entry_141)


# rp
# Cálculos raster
calc_rp_09 = QgsRasterCalculator(f'pi@9 + hsi@9 - hsf@9 - etr@9',
                                  rp_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_rp_09.processCalculation()

# Capas
rp_09 = QgsRasterLayer(rp_09_fn)

# Entradas para la calculadora raster
entry_153 = QgsRasterCalculatorEntry()
entry_153.ref = 'rp@9'
entry_153.raster = rp_09
entry_153.bandNumber = 1
entries.append(entry_153)


# nr
# Cálculos raster
calc_nr_09 = QgsRasterCalculator(f'dcc@9 - etr@9 + etp@9',
                                  nr_09_fn, 
                                  'GTiff', 
                                  p_09.extent(), 
                                  p_09.width(), 
                                  p_09.height(), 
                                  entries)
calc_nr_09.processCalculation()

# Capas
nr_09 = QgsRasterLayer(nr_09_fn)

# Entradas para la calculadora raster
entry_165 = QgsRasterCalculatorEntry()
entry_165.ref = 'nr@9'
entry_165.raster = nr_09
entry_165.bandNumber = 1
entries.append(entry_165)



#
# Mes 10
#

# hsi
# Cálculos raster
calc_hsi_10 = QgsRasterCalculator(f'hsf@9',
                                  hsi_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_hsi_10.processCalculation()

# Capas
hsi_10 = QgsRasterLayer(hsi_10_fn)

# Entradas para la calculadora raster
entry_70 = QgsRasterCalculatorEntry()
entry_70.ref = 'hsi@10'
entry_70.raster = hsi_10
entry_70.bandNumber = 1
entries.append(entry_70)


# c1
# Cálculos raster
calc_c1_10 = QgsRasterCalculator(f'((hsi@10 - {PM_MM} + pi@10)/{CC_PM_MM} < 1) * (hsi@10 - {PM_MM} + pi@10)/{CC_PM_MM} + ((hsi@10 - {PM_MM} + pi@10)/{CC_PM_MM} >= 1) * 1',
                                  c1_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_c1_10.processCalculation()

# Capas
c1_10 = QgsRasterLayer(c1_10_fn)

# Entradas para la calculadora raster
entry_82 = QgsRasterCalculatorEntry()
entry_82.ref = 'c1@10'
entry_82.raster = c1_10
entry_82.bandNumber = 1
entries.append(entry_82)


# c2
# Cálculos raster
calc_c2_10 = QgsRasterCalculator(f'((hsi@10 - {PM_MM} + pi@10 - c1@10*etp@10)/{CC_PM_MM} > 1) * 1 + ((hsi@10 - {PM_MM} + pi@10 - c1@10*etp@10)/{CC_PM_MM} <= 1) * (  ((hsi@10 - {PM_MM} + pi@10 - c1@10*etp@10)/{CC_PM_MM} < 0) * 0 + ((hsi@10 - {PM_MM} + pi@10 - c1@10*etp@10)/{CC_PM_MM} >= 0) * (hsi@10 - {PM_MM} + pi@10 - c1@10*etp@10)/{CC_PM_MM}  )',
                                  c2_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_c2_10.processCalculation()

# Capas
c2_10 = QgsRasterLayer(c2_10_fn)

# Entradas para la calculadora raster
entry_94 = QgsRasterCalculatorEntry()
entry_94.ref = 'c2@10'
entry_94.raster = c2_10
entry_94.bandNumber = 1
entries.append(entry_94)


# hd
# Cálculos raster
calc_hd_10 = QgsRasterCalculator(f'hsi@10 - {PM_MM} + pi@10',
                                  hd_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_hd_10.processCalculation()

# Capas
hd_10 = QgsRasterLayer(hd_10_fn)

# Entradas para la calculadora raster
entry_106 = QgsRasterCalculatorEntry()
entry_106.ref = 'hd@10'
entry_106.raster = hd_10
entry_106.bandNumber = 1
entries.append(entry_106)


# etr
# Cálculos raster
calc_etr_10 = QgsRasterCalculator(f'(hd@10 >= (c1@10 + c2@10)/2*etp@10) * (c1@10 + c2@10)/2*etp@10 + (hd@10 < (c1@10 + c2@10)/2*etp@10) * hd@10',
                                  etr_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_etr_10.processCalculation()

# Capas
etr_10 = QgsRasterLayer(etr_10_fn)

# Entradas para la calculadora raster
entry_118 = QgsRasterCalculatorEntry()
entry_118.ref = 'etr@10'
entry_118.raster = etr_10
entry_118.bandNumber = 1
entries.append(entry_118)


# hsf
# Cálculos raster
calc_hsf_10 = QgsRasterCalculator(f'(hd@10 + {PM_MM} - etr@10 >= {CC_MM}) * {CC_MM} + (hd@10 + {PM_MM} - etr@10 < {CC_MM}) * (hd@10 + {PM_MM} - etr@10)',
                                  hsf_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_hsf_10.processCalculation()

# Capas
hsf_10 = QgsRasterLayer(hsf_10_fn)

# Entradas para la calculadora raster
entry_130 = QgsRasterCalculatorEntry()
entry_130.ref = 'hsf@10'
entry_130.raster = hsf_10
entry_130.bandNumber = 1
entries.append(entry_130)


# dcc
# Cálculos raster
calc_dcc_10 = QgsRasterCalculator(f'{CC_MM} - hsf@10',
                                  dcc_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_dcc_10.processCalculation()

# Capas
dcc_10 = QgsRasterLayer(dcc_10_fn)

# Entradas para la calculadora raster
entry_142 = QgsRasterCalculatorEntry()
entry_142.ref = 'dcc@10'
entry_142.raster = dcc_10
entry_142.bandNumber = 1
entries.append(entry_142)


# rp
# Cálculos raster
calc_rp_10 = QgsRasterCalculator(f'pi@10 + hsi@10 - hsf@10 - etr@10',
                                  rp_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_rp_10.processCalculation()

# Capas
rp_10 = QgsRasterLayer(rp_10_fn)

# Entradas para la calculadora raster
entry_154 = QgsRasterCalculatorEntry()
entry_154.ref = 'rp@10'
entry_154.raster = rp_10
entry_154.bandNumber = 1
entries.append(entry_154)


# nr
# Cálculos raster
calc_nr_10 = QgsRasterCalculator(f'dcc@10 - etr@10 + etp@10',
                                  nr_10_fn, 
                                  'GTiff', 
                                  p_10.extent(), 
                                  p_10.width(), 
                                  p_10.height(), 
                                  entries)
calc_nr_10.processCalculation()

# Capas
nr_10 = QgsRasterLayer(nr_10_fn)

# Entradas para la calculadora raster
entry_166 = QgsRasterCalculatorEntry()
entry_166.ref = 'nr@10'
entry_166.raster = nr_10
entry_166.bandNumber = 1
entries.append(entry_166)



#
# Sumas pendientes
#


# Cálculo de la suma anual de hsi
calc_sum = QgsRasterCalculator(f'hsi@1 + hsi@2 + hsi@3 + hsi@4 + hsi@5 + hsi@6 + hsi@7 + hsi@8 + hsi@9 + hsi@10 + hsi@11 + hsi@12',
                               hsi_suma_fn, 
                               'GTiff', 
                               hsi_01.extent(), 
                               hsi_01.width(), 
                               hsi_01.height(), 
                               entries)
calc_sum.processCalculation()


# Cálculo de la suma anual de hd
calc_sum = QgsRasterCalculator(f'hd@1 + hd@2 + hd@3 + hd@4 + hd@5 + hd@6 + hd@7 + hd@8 + hd@9 + hd@10 + hd@11 + hd@12',
                               hd_suma_fn, 
                               'GTiff', 
                               hd_01.extent(), 
                               hd_01.width(), 
                               hd_01.height(), 
                               entries)
calc_sum.processCalculation()


# Cálculo de la suma anual de etr
calc_sum = QgsRasterCalculator(f'etr@1 + etr@2 + etr@3 + etr@4 + etr@5 + etr@6 + etr@7 + etr@8 + etr@9 + etr@10 + etr@11 + etr@12',
                               etr_suma_fn, 
                               'GTiff', 
                               etr_01.extent(), 
                               etr_01.width(), 
                               etr_01.height(), 
                               entries)
calc_sum.processCalculation()


# Cálculo de la suma anual de hsf
calc_sum = QgsRasterCalculator(f'hsf@1 + hsf@2 + hsf@3 + hsf@4 + hsf@5 + hsf@6 + hsf@7 + hsf@8 + hsf@9 + hsf@10 + hsf@11 + hsf@12',
                               hsf_suma_fn, 
                               'GTiff', 
                               hsf_01.extent(), 
                               hsf_01.width(), 
                               hsf_01.height(), 
                               entries)
calc_sum.processCalculation()


# Cálculo de la suma anual de dcc
calc_sum = QgsRasterCalculator(f'dcc@1 + dcc@2 + dcc@3 + dcc@4 + dcc@5 + dcc@6 + dcc@7 + dcc@8 + dcc@9 + dcc@10 + dcc@11 + dcc@12',
                               dcc_suma_fn, 
                               'GTiff', 
                               dcc_01.extent(), 
                               dcc_01.width(), 
                               dcc_01.height(), 
                               entries)
calc_sum.processCalculation()


# Cálculo de la suma anual de rp
calc_sum = QgsRasterCalculator(f'rp@1 + rp@2 + rp@3 + rp@4 + rp@5 + rp@6 + rp@7 + rp@8 + rp@9 + rp@10 + rp@11 + rp@12',
                               rp_suma_fn, 
                               'GTiff', 
                               rp_01.extent(), 
                               rp_01.width(), 
                               rp_01.height(), 
                               entries)
calc_sum.processCalculation()


# Cálculo de la suma anual de nr
calc_sum = QgsRasterCalculator(f'nr@1 + nr@2 + nr@3 + nr@4 + nr@5 + nr@6 + nr@7 + nr@8 + nr@9 + nr@10 + nr@11 + nr@12',
                               nr_suma_fn, 
                               'GTiff', 
                               nr_01.extent(), 
                               nr_01.width(), 
                               nr_01.height(), 
                               entries)
calc_sum.processCalculation()