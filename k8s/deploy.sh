#!/bin/bash

NAME=flaskservice
LS=`helm ls $NAME`
if [ -z "$LS" ]; then
   helm install --name $NAME .

else
   helm upgrade $NAME .
   helm list $NAME
fi
