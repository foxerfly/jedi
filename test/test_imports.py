import pytest

import jedi
from jedi._compatibility import find_module_py33
from .helpers import cwd_at


@pytest.mark.skipif('sys.version_info < (3,3)')
def test_find_module_py33():
    """Needs to work like the old find_module."""
    print(find_module_py33('_io'))
    assert find_module_py33('_io') == (None, '_io', False)


@cwd_at('test/not_in_sys_path/pkg')
def test_import_not_in_sys_path():
    """
    non-direct imports (not in sys.path)
    """
    jedi.set_debug_function()
    a = jedi.Script(path='module.py', line=3).goto_definitions()
    assert a[0].name == 'int'
