#!/bin/bash
REPO_NAME=sampleapp-db
REPO_URL=$( aws ecr get-authorization-token  | grep Endpoint | cut -d'"' -f 4 | sed -e 's/https:\/\///' )
cmd=$( aws ecr get-login --region us-east-1 --no-include-email)
$cmd
docker build -t $REPO_NAME:latest .
docker tag $REPO_NAME:latest $REPO_URL/$REPO_NAME:latest
docker push $REPO_URL/$REPO_NAME:latest
