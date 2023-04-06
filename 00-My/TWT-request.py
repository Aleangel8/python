from bs4 import BeautifulSoup
import requests




# TUTORIAL 1 ***********************************************************
url = "https://www.amazon.es/Cecotec-InoxBlack-Accesorios-Diet%C3%A9tica-Accesorios/dp/B0BFB5HJCT/ref=zg-bs_kitchen_sccl_3/259-2523958-2017837?pd_rd_w=2xgev&content-id=amzn1.sym.268753cc-a452-4306-a165-5b560a4eaba2&pf_rd_p=268753cc-a452-4306-a165-5b560a4eaba2&pf_rd_r=1GTN6GC947ADEHDKWFWK&pd_rd_wg=wODuY&pd_rd_r=65e1d406-845b-4980-b13d-7ce3ec2cbb35&pd_rd_i=B0BFB5HJCT&th=1"

result = requests.get(url)

print(result.status_code, result.reason,sep="-")

doc = BeautifulSoup(result.text, "html.parser")
print("************************")

prices = doc.find_all(string = "Caliente")

print(prices)

#print(doc.prettify())
