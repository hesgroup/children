__author__ = 'SOROOSH'

from suds.client import Client

parspal_wsdl = 'http://merchant.parspal.com/WebService.asmx?wsdl'

__client__ = Client(parspal_wsdl)

print __client__


def request_payment(merchant_id, password, price=None, desc=None, payer=None, mobile=None, email=None, res_number=None,
                    return_path=None):
    return __client__.service.RequestPayment(merchant_id, password, price, desc, payer, email, mobile, res_number,
                                             return_path)


def verify_payment(merchant_id, password, price, refnum):
    return __client__.service.VerifyPayment(merchant_id, password, price, refnum)


if __name__ == '__main__':
    result = request_payment('1864704', 'TMewkyrp0', 11111, 'desc', 'soroosh', '09122502092',
                             'soroosh.sarabadani@gmail.com', '1', '/')
    print result.PaymentPath