# 📚 Läslistan – Web Test Projekt

Ett webbprojekt för att hantera en lista med favoritböcker, testat med BDD (Behave) och Gherkin-scenarier.

**Webbsidan som testas:** [Läslistan - Testversion](https://tap-ht24-testverktyg.github.io/exam-template/)

---
## Tester

### Vad har testats?
Jag har fokuserat på att testa den grundläggande funktionaliteten i webbsidan:
Följande funktioner har automatiskt testats:

1. **Hantera Favoritböcker**
2. **Lägg till ny bok och författare**
3. **Ta bort favoritbok**
4. **Visa lista med favoritböcker**
5. **Webbläsarkompatibilitet och grundläggande prestanda** - Icke-Funktionella Tester

## Framtidsplaner

Eftersom projektet är tänkt att byggas ut i framtiden, är det viktigt att:
- Fortsätta lägga till tester för ny funktionalitet.
- Säkerställa att existerande tester uppdateras vid förändringar i koden.

---
## Instruktioner för att starta projektet

## Installation

### Förutsättningar
- Python 3.8 eller senare
- Python Behave
- Virtuellt Python-miljö rekommenderas


### Behave (BDD-tester)
Kör alla tester:
```bash
python3 -m behave
```

### Pytest
Kör automatiserade tester:
```bash
pytest
```



## 🛠 Teknologier
- **Testramverk**: Behave (BDD)
- **Webbautomation**: Selenium WebDriver
- **Språk**: Python 3.x
- **Webbläsare**: Chrome, Firefox

## 📁 Projektstruktur
```plaintext
Project/
├── .venv/                   # Virtuell miljö
├── features/
│   ├── add_favorite_marker_feature/
│   ├── add_new_book_and_author_feature/
│   ├── none_functional_feature/
│   ├── remove_favourite_marker_feature/
│   ├── view_my_favorite_book_list_feature/
│   ├── pages/
│   │   └── base_page.py     # Basklasser för sidor
│   ├── steps/
│   │   ├── step_*.py        # Stegdefinitioner
│   └── environment.py       # Testmiljö-konfig
├── STORIES.md               # Användarhistorier
└── README.md                # Du är här
```

## Automation Pyramid ##
          [UI Tests]
             / \
            /   \
    [API Tests]  [Unit Tests]

## Kontakt

Om du har några frågor eller stöter på problem, vänligen kontakta mig via GitHub.
