class Song:
    
    # Liste des accords existants (tuple car non amené à être modifié)
    listeAccord = ("C", "Cm", "Cdim", "CMAJ7", "C7", "Cm7", "C7b5", 
                   "C#", "C#m", "C#dim", "C#MAJ7", "C#7", "C#m7", "C#7b5",
                   "Cb", "Cbm", "Cbdim", "CbMAJ7", "Cb7", "Cbm7", "Cb7b5",
                   "Db", "Dbm", "Dbdim", "DbMAJ7", "Db7", "Dbm7", "Db7b5",
                   "D", "Dm", "Ddim", "DMAJ7", "D7", "Dm7", "D7b5",
                   "D#", "D#m", "D#dim", "D#MAJ7", "D#7", "D#m7", "D#7b5",
                   "Eb", "Ebm", "Ebdim", "EbMAJ7", "Eb7", "Ebm7", "Eb7b5",
                   "E", "Em", "Edim", "EMAJ7", "E7", "Em7", "E7b5",
                   "E#", "E#m", "E#dim", "E#MAJ7", "E#7", "E#m7", "E#7b5",
                   "Fb", "Fbm", "Fbdim", "FbMAJ7", "Fb7", "Fbm7", "Fb7b5",
                   "F", "Fm", "Fdim", "FMAJ7", "F7", "Fm7", "F7b5",
                   "F#", "F#m", "F#dim", "F#MAJ7", "F#7", "F#m7", "F#7b5",
                   "Gb", "Gbm", "Gbdim", "GbMAJ7", "Gb7", "Gbm7", "Gb7b5",
                   "G", "Gm", "Gdim", "GMAJ7", "G7", "Gm7", "G7b5",
                   "G#", "G#m", "G#dim", "G#MAJ7", "G#7", "G#m7", "G#7b5",
                   "Ab", "Abm", "Abdim", "AbMAJ7", "Ab7", "Abm7", "Ab7b5",
                   "A", "Am", "Adim", "AMAJ7", "A7", "Am7", "A7b5",
                   "A#", "A#m", "A#dim", "A#MAJ7", "A#7", "A#m7", "A#7b5",
                   "Bb", "Bbm", "Bbdim", "BbMAJ7", "Bb7", "Bbm7", "Bb7b5",
                   "B", "Bm", "Bdim", "BMAJ7", "B7", "Bm7", "B7b5",
                   "B#", "B#m", "B#dim", "B#MAJ7", "B#7", "B#m7", "B#7b5")
    
    # Répertoire des accords par tonalité (dictionnaire)
    GbChords = {"I" : "Gb","IIm" : "Abm","IIIm" : "Bbm","IV" : "Cb","V" : "Db","VIm" : "Ebm","VIIdim" : "Fdim",
                "IMAJ7" : "GbMAJ7","IIm7" : "Abm7","IIIm7" : "Bbm7","IVMAJ7" : "CbMAJ7","V7" : "Db7","VIm7" : "Ebm7","VIIm7b5" : "Fm7b5"}
    DbChords = {"I" : "Db","IIm" : "Ebm","IIIm" : "Fm","IV" : "Gb","V" : "Ab","VIm" : "Bbm","VIIdim" : "Cdim",
                "IMAJ7" : "DbMAJ7","IIm7" : "Ebm7","IIIm7" : "Fm7","IVMAJ7" : "GbMAJ7","V7" : "Ab7","VIm7" : "Bbm7","VIIm7b5" : "Cm7b5"}
    AbChords = {"I" : "Ab","IIm" : "Bbm","IIIm" : "Cm","IV" : "Db","V" : "Eb","VIm" : "Fm","VIIdim" : "Gdim",
                "IMAJ7" : "AbMAJ7","IIm7" : "Bbm7","IIIm7" : "Cm7","IVMAJ7" : "DbMAJ7","V7" : "Eb7","VIm7" : "Fm7","VIIm7b5" : "Gm7b5"}
    EbChords = {"I" : "Eb","IIm" : "Fm","IIIm" : "Gm","IV" : "Ab","V" : "Bb","VIm" : "Cm","VIIdim" : "Ddim",
                "IMAJ7" : "EbMAJ7","IIm7" : "Fm7","IIIm7" : "Gm7","IVMAJ7" : "AbMAJ7","V7" : "Bb7","VIm7" : "Cm7","VIIm7b5" : "Dm7b5"}
    BbChords = {"I" : "Bb","IIm" : "Cm","IIIm" : "Dm","IV" : "Eb","V" : "F","VIm" : "Gm","VIIdim" : "Adim",
                "IMAJ7" : "BbMAJ7","IIm7" : "Cm7","IIIm7" : "Dm7","IVMAJ7" : "EbMAJ7","V7" : "F7","VIm7" : "Gm7","VIIm7b5" : "Am7b5"} 
    FChords = {"I" : "F","IIm" : "Gm","IIIm" : "Am","IV" : "Bb","V" : "C","VIm" : "Dm","VIIdim" : "Edim",
               "IMAJ7" : "FMAJ7","IIm7" : "Gm7","IIIm7" : "Am7","IVMAJ7" : "BbMAJ7","V7" : "C7","VIm7" : "Dm7","VIIm7b5" : "Em7b5"}
    CChords = {"I" : "C","IIm" : "Dm","IIIm" : "Em","IV" : "F","V" : "G","VIm" : "Am","VIIdim" : "Bdim",
               "IMAJ7" : "CMAJ7","IIm7" : "Dm7","IIIm7" : "Em7","IVMAJ7" : "FMAJ7","V7" : "G7","VIm7" : "Am7","VIIm7b5" : "Bm7b5"}
    GChords = {"I" : "G","IIm" : "Am","IIIm" : "Bm","IV" : "C","V" : "D","VIm" : "Em","VIIdim" : "F#dim",
               "IMAJ7" : "GMAJ7","IIm7" : "Am7","IIIm7" : "Bm7","IVMAJ7" : "CMAJ7","V7" : "D7","VIm7" : "Em7","VIIm7b5" : "F#m7b5"}
    DChords = {"I" : "D","IIm" : "Em","IIIm" : "F#m","IV" : "G","V" : "A","VIm" : "Bm","VIIdim" : "C#dim",
               "IMAJ7" : "DMAJ7","IIm7" : "Em7","IIIm7" : "F#m7","IVMAJ7" : "GMAJ7","V7" : "A7","VIm7" : "Bm","VIIm7b5" : "C#m7b5"}
    AChords = {"I" : "A","IIm" : "Bm","IIIm" : "C#m","IV" : "D","V" : "E","VIm" : "F#m","VIIdim" : "G#dim",
               "IMAJ7" : "AMAJ7","IIm7" : "Bm7","IIIm7" : "C#m7","IVMAJ7" : "DMAJ7","V7" : "E7","VIm7" : "F#m7","VIIm7b5" : "G#m7b5"}
    EChords = {"I" : "E","IIm" : "F#m","IIIm" : "G#m","IV" : "A","V" : "B","VIm" : "C#m","VIIdim" : "D#dim",
               "IMAJ7" : "EMAJ7","IIm7" : "F#m7","IIIm7" : "G#m7","IVMAJ7" : "AMAJ7","V7" : "B7","VIm7" : "C#m7","VIIm7b5" : "D#m7b5"}
    BChords = {"I" : "B","IIm" : "C#m","IIIm" : "D#m","IV" : "E","V" : "F#","VIm" : "G#m","VIIdim" : "A#dim",
               "IMAJ7" : "BMAJ7","IIm7" : "C#m7","IIIm7" : "D#m7","IVMAJ7" : "EMAJ7","V7" : "F#7","VIm7" : "G#m7","VIIm7b5" : "A#m7b5"}
    FdChords = {"I" : "F#","IIm" : "G#m","IIIm" : "A#m","IV" : "B","V" : "C#","VIm" : "D#m","VIIdim" : "E#dim",
                "IMAJ7" : "F#MAJ7","IIm7" : "G#m7","IIIm7" : "A#m7","IVMAJ7" : "BMAJ7","V7" : "C#7","VIm7" : "D#m7","VIIm7b5" : "E#m7b5"}
    # Répertoire des tonalités (dictionnaire)
    Tonalite = {"Gb / Ebm" : GbChords, "Db / Bbm" : DbChords, "Ab / Fm" : AbChords,"Eb / Cm" : EbChords, "Bb / Gm" : BbChords,"F / Dm" : FChords, "C / Am" : CChords, "G / Em" : GChords, "D / Bm" : DChords, "A / F#m"  : AChords, "E / C#m" : EChords, "B / G#m" : BChords, "F# / D#m" : FdChords}
    
    def __init__(self):
        #self.__name()
        self.setChords()
        #self.__lyrics()
    
    def getChords(self):
        return self.__chords
    
    def setChords(self):
        self.__chords = []
        valeurInput = input("Quel est le premier accord du morceau ? ")
        valeurInput = valeurInput.replace(" ","")
        while valeurInput != "OK":
            while valeurInput not in self.listeAccord:
                valeurInput = input("Erreur. Je n'accepte que les accords X, Xm, Xdim, XMAJ7, X7, Xm7, X7b5 avec X remplacé par les notes C, D, E, F, G, A, B.\nQuel est l'accord ? ")
            self.__chords.append(valeurInput)
            valeurInput = input("Quel est le prochain accord ? S'il n'y a plus d'accord à ajouter, indiquer OK. ")
            valeurInput = valeurInput.replace(" ","")

    def tonalite(self) -> list:
        
        songTonalite = []
        
        songChords = self.getChords()
        
        for i, j in self.Tonalite.items():
            testTonalite = j
            l = 0
            while l < len(songChords) and testTonalite != "Non trouvé":
                if songChords[l] in testTonalite.values():
                    pass
                else:
                    testTonalite = "Non trouvé"
                l += 1
            if testTonalite != "Non trouvé":
                songTonalite.append(i)
        return songTonalite
    
    def progression(self) -> dict:
        """
        Remplace chaque accord par sa position dans la tonalité (I, II, III...) pour chaque tonalité possible du morceau appelé
        Affiche les résultats (print d'une ligne par tonalité)

        Returns:
            dict: liste des positions de chaque accord dans l'ordre
        """
        
        # On récupère la tonalité du morceau -> liste d'une ou plusieurs tonalités possibles
        songTonalite = self.tonalite()
        
        # On récupère les accords du morceau -> liste
        songChords = self.getChords()
        
        # On intialise le dictionnaire qui va stocker les résultats (clé = tonalité, valeur = liste des positions de la progression)
        resultatProgression = {}
        
        # On va parcourir la liste de toutes les tonalités (on va faire le travail pour chaque tonalité possible)
        for i in songTonalite:
        
            # On réinitialise la liste qui stockera la progression des positions pour cette tonalité
            progression = []
         
            # On récupère les accords de la tonalité étudiée -> dictionnaire
            tonaliteChords = self.Tonalite[i]
            
            # On va parcourir la liste des accords du morceau
            for j in songChords:
                
                # On va aller chercher la clé correspondant à l'accord dans la tonalité étudiée
                for k, v in tonaliteChords.items():
                    
                    # Si la valeur de l'accord de la tonalité est égale à l'accord de songChords
                    if v == j:
                        
                        # Alors on ajoute la clé à la liste de la progression
                        progression.append(k)
            
            # On a fini de parcourir la liste des accords pour cette tonalité, on vstocke 
            resultatProgression[i] = progression
            
        # On affiche les résultats : une ligne pour chaque tonalité
        for k, v in resultatProgression.items():
            print(f"Pour la tonalité {k} : {v}.")
        
        # On renvoie le dictionnaire au cas où on en a besoin ailleurs
        return resultatProgression


if __name__ == "__main__":
    song = Song()
    print(f"\nLes accords {song.getChords()} se retrouvent dans la/les tonalité/s suivante/s : {song.tonalite()}\n")
    print(f"\nIl s'agit de l'enchainement d'accords : \n")
    song.progression()
            