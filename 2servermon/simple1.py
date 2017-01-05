#--coding:UTF-8--
import difflib

text1 = """text1:
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""  # 定义字符串1
text1_lines = text1.splitlines()  # 以行进行分割，以便进行对比