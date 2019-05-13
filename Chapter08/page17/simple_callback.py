from ansible.callbacks import display

class CallbackModule(object):
    def on_any(self, *args, **kwargs):
        msg = '\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
        display(msg * 8)
