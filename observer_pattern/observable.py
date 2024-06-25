from .interfaces import StockObservable, NotifyAlertObserver


class IphoneObservable(StockObservable):
    def __init__(self):
        self.observers = []
        self.stock = 0

    def add_observer(self, observer: NotifyAlertObserver):
        self.observers.append(observer)

    def remove_observer(self, observer: NotifyAlertObserver):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update()

    def get_state(self):
        return self.stock

    def set_state(self, state):
        if self.stock == 0:
            self.notify_observers()
        self.stock = state
