import logging
import google.generativeai as genai


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    
)

GEMINI_API_KEY = "AIzaSyDA7YAIjasJ7y3rOub7ISeMlc4wCN2UC2w"

genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")


def ask_gemini(content, question):
    logging.info(f"Querying Gemini with question: {question}")
    prompt = f"Context: {content}\nQuestion: {question}"
    try:
        # Use the correct method for generating text with Gemini
        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
        print(response.text.strip())
        # return response.text.strip()
    except Exception as e:
        logging.error(f"Error querying Gemini: {e}")
        return "Error occurred while querying Gemini."
    

if __name__ == "__main__":



 
    json_content="""
        [
  {
    "page": 5,
    "table_index": 0,
    "data": [
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": "Sl.\nNo.",
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": "",
        "null": ""
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": "",
        "null": ""
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": "1.",
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": "2.",
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": "3.",
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": "4.",
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      },
      {
        "ANNEXURE-C\nPOST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A": null,
        "null": null
      }
    ]
  },
  {
    "page": 5,
    "table_index": 1,
    "data": [
      {
        "Sl.": "No."
      }
    ]
  },
  {
    "page": 5,
    "table_index": 2,
    "data": [
      {
        "Functional": "Requirements"
      }
    ]
  },
  {
    "page": 5,
    "table_index": 3,
    "data": [
      {
        "Assistant": "Accounts General"
      },
      {
        "Assistant": "(Audit) / Assistant"
      },
      {
        "Assistant": "Accountant"
      },
      {
        "Assistant": "General (Audit)"
      }
    ]
  },
  {
    "page": 5,
    "table_index": 4,
    "data": [
      {
        "S, BN, RW, SE, C,": "MF"
      }
    ]
  },
  {
    "page": 5,
    "table_index": 5,
    "data": [
      {
        "S, BN, RW, SE, C,": "MF"
      }
    ]
  },
  {
    "page": 5,
    "table_index": 6,
    "data": [
      {
        "Joint Director": "(Audit)"
      }
    ]
  },
  {
    "page": 5,
    "table_index": 7,
    "data": [
      {
        "S, BN, RW, SE, C,": "MF"
      }
    ]
  },
  {
    "page": 5,
    "table_index": 8,
    "data": [
      {
        "Deputy Director": "(Audit)"
      }
    ]
  },
  {
    "page": 5,
    "table_index": 9,
    "data": [
      {
        "S, BN, RW, SE, C,": "MF"
      }
    ]
  },
  {
    "page": 6,
    "table_index": 0,
    "data": [
      {
        "": null,
        "null": null,
        "Dw, AAV": "c) MD involving",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "(a) to (b) above",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "a) D, HH",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "b) OA, BA, OL,",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "BL, OAL, LC,",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "DW, AAV",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "c) MD involving",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "(a) to (b) above",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "a) D, HH",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "b) OA, BA, OL,",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "BL, OAL, LC,",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "Dw, AAV",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "c) MD involving",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "(a) to (b) above",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "d)",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": "",
        "null": "",
        "Dw, AAV": "a) B, LV",
        "final accounts such as profit and\nloss.": ""
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "b) D, HH",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "c) OA, BA, OL,",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "BL, OAL,",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "BLOA, BLA,",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "LC, Dw, AAV",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "d)",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "",
        "final accounts such as profit and\nloss.": null
      },
      {
        "": null,
        "null": null,
        "Dw, AAV": "a) B, LV",
        "final accounts such as profit and\nloss.": null
      }
    ]
  },
  {
    "page": 6,
    "table_index": 1,
    "data": [
      {
        "final accounts such as profit and": "loss."
      }
    ]
  },
  {
    "page": 6,
    "table_index": 2,
    "data": [
      {
        "Assistant Director": "(Audit)"
      }
    ]
  },
  {
    "page": 6,
    "table_index": 3,
    "data": [
      {
        "S, BN, RW, SE, C,": "MF"
      }
    ]
  },
  {
    "page": 6,
    "table_index": 4,
    "data": [
      {
        "Senior Audit": "Officer"
      }
    ]
  },
  {
    "page": 6,
    "table_index": 5,
    "data": [
      {
        "S, BN, RW, SE, C,": "MF"
      }
    ]
  },
  {
    "page": 6,
    "table_index": 6,
    "data": [
      {
        "Additional": "Controller Auditor"
      },
      {
        "Additional": "General of India /"
      },
      {
        "Additional": "Pr. CGA"
      }
    ]
  },
  {
    "page": 6,
    "table_index": 7,
    "data": [
      {
        "S, BN, MF, RW,": "SE, C"
      }
    ]
  }
]
    """

    fitz_content = '''
        1162  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 ANNEXURE-C 
POST IDENTIFIED TO BE RESERVED FOR PERSONS WITH BENCHMARK DISABILITIES IN GROUP A 
Sl. 
No. 
Designation 
Functional 
Requirements 
Suitable category of 
Benchmark 
Disabilities 
Nature of work performed 
Working Condition/Remarks 
1 
2 
3 
4 
5 
6 
 
1. ACCOUNTS& AUDIT 
1. 
Assistant 
Accounts General 
(Audit) / Assistant 
Accountant  
General (Audit) 
S, BN, RW, SE, C, 
MF 
a) D, HH 
b) OA, BA, OL, 
BL, OAL, LC, 
Dw, AAV 
c) MD involving 
(a) to (b) above 
They examine account books and 
records of business establishments, 
private institutions, Government or 
Quasi 
Government 
offices 
for 
accuracy and completeness of book 
keeping 
records 
and 
financial 
statement. Check items of entries in 
day book or journal for correct 
recording, scrutinise bills, vouchers 
and relevant entries in cash books. 
Verify 
ledger 
entries 
against 
receipts for cash payment. Check 
total for proper observance of 
accounts procedure and ensure that 
all revenue and expenditure and 
disbursements 
and 
properly 
authorized, vouched and correctly 
classified. Report to appropriate 
authority irregularities in accounts, 
improper expenditure etc. May 
prepare financial statement and 
The work is performed mostly inside 
in well lighted rooms. The workers 
usually work alone. Occasional group 
activity is required. No hazards are 
involved. Mobility should not be 
restricted with use of appliance for 
field 
duties.Incumbentshould 
be 
considered with appropriate  aids& 
appliances as per needs. 
2. 
Director (Audit) 
S, BN, RW, SE, C, 
MF 
a) D, HH 
b) OA,  BA, OL, 
BL, OAL, LC, 
Dw, AAV 
c) MD involving 
(a) to (b) above 
3. 
Joint Director 
(Audit)  
S, BN, RW, SE, C,  
MF 
a) D, HH 
b) OA, BA, OL, 
BL, OAL, LC, 
Dw, AAV 
c) MD involving 
(a) to (b) above 
4. 
Deputy Director 
(Audit) 
S, BN, RW, SE, C,  
MF 
a) D, HH 
b) OA,  BA, OL, 
BL, OAL, LC, 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1163 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
Dw, AAV 
c) MD involving 
(a) to (b) above 
final accounts such as profit and 
loss. 
5. 
Assistant Director 
(Audit) 
S, BN, RW, SE, C,  
MF 
a) D, HH 
b) OA, BA, OL, 
BL, OAL, LC, 
DW, AAV 
c) MD involving 
(a) to (b) above 
6. 
Senior Audit 
Officer 
S, BN, RW, SE, C, 
MF 
a) D, HH 
b) OA, BA, OL, 
BL, OAL, LC, 
Dw, AAV 
c) MD involving 
(a) to (b) above 
d)  
7. 
Additional 
Controller Auditor 
General of India /  
Pr. CGA 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA,  BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 
They 
 
 
ensure 
 
 
proper  
maintenance   of accounts, accounts 
books, records of business and 
financial establishments, private 
institutions, Govt. or Quasi-Govt. 
offices. Supervise subordinates e.g. 
Account 
Clerks 
engaged 
in 
maintenance 
of 
accounts 
and 
records. Scrutinize bills, receipts, 
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. It does not involve any 
hazards. 
They 
have 
to 
perform 
supervisory and leadership role with 
good communication skill.. For field 
work, mobility of the incumbent 
should 
not 
be 
restricted.  
Incumbentshould be considered with 
8. 
Assistant 
S, BN, MF, RW, 
a) B, LV 


1164  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
Controller of 
Accounts 
SE, C 
b) D, HH 
c) OA,  BA, OL, 
BL, OAL, 
BLOA, 
BLA,LC, Dw, 
AAV 
d) MD 
involving(a) to 
(c) above 
payment etc. for proper entries in 
cash -book, journal, ledger    and 
other records. Keep record of all 
taxes, licenses, fees etc., required to 
be paid by organization in which 
engaged and ensure that they are 
paid in time   and kept   up-to-date.  
Get   annual   budget prepared and 
consolidated 
under 
their 
supervision and place it before 
'Board' or appropriate authority for 
consideration. 
Prepare 
final 
accounts such    as trial balance, 
profit and loss statement or such 
balance sheet etc., as required 
depending upon type of industry or 
organization in which   engaged 
See   that   prescribed   accounting  
procedure    is followed by offices, 
establishments 
and 
institutions  
and    account    books    are 
properly maintained. Ensure   that  
instructions   given   or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks 
of 
accounts. 
Advise 
appropriate authority on financial 
matters including revenue  and  
appropriate  aids& appliances as per 
needs. 
9. 
Deputy Director 
(Accounts) 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1165 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
expenditure  such  as  procedure  
for procurement of raw materials, 
machinery and other purchases  and  
also  disposal  of  assets,  write  off 
depreciation, award of contract etc., 
10. 
Assistant Director 
(Finance &Tariff) 
S, BN, MF, RW, 
SE 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, LC, Dw, 
AAV, MDy 
d) MI 
e) MD involving 
(a) to (d) above 
Finance & Tariff fixation matters, 
supervise work of subordinates. 
Work is performed inside and Should 
have functional communication skills 
with assistive listening devices to 
communicate with subordinates. .  
Incumbent should be considered with 
appropriate  aids& appliances as per 
needs. 
11. 
Assistant 
Registrar 
(Accounts) 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 
They 
 
 
ensure 
 
 
proper  
maintenance   of accounts, accounts 
books, records of business and 
financial establishments, private 
institutions, Govt. or Quasi Govt. 
offices. Supervise subordinates e.g. 
Account 
Clerks 
engaged 
in 
maintenance 
of 
accounts 
and 
records. Scrutinize bills, receipts, 
payment etc. for proper entries in 
cash -book, journal, ledger    and 
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. It does not involve any 
hazards. 
They 
have 
to 
perform 
supervisory and leadership role.  Good 
communication skill is required. For 
field work, mobility of the incumbent 
should not be restricted. Incumbent 
should be considered with appropriate 
software,  aids& appliances as per 
needs. 


1166  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
other records. Keep record of all 
taxes, licenses, fees etc., required to 
be paid by organization in which 
engaged and ensure that they are 
paid in time   and kept   up-to-date.  
Get   annual   budget prepared and 
consolidated 
under 
their 
supervision and place it before 
'Board' or appropriate authority for 
consideration. 
Prepare 
final 
accounts such    as trial balance, 
profit and loss statement or such 
balance sheet etc., as required 
depending upon type of industry or 
organization in which   engaged 
See   that   prescribed   accounting  
procedure    is followed by offices, 
establishments 
and 
institutions  
and    account    books    are 
properly maintained. Ensure   that  
instructions   given   or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks 
of 
accounts. 
Advise 
appropriate authority on financial 
matters including revenue  and  
expenditure  such  as  procedure  
for procurement of raw materials, 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1167 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
machinery and other purchases  and  
also  disposal  of  assets,  write  of 
depreciation, award of contract etc. 
12. 
General Manager 
(Finance) 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 
Planning and scheduling work of 
section,     deal   with   non-routine 
cases referred to, keep   track of  
paper movement,   hold   meetings 
to discuss sections work. 
 
In case work place is in difficult 
terrains and field independent mobility 
with the help of aids and appliances 
should be checked.  
Incumbent should be considered with 
appropriate 
software, 
 
aids& 
appliances as per needs. 
13. 
Deputy  General 
Manager 
 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA,  BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 
Maintain 
books 
and 
accounts  
register, prepare   periodic   returns, 
Pass   bills, supervise and delegate 
work to juniors.  
 
 
 
In case work place is in difficult 
terrains and field independent mobility 
with the help of aids and appliances 
should be checked.  
Incumbent should be considered with 
appropriate 
software, 
 
aids& 
appliances as per needs. 
14. 
Chief Finance 
Manager 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA,  BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
Maintain 
books 
and 
accounts  
register, prepare   periodic   returns, 
Pass   bills,supervise work of  
sub-ordinates. Work delegation to 
juniors.  
 
 
In case work place is in difficult 
terrains 
and 
field 
independent 
mobility with the help of aids and 
appliances should be checked.  


1168  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
d) MD involving 
(a) to (c) above 
 
Incumbent should be considered with 
appropriate 
software, 
 
aids 
& 
appliances as per needs. 
15. 
Finance Manager 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA,  BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 
16. 
Finance Manager 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA,  BA, OL, 
BL, OAL, 
BLOA, LC, 
Dw, AAV 
d) MD involving 
(a) to (c) above  
They 
 
 
ensure 
 
 
proper  
maintenance   of accounts, accounts 
books, records of business and 
financial establishments, private 
institutions, Govt. or Quasi Govt. 
offices. Supervise subordinates e.g. 
Account 
Clerks 
engaged 
in 
maintenance 
of 
accounts 
and 
records. Scrutinize bills, receipts, 
payment etc. for proper entries in 
cash -book, journal, ledger    and 
other records. Keep record of all 
taxes,    licenses, fees  etc.,  
required  to  be  paid  by  
organization in which  engaged  
and  ensure  that  they are  paid in 
time   and kept   up-to-date.   Gets  
annual   budget prepared and 
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. Itdoes not involve any 
hazards. 
They 
have 
to 
perform 
supervisory 
and 
leadership 
role. 
During discussion and presentation, 
good communication skill  is required. 
For field work, mobility of the 
incumbent should not be restricted. 
Incumbent should be considered with 
appropriate 
software, 
 
aids& 
appliances as per needs. 
17. 
Manager 
(Financial ) 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA,  BA, OL, 
BL, OAL, 
BLOA, LC, 
Dw, AAV 
d) MD involving 
(a) to (c) above 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1169 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
consolidated 
under 
their 
supervision and place it before 
'Board' or appropriate authority for 
consideration. 
Prepare 
final 
accounts such    as trial  balance,  
profit  and  loss  statement  or  such  
balance sheet etc. , as required 
depending upon type of industry 
ororganization in which   engaged 
See   that   prescribed   accounting  
procedure    is followed by offices, 
establishments 
and 
institutions  
and    account    books    are 
properly maintained. Ensure   that  
instructions   given   or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks 
of 
accounts. 
Advise 
appropriate authority on financial 
matters including revenue  and  
expenditure  such  as  procedure  
for procurement of raw materials, 
machinery and other purchases  and  
also  disposal  of  assets,  write  of 
depreciation, award of contract etc. 
 


1170  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
18. 
Accounts 
Manager 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, OL, BL, 
OAL, BLOA, 
BLA, LC, Dw, 
AAV 
d) MD involving 
(a) to (c) above 
They 
 
 
ensure 
 
 
proper  
maintenance   of accounts, accounts 
books, records of business and 
financial establishments, private 
institutions, Govt. or Quasi Govt. 
offices. Supervise subordinates e.g. 
Account 
Clerks 
engaged 
in 
maintenance 
of 
accounts 
and 
records. Scrutinize bills, receipts, 
payment etc. for proper entries in 
cash -book, journal, ledger    and 
other records. Keep record of all 
taxes, licenses, fees etc., required to 
be paid by organization in which 
engaged and ensure that they are 
paid in time   and kept   up-to-date.  
Get   annual   budget prepared and 
consolidated 
under 
their 
supervision and place it before 
'Board' or appropriate authority for 
consideration. 
Prepare 
final 
accounts such    as trial balance, 
profit and loss statement or such 
balance sheet etc., as required 
depending upon type of industry or 
organization in which   engaged 
See   that   prescribed   accounting  
procedure    is followed by offices, 
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. It does not involve any 
hazards. 
They 
have 
to 
perform 
supervision and leadership role. During 
discussion and presentation, good 
communication skill  is required. For 
field work, mobility of the incumbent 
should not be restricted.  Incumbent 
should be considered with appropriate 
software,  aids& appliances as per 
needs. 
19. 
Joint Manager 
(Accounts) 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1171 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
establishments 
and 
institutions  
and    account    books    are 
properly maintained. Ensure   that  
instructions   given   or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks 
of 
accounts. 
Advise 
appropriate authority on financial 
matters including revenue  and  
expenditure  such  as  procedure  
for procurement of raw materials, 
machinery and other purchases  and  
also  disposal  of  assets,  write  of 
depreciation, award of contract etc. 
20. 
Deputy Finance 
Manager  
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 
Maintain 
books 
and 
accounts  
register, prepare   periodic   returns, 
Pass   bills, Work delegation to 
juniors.  
In case, work place is in difficult 
terrains and field independent mobility 
with the help of aids and appliances 
should be checked. Incumbent should 
be 
considered 
with 
appropriate 
software,  aids& appliances as per 
needs. 
21. 
Deputy Manager 
(Finance and 
Accounts) 
S, ST, W, BN, 
RW, SE, H, C, MF 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
Administrating 
the 
Institutions, 
monitoring, day-to-day functioning 
of the institutions, staff training, 
The work is performed both inside and 
outside. The work place is well lighted. 
Touring is involved.  Incumbent 


1172  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
BL, OAL, LC, 
Dw, AAV 
d) MD involving 
(a) to (c) above 
 
 
 
 
 
organization 
development, 
seminars/workshops 
for 
quality 
improvement, IT solutions, public 
relations.  To advise on all matters 
of 
policy 
and 
administration.  
Scrutinize proposals for expansion 
of administrative staff, Coordinate 
activities of various units of the 
office, decide the disciplinary action 
to be taken against staff as per rules 
and regulations laid down by the 
Department of personnel and make 
policy decisions in the matter of 
administration.  Implement policies 
of the Govt.    
should be considered with appropriate 
software,  aids& appliances as per 
needs. 
22. 
Assistant Manager 
(Finance) 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
d) MD involving 
(a) to (c) above 
They 
 
 
ensure 
 
 
proper  
maintenance   of accounts, accounts 
books, records of business and 
financial establishments, private 
institutions, Govt. or Quasi Govt. 
offices. Supervise subordinates e.g. 
Account 
Clerks 
engaged 
in 
maintenance 
of 
accounts 
and 
records. Scrutinize bills, receipts, 
payment etc. for proper entries in 
cash -book, journal, ledger    and 
other records. Keep record of all 
taxes, licenses, fees etc., required to 
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. It does not involve any 
hazards. 
They 
have 
to 
perform 
supervisory and leadership role. Good  
communication is required. For field 
work, mobility of the incumbent 
should not be restricted.  Incumbent 
should be considered with appropriate 
software,  aids& appliances as per 
needs. 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1173 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
be paid by organization in which 
engaged and ensure that they are 
paid in time   and kept   up-to-date.  
Get   annual   budget prepared and 
consolidated 
under 
their 
supervision and place it before 
'Board' or appropriate authority for 
consideration. 
Prepare 
final 
accounts such    as trial balance, 
profit and loss statement or such 
balance sheet etc., as required 
depending upon type of industry or 
organization in which   engaged 
See   that   prescribed   accounting  
procedure    is followed by offices, 
establishments 
and 
institutions  
and    account    books    are 
properly maintained. Ensure   that  
instructions   given   or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks 
of 
accounts. 
Advise 
appropriate authority on financial 
matters including revenue  and  
expenditure  such  as  procedure  
for procurement of raw materials, 


1174  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
machinery and other purchases  and  
also  disposal  of  assets,  write  of 
depreciation, award of contract etc. 
23. 
Assistant Finance 
Manager 
S, BN, MF, RW, 
SE, C 
a) D, HH 
b) OA, BA, OL, 
BL, OAL, 
BLOA, LC, 
Dw, AAV 
c) MD involving 
(a) to (b) above 
Maintain payment records, Bill 
passing, 
Record 
 
 
keeping,  
Maintain   records   of sales   tax,  
income   tax   etc .Payments 
Documentation, Data feeding of 
financial 
transactions, 
Budget 
preparation, Supervisory.  
 
Maintain  books  and  accounts  
register, Prepare   periodic   returns,  
Pass   bills, Work delegation to 
juniors.  
 
Planning and scheduling work of 
section,   shall   deal   with   non-
routine cases referred, keep   track 
of    paper movement   ,   hold  
meeting   to discuss sections work. 
 
In case, work place is in terrains and 
field, independent mobility with the 
help of aids and appliances should be 
checked.Incumbent 
should 
be 
considered with appropriate software,  
aids& appliances as per needs. 
24. 
Assistant General 
Manager  
(F & A) 
S, ST, W, BN, MF, 
RW, SE 
 
a) D, HH 
b) OA, BA, OL, 
LC, Dw, AAV 
c) ASD(M), SLD, 
MI 
e) MD involving 
All 
Taxation 
matter 
Financial 
Analysis, Accounts 
Should have Managerial capacity, 
Should have functional commutation 
skills 
with 
effective 
listening 
devices.Incumbent 
should 
be 
considered with appropriatesoftware,  
aids& appliances as per needs. 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1175 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
(a) to (c) above 
25. 
Officer, Corporate 
Finance  
S, W,  MF,  RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, LC, 
Dw, AAV, MDy 
d) ASD (M), MI 
e) MD involving 
(a) to (d) above 
They develop and apply most 
effective methods for collecting, 
tabulating & interpreting data in 
any one of wide variety of fields. 
Determine character and volume of 
information necessary for solution 
of any problem and obtain or 
devise 
methods 
for 
collecting 
necessary information. Determine 
most 
effective 
techniques 
for 
production 
of 
data 
required 
according to nature of available 
information and type of problem 
under Deputy Interpret and present 
data in the required form. May 
write 
reports 
analyzing 
and 
evaluating conclusions on the basis 
of variable conditions affecting 
interpretation of validity. May 
advise 
and 
consult 
private 
industrial concerns or government 
agencies 
on 
matters 
such 
as 
operating 
efficiency, 
marketing 
methods 
and 
fiscal 
problems. 
The work is performed inside. The 
work place is well lighted and 
comfortable. The worker usually 
works alone though some public 
dealing is required. The Branch 
incharge has to do field work also and 
the in the field, may be work place is 
hot, humid and dusty. Should have 
normal 
bilateral 
hand 
functions.Incumbent to be considered 
with use of aids / appliances as per 
needs. 
 
 
 
 


1176  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
Collection, analyzing of statistical 
data, preparation of reports, update 
statistics etc. 
26. 
Corporate Finance 
Officer 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, LC, Dw, 
AAV, MDy 
d) MD involving 
(a) to (c) above 
Duties   assigned   by   appropriate 
authority, 
Informs 
financial 
position 
of 
the 
organization, 
responsible   for   proper  
implementation 
of 
financial 
transactions as per accounts   code/ 
Statutes/ 
Ordinances/ 
rules 
& 
regulations. 
Incase work place is in difficult 
terrains 
and 
field 
independent 
mobility with the help of aids and 
appliances 
should 
be 
checked. 
Incumbent to be considered with use 
of aids / appliances as per needs. 
 
 
27. 
Assistant 
Divisional 
Accounts Officer  
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV, 
MDy 
d) MD involving 
(a) to (c) above 
They 
 
 
ensure 
 
 
proper  
maintenance   of accounts, accounts 
books, records of business and 
financial establishments, private 
institutions, Govt. or Quasi Govt. 
offices. Supervise subordinates e.g. 
Account 
Clerks 
engaged 
in 
maintenance 
of 
accounts 
and 
records. Scrutinize bills, receipts, 
payment etc. for proper entries in 
cash -book, journal, ledger    and 
other records. Keep record of all 
taxes, licenses, fees etc., required to 
be paid by organization in which 
engaged and ensure that they are 
paid in time   and kept   up-to-date.  
Get   annual   budget prepared and 
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. It does not involve any 
hazards. 
They 
have 
to 
perform 
supervisory 
and 
leadership 
role. 
Should have good  communication 
skill. For field work, mobility of the 
incumbent should not be restricted.   
Incumbent should be considered with 
appropriate 
software, 
 
aids 
& 
appliances as per needs. 
28. 
Chief Accountant 
S, BN, MF, RW, 
SE, C 
a) D, HH 
b) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV 
c) MD involving 
(a) to (b) above 
29. 
Chief Accounts 
S, BN, MF, RW, 
a) B, LV 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1177 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
Officer 
SE, C 
b) D, HH 
c) OA, OL, BL, 
OAL, BLOA, 
BLA, LC, Dw, 
AAV 
d) MD involving 
(a) to (c) above 
consolidated 
under 
their 
supervision and place it before 
'Board' or appropriate authority for 
consideration. 
Prepare 
final 
accounts such    as trial balance, 
profit and loss statement or such 
balance sheet etc., as required 
depending upon type of industry or 
organization in which   engaged 
See   that   prescribed   accounting  
procedure    is followed by offices, 
establishments 
and 
institutions  
and    account    books    are 
properly maintained. Ensure   that  
instructions   given   or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks 
of 
accounts. 
Advise 
appropriate authority on financial 
matters including revenue  and  
expenditure  such  as  procedure  
for procurement of raw materials, 
machinery and other purchases  and  
also  disposal  of  assets,  write  of 
depreciation, award of contract etc. 
30. 
Deputy Chief 
Accounts Officer 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, OL, BL, 
OAL, BLOA, 
BLA, LC, Dw, 
AAV 
d) MD involving 
(a) to (c) above 
31. 
Assistant Chief 
Accounts Officer 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, OL, BL, 
OAL, BLOA, 
BLA, LC, Dw, 
AAV 
d) MD involving 
(a) to (c) above 


1178  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
32. 
Accounts Officer-
II 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV, 
MDy 
d) MD involving 
(a) to (c) above 
Maintain payment records, Bill 
passing, Record   keeping, Maintain  
records   of sales   tax, income   tax  
etc. Payments Documentation, Data 
feeding of financial transactions, 
Budget preparation, Supervisory. 
 
Planning and scheduling work of 
section,   shall   deal   with   non-
routine Cases referred, keep   track 
of    paper movement ,   hold  
meeting   to discuss sections work. 
In case work place is in difficult 
terrains 
and 
field 
independent 
mobility with the help of aids and 
appliances 
should 
be 
checked..Incubents to be considred 
with aids and assistive devices as per 
needs. 
 
 
33. 
Accounts Officer-
I 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV, 
MDy 
d) MD involving 
(a) to (c) above 
34. 
Finance Officer 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
LC, Dw, AAV, 
MDy 
d) MD 
involving(a) to 
(c) above 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1179 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
35. 
Officer Scale - I 
S, ST, W,  BN, 
RW, SE, H, C, MF 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
OAL, CP, LC, 
Dw, AAV, MDy 
d) MD involving 
(a) to (c) above 
They ensure proper maintenance of 
accounts, accounts books, records 
of 
business 
and 
financial 
establishments, private institutions, 
Govt. Or Quasi Got. Offices. 
Supervise subordinates engaged in 
maintenance 
of 
accounts 
and 
records. Scrutinize ledger and other 
records. Keep record of all taxes, 
licenses, fees etc. required to be 
paid by the organization in which 
engaged and ensure that they are 
paid in time and kept up-to-date. 
Get annual budget prepared and 
consolidated 
under 
their 
supervision and place it before 
Board or appropriate authority for 
consideration. 
Prepare 
final 
accounts such as trial balance, 
profit and loss statement or such 
balance sheet etc. as required 
depending upon type of industry or 
organization in which engaged. See 
that 
prescribed 
accounting 
procedure is followed by offices, 
establishments and institutions as 
The work is mostly performed inside 
the well-lighted rooms. They have to 
perform supervisory and leadership 
role. 
During 
discussion 
and 
presentation, communication skill is 
required. For field work mobility of the 
incumbent 
should 
not 
be 
restricted.Incumbent 
should 
be 
considered with appropriate software,  
aids& appliances as per needs. 


1180  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
well as account books are properly 
maintained. Ensure that instructions 
given or objections raised are 
carried out or rectified. Make 
periodical and surprise checks of 
accounts. 
36. 
Financial 
&Accounts 
Officer 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, CP, LC, 
Dw, AAV, 
MDy 
d) MD involving 
(a) to (c) above 
To ensure   proper   maintenance  
of 
accounts, 
accounts 
books, 
records of business and financial 
establishments, private institutions, 
Govt. or Quasi Govt. offices. 
Supervise subordinates e.g. Account 
Clerks engaged in maintenance of 
accounts and records. Scrutinize 
bills, receipts, payment etc. for 
proper 
entries 
in 
cash 
-book, 
journal, ledger    and other records. 
Keep record of all taxes,    licenses, 
fees  etc.,  required  to  be  paid  by  
organization in which  engaged  and  
ensure  that  they are  paid in time  
and kept   up-to-date.   Get   annual  
budget prepared and consolidated 
under their supervision and place it 
before 
'Board' 
or 
appropriate 
authority for consideration. Prepare 
final accounts such    as trial  
balance,  profit  and  loss  statement  
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. Itdoes not involve any 
hazards. They have to play supervisory 
and leadership role. During discussion 
and presentation, good  communication 
skill is required. For field work, 
mobility of the incumbent should not 
be 
restricted 
Incubents 
to 
be 
considered with the use of aids and 
assistive devices as per requirement. 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1181 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
or  such  balance sheet etc. , as 
required depending upon type of 
industry ororganization in which  
engaged See   that   prescribed  
accounting   procedure    is followed 
by 
offices, 
establishments 
and 
institutions    and    account    books  
are properly maintained. Ensure  
that   instructions   given   or 
objections raised are carried out or 
rectified.  Make periodical and 
surprise checks of accounts. Advise 
appropriate authority on financial 
matters including revenue  and  
expenditure  such  as  procedure  for 
procurement 
of 
raw 
materials, 
machinery and other purchases  and  
also  disposal  of  assets,  write  of 
depreciation, award of contract etc. 
37. 
Finance & 
Accounts Officer 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, CP, LC, 
Dw, AAV, 
Maintain payment records, Bill 
passing, 
Record 
 
 
keeping,  
Maintain   records   of sales   tax,  
income   tax   etc .Payments 
Documentation, Data feeding of 
financial 
transactions, 
Budget 
 
In case work place is in difficult 
terrains and field independent mobility 
with the help of aids and appliances 
should be checked. Incumbents to be 
considered with the use of aids and 


1182  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
MDy 
d) MD involving 
(a) to (c) above 
preparation, Supervisory.  
 
Maintain  books  and  accounts  
register, Prepare   periodic   returns,  
Pass   bills, Work delegation to 
juniors.  
 
Planning and scheduling work of 
section,   shall   deal   with   non-
routine Cases referred, keep   track 
of    paper movement   ,   hold  
meeting   to discuss sections work. 
assistive devices. 
38. 
Deputy Finance 
Officer 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, CP, LC, 
Dw, AAV, MDy 
d) MD involving 
(a) to (c) above 
Duties   assigned   by   appropriate 
authority, Informs financial position 
of the organization, responsible   for  
proper   implementation of financial 
transactions as per accounts   code/ 
Statutes/ 
Ordinances/ 
rules 
& 
regulations. 
In case, work place is in difficult 
terrains and field independent mobility 
with the help of aids and appliances 
should be checked. Incumbents to be 
considered with the use of aids and 
assistive devices. 
39. 
Assistant 
AccountGeneral/A
ssistant  
Accountant 
General 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
CP, LC, Dw, 
AAV, MDy 
d) MD involving 
(a) to (c) above 
To   ensure   proper   maintenance  
of 
accounts, 
accounts 
books, 
records of business and financial 
establishments, private institutions, 
Govt. or Quasi Govt. offices. 
Supervise 
subordinates 
e.g. 
Account 
Clerks 
engaged 
in 
maintenance 
of 
accounts 
and 
records. Scrutinize bills, receipts, 
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. It does not involve any 
hazards. 
They 
have 
to 
perform 
supervisory and  leadership role. 
During discussion and presentation 
good  communication skill is  required. 
For field work, mobility of the 
incumbent should not be restricted.  


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1183 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
payment etc. for proper entries in 
cash -book, journal, ledger    and 
other records. Keep record of all 
taxes, licenses, fees etc., required to 
be paid by organization in which 
engaged and ensure that they are 
paid in time   and kept   up-to-date.  
Get   annual   budget prepared and 
consolidated 
under 
their 
supervision and place it before 
'Board' or appropriate authority for 
consideration. 
Prepare 
final 
accounts such    as trial balance, 
profit and loss statement or such 
balance sheet etc., as required 
depending upon type of industry or 
organization in which   engaged 
See   that   prescribed   accounting  
procedure    is followed by offices, 
establishments 
and 
institutions  
and    account    books    are 
properly maintained. Ensure   that  
instructions   given   or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks 
of 
accounts. 
Advise 
Incumbent should be considered with 
appropriate 
software, 
 
aids& 
appliances as per needs. 


1184  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
appropriate authority on financial 
matters including revenue  and  
expenditure  such  as  procedure  
for procurement of raw materials, 
machinery and other purchases  and  
also  disposal  of  assets,  write  of 
depreciation, award of contract etc. 
40. 
Assistant Finance 
Officer 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, CP, LC, 
Dw, AAV, MDy 
d) MD involving 
(a) to (c) above 
Duties   assigned   by   appropriate 
authority, Informs financial position 
of the organization, responsible   for  
proper   implementation of financial 
transactions as per accounts   code/ 
Statutes/ 
Ordinances/ 
rules 
& 
regulations. 
In case work place is in difficult 
terrains and field independent mobility 
with the help of aids and appliances 
should be checked.Incumbent should 
be 
considered 
with 
appropriate 
software,  aids& appliances as per 
needs. 
41. 
Section Officer 
(Accounts & 
Audit) 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, CP, LC, 
Dw, AAV, MDy 
d) MD involving 
(a) to (c) above 
42. 
Selection Grade  
in JAG 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
CP, LC, Dw, 
AAV, MDy 
Maintain payment records, Bill 
passing, Record   keeping, Maintain  
records   of sales   tax, income   tax  
etc. Payments Documentation, Data 
feeding of financial transactions, 
Budget preparation, Supervisory.  
 
 
In case work place is in difficult 
terrains 
and 
field, 
independent 
mobility with the help of aids and 
appliances 
should 
be 
checked.Incumbent 
should 
be 
considered with appropriate software,  


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1185 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
d) MD involving 
(a) to (c) above 
aids& appliances as per needs. 
43. 
Senior 
Administrative 
Grade 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
CP, LC, Dw, 
AAV, MDy 
d) MD involving 
(a) to (c) above 
They 
 
 
ensure 
 
 
proper  
maintenance   of accounts, accounts 
books, records of business and 
financial establishments, private 
institutions, Govt. or Quasi Govt. 
offices. Supervise subordinates e.g. 
Account 
Clerks 
engaged 
in 
maintenance 
of 
accounts 
and 
records. Scrutinize bills, receipts, 
payment etc. for proper entries in 
cash -book, journal, ledger    and 
other records. Keeps record of all 
taxes, licenses, fees etc., required to 
be paid by organization in which 
engaged and ensure that they are 
paid in time   and kept   up-to-date.  
Get   annual   budget prepared and 
consolidated 
under 
their 
supervision and place it before 
'Board' or appropriate authority for 
consideration. 
Prepare 
final 
accounts such    as trial balance, 
profit and loss statement or such 
The work is mostly performed inside 
in well lighted rooms. Worker usually 
works alone. It does not involve any 
hazards. 
They 
have 
to 
perform 
supervisory 
and 
leadership 
role. 
During discussion and presentation, 
good  communication skill  is required. 
For field work, mobility of the 
incumbent should not be restricted.  
Incumbent should be considered with 
appropriate software,  aids&appliances 
as per needs. 


1186  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
balance sheet etc., as required 
depending upon type of industry or 
organization in which   engaged 
See   that   prescribed   accounting  
procedure    is followed by offices, 
establishments 
and 
institutions  
and    account    books    are 
properly maintained. Ensure   that  
instructions   given   or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks 
of 
accounts. 
Advise 
appropriate authority on financial 
matters including revenue  and  
expenditure  such  as  procedure  
for procurement of raw materials, 
machinery and other purchases  and  
also  disposal  of  assets,  write  of 
depreciation, award of contract etc. 
44. 
Senior Time Scale 
S, BN, MF, RW, 
SE, C 
a) LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
CP, LC, Dw, 
AAV, MDy 
d) MD involving 
(a) to (c) above 
Maintain payment records, Bill 
passing, Record   keeping, Maintain  
records   of sales   tax, income   tax  
etc. Payments Documentation, Data 
feeding of financial transactions, 
Budget preparation, Supervisory.  
 
 
In case work place is in difficult 
terrains 
and 
field 
independent 
mobility with the help of aids and 
appliances 
should 
be 
cheked.Incumbent 
should 
be 
considered with appropriate software,  
aids& appliances as per needs. 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1187 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
45. 
 
Executive  
(Finance 
/Account) 
 
 
S, ST, W, BN, 
RW, SE,  H, C, 
MF 
a) LV 
b) D, HH 
c) OA, BA, OL, 
OAL, CP, LC, 
Dw, AAV, MDy 
d) MD involving 
(a) to (c) above 
They ensure proper maintenance of 
accounts, accounts books, records 
of 
business 
and 
financial 
establishments, private institutions, 
Govt. or Quasi Govt. offices.  
Supervise subordinates engaged in 
maintenance 
of 
accounts 
and 
records.  Scrutinize ledger and 
other records.  Keep record of all 
taxes, licenses, fees etc.  Required 
to be paid by the organization in 
which engaged and ensure that they 
are paid in time and kept up-to-
date.  Get annual budget prepared 
and 
consolidated 
under 
their 
supervision and place it before 
Board or appropriate authority for 
consideration. 
 
Prepare 
final 
accounts such as trial balance, 
profit and loss statement or such 
balance sheet etc. as required 
depending upon type of industry or 
organization in which engaged.  
See that prescribed accounting 
procedure is followed by offices, 
establishments and institutions as 
In case work place is in difficult 
terrains and field independent mobility 
with the help of aids and appliances 
should be checked. Incumbent should 
be 
considered 
with 
appropriate 
software,  aids& appliances as per 
needs. 


1188  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
well as account books are properly 
maintained. 
 
Ensure 
that 
instructions given or objections 
raised are carried out or rectified.  
Make 
periodical 
and 
surprise 
checks of accounts.   
46. 
Junior Executive 
(Finance) 
S, ST, W, BN, 
RW, SE, H, C, MF 
a) B, LV  
b) D, HH 
c) OA, BA, OL, 
BL, OAL, CP, 
LC, Dw, AAV, 
MDy 
d) MD involving 
(a) to (c) above 
 
Controlling 
&supervising 
cash 
section,scrutiny of files relating to 
purchase/amounts 
spent 
by 
Administration Department  
Works Contract Tax, Deposit of 
Work 
Contract 
Tax, 
thereafter 
issuance 
of 
Form-IX 
TDS 
certificate to firms and submission 
of same to Sales Tax Department. 
Salary and payroll bills, of Head 
Office and Zonal Offices. TA Bills, 
Medical Bills, LTC Bills Leave 
Encashment  
Monthly 
Expenditure 
Bills 
/Statements of ZO. Submission of 
Monthly 
parameters 
related 
to 
MOU to the Coordination Wing. 
Advance to staff. Work relating to 
placement of surplus funds with 
banks. Finalization of PF returns 
&Issuance 
related 
returns, 
monthly/Annual as per the statutory 
The work is mostly performed inside 
in well lighted rooms. The worker 
usually does his work alone. It does 
not involve any hazard.   
Incumbent should be considered with 
appropriate 
software, 
 
aids& 
appliances as per needs. 


[भाग I — खण्‍ड 1] 
भारत‍का‍राजपत्र‍:‍असाधारण  
1189 
 
   
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
 
 
requirements. 
Preparation 
of 
schedules &Sub-schedules at the 
time of closing of accounts, there 
after preparation of Draft Balance 
Sheet. 
Attending 
to 
queries/ 
suggestions 
/observations 
of 
Statutory Auditors/CAG Auditors 
and preparation of final Balance 
Sheet. Participation of   various 
Committee 
formed 
in 
the 
Corporation. Calculation of Income 
Tax for the staff. Maintaining of 
Records of Income Tax as per 
requirement of revised rules of IT 
act. Filing of Form 16 and Form 12 
BA for staff. Issuance of Annual 
Returns in Form no.26K and 26Cfor 
contractors. 
Filing 
the 
Annual 
Returns in Form 24.Issuance of 
Form 
16A 
for 
contractors.Finalization 
of 
PF 
returns &Issuance related returns 
Monthly/Annual as per the statutory 
requirements. 
47. 
Junior 
S, BN, MF, RW, 
a) B, LV 
Maintain payment records, bill  


1190  
THE GAZETTE OF INDIA : EXTRAORDINARY 
   [PART I—SEC. 1] 
  
 
 
FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
MI= Mental Illness, MD=Multiple Disabilities 
Administrative 
Grade 
SE, C 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
CP, LC, Dw, 
AAV, MDy 
d) MD involving 
(a) to (c) above 
passing, record   keeping, maintain  
records   of sales   tax, income   tax  
etc. payments documentation, data 
feeding of financial transactions, 
budget 
preparation, 
supervisory 
work. 
 
In case, work place is in difficult 
terrains 
and 
field 
independent 
mobility with the help of aids and 
appliances 
should 
be 
checked.Incumbent 
should 
be 
considered with appropriate software,  
aids& appliances as per needs. 
48. 
Junior Time Scale 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
CP, LC, Dw, 
AAV, MDy 
d) MD involving 
(a) to (c) above 
49. 
Management 
Trainee 
(Accounts) 
S, BN, MF, RW, 
SE, C 
a) B, LV 
b) D, HH 
c) OA, BA, OL, 
BL, OAL, 
BLOA, BLA, 
CP, LC, Dw, 
AAV, MDy 
d) MD involving 
(a) to (c) above 
 
2. ADMINISTRATIVE OFFICER (SECRETARIAL) 
50. 
Secretary 
S, ST, W, RW, SE, 
a) B, LV 
Administrating 
the 
institutions, The work is mostly performed inside 




    '''
    
    fitz_content_without_header ="""
        [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1163 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    Dw, AAV 
    c) MD involving 
    (a) to (b) above 
    final accounts such as profit and 
    loss. 
    5. 
    Assistant Director 
    (Audit) 
    S, BN, RW, SE, C,  
    MF 
    a) D, HH 
    b) OA, BA, OL, 
    BL, OAL, LC, 
    DW, AAV 
    c) MD involving 
    (a) to (b) above 
    6. 
    Senior Audit 
    Officer 
    S, BN, RW, SE, C, 
    MF 
    a) D, HH 
    b) OA, BA, OL, 
    BL, OAL, LC, 
    Dw, AAV 
    c) MD involving 
    (a) to (b) above 
    d)  
    7. 
    Additional 
    Controller Auditor 
    General of India /  
    Pr. CGA 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA,  BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 
    They 
    
    
    ensure 
    
    
    proper  
    maintenance   of accounts, accounts 
    books, records of business and 
    financial establishments, private 
    institutions, Govt. or Quasi-Govt. 
    offices. Supervise subordinates e.g. 
    Account 
    Clerks 
    engaged 
    in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize bills, receipts, 
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. It does not involve any 
    hazards. 
    They 
    have 
    to 
    perform 
    supervisory and leadership role with 
    good communication skill.. For field 
    work, mobility of the incumbent 
    should 
    not 
    be 
    restricted.  
    Incumbentshould be considered with 
    8. 
    Assistant 
    S, BN, MF, RW, 
    a) B, LV 


    1164  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    Controller of 
    Accounts 
    SE, C 
    b) D, HH 
    c) OA,  BA, OL, 
    BL, OAL, 
    BLOA, 
    BLA,LC, Dw, 
    AAV 
    d) MD 
    involving(a) to 
    (c) above 
    payment etc. for proper entries in 
    cash -book, journal, ledger    and 
    other records. Keep record of all 
    taxes, licenses, fees etc., required to 
    be paid by organization in which 
    engaged and ensure that they are 
    paid in time   and kept   up-to-date.  
    Get   annual   budget prepared and 
    consolidated 
    under 
    their 
    supervision and place it before 
    'Board' or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such    as trial balance, 
    profit and loss statement or such 
    balance sheet etc., as required 
    depending upon type of industry or 
    organization in which   engaged 
    See   that   prescribed   accounting  
    procedure    is followed by offices, 
    establishments 
    and 
    institutions  
    and    account    books    are 
    properly maintained. Ensure   that  
    instructions   given   or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks 
    of 
    accounts. 
    Advise 
    appropriate authority on financial 
    matters including revenue  and  
    appropriate  aids& appliances as per 
    needs. 
    9. 
    Deputy Director 
    (Accounts) 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1165 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    expenditure  such  as  procedure  
    for procurement of raw materials, 
    machinery and other purchases  and  
    also  disposal  of  assets,  write  off 
    depreciation, award of contract etc., 
    10. 
    Assistant Director 
    (Finance &Tariff) 
    S, BN, MF, RW, 
    SE 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, LC, Dw, 
    AAV, MDy 
    d) MI 
    e) MD involving 
    (a) to (d) above 
    Finance & Tariff fixation matters, 
    supervise work of subordinates. 
    Work is performed inside and Should 
    have functional communication skills 
    with assistive listening devices to 
    communicate with subordinates. .  
    Incumbent should be considered with 
    appropriate  aids& appliances as per 
    needs. 
    11. 
    Assistant 
    Registrar 
    (Accounts) 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 
    They 
    
    
    ensure 
    
    
    proper  
    maintenance   of accounts, accounts 
    books, records of business and 
    financial establishments, private 
    institutions, Govt. or Quasi Govt. 
    offices. Supervise subordinates e.g. 
    Account 
    Clerks 
    engaged 
    in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize bills, receipts, 
    payment etc. for proper entries in 
    cash -book, journal, ledger    and 
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. It does not involve any 
    hazards. 
    They 
    have 
    to 
    perform 
    supervisory and leadership role.  Good 
    communication skill is required. For 
    field work, mobility of the incumbent 
    should not be restricted. Incumbent 
    should be considered with appropriate 
    software,  aids& appliances as per 
    needs. 


    1166  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    other records. Keep record of all 
    taxes, licenses, fees etc., required to 
    be paid by organization in which 
    engaged and ensure that they are 
    paid in time   and kept   up-to-date.  
    Get   annual   budget prepared and 
    consolidated 
    under 
    their 
    supervision and place it before 
    'Board' or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such    as trial balance, 
    profit and loss statement or such 
    balance sheet etc., as required 
    depending upon type of industry or 
    organization in which   engaged 
    See   that   prescribed   accounting  
    procedure    is followed by offices, 
    establishments 
    and 
    institutions  
    and    account    books    are 
    properly maintained. Ensure   that  
    instructions   given   or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks 
    of 
    accounts. 
    Advise 
    appropriate authority on financial 
    matters including revenue  and  
    expenditure  such  as  procedure  
    for procurement of raw materials, 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1167 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    machinery and other purchases  and  
    also  disposal  of  assets,  write  of 
    depreciation, award of contract etc. 
    12. 
    General Manager 
    (Finance) 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 
    Planning and scheduling work of 
    section,     deal   with   non-routine 
    cases referred to, keep   track of  
    paper movement,   hold   meetings 
    to discuss sections work. 
    
    In case work place is in difficult 
    terrains and field independent mobility 
    with the help of aids and appliances 
    should be checked.  
    Incumbent should be considered with 
    appropriate 
    software, 
    
    aids& 
    appliances as per needs. 
    13. 
    Deputy  General 
    Manager 
    
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA,  BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 
    Maintain 
    books 
    and 
    accounts  
    register, prepare   periodic   returns, 
    Pass   bills, supervise and delegate 
    work to juniors.  
    
    
    
    In case work place is in difficult 
    terrains and field independent mobility 
    with the help of aids and appliances 
    should be checked.  
    Incumbent should be considered with 
    appropriate 
    software, 
    
    aids& 
    appliances as per needs. 
    14. 
    Chief Finance 
    Manager 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA,  BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    Maintain 
    books 
    and 
    accounts  
    register, prepare   periodic   returns, 
    Pass   bills,supervise work of  
    sub-ordinates. Work delegation to 
    juniors.  
    
    
    In case work place is in difficult 
    terrains 
    and 
    field 
    independent 
    mobility with the help of aids and 
    appliances should be checked.  


    1168  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    d) MD involving 
    (a) to (c) above 
    
    Incumbent should be considered with 
    appropriate 
    software, 
    
    aids 
    & 
    appliances as per needs. 
    15. 
    Finance Manager 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA,  BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 
    16. 
    Finance Manager 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA,  BA, OL, 
    BL, OAL, 
    BLOA, LC, 
    Dw, AAV 
    d) MD involving 
    (a) to (c) above  
    They 
    
    
    ensure 
    
    
    proper  
    maintenance   of accounts, accounts 
    books, records of business and 
    financial establishments, private 
    institutions, Govt. or Quasi Govt. 
    offices. Supervise subordinates e.g. 
    Account 
    Clerks 
    engaged 
    in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize bills, receipts, 
    payment etc. for proper entries in 
    cash -book, journal, ledger    and 
    other records. Keep record of all 
    taxes,    licenses, fees  etc.,  
    required  to  be  paid  by  
    organization in which  engaged  
    and  ensure  that  they are  paid in 
    time   and kept   up-to-date.   Gets  
    annual   budget prepared and 
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. Itdoes not involve any 
    hazards. 
    They 
    have 
    to 
    perform 
    supervisory 
    and 
    leadership 
    role. 
    During discussion and presentation, 
    good communication skill  is required. 
    For field work, mobility of the 
    incumbent should not be restricted. 
    Incumbent should be considered with 
    appropriate 
    software, 
    
    aids& 
    appliances as per needs. 
    17. 
    Manager 
    (Financial ) 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA,  BA, OL, 
    BL, OAL, 
    BLOA, LC, 
    Dw, AAV 
    d) MD involving 
    (a) to (c) above 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1169 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    consolidated 
    under 
    their 
    supervision and place it before 
    'Board' or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such    as trial  balance,  
    profit  and  loss  statement  or  such  
    balance sheet etc. , as required 
    depending upon type of industry 
    ororganization in which   engaged 
    See   that   prescribed   accounting  
    procedure    is followed by offices, 
    establishments 
    and 
    institutions  
    and    account    books    are 
    properly maintained. Ensure   that  
    instructions   given   or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks 
    of 
    accounts. 
    Advise 
    appropriate authority on financial 
    matters including revenue  and  
    expenditure  such  as  procedure  
    for procurement of raw materials, 
    machinery and other purchases  and  
    also  disposal  of  assets,  write  of 
    depreciation, award of contract etc. 
    


    1170  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    18. 
    Accounts 
    Manager 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, OL, BL, 
    OAL, BLOA, 
    BLA, LC, Dw, 
    AAV 
    d) MD involving 
    (a) to (c) above 
    They 
    
    
    ensure 
    
    
    proper  
    maintenance   of accounts, accounts 
    books, records of business and 
    financial establishments, private 
    institutions, Govt. or Quasi Govt. 
    offices. Supervise subordinates e.g. 
    Account 
    Clerks 
    engaged 
    in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize bills, receipts, 
    payment etc. for proper entries in 
    cash -book, journal, ledger    and 
    other records. Keep record of all 
    taxes, licenses, fees etc., required to 
    be paid by organization in which 
    engaged and ensure that they are 
    paid in time   and kept   up-to-date.  
    Get   annual   budget prepared and 
    consolidated 
    under 
    their 
    supervision and place it before 
    'Board' or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such    as trial balance, 
    profit and loss statement or such 
    balance sheet etc., as required 
    depending upon type of industry or 
    organization in which   engaged 
    See   that   prescribed   accounting  
    procedure    is followed by offices, 
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. It does not involve any 
    hazards. 
    They 
    have 
    to 
    perform 
    supervision and leadership role. During 
    discussion and presentation, good 
    communication skill  is required. For 
    field work, mobility of the incumbent 
    should not be restricted.  Incumbent 
    should be considered with appropriate 
    software,  aids& appliances as per 
    needs. 
    19. 
    Joint Manager 
    (Accounts) 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1171 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    establishments 
    and 
    institutions  
    and    account    books    are 
    properly maintained. Ensure   that  
    instructions   given   or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks 
    of 
    accounts. 
    Advise 
    appropriate authority on financial 
    matters including revenue  and  
    expenditure  such  as  procedure  
    for procurement of raw materials, 
    machinery and other purchases  and  
    also  disposal  of  assets,  write  of 
    depreciation, award of contract etc. 
    20. 
    Deputy Finance 
    Manager  
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 
    Maintain 
    books 
    and 
    accounts  
    register, prepare   periodic   returns, 
    Pass   bills, Work delegation to 
    juniors.  
    In case, work place is in difficult 
    terrains and field independent mobility 
    with the help of aids and appliances 
    should be checked. Incumbent should 
    be 
    considered 
    with 
    appropriate 
    software,  aids& appliances as per 
    needs. 
    21. 
    Deputy Manager 
    (Finance and 
    Accounts) 
    S, ST, W, BN, 
    RW, SE, H, C, MF 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    Administrating 
    the 
    Institutions, 
    monitoring, day-to-day functioning 
    of the institutions, staff training, 
    The work is performed both inside and 
    outside. The work place is well lighted. 
    Touring is involved.  Incumbent 


    1172  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    BL, OAL, LC, 
    Dw, AAV 
    d) MD involving 
    (a) to (c) above 
    
    
    
    
    
    organization 
    development, 
    seminars/workshops 
    for 
    quality 
    improvement, IT solutions, public 
    relations.  To advise on all matters 
    of 
    policy 
    and 
    administration.  
    Scrutinize proposals for expansion 
    of administrative staff, Coordinate 
    activities of various units of the 
    office, decide the disciplinary action 
    to be taken against staff as per rules 
    and regulations laid down by the 
    Department of personnel and make 
    policy decisions in the matter of 
    administration.  Implement policies 
    of the Govt.    
    should be considered with appropriate 
    software,  aids& appliances as per 
    needs. 
    22. 
    Assistant Manager 
    (Finance) 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    d) MD involving 
    (a) to (c) above 
    They 
    
    
    ensure 
    
    
    proper  
    maintenance   of accounts, accounts 
    books, records of business and 
    financial establishments, private 
    institutions, Govt. or Quasi Govt. 
    offices. Supervise subordinates e.g. 
    Account 
    Clerks 
    engaged 
    in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize bills, receipts, 
    payment etc. for proper entries in 
    cash -book, journal, ledger    and 
    other records. Keep record of all 
    taxes, licenses, fees etc., required to 
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. It does not involve any 
    hazards. 
    They 
    have 
    to 
    perform 
    supervisory and leadership role. Good  
    communication is required. For field 
    work, mobility of the incumbent 
    should not be restricted.  Incumbent 
    should be considered with appropriate 
    software,  aids& appliances as per 
    needs. 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1173 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    be paid by organization in which 
    engaged and ensure that they are 
    paid in time   and kept   up-to-date.  
    Get   annual   budget prepared and 
    consolidated 
    under 
    their 
    supervision and place it before 
    'Board' or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such    as trial balance, 
    profit and loss statement or such 
    balance sheet etc., as required 
    depending upon type of industry or 
    organization in which   engaged 
    See   that   prescribed   accounting  
    procedure    is followed by offices, 
    establishments 
    and 
    institutions  
    and    account    books    are 
    properly maintained. Ensure   that  
    instructions   given   or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks 
    of 
    accounts. 
    Advise 
    appropriate authority on financial 
    matters including revenue  and  
    expenditure  such  as  procedure  
    for procurement of raw materials, 


    1174  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    machinery and other purchases  and  
    also  disposal  of  assets,  write  of 
    depreciation, award of contract etc. 
    23. 
    Assistant Finance 
    Manager 
    S, BN, MF, RW, 
    SE, C 
    a) D, HH 
    b) OA, BA, OL, 
    BL, OAL, 
    BLOA, LC, 
    Dw, AAV 
    c) MD involving 
    (a) to (b) above 
    Maintain payment records, Bill 
    passing, 
    Record 
    
    
    keeping,  
    Maintain   records   of sales   tax,  
    income   tax   etc .Payments 
    Documentation, Data feeding of 
    financial 
    transactions, 
    Budget 
    preparation, Supervisory.  
    
    Maintain  books  and  accounts  
    register, Prepare   periodic   returns,  
    Pass   bills, Work delegation to 
    juniors.  
    
    Planning and scheduling work of 
    section,   shall   deal   with   non-
    routine cases referred, keep   track 
    of    paper movement   ,   hold  
    meeting   to discuss sections work. 
    
    In case, work place is in terrains and 
    field, independent mobility with the 
    help of aids and appliances should be 
    checked.Incumbent 
    should 
    be 
    considered with appropriate software,  
    aids& appliances as per needs. 
    24. 
    Assistant General 
    Manager  
    (F & A) 
    S, ST, W, BN, MF, 
    RW, SE 
    
    a) D, HH 
    b) OA, BA, OL, 
    LC, Dw, AAV 
    c) ASD(M), SLD, 
    MI 
    e) MD involving 
    All 
    Taxation 
    matter 
    Financial 
    Analysis, Accounts 
    Should have Managerial capacity, 
    Should have functional commutation 
    skills 
    with 
    effective 
    listening 
    devices.Incumbent 
    should 
    be 
    considered with appropriatesoftware,  
    aids& appliances as per needs. 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1175 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    (a) to (c) above 
    25. 
    Officer, Corporate 
    Finance  
    S, W,  MF,  RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, LC, 
    Dw, AAV, MDy 
    d) ASD (M), MI 
    e) MD involving 
    (a) to (d) above 
    They develop and apply most 
    effective methods for collecting, 
    tabulating & interpreting data in 
    any one of wide variety of fields. 
    Determine character and volume of 
    information necessary for solution 
    of any problem and obtain or 
    devise 
    methods 
    for 
    collecting 
    necessary information. Determine 
    most 
    effective 
    techniques 
    for 
    production 
    of 
    data 
    required 
    according to nature of available 
    information and type of problem 
    under Deputy Interpret and present 
    data in the required form. May 
    write 
    reports 
    analyzing 
    and 
    evaluating conclusions on the basis 
    of variable conditions affecting 
    interpretation of validity. May 
    advise 
    and 
    consult 
    private 
    industrial concerns or government 
    agencies 
    on 
    matters 
    such 
    as 
    operating 
    efficiency, 
    marketing 
    methods 
    and 
    fiscal 
    problems. 
    The work is performed inside. The 
    work place is well lighted and 
    comfortable. The worker usually 
    works alone though some public 
    dealing is required. The Branch 
    incharge has to do field work also and 
    the in the field, may be work place is 
    hot, humid and dusty. Should have 
    normal 
    bilateral 
    hand 
    functions.Incumbent to be considered 
    with use of aids / appliances as per 
    needs. 
    
    
    
    


    1176  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    Collection, analyzing of statistical 
    data, preparation of reports, update 
    statistics etc. 
    26. 
    Corporate Finance 
    Officer 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, LC, Dw, 
    AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    Duties   assigned   by   appropriate 
    authority, 
    Informs 
    financial 
    position 
    of 
    the 
    organization, 
    responsible   for   proper  
    implementation 
    of 
    financial 
    transactions as per accounts   code/ 
    Statutes/ 
    Ordinances/ 
    rules 
    & 
    regulations. 
    Incase work place is in difficult 
    terrains 
    and 
    field 
    independent 
    mobility with the help of aids and 
    appliances 
    should 
    be 
    checked. 
    Incumbent to be considered with use 
    of aids / appliances as per needs. 
    
    
    27. 
    Assistant 
    Divisional 
    Accounts Officer  
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV, 
    MDy 
    d) MD involving 
    (a) to (c) above 
    They 
    
    
    ensure 
    
    
    proper  
    maintenance   of accounts, accounts 
    books, records of business and 
    financial establishments, private 
    institutions, Govt. or Quasi Govt. 
    offices. Supervise subordinates e.g. 
    Account 
    Clerks 
    engaged 
    in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize bills, receipts, 
    payment etc. for proper entries in 
    cash -book, journal, ledger    and 
    other records. Keep record of all 
    taxes, licenses, fees etc., required to 
    be paid by organization in which 
    engaged and ensure that they are 
    paid in time   and kept   up-to-date.  
    Get   annual   budget prepared and 
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. It does not involve any 
    hazards. 
    They 
    have 
    to 
    perform 
    supervisory 
    and 
    leadership 
    role. 
    Should have good  communication 
    skill. For field work, mobility of the 
    incumbent should not be restricted.   
    Incumbent should be considered with 
    appropriate 
    software, 
    
    aids 
    & 
    appliances as per needs. 
    28. 
    Chief Accountant 
    S, BN, MF, RW, 
    SE, C 
    a) D, HH 
    b) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV 
    c) MD involving 
    (a) to (b) above 
    29. 
    Chief Accounts 
    S, BN, MF, RW, 
    a) B, LV 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1177 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    Officer 
    SE, C 
    b) D, HH 
    c) OA, OL, BL, 
    OAL, BLOA, 
    BLA, LC, Dw, 
    AAV 
    d) MD involving 
    (a) to (c) above 
    consolidated 
    under 
    their 
    supervision and place it before 
    'Board' or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such    as trial balance, 
    profit and loss statement or such 
    balance sheet etc., as required 
    depending upon type of industry or 
    organization in which   engaged 
    See   that   prescribed   accounting  
    procedure    is followed by offices, 
    establishments 
    and 
    institutions  
    and    account    books    are 
    properly maintained. Ensure   that  
    instructions   given   or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks 
    of 
    accounts. 
    Advise 
    appropriate authority on financial 
    matters including revenue  and  
    expenditure  such  as  procedure  
    for procurement of raw materials, 
    machinery and other purchases  and  
    also  disposal  of  assets,  write  of 
    depreciation, award of contract etc. 
    30. 
    Deputy Chief 
    Accounts Officer 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, OL, BL, 
    OAL, BLOA, 
    BLA, LC, Dw, 
    AAV 
    d) MD involving 
    (a) to (c) above 
    31. 
    Assistant Chief 
    Accounts Officer 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, OL, BL, 
    OAL, BLOA, 
    BLA, LC, Dw, 
    AAV 
    d) MD involving 
    (a) to (c) above 


    1178  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    32. 
    Accounts Officer-
    II 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV, 
    MDy 
    d) MD involving 
    (a) to (c) above 
    Maintain payment records, Bill 
    passing, Record   keeping, Maintain  
    records   of sales   tax, income   tax  
    etc. Payments Documentation, Data 
    feeding of financial transactions, 
    Budget preparation, Supervisory. 
    
    Planning and scheduling work of 
    section,   shall   deal   with   non-
    routine Cases referred, keep   track 
    of    paper movement ,   hold  
    meeting   to discuss sections work. 
    In case work place is in difficult 
    terrains 
    and 
    field 
    independent 
    mobility with the help of aids and 
    appliances 
    should 
    be 
    checked..Incubents to be considred 
    with aids and assistive devices as per 
    needs. 
    
    
    33. 
    Accounts Officer-
    I 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV, 
    MDy 
    d) MD involving 
    (a) to (c) above 
    34. 
    Finance Officer 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    LC, Dw, AAV, 
    MDy 
    d) MD 
    involving(a) to 
    (c) above 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1179 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    35. 
    Officer Scale - I 
    S, ST, W,  BN, 
    RW, SE, H, C, MF 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    OAL, CP, LC, 
    Dw, AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    They ensure proper maintenance of 
    accounts, accounts books, records 
    of 
    business 
    and 
    financial 
    establishments, private institutions, 
    Govt. Or Quasi Got. Offices. 
    Supervise subordinates engaged in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize ledger and other 
    records. Keep record of all taxes, 
    licenses, fees etc. required to be 
    paid by the organization in which 
    engaged and ensure that they are 
    paid in time and kept up-to-date. 
    Get annual budget prepared and 
    consolidated 
    under 
    their 
    supervision and place it before 
    Board or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such as trial balance, 
    profit and loss statement or such 
    balance sheet etc. as required 
    depending upon type of industry or 
    organization in which engaged. See 
    that 
    prescribed 
    accounting 
    procedure is followed by offices, 
    establishments and institutions as 
    The work is mostly performed inside 
    the well-lighted rooms. They have to 
    perform supervisory and leadership 
    role. 
    During 
    discussion 
    and 
    presentation, communication skill is 
    required. For field work mobility of the 
    incumbent 
    should 
    not 
    be 
    restricted.Incumbent 
    should 
    be 
    considered with appropriate software,  
    aids& appliances as per needs. 


    1180  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    well as account books are properly 
    maintained. Ensure that instructions 
    given or objections raised are 
    carried out or rectified. Make 
    periodical and surprise checks of 
    accounts. 
    36. 
    Financial 
    &Accounts 
    Officer 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, CP, LC, 
    Dw, AAV, 
    MDy 
    d) MD involving 
    (a) to (c) above 
    To ensure   proper   maintenance  
    of 
    accounts, 
    accounts 
    books, 
    records of business and financial 
    establishments, private institutions, 
    Govt. or Quasi Govt. offices. 
    Supervise subordinates e.g. Account 
    Clerks engaged in maintenance of 
    accounts and records. Scrutinize 
    bills, receipts, payment etc. for 
    proper 
    entries 
    in 
    cash 
    -book, 
    journal, ledger    and other records. 
    Keep record of all taxes,    licenses, 
    fees  etc.,  required  to  be  paid  by  
    organization in which  engaged  and  
    ensure  that  they are  paid in time  
    and kept   up-to-date.   Get   annual  
    budget prepared and consolidated 
    under their supervision and place it 
    before 
    'Board' 
    or 
    appropriate 
    authority for consideration. Prepare 
    final accounts such    as trial  
    balance,  profit  and  loss  statement  
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. Itdoes not involve any 
    hazards. They have to play supervisory 
    and leadership role. During discussion 
    and presentation, good  communication 
    skill is required. For field work, 
    mobility of the incumbent should not 
    be 
    restricted 
    Incubents 
    to 
    be 
    considered with the use of aids and 
    assistive devices as per requirement. 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1181 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    or  such  balance sheet etc. , as 
    required depending upon type of 
    industry ororganization in which  
    engaged See   that   prescribed  
    accounting   procedure    is followed 
    by 
    offices, 
    establishments 
    and 
    institutions    and    account    books  
    are properly maintained. Ensure  
    that   instructions   given   or 
    objections raised are carried out or 
    rectified.  Make periodical and 
    surprise checks of accounts. Advise 
    appropriate authority on financial 
    matters including revenue  and  
    expenditure  such  as  procedure  for 
    procurement 
    of 
    raw 
    materials, 
    machinery and other purchases  and  
    also  disposal  of  assets,  write  of 
    depreciation, award of contract etc. 
    37. 
    Finance & 
    Accounts Officer 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, CP, LC, 
    Dw, AAV, 
    Maintain payment records, Bill 
    passing, 
    Record 
    
    
    keeping,  
    Maintain   records   of sales   tax,  
    income   tax   etc .Payments 
    Documentation, Data feeding of 
    financial 
    transactions, 
    Budget 
    
    In case work place is in difficult 
    terrains and field independent mobility 
    with the help of aids and appliances 
    should be checked. Incumbents to be 
    considered with the use of aids and 


    1182  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    MDy 
    d) MD involving 
    (a) to (c) above 
    preparation, Supervisory.  
    
    Maintain  books  and  accounts  
    register, Prepare   periodic   returns,  
    Pass   bills, Work delegation to 
    juniors.  
    
    Planning and scheduling work of 
    section,   shall   deal   with   non-
    routine Cases referred, keep   track 
    of    paper movement   ,   hold  
    meeting   to discuss sections work. 
    assistive devices. 
    38. 
    Deputy Finance 
    Officer 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, CP, LC, 
    Dw, AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    Duties   assigned   by   appropriate 
    authority, Informs financial position 
    of the organization, responsible   for  
    proper   implementation of financial 
    transactions as per accounts   code/ 
    Statutes/ 
    Ordinances/ 
    rules 
    & 
    regulations. 
    In case, work place is in difficult 
    terrains and field independent mobility 
    with the help of aids and appliances 
    should be checked. Incumbents to be 
    considered with the use of aids and 
    assistive devices. 
    39. 
    Assistant 
    AccountGeneral/A
    ssistant  
    Accountant 
    General 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    CP, LC, Dw, 
    AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    To   ensure   proper   maintenance  
    of 
    accounts, 
    accounts 
    books, 
    records of business and financial 
    establishments, private institutions, 
    Govt. or Quasi Govt. offices. 
    Supervise 
    subordinates 
    e.g. 
    Account 
    Clerks 
    engaged 
    in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize bills, receipts, 
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. It does not involve any 
    hazards. 
    They 
    have 
    to 
    perform 
    supervisory and  leadership role. 
    During discussion and presentation 
    good  communication skill is  required. 
    For field work, mobility of the 
    incumbent should not be restricted.  


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1183 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    payment etc. for proper entries in 
    cash -book, journal, ledger    and 
    other records. Keep record of all 
    taxes, licenses, fees etc., required to 
    be paid by organization in which 
    engaged and ensure that they are 
    paid in time   and kept   up-to-date.  
    Get   annual   budget prepared and 
    consolidated 
    under 
    their 
    supervision and place it before 
    'Board' or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such    as trial balance, 
    profit and loss statement or such 
    balance sheet etc., as required 
    depending upon type of industry or 
    organization in which   engaged 
    See   that   prescribed   accounting  
    procedure    is followed by offices, 
    establishments 
    and 
    institutions  
    and    account    books    are 
    properly maintained. Ensure   that  
    instructions   given   or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks 
    of 
    accounts. 
    Advise 
    Incumbent should be considered with 
    appropriate 
    software, 
    
    aids& 
    appliances as per needs. 


    1184  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    appropriate authority on financial 
    matters including revenue  and  
    expenditure  such  as  procedure  
    for procurement of raw materials, 
    machinery and other purchases  and  
    also  disposal  of  assets,  write  of 
    depreciation, award of contract etc. 
    40. 
    Assistant Finance 
    Officer 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, CP, LC, 
    Dw, AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    Duties   assigned   by   appropriate 
    authority, Informs financial position 
    of the organization, responsible   for  
    proper   implementation of financial 
    transactions as per accounts   code/ 
    Statutes/ 
    Ordinances/ 
    rules 
    & 
    regulations. 
    In case work place is in difficult 
    terrains and field independent mobility 
    with the help of aids and appliances 
    should be checked.Incumbent should 
    be 
    considered 
    with 
    appropriate 
    software,  aids& appliances as per 
    needs. 
    41. 
    Section Officer 
    (Accounts & 
    Audit) 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, CP, LC, 
    Dw, AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    42. 
    Selection Grade  
    in JAG 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    CP, LC, Dw, 
    AAV, MDy 
    Maintain payment records, Bill 
    passing, Record   keeping, Maintain  
    records   of sales   tax, income   tax  
    etc. Payments Documentation, Data 
    feeding of financial transactions, 
    Budget preparation, Supervisory.  
    
    
    In case work place is in difficult 
    terrains 
    and 
    field, 
    independent 
    mobility with the help of aids and 
    appliances 
    should 
    be 
    checked.Incumbent 
    should 
    be 
    considered with appropriate software,  


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1185 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    d) MD involving 
    (a) to (c) above 
    aids& appliances as per needs. 
    43. 
    Senior 
    Administrative 
    Grade 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    CP, LC, Dw, 
    AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    They 
    
    
    ensure 
    
    
    proper  
    maintenance   of accounts, accounts 
    books, records of business and 
    financial establishments, private 
    institutions, Govt. or Quasi Govt. 
    offices. Supervise subordinates e.g. 
    Account 
    Clerks 
    engaged 
    in 
    maintenance 
    of 
    accounts 
    and 
    records. Scrutinize bills, receipts, 
    payment etc. for proper entries in 
    cash -book, journal, ledger    and 
    other records. Keeps record of all 
    taxes, licenses, fees etc., required to 
    be paid by organization in which 
    engaged and ensure that they are 
    paid in time   and kept   up-to-date.  
    Get   annual   budget prepared and 
    consolidated 
    under 
    their 
    supervision and place it before 
    'Board' or appropriate authority for 
    consideration. 
    Prepare 
    final 
    accounts such    as trial balance, 
    profit and loss statement or such 
    The work is mostly performed inside 
    in well lighted rooms. Worker usually 
    works alone. It does not involve any 
    hazards. 
    They 
    have 
    to 
    perform 
    supervisory 
    and 
    leadership 
    role. 
    During discussion and presentation, 
    good  communication skill  is required. 
    For field work, mobility of the 
    incumbent should not be restricted.  
    Incumbent should be considered with 
    appropriate software,  aids&appliances 
    as per needs. 


    1186  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    balance sheet etc., as required 
    depending upon type of industry or 
    organization in which   engaged 
    See   that   prescribed   accounting  
    procedure    is followed by offices, 
    establishments 
    and 
    institutions  
    and    account    books    are 
    properly maintained. Ensure   that  
    instructions   given   or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks 
    of 
    accounts. 
    Advise 
    appropriate authority on financial 
    matters including revenue  and  
    expenditure  such  as  procedure  
    for procurement of raw materials, 
    machinery and other purchases  and  
    also  disposal  of  assets,  write  of 
    depreciation, award of contract etc. 
    44. 
    Senior Time Scale 
    S, BN, MF, RW, 
    SE, C 
    a) LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    CP, LC, Dw, 
    AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    Maintain payment records, Bill 
    passing, Record   keeping, Maintain  
    records   of sales   tax, income   tax  
    etc. Payments Documentation, Data 
    feeding of financial transactions, 
    Budget preparation, Supervisory.  
    
    
    In case work place is in difficult 
    terrains 
    and 
    field 
    independent 
    mobility with the help of aids and 
    appliances 
    should 
    be 
    cheked.Incumbent 
    should 
    be 
    considered with appropriate software,  
    aids& appliances as per needs. 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1187 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    45. 
    
    Executive  
    (Finance 
    /Account) 
    
    
    S, ST, W, BN, 
    RW, SE,  H, C, 
    MF 
    a) LV 
    b) D, HH 
    c) OA, BA, OL, 
    OAL, CP, LC, 
    Dw, AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    They ensure proper maintenance of 
    accounts, accounts books, records 
    of 
    business 
    and 
    financial 
    establishments, private institutions, 
    Govt. or Quasi Govt. offices.  
    Supervise subordinates engaged in 
    maintenance 
    of 
    accounts 
    and 
    records.  Scrutinize ledger and 
    other records.  Keep record of all 
    taxes, licenses, fees etc.  Required 
    to be paid by the organization in 
    which engaged and ensure that they 
    are paid in time and kept up-to-
    date.  Get annual budget prepared 
    and 
    consolidated 
    under 
    their 
    supervision and place it before 
    Board or appropriate authority for 
    consideration. 
    
    Prepare 
    final 
    accounts such as trial balance, 
    profit and loss statement or such 
    balance sheet etc. as required 
    depending upon type of industry or 
    organization in which engaged.  
    See that prescribed accounting 
    procedure is followed by offices, 
    establishments and institutions as 
    In case work place is in difficult 
    terrains and field independent mobility 
    with the help of aids and appliances 
    should be checked. Incumbent should 
    be 
    considered 
    with 
    appropriate 
    software,  aids& appliances as per 
    needs. 


    1188  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    well as account books are properly 
    maintained. 
    
    Ensure 
    that 
    instructions given or objections 
    raised are carried out or rectified.  
    Make 
    periodical 
    and 
    surprise 
    checks of accounts.   
    46. 
    Junior Executive 
    (Finance) 
    S, ST, W, BN, 
    RW, SE, H, C, MF 
    a) B, LV  
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, CP, 
    LC, Dw, AAV, 
    MDy 
    d) MD involving 
    (a) to (c) above 
    
    Controlling 
    &supervising 
    cash 
    section,scrutiny of files relating to 
    purchase/amounts 
    spent 
    by 
    Administration Department  
    Works Contract Tax, Deposit of 
    Work 
    Contract 
    Tax, 
    thereafter 
    issuance 
    of 
    Form-IX 
    TDS 
    certificate to firms and submission 
    of same to Sales Tax Department. 
    Salary and payroll bills, of Head 
    Office and Zonal Offices. TA Bills, 
    Medical Bills, LTC Bills Leave 
    Encashment  
    Monthly 
    Expenditure 
    Bills 
    /Statements of ZO. Submission of 
    Monthly 
    parameters 
    related 
    to 
    MOU to the Coordination Wing. 
    Advance to staff. Work relating to 
    placement of surplus funds with 
    banks. Finalization of PF returns 
    &Issuance 
    related 
    returns, 
    monthly/Annual as per the statutory 
    The work is mostly performed inside 
    in well lighted rooms. The worker 
    usually does his work alone. It does 
    not involve any hazard.   
    Incumbent should be considered with 
    appropriate 
    software, 
    
    aids& 
    appliances as per needs. 


    [भाग I — खण्‍ड 1] 
    भारत‍का‍राजपत्र‍:‍असाधारण  
    1189 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    
    
    requirements. 
    Preparation 
    of 
    schedules &Sub-schedules at the 
    time of closing of accounts, there 
    after preparation of Draft Balance 
    Sheet. 
    Attending 
    to 
    queries/ 
    suggestions 
    /observations 
    of 
    Statutory Auditors/CAG Auditors 
    and preparation of final Balance 
    Sheet. Participation of   various 
    Committee 
    formed 
    in 
    the 
    Corporation. Calculation of Income 
    Tax for the staff. Maintaining of 
    Records of Income Tax as per 
    requirement of revised rules of IT 
    act. Filing of Form 16 and Form 12 
    BA for staff. Issuance of Annual 
    Returns in Form no.26K and 26Cfor 
    contractors. 
    Filing 
    the 
    Annual 
    Returns in Form 24.Issuance of 
    Form 
    16A 
    for 
    contractors.Finalization 
    of 
    PF 
    returns &Issuance related returns 
    Monthly/Annual as per the statutory 
    requirements. 
    47. 
    Junior 
    S, BN, MF, RW, 
    a) B, LV 
    Maintain payment records, bill  


    1190  
    THE GAZETTE OF INDIA : EXTRAORDINARY 
    [PART I—SEC. 1] 
    
    
    
    FUNCTIONAL REQUIREMENT ABBREVIATIONS USED: S=Sitting, ST=Standing, W=Walking, BN=Bending , L=Lifting, KC=Kneeling &Crouching, JU=Jumping, 
    CRL= Crawling, CL=Climbing, PP=Pulling & Pushing, MF=Manipulation with Fingers, RW=Reading & Writing, SE=Seeing, H=Hearing, C=Communication, 
    CATEGORY ABBREVIATIONS USED:  B=Blind, LV=Low Vision, D=Deaf, HH= Hard of Hearing, OA=One Arm, OL=One Leg, BA=Both Arms, BL=Both Leg, 
    OAL=One Arm and One Leg, BLOA=Both Leg & One Arm , BLA=Both Legs Arms, CP=Cerebral Palsy, LC=Leprosy Cured, Dw=Dwarfism, AAV=Acid Attack 
    Victims, MDy= Muscular Dystrophy, ASD= Autism Spectrum Disorder (M= Mild, MoD= Moderate), ID= Intellectual Disability, SLD= Specific Learning Disability,        
    MI= Mental Illness, MD=Multiple Disabilities 
    Administrative 
    Grade 
    SE, C 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    CP, LC, Dw, 
    AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    passing, record   keeping, maintain  
    records   of sales   tax, income   tax  
    etc. payments documentation, data 
    feeding of financial transactions, 
    budget 
    preparation, 
    supervisory 
    work. 
    
    In case, work place is in difficult 
    terrains 
    and 
    field 
    independent 
    mobility with the help of aids and 
    appliances 
    should 
    be 
    checked.Incumbent 
    should 
    be 
    considered with appropriate software,  
    aids& appliances as per needs. 
    48. 
    Junior Time Scale 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    CP, LC, Dw, 
    AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    49. 
    Management 
    Trainee 
    (Accounts) 
    S, BN, MF, RW, 
    SE, C 
    a) B, LV 
    b) D, HH 
    c) OA, BA, OL, 
    BL, OAL, 
    BLOA, BLA, 
    CP, LC, Dw, 
    AAV, MDy 
    d) MD involving 
    (a) to (c) above 
    
    2. ADMINISTRATIVE OFFICER (SECRETARIAL) 
    50. 
    Secretary 
    S, ST, W, RW, SE, 
    a) B, LV 
    Administrating 
    the 
    institutions, The work is mostly performed inside 




    """

        # question="list all the  designations are under  ADMINISTRATIVE OFFICER (SECRETARIAL) "
    question="what is the Working Condition for Junior Administrative Grade also provide the page number were you picked this info"

    content=fitz_content_without_header
    ask_gemini(content=content,question=question)