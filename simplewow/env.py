import random

class Arena(object):
    """Basic structure of the game environment.

    """
    def __init__(self, char1, char2):
        self.char1 = char1
        self.char2 = char2
        self.frames_elapsed = 0
        self.state_space = {}

    def duel(self, agent1, agent2='random'):
        """The user passes how actions are to be decided. The choices are:
        - 'player'
        - 'random'
        - 'func-approx'

        Arguments:
            agent1 {str} -- The method for actions to be decided.

        Keyword Arguments:
            agent2 {str} -- The method for actions to be
            decided. (default: {'random'})
        """
        while self.char1.hp > 0 and self.char2.hp > 0:
            if not self.char1.busy:
                if agent1 is 'player':
                    print('Your available actions are: ')
                    for a in range(len(self.char1.actions)):
                        print('{} - {}'.format(a, self.char1.actions[a]))
                    action_idx = input('Enter the number of the ability you choose: ')
                    c1_action = self.char1.actions[int(action_idx)]
                    c1_action(self.char2)
                elif agent1 is 'func-approx':
                    pass
                else:
                    c1_action = random.choice(self.char1.actions)
                    c1_action(self.char2)
            if self.char2.hp <= 0:
                break
            if not self.char2.busy:
                if agent2 is 'func-approx':
                    pass
                else:
                    c2_action = random.choice(self.char2.actions)
                    c2_action(self.char1)
            print('Current state:')
            time_elapsed = '%.3f'%(self.frames_elapsed/30)
            print('Time elapsed {}'.format(time_elapsed))
            print('{} - HP {} - Mana {}'.format(self.char1.name, self.char1.hp,
            self.char1.mana))
            print('{} - HP {} - Mana {}'.format(self.char2.name, self.char2.hp,
            self.char2.mana))

    def train(self, eps=1.0, max_iter=10000):
        i = 0
        not_converged = True
        while not_converged and i < max_iter:
            i += 1

