from waybackpy import WaybackMachineCDXServerAPI
import requests







def waybackurl(url,year):


    
    user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    cdx_api = WaybackMachineCDXServerAPI(url, user_agent)




    near = cdx_api.near(year)

    result={}
    oldurl=near.archive_url
    res=requests.get(oldurl)

    result['url']=url
    result['waybackmachineLink']=oldurl
    result['rawHtml']=res.text
    result['waybackTime']=near.timestamp
    return result






if __name__=='__main__':

    oldurl=waybackurl('rel8ed.to','2021')
