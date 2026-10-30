# WordVault 2.5.14 – OCR-asettelukorjaus

Pohja: WordVault 2.5.13. Korjaa tapauksen, jossa 673 × 51 pikselin kaksirivinen teksti tunnistettiin vain PSM 7 -asetuksella.

- Säilyttää PSM 7:n ensisijaisena leveille kuville.
- Jos tunnistus on heikko (paras pistemäärä alle 65), kokeilee PSM 6:ta alkuperäiselle kuvalle.
- Jos tulos on edelleen erittäin heikko (alle 45), kokeilee myös PSM 3:a.
- Kaikki tunnistukset ja raakatekstit näkyvät edelleen diagnostiikassa.
- Ei muuta Voikkoa, sanastoa, käännöksiä tai harjoittelua.

Huomaa: PSM 6 on korjausehdokas, ei vielä mobiilissa todennettu tulos. Testaa erityisesti Leo ja Elsa -kuvalla.
