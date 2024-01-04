import requests

from bs4 import BeautifulSoup

website_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(website_url)
response.raise_for_status()

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movie_list = [movie.getText() for movie in soup.find_all(
    name = "h3",
)]

reverse_movie_list = movie_list[::-1]

with open("movie_list.txt", mode = "w") as file:
    for movie in reverse_movie_list:
        file.write(f"{movie}\n")
        
def movie_ranking():
    user_input = int(input("Position of movie: \n"))
    
    if user_input <= 100:
        print(f"The movie ranked {user_input} was: {reverse_movie_list[user_input][3:]}.")
    
    else:
        print("The movie ranking shows the greatest 100 movie.")
        print("Please choose a ranking between 1 and 100.")

movie_ranking()
    
    