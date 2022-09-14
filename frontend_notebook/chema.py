import urllib.request, json
import requests
news_url = 'https://www.db.com/api/content/limit/100/offset/30/render/false/type/json/query/%20+((categories:adHocRelease%20categories:event1%20categories:mediaRelease%20categories:news%20categories:research)%20&&%20(categories:africa%20categories:americas1%20categories:asiapacific%20categories:europeexGermany%20categories:germany%20categories:middleEast%20categories:art%20categories:assetManagement%20categories:awards%20categories:capitalMarkets%20categories:careers%20categories:company1%20categories:corporateCitizenship%20categories:corporateProducts%20categories:cryptocurrencies%20categories:culture%20categories:digitalBankingServices%20categories:digitalisation%20categories:diversity%20categories:education%20categories:employeeEngagement%20categories:entrepreneurship%20categories:financialResults%20categories:history%20categories:investmentBanking%20categories:managementLeadership%20categories:personnelAnnouncements%20categories:privateProducts%20categories:research3%20categories:sports%20categories:strategy%20categories:sustainability%20categories:wealth))%20%20+conhost:8e29bc28-e0f6-40f1-930a-6258631a0985%20+languageId:1%20+deleted:false%20/orderby/C03News.publishDate%20desc'
backend_api='https://gee16-22-team12.ew.r.appspot.com/api/text'
with urllib.request.urlopen(news_url) as url:
   data = json.load(url)
for news in data['contentlets']:
    print(requests.post(backend_api, data={'text':news['headline']}))
