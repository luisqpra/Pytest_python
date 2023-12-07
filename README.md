# Test unitario con Python

Este proyecto es una guia base de como usar [Pytest](https://docs.pytest.org) para la realización de pruebas en Python. Aquí encontrarás una serie de módulos con ejemplos y casos de prueba que cubren diversas funcionalidades y características de Pytest.

Tambien encontraras ejemplos basicos de [Hypothesis][https://hypothesis.readthedocs.io] (Hypothesis_examples) para realizar pruebas de multiples paramtros. Esta libreria complementa muy bien a **Pytest**.

## Documentación

- Documentación oficial de Pytest: [https://docs.pytest.org](https://docs.pytest.org)
- Documentación personal: [Notion - Python Pytest](https://broadleaf-result-3b7.notion.site/Python-pytest-3ba9d2d68b1040b7a820611532d23a3f?pvs=4)

## Ejecución

Para ejecutar las pruebas, utiliza el siguiente comando en la terminal:

```bash
pytest -v --tb=no
```

## Módulos

### Pytest_topics/

1. **test_module01.py**
   - Ejemplos de funciones aritméticas.

2. **test_module02.py**
   - Ejemplos de pruebas en clases OOP.

3. **test_module03.py**
   - Ejemplos de casos de prueba con fallos esperados.

4. **test_module04.py**
   - Ejemplos de casos donde se seleccionan métodos que no se prueban (saltarlos).

5. **test_module05.py**
   - Ejemplos de pruebas marcadas para facilitar diversos testings.

6. **test_module06.py**
   - Ejemplos de casos donde se saltan métodos que fallan en las pruebas usando marks.

7. **test_module07.py**
   - Ejemplos de uso de parámetros para ingresar valores establecidos a los métodos y probarlos.

8. **test_module08.py**
   - Ejemplos de uso de testing de métodos con fixture (básico) para proporcionar datos o acciones de prueba antes de ejecutar las pruebas.

9. **test_module09.py**
   - Ejemplos de uso de fixture donde se toman valores y acciones iniciales predeterminadas para el testing de los métodos y luego se borran, permitiendo estar en el estado inicial.

10. **test_module10.py**
    - Ejemplos de uso de parámetros para ingresar valores configurados en "conftest.py" que puedes utilizar en las pruebas.

11. **test_module11.py**
    - Ejemplos de mostrar características de los métodos que se están testeando.

12. **test_module12.py**
    - Ejemplos de uso de múltiples parámetros evaluados con fixture.

13. **test_module13.py**
    - Ejemplos de testing en diferentes configuraciones de ambientes.

14. **test_module14.py**
    - Ejemplos de testing usando archivos de configuración para probar diferentes ambientes.

### Fixture scopes

Consulta la [documentación de Pytest sobre fixture scopes](https://docs.pytest.org/en/6.2.x/fixture.html) para entender los alcances de las fixtures.

### Test Outcomes

- **PASSED (.):** La prueba se ejecutó correctamente.
- **FAILED (F):** La prueba no se ejecutó correctamente (o XPASS + strict).
- **SKIPPED (s):** La prueba fue omitida. Puedes omitir una prueba utilizando los decoradores @pytest.mark.skip() o pytest.mark.skipif().
- **xfail (x):** Se esperaba que la prueba fallara, por lo que se ejecutó y falló. Puedes indicar a Pytest que una prueba se espera que falle utilizando el decorador @pytest.mark.xfail().
- **XPASS (X):** La prueba no debía pasar, pero se ejecutó y pasó.
- **ERROR (E):** Ocurrió una excepción fuera de la función de prueba, ya sea en una fixture.

## Estructura de Archivos

```
Pytest_topics/
├── config/
│   ├── prod.ini
│   └── qa.ini
├── conftest.py
├── _first_prog.py
├── __init__.py
├── prod.prop
├── py_assertions/
│   ├── __init__.py
│   └── test_module01.py
├── py_fixtures/
│   ├── conftest.py
│   ├── __init__.py
│   ├── test_module08.py
│   ├── test_module09.py
│   ├── test_module10.py
│   ├── test_module11.py
│   └── test_module12.py
├── qa.prop
├── test_module01.py
├── test_module02.py
├── test_module03.py
├── test_module04.py
├── test_module05.py
├── test_module06.py
├── test_module07.py
├── test_module13.py
├── test_module14.py
└── utils/
    ├── ConfigFileParser.py
    ├── __init__.py
    └── myconfigparser.py
```