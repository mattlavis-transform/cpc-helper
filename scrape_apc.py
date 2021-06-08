import requests
import re
import os.path
from markdownify import markdownify as md

urls1 = [
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-a-series-appendix-2a",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-b-series-appendix-2a",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-c-series-appendix-2a",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-d-series-appendix-2a",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-e-series-appendix-2a",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-f-series-appendix-2a"
]

urls2 = [
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-1-series-appendix-2b",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-0-series-appendix-2b",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-2-series-appendix-2b",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-3-series-appendix-2b",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-4-series-appendix-2b",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-6-series-appendix-2b",
    "https://www.gov.uk/government/publications/appendix-2-de-111-additional-procedure-codes-of-the-customs-declaration-service-cds/additional-procedure-code-9-series-appendix-2b"
]

folder = "/Users/matt.admin/sites and projects/1. Online Tariff/ott prototype/app/data/cpc/markdown-apc"

# The EU APC codes
for url in urls1:
    page = requests.get(url)
    page = str(page.content)
    parts = page.split("<h2")
    index = 0
    for part in parts:
        index += 1
        if index > 1:
            part = "<h2" + part
            regex = '^<h2 id="[a-z0-9]{3}-'
            ret = re.match(regex, part)
            if ret is not None:
                ret2 = md(part)
                ret2 = ret2.replace("\\n", "")
                apc = ret.group(0).replace(
                    '<h2 id="', '').strip("-").upper() + ".md"
                filepath = os.path.join(folder, apc)
                # if not os.path.exists(filepath):
                f = open(filepath, "w+")
                f.write(ret2)
                f.close()
                
                
# The UK APC codes
for url in urls2:
    page = requests.get(url)
    page = str(page.content)
    parts = page.split("<h2")
    for part in parts:
        part = "<h2" + part
        regex = '<span class="number">[0-9A-Za-z]{3}'
        ret = re.search(regex, part, flags=re.MULTILINE)
        if ret is not None:
            ret2 = md(part)
            ret2 = ret2.replace("\\n", "")
            apc = ret.group(0).replace('<span class="number">', '').upper() + ".md"
            filepath = os.path.join(folder, apc)
            f = open(filepath, "w+")
            f.write(ret2)
            f.close()                
