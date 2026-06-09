import threading

path = '/usr/local/lib/python3.12/dist-packages/skidl/logger.py'
with open(path) as f:
    content = f.read()

content = content.replace('import logging\n', 'import logging\nimport threading\n')

old = ('    def __init__(self, *args, **kwargs):\n'
       '        try:\n'
       '            self.filename = kwargs["filename"]\n'
       '        except KeyError:\n'
       '            self.filename = args[0]\n'
       '        try:\n'
       '            super().__init__(*args, **kwargs)\n'
       '        except PermissionError as e:\n'
       '            # Prevents future error when removing non-existent log file.\n'
       '            self.filename = None\n'
       '            print(e)')

new = ('    def __init__(self, *args, **kwargs):\n'
       '        self.filters = []\n'
       '        self.lock = threading.RLock()\n'
       '        self.level = 0\n'
       '        self.formatter = None\n'
       '        self._closed = False\n'
       '        self._name = None\n'
       '        self.stream = None\n'
       '        try:\n'
       '            self.filename = kwargs["filename"]\n'
       '        except KeyError:\n'
       '            self.filename = args[0]\n'
       '        try:\n'
       '            super().__init__(*args, **kwargs)\n'
       '        except PermissionError as e:\n'
       '            self.filename = None\n'
       '            self._closed = True\n'
       '            print(e)')

if old in content:
    content = content.replace(old, new)
    with open(path, 'w') as f:
        f.write(content)
    print('Logger patched for Python 3.12')
else:
    print('Patch target not found - may already be patched or different version')
    if 'self._closed' in content:
        print('Already patched')
    else:
        print('ERROR: Could not find patch target')
        exit(1)
