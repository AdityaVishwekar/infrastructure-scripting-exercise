import requests
from bs4 import BeautifulSoup


def main():
    companies = ["JPM", "MSFT"]
    print("Company Cash Debt")
    for company in companies:
        cash = getTotalCash(company)
        debt = getTotalDebt(company)
        print(company+" "+cash+" "+debt)

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

def getTotalDebt(stock):
    soup = setPage(stock)
    results = soup.find_all('td', class_='Fz(s) Fw(500) Ta(end) Pstart(10px) Miw(60px)')
    return results[53].text

if __name__=='__main__':
    main()