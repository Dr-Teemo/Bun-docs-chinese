#!/usr/bin/env python3
"""
MDX 语法检查器
检查常见的 MDX 语法问题
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

class MDXChecker:
    def __init__(self):
        self.errors = []
        self.warnings = []
        
    def check_file(self, filepath: str) -> List[Tuple[str, int, str]]:
        """检查单个 MDX 文件"""
        issues = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # 检查标签配对
            issues.extend(self.check_tag_matching(filepath, lines))
            
            # 检查 HTML 注释
            issues.extend(self.check_html_comments(filepath, lines))
            
            # 检查代码块
            issues.extend(self.check_code_blocks(filepath, lines))
            
            # 检查缩进问题
            issues.extend(self.check_indentation(filepath, lines))
            
        except Exception as e:
            issues.append((filepath, 0, f"无法读取文件: {str(e)}"))
            
        return issues
    
    def check_tag_matching(self, filepath: str, lines: List[str]) -> List[Tuple[str, int, str]]:
        """检查 JSX 标签是否正确配对"""
        issues = []
        stack = []
        
        # 需要检查的标签
        tags_to_check = ['Note', 'Warning', 'Tip', 'Info', 'Step', 'Steps', 
                        'Accordion', 'Tab', 'Tabs', 'Card', 'CardGroup', 
                        'Frame', 'CodeGroup']
        
        for line_num, line in enumerate(lines, 1):
            # 跳过代码块内的内容
            if line.strip().startswith('```'):
                continue
                
            for tag in tags_to_check:
                # 查找开始标签
                open_matches = re.finditer(rf'<{tag}(?:\s|>)', line)
                for match in open_matches:
                    # 检查是否是自闭合标签
                    if not re.search(rf'<{tag}[^>]*/>', line[match.start():]):
                        stack.append((tag, line_num, line.strip()))
                
                # 查找结束标签
                close_matches = re.finditer(rf'</{tag}>', line)
                for match in close_matches:
                    if not stack:
                        issues.append((filepath, line_num, f"发现未匹配的闭合标签 </{tag}>"))
                    elif stack[-1][0] != tag:
                        issues.append((filepath, line_num, 
                                     f"标签不匹配: 期望 </{stack[-1][0]}>, 但发现 </{tag}>"))
                    else:
                        stack.pop()
        
        # 检查未闭合的标签
        for tag, line_num, line_content in stack:
            issues.append((filepath, line_num, f"标签 <{tag}> 未闭合"))
            
        return issues
    
    def check_html_comments(self, filepath: str, lines: List[str]) -> List[Tuple[str, int, str]]:
        """检查是否使用了 HTML 注释而不是 MDX 注释"""
        issues = []
        in_code_block = False
        
        for line_num, line in enumerate(lines, 1):
            # 跟踪代码块
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
            
            # 跳过代码块内的内容
            if in_code_block:
                continue
                
            # 检查 HTML 注释
            if '<!--' in line:
                issues.append((filepath, line_num, 
                             "使用了 HTML 注释 <!--，应该使用 MDX 注释 {/* */}"))
                             
        return issues
    
    def check_code_blocks(self, filepath: str, lines: List[str]) -> List[Tuple[str, int, str]]:
        """检查代码块是否正确闭合"""
        issues = []
        code_block_start = None
        
        for line_num, line in enumerate(lines, 1):
            if line.strip().startswith('```'):
                if code_block_start is None:
                    code_block_start = line_num
                else:
                    code_block_start = None
        
        if code_block_start is not None:
            issues.append((filepath, code_block_start, "代码块未闭合"))
            
        return issues
    
    def check_indentation(self, filepath: str, lines: List[str]) -> List[Tuple[str, int, str]]:
        """检查 JSX 标签内容的缩进问题"""
        issues = []
        
        for line_num, line in enumerate(lines, 1):
            # 检查 Note/Warning/Tip 等标签后的内容缩进
            if re.match(r'\s*<(Note|Warning|Tip|Info)>\s*$', line):
                if line_num < len(lines):
                    next_line = lines[line_num]
                    # 检查下一行是否正确缩进
                    if next_line.strip() and not next_line.startswith('    '):
                        # 如果下一行不是闭合标签且没有正确缩进
                        if not re.match(r'\s*</(Note|Warning|Tip|Info)>', next_line):
                            issues.append((filepath, line_num + 1, 
                                         "标签内容可能缺少正确的缩进"))
        
        return issues
    
    def check_all_files(self, directory: str = '.') -> None:
        """检查目录中的所有 MDX 文件"""
        mdx_files = list(Path(directory).rglob('*.mdx'))
        
        print(f"正在检查 {len(mdx_files)} 个 MDX 文件...\n")
        
        all_issues = []
        
        for filepath in mdx_files:
            issues = self.check_file(str(filepath))
            all_issues.extend(issues)
        
        # 打印结果
        if all_issues:
            print(f"发现 {len(all_issues)} 个问题:\n")
            
            # 按文件分组
            issues_by_file = {}
            for filepath, line_num, message in all_issues:
                if filepath not in issues_by_file:
                    issues_by_file[filepath] = []
                issues_by_file[filepath].append((line_num, message))
            
            for filepath, issues in sorted(issues_by_file.items()):
                print(f"\n📄 {filepath}")
                for line_num, message in sorted(issues):
                    print(f"  行 {line_num}: {message}")
        else:
            print("✅ 未发现语法问题！")

if __name__ == '__main__':
    checker = MDXChecker()
    checker.check_all_files('.')
