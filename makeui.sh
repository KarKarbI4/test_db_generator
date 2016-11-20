#!/bin/bash
UIDIR=ui
GENDIR=.

for UIFILE in ${UIDIR}/*.ui
do
    FILENAME=$(basename ${UIFILE} .ui)
    GENFILE=${GENDIR}/Ui_${FILENAME}.py
    pyuic5 -x ${UIFILE} -o ${GENFILE}
done