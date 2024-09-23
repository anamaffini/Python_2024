from qgis.core import QgsApplication
import processing

# Starting a QGIS application
qgishome = r'C:\OSGeo4W64\apps\qgis\\'
app = QgsApplication([], True)
QgsApplication.setPrefixPath(qgishome, True)
QgsApplication.initQgis()