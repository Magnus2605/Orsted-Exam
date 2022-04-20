__________________________________________________________________________________________________________________________________________________________________________________________________________________

Forecast Module
__________________________________________________________________________________________________________________________________________________________________________________________________________________

## Introduktion

Dette er et modul der er tiltænkt som et vejrudsigtsmodul. 
Formålet med modulet er at overføre vejrinformation fra .csv filer. 
Vejrinformationen fra .csv filen ses som data til beregning.
Dataen består af tidspunkt, vindretning og vindstyrke.
Med disse data er det muligt at:

Se datointerval og antal af målinger.")

Se den maksimale vindhastighed for hver enkel dag og samlet for alle dage.")

Se graf der viser hyppigheden for vindretningerne.")

Se graf der viser middelhastighed for hver vindretning.")

Se graf der viser vindretningen for hver enkel dato.")

__________________________________________________________________________________________________________________________________________________________________________________________________________________

## Valg af teknologier

Programmeringssprog: python.
I modulet er der gjort brug af software bibliotekerne "csv", "pandas" og "matplotlib".

csv:
"csv" bruges til at læse .csv filer samt lette arbejdet med at behandle data fra .csv filer. 
csv gør det muligt at ændre i .csv filen således at python har lettere ved at forstå. .csv filer kan være forskellige alt efter hvem der har lavet dem, derfor er det godt værktøj at kunne standardisere dem.

Pandas:
Brugt på samme måde som "csv", mulighederne er dog større for bearbejdelse af data. "Pandas" gør det lettere at beregne specifik data i csv-filen. Det kan være data for specifikke datoer eller lign. "Pandas" laver næsten alle beregninger og er derfor et meget væsentligt værktøj i dette vejrudsigtsmodul.

Matplotlib:
Er et essentielt værktøj. Bruges til at konstruere grafer, som er med til at overskueliggøre beregningsresultater. 

__________________________________________________________________________________________________________________________________________________________________________________________________________________

## Dette SKAL gøres for at kunne bruge "Forecast Module"

Download seneste version af Python [Installér Pyton](https://www.python.org/downloads/)

Download seneste version af Pandas [Installér Pandas](https://pypi.org/project/pandas/)

Download seneste version af Matplotlib [Installér Matplotlib](https://matplotlib.org/stable/)

WindData.csv samt Login.txt må ikke slettes, da de er en nødvendighed for modulets operationalitet.

__________________________________________________________________________________________________________________________________________________________________________________________________________________

## Sådan bruges "Forecast Module"

1. Åben (Forecast_Module.py)
2. Skriv dine login oplysninger. Hvis det er første gang du logger ind skal dine login oplysninger godkendes. Efter godkendelse får du adgang.
3. Vælg det menupunkt du ønsker fra menuen ved at trykke på en tast mellem (1) og (6).
4. Programmet afsluttes ved at vælge menupunktet "Afslut", ved at taste (6) eller hvis du er inde i et menupunkt (2).

__________________________________________________________________________________________________________________________________________________________________________________________________________________

## Troubleshoot

Hvis programmet ikke initialiserer som planlagt, sørg da for at disse ting er/ikke er gjort.

Download seneste version af Python [Installér Pyton](https://www.python.org/downloads/)

Download seneste version af Pandas [Installér Pandas](https://pypi.org/project/pandas/)

Download seneste version af Matplotlib [Installér Matplotlib](https://matplotlib.org/stable/)

WindData.csv samt Login.txt må ikke slettes, da de er en nødvendighed for modulets operationalitet.

__________________________________________________________________________________________________________________________________________________________________________________________________________________

## Credits

Emil Bystrup Lenschau

Jonas Hvid Nielsen

Magnus Christophersen

Maria Buur

Mathias Villa Fonseca

__________________________________________________________________________________________________________________________________________________________________________________________________________________

## Licens 

MIT License

Copyright (c) [2021] [Emil Bystrup Lenschau, Jonas Hvid Nielsen, Magnus Christophersen, Maria Buur, Mathias Villa Fonseca]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
(https://choosealicense.com/licenses/mit/#)