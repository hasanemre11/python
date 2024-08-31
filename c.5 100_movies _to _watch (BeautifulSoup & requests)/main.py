import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(F"{URL}").text


soup = BeautifulSoup(response, "html.parser")
liste = soup.find_all(name="h3")
with open("movies.txt", 'w', encoding='utf-8') as file:
    movies = [it.get_text() for it in liste][::-1]
    for item in movies:
        file.write(str(item) + "\n")



