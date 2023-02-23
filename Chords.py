"""
    class Chords
    
    Attributs : RootNote, ChordQuality, ChordName, ChordInterval, ChordNotes
    
    Méthodes : initChords
"""
class Chords:
    
    listNotes = ("Cb","C","C#","Db","D","D#","Eb","E","E#","Fb","F#","Gb","G","G#","Ab","A","A#","Bb","B","B#")
    listChordInterval = {"Majeur" : ["","1 3 5"], "Mineur" : ["m","1 b3 5"], "Augmenté" : ["aug","1 3 #5"], "Diminué" : ["dim","1 b3 b5"],"Majeur 7" : ["MAJ7","1 3 5 7"], "Majeur mineur 7" : ["min7","1 3 5 b7"]}
    
    def __init__(self, attrRootNote, attrChordQuality):
        self.setRootNote(attrRootNote)
        self.setChordQuality(attrChordQuality)
        self.setChordName(attrRootNote,attrChordQuality)
        self.setChordInterval(attrChordQuality)
        self.setChordNotes(attrRootNote,attrChordQuality)

    def getRootNote(self):
        return self.__rootNote
    
    def setRootNote(self, attrRootNote):
        self.__rootNote = attrRootNote

    def getChordQuality(self):
        return self.__chordQuality
    
    def setChordQuality(self, attrChordQuality):
        self.__chordQuality = attrChordQuality

    def getChordName(self):
        return self.__chordName
    
    def setChordName(self, attrRootNote, attrChordQuality):
        if type(attrRootNote) != str:
            raise TypeError ("Erreur sur le nom de la root note.")
        list = Chords.listChordInterval[attrChordQuality]
        self.__chordName = attrRootNote + list[0]
    
    def getChordInterval(self):
        return self.__chordInterval
    
    def setChordInterval(self, attrChordQuality):
        if type(attrChordQuality) != str:
            raise TypeError("Erreur sur la liste des intervalles")
        list = Chords.listChordInterval[attrChordQuality]
        self.__chordInterval = list[1]
    
    def getChordNotes(self):
        return self.__chordNotes
        
    def setChordNotes(self, attrRootNote, attrChordQuality):
        self.__chordNotes = [attrRootNote]
        liste = Chords.listChordInterval[attrChordQuality]
        liste = liste[1]
        liste = liste.split()
        while len(liste) != 0 :
            if liste[0] == " " or liste[0] == "1":
                liste.pop(0)
                continue
            elif liste[0] == "b3": 
                indexNote = self.listNotes.index(attrRootNote) + 5
            elif liste[0] == "3":
                indexNote = self.listNotes.index(attrRootNote) + 6
            elif liste[0] == "b5":
                indexNote = self.listNotes.index(attrRootNote) + 10
            elif liste[0] == "5":
                indexNote = self.listNotes.index(attrRootNote) + 11
            elif liste[0] == "#5":
                indexNote = self.listNotes.index(attrRootNote) + 12
            elif liste[0] == "b7":
                indexNote = self.listNotes.index(attrRootNote) + 16
            elif liste[0] == "7":
                indexNote = self.listNotes.index(attrRootNote) + 17
            if indexNote > len(self.listNotes)-1:
                indexNote = indexNote - len(self.listNotes)+1
            note = self.listNotes[indexNote]
            self.__chordNotes.append(note)
            liste.pop(0)
    
    @staticmethod
    def initChords():
        listChords = []
        for i in Chords.listNotes:
            for k, v in Chords.listChordInterval.items():
                chord = Chords(i,k)
                listChords.append(chord)
        return listChords
        
if __name__ == "__main__":
    listChords = Chords.initChords()
    for i in listChords:
        print(i.getChordName() + " | " + i.getRootNote() + " " + i.getChordQuality() + " | " + str(i.getChordNotes()))