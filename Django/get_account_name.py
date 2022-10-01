import json

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import JsonResponse

#for consuming api
import requests
from requests.structures import CaseInsensitiveDict

#code stands for bank code. For example, GT Bank code is 058.
#accountno bank account number
def getaccountname(request, accountno, code):
    paystackSecret = 'Paystack Publick Secret API Key'
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer "+paystackSecret
    url = "https://api.paystack.co/bank/resolve?account_number="+accountno+"&bank_code="+code+""
    res = requests.get(url, headers=headers)
    res = res.json()
    res = json.dumps(res)
    paystack_resp = json.loads(res)
    #return JsonResponse(monnify_resp)
    response = paystack_resp.get('status')
    if response != True:
        status = 0
        account_name = ''
    else:
        status = 1
        account_name = paystack_resp.get('data')['account_name'] #Gets account name
    response = {'msg': account_name, 'status': status}
    return JsonResponse(response)
