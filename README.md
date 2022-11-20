# The free-time API

Heeft u vrije tijd maar weet u niet hoe deze nuttig te spenderen?  
Voelt u zich verveeld en wilt u iets actiefs doen?

De free-time API biedt u suggesties aan over welke activiteiten mogelijk zijn indien u vrije tijd heeft maar geen enkel idee heeft wat met die vrije tijd te doen.

U heeft de mogelijkheid om te filteren op zowel welk type activiteit alsook met hoeveel personen u een activiteit wilt doen. De mogelijkheid is er ook dat als u twijfels heeft over een bepaalde activiteit de API ook voor u kan kiezen of u aan de bepaalde activiteit deelneemt of niet deelneemt. U kunt deze functie ook gebruiken bij andere omstandigheden waar een beslissing genomen moet worden. Tot slot voorziet de API een klein maar tof gebaar wanneer u een pauze nodig heeft.

Op de website is elke functie van de API beschikbaar welke duidelijk verdeeld zijn op activiteit, de keuze maker en pauze.

## Linken

Mijn hosted API link: https://free-time-mrtv0.cloud.okteto.net/  
Mijn GitHub repository voor de front-end: https://github.com/MrTV0/website  
Mijn hosted front-end link: https://mrtv0.github.io/website/

De externe activiteit API: http://www.boredapi.com/api/activity/  
De externe yesno API: https://yesno.wtf/api

## Postman
### Beide willekeurig
Als zowel het type activiteit als het aantal deelnemers aan de activiteit niet meegegeven wordt is alles willekeurig.

![activity_null_null](https://user-images.githubusercontent.com/57659923/202915866-9cae796a-f2b4-4849-a06b-d32db56de9bd.png)

### Aantal deelnemers willekeurig
Als het type activiteit word meegegeven worden er enkel activiteiten gestuurd van dat specifieke type.

![activity_sel_null](https://user-images.githubusercontent.com/57659923/202915870-b9cccc6a-e9ea-4b26-b196-4d789db8e805.png)

### Type activiteit willekeurig
Als het aantal deelnemers word meegegeven worden er enkel activiteiten gestuurd met het specifieke aantal deelnemers.

![activity_null_amount](https://user-images.githubusercontent.com/57659923/202915873-51f9747f-892a-4955-ade4-c6b4a050ce72.png)

### Beide gespecificeerd
Als beide worden meegegeven worden er enkel activiteiten gestuurd van dat specifieke type en specifieke aantal deelnemers.

![activity_sel_amount](https://user-images.githubusercontent.com/57659923/202915878-0194305d-2053-430f-bade-e8ed85f939d1.png)

### Keuze ontvangen
Het ontvangen van een "yes" of een "no".

![choice](https://user-images.githubusercontent.com/57659923/202915882-313317cd-3262-4a36-88a5-aff035da4215.png)

### Correct gebruik van keuze maker
Als zowel het aantal keer dat de yesno API opgevraagd moet worden alsook het maximum aantal dat de yesno API opgevraagd mag worden, word er het resultaat alsook de beslissing zelf getoond.

![yesnos_max](https://user-images.githubusercontent.com/57659923/202915886-4806c43e-098c-4f95-b6a3-dec5edcbc685.png)

### Over limiet
Als het aantal keer dat de yesno API opgevraagd moet worden hoger is dan het maximum aantal dat de yesno API opgevraagd mag worden, word er een error message verstuurd.

![yesnos_over_max](https://user-images.githubusercontent.com/57659923/202915895-a982d5bf-ecc6-4300-b920-2c3f848fada4.png)

### Over toegestane maximale waarde
Als het maximum aantal dat de yesno API opgevraagd mag worden overschreden word, word er een error message verstuurd.

![yesnos_over_limit](https://user-images.githubusercontent.com/57659923/202915898-5691e27a-cc43-4686-8fdd-eb12d9f9a932.png)

### Koffie ontvangen
Het ontvangen van een geschikte text met bijpassende afbeelding.

![break](https://user-images.githubusercontent.com/57659923/202915900-58b6b3cb-3d1c-4e6e-8766-027c91faaf7b.png)

## OpenAPI

![screencapture-free-time-mrtv0-cloud-okteto-net-docs-2022-11-20-17_30_20](https://user-images.githubusercontent.com/57659923/202914805-84bae13b-4f07-44c4-bc85-039da6032f83.png)
