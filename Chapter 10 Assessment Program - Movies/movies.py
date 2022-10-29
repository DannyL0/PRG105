class Movie:

    def __init__(self, title, release_year, story_year):
        self.title = title
        self.release_year = release_year
        self.story_year = story_year

    # Getters and setters
    def get_title(self):
        return self.title

    def get_release_year(self):
        return self.release_year

    def get_story_year(self):
        return self.story_year

    def set_title(self, title):
        self.title = title

    def set_release_year(self, release_year):
        self.release_year = release_year

    def set_story_year(self, story_year):
        self.story_year = story_year


def main():
    try:
        file = open('MarvelMovies.csv', 'r')
        data = file.read().splitlines()
        movie_list = []  # open list to append

        for movies in data:
            title, re_year, story_year = movies.split(",")
            movie_obj = Movie(title, re_year, story_year)  # creating an object to append into the list
            movie_list.append(movie_obj)

        movie_list.sort(key=Movie.get_title)

        print(f'{"Title":^35} {"Release":^10} {"Storyline":^10}')
        for movies in movie_list:
            print(f'{movies.get_title():<35} {movies.get_release_year():^10} {movies.get_story_year():^10}')
    except FileNotFoundError:
        print("**INVALID FILE**")


main()
