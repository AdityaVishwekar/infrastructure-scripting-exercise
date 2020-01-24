import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


def main():
    # Create workbook
    workbook = Workbook()
    sheet = workbook.active
    
    # Add headers
    sheet["A1"] = "COMPANY"
    sheet["B1"] = "Total Cash"
    sheet["C1"] = "Total Debt"
    sheet["D1"] = "Ratio"

    # List of companies
    companies = ["JPM", "MSFT", "GOOGL"]
    data = []
    
    for company in companies:
        cash = getTotalCash(company)
        debt = getTotalDebt(company)
        data.append([company,cash,debt])
        
    # Add data to xlsx
    for row in data:
        sheet.append(row)
    workbook.save(filename="Reports/test.xlsx")

# Get url
def setPage(stock):
    URL = "https://finance.yahoo.com/quote/"+stock+"/key-statistics?p="+stock
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

# Total cash of the company
def getTotalCash(stock):
    soup = setPage(stock)
    results = soup.find_all('td', class_='Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)')
    return results[51].text

# Total debt of the company
def getTotalDebt(stock):
    soup = setPage(stock)
    results = soup.find_all('td', class_='Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)')
    return results[53].text

if __name__=='__main__':
    main()