# 📚 Läslistan – Web Test Projekt

## 📜 User Stories – Läslistan

Denna fil innehåller användarhistorier och tillhörande scenarier för funktionaliteten på webbsidan **Läslistan**. Scenarierna skrivs enligt **Gherkin-syntax** och är designade för att testa funktionalitet med Behave.
Totalt omfattar testningen fem funktioner: fyra funktionella tester och ett icke-funktionellt test.
---
## 1 Hantera Favoritböcker (Add favorite marker)
**Som** användare  
**vill jag** kunna markera böcker som favoriter  
**så att** jag kan hålla koll på mina favoritböcker.

### Acceptanskriterier:
- Användaren kan markera en bok som favorit genom att klicka på en favoritknapp (t.ex. ett hjärta) på startsidan.
- Boken som markerats som favorit visas på *Mina böcker*-sidan.

### Scenario 1: Lägg till favoritbok
```gherkin
Given Användaren är på startsidan
When Användaren klickar på favorit-knappen för en bok
Then Ska boken finnas på "Mina böcker"-sidan
```


## 2. Lägg till ny bok och författare (Add new book and author)
**Som** användare  
**vill jag** kunna lägga till nya böcker och författare   
**så att** jag kan hålla databasen uppdaterad.


### Acceptanskriterier
- Användaren kan fylla i både titel och författare i formuläret på "Lägg till bok"-sidan.
- När båda fälten är ifyllda och användaren klickar på "Lägg till ny bok", ska boken visas på "Katalog"-sidan.
- Om användaren lämnar något obligatoriskt fält tomt ska "Lägg till ny bok"-knappen vara inaktiv.

#### Scenario Outline: Användare lägger till en ny bok och en ny författare
```gherkin
Given Användaren är på "Lägg till bok"-sidan
When Användaren fyller i titel och författare och klickar på "Lägg till ny bok"
| Titel       | Författare        |
|-------------|-------------------|
| The Hobbit  | J.R.R. Tolkien    |
Then Ska boken som användaren fyller i fälten för titel och författare visas på "Katalog"-sidan.
```

#### Scenario: Användare försöker lägga till bok utan att ange författare
```gherkin
Scenario: Användare försöker lägga till bok utan att ange författare
  Given användare är på Lägg till bok sidan2
  When användare fyller i fälet <Titel> med "The Hobbit"  men lämnar <Författare> tomt
  Then användare kan inte att trycka på Lägg till ny bok-knappen
```
## 3. Ta bort en favoritbok (remove favorite marker)
**Som** användare 

**Vill Jag** kunna ta bort favoritmarkeringen från Mina böcker-sidan

**så att** jag kan hantera min lista med favoritböcker efter behov.

#### Acceptanskriterier
- Användaren kan ta bort en bok från sina favoriter genom att klicka på ett hjärta på startsidan 
- Efter att en bok tas bort från favoriter, ska den inte längre synas på "Mina böcker"-sidan.

#### Scenario: Ta bort en bok från favoritlistan
```gherkin
  Given användaren är på startsidan med två sparade favoritböcker2
  And böckerna "Min katt är min chef" och "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" visas i favoritlistan
  When användaren klickar på ta bort-favorit-knappen för "Min katt är min chef"
  Then "Min katt är min chef" ska inte längre visas i favoritlistan
  And "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" ska fortfarande finnas kvar
```
### 4. Visa min favoritboklista (view my favorite book list)
**som** användare

**vill jag** kunna se en lista med mina favoritböcker

**så att** jag enkelt kan komma åt dem vid behov

#### Acceptanskriterier
- Listan med favoritböcker visas korrekt
- Om inga favoritböcker finns, ska ett tydligt meddelande visas:
  "När du valt, kommer dina favoritböcker att visas här." eller liknande

#### Scenario: Inga favoritböcker finns
```gherkin
    Given användaren öppnar Mina böcker-sidan utan sparade favoritböcker
    Then ska ett meddelande visas: "När du valt, kommer dina favoritböcker att visas här."
    When Användaren lägger till en favoritbok
    Then Ovan meddelande syns ej längre
```
---

## Icke-Funktionella Tester

## 5. Webbläsarkompatibilitet (Browser Compatibility)
**som** användare

**vill jag** kunna använda olika webbläsare

**så att** jag kan få tillgång till olika webbplatser

### Acceptanskriterier 
- Systemet ska fungera i minst de senaste versionerna av Chrome, Firefox, Safari
 - UX/UI ska visas korrekt i alla stödda webbläsare.
 - Funktionaliteten (t.ex. knappar, formulär) ska vara identisk i alla stödda webbläsare.

#### Scenario: Sidan laddar snabbt
```gherkin
    Given Jag öppnar webbplatsen
    Then Laddningstiden ska vara under 3 sekunder
```
#### Scenario: Kompatibilitetstest med firefox
```gherkin
@firefox
  Scenario: Kompatibilitetstest med firefox
    Given Jag öppnar webbplatsen med firefox
    Then Sidan ska renderas korrekt
```
## Teknologi

- **Webbläsartestning**: Chrome, Firefox, 
- **Applikationsteknologi**: HTML, CSS, JavaScript

