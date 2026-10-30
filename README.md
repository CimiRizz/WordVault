# WordVault 2.5.15 – OCR-kohdennettu korjaus

Pohja: 2.5.14. Korjattu painetun kuvan automaattinen rajaus: suurimman riviryhmän valinta ei enää määrää ainoaa rajattua kuvaa. Tunnistetaan koko kuva ja laaja keskialue, tarvittaessa myös yläosa. Näyttökuvassa kokeillaan kaksi PSM 7 -vaihtoehtoa. Sanakohtainen sijaintivertailu voidaan näyttää vaihtoehtona vain, jos Tesseract palauttaa sanakohtaiset rajauslaatikot. Ei arvata puuttuvaa sanaa "ei". Kaikki OCR-ajot näkyvät diagnostiikassa. Voikko ja sanasto ennallaan.

Tämä on testaamaton mobiiliversio; tarkkuutta ei ole vahvistettu.
