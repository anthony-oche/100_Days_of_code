from bs4 import BeautifulSoup
import requests

# response = requests.get(url="https://news.ycombinator.com/")
# hacker_web = response.text

# soup = BeautifulSoup(hacker_web, "html.parser")

# article_text = soup.find(name="span", class_="titleline")
# article_link = soup.select_one(selector=".titleline a").get("href")
# upvote = soup.select_one(selector=".score").getText()

# print(article_text)
# print(article_link)
# print(upvote)

#100 Movies of all time
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movie_list = soup.find_all(name="h3", class_="title")

movie = [item.getText() for item in movie_list[::-1]]

with open("movie.txt", "w", encoding="utf-8") as f:
    for item in movie:
        f.write(item + "\n")



















# with open("website.html") as file:
#     content = file.read()
#
#
# soup = BeautifulSoup(content, "html.parser")
#
# h3_heading = soup.find_all("h3")
# print(h3_heading)
#
# headings = soup.select(".heading")
# print(headings)
#
# name = soup.select_one(".heading")
# print(name)
#
# class_is = soup.find_all(class_="heading")
# print(class_is)

#select_one gives you the first matching tag in the body while select will select every tag
company_url = soup.select_one(selector="p a")

#using the select method to select items in web scraping we have to use the CSS way of selecting
