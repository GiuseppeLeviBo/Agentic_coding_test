import click
from mandelbrot import mandelbrot_set
from render import render

@click.command()
@click.option("--center-x", default=-0.5, help="Centro X")
@click.option("--center-y", default=0.0, help="Centro Y")
@click.option("--zoom", default=1.0, help="Zoom >0")
@click.option("--iter", "max_iter", default=100, help="Iterazioni massime")
@click.option("--size", default=200, help="Dimensione immagine (quadrata)")
@click.option("--outfile", default="mandelbrot.png", help="Output file")
def generate(center_x, center_y, zoom, max_iter, size, outfile):
    """
    Genera immagine Mandelbrot.
    BUG: lo zoom non viene usato.
    """
    half_range = 1.5
    xmin, xmax = center_x - half_range, center_x + half_range
    ymin, ymax = center_y - half_range, center_y + half_range

    array = mandelbrot_set(xmin, xmax, ymin, ymax, size, size, max_iter)
    render(array, max_iter, outfile)
    click.echo(f"Immagine salvata in {outfile}")

if __name__ == "__main__":
    generate()
