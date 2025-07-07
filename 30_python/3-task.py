import os
import logging
import argparse

parser = argparse.ArgumentParser(description="Rename files in a directory by changing their suffixes.")
parser.add_argument('directory', metavar="path", help='The path to the directory containing files.')
parser.add_argument('old_suffix', metavar="sufix1", help='The suffix to be replaced.')
parser.add_argument('new_suffix', metavar="sufix2", help='The new suffix to replace the old one.')

args = parser.parse_args()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def rename_file(directory, old_suffix, new_suffix):
    """
    Renames files in a directory by changing their suffixes.
    
    Args:
        directory (str): The path to the directory containing files.
        old_suffix (str): The suffix to be replaced.
        new_suffix (str): The new suffix to replace the old one.
    """
    try:
        for filename in os.listdir(directory):
            if filename.endswith(old_suffix):
                new_filename = filename[:-len(old_suffix)] + new_suffix
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                logging.info(f"Renamed {filename} to {new_filename}")
    except Exception as e:
        logging.error(f"Error renaming files: {e}")

try:
    path = str(args.directory)
    sufix1 = str(args.old_suffix)
    sufix2 = str(args.new_suffix) 
except ValueError:
    logging.error("Invalid input: Please enter valid strings for path and suffixes.")

rename_file(path, sufix1, sufix2)