from abc import ABC, abstractmethod


class Watcher(ABC):
    @abstractmethod
    def update(self, status):
        pass


class Order:
    def __init__(self):
        self._status = "Placed"
        self._watchers = []

    def add_watcher(self, watcher):
        self._watchers.append(watcher)

    def remove_watcher(self, watcher):
        self._watchers.remove(watcher)

    def set_status(self, status):
        self._status = status
        print(f"Order is now: {status}")
        for watcher in list(self._watchers):
            watcher.update(status)
        print()


class CustomerSMS(Watcher):
    def __init__(self, name):
        self.name = name

    def update(self, status):
        print(f"  SMS to {self.name}: your order is now {status}")


class KitchenScreen(Watcher):
    def update(self, status):
        print(f"  Kitchen screen: {status}")


if __name__ == "__main__":
    order = Order()
    sms = CustomerSMS("Rahim")
    kitchen = KitchenScreen()

    order.add_watcher(sms)
    order.add_watcher(kitchen)

    order.set_status("Cooking")
    order.set_status("Out for delivery")

    order.remove_watcher(kitchen)
    order.set_status("Delivered")