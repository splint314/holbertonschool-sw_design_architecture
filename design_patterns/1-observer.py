#!/usr/bin/env python3

"""Observer pattern implementation with topic filtering."""


class NewsSubject:
    """Subject that notifies observers."""

    def __init__(self):
        self._observers = []

    def subscribe(self, observer, topics=None):
        """Subscribe an observer with optional topic filtering."""
        self._observers.append((observer, topics))

    def unsubscribe(self, observer):
        """Unsubscribe an observer."""
        self._observers = [
            (obs, topics) for obs, topics in self._observers if obs != observer
        ]

    def notify(self, topic, data):
        """Notify observers of a new event."""
        for observer, topics in list(self._observers):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
    subject = NewsSubject()

    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)  # tous les topics

    subject.subscribe(sms, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
