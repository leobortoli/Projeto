import random
import numpy as np
import sys
import copy
from enum import Enum
class Dados():
    def __init__(self, nome, lados: int, multiplicador):
        self.nome = nome
        self.lados = lados
        self.multiplicador = multiplicador
    def setNome(self, nome):
        self.nome = nome
    def setMult(self, multiplicador):
        self.multiplicador = multiplicador
    def getNome(self):
        return self.nome
    def __str__(self):
        return f'Dado: {self.nome}, de {self.lados} lados com multiplicador {self.multiplicador}'
    def getDado(self):
        return self.__str__()
    def rolarDado(self):
        resultado = random.randint(1, self.lados) + self.multiplicador
        return resultado
class Stats():
    def __init__(self, idStat, vida: int, forca:int, destreza: int, \
    tecnica: int, raciocinio: int, vidAtual: int, vidTemp: int, vidMin: int, \
    statPrimario, statSecundario, enMax, enAtual, enMin):
        self.idStat = idStat
        self.vida = vida
        self.forca = forca
        self.destreza = destreza
        self.tecnica = tecnica
        self.raciocinio = raciocinio
        self.vidAtual = vidAtual
        self.vidTemp = vidTemp
        self.vidMin = vidMin
        self.statPrimario = statPrimario
        self.statSecundario = statSecundario
        self.mult1 = 1.0
        self.mult2 = 0.5
        self.enMax = enMax
        self.enAtual = enAtual
        self.enMin = enMin
    def setIdStat(self, idStat):
        self.idStat = idStat
    def setVit(self, vida):
        self.vida = vida
    def setFor(self, forca):
        self.forca = forca
    def setDes(self, destreza):
        self.destreza = destreza
    def setTec(self, tecnica):
        self.tecnica = tecnica
    def setRac(self, raciocinio):
        self.raciocinio = raciocinio
    def setVidAtual(self, vidAtual):
        self.vidAtual = vidAtual
    def setVidTemp(self, vidTemp):
        self.vidTemp = vidTemp
    def setVidMin(self, vidMin):
        self.vidMin = vidMin
    def setStat1(self, statPrimario):
        self.statPrimario = statPrimario
    def setStat2(self, statSecundario):
        self.statSecundario = statSecundario
    def setEnMax(self, enMax):
        self.enMax = enMax
    def setEnAtual(self, enAtual):
        self.enAtual = self, enAtual
    def setEnMin(self, enMin):
        self.enMin = enMin
    def getIdStat(self):
        return self.idStat
    def getVit(self):
        return self.vida
    def getFor(self):
        return self.forca
    def getDes(self):
        return self.destreza
    def getTec(self):
        return self.tecnica
    def getRac(self):
        return self.raciocinio
    def getVidAtual(self):
        return self.vidAtual
    def getVidTemp(self):
        return self.vidTemp
    def getVidMin(self):
        return self.vidMin
    def getStat1(self):
        return self.statPrimario
    def getStat2(self):
        return self.statSecundario
    def getEnMax(self):
        return self.enMax
    def getEnAtual(self):
        return self.enAtual
    def getEnMin(self):
        return self.enMin
    def maisMult1(self):
        self.mult1 = self.mult1 + 0.1
    def menosMult1(self):
        self.mult1 = self.mult1 - 0.1
    def maisMult2(self):
        self.mult2 = self.mult2 + 0.1
    def menosMult2(self):
        self.mult2 = self.mult2 - 0.1
    def getMult1(self):
        return self.mult1
    def getMult2(self):
        return self.mult2
    def __str__(self):
        return f'ID: {self.idStat}, \
        VIDA: {self.vida}, FORÇA: {self.forca}, DESTREZA: {self.destreza}, \
        TÉCNICA: {self.tecnica}, RACIOCÍNIO: {self.raciocinio} \
        HP: {self.vidAtual} / {self.vida} TEMPORÁRIO: {self.vidTemp} \
        ENERGIA: {self.enAtual} / {self.enMax}'
class Profs():
    def __init__(self, idProf, mecanismo: int, externo: int, interno: int, exotico: int):
        self.idProf = idProf
        self.mecanismo = mecanismo
        self.externo = externo
        self.interno = interno
        self.exotico = exotico
    def setIdProf(self, idProf):
        self.idProf = idProf
    def setMec(self, mecanismo):
        self.mecanismo = mecanismo
    def setExt(self, externo):
        self.externo = externo
    def setInt(self, interno):
        self.interno = interno
    def setExo(self, exotico):
        self.exotico = exotico
    def getIdProf(self):
        return self.idProf
    def getMec(self):
        return self.mecanismo
    def getExt(self):
        return self.externo
    def getInt(self):
        return self.interno
    def getExo(self):
        return self.exotico
    def __str__(self):
        return f'ID: {self.idProf}, \
        MEC: {self.mecanismo,"/100"}, EXT: {self.externo,"/100"}, \
        INT: {self.interno,"/100"}, EXO: {self.exotico,"/100"}'
