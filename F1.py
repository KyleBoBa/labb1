import csv

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

    def __str__(self):
        return f"{self.name} ({self.year}) directed by {self.director}"

    def __lt__(self, other):
        return self.year < other.year
    
    def rating_and_viewership(self):
        return self.rating * self.views

    def is_post_2020(self):
        return self.year > 2020

    def get_genre(self):
        return self.genre
    
def read_drama():
    dramas = []
    with open('kdrama.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        for line in csv_reader:
            drama = Drama(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
            dramas.append(drama)
    for drama in dramas:
        print(drama)
    return dramas

def create_object():
    drama1 = Drama("Max and Harry go adventuring", 9.7, "Max, Harry", 9.8, "Romance, Comedy, Adventure", "Kyle", "Kyle", 2023, 24, "LoLClient")
    drama2 = Drama("Max and Harry go golfing", 10, "Max, Harry", 13.7, "Romance, Comedy", "Kyle", "Kyle", 2025, 24, "LoLClient")
    
    print(drama1)
    print(drama2)
    print("Drama 1 is newer than Drama 2:", drama1 > drama2)
    print("Drama 1 Rating * Viewership:", drama1.rating_and_viewership())
    print("Drama 2 Genre:", drama2.get_genre())
    print("Is Drama 1 post 2020?", drama1.is_post_2020())

def list_search(dramas):
    print("\nDramas streamade på Disney+:")
    for drama in dramas:
        if drama.network == "Disney+":
            print(drama.name)

def main():
    dramas = read_drama()
    print("\nNya objekt:")
    create_object()
    list_search(dramas)

if __name__ == "__main__":
    main()