import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import operator
from datetime import date


def main():

    # List of companies
    companiesUS = ["JPM", "MSFT", "GOOGL", "BAC", "TSLA", "FB", "V", "MA", "DIS", "QCOM", "AAPL", "SGEN", "NVDA"]
    report_US = createDebtReport(companiesUS, "US")
    companiesIND = ["DABUR.NS", "GLAXO.NS", "HDFCBANK.NS", "HINDUNILVR.NS", "INFY.NS", "RELIANCE.NS", "TATACOFFEE.NS", "TCS.NS", "TECHM.NS", "WIPRO.NS", "YESBANK.NS"]
    report_IN = createDebtReport(companiesIND, "IN")

def createDebtReport(companies, region):
    # Create workbook
    workbook = Workbook()
    sheet = workbook.active
    
    # Add headers
    sheet["A1"] = "COMPANY"
    sheet["B1"] = "Total Cash"
    sheet["C1"] = "Total Debt"
    sheet["D1"] = "Ratio"

    data = []
    
    for company in companies:
        cash = getTotalCash(company)
        debt = getTotalDebt(company)
        ratio = calculateRatio(cash, debt)
        data.append([company,cash,debt,ratio])
    
    print(data)
    # Sort the data based on ratio
    sortedData = sorted(data, key=lambda x: x[3], reverse=True)
        
    # Add data to xlsx
    for row in sortedData:
        sheet.append(row)
    reportName = "Reports/DebtRatioReport_"+region+"_"+str(date.today())+".xlsx"
    workbook.save(filename=reportName)    
    
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

# Calculate the Ratio
def calculateRatio(cash, debt):
    if cash[-1] == debt[-1]:
        cash = float(cash[0:-1])
        debt = float(debt[0:-1])
        return cash/debt
    elif ( ((cash[-1] == "B") and (debt[-1] == "M")) or ((cash[-1] == "T") and (debt[-1] == "B")) ):
        cash = float(cash[0:-1])
        debt = float(debt[0:-1])*0.001
        return cash/debt
    else:
        return 0.0

if __name__=='__main__':
    main()