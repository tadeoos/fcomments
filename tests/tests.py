from unittest import TestCase
import os

from fcomments.commenter import Commenter
<<<<<<< HEAD
=======
from fcomments import main, create_parser


dir_path = os.path.dirname(os.path.abspath(__file__))
TEST_FILE_PATH = os.path.join(dir_path, 'ex_file.py')
>>>>>>> [wip] to be squashed later


def is_commented(line, comment_symbol='#'):
    if line.startswith(comment_symbol):
        return True
    else:
        return False


def file_check(lines, comm_state=True, path=TEST_FILE_PATH, strict=False):
    with open(path) as test_file:
        for i, line in enumerate(test_file):
            if i + 1 in lines:
                if not is_commented(line):
                    return False
            elif strict:
                if is_commented(line):
                    return False
    return True


<<<<<<< HEAD
dir_path = os.path.dirname(os.path.realpath(__file__))
PATH = os.path.join(dir_path, 'ex_file.py')


class ScriptTest(TestCase):
=======
class fCommentsTestCase(TestCase):

    def __init__( self, *args, **kwargs ):
        super( fCommentsTestCase, self ).__init__( *args, **kwargs )
        self.path = TEST_FILE_PATH
        self.def_dic = {'output': None, 'comment_symbol': '#', 'lines': None,
                'comment': False, 'all_lines': False, 'uncomment': False,
                'in_pattern': None, 'out_pattern': None}
        self.reverse = True
        self.cmnter = Commenter(path=self.path, reverse=self.reverse)

    def run_command(self, atrs, lines, assrt=True):
        custom_dic = dict(self.def_dic)
        custom_dic.update(atrs)
        newcm = Commenter(**custom_dic)
        newcm.comment_file()
        if assrt:
            self.assertTrue(file_check(lines=lines, path=newcm.path))
        else:
            self.assertFalse(file_check(lines=lines, path=newcm.path))

    def tearDown(self):
        atrs = {'uncomment': True, 'all_lines': True,
                'path': self.path, 'reverse': False}
        self.run_command(atrs, [3], assrt=False)
        atrs = {'comment': True, 'lines': [1],
                'path': self.path, 'reverse': False}
        self.run_command(atrs, [1], assrt=True)



class ScriptTest(fCommentsTestCase):
>>>>>>> [wip] to be squashed later

    def test_manual(self):
        parser = create_parser()

    def test_infile_usage(self):
        """Test usage with one Class instatiation and atribs manipulation."""
        lin = [*range(4, 11)]
        c = Commenter(path=TEST_FILE_PATH, lines=lin)
        c.comment_file()
        # c.update(result=1)
        before = c.result
        self.assertTrue(file_check(lines=lin, comm_state=True))  # lines 4-11 are commented
        c.comment_file()
        after = c.result
        self.assertEqual(before, after)
        self.assertTrue(file_check(lines=lin, comm_state=True))  # lines 4-11 are still commented because original not updated
        c.reverse = False
        c.lines = [3, 4, 5]
        c.comment_file()
        self.assertFalse(file_check(lines=lin, comm_state=True))  # nothing changed, -u

<<<<<<< HEAD

class CommenterTests(TestCase):
    dir_path = os.path.dirname(os.path.realpath(__file__))
=======
>>>>>>> [wip] to be squashed later


class CommenterTests(fCommentsTestCase):

    def test_sanity(self):
<<<<<<< HEAD
        self.assertTrue(file_check(self.path, [1]))
        self.assertFalse(file_check(self.path, [1, 3, 4]))
=======
        self.assertTrue(file_check(path=self.path, lines=[1]))
        self.assertFalse(file_check(path=self.path, lines=[1, 3, 4]))
>>>>>>> [wip] to be squashed later

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

<<<<<<< HEAD
        self.assertFalse(file_check(self.path, [*range(13, 23)]))
        self.assertFalse(file_check(self.path, [*range(13, 24)]))
        self.assertFalse(file_check(self.path, [*range(15, 25)]))

        self.assertTrue(file_check(self.path, [*range(14, 23)]))
        self.assertTrue(file_check(self.path, [*range(18, 20)]))
=======
        self.assertFalse(file_check(path=self.path, lines=[*range(13, 23)]))
        self.assertFalse(file_check(path=self.path, lines=[*range(13, 24)]))
        self.assertFalse(file_check(path=self.path, lines=[*range(15, 25)]))

        self.assertTrue(file_check(path=self.path, lines=[*range(14, 23)]))
        self.assertTrue(file_check(path=self.path, lines=[*range(18, 20)]))
>>>>>>> [wip] to be squashed later

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
    #
    # def run_command(self, atrs, lines, assrt=True):
    #     custom_dic = dict(self.def_dic)
    #     custom_dic.update(atrs)
    #     newcm = Commenter(**custom_dic)
    #     newcm.comment_file()
    #     if assrt:
    #         self.assertTrue(file_check(path=newcm.path, lines=lines))
    #     else:
    #         self.assertFalse(file_check(path=newcm.path, lines=lines))

    def line_equal(self, line_in, line_out, cmnt=False):
        line = self.cmnter.handle_line(line_in, cmnt)
        self.assertEqual(line, line_out)
    #
    # def tearDown(self):
    #     atrs = {'uncomment': True, 'all_lines': True,
    #             'path': self.path, 'reverse': False}
    #     self.run_command(atrs, [3], assrt=False)
    #     atrs = {'comment': True, 'lines': [1],
    #             'path': self.path, 'reverse': False}
    #     self.run_command(atrs, [1], assrt=True)
