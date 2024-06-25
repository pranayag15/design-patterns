from abc import ABC, abstractmethod


class NotifyAlertObserver(ABC):

    @abstractmethod
    def update(self):
        pass


class StockObservable(ABC):
    @abstractmethod
    def add_observer(self, observer: NotifyAlertObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: NotifyAlertObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass
