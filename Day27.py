# <Web Scraping with BeautifulSoup>
import requests
from bs4 import BeautifulSoup


#QUESTION NO 1 - Scrape all headlines (h1, h2, h3) from a news website like https://www.thehindu.com.


#Send a Get request to website
url = "https://www.thehindu.com"
headers = {"User-Agent": "Mozilla/5.0"}   # Recommended: to avoid being blocked
response = requests.get(url, headers=headers)


#Parse html content using beautigulsoup
soup = BeautifulSoup(response.text,"html.parser")

#Extract headlines
headlines = soup.find_all(['h1','h2','h3'])

#Print headlines
print("Headlines -\n")
for index,headline in enumerate(headlines):
    print(f"{index+1}.{headline.text.strip()}")


'''
Output :

Headlines -
1.Why does the Axiom-4 mission need 28 hours to reach the ISS?
2.Turbulent skies, turbulent minds: the rising fear of flying and how to combat it      
3.When cities have trees that don’t belong, the birds notice
4.Interview | Sports has to be a lifestyle, not just a result-oriented model: Sajan Prakash
5.50 years of Emergency: Locked up with seven inmates, Stalin was beaten, harassed, fed ‘kali’
6.Manager among three arrested for theft of 58 kg of gold from Canara Bank in Karnataka’s Vijayapura
7.India refuses to sign joint statement in SCO summit
8.Iran-Israel LIVE: Iran approves bill suspending cooperation with IAEA
9.Axiom-4 mission: Dragon spacecraft docks at International Space Station
10.Zohran Mamdani’s New York mayoral win draws flak from Kangana, Congress’s Singhvi
11.‘Not tenable’: ECI sources on Congress seeking digital copy of Maharashtra voters’ list
12.Ahmedabad Air India plane crash: Data extraction from black boxes, analysis of cockpit voice recorder in progress
13.Latest News
14.Qualified cheer: On Shubhanshu Shukla,  Axiom-4 mission
15.Cause and effect: On human rights, citizenship cases
16.Top Videos
17.Top Picks
18.The Hindu Opinion
19.A lofty concept, a Governor and unwanted controversy
20.Enabling voting rights for migrants
21.Trouble from within
22.Byrnihat: world’s most polluted air | Green humour by Rohan Chakravarty
23.The ‘Axis of Upheaval’ in the West Asia conflict
24.When counsel is questioned
25.The Hindu Explains
26.Why does the Axiom-4 mission need 28 hours to reach the ISS?
27.Can India push Pakistan into FATF’s ‘Grey list’?
28.Why oil prices have declined and what are the potential implications? | Explained    
29.Why the Anna University sexual assault case must be a wake-up call on women safety | Explained
30.What is behind the U.S.-Israel ‘special relationship’: Explained
31.Top News Today
32.Featured
33.Why I lift: How more Indian women are taking up strength training
34.States Updates
35.Cities Updates

'''