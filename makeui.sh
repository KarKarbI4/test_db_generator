#!/bin/bash
for UIFILE in *.ui
do
    FILENAME=$(basename ${UIFILE} .ui)
    pyuic5 -x ${UIFILE} -o Ui_${FILENAME}.py
done