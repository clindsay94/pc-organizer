'''
PC Organizer

A program that helps you organize your PC by suggesting folder structures and cleaning up files.
'''

import os
import shutil

def find_large_files(path, size_limit_mb=100):
    '''Find files larger than the specified size limit.'''
    large_files = []
    for foldername, _, filenames in os.walk(path):
        for filename in filenames:
            try:
                file_path = os.path.join(foldername, filename)
                size_in_mb = os.path.getsize(file_path) / (1024 * 1024)
                if size_in_mb > size_limit_mb:
                    large_files.append(file_path)
            except FileNotFoundError:
                # Ignore files that can't be accessed
                pass
    return large_files

def organize_pc():
    '''Main function to organize the PC.'''
    # Start with the user's home directory
    start_path = os.path.expanduser("~")
    print(f"Scanning for large files in: {start_path}")

    large_files = find_large_files(start_path)

    if not large_files:
        print("No large files found. Your PC is already looking clean!")
        return

    print(f"Found {len(large_files)} large files.")

    archive_dir = os.path.join(start_path, "Archive")
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    for file_path in large_files:
        action = input(f"File: {file_path}\n  Size: {os.path.getsize(file_path) / (1024 * 1024):.2f} MB\n  Delete (d), archive (a), or skip (s)? ").lower()

        if action == 'd':
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")
        elif action == 'a':
            try:
                shutil.move(file_path, archive_dir)
                print(f"Archived: {file_path}")
            except OSError as e:
                print(f"Error archiving {file_path}: {e}")
        else:
            print(f"Skipped: {file_path}")

if __name__ == "__main__":
    organize_pc()
