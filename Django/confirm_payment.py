import json

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import JsonResponse

#for consuming api
import requests
from requests.structures import CaseInsensitiveDict

'''login required'''
#from django.contrib.auth.decorators import login_required

#@login_required(login_url='/login')
def verifytrans(request, transactionId):
    paystackSecret = 'Your Paystack Secret Key'
    headers = CaseInsensitiveDict()
    #headers["Content-Type"] = "application/json"
    headers["Authorization"] = "Bearer " + paystackSecret
    url = 'https://api.paystack.co/transaction/verify/:'+transactionId
    res = requests.get(url, headers=headers)
    res = res.json()
    res = json.dumps(res)
    paystack_resp = json.loads(res)
    response = paystack_resp.get('status')
    if response == True:
        #Its successful
        response = {'msg': 'Successful', 'status': 1}        
    else:
        #It failed
        response = {'msg': 'Failed', 'status': 0}
    return JsonResponse(response)
