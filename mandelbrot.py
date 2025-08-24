import numpy as np

def mandelbrot(c: complex, max_iter: int) -> int:
    """
    Calcola quante iterazioni servono perché la sequenza
    z_{n+1} = z_n^2 + c diverga, oppure max_iter se resta entro 2.
    """
    z = 0
    for n in range(max_iter):  # BUG: dovrebbe essere range(max_iter), ma parte da 0
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Ritorna una matrice (height x width) con le iterazioni per ogni pixel.
    BUG: gli assi sono invertiti → immagine ruotata.
    """
    xs = np.linspace(xmin, xmax, width)
    ys = np.linspace(ymin, ymax, height)
    result = np.empty((width, height))  # BUG: dovrebbe essere (height, width)

    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            c = x + 1j * y
            result[i, j] = mandelbrot(c, max_iter)

    return result
