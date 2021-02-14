from inputOutput import takeCommand, initSpeakEngine, speak
from intentValidator import *
from executor import *
from utility import Modes

def processQuery(engine, query, curMode):
    foundIntent = False
    for isIntent, execute in COMMANDS:
        if isIntent(query):
            return execute(engine, query)

    executeUnknownCommand(engine)


COMMANDS = [(isGreetingCommand, executeGreeting), (isByeCommand, executeByeCommand), (isSelectModeCommand, executeSelectModeCommand),
            (isShowInstructionCommand, executeShowInstructionCommand)]

if __name__ == '__main__':
    engine = initSpeakEngine('female')
    curMode = Modes.Iddle

    while True:
        query = takeCommand().lower()

        if curMode != Modes.Iddle:
            curMode = processQuery(engine, query, curMode)
        else:
            if isWakeUpCommand(query):
                curMode = Modes.Waiting