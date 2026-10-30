# WordVault Render PWA

## Julkaisu
1. Luo GitHubiin uusi repository `WordVault` (älä korvaa Uutisvirtaa).
2. Lisää tämän paketin kuusi tiedostoa repositoryn juureen.
3. Render: New > Static Site, yhdistä repository. Build Command: `echo ready`, Publish Directory: `.`.
4. Julkaise ja avaa Renderin HTTPS-osoite puhelimella.
5. Android: Chrome > Lisää aloitusnäyttöön / Asenna. iPhone: Safari > Jaa > Lisää Koti-valikkoon.

Renderin `render.yaml` on vaihtoehto Blueprint-julkaisulle. Valitse joko Static Site käsin tai Blueprint.

Sanat tallennetaan selaimen localStorageen **laitteittain**, ei Renderin palvelimelle. Käytä sovelluksen JSON-varmuuskopiointia. Älä poista sivuston tietoja ilman varmuuskopiota. OCR käyttää internetistä ladattavaa Tesseract.js-kirjastoa, joten ensimmäinen tunnistus vaatii verkkoyhteyden. OCR-tulos tarkistetaan ennen tallennusta.
