# TODO

Lägg in krav i requirements.txt fil 

scraper
(KANSKE KLAR) post processing på json-filer: cross references, ta bort artiklar som inte står i rätt ordning, "st sa st" är fel ordning t.ex.
Bold tags, ska vi kolla om det är på rätt bokstav eller inte

segmenter

cross references
Nåt error just nu?
Om det är från index eller classifier match, ta bort dessa i headword ( ' siffror ; [ :] )
Antaganden: 
Om texten till uppslaget är kortare än 60 tecken och innehåller " Se " så är det en cross reference. Det kan finnas fler som tekniskt sett är eller har med en reference men de är inte lika viktiga för oss
uppslaget som en cross reference (som definerat ovan) refererar till finns alltid, och handlar alltid om samma sak

embeddings
gör bara embeddings på ord som inte är cross references


linker
gör nåt smartare/bättre än threshold, någon ml, Re-ranking, ta fem första från cosine similarity och sen kör fine-tunad binär klassifierare (BERT med sveparafras t.ex.) om de är bra eller inte

classifier för location?


Sätter en väldigt hög threshold till att börja med, tills vi förbättrat linker

fine-tuned kb-bert för att avgöra om wikidata-beskrivning är samma som den från nf
Om vi får flera uppslag som matchar till samma qid, ska vi göra något då? eller bara låta det vara kvar av dem är kvar? 

visualisera koordinater från wikidata
Bra visualiseringar, t.ex: visualisera skillnader mellan e1 och e2, olika färger för e1 och e2, vilka platser finns i ena men inte andra.

refaktorisering
KLAR Funktioner som att öppna json fil med artiklar och skriva artiklar till json fil definieras i flera olika notebooks. Dessa kan definieras i en .py fil.

rapport
https://www.ri.se/sites/default/files/2020-09/SLTC_2020.pdf


möte 2024-05-13
Testa segmenting med 10 (helst fler) exempel, ha med i rapporten, ta 10 slumpmässiga
exempel sida 100, ta 10 st. Kolla på en kolumn, ta raden mitt på kolumnen och ta ut den motsvarande artikeln

post processing efter segmenting: 

skriv i rapport: vi tog bort entries som var ifrågasättbara, man kanske kan göra det på ett bättre sätt

utvärdering av match: 1 till 2 och 2 till 1, kolla på accuracy. 1 till 2, hur många är korrekta
De som är matchade, kolla vad de har för matchning, kolla matchning och få ut accuracy.
Höj threshold

utvärdering för qid match? extremt långt

Ha en utvärdering för alla delar