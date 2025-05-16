from jogo import *
from jogador import *
from plataformaDejogos import *

AgostinhoGames = Plataforma("AgostinhoGames")

#Criando Jogos
Minecraft2 = Jogo("Minecraft 2", "Sandbox", "+10", 249.99)
AgostinhoGames.adicionarJogoCatalogo(Minecraft2)

GTA66 = Jogo("GTA 66", "FPS", "+18", 750.99)
AgostinhoGames.adicionarJogoCatalogo(GTA66)

SlimeRancher3 = Jogo("Slime Rancher 3", "Aventura", "Livre", 130.99)
AgostinhoGames.adicionarJogoCatalogo(SlimeRancher3)

#Criando Jogadores
Davi = Jogador("DevDaviHTRB", 90025091)
AgostinhoGames.adicionarJogador(Davi)

Gabriel = Jogador("GabrielNsCorreia", 80027092)
AgostinhoGames.adicionarJogador(Gabriel)

#Adicionando Saldo
pap = 400
clt = 1300
Davi.AdicionaSaldo(pap)
Gabriel.AdicionaSaldo(clt)
print("")
#Listar Calogo
AgostinhoGames.listarCatalogo()
print("")
#Gabriel tenta comprar Minecraft 2
AgostinhoGames.realizarCompra("Minecraft 2", 80027092)
print("")
# Gabriel verifica seu saldo
Gabriel.exibirPerfil()
print("")
#Gabriel tenta comprar Minecraft 2 novamente
AgostinhoGames.realizarCompra("Minecraft 2", 80027092)
print("")
#Davi tenta comprar GTA 66
AgostinhoGames.realizarCompra("GTA 66", 90025091)
print("")
#Davi Adiciona saldo
Davi.AdicionaSaldo(1000)
print("")
#Davi Tenta novamente
AgostinhoGames.realizarCompra("GTA 66", 90025091)
print("")
#Davi verifica seu saldo
Davi.exibirPerfil()