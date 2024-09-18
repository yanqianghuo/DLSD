import os
import re

def rename_files_with_suffix(folder_path):
    # List all files in the specified folder
    files = os.listdir(folder_path)
    
    # Filter out files only (ignore directories)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    
    # Create a map to group files by their suffixes
    suffix_groups = {}
    
    for file_name in files:
        # Extract suffixes
        match = re.match(r'(.+?)_([^_]+)\.(\w+)$', file_name)
        if match:
            base_name, suffix, ext = match.groups()
            if base_name not in suffix_groups:
                suffix_groups[base_name] = []
            suffix_groups[base_name].append((suffix, ext, file_name))

    # Rename files sequentially
    index = 1
    for base_name, items in suffix_groups.items():
        for suffix, ext, old_name in items:
            # Create the new file name with index and suffix
            new_name = f"{index}_{suffix}.{ext}"
            
            # Define old and new file paths
            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")
        
        index += 1

# Example usage
folder_path = r'C:\Users\25298\Desktop\中公高科\英文论文写作\绘图\HTML_PAGE\select'  # Update this path to your folder
rename_files_with_suffix(folder_path)
