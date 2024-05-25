import sys
import os

# Add the parent directory of the script to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import capitalize

assert capitalize('') == ''
assert capitalize('hello') == 'Hello'

print('Все тесты пройдены!')