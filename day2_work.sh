#!/bin/bash

echo "Creating project structure"
mkdir -p project/{src,docs,scripts,backup}

echo "Creating files"
touch project/src/main.c
touch project/src/helper.c
touch project/docs/readme.txt
touch project/scripts/run.sh

echo "Adding content to README"
echo "Linux Mission Impossible" > project/docs/readme.txt

echo "Copying readme"
cp project/docs/redme.txt project/backup/

echo "Moving helper.c"
mv project/src/helper.c project/backup/

echo "Renaming main.c to app.c"
mv project/src/main.c project/src/app.c

echo "Searching for app.c"
find project -name "app.c"

echo "Giving execute permission"
chmod +x project/scripts/run.sh

echo "Creating archive"
tar -czvf project.tar.gz project

echo "Extracting archive"
mkdir recovered_project
tar -xzvf project.tar.gz -C recovered_Project

echo "Final Structure:"
find recovered_project

