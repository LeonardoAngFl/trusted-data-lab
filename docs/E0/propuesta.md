# Propuesta del Observatorio — Trusted Data Lab
## Observatorio del Precio del Limón Mexicano en Colima

**Integrante:** Leonardo Gerardo Anguiano Flores
**Entrega:** E0 · Noviembre 2026

---

## 1. Ficha del observatorio

| Campo | Descripción |
|---|---|
| **Sector** | Agroalimentario: comercialización de limón mexicano (*Citrus aurantifolia*) |
| **Región** | Colima (zona productora Tecomán–Armería), con comparación en mercados mayoristas nacionales |
| **Pregunta detonadora** | ¿Podemos anticipar el precio mayorista del limón en las próximas semanas y entender qué factores explican su volatilidad, para que productores y compradores de Colima decidan mejor cuándo vender o comprar? |
| **Cliente potencial** | Productores y empacadoras de limón de Tecomán. Comercializadores y restauranteros que compran limón en volumen. |

### Justificación
Colima es uno de los principales estados productores de limón mexicano, y la economía de municipios como Tecomán depende fuertemente de este cultivo. El precio tiene una volatilidad muy alta: puede multiplicarse o desplomarse en pocas semanas por la estacionalidad, el clima, las plagas (por ejemplo, el HLB o dragón amarillo) y la entrada de fruta de otros estados. Hoy el productor pequeño suele enterarse del precio por intermediarios, con información incompleta y tardía. Un observatorio que capture precios públicos de forma automática, los limpie y los pronostique reduce esa asimetría de información.

---

## 2. Entrevista de campo

| Campo | Dato |
|---|---|
| Entrevistado | Don Chayo |
| Rol en el sector | Empacador y comprador de limón, 22 años de experiencia |
| Lugar y fecha | Afuera de su bodega, Tecomán, Colima — 08/11/2026 |
| Medio y duración | Presencial — 20 min |
| Transcripción completa | [`docs/E0/entrevista_transcripcion.md`](entrevista_transcripcion.md) |

### Preguntas y respuestas (resumen)
1. **¿Cuántos años lleva moviendo limón en la zona de Tecomán?**
   R: 22 años. Empezó con su padre juntando rejas de limón verde y hoy trabaja en el empaque.
2. **¿Cómo ha visto el movimiento del precio esta semana?**
   R: Lo describe como una "montaña rusa". El limón de primera se paga en campo a 14–15 $/kg, según tamaño y jugo. La semana anterior estaba cerca de 18 $/kg, pero la entrada de fruta de Michoacán y Veracruz saturó la oferta y el precio bajó de un día para otro.
3. **¿Cuáles son los principales problemas de un comprador o empacador en la región?**
   R: (a) El HLB (dragón amarillo), que ha reducido el rendimiento por hectárea durante años. (b) Las exigencias de calidad: los clientes del norte y de la Central de Abasto de la CDMX piden fruta uniforme, verde intenso y sin daños por trips ni sol. La fruta de menor calidad se castiga en precio o pasa a la categoría comercial, y el margen se reduce.
4. **¿Qué le afecta al cliente final de esta variación de precios?**
   R: Cuando el limón llega a 40–50 $/kg en supermercados y fondas, el público culpa al bodeguero. En realidad, el precio final incluye intermediarios, flete (a veces refrigerado), merma en el traslado y el costo de las rejas. El margen del empacador es de apenas 1–2 $/kg.
5. **¿Qué consejo le daría a alguien que quiera entrar al negocio?**
   R: Conocer bien la fruta (calidad y jugo) y cumplir con los pagos a los productores. El negocio se basa en la confianza, y quien especula sin saber de calidad pierde rápido.

### Aprendizajes
1. **Se confirma la alta volatilidad del precio.** Hubo una caída de unos 18 a 14–15 $/kg en una semana, lo que valida la pregunta de pronóstico (E1) y el valor de un aviso temprano para el productor.
2. **El origen de la fruta mueve el precio.** La entrada de limón de Michoacán y Veracruz satura el mercado. Esto confirma el **estado de origen** como factor del experimento (E2).
3. **La calidad define el precio.** La diferencia entre limón de primera y comercial es determinante. Se incorporará la **presentación/calidad** reportada por SNIIM como variable de control en E2 y E3.
4. **Hay una brecha grande entre campo y consumidor.** El limón pasa de 14–15 $/kg en campo a 40–50 $/kg al consumidor, con un margen de 1–2 $/kg para el empacador. Esto abre una línea para el observatorio: comparar la cadena **campo → mayoreo → consumidor**.
5. **La oferta estructural ha caído por el HLB.** Esto refuerza el uso de datos de producción del SIAP como covariable de oferta.

### Cambios al diseño a partir de la entrevista
- Se agrega la calidad/presentación como variable de segmentación en la capa Plata.
- Se agrega como posible fuente futura un precio al consumidor, para medir el margen de la cadena.
- El tablero final mostrará el precio semanal, su variación y un pronóstico a 4 semanas. Es la información que hoy el empacador obtiene solo "de boca en boca".

