reviews = ["This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

for review in reviews:
    summary = review[:30].rsplit(' ', 1)[0] + "…"
    print(summary)
