# Roadmap

- [ ] Completar perfil y enlaces profesionales del README.
- [ ] Implementar framework Playwright for .NET.
- [x] Añadir suite Selenium WebDriver con C#.
- [ ] Crear colección Postman y documentación API.
- [ ] Automatizar pruebas API con .NET.
- [ ] Crear escenario de rendimiento JMeter.
- [ ] Integrar ejecución y publicación de resultados en Jenkins.
- [ ] Añadir evidencias reproducibles y decisiones técnicas.
- [ ] Revisar documentación y preparar demo para entrevistas.

## Pending validation on macOS

The Selenium framework has been successfully built and its existing test passed on the corporate Windows machine.

However, Windows Smart App Control initially blocked the NUnit test adapter DLL with error `0x800711C7`.

The corporate security restrictions must not be disabled or bypassed.

When the repository is cloned on the personal Mac:

- [ ] Restore .NET dependencies.
- [ ] Run the Selenium test suite using `dotnet test`.
- [ ] Verify that NUnit discovers and executes all tests.
- [ ] Validate automatic screenshot capture when a test fails.
- [ ] Document the validation results.

**Note:** Screenshot capture has been implemented in the framework, but still needs to be validated on an environment where test execution is not blocked.