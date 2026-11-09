# Objetivos de calidad medibles (PSP)

| # | Objetivo | Métrica | Meta | Fuente de medición |
|---|---|---|---|---|
| 1 | Confiabilidad de la captura | % de ejecuciones programadas de GitHub Actions exitosas por semana | ≥ 95 % | Historial de Actions + `logs/captura.log` |
| 2 | Densidad de defectos | Defectos encontrados en pruebas por cada 1000 líneas de código (KLOC) | ≤ 10 def/KLOC | `calidad/defectos-*.csv` |
| 3 | Precisión de estimación | Error absoluto entre tiempo estimado y real por tarea | ≤ 25 % | `calidad/tiempo-*.csv` |

Tipos de defecto PSP: 10 Documentación, 20 Sintaxis, 30 Construcción, 40 Asignación, 50 Interfaz, 60 Verificación, 70 Datos, 80 Función, 90 Sistema, 100 Ambiente.

Revisión: semanal, al cierre de cada entrega (e0, e1, e2…).
