#!/usr/bin/env python3

import re

def extract_sort_key(reference):
    """
    Extract the primary sorting key from a reference.
    Prioritizes:
    1. Author's last name 
    2. Year of publication
    """
    # Remove leading/trailing whitespace
    reference = reference.strip()
    
    # Try to extract last name using regex
    # Look for a name at the start of the reference, typically in the format "LastName, FirstInitial."
    name_match = re.match(r'^([A-Z][a-z]+)', reference)
    
    # If no name found, use the entire reference
    last_name = name_match.group(1) if name_match else reference
    
    # Try to find a year
    year_match = re.search(r'\((\d{4})\)|\,\s*(\d{4})', reference)
    year = year_match.group(1) or year_match.group(2) if year_match else '0000'
    
    # Create sort key: lowercase last name + year
    return f"{last_name.lower()} {year}"

def alphabetize_references(filename):
    """
    Alphabetize references in a file, preserving multi-line entries.
    """
    try:
        # Read the entire file
        with open(filename, 'r') as f:
            content = f.read()
        
        # Split into individual references (separated by newlines)
        references = [ref.strip() for ref in content.split('\n') if ref.strip()]
        
        # Sort references
        sorted_references = sorted(references, key=extract_sort_key)
        
        # Write back to file
        with open(filename, 'w') as f:
            # Join sorted references with newlines
            f.write('\n'.join(sorted_references))
            # Ensure file ends with a newline
            f.write('\n')
        
        # Print statistics
        print(f"Alphabetized {len(sorted_references)} references.")
        
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    alphabetize_references('reference.txt')
