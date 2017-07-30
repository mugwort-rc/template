template
========

Jinja2 based template generator

Usage
-----

```
usage: template.py [-h] [--dest DEST] template context
```

### PyQt5

```
$ unzip -l examples/PyQt5.zip 
Archive:  examples/PyQt5.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2017-07-30 13:41   tools/
       65  2017-07-30 13:41   tools/pyqt.sh
        0  2017-07-30 13:41   ui/
       18  2017-07-30 13:40   ui/.gitignore
      594  2017-07-30 13:41   ui/mainwindow.ui
        0  2017-07-30 13:39   ui/__init__.py
       32  2017-07-30 13:53   APPLICATION.pro
      256  2017-07-22 12:59   main.py
      248  2017-07-22 13:03   mainwindow.py
      440  2017-07-30 13:49   setup.py
---------                     -------
     1653                     10 files
$ cat examples/PyQt5.yml
binaries: []
dynamic_filename:
  APPLICATION.pro: "{{ application_name }}.pro"
ctx:
  application_name: "PyQt5"

$ ./template.py examples/PyQt5.zip examples/PyQt5.yml --dest some/target/path/
$ ls some/target/path/
PyQt5.pro  main.py  mainwindow.py  setup.py  tools  ui
```
