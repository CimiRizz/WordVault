# WordVault 2.5 – älykäs harjoittelu

Perustuu toimivaan WordVault 2.4 -versioon. OCR, Voikko ja käännökset säilyvät ennallaan.

## Uutta
- Kertaa nyt: näyttää vain erääntyneet sanat (enintään 20 / harjoitus).
- Vaikeat sanat: harjoittelee aiemmin väärin vastattuja sanoja.
- Kaikki sanat: harjoittelee myös sanoja, joiden kertaus ei ole vielä ajankohtainen.
- Oikein vastattu sana siirtyy 1, 3 ja myöhemmin pidemmille kertausväleille.
- Väärin vastattu sana siirtyy uudelleen kerrattavaksi 5 minuutin kuluttua.
- Näyttää sanaston, erääntyvien, hyvin opittujen ja vaikeiden sanojen määrät.
- Oppimishistoria tallentuu sanan mukana samaan localStorage-avaimeen `wordvault-mvp-1` ja kulkee JSON-viennissä.

## Päivitys
Päivitä vain ZIP:n 6 staattista tiedostoa GitHubiin. Säilytä toimivat `api.py` ja `Dockerfile` ennallaan.

## Huomio
Harjoittelu vertaa vastausta valittuun tallennettuun englanninkieliseen käännökseen. Samaa tarkoittavat muut vastineet voivat siksi tulla merkityiksi vääriksi. Kertausväli on yksinkertainen SM-2-tyylinen malli.

## v2.5.1
Omat sanat -näkymässä on Poista kaikki sanat -painike. Poisto edellyttää vahvistusta ja tyhjentää vain tallennetut sanat sekä niihin liittyvän harjoitteluhistorian.


## 2.5.2
Kuulustelussa seuraava sana tai tulos avautuu automaattisesti 1,6 sekunnin kuluttua vastauksen tarkistamisesta. Siirtymisen voi tehdä myös heti painikkeella.
