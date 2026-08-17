# Football Match Analysis - Roadmap de 3 semanas

**Fechas:** 17 de agosto al 6 de septiembre de 2026  
**Ritmo base:** minimo 2 horas por dia  
**Objetivo final:** publicar un analisis reproducible de **Argentina vs Colombia - Copa America 2024**, aprendiendo Python, Pandas, visualizacion, Git/GitHub y fundamentos de Football Analytics durante el proceso.

## Rutina diaria

- 20 min - concepto nuevo y apuntes.
- 30 min - ejercicios controlados.
- 60 min - aplicacion directa al proyecto.
- 10 min - cuaderno + `git status` / `git add` / `git commit` + proximo paso.

> 2 horas es el piso, no el techo. En sesiones largas conviene profundizar, corregir o adelantar sin sacrificar comprension.

---

# Semana 1 - Fundamentos: Git, entorno y Python

**17-23 agosto**  
**Objetivo semanal:** dejar una base de desarrollo profesional y terminar la semana pudiendo leer y escribir Python basico con ejemplos futbolisticos.  
**Definicion de terminado:** repo local + GitHub sincronizados, entorno virtual listo, dependencias controladas y mini analisis sobre datos ficticios.

## Dia 1 - Repositorio y primer historial
- [x] Entender working directory, staging, commit y repositorio local/remoto.
- [x] Crear `README.md` y `.gitignore`.
- [x] Hacer el primer commit.
- [x] Crear el repo remoto en GitHub y hacer el primer push.
- [x] Anotar con tus palabras la diferencia entre Git y GitHub.

**Entregable:** repositorio online con primer commit visible.

## Dia 2 - Entorno Python reproducible
- [ ] Entender `venv`, `pip`, interprete, paquete y dependencia.
- [ ] Crear `.venv` en `E:\Proyectos\football-match-analysis`.
- [ ] Seleccionar el interprete correcto en VS Code.
- [ ] Instalar Pandas, Matplotlib, mplsoccer y Jupyter dentro del entorno.
- [ ] Registrar las dependencias del proyecto.

**Entregable:** entorno aislado y reproducible funcionando.

## Dia 3 - Python I: variables y tipos
- [ ] Variables.
- [ ] `str`, `int`, `float`, `bool`.
- [ ] `print()`.
- [ ] Operadores basicos.
- [ ] Modelar equipos, goles, minutos, tiros y xG.

**Entregable:** ejercicios de Python I aplicados al futbol + commit.

## Dia 4 - Python II: listas y diccionarios
- [ ] Listas e indices.
- [ ] Diccionarios, claves y valores.
- [ ] Estructuras anidadas.
- [ ] Modelar planteles y estadisticas de jugadores.

**Entregable:** mini dataset en memoria de jugadores.

## Dia 5 - Python III: condiciones
- [ ] Comparaciones y booleanos.
- [ ] `if`, `elif`, `else`.
- [ ] `and`, `or`, `not`.
- [ ] Crear reglas simples para clasificar rendimientos.

**Entregable:** decisiones futbolisticas simples basadas en metricas.

## Dia 6 - Python IV: bucles y funciones
- [ ] `for`.
- [ ] Funciones.
- [ ] Parametros.
- [ ] `return`.
- [ ] Crear funciones como tiros por 90 y resumen de jugador.

**Entregable:** primeras funciones reutilizables.

## Dia 7 - Mini desafio de cierre
- [ ] Integrar los conceptos de la semana.
- [ ] Resolver un analisis sobre datos ficticios sin copiar una solucion completa.
- [ ] Leer y corregir errores simples.
- [ ] Actualizar README.
- [ ] Commit de cierre semanal.

**Entregable:** mini analisis terminado y semana 1 documentada.

---

# Semana 2 - Datos: Jupyter, Pandas y StatsBomb

**24-30 agosto**  
**Objetivo semanal:** pasar de Python basico a manipular datos tabulares reales y comprender la estructura de eventos de un partido.  
**Definicion de terminado:** notebook capaz de cargar Argentina vs Colombia, explorar eventos y responder preguntas basicas con Pandas.

## Dia 8 - Jupyter Notebook
- [ ] Entender celdas de codigo y Markdown.
- [ ] Entender kernel y orden de ejecucion.
- [ ] Crear el notebook principal.
- [ ] Documentar el analisis dentro del propio notebook.

**Entregable:** primer `.ipynb` limpio y versionado.

## Dia 9 - Formatos de datos
- [ ] Dataset, registro, fila y columna.
- [ ] CSV.
- [ ] JSON.
- [ ] Datos estructurados.
- [ ] Crear y leer pequenos datasets futbolisticos.

**Entregable:** ejercicios de lectura y carga de formatos.

## Dia 10 - Pandas I: DataFrame
- [ ] `DataFrame` y `Series`.
- [ ] `.head()`.
- [ ] `.shape`.
- [ ] `.columns`.
- [ ] `.dtypes`.
- [ ] Indice.

**Entregable:** inspeccion estructurada de una tabla de eventos.

