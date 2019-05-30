
## SECTION 1 : PROJECT TITLE
## Deck Sorcery: Hearthstone Deck Building

<img src="Miscellaneous/Deck Sorcery.png"
     style="float: left; margin-right: 0px;" />

---
## SECTION 2 : EXECUTIVE SUMMARY

ISSAC is the implementation of an Automated Chatbot to provide information about the Institute of System Science (ISS) of the National University of Singapore. The key challenge was to identify key information contained with the website and extracting the relevant information from the website. Information Extraction (IE) techniques were applied to the website to summarize natural language text into a structured set of facts. We developed a framework for plugging in and executing IE methods over 150 pages in the ISS website. We also integrated a generic web crawler in the system.

---
## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID  | Work Items | 
| :------------ |:---------------:| :-----| 
| Tan Jun Khiang | A0195169N | Project Report, Knowledge Discovery, Video| 
| Tan Wei Lian | A0048135J | Python Application - Genetic Algorithmn & Knowledge Discovery|
| Tang Meng | A0137099U | Flask Web Application |
| Leong Jun Hun, Darryl | A0195318X | Project Report, Knowledge Discovery| 

---
## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

<a href="https://youtu.be/Vxq8k3xzHlw"><img src="Miscellaneous/YTDeck Sorcery.png"
     style="float: left; margin-right: 0px;" /></a>

---
## SECTION 5 : USER GUIDE

`<Github File Link>` : <https://github.com/musicrokr/IRS-RS-2019-03-09-IS01PT-GRP-TheSundayLunatics-DeckSorcery/blob/master/UserGuide/Deck%20Sorcery%20User%20Guide.pdf>

### [ 1 ] To run the system using iss-vm

> download pre-built virtual machine from http://bit.ly/iss-vm

> start iss-vm

> open terminal in iss-vm

> $ git clone https://github.com/musicrokr/IRS-RS-2019-03-09-IS01PT-GRP-TheSundayLunatics-DeckSorcery.git

> $ cd folder_location/SystemCode/deck-sorcery-master

> $ py -m venv env

> $ env\Scripts\activate

> $ pip install flask

> $ set FLASK_APP=main.py

> $ pip install sklearn

> $ pip install deap

> $ flask run

> **Go to URL listed in Command Prompt using web browser** http://127.0.0.1:5000

### [ 2 ] To run the system in other/local machine:
### Install additional necessary libraries. This application works in Python 3 only.

> $ git clone https://github.com/musicrokr/IRS-RS-2019-03-09-IS01PT-GRP-TheSundayLunatics-DeckSorcery.git

> $ cd folder_location/SystemCode/deck-sorcery-master

> $ py -m venv env

> $ env\Scripts\activate

> $ pip install flask

> $ set FLASK_APP=main.py

> $ pip install sklearn

> $ pip install deap

> $ flask run

> **Go to URL listed in Command Prompt using web browser** http://127.0.0.1:5000


---
## SECTION 6 : PROJECT REPORT / PAPER

`<Github File Link>` : <https://github.com/musicrokr/IRS-RS-2019-03-09-IS01PT-GRP-TheSundayLunatics-DeckSorcery/blob/master/ProjectReport/Deck%20Sorcery%20Project%20Report.pdf>

---
## SECTION 7 : MISCELLANEOUS

N.A.


---

---

**This [Machine Reasoning (MR)](https://www.iss.nus.edu.sg/executive-education/course/detail/machine-reasoning "Machine Reasoning") course is part of the Analytics and Intelligent Systems and Graduate Certificate in [Intelligent Reasoning Systems (IRS)](https://www.iss.nus.edu.sg/stackable-certificate-programmes/intelligent-systems "Intelligent Reasoning Systems") series offered by [NUS-ISS](https://www.iss.nus.edu.sg "Institute of Systems Science, National University of Singapore").**

**Lecturer: [GU Zhan (Sam)](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan "GU Zhan (Sam)")**

[![alt text](https://www.iss.nus.edu.sg/images/default-source/About-Us/7.6.1-teaching-staff/sam-website.tmb-.png "Let's check Sam' profile page")](https://www.iss.nus.edu.sg/about-us/staff/detail/201/GU%20Zhan)

**zhan.gu@nus.edu.sg**
