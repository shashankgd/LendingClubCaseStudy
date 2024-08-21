# Project Name: Lending Club Case Study
> The project is a data science project that uses the lending club data set to predict whether a loan will be defaulted or not.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Conclusions](#conclusions)
* [Acknowledgements](#acknowledgements)

<!-- You can include any other section that is pertinent to your problem -->

## General Information
- Project Background:
  This company is the largest online loan marketplace, facilitating personal loans, business loans, and financing of   
  medical procedures.
  Borrowers can easily access lower interest rate loans through a fast online interface.
  
- Business Problem: 
   Like most other lending companies, lending loans to ‘risky’ applicants is the largest source of financial loss   
   (called credit loss). Credit loss is the amount of money lost by the lender when the borrower refuses to pay or runs 
   away with the money owed. In other words, borrowers who default cause the largest amount of loss to the lenders. In 
   this case, the customers labelled as 'charged-off' are the 'defaulters'.

-  Target: 
   If one is able to identify these risky loan applicants, then such loans can be reduced thereby cutting down the 
   amount of credit loss. Identification of such applicants using EDA is the aim of this case study.

- Datset: 
  Dataset contains loan data for all loans issued through the time period 2007 t0 2011.

## Conclusions
### Recommendations

#### Major Driving factor which can be used to predict the chance of defaulting and avoiding Credit Loss:
- DTI
- Grades
- Verification Status
- Annual income
- Pub_rec_bankruptcies
#### Other considerations for 'defaults' :
- Burrowers not from large urban cities like california, new york, texas, florida etc.
- Burrowers having annual income in the range 50000-100000.
- Burrowers having Public Recorded Bankruptcy.
- Burrowers with least grades like E,F,G which indicates high risk.
- Burrowers with very high Debt to Income value.
- Burrowers with working experience 10+ years.

To incorporate the findings into decision-making using specific numbers or ranges, you can set thresholds and ranges based on the statistical analysis we’ve conducted. Here’s how you can proceed:

1. Income-Based Loan Approval Criteria

Income Segment Thresholds

	•	Low Income Segment: Borrowers with annual income below approximately $40,404 (25th percentile, from the earlier annual_inc.describe() output) fall into the Low income segment.
	•	Decision Criteria:
	•	Loan Amount: Limit the loan amount for borrowers in the Low income segment to a maximum of $10,000. This cap reduces exposure to risk.
	•	Interest Rate: Apply a higher interest rate, e.g., 2% above the average rate, for borrowers in this segment to compensate for the higher risk.
	•	Loan Term: Offer only 36-month terms to borrowers in this segment. Discourage or disallow 60-month terms due to their higher default rates.
	•	Very High Income Segment: Borrowers with annual income above approximately $82,300 (75th percentile) fall into the Very High income segment.
	•	Decision Criteria:
	•	Loan Amount: Allow higher loan amounts, up to the maximum loan amount available ($35,000).
	•	Interest Rate: Offer a lower interest rate, e.g., 1% below the average rate, to encourage borrowing from lower-risk borrowers.
	•	Loan Term: Allow flexibility in choosing between 36 and 60 months, with possibly better terms (e.g., lower fees or rates) for 36-month loans.

2. Loan Term Criteria

Term-Based Adjustments

	•	60-Month Term:
	•	Income Requirement: Require a minimum annual income of $60,000 for approval of a 60-month loan term. This threshold is set above the median income to ensure that longer-term loans are extended only to more financially stable borrowers.
	•	Interest Rate Adjustment: For 60-month loans, add an additional 0.5% to 1% on the interest rate compared to 36-month loans to account for the higher risk of default.
	•	36-Month Term:
	•	Income Flexibility: Offer loans to borrowers with incomes as low as $40,000 but apply stricter limits on the loan amount and interest rate if the income is below $50,000.
	•	Interest Rate: Offer standard interest rates or potentially lower rates to encourage shorter-term borrowing.

3. Purpose-Based Adjustments

High-Risk Loan Purposes

	•	Small Business Loans:
	•	Default Rate: With a default rate of approximately 25.9%, impose stringent requirements:
	•	Minimum Income: Require a minimum income of $75,000.
	•	Collateral: Demand collateral or a co-signer to mitigate risk.
	•	Loan Amount: Cap the loan amount at $15,000 for small business purposes.
	•	Other High-Risk Purposes (e.g., Educational, Medical):
	•	Minimum Income: Set a minimum income threshold of $50,000.
	•	Interest Rate: Apply a risk premium of 1.5% to 2% above the standard rate.
	•	Loan Term: Limit the term to 36 months unless the borrower has an income exceeding $80,000, in which case a 60-month term might be considered.

Low-Risk Loan Purposes

	•	Credit Card Consolidation:
	•	Default Rate: With a lower default rate (~10.6%), offer favorable terms:
	•	Interest Rate: Provide competitive rates, potentially below the average, to encourage consolidation.
	•	Loan Amount: Allow up to $35,000, especially if the borrower’s income is above $60,000.
	•	Major Purchases/Weddings:
	•	Terms: Offer standard or slightly favorable terms, with interest rates 0.5% below average for those in the High or Very High income segments.

4. Revolving Credit Utilization

Utilization-Based Risk Adjustment

	•	High Utilization (Above 50%):
	•	Interest Rate: Increase the interest rate by 1% for borrowers with credit utilization above 50%.
	•	Loan Amount: Reduce the maximum loan amount available by 20% to 30% for high utilization borrowers.
	•	Credit Monitoring: Implement more frequent monitoring of borrowers’ credit utilization if they are approved for a loan.
	•	Low Utilization (Below 30%):
	•	Incentives: Offer better terms, such as reduced interest rates (0.5% to 1% below average) or higher loan amounts (up to $35,000), for borrowers with lower utilization rates.

5. Implementation and Monitoring

   •	Regular Reviews: Conduct quarterly reviews of loan performance data to assess whether these criteria effectively reduce default rates. Adjust thresholds and rates as necessary.


## Technologies Used
- python - version 3.12.4
- matplotlib - version 3.9.2
- numpy - version 2.0.1
- openpyxl - version 3.1.5
- pandas - version 2.2.2
- scipy - version 1.14.0
- seaborn - version 0.13.2


## Acknowledgements
- This project was inspired by UpGrad IITB Programme as a case study for the Machine Learning and Artificial Intelligence course.


## Contact
- Created by [@shashankgd] - feel free to contact me!
- Co-Authored by [@rdas15]

## License
- This project is open source and available without restrictions.
