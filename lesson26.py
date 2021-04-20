import re

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')

print(phoneRegex)

resume = '''Mildred Kolenda, Loan Processor

mildred.q.kolenda@gmail.com

256-809-1093

 

Professional Summary
 

Accurate and efficient Loan Processor with 3+ years of experience. Skilled at evaluating financial documents and client interaction. Seeking to increase efficiency and accuracy at Stadrand Mortgage Loans. At Gauge Home Loans, used Calyx Point to process 15 loans per week with 99.9% accuracy. Commended 11x by loan officer for attention to detail.

 

Work Experience
 

Loan Processor

Gauge Home Loans, 615-657-2033

Feb 2017–May 2019

Used Calyx Point mortgage loan software to process 15 loans a week with 99.9% accuracy.
Gathered and analyzed financial data from 1,800 clients.
Commended 11x by loan officer for strict attention to detail.
Found a major inaccuracy that saved the bank from agreeing to a $3.5M bad loan.
 

Loan Processor

Zack Robbins Financial, 213-456-7890

Feb 2016–Feb 2017

Raised rate of identifying inconsistencies in loan applications and financial documents by 23%.
Worked directly with 5 clients per week to provide financial guidance and customer service.
 

Education
 

2012–2016 University of North Alabama

BS in Business Administration

Excelled in banking and finance coursework.
Conducted senior project that used MS Excel to analyze 200+ financial documents.
 

Skills
Technical Skills: Processing loans, gathering client data, Calyx Point
Soft Skills: Interpersonal skills, collaboration, active listening, problem solving
 

Activities
 

Worked with Huntston County Animal Shelter to secure $55,000 loan for new cat building.
Run in annual marathons for fun and fitness.'''

mo = phoneRegex.findall(resume)
# the findall() method stores all matches in a list
# unless there are one or more groups present
# findall() will store multiple groupped patterns in Tuples

print(mo)