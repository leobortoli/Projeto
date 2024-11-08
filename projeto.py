import random
import numpy as np
from typing import NewType
def val_en(self, enAtual):
    if enAtual > self.enMax:
        return self.enMax
    elif enAtual < self.enMin:
        return self.enMin
    else:
        return enAtual
def val_hp(self, vidAtual):
    if (self.vidAtual > self.vidMax):
        return self.vidMax
    if (self.vidAtual < self.vidMin):
        return self.vidMin
    else:
        return vidAtual
def rolarDado():
    dadoTipo= input("O dado possui algum multiplicador? (S/N) ")
    lados= int(input("Dado de quantos lados? "))
    match dadoTipo:
        case 'S':
            multiplicador = int(input("Qual é o valor do multiplicador? "))
            return print(f'O número rolado é {random.randint(1, lados) + multiplicador}')
        case 'N':
            return print("O número rolado é", random.randint(1, lados))
class Stats():
    def __init__(self, idStat, vida: int, forca:int, destreza: int, tecnica: int, raciocinio: int):
        self.idStat = idStat
        self.vida = vida
        self.forca = forca
        self.destreza = destreza
        self.tecnica = tecnica
        self.raciocinio = raciocinio
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
    def __str__(self):
        return f'VIDA: {self.vida}, FORÇA: {self.forca}, DESTREZA: {self.destreza}, TÉCNICA: {self.tecnica}, RACIOCÍNIO: {self.raciocinio}'
class Profs():
    def __init__(self, idProf, mecanismo: int, externo: int, interno: int, exotico: int):
        self.idProf = idProf
        self.mecanismo = mecanismo
        self.externo = externo
        self.interno = interno
        self.exotico = exotico
    def setMec(self, mecanismo):
        self.mecanismo = mecanismo
    def setExt(self, externo):
        self.externo = externo
    def setInt(self, interno):
        self.interno = interno
    def setExo(self, exotico):
        self.exotico = exotico
    def getMec(self):
        return self.mecanismo
    def getExt(self):
        return self.externo
    def getInt(self):
        return self.interno
    def getExo(self):
        return self.exotico
    def __str__(self):
        return f'MEC: {self.mecanismo}, EXT: {self.externo}, INT: {self.interno}, EXO: {self.exotico}'
class Habilidades():
    def __init__(self, codHab: int ,nomHab: str, lvlHab: int, descHab: str, effHab):
        self.codHab = codHab
        self.nomHab = nomHab
        self.lvlHab = lvlHab
        self.descHab = descHab
        self.effHab = effHab
    def setCodigoHab(self, codHab):
        self.codHab = codHab
    def setNomeHab(self, nomHab):
        self.nomHab = nomHab
    def setLvlHab(self, lvlHab):
        self.lvlHab = lvlHab
    def setDescHab(self, descHab):
        self.descHab = descHab
    def setEffHab(self, effHab):
        self.effHab = effHab
    def getCodigoHab(self):
        return self.codHab
    def getNomeHab(self):
        return self.nomHab
    def getLvlHab(self):
        return self.lvlHab
    def getDescHab(self):
        return self.descHab
    def getEffHab(self):
        return self.effHab
    def __str__(self):
        return f'COD: {self.codHab} [HABILIDADE: {self.nomHab}] (NÍVEL: {self.lvlHab}): {self.descHab}. Seu efeito é {self.effHab}'
class Capacidade():
    def __init__(self, habilidade):
        self.skills = habilidade
class Vidas(Stats):
    def __init__(self, idStat, vida, forca, destreza, tecnica, raciocinio, vidAtual: int, vidTemp: int, vidMin: int):
        super().__init__(idStat, vida, forca, destreza, tecnica, raciocinio)
        self.vidMax = vida
        self.vidAtual = val_hp(self, vidAtual)
        self.vidTemp = vidTemp
        self.vidMin = vidMin
    def setVidMax(self, vida):
        if (vida or self.vidMax < 1):
            return False
        self.vidMax = vida
    def setVidAtual(self, vidAtual):
        self.vidAtual = val_hp(self, vidAtual)
    def setVidTemp(self, vidTemp):
        self.vidTemp = vidTemp
    def setVidMin(self):
        self.vidMin = (self.vidMax *-1)
    def getVidMax(self):
        return self.vidMax
    def getVidAtual(self):
        return self.vidAtual
    def getVidTemp(self):
        return self.vidTemp
    def getVidMin(self):
        return self.vidMin
    def __str___(self):
        return f'HP: {self.vidAtual} / {self.vidMax} TEMPORÁRIO: {self.vidTemp}'
