class HeavyAccessRestrictionError(Exception):
    def __init__(self, message='Request to MAL denied due to heavy site access.'):
        self.message = message
        super().__init__(self.message)

