#!/bin/bash
pip3 install virtualenv

if [[ ! -d "docksrv" ]];
then
    virtualenv docksrv
fi
source docksrv/bin/activate
pip3 install fastapi uvicorn
pip3 install docker

uvicorn main:app --reload
 

