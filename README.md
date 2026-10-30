# WordVault 2.4

Päivitys 2.3.1-versiosta. Säilyttää OCR:n, Voikko-rajapinnan, paikallisen sanavaraston ja kuulustelun.

Uutta:
1. Sama Voikko-perusmuoto näkyy vain kerran kuvakohtaisesti.
2. Käännöksille käytetään tarkistettua pientä sanastoa ja MyMemoryn vastausten suodatusta; epävarmat ehdotukset merkitään. Tämä EI ole luotettava sanakirjavalidointi.
3. Mahdolliset vaihtoehtoiset MyMemory-käännökset näytetään valikossa.
4. Alkuperäinen lause ja mahdollinen lausekäännös näkyvät asiayhteytenä. Lausekäännös ei vahvista yksittäisen sanan merkitystä.
5. Aiemmin tallennettuja suomenkielisiä perusmuotoja ei ehdoteta uudelleen. Tallennus ohittaa myös käsin muokatut duplikaatit.

## Julkaisu
Päivitä GitHubin WordVault Static Site -tiedostot: index.html, sw.js, manifest.webmanifest, icon-192.png, icon-512.png ja README.md. Renderin toimiva Voikko-palvelu (api.py ja Dockerfile) jätetään ennalleen. render.yaml on mukana viitteenä; älä luo uusia palveluita, jos nykyiset toimivat.

Käännökset edellyttävät internetyhteyttä ja MyMemory-palvelu voi rajoittaa kyselyitä. Tarkista ehdotukset ennen tallentamista. Vanha localStorage-avain wordvault-mvp-1 säilyy.
