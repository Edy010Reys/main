
class Individual:

    __number = 1
    __genotypes = ('AA', 'Ai', 'BB', 'Bi', 'AB', 'ii')

    def __init__(self, genotype, name=''):
        if not isinstance(genotype, str):
            raise TypeError('Argument must be string')

        self.__genotype = genotype
        self.__name = name 

        if name == '':
            self.__name = 'Indiv' + str(Individual.__number)
            Individual.__number += 1

        if self.__genotype not in Individual.__genotypes: 
            raise TypeError('Invalid format of genotype')

    def __str__(self):
        return '(Name: %s, Genotype: %s)' % (self.__name, self.__genotype)       

    @property
    def name(self):
        return self.__name

    @property
    def genotype(self):
        return self.__genotype

    @property
    def blood_type(self):
        if self.__genotype == 'AA' or self.__genotype == 'Ai':
            return 'A'
        if self.__genotype == 'BB' or self.__genotype == 'Bi':
            return 'B'
        if self.__genotype == 'AB':
            return 'AB' 
        if self.__genotype == 'ii':
            return 'O'    

    @property
    def agglutinogens(self):
        if self.__genotype == 'AA' or self.__genotype == 'Ai':
            return 'A'
        if self.__genotype == 'BB' or self.__genotype == 'Bi':
            return 'B'
        if self.__genotype == 'AB':
            return 'A and B'
        if self.__genotype == 'ii':
            return "Don't have"

    @property
    def agglutinins(self):
        if self.__genotype == 'AA' or self.__genotype == 'Ai':
            return 'B'
        if self.__genotype == 'BB' or self.__genotype == 'Bi':
            return 'A'
        if self.__genotype == 'AB':
            return "Don't have"
        if self.__genotype == 'ii':
            return 'A and B'

    def offsprings_genotypes(self, g):
        gene = list()
        alel = list()
        for x1 in self.__genotype:
            for l1 in g.__genotype:
                gene.append(x1 + l1) 
        
        for l2 in gene:
            if l2 == 'iA':
                l2 = 'Ai'
            if l2 == 'iB':
                l2 = 'Bi'
            if l2 == 'BA':
                l2 = 'AB'
            if l2 not in alel:
                alel.append(l2)
        alel.sort()
        return alel

    def offsprings_blood_types(self, g):
        gene = list()
        alel = list()
        for x1 in self.__genotype:
            for l1 in g.__genotype:
                gene.append(x1 + l1) 
        
        for l2 in gene:
            if l2 == 'iA':
                l2 = 'Ai'
            if l2 == 'iB':
                l2 = 'Bi'
            if l2 == 'BA':
                l2 = 'AB'
            if l2 == 'AA' or l2 == 'Ai':
                l2 = 'A'
            if l2 == 'BB' or l2 == 'Bi':
                l2 = 'B'
            if l2 == 'ii':
                l2 = 'O'
            if l2 not in alel:
                alel.append(l2)
            alel.sort()
        return alel 

    def can_donate(self, g):
        if self.__genotype == 'AA' or self.__genotype == 'Ai':
            if g.__genotype == 'AA' or g.__genotype == 'Ai':
                return True
            elif g.__genotype == 'BB' or g.__genotype == 'Bi':
                return False
            elif g.__genotype == 'AB':
                return True
            elif g.__genotype == 'ii':
                return False
        elif self.__genotype == 'BB' or self.__genotype == 'Bi':
            if g.__genotype == 'AA' or g.__genotype == 'Ai':
                return False
            elif g.__genotype == 'BB' or g.__genotype == 'Bi':
                return True
            elif g.__genotype == 'AB':
                return True
            elif g.__genotype == 'ii':
                return False
        elif self.__genotype == 'AB':
            if g.__genotype == 'AA' or g.__genotype == 'Ai':
                return False
            elif g.__genotype == 'BB' or g.__genotype == 'Bi':
                return False
            elif g.__genotype == 'AB':
                return True
            elif g.__genotype == 'ii':
                return False
        elif self.__genotype == 'ii':
            return True

    def can_receive(self, g):
        if self.__genotype == 'AA' or self.__genotype == 'Ai':
            if g.__genotype == 'AA' or g.__genotype == 'Ai':
                return True
            elif g.__genotype == 'BB' or g.__genotype == 'Bi':
                return False
            elif g.__genotype == 'AB':
                return False
            elif g.__genotype == 'ii':
                return True  
        elif self.__genotype == 'BB' or self.__genotype == 'Bi':
            if g.__genotype == 'AA' or g.__genotype == 'Ai':
                return False
            elif g.__genotype == 'BB' or g.__genotype == 'Bi':
                return True
            elif g.__genotype == 'AB':
                return False
            elif g.__genotype == 'ii':
                return True
        elif self.__genotype == 'AB':
            return True
        elif self.__genotype == 'ii':
            if g.__genotype == 'AA' or g.__genotype == 'Ai':
                return False
            elif g.__genotype == 'BB' or g.__genotype == 'Bi':
                return False
            elif g.__genotype == 'AB':
                return False
            elif g.__genotype == 'ii':
                return True
