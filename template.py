#!/usr/bin/env python
import argparse
import sys
import os
import shutil
import zipfile

import jinja2
import yaml


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("template", type=argparse.FileType("rb"))
    parser.add_argument("context", type=argparse.FileType("r", encoding="utf-8"))
    parser.add_argument("--dest", default=os.getcwd())

    args = parser.parse_args()

    zfp = zipfile.ZipFile(args.template)
    context = yaml.load(args.context)
    assert isinstance(context, dict)

    binaries = context.get("binaries", [])
    dynamic_filename = context.get("dynamic_filename", {})
    ctx = context.get("ctx", {})

    for info in zfp.infolist():
        filename = info.filename
        if info.filename in dynamic_filename:
            tmpl = jinja2.Template(dynamic_filename[info.filename])
            filename = tmpl.render(ctx)
        opath = os.path.join(args.dest, filename)

        if info.filename.endswith("/"):
            if not os.path.exists(opath):
                os.makedirs(opath)
        else:
            if info.filename in binaries:
                with zfp.open(info, "rb") as ifp:
                    with open(opath, "wb") as ofp:
                        shutil.copyfileobj(ifp, ofp)
            else:
                with zfp.open(info, "r") as ifp:
                    tmpl = jinja2.Template(ifp.read().decode("utf-8"))
                with open(opath, "w", encoding="utf-8") as ofp:
                    ofp.write(tmpl.render(ctx))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
