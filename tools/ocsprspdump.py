#!/usr/bin/env python
#
# This file is part of pyasn1-modules software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pyasn1.sf.net/license.html
#
# Read ASN.1/PEM OCSP response on stdin, parse into
# plain text, then build substrate from it
#
from pyasn1.codec.der import decoder, encoder
from pyasn1_modules import rfc2560, pem
import sys

if len(sys.argv) != 1:
    print("""Usage:
$ cat ocsp-response.pem | %s""" % sys.argv[0])
    sys.exit(-1)
    
ocspReq = rfc2560.OCSPResponse()

substrate = pem.readBase64FromFile(sys.stdin)
if not substrate:
    sys.exit(0)
        
cr, rest = decoder.decode(substrate, asn1Spec=ocspReq)

print(cr.prettyPrint())

assert encoder.encode(cr) == substrate, 'OCSP request recode fails'
