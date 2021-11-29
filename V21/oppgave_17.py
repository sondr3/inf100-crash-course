# Airport codes
# 25% - 60 min 

"""
Programmet ditt skal gjøre det følgende:

-  Les data fra filen inn i passende datastrukturer (list / dict / ...). 
   Vi trenger kun informasjonen fra de 3 kolonnene som er nevnt nedenfor. ¨
   Det er nyttig å splitte koordinatene i lengde og bredde allerede her.

    Kolonne 1 ("type") viser størrelse til flyplassen, enten "medium_airport" eller "large_airport".
    Kolonne 9 ("iata_code") viser 3-bokstavs IATA koden til flyplassen (f.eks BGO for Bergen).
    Kolonne 11 ("coordinates") viser geografisk posisjon som en streng med et tall for nord-sør
               (breddegrad), et komma, et mellomrom, og et tall for øst-vest (lengdegrad).

- Bruk matplotlib for å plotte posisjonen til de ulike flyplassene på en kart. Bruk en liten prikk for
  de mellomstore flyplassene, og en større prikk for de store flyplassene. Velg en lys farge for
  prikkene.

- Bruk matplotlib.annotate( iata_code, (lengde, bredde) ) i en løkke over alle store flyplassene for
  å skrive IATA-navnet på bildet

- Sett inn en tittel og aksebeskrivelser

- Avslutt med matplotlib.show() for å åpne interaktivt modus

"""
import pandas as pd
import matplotlib.pyplot as plt

airport = pd.read_csv("airport-codes.csv", 
    delimiter=';',
    encoding='iso-8859-1',
    header=0)


airport_types = [airport_size for airport_size in airport['type']]
iata_codes = [iata for iata in airport['iata_code']]

# Alternativ 1, konvertere til float vha. map()
coordinates = [tuple(map(float, coords.split(", ")))[::-1] for coords in airport['coordinates']]

for i in range(len(airport_types)):
  if airport_types[i] == "large_airport":
    plt.scatter(coordinates[i][0], coordinates[i][1], color="orange", s=35)
    plt.annotate(iata_codes[i], coordinates[i]) # annotate takes (str, (float, float)) and coordinates is a list of tuples
  
  plt.scatter(coordinates[i][0], coordinates[i][1], color = "orange", s=15)

plt.title("Airports")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.savefig("airports.png")

plt.show()


