# BDC-Geoserver-Tests

## Tests

In order to run tests, use the following command:

```bash
cd ..
python3 manager.py test
```

It will generate folder htmlcov with code coverage. You can serve these files through web server. You can also check locally with the command:


```bash
cd htmlcov
# For Python 3
python -m http.server
```

Access the web browser the url: http://127.0.0.1:8000