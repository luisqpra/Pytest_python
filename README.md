# Pytest 

Documentacion de "Pytest"
https://docs.pytest.org

Documentacion personal
https://broadleaf-result-3b7.notion.site/Python-pytest-3ba9d2d68b1040b7a820611532d23a3f?pvs=4

## RUN

ejecutar pytest con el siguente comando cmd:
pytest -v --tb=no

## Modulos

Directorio: Pytest_topics/

* En el modulo 1 (test_module01.py), encontraras ejemplos de funciones aritmeticas
* En el modulo 2 (test_module02.py), encontraras ejemplos de testing en clases OOP
* En el modulo 3 (test_module03.py), encontraras ejemplos de casos fallidos esperados
* En el modulo 4 (test_module04.py), encontraras ejemplos de casos donde se seleccionan metodos que no se testean (saltarlos)
* En el modulo 5 (test_module05.py), encontraras ejemplos de testing marcados para facilitar diversos testings
* En el modulo 6 (test_module06.py), encontraras ejemplos de casos donde se saltan metodos que fallan en el testing usando marks
* En el modulo 7 (test_module07.py), encontraras ejemplos de uso de parametros para ingresar valores establecidos a los metodos y testearlos
* En el modulo 8 (test_module08.py), encontraras ejemplos de uso de testar metodos con fixture (basico) para proporcionar datos o acciones de prueba antes de ejecutar las pruebas
* En el modulo 9 (test_module09.py), encontraras ejemplos de uso de fixture donde se toman valores y acciones iniciales predeterminadas para el testing de los metodos y luego se borran permitiento estar en el estado inicial
* En el modulo 10 (test_module10.py), encontraras ejemplos de uso de parametros para ingresar valores configurados en "conftest.py" que podras usar en los testing
* En el modulo 11 (test_module11.py), encontraras ejemplos de uso de mostrar caracteristicas de los metodos que se estan testeand.
* En el modulo 12 (test_module12.py), encontraras ejemplos de uso de multiple parametros evaluados con fixture.
* En el modulo 13 (test_module12.py), encontraras ejemplos de uso del testing en diferentes configuraciones de ambientes

## Fixture scopes

link: https://docs.pytest.org/en/6.2.x/fixture.html

Fixtures are created when first requested by a test, and are destroyed based on their scope:

* "function": the default scope, the fixture is destroyed at the end of the test.

* "class": the fixture is destroyed during teardown of the last test in the class.

* "module": the fixture is destroyed during teardown of the last test in the module.

* "package": the fixture is destroyed during teardown of the last test in the package.

* "session": the fixture is destroyed at the end of the test session.


## Test Outcomes

* "PASSED (.)": The test ran successfully.
* "FAILED (F)": The test did not run successfully (or XPASS + strict).
* "SKIPPED (s)": The test was skipped. You can tell pytest to skip a test by using either the @pytest.mark.skip() or pytest.mark.skipif()
decorators, discussed in Skipping Tests .
* "xfail (x)": The test was expected to fail, so ran and failed. You can tell pytest that a test is expected to fail by using the @pytest.mark.xfail()
decorator.
* "XPASS (X)": The test was not supposed to pass but ran and passed.
* "ERROR (E)": An exception happened outside of the test function, in either a fixture.