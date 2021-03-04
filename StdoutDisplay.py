from BaseballDisplayInterface import BaseballDisplayInterface

class StdoutDisplay(BaseballDisplayInterface):
    def display_linescore(self, linescore):
        print(linescore)
    
    def display_standings(self, standings):
        print(standings)

    def display_messages(self, messages):
        for m in messages:
            print(m)
            
    def display_message(self, message):
        print(message)