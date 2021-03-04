from StdoutDisplay import StdoutDisplay
from BaseballData import BaseballData
import readchar
import datetime


class TerminalBaseball:
    def __init__(self):
        self.display = StdoutDisplay()
        self.date = datetime.date.today()
        self.gamedate = self.date
        self.teamid = 113 #reds
        self.bbdata = BaseballData()

        
    def getDateString(self, date):
        return date.strftime("%m/%d/%Y")

    def print_help(self):
        messages = ["Welcome to the terminal baseball.",
                    "This will allow you to see scores of your favorite teams",
                    "Usage:",
                    "h - help (This menu)",
                    "t - change teams (Default is the Cincinnati Reds)",
                    "c - current game or upcoming game",
                    "n - next game"
                    "p - previous game",
                    "s - standings for division of selected team",
                    "x - exit"
                    ]
        self.display.display_messages(messages)
    
    def run(self):
        stopped = False
        self.print_help()
        while(not stopped):
            c = readchar.readchar()
            if(c == 'x'):
                stopped = True
            if(c == 'h'):
                self.print_help()
            if(c == 'c'):
                self.gamedate = self.date
                linescore = self.bbdata.get_linescore(self.bbdata.get_game_id_from_date(self.getDateString(self.date), self.teamid))
                self.display.display_linescore(linescore)
            if(c == 'p'):
                self.gamedate -= datetime.timedelta(days=1)
                linescore = self.bbdata.get_linescore(self.bbdata.get_game_id_from_date(self.getDateString(self.gamedate), self.teamid))
                self.display.display_linescore(linescore)
            if(c == 'n'):
                self.gamedate += datetime.timedelta(days=1)
                linescore = self.bbdata.get_linescore(self.bbdata.get_game_id_from_date(self.getDateString(self.gamedate), self.teamid))
                self.display.display_linescore(linescore)

if __name__ == "__main__":
    app = TerminalBaseball()
    app.run()
    
    
            