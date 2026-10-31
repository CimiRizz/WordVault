# WordVault 3.0 – OCR-integraatio / maksuton MVP

Tämä paketti on **testiversio**, ei vahvistettu PaddleOCR-tuotantojulkaisu. Pohjana paikallisesti saatavilla ollut WordVault **2.5.19**. GitHub-repositorion uusinta tilaa tai erillisen Voikko-palvelun lähdekoodia ei voitu lukea (GitHub-yhteys ei toiminut).

## Sisältö
- `frontend/`: valmis WordVault-käyttöliittymä, jossa voi vaihtaa selain-OCR:n ja palvelin-OCR:n välillä. Nykyiset sanat ja Voikko-rajapinta säilyvät.
- `ocr-service/`: erillinen FastAPI/PaddleOCR-palvelu; kuvakoko-, tiedostomuoto- ja CORS-tarkistukset, terveystarkistus.
- `tests/`: automaattiset API-testit mockatulla OCR-moottorilla.

## Julkaisujärjestys
1. **Ota ensin varmuuskopio WordVaultin sanoista** (Sanat → Vie JSON-tiedosto). Älä poista selaintietoja.
2. Luo Renderiin **erillinen testipalvelu** GitHub-repositorion `ocr-service/`-hakemistosta. Render Web Service: runtime Docker, root directory `ocr-service`, Dockerfile `Dockerfile`, environment `ALLOWED_ORIGINS=https://word-vault-vey6.onrender.com`. Kokeile Free-instanssia, mutta **PaddleOCR ei välttämättä mahdu maksuttoman palvelun muistiin**.
3. Odota deployn onnistumista. Testaa `https://PALVELUSI.onrender.com/health` ja `POST /ocr` kuvaa käyttäen. `/health`-vastaus yksin ei tarkoita, että OCR-malli käynnistyy.
4. Julkaise `frontend/`-hakemiston tiedostot WordVaultin staattisen sivuston juureen. Render Static Site: julkaistava hakemisto on se hakemisto, jossa `index.html` sijaitsee.
5. Avaa WordVault → **Tekstintunnistuksen tapa** → **Uusi OCR-palvelu** → anna uuden palvelun HTTPS-juuriosoite → **Testaa OCR-palveluyhteys** → valitse kuva → **Tunnista teksti**.
6. Vertaa vähintään kolmea oikeaa kuvaa: näyttöteksti, selkeä sivu ja värikäs oppikirjan sivu. Hyväksy tunnistettu teksti vasta tarkistettuasi sen.

## Palautus
Valitse WordVaultissa **Nykyinen selain-OCR (Tesseract)**. Jos haluat palauttaa koko käyttöliittymän, julkaise aiempi `index.html` ja `sw.js`. Tallennettu sanasto käyttää edelleen avainta `wordvault-mvp-1`.

## Tietosuoja ja kustannukset
OCR-palvelu ei tallenna lähetettyjä kuvia levylle. Palvelin käsittelee kuvan muistissa, mutta verkkopalvelun lokit ja ulkopuoliset mallilataukset ovat erillisiä tietosuojakysymyksiä. Rajapinta on ilman käyttäjätunnistusta: **älä julkaise avoimena tuotantokäyttöön ilman käyttörajoituksia**. CORS ei ole autentikointia. Renderin ilmaisrajoitukset, muistinkäyttö, kylmäkäynnistykset ja mallilataukset voivat estää onnistuneen ajon; 0 €/kk ei ole todennettu. PaddleOCR:n mallien ja pakettien todellista käynnistymistä ei ole voitu testata tässä ympäristössä.

## Paikallinen API-testi
`cd ocr-service` → `pip install -r requirements.txt` → `uvicorn app:app --reload --port 10000`.
Testit: `PYTHONPATH=ocr-service pytest -q tests/` (testiriippuvuudet: `pytest`, `httpx`).