---

## 3. Las tres preguntas analíticas

### E1 — Variable a pronosticar
**¿Cuál será el precio frecuente mayorista (MXN/kg) del limón con semilla en las próximas 4 semanas?**
- Variable objetivo: precio frecuente reportado por SNIIM, agregado semanal y mensualmente.
- Covariables candidatas: INPC general y tipo de cambio FIX (Banxico), mes del año (estacionalidad).
- Métodos tentativos: regresión con componentes estacionales, suavizamiento exponencial y ARIMA/SARIMA.

### E2 — Factores a experimentar
**¿El precio del limón difiere significativamente según el mercado destino, el estado de origen y la temporada?**
- Factor A: mercado destino (por ejemplo, Central de Abasto CDMX, Guadalajara, Monterrey).
- Factor B: estado de origen (Colima vs. Michoacán vs. Veracruz/otros).
- Factor C: temporada (secas: noviembre–mayo vs. lluvias: junio–octubre).
- Variable de control: presentación/calidad.
- Método: ANOVA factorial con análisis de interacciones y pruebas post hoc.

### E3 — Grupos multivariados a comparar
**¿Existen perfiles distintos de mercados según el comportamiento conjunto de su precio promedio, su volatilidad y su diferencial entre precio mínimo y máximo?**
- Variables: precio medio, desviación estándar, rango mín–máx y tendencia por mercado.
- Métodos: MANOVA entre grupos de mercados y análisis de conglomerados (k-medias / jerárquico) con componentes principales.

---

## 4. Plan de recopilación de datos

### Fuente 1 — SNIIM (Sistema Nacional de Información e Integración de Mercados, Secretaría de Economía)
- **Contenido:** precios mayoristas diarios de frutas y hortalizas por producto, origen y mercado destino (mínimo, máximo y frecuente).
- **Método:** web scraping de la consulta pública por rango de fechas (`src/bronce/extraer_sniim.py`).
- **Periodicidad y alcance:** 40 meses hacia atrás (más de 36 periodos) y actualización diaria.

### Fuente 2 — Banco de México, Sistema de Información Económica (SIE API)
- **Contenido:** INPC general (serie SP1, mensual desde 2015) y tipo de cambio FIX (serie SF43718, diaria).
- **Método:** API REST oficial con token personal (`src/bronce/extraer_banxico.py`).

### Fuentes futuras (E1–E2)
- SIAP: producción mensual de limón por estado, como covariable de oferta.
- Precios al consumidor, para medir el margen de la cadena (aprendizaje de la entrevista).

### Análisis ético y legal

| Aspecto | SNIIM | Banxico SIE API |
|---|---|---|
| Naturaleza de los datos | Información pública gubernamental, sin datos personales | Información económica pública, sin datos personales |
| robots.txt | El extractor lo consulta automáticamente antes de cada ejecución y se detiene si la ruta está bloqueada. Resultado registrado en `logs/captura.log`. | No aplica: es un servicio de API oficial diseñado para consumo automatizado |
| Términos de uso | Uso con fines académicos y citando la fuente | Requiere token personal; uso conforme a los términos del SIE; citar a Banco de México como fuente |
| Carga al servidor | Una petición cada 3 s; descarga incremental; una ejecución diaria | Una petición por ejecución diaria |
| Transparencia | User-Agent identifica el proyecto y el repositorio | Token por usuario |
| Seguridad | Sin credenciales | El token se guarda como *GitHub Secret*, nunca en el código |

---

## 5. Máquina de captura (Capa Bronce)

- **Orquestación:** GitHub Actions (`.github/workflows/captura_bronce.yml`), diario a las 07:00 hora CDMX y ejecutable manualmente.
- **Principio Bronce:** se guarda la respuesta tal como llega (JSON de Banxico y HTML de SNIIM), más una versión tabular sin limpiar. Cada fila lleva `fecha_captura` para su trazabilidad.
- **Bitácora:** cada ejecución deja registro en `logs/captura.log`.
- **Tolerancia a fallos:** si SNIIM falla, Banxico se captura de todos modos y el error queda registrado.

---

## 6. Sistema de calidad inicial (PSP)
- Registros por integrante: `calidad/tiempo-leonardo.csv` y `calidad/defectos-leonardo.csv`.
- Objetivos medibles: `calidad/objetivos-calidad.md` (confiabilidad de la captura ≥ 95 %, densidad de defectos ≤ 10/KLOC y error de estimación ≤ 25 %).

---

## 7. Riesgos y mitigación

| Riesgo | Mitigación |
|---|---|
| Cambios en la estructura de la página de SNIIM | URL y parámetros configurables por variables del repositorio. Se respalda el HTML crudo para poder reprocesarlo. |
| Huecos en la serie (días sin reporte) | Agregación semanal y mensual en la capa Plata. Las puertas de calidad detectan los faltantes. |
| Caída de la API de Banxico | Reintento en la siguiente ejecución diaria. La historia ya capturada se conserva en el repositorio. |
