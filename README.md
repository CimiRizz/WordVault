# WordVault 2.5.17 – sijaintipohjainen OCR-ehdotus

Perustuu 2.5.16-versioon. Säilyttää PSM 6 -polun ja sanaston.

Näyttökuvien kahdesta PSM 7 -ajosta muodostetaan vain tarkistettava vaihtoehto, kun Tesseract palauttaa luotettavat sanakohtaiset koordinaatit. Tunnistus ei lisää puuttuvaa sanaa ”ei” arvauksena. Jos koordinaatteja ei ole, nykyinen tulos säilyy.

Testaa sama näyttökuva ja varmista, että painikkeella tarjottu vaihtoehto sisältää sanan kamera sekä lauseen lopun. Tulos voi edelleen sisältää virheitä.

Asennus: korvaa GitHubin WordVault-repositorion juuren kuusi tiedostoa ja tee commit. Älä tyhjennä mobiiliselaimen paikallista tallennustilaa.
