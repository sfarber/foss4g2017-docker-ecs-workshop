#!/bin/bash
REPO_NAME=sampleapp-db
REPO_URL=015204734367.dkr.ecr.us-east-1.amazonaws.com
cmd=$( aws ecr get-login --region us-east-1 )
$cmd
docker build -t $REPO_NAME:latest .
docker tag $REPO_NAME:latest $REPO_URL/$REPO_NAME:latest
docker push $REPO_URL/$REPO_NAME:latest
