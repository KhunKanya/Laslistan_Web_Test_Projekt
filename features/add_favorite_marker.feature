Feature: Hantera favoritböcker
# som änvändare
# vill jag markera böcker som favorit ,
# så att jag kan hålla koll på mina favoriter

  ### Acceptanskriterier ###
  # 1. Användaren kan markera en bok som favorit genom att klicka på en favoritknapp (t.ex. ett hjärta) på startsidan.
  # 2. En bok som markerats som favorit visas på "Mina böcker"-sidan


 Scenario Outline: Lägg till favoritbok
   Given Användaren är på startsidan
   When änvändare klickar på favorit-knappen för <title>
   Then ska boken <title> finnas i mina böcker-sidan

   Examples:
     | title                                              |
     | Min katt är min chef                               |
     | Hur man tappar bort sin TV-fjärr 10 gånger om dagen|

