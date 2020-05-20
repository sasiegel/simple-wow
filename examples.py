import simplewow as wow

char1 = wow.Mage('Tom', 4)
char2 = wow.Paladin('Jake', 5)

arena = wow.Arena(char1, char2)
arena.duel('player', 'random')