from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from parspal_client import ws_proxy
from django.conf import settings
from payment.models import Transaction, TransactionResult


class StartView(View):
    def get(self, request):
        pass

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        transaction = Transaction()
        transaction.amount = amount
        transaction.email = email
        transaction.name = name
        transaction.save()

        request_result = ws_proxy.request_payment(settings.MERCHANT_ID, settings.MERCHANT_PASSWORD, amount,
                                                  '1Hes Donation', name,
                                                  '09121231231', email, transaction.id,
                                                  settings.SERVER_BASE_ADDRESS + '/payment/result/' + str(transaction.id))
        if request_result.ResultStatus == 'Succeed':
            return HttpResponseRedirect(request_result.PaymentPath)


class ResultView(View):
    @csrf_exempt
    def post(self, request, transaction_id):
        transaction = Transaction.objects.get(id=int(transaction_id))
        status = request.POST.get('status')
        resnumber = request.POST.get('resnumber')
        refnumber = request.POST.get('refnumber')

        if str(resnumber) != str(transaction_id):
            raise Exception("resnumber and transaction_id are not equal. resnumber:%s , trasaction_id:%s" % (resnumber, transaction_id))

        transaction_result = TransactionResult()
        transaction_result.refnumber = refnumber
        transaction_result.resnumber = resnumber
        transaction_result.status = status
        transaction_result.transaction_id = transaction_id
        transaction_result.save()

        result = ws_proxy.verify_payment(settings.MERCHANT_ID, settings.MERCHANT_PASSWORD, transaction.amount, refnumber)
        transaction_result.status = result.ResultStatus
        paymented_price = result.PayementedPrice
        transaction_result.save()

        if int(paymented_price) != transaction.amount:
            raise Exception("Paymented amount is not equal with transaction amount")
        print result
        return HttpResponse(result)
