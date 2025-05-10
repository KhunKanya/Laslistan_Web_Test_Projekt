Feature: Add New Book and Author
# Som användare
# Vill jag kunna lägga till en ny bok och en ny författare
# Så att jag kan hålla databasen uppdaterad med nya böcker och deras författare.

  ### Acceptanskriterier ###
  # 1. Användaren kan fylla i både titel och författare i formuläret på Lägg till bok-sidan
  # 2. När båda fälten är ifyllda och användaren klickar på "Lägg till ny bok" så ska boken visas på Katalog-sidan.
  # 3. Om användaren lämnar något obligatoriskt fält tomt (titel eller författare), ska "Lägg till ny bok"-knappen vara inaktiv


Scenario Outline: Användare lägger till en ny bok och en ny författare
  Given användare är på Lägg till bok sidan
  When användare fyller i fälten <Titel> och <Författare>
  Examples:
   | Titel       | Författare        |
   | The Hobbit  | J.R.R. Tolkien    |
  Then boken som användare fyller i fälten ska visas i Katalog-sidan


Scenario: Användare försöker lägga till bok utan att ange författare
  Given användare är på Lägg till bok sidan2
  When användare fyller i fälet <Titel> med "The Hobbit"  men lämnar <Författare> tomt
  Then användare kan inte att trycka på Lägg till ny bok-knappen






