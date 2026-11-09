# Ficha de entrega técnica — E0

| Campo | Valor |
|---|---|
| Proyecto | Trusted Data Lab — Observatorio del Precio del Limón Mexicano (Colima) |
| Integrante(s) | Leonardo Gerardo Anguiano Flores |
| Repositorio | https://github.com/LeonardoAngFl/trusted-data-lab |
| Tag | `e0` |
| Fecha | 09/11/2026 |

## Checklist de entregables
- [x] Propuesta del observatorio → `docs/E0/propuesta.md`
- [x] Ficha del observatorio (sector, región, pregunta, cliente)
- [x] Entrevista de campo → sección 2 de la propuesta y `docs/E0/entrevista_transcripcion.md`
- [x] Tres preguntas analíticas (E1, E2, E3)
- [x] Plan de datos con 2 fuentes y análisis ético y legal
- [x] Extractor automático con GitHub Actions → `.github/workflows/captura_bronce.yml`
- [x] Serie histórica con 36 periodos o más → `data/bronce/banxico/banxico_series_crudo.csv` (SP1 mensual desde 2015) y `data/bronce/sniim/`
- [x] Registros PSP → `calidad/tiempo-leonardo.csv`, `calidad/defectos-leonardo.csv`
- [x] Tres objetivos de calidad → `calidad/objetivos-calidad.md`
- [x] Profesores agregados como colaboradores

## Cómo reproducir
1. Configurar el secret `BANXICO_TOKEN` y la variable `SNIIM_PRODUCTO_ID` en el repositorio.
2. Ir a Actions → "Captura Bronce" → Run workflow.
3. Revisar `logs/captura.log` y `data/bronce/`.

## Evidencia de funcionamiento
- Última ejecución exitosa del workflow: ver pestaña Actions del repositorio.
- Periodos capturados: ver `logs/captura.log`.

## Uso de herramientas de IA
Se utilizó un asistente de IA (Claude) como apoyo para estructurar el repositorio y generar el código base. El código fue revisado, ejecutado y probado por el equipo.
