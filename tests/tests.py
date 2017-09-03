from unittest import TestCase
import os

from fcomments.commenter import Commenter


def is_commented(line, comment_symbol='#'):
    if line.startswith(comment_symbol):
        return True
    else:
        return False


def file_check(path, lines, comm_state=True):
    with open(path) as test_file:
        for i, line in enumerate(test_file):
            if i + 1 in lines:
                if not is_commented(line):
                    return False
    return True


dir_path = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.join(dir_path, 'ex_file.py')


class ScriptTest(TestCase):

    def test_manual(self):
        # main()
        pass


class CommenterTests(TestCase):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    path = os.path.join(dir_path, 'ex_file.py')
    def_dic = {'output': None, 'comment_symbol': '#', 'lines': None,
               'comment': False, 'all_lines': False, 'uncomment': False,
               'in_pattern': None, 'out_pattern': None}
    reverse = True
    cmnter = Commenter(path=path, reverse=reverse, **def_dic)

    def test_sanity(self):
        self.assertTrue(file_check(self.path, [1]))
        self.assertFalse(file_check(self.path, [1, 3, 4]))

    def test_handle_line(self):
        self.line_equal('    sth()', '#    sth()', True)
        self.line_equal('    sth()', '#    sth()', False)
        self.line_equal('#    sth()', '    sth()', False)
        self.line_equal('#    sth()', '    sth()', False)
        self.cmnter.reverse = False
        self.line_equal('    sth()', '    sth()', False)
        self.line_equal('    sth()', '#    sth()', True)
        self.line_equal('#    sth()', '#    sth()', True)

    def test_comment_file(self):

        self.cmnter.reverse = True
        self.cmnter.lines = [2, 4, 5]
        self.cmnter.comment_file()
        self.cmnter.comment_file()

        self.cmnter.lines = None

        self.cmnter.in_pattern = '\s+operations\s?=\s?\['
        self.cmnter.out_pattern = '\s+\]'
        self.cmnter.comment_file()

        self.assertFalse(file_check(self.path, [*range(13, 23)]))
        self.assertFalse(file_check(self.path, [*range(13, 24)]))
        self.assertFalse(file_check(self.path, [*range(15, 25)]))

        self.assertTrue(file_check(self.path, [*range(14, 23)]))
        self.assertTrue(file_check(self.path, [*range(18, 20)]))

        atrs = {'lines': [1, 2, 4, 5], 'comment': True,
                'path': self.path, 'reverse': False}
        self.run_command(atrs, [1, 2, 4, 5])

    def test_all_lines(self):
        atrs = {'all_lines': True, 'path': self.path,
                'reverse': False, 'comment': True}
        self.run_command(atrs, [13, 14, 7, 2, 21])
        atrs = {'all_lines': True, 'path': self.path,
                'reverse': False, 'uncomment': True}
        self.run_command(atrs, [])

    def run_command(self, atrs, lines, assrt=True):
        custom_dic = dict(self.def_dic)
        custom_dic.update(atrs)
        newcm = Commenter(**custom_dic)
        newcm.comment_file()
        if assrt:
            self.assertTrue(file_check(newcm.path, lines))
        else:
            self.assertFalse(file_check(newcm.path, lines))

    def line_equal(self, line_in, line_out, cmnt=False):
        line = self.cmnter.handle_line(line_in, cmnt)
        self.assertEqual(line, line_out)

    def tearDown(self):
        atrs = {'uncomment': True, 'all_lines': True,
                'path': self.path, 'reverse': False}
        self.run_command(atrs, [3], assrt=False)
        atrs = {'comment': True, 'lines': [1],
                'path': self.path, 'reverse': False}
        self.run_command(atrs, [1], assrt=True)
