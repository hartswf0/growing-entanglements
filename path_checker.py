#!/usr/bin/env python3

import os
import re
from pathlib import Path
import json
from bs4 import BeautifulSoup
import markdown

class PathChecker:
    def __init__(self, repo_root):
        self.repo_root = Path(repo_root).resolve()
        self.issues = []
        self.fixed_count = 0
        
    def check_html_file(self, file_path):
        """Check HTML files for problematic paths in src, href, and data attributes."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check all elements with src, href, or data attributes
        elements_with_paths = soup.find_all(lambda tag: any(attr in tag.attrs 
                                          for attr in ['src', 'href', 'data-src']))
        
        fixed_content = content
        for element in elements_with_paths:
            for attr in ['src', 'href', 'data-src']:
                if attr in element.attrs:
                    path = element[attr]
                    if self._is_problematic_path(path):
                        fixed_path = self._fix_path(path, file_path)
                        fixed_content = fixed_content.replace(f'{attr}="{path}"', 
                                                           f'{attr}="{fixed_path}"')
                        self.issues.append(f"Fixed {attr} in {file_path}: {path} -> {fixed_path}")
                        self.fixed_count += 1
        
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)

    def check_markdown_file(self, file_path):
        """Check Markdown files for problematic paths in links and images."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find markdown links and images
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        
        fixed_content = content
        for pattern in [link_pattern, image_pattern]:
            for match in re.finditer(pattern, content):
                path = match.group(2)
                if self._is_problematic_path(path):
                    fixed_path = self._fix_path(path, file_path)
                    fixed_content = fixed_content.replace(f']({path})', f']({fixed_path})')
                    self.issues.append(f"Fixed link in {file_path}: {path} -> {fixed_path}")
                    self.fixed_count += 1
        
        if fixed_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)

    def check_json_file(self, file_path):
        """Check JSON files for problematic paths in any string value."""
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                self.issues.append(f"Error: Could not parse JSON file {file_path}")
                return
        
        def fix_json_paths(obj):
            if isinstance(obj, dict):
                return {k: fix_json_paths(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [fix_json_paths(item) for item in obj]
            elif isinstance(obj, str) and self._is_problematic_path(obj):
                fixed_path = self._fix_path(obj, file_path)
                if fixed_path != obj:
                    self.issues.append(f"Fixed path in {file_path}: {obj} -> {fixed_path}")
                    self.fixed_count += 1
                return fixed_path
            return obj
        
        fixed_data = fix_json_paths(data)
        if fixed_data != data:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(fixed_data, f, indent=2)
    
    def _is_problematic_path(self, path):
        """Check if a path needs fixing."""
        if not path:
            return False
        if path.startswith(('http://', 'https://', 'mailto:', '#', 'tel:')):
            return False
            
        problematic_indicators = [
            'file:///',
            str(self.repo_root),
            'C:',
            'D:',
            '/Users/',
            '\\',  # Windows path separator
            Path.home().as_posix()
        ]
        
        return any(indicator in str(path) for indicator in problematic_indicators)
    
    def _fix_path(self, path, current_file):
        """Convert absolute or problematic paths to relative paths."""
        # Remove file:/// prefix if present
        path = path.replace('file:///', '')
        
        # Handle Windows paths
        if ':' in path:  # Windows drive letter
            path = Path(path).name  # Just keep the filename
        
        # Convert path to Path object
        try:
            path = Path(path)
        except Exception:
            return path  # Return original if can't parse
        
        # If path is absolute or contains repo path, make it relative
        if path.is_absolute() or str(self.repo_root) in str(path):
            try:
                # Get the relative path from current file to target
                current_dir = Path(current_file).parent
                
                # If path contains repo path but isn't absolute, make it absolute first
                if not path.is_absolute() and str(self.repo_root) in str(path):
                    path = self.repo_root / path.relative_to(Path(str(self.repo_root).split('/')[-1]))
                
                # If path is within repo, make it relative to current file
                if str(path).startswith(str(self.repo_root)):
                    path = os.path.relpath(path, current_dir)
                else:
                    # If path is outside repo, just use the name
                    path = path.name
            except ValueError:
                # If path is outside repo or can't be made relative, just use the name
                path = path.name
        
        # Normalize path separators to forward slashes
        return str(path).replace('\\', '/')
    
    def check_repository(self):
        """Check all relevant files in the repository."""
        for root, _, files in os.walk(self.repo_root):
            for file in files:
                file_path = Path(root) / file
                
                # Skip the script itself and any dot files
                if file == 'path_checker.py' or file.startswith('.'):
                    continue
                
                # Process files based on extension
                if file.endswith('.html'):
                    self.check_html_file(file_path)
                elif file.endswith('.md'):
                    self.check_markdown_file(file_path)
                elif file.endswith('.json'):
                    self.check_json_file(file_path)
        
        # Print report
        print(f"\nPath Checker Report:")
        print(f"==================")
        print(f"Files checked: {len(self.issues)}")
        print(f"Paths fixed: {self.fixed_count}")
        print("\nDetailed fixes:")
        for issue in self.issues:
            print(f"- {issue}")

if __name__ == "__main__":
    checker = PathChecker('/Users/gaia/resistance-topology')
    checker.check_repository()
