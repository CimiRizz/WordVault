# WordVault 2.5.10 — automaattinen tekstialue (testiversio)

Korvaa GitHubin juuritiedostot tämän paketin tiedostoilla. Render julkaisee muutoksen main-haaran commitin jälkeen.

- Vaakasuuntaiselle yhden rivin kuvalle kontrasti + Tesseract PSM 7.
- Pystysuuntaiselle moniriviselle kuvalle kuvapohjainen keskialueen tunnistus ja PSM 3; tarvittaessa rajattu PSM 11.
- Enintään kolme OCR-ajoa, ei sanalistojen yhdistämistä, yli 35 sanan ehdokkaat hylätään pisteytyksessä.
- Raakateksti hyväksytään edelleen käyttäjän toimesta ennen Voikkoa.
- Sanasto ja harjoittelu ennallaan.

HUOM: Selaimen Tesseract.js-tuloksia ei ole tässä ympäristössä testattu puhelimella. Rajaus on heuristinen eikä takaa kaikkien kuvien onnistumista.