class Alvos(Enum):
    SELF = 1
    ALLY = 2
    ENEMY = 3
class Escalas(Enum):
    NENHUM = 0
    VID = 1
    FOR = 2
    DES = 3
    TEC = 4
    RAC = 5
    TODOS = 6
class Habilidades():
    def __init__(self, codHab: int, nomHab: str, lvlHab: int, custo: int,\
        recarga: int, umAlvo: Alvos, descHab):
        self.codHab = codHab
        self.nomHab = nomHab
        self.lvlHab = lvlHab
        self.custo = custo
        self.recarga = recarga
        self.alvo = umAlvo
        self.descHab = descHab
        self.tempoRecarga = 0
    def setCodHab(self, codHab):
        self.codHab = codHab
    def setNomeHab(self, nomHab):
        self.nomHab = nomHab
    def setLvlHab(self, lvlHab):
        self.lvlHab = lvlHab
    def setCusto(self, custo):
        self.custo = custo
    def setRecarga(self, recarga):
        self.recarga = recarga
    def setAlvo(self, umAlvo):
        self.alvo = umAlvo
    def setMult(self, habMult):
        self.habMult = habMult
    def setDescHab(self, descHab):
        self.descHab = descHab
    def getCodHab(self):
        return self.codHab
    def getNomeHab(self):
        return self.nomHab
    def getLvlHab(self):
        return self.lvlHab
    def getCusto(self):
        return self.custo
    def getRecarga(self):
        return self.recarga
    def getAlvo(self):
        return self.alvo
    def getScale(self):
        return self.scale
    def getDescHab(self):
        return self.descHab
    def ativar(self):
        pass
    def habUp(self):
        return self.lvlHab + int(1)
    def __str__(self):
        pass
class Efeitos(Habilidades):
    def __init__(self, codHab: int, nomHab: str, lvlHab: int, custo: int,\
        recarga: int, umAlvo: Alvos,  descHab, tempo: int, umStat: Stats, \
        buffEscala: Escalas, deBuff= False, buffQtd: float = 1.0):
        super().__init__(codHab, nomHab, lvlHab, custo, recarga, umAlvo, descHab)
        self.tempo = tempo
        self.statBuff = umStat
        self.scale = buffEscala
        self.deBuff = deBuff
        self.buffQtd = buffQtd
    def setTempo(self, tempo): #polimorfismo de habilidades, ao lado de ataques
        self.tempo = tempo
    def setFichaStats(self, umStat):
        self.statBuff = umStat
    def setStatBuffado(self, buffEscala):
        self.scale = buffEscala #stat selecionado para buffar
    def setDebuff(self, deBuff):
        self.deBuff = deBuff #define se é buff ou debuff
    def setBuffQtd(self, buffQtd):
        self.buffQtd = buffQtd #quantidade do buff
    def ativar(self):
        if self.scale.value == 0:
            return
        elif self.scale.value == 1:
            self.statBuff.vida = int(self.statBuff.vida * self.buffQtd)
        elif self.scale.value == 2:
            self.statBuff.forca = int(self.statBuff.forca * self.buffQtd)
        elif self.scale.value == 3:
            self.statBuff.destreza = int(self.statBuff.destreza * self.buffQtd)
        elif self.scale.value == 4:
            self.statBuff.tecnica = int(self.statBuff.tecnica * self.buffQtd)
        elif self.scale.value == 5:
            self.statBuff.raciocinio = int(self.statBuff.raciocinio * self.buffQtd)
        elif self.scale.value == 6:
            self.statBuff.vida = int(self.statBuff.vida * self.buffQtd)
            self.statBuff.forca = int(self.statBuff.forca * self.buffQtd)
            self.statBuff.destreza = int(self.statBuff.destreza * self.buffQtd)
            self.statBuff.tecnica = int(self.statBuff.tecnica * self.buffQtd)
            self.statBuff.raciocinio = int(self.statBuff.raciocinio * self.buffQtd)
        else:
            return
    def menosBuff10(self):
        return float(self.buffQtd - 0.1)
    def maisBuff10(self):
        return float(self.buffQtd + 0.1)
    def getTempo(self):
        return self.tempo
    def getFichaStats(self):
        return self.statBuff
    def getStatBuffado(self):
        return self.scale
    def getDebuff(self):
        return self.deBuff
    def getBuffQtd(self):
        return self.buffQtd
    def __str__(self):
        return f'COD: {self.codHab} [HABILIDADE: {self.nomHab}] \
        (NÍVEL: {self.lvlHab}): {self.descHab}. Seu efeito é modificar em \
        {self.buffQtd*100}% de {self.scale} do {self.getAlvo()}'
