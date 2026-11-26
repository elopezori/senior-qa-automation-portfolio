# 08. BUENAS PRÁCTICAS QA AUTOMATION

## Organización

- Mantener una estructura clara de carpetas.
- Separar los tests de las utilidades.
- Evitar duplicar código.
- Documentar los procedimientos importantes.

## Desarrollo de tests

- Utilizar nombres descriptivos.
- Crear pruebas independientes.
- Mantener un único objetivo por test.
- Utilizar assertions claras.
- Evitar dependencias entre pruebas.

## Playwright

- Priorizar get_by_role y get_by_label cuando sean adecuados.
- Utilizar identificadores estables.
- Evitar selectores frágiles.
- Evitar esperas fijas con time.sleep().
- Aprovechar las esperas automáticas de Playwright.

## Pytest

- Nombrar los archivos como test_*.py.
- Nombrar las funciones como test_*.
- Utilizar fixtures cuando sea necesario.
- Ejecutar las pruebas antes de realizar cambios importantes.
- Revisar los errores y resultados.

## Gestión de dependencias

- Trabajar con entorno virtual.
- Mantener actualizado requirements.txt.
- Evitar instalar paquetes innecesarios.
- Registrar las versiones utilizadas.

## Informes

- Generar informes después de las ejecuciones.
- Conservar históricos cuando sea necesario.
- Revisar los errores de cada ejecución.
- Comprobar que los datos del JSON son correctos.

## Seguridad

- No guardar contraseñas en el código.
- No subir credenciales a Git.
- Utilizar variables de entorno para información sensible.
- Mantener protegido el acceso a los informes que contengan datos privados.

## Control de versiones

- Utilizar Git.
- Realizar commits descriptivos.
- Mantener un archivo .gitignore.
- No subir la carpeta venv.

## Objetivo final

Conseguir una automatización mantenible, fiable, organizada y fácil de ampliar.
