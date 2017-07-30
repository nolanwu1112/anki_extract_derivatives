# -*- coding: utf-8 -*-

from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *

def changeDef():
    # Obtaining cards ids by searching
    # ids_def1 = mw.col.findCards('mid:1496356407592 "def1:*:*" def1e: card:def1 vocab:abandon')
    ids_def1 = mw.col.findCards('mid:1496356407592 def1:"*:*" def1e: card:def1')
    ids_def2 = mw.col.findCards('mid:1496356407592 def2:"*:*" def2e: card:def1')
    ids_def3 = mw.col.findCards('mid:1496356407592 def3:"*:*" def3e: card:def1')
    ids_def4 = mw.col.findCards('mid:1496356407592 def4:"*:*" def4e: card:def1')
    ids_def5 = mw.col.findCards('mid:1496356407592 def5:"*:*" def5e: card:def1')

    # Putting search results in a list for recurring operation
    ids_list = [ids_def1, ids_def2, ids_def3, ids_def4, ids_def5]

    # Setting up counter to tract results
    count1, count2, count3, count4, count5 = 0, 0, 0, 0, 0
    count_list = [count1, count2, count3, count4, count5]

    # Main section
    # first try for def1
    # access card, load content in def1, search for colon, reassign def1 and def1e
    def sepDef(unchanged_def):
        # make sure it is a string
        unchanged_def = unchanged_def.encode("utf-8")
        col_index = unchanged_def.find(":")
        return unchanged_def[:col_index+1], unchanged_def[col_index+1:]

    for num, ids in enumerate(ids_list, start=1):
        for id in ids:
            card = mw.col.getCard(id)
            note = card.note()
            org_def = note["def"+str(num)]
            showInfo(org_def)
            showInfo("def"+str(num))
            def1, def1e = sepDef(org_def)
            note["def"+str(num)] = def1.decode('utf-8')
            note["def"+str(num)+"e"] = def1e.decode('utf-8')
            note.flush()
            count_list[num-1] =  count_list[num-1] + 1

    # resetting the database after change
    mw.reset()

    #  displaying how many records have been fixed.
    showInfo("def Change completed\n" +
    	"def1: " + str(count1) + " " + str(len(ids_def1)) + "\n"
        "def2: " + str(count2) + " " + str(len(ids_def2)) + "\n"
        "def3: " + str(count3) + " " + str(len(ids_def3)) + "\n"
        "def4: " + str(count4) + " " + str(len(ids_def4)) + "\n"
        "def5: " + str(count5) + " " + str(len(ids_def5)) + "\n"
        )

# Tag action
action = QAction("Organizing_definition", mw)
action.triggered.connect(changeDef)
mw.form.menuTools.addAction(action)

