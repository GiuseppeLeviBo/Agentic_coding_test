import os
from mandelbrot import mandelbrot_set
from render import render

def test_render_creates_file(tmp_path):
    arr = mandelbrot_set(-2, 1, -1.5, 1.5, 50, 50, 10)
    outfile = tmp_path / "out.png"
    render(arr, 10, outfile)
    assert outfile.exists()
    assert outfile.stat().st_size > 0
