from otree.api import *


doc = """
Your app description
"""

## THIS IS THE MONTPELLIER BRANCH ##
class Constants(BaseConstants):
    name_in_url = 'pilot'
    players_per_group = None
    num_rounds = 1
    app_debut_old = "11 septembre" # should be a sunday
    app_end_old= "17 septembre" # should be a saturday
    app_debut = "18 septembre"
    app_end= "24 septembre"
    Phase1_date = "19 septembre"
    Phase2_date = "25 septembre"
    prize = cu(25)
    probability = "25%"
    TABS_TEMPLATE = __name__ + '/tabs.html'
    TABS_TEMPLATE2 = __name__ + '/tabs2.html'
    DROPPED = __name__ + '/Dropped.html'
    payment_day = "29 septembre"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # consumption variables
    wifi_consumption = models.FloatField(label="Votre consommation de données par <b>Wi-Fi</b> : ")
    wifi_consumption_old = models.FloatField(label="Votre consommation de données par <b>Wi-Fi</b> : ")
    wifi_facebook = models.FloatField(label="", blank=True)
    wifi_instagram = models.FloatField(label="", blank=True)
    wifi_tiktok = models.FloatField(label="", blank=True)
    wifi_snapchat = models.FloatField(label="", blank=True)
    wifi_youtube = models.FloatField(label="", blank=True)
    mobile_consumption = models.FloatField(label="Votre consommation de données par <b>Mobile</b> : ")
    mobile_consumption_old = models.FloatField(label="Votre consommation de données par <b>Mobile</b> : ")
    mobile_facebook = models.FloatField(label="", blank=True)
    mobile_instagram = models.FloatField(label="", blank=True)
    mobile_tiktok = models.FloatField(label="", blank=True)
    mobile_snapchat = models.FloatField(label="", blank=True)
    mobile_youtube = models.FloatField(label="", blank=True)

    wifi_UM = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        widget=widgets.RadioSelectHorizontal,
        label="Unité de mesure indiquée"
    )
    wifi_UM_old = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        widget=widgets.RadioSelectHorizontal,
        label="Unité de mesure indiquée"
    )
    wifi_UM_facebook = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    wifi_UM_instagram = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    wifi_UM_tiktok = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    wifi_UM_snapchat = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    wifi_UM_youtube = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    mobile_UM = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    mobile_UM_old = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        widget=widgets.RadioSelectHorizontal,
        label=""
    )
    mobile_UM_facebook = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    mobile_UM_instagram = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    mobile_UM_tiktok = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    mobile_UM_snapchat = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )
    mobile_UM_youtube = models.StringField(
        choices=[["Gb","Gb"],["Mb","Mb"],["Kb","Kb"]], initial=None,
        label="", blank=True
    )

    age = models.IntegerField(label='Quelle est votre age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Homme', 'Homme'], ['Femme', 'Femme'], ['Autre','Autre']],
        label='Vous êtes : ',
        widget=widgets.RadioSelectHorizontal,
    )
    wifi_home = models.StringField(label="Avez-vous une connexion Wi-Fi à votre domicile ?",
                                    choices=[['Oui','Oui'], ['Non','Non']],widget=widgets.RadioSelect)
    wifi_home_freq = models.IntegerField(label="Sur une échelle de 1 à 5 (1 étant “Jamais” et 5 “Très souvent”), à quelle fréquence utilisez-vous une connexion Wi-Fi à votre domicile avec votre smartphone ?",
                                    choices=[['1','1 - Jamais'],
                                             ['2',''],
                                             ['3',''],
                                             ['4',''],
                                             ['5','5 - Très souvent'],
                                             ],
                                         widget=widgets.RadioSelect)
    wifi_on = models.StringField(label="Sur votre box internet, quand le Wi-Fi est-il activé ?",
                                    choices=[['Jamais','Jamais'], ['Globalement, lorsque j’en ai besoin (ou quelqu’un d’autre dans mon domicile en a besoin)','Globalement, lorsque j’en ai besoin (ou quelqu’un d’autre dans mon domicile en a besoin)'],
                                             ['En permanence','En permanence']],widget=widgets.RadioSelect)
    box_on = models.StringField(label="A votre domicile, votre box internet est-elle allumée en permanence ?",
                                    choices=[['Oui','Oui'], ['Non','Non']],widget=widgets.RadioSelect)
    wifi_on_absence = models.StringField(label="Votre box Wi-Fi reste-elle allumée lorsque vous absentez pendant plusieurs jours (vacances etc.) ?",
                                    choices=[['Oui','Oui'], ['Non','Non']],widget=widgets.RadioSelect)
    wifi_coverage = models.IntegerField(label="Sur une échelle de 1 à 5 (0 étant “Très insatisfait” et 5 “Très satisfait”) dans quelle mesure êtes-vous satisfait de votre signal Wi-Fi dans votre habitation habituelle ?",
                                    choices=[['1','1 - Très insatisfait'],
                                             ['2','2'],
                                             ['3','3'],
                                             ['4','4'],
                                             ['5','5 - Très satisfait'],
                                             ],
                                        widget=widgets.RadioSelect)
    wifi_home_people = models.IntegerField(label="Combien de personnes composent votre domicile ?")
    wifi_external = models.IntegerField(label="Sur une échelle de 1 à 5 (1 étant “Jamais” et 5 “Très souvent”), à quelle fréquence utilisez-vous une connexion Wi-Fi qui ne soit pas celle de votre domicile (par exemple, Wi-Fi de l’université, travail, public) ?",
                                    choices=[['1','1 - Jamais'],
                                             ['2',''],
                                             ['3',''],
                                             ['4',''],
                                             ['5','5 - Très souvent'],
                                             ],
                                        widget=widgets.RadioSelect)
    wifi_automatic = models.StringField(label="Votre smartphone est-il réglé pour qu’il se connecte automatiquement aux réseaux Wi-Fi ?",
                                    choices=[['Oui','Oui'], ['Non','Non']],widget=widgets.RadioSelect)
    wifi_updates = models.StringField(label="Votre smartphone est-il réglé pour que les mises à jour soient faites par Wifi exclusivement ?",
                                    choices=[['Oui','Oui'], ['Non','Non']],widget=widgets.RadioSelect)
    hotspot = models.IntegerField(label="A quelle fréquence utilisez-vous votre portable pour faire des partages de connexion ?",
                                    choices=[['1','1 - Jamais'],
                                             ['2',''],
                                             ['3',''],
                                             ['4',''],
                                             ['5','5 - Très souvent'],
                                             ],
                                  widget=widgets.RadioSelect)
    forfait_mobile = models.StringField(label="Avez-vous un forfait mobile 4G ou 5G ?",
                                    choices=[['Oui','Oui'], ['Non','Non']],widget=widgets.RadioSelect)
    giga_mobile = models.IntegerField(label="Si oui, combien de Go ?", blank=True)
    preference_mobile = models.StringField(label="En général, quand du Wi-Fi est disponible, préférez-vous utiliser votre smartphone en utilisant le Wi-Fi plutôt que le réseau mobile ?",
                                    choices=[['Oui','Oui'], ['Non','Non']],widget=widgets.RadioSelect)
    preference_mobile_reason = models.LongStringField(label="Pourquoi ?", blank=True)
    dropped = models.IntegerField(initial=0)

    pass


