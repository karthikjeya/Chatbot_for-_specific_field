import os
from embedchain import App

os.environ["OPEN_API_KEY"]="paste the api key"
jk=App()
jk.add("web_page","https://en.wikipedia.org/wiki/Google")
jk.add("youtube_video","https://youtu.be/WRepw27cUMc?si=iLvjyZsG9A_jCbdB")

response=jk.query("who is founder of google")
print(response)
