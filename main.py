# Importando as bibliotecas necessárias
from flask import Flask, render_template
from qgis.core import QgsApplication, QgsProject, QgsCoordinateReferenceSystem

# Configurando o ambiente QGIS
QgsApplication.setPrefixPath("/usr/bin", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Inicializando o projeto QGIS
project = QgsProject.instance()
project.setCrs(QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId))

# Criando uma função para gerar um mapa simples
def create_map( ):
    # Criando uma camada de terra
    layer = QgsVectorLayer("https://raw.githubusercontent.com/qgis/qgis-earthengine-examples/master/datasets/ne_110m_land/ne_110m_land.shp", "Terra", "ogr")
    project.addMapLayer(layer)



    # Seu código QGIS para criar o mapa aqui
    # Certifique-se de adicionar camadas, definir estilos, etc.

# Inicializando o Flask
app = Flask(__name__)

# Rota para exibir o mapa
@app.route('/')
def display_map():
    create_map()  # Chamando a função para criar o mapa
    return render_template('map.html')  # Página HTML para exibir o mapa

# Rodando o aplicativo Flask na rede local
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
