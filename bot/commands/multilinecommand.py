
class MultiLineCommand:

    def __init__(self, desc):
        self.names = []
        self._name_tags = {}
        self.desc = desc
        self._lines = []

    def add_name(self, name, tags):
        assert type(tags) is set, 'unexpected type: {}'.format(type(tags).__name__)
        self.names.append(name)
        self._name_tags[name] = tags

    def add_line(self, text, tags):
        assert type(tags) is set, 'unexpected type: {}'.format(type(tags).__name__)
        self._lines.append(_Line(text, tags))

    @property
    def text(self):
        return '\n'.join(line.text for line in self._lines)

    def message(self, message, command, args):
        tags = self._name_tags[command]
        if not tags:
            filtered_lines = self._lines
        else:
            filtered_lines = [line for line in self._lines if bool(tags & line.tags)]
        # todo: cache text per name
        return '\n'.join(filtered_lines)

    def __repr__(self):
        return __class__.__name__ + ' ' + str(self.names)


class _Line:
    """An entry with tags. If one or more tag matches, the entry shall be printed"""
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags