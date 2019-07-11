testo = open("test.txt", "r")
porte = open("porte.txt", "w+")
report = open("report.txt", "w+")

for riga in testo:
    if 'secure' in riga:
        report.write(f"Come ci indica questa riga dell'output di nmap, la flag di sicurezza è disattivata: \n {riga}")
        report.write('\n')    

    if 'MAC Address' in riga:
        report.write(riga)
        report.write('\n')
        MAC=riga[13:29]
        
    if 'open' in riga:
        k=str(riga)
        porte.write(riga)
        porte.write('\n')
        report.write(riga)
        report.write('\n')
        
print(riga)
testo.close()
porte.close()
report.close()
