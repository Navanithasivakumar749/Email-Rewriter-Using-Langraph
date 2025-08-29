from abbreviations import abbreviation_dict
import re

def expand_abbreviations(raw_email: str) -> str:
    def replacer(match):
        abbr = match.group(0)
        full = abbreviation_dict.get(abbr)
        return f"{abbr} ({full})" if full else abbr

    pattern = r'\b(' + '|'.join(re.escape(key) for key in abbreviation_dict.keys()) + r')\b'
    expanded_email = re.sub(pattern, replacer, raw_email)
    return expanded_email
