from bs4 import BeautifulSoup

import requests

"""
# Input
Please input the connpass event's number:60207

# Output
Attendees
[ ]id1
[ ]id2
... remaining omitted ...

Waiting List
[ ]id3
[ ]id4
... remaining omitted ...
"""

def printList(soup, className, title):
    area = soup.find("div", {"class":className})
    names = list()
    for name in area.find_all("p", {"class":"display_name"}):
        names.append(name.find('a').contents[0])
    names.sort()
    print(title)
    printout(names)

def printout(list):
    for item in list: print('[ ]'+item)

def main(eventId):
    thisurl = "https://webhack.connpass.com/event/"+eventId+"/participation/#participants"
    response = requests.get(thisurl)
    data = response.text
    soup = BeautifulSoup(data, "lxml")

    printList(soup, "participation_table_area", "Attendees")
    print()
    printList(soup, "waitlist_table_area", "Waiting List")

if __name__ == '__main__':
    var = input("Please input the connpass event's number:")
    main(var)