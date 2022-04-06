class squadra:
  def __init__(self, nome, punteggio):
    self.nome=nome
    self.punteggio=punteggio




class campionato_sportivo:
  def __init__(self, *squadra):
    self.campionato_sportivo = list(squadra)
  def aggiungi(self, squadra):
    self.campionato_sportivo.append(squadra)
  def togli(self, squadra):
    self.campionato_sportivo.pop(squadra)
  def punti(self):
    print(self.punteggio) # self.squadra.punteggio?

squadra_1 = campionato_sportivo(squadra('squadra_A', '123'))
print(squadra_1)
campionato_sportivo.aggiungi(squadra('squadra_B', '144'))
campionato_sportivo.aggiungi(squadra('squadra_C', '134'))