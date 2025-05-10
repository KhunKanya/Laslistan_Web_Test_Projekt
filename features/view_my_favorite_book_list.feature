Feature: Visa min favoritboklista
  # Som användare
  #  Vill jag kunna se en lista med mina favoritböcker
  #  Så att jag enkelt kan komma åt dem vid behov

  ### Acceptanskriterier ###
  # 1. Listan med favoritböcker visas korrekt
  # 2. Om inga favoritböcker finns, ska ett tydligt meddelande visas:
  #"När du valt, kommer dina favoritböcker att visas här." eller liknande


  Scenario: Inga favoritböcker finns
    Given användaren öppnar Mina böcker-sidan utan sparade favoritböcker
    Then ska ett meddelande visas: "När du valt, kommer dina favoritböcker att visas här."
    When Användaren lägger till en favoritbok
    Then Ovan meddelande syns ej längre