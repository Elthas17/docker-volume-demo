### Docker-compose
een lokale folder/volume op de host 'image-classification' heet in de docker container de folder 'data' in de root directory van de service. 
Deze datafolder is een gedeelde folder/volume tussen de services/containers.
````
volumes:
  - image-classification:/data
````

FYI Vergeet niet dat je image per service uniek moet zijn
```
image: atlascopco.azurecr.io/image-classification-write:latest
```

### Dockerfile
in de Dockerfile willen we niet dat de python code vd verschillende services mekaar overschrijven, deze mogen dus niet in het gedeelde volume. 

We stoppen de logica in een lokale sub folder 'app' zodat we eenvoudig enkel de inhoud van die folder in een app folder in de container kopieren.
De app folder is een broer van de data folder in docker-compose, en is dus niet gedeeld tussen de services/containers -> overschrijven mekaars services niet.
````
COPY ./app /app
````

### Code
in de main.py moeten we dan de datafolder gaan zoeken in de grandparent folder gezien het de broer is van de parent folder 'app'.
````
datapath = os.path.join(Path(__file__).parents[1], DATAFOLDER)
````

### Run
je kan de code via de main functie runnen voor dev, en dan heeft elke service zijn eigen niet gedeelde data folder.

in productie is de data dan een shared volume via docker-compoose. 

```angular2html
docker-compose up write
```
```
Creating network "ddemo_default" with the default driver
Creating volume "ddemo_image-classification" with default driver
Creating write ... done
Attaching to write
write    | DATAFOLDER contains []
write    | written hello
write    | DATAFOLDER contains ['hello.txt']
write exited with code 0
```

````angular2html
docker-compose up read
```
```
Creating read ... done
Attaching to read
read     | DATAFOLDER contains ['hello.txt']
read     | Content of the file is:
read     | ['Hello World']
````

Vergeet niet volume is persistent, dus eens gecreerd blijft alles erin bestaan. wil je de boel resetten moet je de volumes prunen.

```angular2html
docker volume prune [volumename]
```

### Bonus
voor de settings heb ik .env files gebruikt voor locale dev, en in docker compose environment variables voor productie.