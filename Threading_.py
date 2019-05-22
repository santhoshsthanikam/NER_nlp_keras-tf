import difflib
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print(fuzz.ratio("Python.3.6", "python"))
a = "Python.3.6"
b = "python"

seq = difflib.SequenceMatcher(None,a,b)
d = seq.ratio()*100
print(d)