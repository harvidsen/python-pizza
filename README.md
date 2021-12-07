# Python og Pizza

Demonstrasjon av diverse gøye ting man kan gjøre med python, med pizza på si.

## Installguide

Vi anbefaler at du installerer Python og Visual Studio Code i forkant av
arrangementet.

- Python kan du installere ved å opne Microsoft Store på din BKK-PC, og der
  installere Python 3.9.
- Visual Studio Code kan du laste ned her: https://code.visualstudio.com/

I Visual Studio Code kjem vi til å bruke eit verktøy som heiter Jupyter
Notebook. Ein liten guide for oppsett av det finner du
[her](https://towardsdatascience.com/installing-jupyter) (frå "Installing the
Jupyter Extension" og nedover).

### Python dependencies

Til slutt må dere installere kjente Python-biblioteker. Her har vi lagt opp til
pakkehåndtering på 3 forskjellige måter.

1. `pip`: Python sin innebygde pakke manager. Dette innstallerer pakker rett på aktiv python installasjon.

```cmd
python -m pip install pandas numpy requests scikit-learn azure-storage-blob jupyter matplotlib seaborn
```

2. [`poetry`](https://python-poetry.org/docs/): En av mange verktøy for _dependency management_ i python. Dette lager et nytt virtuelt mijlø for dette prosjektet.

```bash
poetry install
poetry shell
```

3. [`nix`](https://nixos.org/guides/install-nix.html): Et verktøy for fullstendig dependency management på unix lignende systemer. Veldig mektig, men bratt læringskurve.

```bash
nix-shell
```

## Litt ekstra notater

Åpne `.ipynb`-filer for å åpne Jupyter Notebooks som vi har laget. Åpne
`.py`-filer for å åpne Python-filer som vi har laget. Jupyter Notebook-filene
våre kjører Python i bakgrunnen, men gjør også mye annet moro slik at dere ikke
trenger å tenke så altfor mye på tekniske detaljer. Håper vi.
