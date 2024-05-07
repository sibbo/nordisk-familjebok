# TODO

KLAR Lägg till en datapunkt som säger hur det uppslaget klassificerades, om det var med bold, index eller NN
Ta bort alla tags inom <> förutom <b> och </b>, <i> och </i>. Ofta är det <a ref ...> och så någonting där inuti. Helt ärligt, kan göra en regex som tar alla sånna tags och tar bort, de tjänar inget till.
Ännu smartare första bokstav-grej, om det senaste uppslaget (eller en sekvens av uppslag) började på "Hi" så måste nästa vara "Hi" eller "Hj" osv, det kan aldrig gå "bakåt" åtminstone. Är det värt det? //Gör en post processing på detta, det är enklast
Lägg in krav i requirements.txt fil 

scraper
post processing på råtext: ta bort tags <hej>, [rättelse ...] i första upplagan
ändra ordning på celler, skapa träningsdata, träna modell osv innan man kör segmenting
post processing på json-filer: cross references, ta bort artiklar som inte står i rätt ordning, "st sa st" är fel ordning t.ex.
ta bort logistic regression, ha kvar mlp
göra det lite snyggare allmänt
gömma config-grejer så varje notebook gör en grej: en scraper med post processing, en för att träna modell, en segmenter med post processing

segmenter
fixa när träningsdata skapas så att den inte tar hela first_letter_list utan bara den bokstaven som just nu är rätt

linker
gör nåt smartare/bättre än threshold, någon ml, Re-ranking, ta fem första från cosine similarity och sen kör fine-tunad binär klassifierare (BERT med sveparafras t.ex.) om de är bra eller inte

classifier för location?


Sätter en väldigt hög threshold till att börja med, tills vi förbättrat linker

kunna söka i wikidata, jämför embeddings med kb-sbert? och kunna få ut motsvarande svenska wikipedia-artikel
köra igenom alla entries i wikidata
fine-tuned kb-bert för att avgöra om wikidata-beskrivning är samma som den från nf

visualisera koordinater från wikidata

refaktorisering
Funktioner som att öppna json fil med artiklar och skriva artiklar till json fil definieras i flera olika notebooks. Dessa kan definieras i en .py fil.