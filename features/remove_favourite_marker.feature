Feature: Ta bort en favoritbok
# som änvändare
# Vill jag kunna ta bort favoritmarkeringen från Mina böcker-sidan
# Så att jag kan hantera min lista med favoritböcker efter behov

  ### Acceptanskriterier ###
  # 1. Användaren kan ta bort en bok från sina favoriter genom att klicka på ett hjärta på startsidan
  # 2. Efter att en bok tas bort från favoriter, ska den inte längre synas på "Mina böcker"-sidan.


Scenario: Ta bort en bok från favoritlistan
  Given användaren är på startsidan med två sparade favoritböcker2
  And böckerna "Min katt är min chef" och "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" visas i favoritlistan
  When användaren klickar på ta bort-favorit-knappen för "Min katt är min chef"
  Then "Min katt är min chef" ska inte längre visas i favoritlistan
  And "Hur man tappar bort sin TV-fjärr 10 gånger om dagen" ska fortfarande finnas kvar