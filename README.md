## SECTION 1 : PROJECT TITLE
## Intelligent Specialty Coffee Recommender

<img src="coffeeSite.png"
     style="float: left; margin-right: 0px;" />

---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
Singapore ranks amongst countries with the highest population density in the world. In a bid to have firm control over long term urban planning, the Singapore government came up with the “Built to Order” (abbreviated BTO) initiative back in 2001. These are new Housing Development Board (HDB) flats tightly controlled by their eligibility and quantity released every year. In more recent years, the modern BTO scheme in Singapore requires a waiting period of 3-4 years, and is generally targeted at young Singaporean couples looking to purchase their first property and set up a family. Nationality and income ceilings are some of the broad filters that determine one’s eligibility for the highly sought after projects. 


Our team, comprising of 6 young Singaporeans, all hope to be property owners one day. Many of our peers opt for BTO flats due to their affordability, existence of financial aid from the government, as well as their resale value. However, there often exists a knowledge gap for these young couples during the decision making process and they end up making potentially regretful decisions. We would like to bridge this knowledge gap, and have hence chosen to base our project on creating a recommender system for BTO flats, utilizing the data from recent launches in Tampines, Eunos, Sengkang and Punggol. 


Using the techniques imparted to us in lectures, our group first set out to build a sizeable knowledge base via conducting an interview and administering a survey. While building the system, we utilized tools such as Java to scrape real time data from HDB website and transform it into a database, CLIPS to synthesize the rule based reasoning process, and Python to integrate it into an easy to use UI for the everyday user. To add icing on the cake, we even hosted the system on a website so that the everyday user can access it through the click of a link.


Our team had an amazing time working on this project, and hope to share our insights with everyone. Despite a focus on BTO flats, we would recommend it for everybody interested in understanding property market trends for residence or investment purposes. There truly are a wide array of factors behind the decision to invest in a property, and we only wish there was more time to work on the scope and scale of the project. 

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Jingyi Zhang | A0269366M | Ideation, Data Collection, Data Preprocessing, Data feature extraction, Recommendation algorithm design  | e1112237@u.nus.edu |
| Lin Ji | A0269369H | Ideation, Data Collection, Data Preprocessing, Data feature extraction, Recommendation algorithm design, Video Editing | e1112240@u.nus.edu |
| HuiWen Tang | A0269361X | UI/UX Design, Data Preprocessing, Recommendation algorithm design | e1112232@u.nus.edu |
| Li Gengwei | A0269362W | Ideation, Data Collection, Data Preprocessing, Data feature extraction, Recommendation algorithm design | e1112233@u.nus.edu |
| Fong Zhi En Kelvin | A0269365N | Data Preprocessing, Frontend Dev, Backend Dev, Code Integration | e1112236@u.nus.edu |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![Coffee Recommender](http://img.youtube.com/vi/-AiYLUjP6o8/0.jpg)](https://youtu.be/-AiYLUjP6o8 "Intelligent Specialty Coffee Recommender")

---

## SECTION 5 : USER GUIDE

### [ 1 ] To run the Backend
### Using any Ubuntu based environment, or Ubuntu on WSL on Windows 

> $ pip install jupyter_kernel_gateway

> Navigate to "BackEnd" folder

> $ jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' --KernelGatewayApp.seed_uri='Backend.ipynb' --KernelGatewayApp.port=8899

### [ 2 ] To run the Frontend

> pip install flask

> Navigate to "\FrontEnd\KnowYourCoffee" Folder

> $ python main.py

> **Go to URL using web browser** http://0.0.0.0:5000 or http://127.0.0.1:5000

---
## SECTION 6 : PROJECT REPORT / PAPER


**Recommended Sections for Project Report / Paper:**
- Executive Summary / Paper Abstract
- Business Problem Background
- Market Research
- Project Objectives & Success Measurements
- Project Solution (To detail domain modelling & system design.)
- Project Implementation (To detail system development & testing approach.)
- Project Performance & Validation (To prove project objectives are met.)
- Project Conclusions: Findings & Recommendation
- Appendix of report: Project Proposal
- Appendix of report: Mapped System Functionalities against knowledge, techniques and skills of modular courses: MR, RS, CGS
- Appendix of report: Installation and User Guide
- Appendix of report: 1-2 pages individual project report per project member, including: Individual reflection of project journey: (1) personal contribution to group project (2) what learnt is most useful for you (3) how you can apply the knowledge and skills in other situations or your workplaces
- Appendix of report: List of Abbreviations (if applicable)
- Appendix of report: References (if applicable)

---
## SECTION 7 : MISCELLANEOUS

---

