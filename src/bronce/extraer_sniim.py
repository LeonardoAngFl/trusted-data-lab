"""Extractor ético SNIIM — precios mayoristas del limón (capa Bronce).

Prácticas éticas: verifica robots.txt, se identifica con User-Agent,
hace 1 petición cada 3 s y es incremental (solo vuelve a pedir el mes en curso).
"""
import datetime as dt
import os
import time
from io import StringIO

import pandas as pd
import requests

from common import BRONCE, USER_AGENT, ahora, log, robots_permite

URL = os.environ.get("SNIIM_URL") or (
    "http://www.economia-sniim.gob.mx/NUEVO/Consultas/MercadosNacionales/"
    "PreciosDeMercado/Agricolas/ResultadosConsultaFechaFrutasYHortalizas.aspx"
)
PRODUCTO_ID = os.environ.get("SNIIM_PRODUCTO_ID", "").strip()
MESES_HISTORIA = 40
PAUSA_SEG = 3
DIR_HTML = BRONCE / "sniim" / "html"
SALIDA = BRONCE / "sniim" / "sniim_limon_crudo.csv"


def lista_meses(n):
    y, m = dt.date.today().year, dt.date.today().month
    out = []
    for _ in range(n):
        out.append((y, m))
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    return sorted(out)


def rango_mes(y, m):
    ini = dt.date(y, m, 1)
    sig = dt.date(y + 1, 1, 1) if m == 12 else dt.date(y, m + 1, 1)
    fin = sig - dt.timedelta(days=1)
    return ini.strftime("%d/%m/%Y"), fin.strftime("%d/%m/%Y")


def descargar():
    DIR_HTML.mkdir(parents=True, exist_ok=True)
    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    mes_actual = dt.date.today().strftime("%Y-%m")

    for y, m in lista_meses(MESES_HISTORIA):
        clave = f"{y}-{m:02d}"
        archivo = DIR_HTML / f"{clave}.html"
        if archivo.exists() and clave != mes_actual:
            continue
        ini, fin = rango_mes(y, m)
        params = {
            "fechaInicio": ini, "fechaFinal": fin, "ProductoId": PRODUCTO_ID,
            "OrigenId": "-1", "Origen": "Todos", "DestinoId": "-1", "Destino": "Todos",
            "PreciosPorId": "2", "RegistrosPorPagina": "1000",
        }
        try:
            r = s.get(URL, params=params, timeout=60)
            r.raise_for_status()
            archivo.write_text(r.text, encoding="utf-8")
            log(f"SNIIM {clave}: {len(r.text)} bytes descargados")
        except Exception as e:
            log(f"SNIIM {clave}: error {e}")
        time.sleep(PAUSA_SEG)


def consolidar():
    marcos = []
    for f in sorted(DIR_HTML.glob("*.html")):
        try:
            tablas = pd.read_html(StringIO(f.read_text(encoding="utf-8")))
        except ValueError:
            log(f"SNIIM {f.stem}: sin tablas en la respuesta")
            continue
        t = max(tablas, key=len)
        if isinstance(t.columns, pd.MultiIndex):
            t.columns = [" ".join(map(str, c)) for c in t.columns]
        t = t.astype(str)
        t.insert(0, "mes_consulta", f.stem)
        marcos.append(t)

    if marcos:
        df = pd.concat(marcos, ignore_index=True)
        df["fecha_captura"] = ahora()
        df.to_csv(SALIDA, index=False, encoding="utf-8")
        log(f"SNIIM consolidado: {len(df)} filas de {len(marcos)} meses")


def main():
    if not PRODUCTO_ID:
        log("SNIIM: falta SNIIM_PRODUCTO_ID; se omite esta fuente")
        return
    if not robots_permite(URL):
        log("SNIIM: robots.txt no permite la descarga; se omite")
        return
    descargar()
    consolidar()


if __name__ == "__main__":
    main()
