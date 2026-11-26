# Arquitectura del portfolio

## Objetivo
Documentar las decisiones de diseño de los frameworks de automatización y mantener una separación clara entre pruebas, datos, configuración y utilidades.

## Principios
- Preferir pruebas independientes y deterministas.
- Reutilizar código solo cuando reduzca duplicación sin ocultar el comportamiento.
- Mantener selectores robustos y sincronización explícita.
- Separar configuración y secretos del código.
- Publicar evidencias útiles para diagnosticar fallos.

## Stack principal
- C# y .NET.
- Playwright for .NET para automatización web.
- Selenium WebDriver con C# como implementación complementaria.

## Decisiones pendientes
- Versión de .NET y estrategia de actualización.
- Framework de testing (.NET test / NUnit / xUnit).
- Estrategia de ejecución paralela.
- Gestión de datos y entornos.
- Formato de reporting.
