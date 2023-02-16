import challonge

challonge.set_credentials("romn2112", "zVcOJxFklUGothNCFi4mcWjRa0k7xDs7kLyQMFT4")

singles2022 = challonge.tournaments.show('uvadrumlinesingles2022')
doubles2022 = challonge.tournaments.show('uva')

players_singles = challonge.participants.index(singles2022['id'])