#Puerto, Río, Último Registro, Fecha Hora, y Estado
import requests
from bs4 import BeautifulSoup
pagina = requests.get("https://contenidosweb.prefecturanaval.gob.ar/alturas/index.php")
soup = BeautifulSoup(pagina.text,'html.parser')

filas = soup.find("table").find("tbody").find_all("tr")

puertos = []
rios = []
ultimo_registro = []
fecha_hora = []
estado = []

for fila in filas:
    puertos.append(fila.find("th").get_text())
    rios.append(fila.find_all("td")[0].get_text())
    ultimo_registro.append(fila.find_all("td")[1].get_text())
    fecha_hora.append(fila.find_all("td")[4].get_text())
    estado.append(fila.find_all("td")[5].get_text())

def get_puertos():
    return puertos

def get_rios():
    return rios

def get_ultimo_registro():
    return ultimo_registro

def get_fecha_hora():
    return fecha_hora

def get_estado():
    return estado