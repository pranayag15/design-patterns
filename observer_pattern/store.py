# https://youtu.be/Ep9_Zcgst3U?si=dpEqJfVRMvvrIHeG

from .observable import StockObservable, IphoneObservable
from .observer import NotifyAlertObserver, EmailNotifier, SmsNotifier


iphoneObservable: StockObservable = IphoneObservable()

observer1: NotifyAlertObserver = EmailNotifier("abc@gmail.com", iphoneObservable)
observer2: NotifyAlertObserver = EmailNotifier("xyz@gmail.com", iphoneObservable)
observer3: NotifyAlertObserver = SmsNotifier("+91-9123454321", iphoneObservable)

iphoneObservable.add_observer(observer1)
iphoneObservable.add_observer(observer2)
iphoneObservable.add_observer(observer3)

iphoneObservable.set_state(10)
iphoneObservable.set_state(0)
iphoneObservable.set_state(50)
