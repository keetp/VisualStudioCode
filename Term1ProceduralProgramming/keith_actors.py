# program contains a dictionary with the names of actors and the movies they acted in. Program will print the actors and
# movies in sentence form. was ben affleck in the dark knight? i can't remember

def main():
    # dictionary containing actor names as keys and the movies they acted in as values
    actor_dict = {'Matt Damon': 'Good Will Hunting', 'Sandra Bullock': 'While You Were Sleeping',
                  'Anthony Hopkins': 'Silence of the Lambs', 'Julia Roberts': 'Pretty Woman',
                  'Samuel L. Jackson': 'Patriot Games', 'Johnny Depp': 'Pirate of the Caribbean',
                  'Ben Affleck': 'Dark Knight', 'Clint Eastwood': 'Dirty Harry', 'Brad Pitt': 'Fight Club',
                  'Morgan Freeman': 'Shawshank Redemption'}
    # for each key-value pair in the dictionary
    for key, value in actor_dict.items():
        # printing the key acted in value, which will be formatted to ACTOR acted in MOVIE
        print(key, 'acted in', value)


main()
