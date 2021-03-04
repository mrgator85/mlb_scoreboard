import statsapi

class BaseballData:
    def __init__(self):
        self.teams = statsapi.lookup_team("")
    
    def getTeamById(self, teamid):
        for t in self.teams:
            if(t['id'] == teamid):
                return t
    
    def getTeamByMascot(self, mascot):
        for t in self.teams:
            if(t['teamName'] == mascot):
                return t
    
    def get_linescore(self, gamePk):
        """gets a formatted linescore"""
        return statsapi.linescore(gamePk)

    def get_game_id_from_date(self, date_string, teamid):
        daysgames = statsapi.schedule(date=date_string, team=teamid)
        return daysgames[0]['game_id']
    