class Ataques(Habilidades):
    def __init__(self, codHab: int, nomHab: str, lvlHab: int, custo: int,\
        recarga: int, umAlvo: Alvos,  descHab, atqEscala: Escalas, \
        umDado: Dados, habMult: int):
        super().__init__(codHab, nomHab, lvlHab, custo, recarga, umAlvo, descHab)
        self.scale = atqEscala
        self.habMult = habMult
        self.effHab = umDado
        self.tempoRecarga = 0
    def setScale(self, atqEscala):
        self.scale = atqEscala
    def setMult(self, habMult):
        self.habMult = habMult
    def setEffHab(self, umDado):
        self.effHab = umDado
    def getScale(self):
        return self.scale
    def setMult(self):
        return self.habMult
    def getEffHab(self):
        return self.effHab
    def ativar(self):
        somaDano= 0
        rolagem = np.array([self.effHab.rolarDado() for _ in range(self.habMult)])
        np.set_printoptions(threshold=sys.maxsize)
        somaDano = np.sum(rolagem)    
        return somaDano
    def habUp(self):
        return self.lvlHab + int(1)
    def __str__(self):
        return f'COD: {self.codHab} [HABILIDADE: {self.nomHab}] \
        (NÍVEL: {self.lvlHab}): {self.descHab}. Seu efeito é causar \
        {self.habMult} {self.effHab}'
class Personagens(Stats):
    def __init__(self, persoCod, persoNome: str, persoNivel: int, persoRaca: str, \
    persoClasse, persoStats, persoProfs, persoHab, umAllign): #herança de stats junto de agregação
        super().__init__(persoStats.idStat, persoStats.vida, persoStats.forca, \
        persoStats.destreza, persoStats.tecnica, persoStats.raciocinio,
        persoStats.vidAtual, persoStats.vidTemp,
        persoStats.vidMin, persoStats.statPrimario,
        persoStats.statSecundario, persoStats.enMax,
        persoStats.enAtual, persoStats.enMin)
        self.persoCod = persoCod
        self.persoNome = persoNome
        self.persoNivel = persoNivel
        self.persoRaca = persoRaca
        self.persoClasse = persoClasse
        self.stats = persoStats
        self.profs = persoProfs
        self.persoHab = persoHab
        self.umAllign = umAllign
    def setCod(self, persoCod):
        self.persoCod = persoCod
    def setNome(self, persoNome):
        self.persoNome = persoNome
    def setNivel(self, persoNivel):
        self.persoNivel = persoNivel
    def setRaca(self, persoRaca):
        self.persoRaca = persoRaca
    def setClasses(self, persoClasse):
        self.persoClasse = persoClasse
    def setStats(self, persoStats):
        self.stats = persoStats
    def setProfs(self, persoProfs):
        self.profs = persoProfs
    def setHabs(self, persoHab):
        self.persoHab = persoHab
    def setAllign(self, umAllign):
        self.umAllign = umAllign
    def getPersoCod(self):
        return self.persoCod
    def getNome(self):
        return self.persoNome
    def getNivel(self):
        return self.persoNivel
    def getRaca(self):
        return self.persoRaca
    def getClasses(self):
        return self.persoClasse
    def getStats(self):
        return self.stats
    def getProfs(self):
        return self.profs
    def getHabs(self):
        return self.persoHab
    def getAllign(self):
        return self.umAllign
    def persoUp(self):
        return self.persoNivel + int(1)
    def __str__(self):
        return f'NOME: {self.persoNome} NÍVEL: {self.persoNivel} COD: {self.persoCod}\
        RAÇA: {self.persoRaca} CLASSE: {self.persoClasse} \
        HP: {self.stats.vidAtual} / {self.stats.vida} TEMPORÁRIO: {self.stats.vidTemp}\
        ENERGIA: {self.stats.enAtual} / {self.stats.enMax} \
        STATS: {self.stats} \
        PROFICIÊNCIAS: {self.profs} \
        HABILIDADES: {self.persoHab}, É UM {self.umAllign}'
dado5 = Dados("dado5", 5, 0)
dado6 = Dados("dado6", 6, 0)
dado8 = Dados("dado8", 8, 0)
dado10 = Dados("dado10", 10, 0)
dado20 = Dados("dado20", 20, 0)
st1 = Stats(1, 60, 80, 15, 30, 15, 60, 0, 0, 80, 30, 95, 95, 0)
pf1 = Profs(2, 1, 2, 1, 1)

st2 = Stats(3, 50, 5, 5, 70, 70, 50, 0, 0, 70, 70, 105, 105, 0)
pf2 = Profs(4, 1, 1, 2, 1)

st3 = Stats(5, 30, 30, 80, 50, 10, 30, 0, 0, 80, 50, 105, 105, 0)
pf3 = Profs(6, 1, 2, 1, 1)

