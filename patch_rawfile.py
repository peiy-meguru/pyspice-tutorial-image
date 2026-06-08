import re

path = '/usr/local/lib/python3.12/dist-packages/PySpice/Spice/RawFile.py'
with open(path) as f:
    content = f.read()

old = """        if label != expected_label:
            raise NameError("Expected label %s instead of %s" % (expected_label, label))"""

new = """        # Skip ngspice 42+ Note/Warning header lines
        if label in ('Note', 'Warning'):
            line = self._read_line(header_line_iterator)
            self._logger.debug(line)
            if has_value:
                location = line.find(': ')
                label, value = line[:location], line[location + 2:]
            else:
                label = line[:-1]
        if label != expected_label:
            raise NameError("Expected label %s instead of %s" % (expected_label, label))"""

if old in content:
    content = content.replace(old, new)
    with open(path, 'w') as f:
        f.write(content)
    print('RawFile.py patched successfully for ngspice 42+')
else:
    print('Patch target not found - may already be patched or different version')
    # Check existing content
    if 'if label in' in content:
        print('Already patched')
    else:
        print('ERROR: Could not find patch target')
        exit(1)
