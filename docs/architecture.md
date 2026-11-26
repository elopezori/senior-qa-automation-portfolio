\# Arquitectura del portfolio



\## 1. Objetivo



Documentar las decisiones de diseño, tecnologías y principios arquitectónicos utilizados en los frameworks de automatización del Senior QA Automation Portfolio.



La arquitectura busca mantener soluciones modulares, mantenibles y escalables, separando responsabilidades entre pruebas, clientes, datos, configuración y utilidades.



\## 2. Principios de diseño



\- Preferir pruebas independientes y deterministas.

\- Aplicar patrones de diseño cuando aporten mantenibilidad y reduzcan duplicación.

\- Separar responsabilidades entre tests, lógica de automatización y configuración.

\- Mantener selectores robustos y sincronización explícita.

\- Gestionar datos de prueba de forma controlada.

\- Separar configuración y secretos del código fuente.

\- Generar evidencias útiles para diagnosticar fallos.

\- Facilitar la ejecución local y futura integración en CI/CD.



\## 3. Stack tecnológico



\### Automatización web



\- C# y .NET.

\- Playwright for .NET.

\- NUnit.

\- Python.

\- Playwright para Python.

\- Pytest.

\- Page Object Model (POM).



\### Automatización de APIs



\- Python.

\- Requests.

\- Pytest.

\- JSON Schema.

\- Allure.

\- Postman y .NET como tecnologías previstas para futuras implementaciones.



\### Otras tecnologías previstas



\- Selenium WebDriver con C#.

\- Apache JMeter.

\- Jenkins.

\- Git y GitHub.



\## 4. Organización de los proyectos



Los frameworks se mantienen como proyectos independientes dentro del repositorio.



Cada proyecto dispone de su propia configuración y dependencias, permitiendo ejecutar y mantener sus pruebas sin acoplamiento innecesario con los demás.



La separación de responsabilidades se aplica de la siguiente manera:



\- \*\*Tests:\*\* contienen los escenarios y verificaciones.

\- \*\*Clients:\*\* encapsulan las comunicaciones y operaciones reutilizables, especialmente en API Testing.

\- \*\*Pages:\*\* contienen la lógica de interacción con las páginas web cuando se aplica POM.

\- \*\*Schemas:\*\* mantienen los contratos de validación de estructuras JSON.

\- \*\*Config:\*\* centraliza parámetros de configuración.

\- \*\*Reporting:\*\* gestiona los resultados y evidencias de ejecución.



La organización concreta puede variar según las necesidades de cada framework.



\## 5. Decisiones técnicas actuales



| Área | Decisión |

|---|---|

| Automatización web .NET | Playwright for .NET |

| Framework de testing .NET | NUnit |

| Automatización web Python | Playwright + Pytest |

| Patrón de diseño web | Page Object Model |

| Automatización API | Requests + Pytest |

| Validación de contratos API | JSON Schema |

| Reporting API | Pytest HTML + Allure |

| Control de versiones | Git + GitHub |



\## 6. Decisiones pendientes



Las siguientes decisiones se evaluarán conforme evolucionen los proyectos:



\- Estrategia de ejecución paralela.

\- Gestión avanzada de datos y entornos.

\- Estrategia común de reporting entre frameworks.

\- Integración de los proyectos en Jenkins.

\- Estrategia de ejecución en distintos navegadores y plataformas.

\- Gestión de configuración y secretos para CI/CD.



\## 7. Evolución de la arquitectura



La arquitectura evolucionará progresivamente con la incorporación de nuevos frameworks y herramientas.



Las futuras implementaciones incluirán:



\- Selenium WebDriver con C#.

\- Automatización API con Postman.

\- Automatización API con .NET.

\- Pruebas de rendimiento con Apache JMeter.

\- Integración continua mediante Jenkins.



Las decisiones arquitectónicas se revisarán y documentarán según las necesidades reales de cada proyecto.