golpePoderoso= Ataques(codHab=1, nomHab="Golpe Poderoso", lvlHab=1, custo=5, \
recarga=1, umAlvo=Alvos.ENEMY,   descHab="Um ataque forte que causa dano.", \
atqEscala= Escalas.FOR, umDado= dado10, habMult=2)    

auraFortificante= Efeitos(codHab=2, nomHab="Aura Fortificante", lvlHab=1, custo=10, \
recarga=2, umAlvo=Alvos.ALLY,   descHab="Aumenta a força de um aliado.", tempo=2, umStat= st1,\
buffEscala= Escalas.FOR, deBuff=False, buffQtd=1.2)

flechaPrecisa= Ataques(codHab=3, nomHab="Flecha Precisa", lvlHab=1, custo=3, \
recarga=0, umAlvo=Alvos.ENEMY,   descHab="Utiliza de uma técnica avançada para lançar a flecha.", \
atqEscala= Escalas.DES, umDado= dado8, habMult=3)

g1 = Personagens(persoCod= 13, persoNome= "Wesley", persoNivel= 1, persoRaca= "HUMANO", persoClasse= "GUERREIRO", \
persoStats= st1, persoProfs= pf1, persoHab= golpePoderoso, umAllign= Alvos.ALLY)

m1 = Personagens(persoCod= 12, persoNome= "Francisco", persoNivel= 1, persoRaca= "ZUMBI", persoClasse= "MAGO", \
persoStats= st2, persoProfs= pf2, persoHab= auraFortificante, umAllign= Alvos.ENEMY)

a1 = Personagens(persoCod= 11, persoNome= "Victor", persoNivel= 1, persoRaca= "ELFO", persoClasse= "ARQUEIRO", \
persoStats= st3, persoProfs= pf3, persoHab= flechaPrecisa, umAllign= Alvos.ENEMY)

listaDados = [dado5, dado6, dado8, dado10, dado20]
listaStats = [st1, st2, st3]
listaProfs = [pf1, pf2, pf3]
listaHabs = [golpePoderoso, auraFortificante, flechaPrecisa]                    
listaPersonagens = [g1, m1, a1]

def jogar():
    print("A luta começará. Os personagens disponíveis são:\n")
    for perso in listaPersonagens:
        print(perso)
        print("\n")
    skip = None
    skip = input("Digite qualquer coisa para continuar:")
    print("Escolha um personagem do alinhamento ALLY: ")
    listaSelecionados = []
    select1 = True
    select2 = True
    while select1 is True:
            try:
                pegarPer = int(input("Qual é o código do personagem desejado? "))
                persoAtual = None
                for perso in listaPersonagens:
                    if pegarPer == int(perso.persoCod):
                        persoAtual = copy.deepcopy(perso)
                        listaSelecionados.append(persoAtual)
                        break
                if persoAtual is not None:
                    print(f"Ficha encontrada: {persoAtual.getPersoCod()}")
                    select1 = False
                    break
                else:
                    print("Nenhuma ficha encontrada, tente de novo!")
            except ValueError:
                print("Formato inválido, digite um número inteiro!\n")
    print("Escolha um personagem do alinhamento ENEMY: ")
    listaInimigos = []
    while select2 is True:
            try:
                pegarPer2 = int(input("Qual é o código do personagem desejado? "))
                inimAtual = None
                for perso in listaPersonagens:
                    if pegarPer2 == int(perso.persoCod):
                        inimAtual = copy.deepcopy(perso)
                        listaInimigos.append(inimAtual)
                        break
                if inimAtual is not None:
                    print(f"Ficha encontrada: {inimAtual.getPersoCod()}")
                    select2 = False
                    break
                else:
                    print("Nenhuma ficha encontrada, tente de novo!")
            except ValueError:
                print("Formato inválido, digite um número inteiro!\n")
    if skip is not None:
        final = False  
    while not final:
        for persoAtual, inimAtual in zip(listaSelecionados, listaInimigos):
            turno = 0
            if inimAtual.stats.vidAtual > 0:
                print(f"É o turno de {persoAtual.persoNome}, da classe {persoAtual.persoClasse}.")
                print("=============================================")
                print(f"=============HP:{persoAtual.stats.vidAtual}/{persoAtual.stats.vida} EP:{persoAtual.stats.enAtual}/{persoAtual.stats.enMax}=============")
                print(f"============={persoAtual.persoHab}=============")
                print("=============================================")
                usarSkill = input("Você deseja utilizar a habilidade acima? ")
                if usarSkill in ["S", "s", "Sim", "sim", "SIM"]:
                    acerto = dado20.rolarDado()
                    print("O dado rolou ", acerto)
                if acerto >= 9:
                    if inimAtual.umAllign == Alvos.ENEMY and inimAtual.stats.vidAtual > 0:
                        dano = persoAtual.persoHab.ativar()
                        print("O dano foi: ", dano)
                        inimAtual.stats.vidAtual -= dano
                        print(f"{inimAtual.persoNome} agora tem {inimAtual.stats.vidAtual} HP.")
                else:
                    dano = 0
                    print("O ataque errou!!")
            else:
                final= True
                print("A luta acabou!")
            if inimAtual.stats.vidAtual > 0:
                print(f"É o turno de {inimAtual.persoNome}, da classe {inimAtual.persoClasse}.")
                print("=============================================")
                print(f"=============HP:{inimAtual.stats.vidAtual}/{inimAtual.stats.vida} EP:{inimAtual.stats.enAtual}/{inimAtual.stats.enMax}=============")
                print(f"============={inimAtual} utilizou {inimAtual.persoHab}=============")
                print("=============================================")
                acerto = dado20.rolarDado()
                print("O dado rolou ", acerto)
                if acerto >= 9:
                    if persoAtual.umAllign == Alvos.ALLY and persoAtual.stats.vidAtual > 0:
                        dano = inimAtual.persoHab.ativar()
                        print("O dano foi: ", dano)
                        persoAtual.stats.vidAtual -= dano
                        print(f"{persoAtual.persoNome} agora tem {persoAtual.stats.vidAtual} HP.")
                else:
                    dano = 0
                    print("O ataque errou!!")
                turno += 1
            else:
                final= True
                print("A luta acabou!")

