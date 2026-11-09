"""Utilidades comunes de la capa Bronce: rutas, bitácora y verificación de robots.txt."""
import datetime as dt
from pathlib import Path
from urllib import robotparser
from urllib.parse import urlparse

RAIZ = Path(__file__).resolve().parents[2]
BRONCE = RAIZ / "data" / "bronce"
LOGS = RAIZ / "logs"

USER_AGENT = "TrustedDataLab-Bot/0.1 (proyecto academico; github.com/LeonardoAngFl/trusted-data-lab)"


def ahora() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def log(msg: str) -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    linea = f"[{ahora()}] {msg}"
    print(linea)
    with open(LOGS / "captura.log", "a", encoding="utf-8") as f:
        f.write(linea + "\n")


def robots_permite(url: str) -> bool:
    """Consulta robots.txt antes de descargar. Si no permite, no se descarga."""
    p = urlparse(url)
    rp = robotparser.RobotFileParser()
    rp.set_url(f"{p.scheme}://{p.netloc}/robots.txt")
    try:
        rp.read()
    except Exception as e:
        log(f"robots.txt de {p.netloc} no disponible ({e}); se procede con pausas conservadoras")
        return True
    ok = rp.can_fetch(USER_AGENT, url)
    log(f"robots.txt {p.netloc}: {'PERMITIDO' if ok else 'BLOQUEADO'}")
    return ok
