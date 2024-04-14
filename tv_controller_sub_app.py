class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self._current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self._current_channel()

    def turn_channel(self, n):
        self.current_channel_index = n - 1 if 1 <= n <= len(self.channels) else 0
        return self._current_channel()

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self._current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self._current_channel()

    def current_channel(self):
        return self._current_channel()

    def is_exist(self, query):
        return "Yes" if query in self.channels else "No"

    def _current_channel(self):
        return self.channels[self.current_channel_index]


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
