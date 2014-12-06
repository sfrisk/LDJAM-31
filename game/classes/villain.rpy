init python:

    class Villain(object):
        def __init__(self, name='', bio='', sex='', hair='', eyes=''):
            self.name = name
            self.bio = bio
            self.sex = sex
            self.hair = hair
            self.eyes = eyes
            self.pronoun = self.get_pronoun()

        def get_pronoun(self):
            if self.sex == 'Male':
                return "he"
            else:
                return "she"

        def get_possessive(self):
            if self.sex == 'Male':
                return 'his'
            else:
                return 'her'
