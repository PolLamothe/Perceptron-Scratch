import snakeGame
import json

with open('./data/game.json', 'r') as fichier:
    jsonData = json.load(fichier)

grid = None

gameIndex = 0
gridIndex = 0

iterationAvaible = []

for i in range(len(jsonData)):
    iterationAvaible.append(jsonData[i]["iteration"])

def updateData():
    global gridIndex
    gridIndex += 1
    try:
        ui.grid = jsonData[gameIndex]["data"][gridIndex]
    except IndexError:
        return "GameOver"
    
def replayData():
    global gridIndex
    gridIndex = 0
    ui.grid = jsonData[gameIndex]["data"][gridIndex]

def iterationChoosed(iteration : int):
    global ui
    global gameIndex
    for i in range(len(jsonData)):
        if(jsonData[i]["iteration"] == iteration):
            gameIndex = i
    ui.startGame(jsonData[gameIndex]["data"][gridIndex])

ui = snakeGame.UI(5,updateGrid=updateData,replayGame=replayData)
ui.startChoosingMenu(iterationAvaible,iterationChoosed)