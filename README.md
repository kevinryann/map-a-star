# Map A Star (Map A*)
> This project uses A-star (A*) algorithm to calculate the nearest distance between two points given certain routes in a map, giving the outlook of how digital maps generally calculate and construct a path between two points.

## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [How to Use](#how-to-use)
* [Features](#features)
* [Author](#author)

## Technologies
* Python 3
* Flask
* Plotly
* Geopy

## Setup
1. If you are using a virtual environment, open terminal and activate your virtual environment
2. Make sure you have installed the requirements. If you haven't, run your terminal, go to the directory of this program and type in `pip install -r src/requirements.txt'

## How to Use
### Run Using Windows Batch File
1. If you are using virtual environment, activate it beforehand through terminal
2. Go to bin directory
`cd bin`
3. Execute batch file (run.bat) and a web page will open
`run.bat`
4. Click anywhere on the map to get the latitude and longitude of the clicked point. The points clicked will be added to coordinates.txt located in src/coordinate/. These points will later be used for input
5. Press Ctrl + C in terminal and type in "N" to continue the program
6. Now is the time to build the adjacency matrix. This matrix represents the existence of route between two points. If you wanted to "build" a route between the first coordinate and third coordinate, type in "1 3". To stop building, type in "-99"
7. If you have finished building adjacency matrix, choose number 1 and the program will ask you to input start point and end point. Type in the index of the coordinates
8. Choose to visualize the connected graph or the path from start point to end point
9. The program will automatically open your browser to visualize

### Run Manually
*If you have prepares the test case(s), do number 1 and jump to number 7*
1. Go to src directory
`cd src`
2. Run server.py and make sure localhost address matches the one on your browser. If it doesn't, type in the address manually
`python server.py`
or
`python3 server.py`
3. Click anywhere on the map to get the latitude and longitude of the clicked point. The points clicked will be added to coordinates.txt located in src/coordinate/. These points will later be used for input.
4. Press Ctrl + C in terminal
5. Run makeRoute.py
`python makeRoute.py`
or
`python3 makeRoute.py`
6. Now is the time to build the adjacency matrix. This matrix represents the existence of route between two points. If you wanted to "build" a route between the first coordinate and third coordinate, type in "1 3". To stop building, type in "-99"
7. Run main.py
`python main.py`
or
`python3 main.py`
8. The program will ask which method will you use for the coordinates and ask you to input start point and end point. Type in the index of the coordinates.
9. Choose to visualize the connected graph or the path from start point to end point
10. The program will automatically open your browser to visualize

### Input Format in File
```(N numbers of nodes)
(x1, y1)
(x2, y2)
.
.
.
(xn, yn)
(adjacency matrix)
```
*if unclear, refer to test directory*

## Features
* This program uses OpenLayers API, which allows you to get the latitude and longitude of a point by clicking on the map.
* This program is equipped with tool to build adjacency matrix

## Author
Created by 
* [@kevinryann](https://www.github.com/kevinryann)
* [@cyn-rus](https://www.github.com/cyn-rus)