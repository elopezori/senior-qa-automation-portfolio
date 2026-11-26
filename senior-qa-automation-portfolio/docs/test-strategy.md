# Estrategia de pruebas

## Objetivo
Definir cómo seleccionar, diseñar, ejecutar y mantener pruebas de acuerdo con el riesgo del producto.

## Alcance inicial
- UI / E2E.
- API.
- Rendimiento.
- Integración continua.

## Enfoque basado en riesgos
Para cada funcionalidad se valorarán:
- Impacto del fallo.
- Probabilidad de ocurrencia.
- Exposición y frecuencia de uso.
- Complejidad e historial de defectos.

## Tipos de prueba
- Smoke: validar que los flujos críticos están disponibles.
- Regression: comprobar que cambios no rompen comportamientos existentes.
- API: validar contratos, reglas de negocio y errores.
- Performance: medir comportamiento bajo una carga definida.

## Criterios de entrada y salida
Se concretarán por proyecto. Los umbrales y resultados se documentarán con datos de ejecuciones reales, nunca estimados.
