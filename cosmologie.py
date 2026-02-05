import numpy as np

HUBBLE_CONSTANT = 70.0  # km/s/Mpc

def vitesse_galaxies(distances):
    """
    Prend une liste (ou un array NumPy) de distances 
    et calcule toutes les vitesses d'un coup.
    """
    distances_array = np.array(distances)
    if np.any(distances_array < 0):
        raise ValueError("Les distances ne peuvent pas être négatives.")
    return distances_array * HUBBLE_CONSTANT

def norme_espace(vecteurs):
    """Calcule la distance euclidienne pour plusieurs points en 3D."""
    v = np.array(vecteurs)
    return np.linalg.norm(v, axis=1)