# Section 12: List comprehension


stop_words = "I love and to".split(" ")
txt = "I love AI and listen to music"

out = [word for word in txt.split(" ") if word not in stop_words]
print(out)
