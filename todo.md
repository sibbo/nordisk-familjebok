# TODO

Lägg in krav i requirements.txt fil 

scraper
(KANSKE KLAR) post processing på json-filer: cross references, ta bort artiklar som inte står i rätt ordning, "st sa st" är fel ordning t.ex.
Ändra hur vi tar fram headword, generellt ta första ordet. Om vi mest bryr oss om platser så kan vi alltid ta första ordet och skita i resten. Om vi bryr oss om personer också får vi nog göra det här i en separat klassificerare, i samband med om vi tror att uppslaget är en person, plats etc och fixa headword utifrån det.
Tar bara första ordet för tillfället. Ibland kan det vara bättre med fler ord för sökningen med headword i wikidata, t.ex. Aalborg (stad), Aalborg (Niels Mikkelsen, präst), Aalborg (amt), Aalborg (stift)
Ta bort till första punctuation (, och .)
om det lades till av klassificeraren, den kan göra lite konstigt ibland. //tror det är indexen som knasar sig snarare
Prudentlig-Prud'hon etc kan matchas av index, inte bra. Kanske ett villkor: if (len(line) > {typ 50?} or " Se " in line)', för vi vet att det inte finns några artiklar som är så korta som inte är korsreferenser.
Flytta så att funktionen som tar bort æ till ae och andra knasiga tecken ligger redan i scraper, ta också bort [' ^ siffror ; \[ : ]


segmenter
KLAR fixa när träningsdata skapas så att den inte tar hela first_letter_list utan bara den bokstaven som just nu är rätt

cross references
Antaganden: 
Om texten till uppslaget är kortare än 60 tecken och innehåller " Se " så är det en cross reference. Det kan finnas fler som tekniskt sett är eller har med en reference men de är inte lika viktiga för oss
uppslaget som en cross reference (som definerat ovan) refererar till finns alltid, och handlar alltid om samma sak


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