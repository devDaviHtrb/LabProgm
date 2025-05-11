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

#Listar Calogo
AgostinhoGames.listarCatalogo()

#Gabriel tenta comprar Slime Rancher 3
AgostinhoGames.realizarCompra("Minecraft 2", 80027092)
# Gabriel verifica seu saldo
Gabriel.exibirPerfil()
#Gabriel tenta comprar Slime Rancher 3 novamente
AgostinhoGames.realizarCompra("Minecraft 2", 80027092)

