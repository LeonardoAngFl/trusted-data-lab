# Trusted Data Lab — Observatorio del Precio del Limón Mexicano (Colima)

Proyecto Integrador Interdisciplinario (Unidades 3 y 4).
Arquitectura por capas: **Bronce** (datos crudos) → **Plata** (limpios, con puertas de calidad) → **Oro** (integrados para modelado y tableros).

## Integrantes
- Leonardo Gerardo Anguiano Flores

## Fuentes de datos
| Fuente | Tipo | Contenido |
|---|---|---|
| SNIIM – Secretaría de Economía | Web scraping ético | Precios mayoristas diarios del limón por mercado y origen |
| Banxico SIE API | API REST (token) | INPC general (mensual) y tipo de cambio FIX (diario) |

## Ejecución local
```bash
pip install -r requirements.txt
export BANXICO_TOKEN=tu_token
export SNIIM_PRODUCTO_ID=id_del_limon
python src/bronce/extraer_banxico.py
python src/bronce/extraer_sniim.py
```

## Automatización
GitHub Actions (`.github/workflows/captura_bronce.yml`) se ejecuta diario a las 07:00 (hora CDMX) y guarda los datos crudos en `data/bronce/`.

## Entregas
- `e0` — Arranque, propuesta y máquina de captura → `docs/E0/`
