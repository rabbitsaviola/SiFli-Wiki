import os
import re

def replace_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = r'(example/hal/[^\s\)]+)'
    
    def replacer(match):
        path = match.group(1)
        return f'[{path}](https://github.com/OpenSiFli/SiFli-SDK/tree/main/{path})'
    
    new_content = re.sub(pattern, replacer, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated: {file_path}")

def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                replace_in_file(file_path)

# 使用当前目录作为起始点
current_directory = os.getcwd()
traverse_directory(current_directory)
