#!/usr/bin/env python
import argparse
import codecs
import string
import sys


# Stateless encoder/decoder
LOWER_CHARS = set(string.lowercase)
OLA_K_ASE_CODEC = 'OLA_K_ASE'


class InvertCapsCodec(codecs.Codec):
    def encode(self, input, errors='strict'):
        for line in input.split("\n"):
            line = line.strip()
            if (line and (bool(LOWER_CHARS.intersection(set(line)))
                          or not line.startswith("OLA K ASE ")
                          or not line.endswith(" O K ASE"))):
                raise SyntaxError("OLA K ASE SYNTAXERROR O K ASE:"
                                  " {0}".format(line))
        return input.replace("OLA K ASE ", "").replace(" O K ASE", "").lower(), 0


# Register the codec search function
def find_ola_k_ase(encoding):
    """Return the codec for 'OLA_K_ASE'.
    """
    if encoding.upper() == OLA_K_ASE_CODEC:
        return codecs.CodecInfo(
            name=OLA_K_ASE_CODEC,
            encode=InvertCapsCodec().encode,
            decode=InvertCapsCodec().decode,
        )
    return None

codecs.register(find_ola_k_ase)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='OLA O K ASE PROGRAMA EN '
                                                 'PYTHON O K ASE')
    parser.add_argument('infile', nargs=1, type=argparse.FileType('r'),
                        default=sys.stdin)
    args = parser.parse_args()
    text = args.infile[0].read()
    encoder = codecs.getencoder(OLA_K_ASE_CODEC)
    encoded_text, consumed = encoder(text)
    print "OLA K ASE"
    exec encoded_text
    print "O K ASE"
