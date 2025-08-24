# Mandelbrot Explorer (Repo Seed)

Progetto didattico: un generatore di immagini dell’insieme di Mandelbrot.
A scopo didattico per confrontare in classe i diversi agenti di per il coding
alcuni bug sono stati lasciati per verificare se gli agenti sono in grado di trovarli.
Potete clonare il progetto in una directory togliere i commenti che indicano i bug e fateli trovare all'agente.
## Funzionalità
- Calcolo iterazioni per pixel
- Rendering in PNG in scala di grigi
- CLI per generare immagini

## Da fare (studenti / agenti)
- Correggere i bug:
  - assi invertiti
  - normalizzazione scorretta
  - zoom ignorato
- Estendere con nuove feature:
  - palette colore
  - supporto Julia set
  - esportazione alta risoluzione
- Aggiungere test
- Migliorare documentazione

## Uso rapido
```bash
pip install -r requirements.txt
python cli.py --outfile prova.png
