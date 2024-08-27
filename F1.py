#DD1326 Laboration 1
#Labbgrupp: Kyle Boström och Roberto Fernandez
#Startdatum: 2024-08-26
#Redovisningsdatum: 2024-08-28

import csv

#klass drama med olika attribut
class Drama:
    def __init__(self, name, rating, actors, views, genre, director, writer, year, episodes, network):
        self.name = name
        self.rating = float(rating)
        self.actors = actors
        self.views = float(views)
        self.genre = genre
        self.director = director
        self.writer = writer
        self.year = int(year)
        self.episodes = int(episodes)
        self.network = network
#metod för utskrift av objekt i sträng
    def __str__(self):
        return f"{self.name} ({self.year}) directed by {self.director}"

#metod som jämför dramaserier på året, returnerar true om serien är äldre än andra objekt
    def __lt__(self, other):
        return self.year < other.year

#metod som multiplicerar tittarsiffror med betygsättningen
    def rating_and_viewership(self):
        return self.rating * self.views

#metod som kollar ifall serien släpptes efter år 2020
    def is_post_2020(self):
        return self.year > 2020

#metod som visar genre
    def get_genre(self):
        return self.genre

#funktion taget från Linda frö exempel, står i uppgiftsbeskrivning okej att använda
#funktionen läser en csv fil
def read_drama():
    #listan dramas skapas
    dramas = []
    with open('kdrama.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        #allting i csv fil läggs till i de attributer som skapades ovan
        for line in csv_reader:
            drama = Drama(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
            dramas.append(drama)
    #listan skrivs ut
    for drama in dramas:
        print(drama)
    return dramas

#funktion som skapar två nya objekt och jämför dem med metoderna i klass
def create_object():
    drama1 = Drama("Max and Harry go adventuring", 9.7, "Max, Harry", 9.8, "Romance, Comedy, Adventure", "Kyle", "Kyle", 2023, 24, "LoLClient")
    drama2 = Drama("Max and Harry go golfing", 10, "Max, Harry", 13.7, "Romance, Comedy", "Kyle", "Kyle", 2025, 24, "LoLClient")
    
    print(drama1)
    print(drama2)
    print("Drama 1 är nyare än Drama 2:", drama1 > drama2)
    print("Drama 1 rating * view:", drama1.rating_and_viewership())
    print("Drama 2 Genre:", drama2.get_genre())
    print("Är Drama 1 post 2020?", drama1.is_post_2020())

#funktion som söker efter dramaserier som finns endast på Disney+
def list_search(dramas):
    print("\nDramas streamade på Disney+:")
    for drama in dramas:
        if drama.network == "Disney+":
            print(drama.name)

#funktion som kör allting, huvudfunktionen i princip, andra funktioner anropas här
def main():
    dramas = read_drama()
    print("\nNya objekt:")
    create_object()
    list_search(dramas)

#Kyle får förklara vad det här är, jag brukar bara använda main()
if __name__ == "__main__":
    main()