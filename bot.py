from rubpy import Client 
from os import system 
url = input("Enter Your Link: ") 
regex = url[15:] 
system(f"wget {url} && mv ./{regex} ./FreeTube.mp4") 
app = Client("xdiwehhjsizxtgawudacczfqoegmcjyc") 
async def send(app): 
    await app.sendFile("c0BTbEE06bf77d2a9635c01bcaf13afc","FreeTube.mp4","مربوط به پست بالا 👆") 
app.run(send)
