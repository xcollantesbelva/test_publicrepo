"""Dummy app."""

from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

import datetime
import random

app = FastAPI()

cat_facts = [
    "See cats: https://www.youtube.com/watch?v=VZrDxD0Za9I",
    "Cat video: https://www.youtube.com/watch?v=VZrDxD0Za9I",
    "Super funny video: https://www.youtube.com/watch?v=VZrDxD0Za9I",
    "Cats sleep 70% of their lives.",
    "A group of cats is called a clowder.",
    "Cats have five toes on their front paws, but only four toes on their back paws.",
    "The world's largest cat measured 48.5 inches long.",
    "Cats have whiskers on the backs of their front legs as well.",
    "A house cat can run to the speed of about 30 mph over short distances.",
    "Cats can make over 100 different sounds.",
    "The first cat in space was a French cat named Felicette (a.k.a. 'Astrocat') in 1963.",
    "Cats' claws all curve downward, which means that they can't climb down trees head-first.",
    "Each cat's nose print is unique, much like a human fingerprint.",
]


class CatFact(BaseModel):
    cat_fact: str


@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <h2>App created from public repo: <a href='https://github.com/xcollantesbelva/test_publicrepo'>https://github.com/xcollantesbelva/test_publicrepo</a></h2>
    <iframe width="860" height="515" src="https://www.youtube.com/embed/VZrDxD0Za9I?si=SqlyK4N3x_3TDQzE"
        title="YouTube video player" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write;
        encrypted-media; gyroscope; picture-in-picture;
        web-share" referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen>
    </iframe>
    """


@app.get("/cat_fact", response_model=CatFact)
async def get_cat_fact(req: Request):
    print(req.headers)
    fact = random.choice(cat_facts)
    return CatFact(cat_fact=fact)


if __name__ == "__main__":
    import uvicorn

    print(datetime.datetime.now())
    uvicorn.run(app, host="0.0.0.0", port=5002)
