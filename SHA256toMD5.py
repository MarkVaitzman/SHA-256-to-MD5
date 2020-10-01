"""
Get the MD5 value using the SHA256 from VT.
Author: Mark Vaitzman
Ver: 0.1

Input: Text file, each line contains 1 sha256 value
Output: Text file with MD5 values, also prints the number of unknown hashes.

Usage:
Run cmd with the follwoing command:
sha256tomd5.py <InputFileName> <OutputFileName> <VT_API key>

*VT_API key can be found in VT profile (public, free version)
Limited to 4 requests in a minute and 
"""

import vt
import sys
import time

filename = sys.argv[1]
outputfile = sys.argv[2]
vtApi = sys.argv[3]
client = vt.Client(vtApi)

result = open(outputfile, "x")
lineList = [line.rstrip('\n') for line in open(filename)]
unknownHashes = 0
unknownHashesList =[]

for sha256 in lineList:
    try:
        md5 = client.get_object("/files/" + sha256.md5)
        result.write(md5)
        result.write("\n")
    except:
        unknownHashes = unknownHashes+1
        unknownHashesList.append(sha256)
    time.sleep(16)
    
result.close()
print("Unknown hashes: ", unknownHashes,"\n", unknownHashesList)
