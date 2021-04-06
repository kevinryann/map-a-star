@echo off
cd %CD%/src/

echo.
echo =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
echo Running server...
timeout 2 > NUL
echo.
echo Click Ctrl+C and choose 'N' after choosing coordinates
echo.
python server.py

echo.
echo =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
echo Choose coordinates to be connected
echo.
echo Retrieving addresses...
echo.
python makeRoute.py

echo.
echo =+=+=+=+=+=+=+=+=+
echo Running program...
echo.
python main.py

cd ..