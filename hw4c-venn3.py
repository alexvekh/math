import matplotlib.pyplot as plt
from matplotlib_venn import venn3

total = 40
python_coders = 18
cpp_coders = 19
java_coders = 21
python_and_cpp = 10
python_and_java = 7
cpp_and_java = 8
others = 3

x = total - others - python_coders - cpp_coders - java_coders + python_and_cpp + python_and_java + cpp_and_java
print("одночасно знають усі три мови: ", x)

python_only = python_coders - python_and_cpp - python_and_java + x
cpp_only = cpp_coders - python_and_cpp - cpp_and_java + x
java_only = java_coders - python_and_java - cpp_and_java + x

check = python_only + cpp_only + java_only + x + (python_and_cpp - x) + (python_and_java - x) + (cpp_and_java - x) + others == total
print("Test: ", check)

#venn3([set1, set2, set3], ('>10', 'Парні', 'Кратні 3'))
venn3(subsets = (python_only, cpp_only, (python_and_cpp - x), java_only, (python_and_java - x), (cpp_and_java - x), x), set_labels=('Python', 'C++', 'Java'))
plt.show()