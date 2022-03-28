# PythonOpenSourceWSB
Repozytorium na zajęcia WSB

# Instrukcja uruchamiania aplikacji webowej

***Aplikacja została stworzona na potrzeby zajęć "Podstawowe narzędzia: Python i Open Source".***

## Krok 1

Aby rozpocząć pracę z aplikacją należy pobrać środowisko Python'a na swój komputer. Można to zrobić za pośrednictwem strony https://www.python.org/downloads/

## Krok 2

Repozytorium należy skopiować do folderu, w którym znajdować się będzie projekt. Następnie folder ten otwieramy w dowolnym IDE obsługującym konsolę/terminal.

## Krok 3

W folderze uruchamiamy komendę, tworzącą środowisko wirtualne z którego będziemy korzystać:

```
py -3 -m venv .venv
```
## Krok 4

Po stworzeniu środowiska wirtualnego, wybieramy w naszym IDE interpreter z tego właśnie środowiska. W Visual Studio Code można to zrobić wywołując menu, za pomocą skrótu *CTRL + SHIFT + P*, a następnie wybierając *"Python: Select Interpreter"*. Wybieramy ten, znajdujący się w podfolderze *.venv*.

## Krok 5

Uruchamiamy terminal w środowisku wirtualnym, które przed chwilą utworzyliśmy. W Visual Studio Code możemy to zrobić za pomocą skrótu *Ctrl+Shift+`*. Wtedy terminal przeładuje się nam, nawet jeśli wcześniej otwarta była jego inna instancja.

## Krok 6

Upewniamy się, że po instalacji Python'a mamy aktualną wersję instalatora Pip. Możemy zrobić to za pomocą kodu:
    
    python -m pip install --upgrade pip
    
   Jeśli jest on już aktualny, instalujemy potrzebne pakiety za pomocą komendy:
   

    pip install -r requirements.txt

Po ich aktualizacji/pobraniu instalujemy już tylko środowisko Flask:

   
    python -m pip install flask
   
  ## Krok 7

Uruchamiamy aplikację z pomocą komendy:

    python -m flask run
