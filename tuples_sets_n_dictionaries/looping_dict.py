cartoon_ratings ={
    'shinchan' : 3,
    'ninja hattori':4,
    'pokemon':5,
    'tom n jerry':5,
    'Dexters Laboratory':5,
    'Sam the fireman':4,
    'Spongebob Squarepants':5
}

for k in cartoon_ratings:
    print(k)

# for k in cartoon_ratings.keys():
#     print(k)

# get all values
for val in cartoon_ratings.values():
    print(val)

# BOTH k, v in dict
for k, v in cartoon_ratings.items():
    print(k,v)