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
    
    def distribute(self, network):
        if network == "Disney+":
            return self.network
    
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

def main():
    read_drama()
main()