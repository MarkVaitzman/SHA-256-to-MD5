# SHA-256-to-MD5
Get MD5 hash from VT using SHA-256 list.


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

Requirments: pip install vt-py
