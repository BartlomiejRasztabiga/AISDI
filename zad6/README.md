# Link do repozytorium
[https://gitlab-stud.elka.pw.edu.pl/brasztab/brzezinski-rasztabiga-aisdi-lab]()

# Przygotowanie wirtualnego środowiska
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Uruchomienie programu
```bash
python main.py
```

# Uruchomienie testów
```bash
pytest test_main.py
```

## Podział pracy
Piotr Brzeziński:
- Część implementacji (algorytm)
- Wyświetlanie trasy

Bartłomiej Rasztabiga:
- Część implementacji (wczytywanie danych, tworzenie grafu)
- Testy jednostkowe
- Raport
