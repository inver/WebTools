# curl 'https://www.thingiverse.com/api/things' \
#   --compressed \
#   -X POST \
#   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: en-US,en;q=0.5' \
#   -H 'Accept-Encoding: gzip, deflate, br, zstd' \
#   -H 'Content-Type: application/json' \
#   -H 'Origin: https://www.thingiverse.com' \
#   -H 'Connection: keep-alive' \
#   -H 'Referer: https://www.thingiverse.com/thing:0/edit' \
#   -H 'Cookie: CookieConsent={stamp:%275XvNCDJGCujZq3P+mpjU/gKpkCZau9OYdHlZohdrljwkFbdlC+p4Qw==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:3%2Cutc:1750423015309%2Cregion:%27ru%27}; _cfuvid=PsVNxikjShzfzYjX6AllqFEWpNCbyExT5oMaa2kp39Y-1754592772358-0.0.1.1-604800000; PHPSESSID=93d4f6677ae916071dd10ae9e612290e; previous_url=%2F; _dd_s=logs=0^&expire=1755029933267; thingitoken=5090241172773cfb12c2e4e5717a44342d771f79c3cd20ea087d78a62ff0d6bd847086f1e82956e3bb528865a3a4c08e03b68c740ea936c404666c7955eea2f8dfd434347f0c322ad9d01d904da5586f669a579ba28e840e3b8449a661b5ab6bed703ce9b2216a250fdb36d1f86da14f1ca6906669778754bd6f743efc8e547; EA_SESSION_SAMPLED=true; EA_UID=25ad5335-10aa-4292-9bdd-899bccbbde6b; EA_SID=c8c35728-50bc-48a5-8fde-70f4795628a5' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Priority: u=0' \
#   -H 'Pragma: no-cache' \
#   -H 'Cache-Control: no-cache' \
#   -H 'TE: trailers' \
#   --data-raw $'{"name":"OpenZ 1x24 wheel","category":155,"files":[{"id":43705195,"type":"pending"},{"id":43705196,"type":"pending"}],"images":[],"description":"\u0426heel for openz project in 1x24 scale","is_customizer":false,"is_wip":true,"is_ai":false,"tags":["openz"],"license":"cc-sa","thing_groups":[],"thing_programs":[46],"is_remix":false,"ancestors":[],"details_parts":[{"type":"summary","data":[{"content":"\u0426heel for openz project in 1x24 scale"}]},{"type":"settings"},{"type":"tips"},{"type":"design"},{"type":"custom"}],"included_apps":[],"is_edu":false,"education":{"grades":[],"subjects":[],"standards":[]},"edu_details_parts":[{"type":"skills"},{"type":"duration"},{"type":"overview"},{"type":"plan"},{"type":"materials"},{"type":"prep"},{"type":"assessment"},{"type":"references"},{"type":"grades"},{"type":"subjects"},{"type":"standards"}]}'

# curl 'https://www.thingiverse.com/api/files/0/FinalizeFiles' \
#   -X POST \
#   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0' \
#   -H 'Accept: */*' \
#   -H 'Accept-Language: en-US,en;q=0.5' \
#   -H 'Accept-Encoding: gzip, deflate, br, zstd' \
#   -H 'Content-Type: application/json' \
#   -H 'Origin: https://www.thingiverse.com' \
#   -H 'Connection: keep-alive' \
#   -H 'Referer: https://www.thingiverse.com/thing:0/edit' \
#   -H 'Cookie: CookieConsent={stamp:%275XvNCDJGCujZq3P+mpjU/gKpkCZau9OYdHlZohdrljwkFbdlC+p4Qw==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:3%2Cutc:1750423015309%2Cregion:%27ru%27}; _cfuvid=PsVNxikjShzfzYjX6AllqFEWpNCbyExT5oMaa2kp39Y-1754592772358-0.0.1.1-604800000; PHPSESSID=93d4f6677ae916071dd10ae9e612290e; previous_url=%2F; _dd_s=logs=0^&expire=1755029933267; thingitoken=5090241172773cfb12c2e4e5717a44342d771f79c3cd20ea087d78a62ff0d6bd847086f1e82956e3bb528865a3a4c08e03b68c740ea936c404666c7955eea2f8dfd434347f0c322ad9d01d904da5586f669a579ba28e840e3b8449a661b5ab6bed703ce9b2216a250fdb36d1f86da14f1ca6906669778754bd6f743efc8e547; EA_SESSION_SAMPLED=true; EA_UID=25ad5335-10aa-4292-9bdd-899bccbbde6b; EA_SID=c8c35728-50bc-48a5-8fde-70f4795628a5' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Pragma: no-cache' \
#   -H 'Cache-Control: no-cache' \
#   -H 'TE: trailers' \
#   --data-raw '{"target_id":7116538,"target_type":"thing","pending_uploads":[{"id":43705195,"rank":0},{"id":43705196,"rank":1}]}'

from __future__ import print_function

import os

import Draft
import FreeCAD
from PySide import QtCore, QtGui

if FreeCAD.GuiUp:
    import FreeCADGui
    from DraftTools import translate
    from PySide.QtCore import QT_TRANSLATE_NOOP
else:
    # \cond
    def translate(ctxt, txt):
        return txt


    def QT_TRANSLATE_NOOP(ctxt, txt):
        return txt
    # \endcond

__title__ = "Thingiverse uploader"
__author__ = "Alexey Nevinsky"
__url__ = "http://www.freecadweb.org"


class CommandThingiverse:
    """the WebTools_Thingiverse command definition"""

    def GetResources(self):
        return {'Pixmap': os.path.join(os.path.dirname(__file__), "icons", 'thingiverse.svg'),
                'MenuText': QtCore.QT_TRANSLATE_NOOP("WebTools_Thingiverse", "Thingiverse"),
                'ToolTip': QtCore.QT_TRANSLATE_NOOP("WebTools_Thingiverse", "Upload models to thingiverse")}

    def Activated(self):
        if not FreeCAD.ActiveDocument or not hasattr(FreeCAD.ActiveDocument, "FileName"):
            FreeCAD.Console.PrintError(
                translate("WebTools", "No document opened. Please open or create a document first.") + "\n")
            return
        try:
            import requests
        except:
            FreeCAD.Console.PrintError(
                translate("WebTools", "requests python module not found, aborting. Please install python-requests\n"))
            return
        try:
            import json
        except:
            FreeCAD.Console.PrintError(
                translate("WebTools", "json python module not found, aborting. Please install python-json\n"))
        else:
            FreeCADGui.Control.showDialog(ThingiverseTaskPanel())


class ThingiverseTaskPanel:
    """The TaskPanel for the Git command"""

    def __init__(self):
        self.form = FreeCADGui.PySideUic.loadUi(os.path.join(os.path.dirname(__file__), "ui", "TaskThingiverse.ui"))
        self.form.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "icons", "thingiverse.svg")))
        self.form.labelStatus.setText("")


if FreeCAD.GuiUp:
    FreeCADGui.addCommand('WebTools_Thingiverse', CommandThingiverse())
