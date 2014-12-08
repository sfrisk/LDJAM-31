init python:
    import random
    import copy

    class Trait(object):
        def __init__(self, name):
            self.name = name
            self.types = []

        def add_type(self, trait_type):
            self.types.append(trait_type)

        def get_trait_clue(self, name):
            for t in self.types:
                if name == t.name:
                    return t.get_rand_clue()


    class Trait_Type(object):
        def __init__(self, name):
            self.name = name
            self.clues = []

        def add_clue(self, clue):
            self.clues.append(clue)

        def get_rand_clue(self):
            return self.clues[randrange(len(self.clues))]



    character_traits = []

    hair = Trait('hair')

    hair_type = Trait_Type('Blond')
    hair_type.add_clue("hair the color of straw")
    hair_type.add_clue("hair reminded them of the road in Wizard of Oz")
    hair.add_type(copy.deepcopy(hair_type))

    hair_type = Trait_Type('Brown')
    hair_type.add_clue("hair that looked like chocolate")
    hair_type.add_clue("dark brown hair that was excellently groomed")
    hair.add_type(copy.deepcopy(hair_type))

    hair_type = Trait_Type('Red')
    hair_type.add_clue("hair looked like it would burn to touch it")
    hair_type.add_clue("flowing auborn hair")
    hair.add_type(copy.deepcopy(hair_type))

    hair_type = Trait_Type('Black')
    hair_type.add_clue("hair reflected the darkness of their deeds")
    hair_type.add_clue("hair the color of the emptyness of space")
    hair.add_type(copy.deepcopy(hair_type))

    character_traits.append(hair)

    eyes = Trait('eyes')

    eye_type = Trait_Type('Blue')
    eye_type.add_clue("beautiful baby blue eyes")
    eye_type.add_clue("eyes that reminded people of a robin egg")
    eyes.add_type(copy.deepcopy(eye_type))


    eye_type = Trait_Type('Green')
    eye_type.add_clue("eyes the color of emeralds")
    eye_type.add_clue("bright green eyes")
    eyes.add_type(copy.deepcopy(eye_type))

    eye_type = Trait_Type('Brown')
    eye_type.add_clue("eyes the color of dirt")
    eye_type.add_clue("brown puppy dog eyes")
    eyes.add_type(copy.deepcopy(eye_type))

    character_traits.append(eyes)


    skin = Trait('skin')
    skin_type = Trait_Type('Fair')
    skin_type.add_clue("a fair complexion")
    skin.add_type(copy.deepcopy(skin_type))

    skin_type = Trait_Type('Dark')
    skin_type.add_clue("a dark complextion")
    skin.add_type(copy.deepcopy(skin_type))

    character_traits.append(skin)


    def get_character_clue(f):
        trait = character_traits[randrange(len(character_traits))]
        clue = ''

        if trait.name == 'eyes':
            clue = trait.get_trait_clue(villain.eyes)

        if trait.name == 'hair':
            clue = trait.get_trait_clue(villain.hair)

        if trait.name == 'skin':
            clue = trait.get_trait_clue(villain.skin)

        if f == 40:
            clue = character_traits[0].get_trait_clue(villain.hair)
        if f == 30:
            clue = character_traits[1].get_trait_clue(villain.eyes)
        if f == 20:
            clue = character_traits[2].get_trait_clue(villain.skin)


        return clue
