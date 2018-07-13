from src.coin import Coin

class Experiment:
    def p_2_heads(self):
        c = Coin()
        successes = []
        trials = 100_000
        for _ in range(trials):
            is_success = [c.flip() for _ in range(2)].count('H') == 2
            successes.append(is_success)
        return sum(successes) / trials

    def p_pattern(self, pattern):
        c = Coin()
        successes = []
        trials = 100_000
        for _ in range(trials):
            is_success = ''.join( [c.flip() for _ in range(len(pattern))]) == pattern
            successes.append(is_success)
        return sum(successes) / trials




    





        