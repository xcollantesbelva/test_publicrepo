"""Dummy app."""

from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

cat_facts = [
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


@app.get("/cat_fact", response_model=CatFact)
async def get_cat_fact():
    fact = random.choice(cat_facts)
    return CatFact(cat_fact=fact)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5002)
