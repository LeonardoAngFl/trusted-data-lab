"""Extractor Banxico SIE API — INPC general (SP1) y tipo de cambio FIX (SF43718). Capa Bronce."""
import datetime as dt
import json
import os
import sys

import pandas as pd
import requests

from common import BRONCE, ahora, log

SERIES = {
    "SP1": "INPC general (mensual)",
    "SF43718": "Tipo de cambio FIX pesos por dólar (diario)",
}
FECHA_INICIO = "2015-01-01"
URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/{ids}/datos/{ini}/{fin}"
DESTINO = BRONCE / "banxico"


def main() -> None:
    token = os.environ.get("BANXICO_TOKEN")
    if not token:
        log("BANXICO: falta la variable BANXICO_TOKEN")
        sys.exit(1)

    hoy = dt.date.today().isoformat()
    url = URL.format(ids=",".join(SERIES), ini=FECHA_INICIO, fin=hoy)
    r = requests.get(url, headers={"Bmx-Token": token, "Accept": "application/json"}, timeout=60)
    r.raise_for_status()
    datos = r.json()

    (DESTINO / "raw").mkdir(parents=True, exist_ok=True)
    with open(DESTINO / "raw" / f"banxico_{hoy}.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False)

    filas = []
    for s in datos["bmx"]["series"]:
        for d in s.get("datos", []):
            filas.append({
                "id_serie": s["idSerie"],
                "titulo": s["titulo"],
                "fecha": d["fecha"],
                "dato": d["dato"],
                "fecha_captura": ahora(),
            })
    df = pd.DataFrame(filas)
    df.to_csv(DESTINO / "banxico_series_crudo.csv", index=False, encoding="utf-8")

    for sid, n in df.groupby("id_serie").size().items():
        log(f"BANXICO {sid}: {n} periodos capturados")


if __name__ == "__main__":
    main()
