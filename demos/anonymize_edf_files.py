import glob
import os
from pathlib import Path

import sys

# Add the path to the parent folder (where ensemble_eeg is located)
sys.path.append(str(Path.cwd().parent))

from ensemble_eeg import ensemble_edf

# !!! change this to the location of the edf files you want to anonymize
path2edffiles = "/volatile/home/js283516/Documents/IHU-ICE_WP4/repertoire_clair/test"
files = glob.glob(os.path.join(path2edffiles, "*.edf"))

for file in files:
    ensemble_edf.fix_edf_header(file)  # fix edf header to edf+ standard
    ensemble_edf.anonymize_edf_header(file)  # anonymize edf header

# organize anonymized files in a subfolder
ensemble_edf.organize_anonymized_files(path2edffiles)
