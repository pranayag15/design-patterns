from .interfaces import NotifyAlertObserver, StockObservable


class EmailNotifier(NotifyAlertObserver):

    def __init__(self, email: str, observable: StockObservable) -> None:
        self.email = email
        self.stockObservable: observable

    def update(self):
        self.sendEmail()

    def sendEmail(self):
        print("Email sent to: ", self.email)


class SmsNotifier(NotifyAlertObserver):

    def __init__(self, email: str, observable: StockObservable) -> None:
        self.email = email
        self.stockObservable: observable

    def update(self):
        self.sendSms()

    def sendSms(self):
        print("SMS sent to: ", self.email)
