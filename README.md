
## SECTION 1 : PROJECT TITLE
## Deck Sorcery: Hearthstone Deck Building

<img src="Miscellaneous/Deck Sorcery.png"
     style="float: left; margin-right: 0px;" />

---
## SECTION 2 : EXECUTIVE SUMMARY

Computer gaming is a billion dollar industry, characterized by video and mobile games which provide endless hours of entertainment to gamers. Nonlinear gamplays presents players with challenges that can be completed in a number of different sequences and could result in a variety of outcomes. Increasingly, game developers are leveraging on  machine learning methods, such as supervised learning like support vector machines or neural networks to build the models of player experience to enhance gameplay. 

Hearthstone, a online collectible card game (CCG) is a turn-based 1-vs-1 strategy game  set in the Warcraft universe. In CCGs every  player is asked to construct a specific deck of 30 cards before the actual match. With 9 different hero classes and over 2,000 possible cards to choose from, this is no doubt a daunting task. Each card include specific rules that affect the interaction between players, promoting a varied and dynamic game play. Players need to deal with hidden information and randomness, with the combination of states, rules and cards that may result in complex or unpredicted reactions, such as combos, combination of card. Hearthstone is a game where actions may have non-deterministic results, and the challenge for each user to maximize the possibility of winning using their constructed deck.

TSL has developed Deck Sorcery, a web based platform, which focuses on the automated deck construction and deck win rate optimization using information from historical dataset of decks.  The actual gameplay mechanisms are not covered in this project but they can be considered in future enhancement of the intelligent system. Deck Sorcery is based on a Hybrid Reasoning System: Co-operating Experts architecture, considering the complex nature of deck construction and requirements for various techniques. Deck Sorcery leverages on a combination of machine reasoning techniques such as deductive and inductive reasoning, as well as planning & optimization in Synthetic Problem Solving.

The lack of any universal benchmarking methods for win rate prediction made assess the strength of the deck other than by human observation. Also, a multitude of factors such as the player’s intrinsic ability or the number of actions in the game are not considered in our analysis. 

The technologies used in our POC solution are a combination of Flask, Python and external Python libraries such as Scikit Learn, DEAP and Apyori.


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
