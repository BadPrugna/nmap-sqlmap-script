f= """1/tcp	TCP Multiplexor
2/tcp	compressnet Management Utility
3/tcp	compressnet Compression Process
7/udp	Echo Protocol
8/udp	Bif Protocol
9/udp	Discard Protocol
13/tcp	Daytime Protocol
17/tcp	Quote of the Day
19/udp	Chargen Protocol
20/tcp	FTP - Il file transfer protocol - data
21/tcp	FTP - Il file transfer protocol - control
22/tcp	SSH - Secure login, file transfer (scp, sftp) e port forwarding
23/tcp	Telnet insecure text communications
25/tcp	SMTP - Simple Mail Transfer Protocol (E-mail)
53/udp	DNS - Domain Name System
67/udp	BOOTP Bootstrap Protocol (Server) e DHCP Dynamic Host Configuration Protocol (Server)
68/udp	BOOTP Bootstrap Protocol (Client) e DHCP Dynamic Host Configuration Protocol (Client)
69/udp	TFTP Trivial File Transfer Protocol
70/tcp	Gopher
79/tcp	finger Finger
80/tcp	HTTP HyperText Transfer Protocol (WWW)
88/tcp	Kerberos Authenticating agent
104/tcp	DICOM - Digital Imaging and Communications in Medicine
110/tcp	POP3 Post Office Protocol (E-mail)
113/tcp	ident vecchio sistema di identificazione dei server
119/tcp	NNTP usato dai newsgroups usenet
123/udp	NTP usato per la sincronizzazione degli orologi client-server
137/udp	NetBIOS Name Service
138/udp	NetBIOS Datagram Service
139/tcp	NetBIOS Session Service
143/tcp	IMAP4 Internet Message Access Protocol (E-mail)
161/udp	SNMP Simple Network Management Protocol (Agent)
162/udp	SNMP Simple Network Management Protocol (Manager)
389/tcp	LDAP
411/tcp	Direct Connect Usato per gli hub della suddetta rete
443/tcp	HTTPS usato per il trasferimento sicuro di pagine web
445/tcp	Microsoft-DS (Active Directory, share di Windows, Sasser-worm)
445/udp	Microsoft-DS SMB file sharing
465/tcp	SMTP - Simple Mail Transfer Protocol (E-mail) su SSL
502/tcp	Modbus
514/udp	SysLog usato per il system logging
554/udp	RTSP per lo streaming live
563/tcp	NNTP Network News Transfer Protocol (newsgroup Usenet) su SSL
587/tcp	e-mail message submission (SMTP)
591/tcp	FileMaker 6.0 Web Sharing (HTTP Alternate, si veda la porta 80)
631/udp	IPP / CUPS Common Unix printing system (Il server di stampa sui sistemi operativi UNIX/Linux)
636/tcp	LDAP su SSL
666/tcp	Doom giocato in rete via TCP
993/tcp	IMAP4 Internet Message Access Protocol (E-mail) su SSL
995/tcp	POP3 Post Office Protocol (E-mail) su SSL
Da 1024 a 49151
Porta	Descrizione
1080/tcp	SOCKS Proxy
1194/udp	OpenVPN
1883/tcp	MQTT
1433/tcp	Microsoft-SQL-Server
1434/tcp	Microsoft-SQL-Monitor
1434/udp	Microsoft-SQL-Monitor
1984/tcp	Big Brother
2049/udp	Network File System
2101/tcp	rtcm-sc104 usato per le correzioni differenziali dei gps
2101/udp	rtcm-sc104 usato per le correzioni differenziali dei gps
2761/both	DICOM ISCL (Integrated Secure Communication Layer)
2762/both	DICOM TLS
3050/tcp	Firebird Database system
3128/tcp	HTTP usato dalle web cache e porta di default per Squid cache
3306/tcp	MySQL Database system
3389/tcp	Desktop Remoto di Windows e Microsoft Terminal Server (RDP)
3541/tcp	Voispeed
3542/tcp	Voispeed
3690/tcp	Subversion
3690/udp	Subversion
4662/tcp	eMule (versioni precedenti alla 0.47, le più recenti la generano casualmente)
4672/udp	eMule (versioni precedenti alla 0.47, le più recenti la generano casualmente)
4711/tcp	eMule Web Server
4899/tcp	Radmin Connessione Remota
5000/tcp	Sybase database server (default)
5060/tcp	SIP
5060/udp	SIP
5084/tcp	EPCglobal Low-Level Reader Protocol (LLRP)
5084/udp	EPCglobal Low-Level Reader Protocol (LLRP)
5085/tcp	EPCglobal Low-Level Reader Protocol (LLRP) criptato
5085/udp	EPCglobal Low-Level Reader Protocol (LLRP) criptato
5190/tcp	AOL e AOL Instant Messenger
5222/tcp	XMPP Client Connection
5269/tcp	XMPP Server Connection
5432/tcp	PostgreSQL Database system
5631/tcp	Symantec PcAnywhere
5632/udp	Symantec PcAnywhere
5800/tcp	Ultra VNC (http)
5900/tcp	Ultra VNC (main)
6000/tcp	X11 usato per X-windows
6566/tcp	SANE
6667/tcp	IRC, Internet Relay Chat
8000/tcp	iRDMI. Spesso usato per sbaglio al posto della porta 8080. Anche utilizzata per la gestione di pyLoad.
8080/tcp	HTTP Alternate (http-alt) o WWW caching service (web cache). Usato spesso quando un secondo server web opera sulla stessa macchina, come server proxy e di caching, o per far girare un server web come utente non di root. Si veda anche la porta 80. Tomcat usa di default questa porta.
8118/tcp	privoxy http filtering proxy service
8883/tcp	MQTT con SSL
41951/tcp	TVersity Media Server
41951/udp	TVersity Media Server
Da 49152 a 65535
Sezione vuota
Questa sezione è ancora vuota. Aiutaci a scriverla!
Porte non registrate
Queste sono porte che possono essere di uso comune, ma non sono formalmente registrate con la IANA. Dove l'uso è in conflitto con un uso registrato, viene usata la notazione CONFLITTO.

Porta	Descrizione
80/tcp	Skype, attiva di default, disattivabile
1337/tcp	WASTE Encrypted File Sharing Program
1352/tcp	IBM Lotus Lotus Domino/Notes
1521/tcp	Oracle database default listener (CONFLITTO con l'uso registrato: nCube License Manager)
2082/tcp	CPanel, porta di default port (CONFLITTO con l'uso registrato: Infowave Mobility Server)
2086/tcp	Web Host Manager, porta di default (CONFLITTO con l'uso registrato: GNUnet)
4662/tcp	eMule AdunanzA, porta di default per il protocollo eDonkey usato da eMule AdunanzA
4672/udp	eMule AdunanzA, porta di default per il protocollo eDonkey usato da eMule AdunanzA
5000/tcp	Universal plug-and-play Windows network device interoperability (CONFLITTO con l'uso registrato: complex-main)
5223/tcp	XMPP porta di default per SSL Client Connection
5800/tcp	VNC remote desktop protocol (per l'uso via HTTP)
5900/tcp	VNC remote desktop protocol (porta standard)
6881/tcp	BitTorrent porta spesso usata
6969/tcp	BitTorrent tracker port (CONFLITTO con l'uso registrato: acmsoda)
9050/tcp	TOR, porta di default per il socks5
9987/udp	TeamSpeak, software VoIP proprietario, porta di default "virtual voice server"
9091/tcp	Transmission, porta di default per la gestione da browser
10000/tcp	Webmin interfaccia web di amministrazione
25565/tcp	Minecraft videogioco di tipo sand-box
27960/udp	(fino a 27969) Quake 3 e videogiochi derivati da Quake 3
31337/tcp	Back Orifice Remote administration tool (spesso usata dai Trojan)
10101/tcp	Metin2 videogioco di tipo MMO"""
b=f.split('\n')
d={}
k=[]
g=[]
for e in b:
    coppia=e.split('/')
    k.append(coppia)
for i in k:
    if len(i)==2:
        d[i[0]]=i[1]
a=list(d.keys())
for s in a:
    s=int(s)
    g.append(s)
print(g)
    


