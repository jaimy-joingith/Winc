# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

# 1 Players

class Player():

    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        if speed > 1 or speed < 0:
            raise ValueError('speed must be between 0 and 1')
        self.endurance = endurance
        if endurance > 1 or endurance < 0:
            raise ValueError('endurance must be between 0 and 1')
        self.accuracy = accuracy
        if accuracy > 1 or accuracy < 0:
            raise ValueError('accuracy must be between 0 and 1')

    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'

    def strength(self):
        if self.speed >= self.endurance and self.speed >= self.accuracy:
            return ('speed', self.speed)
        elif self.endurance >= self.accuracy:
            return ('endurance', self.endurance)
        else:
            return ('accuracy', self.accuracy)


class Commentator():

    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        accuracy = getattr(player, "accuracy")
        speed = getattr(player, "speed")
        endurance = getattr(player, "endurance")
        return accuracy + speed + endurance

    def compare_players(self, player_one, player_two, attribute):
        player_one_name = getattr(player_one, "name")
        player_two_name = getattr(player_two, "name")
        if getattr(player_one, attribute) > getattr(player_two, attribute):
            return player_one_name
        if getattr(player_two, attribute) > getattr(player_one, attribute):
            return player_two_name
        else:
            player_one_strength = getattr(player_one, 'strength')
            player_two_strength = getattr(player_two, 'strength')
            if player_one_strength()[1] > player_two_strength()[1]:
                return player_one_name
            if player_one_strength()[1] < player_two_strength()[1]:
                return player_two_name
            else:
                return 'These two players might as well be twins!'