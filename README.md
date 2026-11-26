# Senior QA Automation Portfolio

> Portfolio técnico de **QA Automation Engineer** enfocado en automatización de pruebas, estrategia de calidad y entrega continua.

[![C#](https://img.shields.io/badge/C%23-.NET-512BD4?logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/)
[![Playwright](https://img.shields.io/badge/Playwright-.NET-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/dotnet/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Postman](https://img.shields.io/badge/API-Postman-FF6C37?logo=postman&logoColor=white)](https://www.postman.com/)
[![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-D24939?logo=jenkins&logoColor=white)](https://www.jenkins.io/)
[![JMeter](https://img.shields.io/badge/Performance-JMeter-D22128?logo=apachejmeter&logoColor=white)](https://jmeter.apache.org/)

## Sobre este portfolio

Este repositorio reúne proyectos prácticos y documentación técnica relacionados con Quality Engineering y QA Automation. 
El objetivo es mostrar cómo diseño, implemento y mantengo soluciones de testing fiables, mantenibles y alineadas con el riesgo del producto.

**Perfil objetivo:** Senior QA Automation Engineer  
**Lenguaje principal:** C#  
**Idioma de la documentación:** Español

> Personaliza esta sección con tu experiencia real, especialización, sectores y logros verificables antes de publicar el repositorio.

## Stack tecnológico

| Área | Tecnologías |
|---|---|
| Automatización web principal | Playwright for .NET, C# |
| Automatización web complementaria | Selenium WebDriver, C# |
| Automatización E2E complementaria | Cypress (JavaScript/TypeScript) |
| API testing | Requests, JSON Schema, Postman |
| Reporting | Allure, Pytest HTML |
| CI/CD | Jenkins |
| Rendimiento | Apache JMeter |
| Control de versiones | Git y GitHub, AzureDevops |

## Proyectos del repositorio

Los proyectos se incorporarán progresivamente. Cada uno incluirá instrucciones para ejecutarlo, alcance, estrategia, estructura, evidencias y limitaciones conocidas.

### 1. UI Automation — Python — Playwright + Pytest
**Estado:** 
Proyecto de automatización web desarrollada con Python, Playwright y Pytest.

**Incluye**
- Page Object Model (POM).
- Organización de tests y componentes reutilizables.
- Fixtures y configuración.
- Ejecución mediante Pytest.
- Generación de informes HTML.
- Script PowerShell para ejecutar las pruebas.

**Ubicación: playwright_learning/**

### 2. UI Automation — C# + .NET + Playweight + NUnit
**Estado:** 
Proyecto de automatización web desarrollado con C#, .NET y Playwright.

**Incluye**
-Estructura de solución .NET.
-Integración de Playwright.
-NUnit como framework de testing.
-Organización del proyecto para facilitar su mantenimiento y ampliación.

**Ubicación: dotnet_automation/**
Nota: La compilación del proyecto se ha validado. La ejecución de los tests está pendiente de validación en un entorno que permita ejecutar los procesos de Playwright.

### 3. API Automation — Python + Requests + Pytest
**Estado:**
Framework de automatización de APIs desarrollado con Python

**Incluye**
- Cliente HTTP reutilizable.
- Métodos GET, POST, PUT, PATCH y DELETE.
- Gestión de configuración y timeouts.
- Fixtures para gestionar el ciclo de vida del cliente.
- Validación de respuestas HTTP.
- Validación de estructuras JSON mediante JSON Schema.
- Validación de formatos de datos.
- Generación de informes HTML.
- Integración con Allure para reporting.

**Ubicación: api_automation/**
API utilizada: JSONPlaceholder, servicio público de pruebas. Las operaciones de escritura son simuladas y no persisten los datos.

### 4. UI Automation — Selenium WebDriver + C#
**Estado:** Pendiente
Proyecto previsto para ampliar la cobertura de automatización web con Selenium WebDriver.

**Objetivos:**
- Automatización con C# y Selenium.
- Page Object Model.
- Explicit Waits y sincronización.
- Gestión de navegadores.
- Configuración y ejecución de pruebas.

### 5. API Automation — Postman
**Estado:** Pendiente
Proyecto previsto para ampliar la estrategia de API Testing mediante Pstman

**Objetivos:**
- Colecciones de pruebas.
- Gestión de entornos y variables.
- Validación de códigos HTTP y payloads.
- Scripts de pre-request y post-response.
- Casos positivos, negativos y de límites.
- Ejecución automatizada mediante Newman.

### 6. API Automation — .NET
**Estado:** Pendiente
Proyecto previsto para desarrollar automatización de APIs utilizando C# y .NET.

**Objetivos:**
- Cliente HTTP reutilizable.
- Validación de respuestas y códigos de estado.
- Serialización y deserialización JSON.
- Validación de contratos.
- Integración con un framework de testing.

### 7. Performance Testing — Apache JMeter
**Estado:** Pendiente

**Objetivos:**
- Diseño de escenarios de carga.
- Configuración de usuarios concurrentes y ramp-up.
- Análisis de tiempos de respuesta y throughput.
- Identificación de cuellos de botella.
- Documentación de resultados.

### 8. CI/CD — Jenkins
**Estado:** Pendiente

**Objetivos:**
- Pipelines de ejecución automatizada.
- Integración de suites de pruebas.
- Publicación de resultados y artefactos.
- Gestión segura de parámetros y secretos.
- Notificaciones y criterios de fallo.

## Enfoque de Quality Engineering

En los proyectos se documentarán, cuando sean relevantes:

- Estrategia de pruebas basada en riesgos.
- Pirámide de testing y selección del nivel adecuado.
- Diseño de casos de prueba y cobertura.
- Prevención y análisis de pruebas flaky.
- Trazabilidad entre requisitos, riesgos y pruebas.
- Gestión de defectos y análisis de causa raíz.
- Accesibilidad y observabilidad de resultados.
- Mantenibilidad, tiempos de feedback y coste de ejecución.

## Estructura

```text
senior-qa-automation-portfolio/
├── README.md
├── LICENSE
├── .gitignore
├── ui-automation/
│   ├── playwright-dotnet/
│   └── selenium-dotnet/
├── api-automation/
│   ├── postman/
│   └── dotnet/
├── performance-testing/
│   └── jmeter/
├── ci-cd/
│   └── jenkins/
└── docs/
    ├── architecture.md
    ├── test-strategy.md
    └── roadmap.md
```

## Documentación

- [Arquitectura](docs/architecture.md)
- [Estrategia de pruebas](docs/test-strategy.md)
- [Roadmap del portfolio](docs/roadmap.md)

## Contacto

- **LinkedIn:** [Añade aquí tu perfil]
- **GitHub:** elopezori
- **Email profesional:** [Añade aquí tu email, si deseas publicarlo]

---

Este portfolio es un trabajo en evolución. Los estados de los proyectos se actualizarán a medida que se implementen y validen. 
No se publicarán credenciales, datos privados ni información confidencial de clientes o empresas.
