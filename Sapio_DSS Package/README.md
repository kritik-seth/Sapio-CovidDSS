# Sapio_DSS

Some of the projects I did at Sapio Analytics for their Covid-19 Decision Support System as an intern

### gsheet_data.py
This module allows any person who has valid credentials to get data from Sapio Google Sheets:
#### Procedure:
1. Fetches URLs of other sheets (stored the in master sheet)
2. Updates the URLs of sheets on the basis of sheet readiness and Region
3. Extracts data from one URL on the basis of Region mentioned by the user
4. Cleans the data and returns it as type DataFrame

### transform.py
This module allows any person to transform the data into the required format
#### Functions:
1. gdp1- Warangal
2. gdp2- MCGM, Daman Diu DNH, PCMC, Pune Master, Joodhpur, Agra, Bhopal, Chennai, Port Blair, Surat, Kanpur, Aurangabad, Amritsar, Sangli.

### Author- Kritik Seth