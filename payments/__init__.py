from otree.api import *


doc = """
Payments page
"""


class Constants(BaseConstants):
    name_in_url = 'payments'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    paid = models.IntegerField(initial=0)
    pass

# FUNCTIONS
def paid_function(player: Player):
    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
    print(participant_label)
    if participant_label == "Andrea":
        print("sucaaaaaaaaa")
        Player.paid = 1


# PAGES
class MyPage(Page):
    paid_function
    pass


class ResultsWaitPage(WaitPage):
    @staticmethod
    def before_next_page(player, timeout_happened):
        Player.paid_function()
    pass


class Results(Page):
    pass


page_sequence = [MyPage]
