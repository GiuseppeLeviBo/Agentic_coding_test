import numpy as np
from mandelbrot import mandelbrot, mandelbrot_set

def test_point_inside():
    # 0 dovrebbe rimanere dentro fino al max_iter
    assert mandelbrot(0+0j, 50) == 50

def test_point_outside():
    # 2+2i diverge subito
    assert mandelbrot(2+2j, 50) < 5

def test_array_shape():
    arr = mandelbrot_set(-2, 1, -1.5, 1.5, 100, 80, 10)
    # BUG: atteso (80, 100), ma ritorna (100, 80)
    assert arr.shape == (80, 100)

