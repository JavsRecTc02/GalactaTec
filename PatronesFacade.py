from PatronesEnemigos import PatronesEnemigos

#Patron estructural Facade
class EnemyPatternsFacade:
    def __init__(self):
        self.patrones = PatronesEnemigos()

    def zigzag_pattern(self, enemigos):
        self.patrones.patron1(enemigos)

    def circular_pattern(self, enemigos):
        self.patrones.patron2(enemigos)

    def descending_pattern(self, enemigos):
        self.patrones.patron_descenso(enemigos)

    def column_pattern(self, enemigos):
        self.patrones.patron3(enemigos)

    def sinusoidal_pattern(self, enemigos):
        self.patrones.patron4(enemigos)
