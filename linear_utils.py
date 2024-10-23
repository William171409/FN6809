import re
import pandas as pd
import numpy as np

def get_fuel_type(spec):
    value = re.search(r'(?i)(Electric|Motor|Battery|gasoline|hybrid|flex|EV|Electric|Battery)',spec)
    return value.group(0) if value else 'NA'

def get_hp(spec):
    value = re.search(r'(\d+(?:\.\d+)?)HP', spec)
    return float(value.group(1)) if value else pd.NA

def get_engine(spec):
    value = re.search(r'(\d+(?:\.\d+)?)\s?L(iter)?', spec)
    return float(value.group(1)) if value else pd.NA

def get_cylinder(spec):
    value = re.search(r'(?i)((?:straight\s+|flat\s+)?\d+ Cylinder|V\d+|V-\d+|h\d+|i-?\d+|w\d+)', spec)
    return value.group(1) if value else 'NA'

def get_fi(spec):
    value = re.search(r'(?i)(PDI|GDI|MPFI|TFSI|DDI|SIDI|GTDI|TSI)', spec)
    return value.group(0) if value else 'NA'

def get_turbo(spec):
    value = re.search(r'(?i)(Turbo|Twin Turbo|Intercooled|Supercharged|sc|T/C)', spec)
    return value.group(0) if value else 'NA'

def get_trans_type(spec):
    value = re.search(r'(?i)(Automatic cvt|Automatic|a/?t|m/?t|cvt|Variable|manual|fixed|dual)',spec)
    return value.group(0) if value else 'M/T'

def get_speed(spec):
    value = re.search(r'(?i)(\d+)-?\s?(?:speed)?',spec)
    return int(value.group(1)) if value else pd.NA

def get_color(spec):
    value = re.search(r'(?i)(Black|White|Gray|Silver|Blue|Red|Green|Gold|Brown|Orange|Beige|Yellow|Brown|Ebony)',spec)
    return value.group(0) if value else 'Miscellaneous'

def get_color_type(spec):
    value = re.search(r'(?i)(Metallic|Metal|chrome)',spec)
    return value.group(0) if value else 'Gloss'
