import glob
import xml.etree.ElementTree as ET

filenames = glob.glob('..\\parseJMeter\\response\\*.soap+xml') #get all files in response directory
count = 0

for filename in filenames:
    with open(filename, 'r', encoding="utf-8") as content:
        tree = ET.parse(content) #parse opened file with ElementTree
        x = tree.findall('.//') #find everything
        if "sendMessageResponse" in x[1].text: #if array-position 1 in x contains "sendMessageResponse" we pass on the file
            pass
        else: #if array-position 1 in x does not contain "sendMessageResponse" we continue
            with open('..\\parseJMeter\\jmeter_ids.csv', 'a') as f:
                f.write(x[6].text + '\n') #array-position 6 in x gets written to jmeter_ids.csv
            count = count + 1

print(f"Es wurden {count} MessageIDs gefunden")