__artifacts_v2__ = {
    "bankid_uhi": {
        "name": "BankId UHI value",
        "description": "Calculates and retrieves the UHI value from BankId application.",
        "author": "mattias9502",  # Replace with the actual author's username or name
        "version": "0.1",  # Version number
        "date": "2025-12-14",  # Date of the latest version
        "requirements": "none",
        "category": "Bankid",
        "notes": "",
        "paths": ('*/data/system/users/*/settings_ssaid.xml',),
        "function": "get_bankid_uhi",
        "output_types": ["html", "lava", "tsv"]
    }
}

import hashlib
import re
import xml.etree.ElementTree as ET
from scripts.ilapfuncs import abxread, checkabx


def get_bankid_uhi(files_found, report_folder, seeker, wrap_text):

    user = re.compile(r'.*/data/system/users/(\d+)/settings_ssaid\.xml$')
    regexp_adx = re.compile(r'com.bankid.bus.*?([a-z0-9]+)')

    data_list = []
    source_path = ""

    for file_path in files_found:
        source_path = file_path
        user_match = user.match(file_path)
        if user_match:
            user_id = user_match.group()
            if checkabx(file_path):
                tree = abxread(file_path, multi_root=True)
            else:
                tree = ET.parse(file_path)
            
            root = tree.getroot()
            for elem in root:
                
                
                        data_list.append((uhi_value, user_id))



        
    data_headers = ('UHI Value', 'User')
    return data_headers, data_list, source_path