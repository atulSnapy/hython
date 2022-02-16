import pyinstaller_versionfile
from version import VERSION

pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version=VERSION,
    company_name="Hython",
    file_description="Hython.exe to run hython files",
    internal_name="Hython",
    legal_copyright="© Snapy. All rights reserved.",
    original_filename="hython.exe",
    product_name="Hython"
)