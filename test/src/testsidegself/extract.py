import os.path
import testsidegself.command


TEMPLATE_HEAD = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://selenium-ide.openqa.org/profiles/test-case">
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="selenium.base" href="http://code.google.com/" />
<title>TestCase</title>
</head>
<body>
<table cellpadding="1" cellspacing="1" border="1">
<thead>
<tr><td rowspan="1" colspan="3">TestCase</td></tr>
</thead><tbody>
"""

TEMPLATE_FOOT = """\
</tbody></table>
</body>
</html>
"""


def write_test_file(commands, dest_path):
    """Writes the commands into a HTML selenium file."""
    f = file(os.path.join(dest_path, 'testcase.html'), 'w')
    f.write(TEMPLATE_HEAD)
    for command in commands:
        f.write('<tr>\n')
        for index in range(3):
            try:
                value = command[index]
            except IndexError:
                value = ''
            f.write('<td>%s</td>\n' % value)
        f.write('</tr>\n')
    f.write(TEMPLATE_FOOT)
    f.close()


def extract_commands(src_path, dest_path):
    """Extracts the commands from the reference and creates a selenium file."""
    # Entry point
    commands = testsidegself.command.extract(src_path)
    write_test_file(commands, dest_path)