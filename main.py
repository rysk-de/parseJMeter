import glob
import xml.etree.ElementTree as ET

filenames = glob.glob('response\\*.soap+xml') #get all files in response directory
count_found = 0
count_lost = 0

for filename in filenames:
    with open(filename, 'r', encoding="utf-8") as content:
        tree = ET.parse(content) #parse opened file with ElementTree
        x = tree.findall('.//') #find everything
        if "sendMessageResponse" in x[1].text: #if array-position 1 in x contains "sendMessageResponse" we pass on the file
            pass
        else: #if array-position 1 in x does not contain "sendMessageResponse" we continue
            with open('JMeter_IDs.csv', 'a') as f:
                f.write(x[6].text + '\n') #array-position 6 in x gets written to JMeter_IDs.csv
            count_found = count_found + 1

print(f"Es wurden {count_found} MessageIDs gefunden und in JMeter_IDs.csv geschrieben.")

with open('Conversations.csv', 'r') as t1, open('JMeter_IDs.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('Lost.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
            count_lost = count_ids_lost + 1

print(f"{count_lost} von {count_found} MessageIDs wurden im PSB-Export nicht gefunden und in Lost.csv geschrieben.")