class HeavyAccessRestrictionError(Exception):
    def __init__(self, message='Request to MAL denied due to heavy site access.'):
        self.message = message
        super().__init__(self.message)


class MALScrapingError(Exception):
    def __init__(self, message='There was an error when attempting to access myanimelist.net.'):
        self.message = message
        super().__init__(self.message)