# PAGES
class Reserver_place(Page):
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.dropped = 1
            player.wifi_home = 'DROPPED'
    pass

class Confirmation_place(Page):
    pass

class Welcome(Page):
    pass

class Phase1(Page):
    pass

class Phase1_questionnaire(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','wifi_home','wifi_home_people'
                   #'wifi_home_freq', 'wifi_on','wifi_on_absence', 'wifi_coverage','wifi_external','wifi_automatic','wifi_updates','hotspot','forfait_mobile','giga_mobile',
                   #'preference_mobile','preference_mobile_reason',
                   ]
    pass

class Phase2_questionnaire(Page):
    def is_displayed(player: Player):
        return player.wifi_home == 'Oui'
    pass
    form_model = 'player'
    form_fields = ['wifi_home_freq', 'box_on','wifi_on','wifi_on_absence', 'wifi_coverage',
                   #'wifi_external','wifi_automatic','wifi_updates','hotspot','forfait_mobile','giga_mobile',
                   #'preference_mobile','preference_mobile_reason',
                   ]
    pass

class Phase3_questionnaire(Page):
    form_model = 'player'
    form_fields = ['wifi_external','wifi_automatic','wifi_updates','hotspot','forfait_mobile','giga_mobile',
                   'preference_mobile','preference_mobile_reason',
                   ]
    pass

class EndPhase1(Page):
    pass

class Phase2(Page):
    form_model = 'player'
    form_fields = ['wifi_consumption','wifi_UM']
    pass

class Phase2_mobile(Page):
    form_model = 'player'
    form_fields = ['mobile_consumption','mobile_UM']
    pass

class Phase2_old_data(Page):
    form_model = 'player'
    form_fields = ['wifi_consumption_old','mobile_consumption_old','wifi_UM_old','mobile_UM_old']
    pass

class Phase2_apps(Page):
    form_model = 'player'
    form_fields = ['mobile_facebook','wifi_facebook','mobile_UM_facebook','wifi_UM_facebook',
                   'mobile_instagram','wifi_instagram','mobile_UM_instagram','wifi_UM_instagram',
                   'mobile_tiktok','wifi_tiktok','mobile_UM_tiktok','wifi_UM_tiktok',
                   'mobile_snapchat','wifi_snapchat','mobile_UM_snapchat','wifi_UM_snapchat',
                   'mobile_youtube','wifi_youtube','mobile_UM_youtube','wifi_UM_youtube',]
    pass

class EndPhase2(Page):
    pass

page_sequence = [Reserver_place,Confirmation_place,Welcome, Phase1, Phase1_questionnaire, Phase2_questionnaire, Phase3_questionnaire, EndPhase1, Phase2, Phase2_mobile, Phase2_apps, Phase2_old_data, EndPhase2]