## Dia 11 - Pandas II: seleccionar y filtrar
- [ ] Seleccionar columnas.
- [ ] Filtrar filas.
- [ ] Mascaras booleanas.
- [ ] Valores nulos.
- [ ] Aislar equipo, jugador y tipo de evento.

**Entregable:** consultas reproducibles sobre eventos.

## Dia 12 - Pandas III: resumir datos
- [ ] `.value_counts()`.
- [ ] `.groupby()`.
- [ ] `.sort_values()`.
- [ ] `count`, `sum`, `mean`.
- [ ] Crear columnas nuevas.

**Entregable:** primer resumen estadistico propio.

## Dia 13 - StatsBomb: datos reales
- [ ] Competicion y temporada.
- [ ] Partido.
- [ ] Evento.
- [ ] Coordenadas.
- [ ] Campos principales.
- [ ] Cargar Copa America 2024 y localizar Argentina vs Colombia.

**Entregable:** eventos reales cargados + diccionario inicial de campos.

## Dia 14 - Exploracion del partido
- [ ] Traducir preguntas futbolisticas a consultas de datos.
- [ ] Tiros.
- [ ] xG.
- [ ] Pases.
- [ ] Jugadores.
- [ ] Eventos principales.
- [ ] Commit de cierre semanal.

**Entregable:** resumen exploratorio del partido.

---

# Semana 3 - Football Analytics y portfolio

**31 agosto-6 septiembre**  
**Objetivo semanal:** transformar eventos en visualizaciones e interpretacion futbolistica y publicar un proyecto que pueda mostrarse en una postulacion.  
**Definicion de terminado:** analisis final documentado con visualizaciones, conclusiones, codigo ordenado y README profesional en GitHub.

## Dia 15 - Tiros y xG
- [ ] Entender xG.
- [ ] Volumen vs calidad de ocasiones.
- [ ] Agregar xG por equipo y jugador.
- [ ] Extraer primeras conclusiones.

**Entregable:** tabla y conclusiones de finalizacion.

## Dia 16 - Matplotlib
- [ ] Figura y axes.
- [ ] Scatter.
- [ ] Barras.
- [ ] Titulos y etiquetas.
- [ ] Exportar graficos.

**Entregable:** primeras figuras en `outputs/`.

## Dia 17 - Cancha y coordenadas
- [ ] Sistema de coordenadas StatsBomb.
- [ ] Fundamentos de mplsoccer.
- [ ] Dibujar una cancha.
- [ ] Ubicar eventos reales correctamente.

**Entregable:** primera visualizacion espacial validada.

## Dia 18 - Shot map profesional
- [ ] Posicion de tiros.
- [ ] Tamano de marcador segun xG.
- [ ] Etiquetas y legibilidad.
- [ ] Comparar Argentina y Colombia.

**Entregable:** shot map final listo para el README.

## Dia 19 - Pases y progresion
- [ ] Definir progresion.
- [ ] Analizar zonas del campo.
- [ ] Elegir criterios reproducibles.
- [ ] Comparar como avanzaron la pelota ambos equipos.

**Entregable:** visualizacion + interpretacion de progresion.

## Dia 20 - Defensa y territorio
- [ ] Recuperaciones.
- [ ] Presiones.
- [ ] Acciones defensivas.
- [ ] Zonas de recuperacion.
- [ ] Limites del dataset.

**Entregable:** segundo bloque analitico del informe.

## Dia 21 - Sintesis, limpieza y publicacion
**Sesion extendida ideal: 3-4 horas.**

- [ ] Elegir la historia final del analisis.
- [ ] Limpiar notebook y codigo.
- [ ] Mover funciones reutilizables a `src/` cuando tenga sentido.
- [ ] Mejorar todas las visualizaciones.
- [ ] Completar README profesional.
- [ ] Explicar metodologia, resultados y limites.
- [ ] Revisar reproducibilidad.
- [ ] Revisar `git status` y el historial.
- [ ] Hacer commit final y push.

**Entregable:** Proyecto 1 terminado y presentable en GitHub.

---

# Checklist de egreso del Proyecto 1

- [ ] Puedo explicar Git vs GitHub, local vs remoto, staging vs commit.
- [ ] Puedo crear/activar un entorno virtual e instalar dependencias con `pip`.
- [ ] Entiendo variables, listas, diccionarios, condiciones, bucles y funciones.
- [ ] Puedo inspeccionar, filtrar, agrupar y resumir un DataFrame.
- [ ] Entiendo la estructura basica de un evento de StatsBomb.
- [ ] Puedo calcular e interpretar tiros y xG.
- [ ] Puedo crear graficos con Matplotlib.
- [ ] Puedo representar eventos sobre una cancha con mplsoccer.
- [ ] Puedo formular una pregunta futbolistica y definir una metodologia para responderla.
- [ ] El notebook esta documentado y es comprensible.
- [ ] El README explica objetivo, datos, metodologia, resultados, limites y reproduccion.
- [ ] El repo esta limpio y tiene commits descriptivos.
- [ ] Puedo explicar personalmente cada decision importante del proyecto.

## Siguiente proyecto

**Football Scouting & Recruitment Analytics**: metricas por 90, percentiles, perfiles por posicion, comparacion de jugadores y shortlists.
