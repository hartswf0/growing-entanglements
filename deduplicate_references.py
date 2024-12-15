#!/usr/bin/env python3

def deduplicate_references(filename):
    """
    Remove duplicate entries from a reference file while preserving order.
    Each reference is assumed to be a complete entry that may span multiple lines.
    Entries are separated by blank lines.
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # Split content into individual references
        # References are separated by one or more blank lines
        references = [ref.strip() for ref in content.split('\n\n') if ref.strip()]
        
        # Use dict to preserve order while removing duplicates
        # Python 3.7+ dicts maintain insertion order
        unique_refs = dict.fromkeys(references)
        
        # Join unique references back together with double newlines
        deduped_content = '\n\n'.join(unique_refs)
        
        # Write back to file
        with open(filename, 'w') as f:
            f.write(deduped_content)
            # Ensure file ends with newline
            if deduped_content:
                f.write('\n')
        
        # Print statistics
        original_count = len(references)
        unique_count = len(unique_refs)
        if original_count != unique_count:
            print(f"Removed {original_count - unique_count} duplicate references.")
            print(f"File now contains {unique_count} unique references.")
        else:
            print("No duplicate references found.")
            
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    deduplicate_references('reference.txt')
