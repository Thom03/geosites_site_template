#!/usr/bin/env bash

DOMAIN=$1
SITE_ID=$2
SITE_ID=$3


# update project name everywhere and working directory

find . -type f ! -name setup.sh -exec sed -i "s/{{ domain }}/$DOMAIN/g" {} +
find . -type f ! -name setup.sh -exec sed -i "s/{{ site_id }}/$SITE_ID/g" {} +
find . -type f ! -name setup.sh -exec sed -i "s/{{ project_n }}/$SITE_ID/g" {} +



