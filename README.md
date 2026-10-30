# WordVault 2.1 – Voikko

## Käyttöönotto Renderissä

1. Päivitä WordVaultin olemassa oleva **Static Site** GitHubissa (HTML, ikonit, sw.js, manifest).
2. Luo Renderissä **New > Web Service** samasta GitHub-reposta. Runtime: **Docker**. Nimeksi `wordvault-voikko` (tai muu vapaa nimi). Dockerfile on projektin juuressa. Deploy.
3. Avaa uuden Web Servicen julkinen HTTPS-osoite, esimerkiksi `https://wordvault-voikko-xxxx.onrender.com`. Tarkista `/health`.
4. Avaa nykyinen WordVault-sivu ja syötä tämä URL kenttään **Voikko-palvelun osoite**. Osoite tallentuu selaimeen.
5. Kuvaa teksti ja paina Tunnista teksti. OCR toimii selaimessa; vain erilliset sanat lähetetään API:in.

Voikko tunnistaa sanojen taivutusmuotoja, mutta ei korjaa OCR-virheitä eikä aina ratkaise monitulkintaisia muotoja yksiselitteisesti. Tuntemattomia sanoja ei arvata. API ei tallenna sanoja. Renderin ilmainen palvelu voi nukahtaa ja ensimmäinen pyyntö voi olla hidas. Käyttö vaatii verkkoyhteyden.

## Huomio

Olemassa olevaa Render Static Site -palvelua ei tarvitse poistaa tai muuttaa Docker-palveluksi. Voikko on erillinen palvelu. `render.yaml` on esimerkkiasetus, mutta yksinkertaisin tapa on luoda Docker Web Service Renderin hallintapaneelista. `Dockerfile` asentaa Debianin libvoikko- ja voikko-fi-paketit.
