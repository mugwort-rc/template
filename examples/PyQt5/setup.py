import py2exe
from distutils.core import setup

APPLICATION_NAME = "{{ application_name }}"


py2exe_options = {
    "compressed": 1,
    "optimize": 2,
    "bundle_files": 1,
    "includes" : ["sip",],
    "excludes": [],
    "dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
}
setup(
    options={"py2exe" : py2exe_options},
    windows=[{"script" : "main.py",
              "dest_base": APPLICATION_NAME}],
    zipfile=None,
)
