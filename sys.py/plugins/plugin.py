class Plugin:
    """This base class only exist to provide empty handler if not used/supported by the plugin"""
    def __init__(self):
        # Nothing to do on default handler
        pass

    def event_handler(self):
        # Nothing to do on default handler
        pass

    def tick(self):
        # Nothing to do on default handler
        pass

    def draw(self):
        # Nothing to do on default handler
        pass
