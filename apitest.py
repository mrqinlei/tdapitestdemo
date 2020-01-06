import requests
import json
class RunMain:
    def send_post(self,url,data):
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res

    def send_get(self,url,params):
        result = requests.get(url=url,params=params).json()
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res

    def run_main(self,method,url=None,data=None):
        result = None
        if method == 'post':
            result = self.send_post(url,data)
        elif method == 'get':
            result = self.send_get(url,data)
        else:
            print("错误")
        return result

if __name__=='__main__':
    url = "http://106.75.9.19:88/active/get_info"
    data = {"pid":"1"}
    run = RunMain()
    res = run.run_main("get",url,data)
    print(type(res))
    print(res)