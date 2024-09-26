import pytest
from notenrechner import berechne_prozentwert, berechne_note

def test_berechne_prozentwerte():
    # Arrange
    erreichte_punkte = 85
    maximale_punkte = 100
    expected_prozent = 85.0

    # Act
    actual_prozent = berechne_prozentwert(erreichte_punkte, maximale_punkte)

    # Assert
    assert expected_prozent == actual_prozent

def test_berechne_prozentwert_zero_max_points():
    # Arrange
    erreichte_punkte = 50
    maximale_punkte = 0

    # Act and Assert
    with pytest.raises(ValueError):
        berechne_prozentwert(erreichte_punkte, maximale_punkte)

def test_berechne_prozentwert_value_error_negative_punkte():
    # Arrange
    erreichte_punkte = -10  
    max_punkte = 100
    
    # Act & Assert
    with pytest.raises(ValueError):
        berechne_prozentwert(erreichte_punkte, max_punkte)

def test_berechne_note_sehr_gut_obere_grenze():
    # Arrange
    prozent = 100
    expected_note = "sehr gut"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_sehr_gut_untere_grenze():
    # Arrange
    prozent = 92
    expected_note = "sehr gut"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_gut_obere_grenze():
    # Arrange
    prozent = 91
    expected_note = "gut"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_gut_untere_grenze():
    # Arrange
    prozent = 81
    expected_note = "gut"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_befriedigend_obere_grenze():
    # Arrange
    prozent = 80
    expected_note = "befriedigend"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_befriedigend_untere_grenze():
    # Arrange
    prozent = 67
    expected_note = "befriedigend"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_ausreichend_obere_grenze():
    # Arrange
    prozent = 66
    expected_note = "ausreichend"

    # Act
    actual_note = berechne_note(prozent)

    # Assert
    assert expected_note == actual_note

def test_berechne_note_ausreichend_untere_grenze():
    # Arrange
    prozent = 50
    expected_note = "ausreichend"

    # Act
    actual_note = berechne_note(prozent)

    # Assert
    assert expected_note == actual_note

def test_berechne_note_mangelhaft_obere_grenze():
    # Arrange
    prozent = 49
    expected_note = "mangelhaft"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_mangelhaft_untere_grenze():
    # Arrange
    prozent = 30
    expected_note = "mangelhaft"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_ungenuegend_obere_grenze():
    # Arrange
    prozent = 29
    expected_note = "ungenügend"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_note_ungenuegend_untere_grenze():
    # Arrange
    prozent = 0
    expected_note = "ungenügend"

    # Act
    actual_note = berechne_note(prozent)
    
    # Assert
    assert expected_note == actual_note

def test_berechne_prozentwert_type_error():
    # Arrange
    erreichte_punkte = "85"  
    max_punkte = 100
    
    # Act & Assert
    with pytest.raises(TypeError):
        berechne_prozentwert(erreichte_punkte, max_punkte)

def test_berechne_note_type_error():
    # Arrange
    prozentwert = "90" 
    
    # Act & Assert
    with pytest.raises(TypeError):
        berechne_note(prozentwert)