class Energias(Stats): 
    def __init__(self, idStat, vida, forca, destreza, tecnica, raciocinio, statPrimario, statSecundario, enAtual: int, enMin: int, enMax = None):
        super().__init__(self, idStat, vida, forca, destreza, tecnica, raciocinio)
        self.stat1 = statPrimario
        self.stat2 = statSecundario
        self.mult1 = 1.0
        self.mult2 = 0.5        
        if self.enMax is not None:
            self.enMax = enMax
        else:
            self.enMax = int(int(self.stat1 * self.mult1) + int(self.stat2 * self.mult2))
        self.enAtual = val_en(self, enAtual)
        if self.enMin < 0:
            self.enMin = enMin
        else:
            self.enMin = 0
    def setStat1(self, statPrimario):
        self.stat1 = statPrimario
    def setStat2(self, statSecundario):
        self.stat2 = statSecundario
    def setEnAtual(self, enAtual):
        self.enAtual = val_en(self, enAtual)
    def setEnMin(self, enMin): 
        self.enMin = enMin
    def setEnMax(self, enMax):
        self.enMax = enMax
    def getStat1(self):
        return self.stat1
    def getStat2(self):
        return self.stat2
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
    def setEnMin(self):
        return self.enMin
    def setEnMax(self):
        return self.enMax
    def __str__(self):
        return f'ENERGIA: {self.enAtual} / {self.enMax}'
class Personagens():
    def __init__(self, persoNome: str, persoNivel, persoRaca: str, persoClasse, persoVida, persoEnergia, persoStats, persoProfs, persoSkills):
        self.persoNome = persoNome
        self.persoNivel = persoNivel
        self.persoRaca = persoRaca
        self.classe = persoClasse
        self.hp = persoVida
        self.ep = persoEnergia
        self.stats = persoStats
        self.profs = persoProfs
        self.habilidades = persoSkills
    def setNome(self, persoNome):
        self.persoNome = persoNome
    def setNivel(self, persoNivel):
        self.persoNivel = persoNivel
    def setRaca(self, persoRaca):
        self.persoRaca = persoRaca
    def setClasses(self, persoClasse):
        self.classe = persoClasse
    def setHP(self, persoVida):
        self.hp = persoVida
    def setEP(self, persoEnergia):
        self.ep = persoEnergia
    def setStats(self, persoStats):
        self.stats = persoStats
    def setProfs(self, persoProfs):
        self.profs = persoProfs
    def setSkills(self, persoSkills):
        self.habilidades = persoSkills
    def getNome(self):
        return self.persoNome
    def getNivel(self):
        return self.persoNivel
    def getRaca(self):
        return self.persoRaca
    def getClasses(self):
        return self.classe
    def getHP(self):
        return self.hp
    def getEP(self):
        return self.ep
    def getStats(self):
        return self.stats
    def getProfs(self):
        return self.profs
    def getSkills(self):
        return self.habilidades
    def __str__(self):
        return f'NOME: {self.persoNome} NÍVEL: {self.persoNome} \
        RAÇA: {self.persoRaca} CLASSE: {self.persoClasse} \
        HP: {self.vidAtual} / {self.vidMax} TEMPORÁRIO: {self.vidTemp} + ENERGIA: {self.enAtual} / {self.enMax} \
        STATS: {self.stats} \
        PROFICIÊNCIAS: {self.profs} \
        HABILIDADES: {self.habilidades}'

listaStats = []
listaProfs = []
listaHabs = []
listaCapc = []
listaHPs = []
listaEPs = []
listaPesonagens = []
continuar = int(1)

while continuar >0:
    print("1 - Cadastrar Stats")
    print("2 - Cadastrar Proficiências")
    print("3 - Cadastrar Habilidades")
    print("4 - Cadastrar Capacidades")
    print("5 - Cadastrar")
    print("6 - Cadastrar")
    print("7 - Cadastrar Personagem")
    print("8 - Listar Fichas de Stats")
    print("9 - Listar Fichas de Proficiências")
    print("10 - Listar Habilidades")
    print("11 - Listar Fichas de Capacidades")
    print("12 - Listar Personagens")