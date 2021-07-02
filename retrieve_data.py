import wikipedia
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib.parse
import random


teams = [
    # {
    #     "team": "Czech Republic",
    #     "players": {
    #         "goalkeepers": ["Ales Mandous", "Jiri Pavlenka", "Tomas Vaclik"],
    #         "defenders": ["Jan Boril", "Jakub Brabec", "Ondrej Celustka"," Vladimir Coufal",
    #                       "Pavel Kaderabek", "Tomas Kalas", "Ales Mateju", "David Zima"],
    #         "midfielders": ["Tomas Holes", "Antonin Barak", "Vladimir Darida", "Jakub Jankto", "Alex Kral",
    #                         "Lukas Masopust", "Jakub Pesek", "Michal Sadilek",
    #                         "Petr Sevcik", "Tomas Soucek", "Adam Hlozek"],
    #         "forwards": ["Michael Krmencik", "Tomas Pekhart", "Patrik Schick", "Matej Vydra"]
    #     }
    # },
    # {
    #     'team': 'France',
    #     "players": {
    #         "goalkeepers": ["Hugo Lloris", "Mike Maignan", "Steve Mandanda"],
    #         "defenders": ["Lucas Digne", "Léo Dubois", "Lucas Hernandez", "Presnel Kimpembe", "Jules Koundé",
    #                       "Clément Lenglet", "Benjamin Pavard", "Raphaël Varane", "Kurt Zouma"],
    #         "midfielders": ["Golo Kanté", "Thomas Lemar", "Paul Pogba", "Adrien Rabiot", "Moussa Sissoko",
    #                         "Corentin Tolisso"],
    #         "forwards": ["Kingsley Coman", "Wissam Ben Yedder", "Karim Benzema", "Ousmane Dembélé", "Olivier Giroud",
    #                      "Antoine Griezmann", "Kylian Mbappé", "Marcus Thuram"]
    #     }
    # },
    # {
    #     'team': 'Switzerland',
    #     "players": {
    #         "goalkeepers": ["Yann Sommer", "Yvon Mvogo", "Jonas Omlin"],
    #         "defenders": ["Manuel Akanji", "Loris Benito", "Eray Cömert", "Nico Elvedi", "Jordan Lotomba",
    #                       "Kevin Mbabu", "Becir Omeragic", "Ricardo Rodríguez", "Fabian Schär", "Silvan Widmer"],
    #         "midfielders": ["Christian Fassnacht", "Edimilson Fernandes", "Remo Freuler", "Admir Mehmedi",
    #                         "Xherdan Shaqiri", "Djibril Sow", "Ruben Vargas", "Granit Xhaka", "Denis Zakaria",
    #                         "Steven Zuber"],
    #         "forwards": ["Breel Embolo", "Mario Gavranović", "Haris Seferovic"]
    #     }
    # },
    # {
    #     "team": "Sweden",
    #     "players": {
    #         "goalkeepers": ["Karl-Johan Johnsson", "Kristoffer Nordfeldt", "Robin Olsen"],
    #         "defenders": ["Ludwig Augustinsson", "Marcus Danielson", "Andreas Granqvist", "Filip Helander",
    #                       "Pontus Jansson", "Emil Krafth", "Mikael Lustig", "Victor Lindelöf", "Pierre Bengtsson"],
    #         "midfielders": ["Jens Cajuste", "Albin Ekdal", "Emil Forsberg", "Dejan Kulusevski", "Sebastian Larsson",
    #                         "Kristoffer Olsson", "Mattias Svanberg", "Gustav Svensson"],
    #         "forwards": ["Marcus Berg", "Viktor Claesson", "Alexander Isak",
    #                      "Jordan Larsson", "Robin Quaison", "Ken Sema"]
    #     }
    # },
    # {
    #     "team": "Ukraine",
    #     "players": {
    #         "goalkeepers": ["Georgiy Bushchan", "Andriy Pyatov", "Anatolii Trubin"],
    #         "defenders": ["Oleksandr Karavaev", "Serhiy Kryvtsov", "Mykola Matviyenko", "Vitaliy Mykolenko",
    #                       "Denys Popov", "Eduard Sobol", "Oleksandr Tymchyk", "Illia Zabarnyi"],
    #         "midfielders": ["Oleksandr Zinchenko", "Roman Bezus", "Yevhen Makarenko", "Ruslan Malinovskyi",
    #                         "Marlos", "Mykola Shaparenko", "Taras Stepanenko", "Heorhii Sudakov", "Serhiy Sydorchuk",
    #                         "Viktor Tsygankov", "Andriy Yarmolenko", "Oleksandr Zubkov"],
    #         "forwards": ["Artem Besedin", "Artem Dovbyk", "Roman Yaremchuk"]
    #     }
    # },
    # {
    #     "team": "Spain",
    #     "players": {
    #         "goalkeepers": ["David de Gea", "Unai Simón", "Robert Sánchez"],
    #         "defenders": ["José Gayà", "Jordi Alba", "Pau Torres", "Aymeric Laporte", "Eric García", "Diego Llorente",
    #                       "César Azpilicueta", "Marcos Llorente"],
    #         "midfielders": ["Thiago Alcântara", "Sergio Busquets", "Koke", "Dani Olmo", "Rodri",
    #                         "Fabián Ruiz", "Pedri"],
    #         "forwards": ["Pablo Sarabia", "Ferran Torres", "Adama Traoré", "Álvaro Morata", "Gerard Moreno",
    #                      "Mikel Oyarzabal"]
    #     }
    # },
    # {
    #     "team": "England",
    #     "players": {
    #         "goalkeepers": ["Aaron Ramsdale", "Sam Johnstone", "Jordan Pickford"],
    #         "defenders": ["Ben Chilwell", "Conor Coady", "Reece James", "Harry Maguire", "Tyrone Mings",
    #                       "Luke Shaw", "John Stones", "Kieran Trippier", "Kyle Walker", "Ben White"],
    #         "midfielders": ["Jude Bellingham", "Phil Foden", "Jack Grealish", "Jordan Henderson", "Mason Mount",
    #                         "Kalvin Phillips", "Declan Rice", "Bukayo Saka", "Jadon Sancho"],
    #         "forwards": ["Dominic Calvert-Lewin", "Harry Kane", "Marcus Rashford", "Raheem Sterling"]
    #     }
    # },
    # {
    #     "team": "Denmark",
    #     "players": {
    #         "goalkeepers": ["Kasper Schmeichel", "Jonas Lössl", "Frederik Rønnow"],
    #         "defenders": ["Jens Stryger Larsen", "Simon Kjær", "Andreas Christensen", "Joachim Andersen", "Daniel Wass",
    #                       "Mathias Jørgensen", "Joakim Mæhle", "Jannik Vestergaard", "Nicolai Boilesen"],
    #         "midfielders": ["Mathias Jensen", "Christian Nørgaard", "Pierre-Emile Højbjerg", "Thomas Delaney",
    #                         "Anders Christiansen", "Christian Eriksen", "Mikkel Damsgaard", "Robert Skov"],
    #         "forwards": ["Martin Braithwaite", "Andreas Cornelius", "Andreas Skov Olsen", "Yussuf Poulsen",
    #                      "Kasper Dolberg", "Jonas Wind"]
    #     }
    # },
    # {
    #     "team": "Belgium",
    #     "players": {
    #         "goalkeepers": ["Thibaut Courtois", "Simon Mignolet", "Matz Sels"],
    #         "defenders": ["Toby Alderweireld", "Dedryck Boyata", "Jason Denayer", "Thomas Vermaelen",
    #                       "Jan Vertonghen", "Timothy Castagne", "Thomas Meunier"],
    #         "midfielders": ["Kevin De Bruyne", "Leander Dendoncker", "Dennis Praet",
    #                         "Youri Tielemans", "Hans Vanaken", "Axel Witsel"],
    #         "forwards": ["Nacer Chadli", "Yannick Carrasco", "Thorgan Hazard", "Michy Batshuayi",
    #                      "Christian Benteke", "Jérémy Doku", "Eden Hazard", "Romelu Lukaku",
    #                      "Dries Mertens", "Leandro Trossard"]
    #     }
    #
    # },
    {
        "team": "Italy",
        "players": {
            "goalkeepers": ["Gianluigi Donnarumma", "Salvatore Sirigu", "Alex Meret"],
            "defenders": ["Francesco Acerbi", "Alessandro Bastoni", "Leonardo Bonucci", "Giorgio Chiellini",
                          "Giovanni Di Lorenzo", "Alessandro Florenzi", "Leonardo Spinazzola", "Rafael Tolói",
                          "Emerson Palmieri"],
            "midfielders": ["Nicolò Barella", "Bryan Cristante", "Jorginho", "Manuel Locatelli", "Gaetano Castrovilli",
                            "Matteo Pessina", "Marco Verratti"],
            "forwards": ["Andrea Belotti", "Domenico Berardi", "Federico Bernardeschi", "Federico Chiesa",
                         "Ciro Immobile", "Giacomo Raspadori"]
        }
    }

]
players = []
for team in teams:
    for key, values in team['players'].items():
        for value in values:
            time.sleep(random.randint(3, 7))
            age_started_senior_career = None
            age_started_youth_career = None
            print(value)
            result = wikipedia.search(value, results=1)
            print(result)
            # content = wikipedia.page(result).html()
            # soup = BeautifulSoup(content, 'lxml')
            # table = soup.find('table', {'class': 'infobox vcard'})
            # print(table)

            processed_name = urllib.parse.quote(result[0])
            # processed_name = processed_name.encode('utf-8').decode('ascii')
            url = "https://en.wikipedia.org/wiki/"+processed_name
            print(url)
            try:
                table = pd.read_html(url, header=0)[0]

                print(table.columns)
                print(table)
                table.columns = [0, 1, 2, 3]
            except ValueError:
                continue
            if not table.empty:

                age_row_index = table.index[table[0] == 'Date of birth'].to_list()[0]
                age_row = table.iloc[age_row_index]
                print(age_row)

                if __name__ == '__main__':
                    age_value = age_row[1].replace('(', '').replace(')', '').\
                        replace('[2]', '').replace('[1]', '').replace('[3]', '')

                age = [int(s) for s in age_value.split() if s.isdigit()][0]
                print(age)

                senior_career = None
                try:
                    senior_career_index = table.index[
                        table[0].str.lower().str.contains('senior career', na=False)
                    ].to_list()[0]
                    senior_career = table.iloc[senior_career_index+2][0]

                    print(senior_career)
                    # print(senior_career[0])
                    # senior_career_start = int(senior_career[0].split('–')[0].replace('-', ''))
                    # print(senior_career_start)
                    # if senior_career_start:
                    #     age_started_senior_career = age - (2021 - senior_career_start)

                except Exception:
                    pass

                youth_career = None
                had_youth_career = False
                youth_career_index = table.index[table[0].str.lower().str.contains('youth career', na=False)].to_list()
                print("youth_career_index list", youth_career_index)
                if youth_career_index:
                    had_youth_career = True
                    print("table", table.iloc[youth_career_index[0]:senior_career_index])
                    youth_career = str(table.iloc[youth_career_index[0] + 1][0])
                    # youth_career = youth_career.replace('–', ' ')

                    if not youth_career.isdigit():
                        youth_career = youth_career.split('-')[0]

                    print('youth', youth_career)
                    if 'nan' in youth_career:
                        youth_career_next_row = str(table.iloc[youth_career_index[0] + 2][0])
                        if 'senior' not in youth_career_next_row.lower():
                            youth_career = youth_career_next_row
                        print('youth next row', youth_career)
                player_data = {
                    'team': team['team'],
                    'name': value,
                    'age': age,
                    'senior_career': senior_career,
                    'youth_career': youth_career,
                    'had_youth_career': had_youth_career
                }
                players.append(player_data)

players_df = pd.DataFrame(players)
players_df.to_csv('data/Italy.csv', index=False)
