#### ------ Icke-funktionella testing ------- ######

  Feature: Enkla icke-funktionella tester
  # som användare
  # vill jag kunna använda olika webbläsare,
  # så att jag kan få tillgång till olika webbplatser

  ### Acceptanskriterier ###
  # 1. Systemet ska fungera i minst de senaste versionerna av Chrome, Firefox, Safari
  # 2. UX/UI ska visas korrekt i alla stödda webbläsare.
  # 3. Funktionaliteten (t.ex. knappar, formulär) ska vara identisk i alla stödda webbläsare.

#@no_environment
  Scenario: Sidan laddar snabbt
    Given Jag öppnar webbplatsen
    Then Laddningstiden ska vara under 3 sekunder


@firefox
  Scenario: Kompatibilitetstest med firefox
    Given Jag öppnar webbplatsen med firefox
    Then Sidan ska renderas korrekt