continuar = int(1)
while continuar >0:
    print("1 - Cadastrar Dado")
    print("2 - Cadastrar Stats")
    print("3 - Cadastrar Proficiências")
    print("4 - Cadastrar Habilidades")
    print("5 - Cadastrar Personagens")
    print("6 - Adição de Habilidades")
    print("7 - Listar Dados")
    print("8 - Listar Fichas de Stats")
    print("9 - Listar Fichas de Proficiências")
    print("10 - Listar Habilidades")
    print("11 - Listar Personagens")
    print("12 - Jogar!")
    escolha= input("Escolha o processo desejado de acordo com o número: ")
    match escolha:
        case '1':
            for dado in range(1, 10000):
                print("PROCESSO 1: Cadastrar Dados:")
                resp2 = input("Deseja cadastrar um dado? ")
                if resp2 in ["Não", "não", "nao", "não", "N", "n"]:
                    break
                nome = input("Insira um nome para o dado: ").strip().lower()
                while True:
                    try:
                        lados = int(input("O dado tem quantos lados? "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                multResp = input("O dado possui multiplicador? ")
                if multResp in ["Não", "não", "nao", "não", "N", "n"]:
                    multiplicador = 0
                else:
                    while True:
                        try:
                            multiplicador = int(input("Qual é o multiplicador do \
                            dado?: "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                dado= Dados(nome, lados, multiplicador)
                listaDados.append(dado)
                break
        case '2':
            for stat in range(1, 10000):
                print("PROCESSO 2: Cadastrar Stats:")
                resp1 = input("Deseja cadastrar uma ficha de stat? ")
                if resp1 in ["Não", "não", "nao", "não", "N", "n"]:
                    break
                idStat = input("Defina um identificador para a ficha: ")
                while True:
                    try:
                        vida = int(input("Digite o valor de vida: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                while True:
                    try:
                        forca = int(input("Digite o valor de força: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                while True:
                    try:    
                        destreza = int(input("Digite o valor de destreza: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                while True:
                    try:
                        tecnica = int(input("Digite o valor de técnica: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                while True:
                    try:
                        raciocinio = int(input("Digite o valor de raciocínio: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                vidAtual = vida
                cond1 = input("O personagem possui alguma vida temporária? ")
                if cond1 in ["Sim", "sim", "s", "S"]:
                    while True:
                        try:
                            vidTemp = int(input("Qual é o valor de vida temporária?"))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                else:
                    vidTemp = 0
                vidMin = vida*(-1)
                q1 = input("O stat primário para obter energia é? (escreva as 3 primeiras letras do stat): ")
                if (q1 == "vid" or q1 == "VID"):
                    statPrimario = vida
                elif (q1 == "for" or q1 == "FOR"):
                    statPrimario = forca
                elif (q1 == "des" or q1 == "DES"):
                    statPrimario = destreza
                elif (q1 == "tec" or q1 == "TEC"):
                    statPrimario = tecnica
                elif (q1 == "rac" or q1 == "RAC"):
                    statPrimario = raciocinio
                else:
                    print("ATRIBUTO INVÁLIDO!")
                    break
                q2 = input("O stat secundário para obter energia é? (escreva as 3 primeiras letras do stat): ")
                if (q2 == "vid" or q2 == "VID"):
                    statSecundario = vida
                elif (q2 == "for" or q2 == "FOR"):
                    statSecundario = forca
                elif (q2 == "des" or q2 == "DES"):
                    statSecundario = destreza
                elif (q2 == "tec" or q2 == "TEC"):
                    statSecundario = tecnica
                elif (q2 == "rac" or q2 == "RAC"):
                    statSecundario = raciocinio
                else:
                    print("ATRIBUTO INVÁLIDO!")
                    break
                cond2 = input("O personagem possui um valor especial de en. máxima? ")
                if cond2 in ["Sim", "sim", "s", "S"]:
                    while True:
                        try:
                            enMax = int(input("Qual é o valor de energia máxima? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                else:
                    enMax = (int(statPrimario * 1) + int(statSecundario * 0.5))
                enAtual = enMax
                while True:
                    try:
                        enMin = int(input("Qual é o valor de energia mínima? "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                stat= Stats(idStat, vida, forca, destreza, tecnica, raciocinio \
                , vidAtual, vidTemp, vidMin, statPrimario, statSecundario, \
                enMax, enAtual, enMin)
                listaStats.append(stat)
                break
        case '3':
            for prof in range(1, 10000):
                print("PROCESSO 3: Cadastrar Proficiências:")
                resp2 = input("Deseja cadastrar uma ficha de proficiências? ")
                if resp2 in ["Não", "não", "nao", "não", "N", "n"]:
                    break
                idProf = input("Defina um identificador para a ficha: ")
                while True:
                    try:
                        mecanismo = int(input("Digite o valor de mecanismo: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                while True:
                    try:
                        externo = int(input("Digite o valor de externo: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                while True:
                    try:
                        interno = int(input("Digite o valor de interno: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                while True:
                    try:
                        exotico = int(input("Digite o valor de exótico: "))
                        break
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                prof= Profs(idProf, mecanismo, externo, interno, exotico)
                listaProfs.append(prof)
                break
        case '4':
            for hab in range(1, 10000):
                print("PROCESSO 4: Cadastrar Habilidades:")
                resp3 = input("Deseja cadastrar uma habilidade? ")
                if resp3 in ["Não", "não", "nao", "não", "N", "n"]:
                    break
                resp4 = input("Você deseja cadastrar uma habilidade de ataque \
                ou de efeito? ")
                if resp4 in ["ataque", "Ataque", "ATAQUE"]:
                    while True:
                        try:
                            codHab = int(input("Defina um identificador para a ficha: "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    nomHab = input("Qual é o nome da habilidade? ")
                    while True:
                        try:
                            lvlHab = int(input("Qual é o nível da habilidade? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    while True:
                        try:
                            custo = int(input("Qual é o custo da habilidade? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    while True:
                        try:
                            recarga = int(input("Qual é o tempo de recarga da \
                            habilidade? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    print("A habilidade afeta quem? SELF, a si mesmo; ALLY \
                    um aliado; ENEMY, um inimigo: ")
                    while True:
                        alvoHab = input("Digite (SELF, ALLY, ENEMY): ").strip().upper()
                        try:
                            umAlvo = Alvos[alvoHab]
                            break
                        except KeyError:
                            print("Formato inválido, digite SELF, ALLY, ou ENEMY.")
                    descHab = input("Faça uma breve descrição da habilidade: ")
                    while True:
                        habScale = input("Digite o atributo com o qual a \
                        habilidade escala:, podendo ser VID, FOR, DES, TEC, RAC: ").strip().upper()
                        try:
                            atqEscala = Escalas[habScale]
                            break
                        except KeyError:
                            print("Formato inválido, digite VID, FOR, DES, TEC, RAC.")
                    print("DADOS DISPONÍVEIS: ")
                    for dado in listaDados:
                        print(dado.getDado())
                    while True:
                        escolhaDado = input("Qual é o nome do dado desejado? ").strip().lower()
                        umDado = None
                        for dado in listaDados:
                            if escolhaDado.strip().lower() == dado.getNome().strip().lower():
                                umDado = dado
                                break
                        if umDado is not None:
                            break
                        else:
                                print("Nenhum dado encontrado, tente de novo!")
                    while True:
                        try:
                            habMult = int(input("Quantas vezes o dado será rolado? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    hab = Ataques(codHab, nomHab, lvlHab, custo, recarga, \
                    umAlvo, descHab, atqEscala, umDado, habMult)
                    listaHabs.append(hab)
                    break
                elif resp4 in ["efeito", "Efeito", "EFEITO"]:
                    while True:
                        try:
                            codHab = int(input("Defina um identificador para a ficha: "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    nomHab = input("Qual é o nome da habilidade? ")
                    while True:
                        try:
                            lvlHab = int(input("Qual é o nível da habilidade? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    while True:
                        try:
                            custo = int(input("Qual é o custo da habilidade? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    while True:
                        try:
                            recarga = int(input("Qual é o tempo de recarga da \
                            habilidade? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    print("A habilidade afeta quem? SELF, a si mesmo; ALLY \
                    um aliado; ENEMY, um inimigo: ")
                    while True:
                        alvoHab = input("Digite (SELF, ALLY, ENEMY): ").strip().upper()
                        try:
                            umAlvo = Alvos[alvoHab]
                            break
                        except KeyError:
                            print("Formato inválido, digite SELF, ALLY, ou ENEMY.")
                    descHab = input("Faça uma breve descrição da habilidade: ")
                    while True:
                        try:
                            tempo = input("Faça uma breve descrição da habilidade: ")
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    print("FICHAS DE STATS DISPONÍVEIS: ")
                    for stat in listaStats:
                        print(f'ID: {stat.idStat}, \
                        VIDA: {stat.vida}, FORÇA: {stat.forca}, DESTREZA: {stat.destreza}, \
                        TÉCNICA: {stat.tecnica}, RACIOCÍNIO: {stat.raciocinio} \
                        HP: {stat.vidAtual} / {stat.vida} TEMPORÁRIO: {stat.vidTemp} \
                        ENERGIA: {stat.enAtual} / {stat.enMax}')
                    while True:
                        escolhaStat = int(input("Qual é o código da ficha desejada? "))
                        umStat = None
                        for stat in listaStats:
                            if escolhaStat == stat.getIdStat():
                                umStat = stat
                                break
                        if umStat is not None:
                            break
                        else:
                                print("Nenhuma ficha encontrada, tente de novo!")
                    while True:
                        buffScale = input("Digite o atributo com o qual a \
                        habilidade escala:, podendo ser NENHUM, VID, FOR, DES, \
                        TEC, RAC ou TODOS: ").strip().upper()
                        try:
                            buffEscala = Escalas[buffScale]
                            break
                        except KeyError:
                            print("Formato inválido, digite NENHUM, VID, FOR, \
                            DES, TEC, RAC ou TODOS.")
                    while True:
                        try:
                            check = input("Essa habilidade de efeito é um BUFF \
                            ou um DEBUFF? ").strip().upper()
                            if check.strip().upper() == "BUFF":
                                deBuff = False
                                break
                            elif check.strip().upper() == "DEBUFF":
                                deBuff = True
                                break
                            else:
                                print("Formato inválido, digite BUFF ou DEBUFF.")
                        except Exception as e:
                                print(f"Ocorreu um erro: {e}")
                    while True:
                        try:
                            numPor = int(input("Qual será a porcentagem do buff \
                            ou debuff, exemplo: 10, 20, 30, 40, 50 (NÚMERO INTEIRO)?"))
                            if deBuff == False:
                                buffQtd = (1.0 + float(numPor/100))
                                break
                            elif deBuff == True:
                                buffQtd = (1.0 - float(numPor/100))
                                break
                            else:
                                print("Não foi possível saber se é buff ou \
                                debuff!\n")
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                    hab = Efeitos(codHab, nomHab, lvlHab, custo, recarga, \
                    umAlvo, descHab, tempo, umStat, buffEscala, deBuff, buffQtd)
                    listaHabs.append(hab)
                    break
                else:
                    print("Insira corretamente o tipo de habilidade!")
        case '5':
            for perso in range(1, 10000):
                print("PROCESSO 5: Cadastrar Personagens:")
                resp5 = input("Deseja cadastrar um personagem? ")
                if resp5 in ["Não", "não", "nao", "não", "N", "n"]:
                    break
                while True:
                        try:
                            persoCod = int(input("Qual é código do(a) personagem? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                persoNome = input("Qual é o nome do(a) personagem? ")
                while True:
                        try:
                            persoNivel = int(input("Qual é nível do(a) personagem? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                persoRaca = input("Qual é a raça do personagem? ")
                persoClasse = input("Qual é a classe do personagem? ").strip().upper()
                print("FICHAS DE STATS DISPONÍVEIS:")
                for stat in listaStats:
                    print(stat)
                while True:
                    try:
                        pegarStat = int(input("Qual é o código da ficha desejada? "))
                        persoStats = None
                        for stat in listaStats:
                            if pegarStat == int(stat.idStat):
                                persoStats = stat
                                break
                        if persoStats is not None:
                            print(f"Ficha encontrada: {persoStats.getIdStat()}")
                            break
                        else:
                            print("Nenhuma ficha encontrada, tente de novo!")
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                print("FICHA DE PROFICIÊNCIAS DISPONÍVEIS:")
                for prof in listaProfs:
                    print(prof)
                while True:
                    try:
                        pegarProf = int(input("Qual é o código da ficha desejada? "))
                        persoProfs = None
                        for prof in listaProfs:
                            if pegarProf == int(prof.idProf):
                                persoProfs = prof
                                break
                        if persoProfs is not None:
                            print(f"Ficha encontrada: {persoProfs.getIdProf()}")
                            break
                        else:
                            print("Nenhuma ficha encontrada, tente de novo!")
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                while True:
                    if persoClasse.strip().upper() == "GUERREIRO":
                        persoHab = golpePoderoso
                        break
                    elif persoClasse.strip().upper() == "MAGO":
                        persoHab = auraFortificante
                        break
                    elif persoClasse.strip().upper() == "ARQUEIRO":
                        persoHab = flechaPrecisa
                        break
                    for hab in listaHabs:
                        print(f"Código: {hab.getCodHab()}, Nome: {hab.getNomeHab()}")
                    else:
                        try:
                            pegarHab = int(input("Qual é o código da habilidade desejada? "))
                            persoHab = None
                            for hab in listaHabs:
                                if pegarHab == int(hab.codHab):
                                    persoHab = hab
                                    break
                            if persoHab is not None:
                                print(f"Habilidade encontrada: {persoHab.getCodHab()}")
                                break
                            else:
                                print("Nenhuma habilidade encontrada, tente de novo!")  
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                while True:
                    alvoPerso = input("Digite (O personagem é ALLY ou ENEMY?): ").strip().upper()
                    try:
                        umAllign = Alvos[alvoPerso]
                        break
                    except KeyError:
                        print("Formato inválido, digite ALLY, ou ENEMY.")
                perso = Personagens(persoCod, persoNome, persoNivel, persoRaca, \
                persoClasse, persoStats, persoProfs, persoHab, umAllign)
                listaPersonagens.append(perso)
                break
        case '6':
            print("PROCESSO 6: Adição de Habilidades:")
            print("PERSONAGENS DISPONÍVEIS:")
            for perso in listaPersonagens:
                print(perso)
                select= input("Você deseja selecionar esse personagem? ")
                if select in ["s", "S", "Sim", "SIM", "sim"]:
                    while True:
                        try:
                            marca= True
                            for hab in listaHabs:
                                print("HABILIDADES DISPONÍVEIS:")
                                print(f"Código: {hab.getCodHab()}, Nome: {hab.getNomeHab()}")
                                select2= input("Você deseja selecionar essa habilidade? ")
                                if select2 in ["s", "S", "Sim", "SIM", "sim"]:
                                    while True:
                                        escolherHab = int(input("Qual é o código da habilidade deseja \
                                adicionar ao personagem?"))
                                        if escolherHab == int(hab.codHab):
                                            perso.setHabs(hab)
                                            print(f"Habilidade '{hab.getNomeHab()}' \
                                            adicionada ao personagem '{perso.persoNome}' \
                                            com sucesso!")
                                            marca = False
                                            break
                                else:
                                    continue
                            if marca == False:
                                break
                            else:
                                print("Nenhuma habilidade encontrada, tente de novo!")
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                else:
                    continue    
        case '7':
            print("PROCESSO 7: Listar Dados:")
            print("DADOS DISPONÍVEIS:")
            for dado in listaDados:
                print(dado)
        case '8':
            print("PROCESSO 8: Listar Fichas de Stats:")
            print("FICHAS DE STAT DISPONÍVEIS:")
            for stat in listaStats:
                print(stat)
        case '9':
            print("PROCESSO 9: Listar Fichas de Proficiências:")
            print("FICHAS DE PROF DISPONÍVEIS:")
            for prof in listaProfs:
                print(prof)
        case '10':
            print("PROCESSO 10: Listar Habilidades:")
            print("HABILIDADES DISPONÍVEIS:")
            for hab in listaHabs:
                print(hab)
        case '11':
            print("PROCESSO 11: Listar Personagens:")
            for perso in listaPersonagens:
                print(f"NOME: {perso.persoNome} RAÇA: {perso.persoRaca} CLASSE:\
        {perso.persoClasse} COD: {perso.persoCod}\
        HP: {perso.stats.vidAtual} / {perso.stats.vida} TEMPORÁRIO: {perso.stats.vidTemp}\
        ENERGIA: {perso.stats.enAtual} / {perso.stats.enMax} \
        STATS: {perso.stats} \
        PROFICIÊNCIAS: {perso.profs} \
        HABILIDADES: {perso.persoHab}'")
        case '12':
            jogar()
        case _:
            processo = input("DESEJA CONTINUAR OPERAÇÕES? ")
            match processo:
                case "S":
                    continuar = (continuar + 0)
                case "Sim":
                    continuar = (continuar + 0)
                case "SIM":
                    continuar = (continuar + 0)
                case "s":
                    continuar = (continuar + 0)
                case "sim":
                    continuar = (continuar + 0)
                case _:    
                    continuar = (continuar - 1)