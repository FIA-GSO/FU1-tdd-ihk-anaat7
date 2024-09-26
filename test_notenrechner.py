import pytest
from notenrechner import berechne_prozentwert, berechne_note 

def test_berechne__prozentwerte(self):
    #Arrange
    erreichte_punkte = 85
    maximale_punkte = 100
    expected_prozent = 85.0

    #Act
    actual_prozent = berechne_prozentwert(erreichte_punkte, maximale_punkte)

    #Assert
    self.assertEqual(expected_prozent, actual_prozent)

def test_berechne_prozentwert_zero_max_points(self):
    # Arrange
    erreichte_punkte = 50
    maximale_punkte = 0

    # Act and Assert
    with self.assertRaises(ValueError):
        berechne_prozentwert(erreichte_punkte, maximale_punkte)

def test_berechne_prozentwert_value_error_negative_punkte(self):
    # Arrange
    erreichte_punkte = -10  
    max_punkte = 100
    
    # Act & Assert
    with self.assertRaises(ValueError):
        berechne_prozentwert(erreichte_punkte, max_punkte)


def test_berechne_note__sehr_gut_obere_grenze(self):
    #Arrange
    prozent = 100
    expected_note = "Sehr gut"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__sehr_gut_untere_grenze(self):
    #Arrange
    prozent = 92
    expected_note = "Sehr gut"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__gut_obere_grenze(self):
    #Arrange
    prozent = 91
    expected_note = "Gut"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__gut_untere_grenze(self):
    #Arrange
    prozent = 81
    expected_note = "Gut"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__befriedigend_obere_grenze(self):
    #Arrange
    prozent = 80
    expected_note = "Befriedigend"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__befriedigend_untere_grenze(self):
    #Arrange
    prozent = 67
    expected_note = "Befriedigend"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__ausreichend_obere_grenze(self):
    #Arrange
    prozent = 66
    expected_note = "Ausreichend"

    #Act
    actual_note = berechne_note(prozent)

    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__ausreichend_untere_grenze(self):
    #Arrange
    prozent = 50
    expected_note = "Ausreichend"

    #Act
    actual_note = berechne_note(prozent)

    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__mangelhaft_obere_grenze(self):
    #Arrange
    prozent = 49
    expected_note = "mangelhaft"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__mangelhaft_untere_grenze(self):
    #Arrange
    prozent = 30
    expected_note = "mangelhaft"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__ungenuegend_obere_grenze(self):
    #Arrange
    prozent = 29
    expected_note = "ungenugend"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_note__ungenuegend_untere_grenze(self):
    #Arrange
    prozent = 0
    expected_note = "ungenugend"

    #Act
    actual_note = berechne_note(prozent)
    
    #Assert
    self.assertEqual(expected_note, actual_note)

def test_berechne_prozentwert_type_error(self):
    # Arrange
    erreichte_punkte = "85"  
    max_punkte = 100
    
    # Act & Assert
    with self.assertRaises(TypeError):
        berechne_prozentwert(erreichte_punkte, max_punkte)

def test_berechne_note_type_error(self):
    # Arrange
    prozentwert = "90" 
    
    # Act & Assert
    with self.assertRaises(TypeError):
        berechne_note(prozentwert)
