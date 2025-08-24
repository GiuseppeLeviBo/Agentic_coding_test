from PIL import Image
import numpy as np

def render(array, max_iter, outfile):
    """
    Converte la matrice di iterazioni in PNG in scala di grigi.
    BUG: normalizzazione errata (risultati troppo scuri).
    """
    norm = (array / max_iter) * 128  # BUG: dovrebbe moltiplicare per 255
    img = Image.fromarray(norm.astype(np.uint8), mode="L")
    img.save(outfile)
    return outfile
[201~from PIL import Image
import numpy as np

def render(array, max_iter, outfile):
    """
    Converte la matrice di iterazioni in PNG in scala di grigi.
    BUG: normalizzazione errata (risultati troppo scuri).
    """
    norm = (array / max_iter) * 128  # BUG: dovrebbe moltiplicare per 255
    img = Image.fromarray(norm.astype(np.uint8), mode="L")
    img.save(outfile)
    return outfile
