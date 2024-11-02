import random
import numpy as np
from typing import NewType
class STAT():
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
class PROF():
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
class HABILIDADE():
    def __init__(self, nomHab: str, lvlHab: int, descHab: str, effHab):
        self.nomHab = nomHab
        self.lvlHab = lvlHab
        self.descHab = descHab
        self.effHab = effHab
    def setNomeHab(self, nomHab):
        self.nomHab = nomHab
    def setLvlHab(self, lvlHab):
        self.lvlHab = lvlHab
    def setDescHab(self, descHab):
        self.descHab = descHab
    def setEffHab(self, effHab):
        self.effHab = effHab
    def getNomeHab(self):
        return self.nomHab
    def getLvlHab(self):
        return self.lvlHab
    def getDescHab(self):
        return self.descHab
    def getEffHab(self):
        return self.effHab
class VIDAS(STAT):
    def __init__(self, idStat, vida, vidAtual: int, vidTemp: int, vidMin: int):
        super().__init__(self, idStat, vida)
        self.vidMax = vida
        self.vidAtual = vidAtual
        self.vidTemp = vidTemp
        self.vidMin = vidMin
    def setVidMax(self, vida):
        if (vida or self.vidMax < 1):
            return False
        self.vidMax = vida
    def setVidAtual(self, vidAtual):
        if (self.vidAtual > self.vidMax):
            self.vidAtual = self.vidMax
        if (self.vidAtual < self.vidMin):
            self.vidAtual = self.vidMin
        self.vidAtual = vidAtual
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
class ENERGIAS(STAT): 
    def __init__(self, idStat, vida, forca, destreza, tecnica, raciocinio, statPrimario, statSecundario, enAtual: int, enMin: int):
        super().__init__(self, idStat, vida, forca, destreza, tecnica, raciocinio)
        self.stat1 = statPrimario
        self.stat2 = statSecundario
        self.mult1 = 1.0
        self.mult2 = 0.5
        self.enMax = int(int(self.stat1 * self.mult1) + int(self.stat2 * self.mult2))
        self.enAtual = enAtual
        self.enMin = enMin
    def setStat1(self, statPrimario):
        self.stat1 = statPrimario
    def setStat2(self, statSecundario):
        self.stat2 = statSecundario
    def setEnAtual(self, enAtual):
        if (self.enAtual > self.enMax):
            self.enAtual = self.enMax
        if (self.enAtual < self.enMin):
            self.enAtual = self.enMin
        self.enAtual = enAtual
    def setEnMin(self, enMin):
        self.enMin = 0
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
    def __str__(self):
        return f'ENERGIA: {self.enAtual} / {self.enMax}'
class PERSONAGEM():
    def __init__(self, persoNome: str, persoNivel, persoRaca: str, persoClasse, persoVidas, persoEnergia, persoStats, persoProfs):
        self.persoNome = persoNome
        self.persoNivel = persoNivel
        self.persoRaca = persoRaca
        self.classe = persoClasse
        self.hp = persoVidas
        self.ep = persoEnergia
        self.stats = persoStats
        self.profs = persoProfs
    def setStats(self, persoStats):
        self.stats = persoStats
    def setProfs(self, persoProfs):
        self.profs = persoProfs
    def getStats(self):
        return self.stats
    def getProfs(self):
        return self.profs
def rolarDado():
    dadoTipo= input("O dado possui algum multiplicador? (S/N) ")
    lados= int(input("Dado de quantos lados? "))
    match dadoTipo:
        case 'S':
            multiplicador = int(input("Qual é o valor do multiplicador? "))
            return print(f'O número rolado é {random.randint(1, lados) + multiplicador}')
        case 'N':
            return print("O número rolado é", random.randint(1, lados)) 
