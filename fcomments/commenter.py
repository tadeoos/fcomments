import re


class Commenter:
    """Comment or uncomment lines in file."""

    def __init__(self, **kwargs):
        self.result = ''
        self.path = None
        self.output = None
        self.all_lines = False
        self.uncomment = False
        self.comment = False
        self.reverse = True
        self.in_pattern = None
        self.out_pattern = None
        self.lines = None
        self.comment_symbol = '#'
        for key in kwargs:
            setattr(self, key, kwargs[key])
        with open(self.path, "r") as f:
            self.original = [l for l in f]
        if self.all_lines:
            self.lines = [i for i in range(len(self.original) + 1)]

    def comment_file(self):
        if self.lines:
            self.line_based(lines=self.lines, original=self.original, comment=self.comment)
        else:
            self.pattern_based()
        self.save_file()

    def update(self, result=False):
        if not result:
            with open(self.path, "r") as f:
                self.original = [l for l in f]
        else:
            print(self.result.split())
            self.original = self.result.split()


    def handle_line(self, line, comment, reverse=True):
        is_comment = re.match('\s*' + self.comment_symbol, line) is not None
        if reverse:
            comment = False if is_comment else True
        elif not (comment or is_comment):
            return line

        if comment:
            if is_comment:
                print('Warning: line already commented')
                return line
            else:
                return self.comment_symbol + line
        else:
            assert is_comment
            return line[1:]


    def line_based(self, lines=None, original=None,
                    comment=False, update=False):
        res_file = []
        assert lines
        for i, line in enumerate(original):
            if i + 1 in lines:
                line = self.handle_line(line, comment)
            res_file.append(line)
        self.result = ''.join(res_file)
        if update:
            pass

    def pattern_based(self):
        start_pattern = False
        end_pattern = False
        res_file = []
        for line in self.original:
            if start_pattern and re.match(self.out_pattern, line):
                end_pattern = True
                start_pattern = False
            if start_pattern:
                line = self.handle_line(line, self.comment)
            res_file.append(line)
            if end_pattern:
                continue
            if re.match(self.in_pattern, line):
                start_pattern = True

        self.result = ''.join(res_file)

    def save_file(self):
        path = self.output if self.output else self.path
        with open(path, "w") as f:
            f.write(self.result)
