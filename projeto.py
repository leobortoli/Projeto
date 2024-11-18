import random
import numpy as np
import sys
import copy
from typing import NewType
from enum import Enum
from typing import Optional
def val_en(self, enAtual):
    if enAtual > self.enMax:
        return self.enMax
    elif enAtual < self.enMin:
        return self.enMin
    else:
        return enAtual 
def val_hp(self, vidAtual):
    if (self.vidAtual > self.vida):
        return self.vida
    if (self.vidAtual < self.vidMin):
        return self.vidMin
    else:
        return vidAtual
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
        self.stat1 = statPrimario
        self.stat2 = statSecundario
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
        self.vidAtual = val_hp(self, vidAtual)
    def setVidTemp(self, vidTemp):
        self.vidTemp = vidTemp
    def setVidMin(self, vidMin):
        self.vidMin = vidMin
    def setStat1(self, statPrimario):
        self.stat1 = statPrimario
    def setStat2(self, statSecundario):
        self.stat2 = statSecundario
    def setEnMax(self, enMax):
        self.enMax = enMax
    def setEnAtual(self, enAtual):
        self.enAtual = val_en(self, enAtual)
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
        return self.stat1
    def getStat2(self):
        return self.stat2
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
    def __del__(self):
        if self.habBuff is not None:
            del self.habBuff
            self.habBuff = None
    def setCodigoHab(self, codHab):
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
    def getCodigoHab(self):
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
    def setTempo(self, tempo):
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
            self.umStat.vida = int(self.umStat.vida * self.buffQtd)
        elif self.scale.value == 2:
            self.umStat.forca = int(self.umStat.forca * self.buffQtd)
        elif self.scale.value == 3:
            self.umStat.destreza = int(self.umStat.destreza * self.buffQtd)
        elif self.scale.value == 4:
            self.umStat.tecnica = int(self.umStat.tecnica * self.buffQtd)
        elif self.scale.value == 5:
            self.umStat.raciocinio = int(self.umStat.raciocinio * self.buffQtd)
        elif self.scale.value == 6:
            self.umStat.vida = int(self.umStat.vida * self.buffQtd)
            self.umStat.forca = int(self.umStat.forca * self.buffQtd)
            self.umStat.destreza = int(self.umStat.destreza * self.buffQtd)
            self.umStat.tecnica = int(self.umStat.tecnica * self.buffQtd)
            self.umStat.raciocinio = int(self.umStat.raciocinio * self.buffQtd)
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
        {self.buffQtd*100}% de {self.buffEscala} do {self.getAlvo()}'
class Ataques(Habilidades):
    def __init__(self, codHab: int, nomHab: str, lvlHab: int, custo: int,\
        recarga: int, umAlvo: Alvos,  descHab, atqEscala: Escalas, \
        umDado: Dados, habMult: int):
        super().__init__(codHab, nomHab, lvlHab, custo, recarga, umAlvo, descHab)
        self.scale = atqEscala
        self.habMult = habMult
        self.effHab = umDado
        self.tempoRecarga = 0
    def __del__(self):
        if self.habBuff is not None:
            del self.habBuff
            self.habBuff = None
    def setScale(self, atqEscala):
        self.scale = atqEscala
    def setBuff(self, buff):
        self.habBuff = buff
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
        rolagem = np.array([self.umDado.rolarDado() for _ in range(self.habMult)])
        np.set_printoptions(threshold=sys.maxsize)
        somaDano = np.sum(rolagem)    
        return f'Dano causado por {self.nomHab} foi {somaDano}. Dados: {np.array}'
    def habUp(self):
        return self.lvlHab + int(1)
    def __str__(self):
        return f'COD: {self.codHab} [HABILIDADE: {self.nomHab}] \
        (NÍVEL: {self.lvlHab}): {self.descHab}. Seu efeito é causar \
        {self.habMult} {self.effHab}(s)'
class Personagens(Stats):
    def __init__(self, persoNome: str, persoNivel: int, persoRaca: str, \
    persoClasse, persoStats, persoProfs, habilidades=None):
        super().__init__(persoStats.vida, persoStats.forca, persoStats.destreza, 
        persoStats.tecnica, persoStats.raciocinio, 
        persoStats.vidAtual, persoStats.vidTemp, 
        persoStats.vidMin, persoStats.statPrimario, 
        persoStats.statSecundario, persoStats.enMax, 
        persoStats.enAtual, persoStats.enMin)
        self.persoNome = persoNome
        self.persoNivel = persoNivel
        self.persoRaca = persoRaca
        self.classe = persoClasse
        self.stats = persoStats
        self.profs = persoProfs
        if habilidades is None:
            habilidades = []
        self.habilidades = habilidades
    def addSkill(self, hab):
        if not hasattr(self, 'habilidades'):
            self.habilidades = []
        self.habilidades.append(copy.deepcopy(hab))
    def setNome(self, persoNome):
        self.persoNome = persoNome
    def setNivel(self, persoNivel):
        self.persoNivel = persoNivel
    def setRaca(self, persoRaca):
        self.persoRaca = persoRaca
    def setClasses(self, persoClasse):
        self.classe = persoClasse
    def setStats(self, persoStats):
        self.stats = persoStats
    def setProfs(self, persoProfs):
        self.profs = persoProfs
    def getNome(self):
        return self.persoNome
    def getNivel(self):
        return self.persoNivel
    def getRaca(self):
        return self.persoRaca
    def getClasses(self):
        return self.classe
    def getStats(self):
        return self.stats
    def getProfs(self):
        return self.profs
    def getSkills(self):
        return list(enumerate(self.habilidades))
    def persoUp(self):
        return self.persoNivel + int(1)
    def __str__(self):
        return f'NOME: {self.persoNome} NÍVEL: {self.persoNivel} \
        RAÇA: {self.persoRaca} CLASSE: {self.classe} \
        HP: {self.stat.vidAtual} / {self.stat.vida} TEMPORÁRIO: {self.stat.vidTemp}\
        ENERGIA: {self.stat.enAtual} / {self.stat.enMax} \
        STATS: {self.stat} \
        PROFICIÊNCIAS: {self.profs} \
        HABILIDADES: {self.habilidades}'
class Guerreiros(Personagens):
    def __init__(self, persoNome: str, persoNivel: int, persoRaca: str, \
    persoClasse, persoStats, persoProfs, habilidades=None):
        super().__init__(self, persoNome, persoNivel, persoRaca, \
        persoClasse, persoStats, persoProfs, habilidades)
    
    def addSkill(self, hab):
        if not hasattr(self, 'habilidades'):
            self.habilidades = [socoPerfurante]
        self.habilidades.append(copy.deepcopy(hab))
    def persoUp(self):
        return self.persoNivel + int(1)
    def __str__(self):
        return f'NOME: {self.persoNome} NÍVEL: {self.persoNivel} \
        RAÇA: {self.persoRaca} CLASSE: {self.classe} \
        HP: {self.stat.vidAtual} / {self.stat.vida} TEMPORÁRIO: {self.stat.vidTemp}\
        ENERGIA: {self.stat.enAtual} / {self.stat.enMax} \
        STATS: {self.stat} \
        PROFICIÊNCIAS: {self.profs} \
        HABILIDADES: {self.habilidades}'
dado5 = Dados("dado5", 5, 0)
dado6 = Dados("dado6", 6, 0)
dado8 = Dados("dado8", 8, 0)
dado10 = Dados("dado10", 10, 0)
dado20 = Dados("dado20", 20, 0)
socoPerfurante= Ataques(codHab=1, nomHab="Golpe Poderoso", lvlHab=1, custo=5, \
recarga=3, umAlvo=Alvos.ENEMY,   descHab="Um ataque forte que causa dano extra.", \
atqEscala=Escalas.FOR, umDado=dado10, habMult=2)    
listaDados = [dado5, dado6, dado8, dado10, dado20]
listaStats = []
listaProfs = []
listaHabs = [socoPerfurante]                    
listaPersonagens = []
listaGuerreiros = []

