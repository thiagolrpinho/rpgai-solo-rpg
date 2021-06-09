""" REGRAS
Estas são as regras do sistema Dominus.
Regra 1: Preparação
Para começar, escolha (ou role) um Arquétipo na tabela e dê um nome para seu personagem.
Depois role um dado três vezes na tabela de Trama.
Regra 2: História
Para começar a sua história, escolha (ou role) um Lugar na tabela de Cenas. Sempre que entrar
em uma Cena, role um dado. Se cair 3 ou menos, adicione um Personagem. Se cair 4 ou mais,
adicione um Evento. Você pode ir para uma nova cena se achar apropriado (e tenha resolvido
qualquer conflito aparente).
Regra 3: Desafio
Sempre que seu personagem tentar fazer algo que possa dar errado, você tem um Desafio: role
um dado. Se tirar 4 ou mais, você conseguiu vencê-lo. Se houver algo nesta situação que lhe dê
vantagem nesse Desafio, role 2 dados e escolha o maior. Caso algo lhe dê desvantagem, role 2
dados e escolha o menor.
Regra 4: Dilema
Sempre que tiver uma dúvida cuja resposta não seja óbvia, determine duas opções possíveis (sim
ou não, esquerda ou direita, acontece A ou acontece B etc) e role um dado. Se cair 3 ou menos é
a primeira opção, e se cair 4 ou mais é a segunda opção.
Regra 5: Banco de Ideias
Sempre que precisar elaborar melhor um Lugar, Personagem ou Evento, role no Banco de Ideias e
interprete o resultado de acordo com o Cenário.
Regra X: Especial
O Cenário pode ter regras especiais e únicas dele.
"""
import pandas as pd
import random as rnd


ARCHETYPE_PATH = 'rpgai-solo-rpg/resources/archetypes.xlsx'
PLOT_PATH = 'rpgai-solo-rpg/resources/plot.xlsx'
SCENES_PATH = 'rpgai-solo-rpg/resources/scenes.xlsx'

class Mechanics:
    archetypes: pd.DataFrame
    plots: pd.DataFrame

    def __init__(self):
        self.player = Player()
        self.archetypes = pd.read_excel(ARCHETYPE_PATH)
        self.plots = pd.read_excel(PLOT_PATH)
        self.scenes = pd.read_excel(SCENES_PATH)

    def roll_dice(self) -> int:
        return rnd.randint(1, 6)

    def preparation(
            self, character_name: str, choosen_value: int = None) -> str:
        """ Regra 1: Preparação
        Para começar, escolha (ou role) um Arquétipo na tabela e dê
        um nome para seu personagem.
        Depois role um dado três vezes na tabela de Trama. """
        self.player.name = character_name

        if choosen_value is None:
            dice_value = self.roll_dice()
        else:
            dice_value = choosen_value
        archetype_mask = self.archetypes['DiceNumber'] == dice_value
        self.player.archetype = self.archetypes[
            archetype_mask]['Name'].to_list()[0]

        dice_value = self.roll_dice()
        plot_fact_mask = (self.plots['DiceNumber'] == dice_value)
        self.player.fact = self.plots[
            plot_fact_mask]['Fact'].to_list()[0]
        
        dice_value = self.roll_dice()
        plot_mission_mask = (self.plots['DiceNumber'] == dice_value)
        self.player.mission = self.plots[
            plot_mission_mask]['Mission'].to_list()[0]
        
        dice_value = self.roll_dice()
        plot_bad_outcome_mask = (self.plots['DiceNumber'] == dice_value)
        self.player.bad_outcome = self.plots[
            plot_bad_outcome_mask]['BadOutcome'].to_list()[0]

        print("Welcome! ", self.player.name)
        print("Your archetype is ", self.player.archetype)
        print("What happened: ", self.player.fact)
        print("You should: ", self.player.mission)
        print("Or else: ", self.player.bad_outcome)




class Player():
    name: str
    archetype: str
    fact: str
    mission: str
    bad_outcome: str


