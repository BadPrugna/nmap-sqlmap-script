# nmap-sqlmap-script
A script that combine sqlmap+nmap to scan a domaine and generate few useful file in your directory

Purtroppo non sono arrivata alle tabelle, ma se da terminale 
lanciate:
sudo ./provabash 
Dopo circa tre minuti avrete nella stessa cartella:
-file di report completo di nmap (test.txt)
  L'opzione "verbose" vi restituirà i certificati ssl, le informazioni sul S.O, il MAC address,un elenco dettagliato delle risposte con     gli errori HTTP (essendo un file txt vi basterà cercarle con Ctrl+F)
  Usa l'opzione Aggressive e la frammentazione dei pacchetti con una finestra valida sia per connessioni ethernet che wi-fi)
-file con l'elenco di tutte le porte aperte, relativo ttl e nome del servizio (porte.txt):
-file di report completo di sqlmap (porte.txt) -> Al momento purtroppo è solo una copia del file porte.txt, ma conto di aggiungerci anche   un riassunto di tutte le informazioni utili
-stampa a video del tipo di db usato e del nome dei db trovati

NB:Le funzioni usate nei file python non si chiamavo a vicenda quindi potrete usarli anche cambiando le opzioni dei tools

NB:Aprendo il file bash (sudo nano provabash.sh), potrete modificare a piacimento le opzioni di nmap ed sqlmap per aggiungere il dominio su cui dovete fare l'analisi, e renderlo il più possibile adattabile al vostro caso
(Cercate di non togliere la parte > file.txt perchè permette di avere dei file da far analizzare agli script python)
