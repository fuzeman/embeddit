from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, map, *items):
        super(RegexConverter, self).__init__(map)
        self.regex = items[0]
