from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from parspal_client import ws_proxy
from django.conf import settings


class StartView(View):
    def get(self, requesr):
        pass

    def post(self, request, name, email, amount):
        request_result = ws_proxy.request_payment(settings.MERCHANT_ID, settings.MERCHANT_PASSWORD, amount,
                                                  '1Hes Donation', name,
                                                  '09121231231', email, 1,
                                                  settings.SERVER_BASE_ADDRESS + '/payment/result/1')
        if request_result.ResultStatus == 'Succeed':
            return HttpResponseRedirect(request_result.PaymentPath)