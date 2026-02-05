import pytest
import numpy as np
from cosmologie import vitesse_galaxies, norme_espace

def test_vitesse_multiples():
    distances = [10, 20, 30]
    attendus = [700, 1400, 2100]
    resultats = vitesse_galaxies(distances)
    # np.testing vérifie que les tableaux sont quasi identiques
    np.testing.assert_allclose(resultats, attendus)

def test_norme_3d():
    points = [[3, 4, 12], [0, 0, 0]]
    attendus = [13.0, 0.0]
    np.testing.assert_allclose(norme_espace(points), attendus)