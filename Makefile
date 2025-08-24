
---

# 📄 `Makefile`

```makefile
run:
	python cli.py --outfile mandelbrot.png

test:
	pytest -q

coverage:
	pytest --cov=.

evaluate: test
	@echo "Valutazione automatica completata"