continuar = int(1)
while continuar >0:
    print("1 - Cadastrar Dado")
    print("2 - Cadastrar Stats")
    print("3 - Cadastrar Proficiências")
    print("4 - Cadastrar Habilidades")
    print("5 - Cadastrar Personagem")
    print("6 - Adição de Habilidades")
    print("7 - Listar Fichas de Stats")
    print("8 - Listar Fichas de Proficiências")
    print("9 - Listar Habilidades")
    print("10 - Listar Fichas de Capacidades")
    print("11 - Listar Personagens")
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
                if (q1 == "vid" or "VID"): 
                    statPrimario = vida
                elif (q1 == "for" or "FOR"):
                    statPrimario = forca
                elif (q1 == "des" or "DES"):
                    statPrimario = destreza
                elif (q1 == "tec" or "TEC"):
                    statPrimario = tecnica
                elif (q1 == "rac" or "RAC"):
                    statPrimario = raciocinio
                else:
                    print("ATRIBUTO INVÁLIDO!")
                    break
                q2 = input("O stat secundário para obter energia é? (escreva as 3 primeiras letras do stat): ")
                if (q2 == "vid" or "VID"): 
                    statSecundario = vida
                elif (q2 == "for" or "FOR"):
                    statSecundario = forca
                elif (q2 == "des" or "DES"):
                    statSecundario = destreza
                elif (q2 == "tec" or "TEC"):
                    statSecundario = tecnica
                elif (q2 == "rac" or "RAC"):
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
                cond3 = input("O personagem possui um valor especial de en. mínima? ")
                if cond3 in ["Sim", "sim", "s", "S"]:
                    while True:
                        try:
                            enMin = int(input("Qual é o valor de energia mínima? "))
                            break
                        except ValueError:
                            print("Formato inválido, digite um número inteiro!\n")
                else:
                    enMin = 0
                stat= Stats(idStat, vida, forca, destreza, tecnica, raciocinio \
                , vidAtual, vidTemp, vidMin, statPrimario, statSecundario, \
                enAtual, enMin, enMax)
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
                            if pegarStat == stat.getIdStat():
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
                            if pegarProf == prof.getIdProf():
                                persoProfs = prof
                                break
                        if persoProfs is not None:
                            print(f"Ficha encontrada: {persoProfs.getIdProf()}")
                            break
                        else:
                            print("Nenhuma ficha encontrada, tente de novo!")
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
                if persoClasse == "Guerreiro":
                    guerreiro = Guerreiros(persoNome, persoNivel, persoRaca, persoClasse, \
                    persoStats, persoProfs) 
                    listaGuerreiros.append(guerreiro)
                    break
                else:
                    perso = Personagens(persoNome, persoNivel, persoRaca, persoClasse, \
                    persoStats, persoProfs) 
                    listaPersonagens.append(perso)
                    break
        case '6':
            print("PROCESSO 6: Adição de Habilidades:")
            print("PERSONAGENS DISPONÍVEIS:")
            for perso in listaPersonagens:
                print(perso)
            nomeEscolhido = input("Qual é o nome do personagem que receberá habilidades? ")
            perso = next((p for p in listaPersonagens if p.nome.lower() == nomeEscolhido.lower()), None)
            if perso is None:
                print("Personagem não encontrado.")
            else:
                print("HABILIDADES DISPONÍVEIS:")
                for hab in listaHabs:
                    print(f"Código: {hab.getCodigoHab()}, Nome: {hab.getNomeHab()}")
                while True:
                    try:
                        escolherHab = int(input("Qual é o código da habilidade deseja \
                        adicionar ao personagem?"))
                        habSel = False #marca que habilidade não foi selecionada ainda
                        for hab in listaHabs:
                            if escolherHab == hab.getCodigoHab():
                                perso.addSkill(hab)
                                habSel = True
                                print(f"Habilidade '{hab.getNomeHab()}' \
                                adicionada ao personagem '{perso.nome}' \
                                com sucesso!")
                                break
                        if habSel:
                            break
                        else:
                            print("Nenhuma habilidade encontrada, tente de novo!")
                    except ValueError:
                        print("Formato inválido, digite um número inteiro!\n")
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