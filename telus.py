# Default ESSID is ZyXELXXXXX
# https://www.ebay.com/itm/154987272276?hash=item2415f61854:g:0mkAAOSw7jJieWgr
# Zyxel SBG3500-N000
import hashlib
import argparse

def SBG3500(serial):

	junk = 'agnahaakeaksalmaltalvandanearmaskaspattbagbakbiebilbitblableblib'\
	'lyboabodbokbolbomborbrabrobrubudbuedaldamdegderdetdindisdraduedu'\
	'kdundypeggeieeikelgelvemueneengennertesseteettfeifemfilfinflofly'\
	'forfotfrafrifusfyrgengirglagregrogrygulhaihamhanhavheihelherhith'\
	'ivhoshovhuehukhunhushvaideildileinnionisejagjegjetjodjusjuvkaika'\
	'mkankarkleklikloknaknekokkorkrokrykulkunkurladlaglamlavletlimlin'\
	'livlomloslovluelunlurlutlydlynlyrlysmaimalmatmedmegmelmenmermilm'\
	'inmotmurmyemykmyrnamnednesnoknyenysoboobsoddodeoppordormoseospos'\
	'sostovnpaiparpekpenpepperpippopradrakramrarrasremrenrevrikrimrir'\
	'risrivromroprorrosrovrursagsaksalsausegseiselsensessilsinsivsjus'\
	'jyskiskoskysmisnesnusolsomsotspastistosumsussydsylsynsyvtaktalta'\
	'mtautidtietiltjatogtomtretuetunturukeullulvungurourtutevarvedveg'\
	'veivelvevvidvikvisvriyreyte'

	md5 = hashlib.md5()
	md5.update(serial.encode())

	p = ""
	summ = 0
	for b in md5.digest():
		d1 = hex(b)[2:].upper()
		if len(d1) == 1:
			d1 += d1
		p += d1
	summ = sum([ord(char) for char in p])
	i = summ % 265
	if summ & 1:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:]
	else:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:].upper()

	s2 = "%s%s%s%s%s%s%s" % (p[0], s1[0:2], p[1:3], s1[2:4], p[3:6], s1[4:6], p[6:])

	md52 = hashlib.md5()
	md52.update(s2.encode())
	hex_digest = ""
	for b in md52.digest():
		d2 = hex(b)[2:].upper()
		if len(d2) == 1:
			d2 += d2
		hex_digest += d2

	# Seems as though the 3rd MD5 round is not needed at the moment
	# s3 = "%s%s%s%s%s%s%s%s%s%s%s%s%s" % (hex_digest[5], s1[3], s1[1], hex_digest[4], hex_digest[3], s1[0], s1[5], hex_digest[2], hex_digest[1], hex_digest[0], s1[1], s1[4], hex_digest[6:])

	# md53 = hashlib.md5()
	# md52.update(s3.encode())
	# hex_digest3 = ""
	# for b in md53.digest():
	# 	d3 = hex(b)[2:].upper()
	# 	if len(d3) == 1:
	# 		d3 += d3
	# 	hex_digest3 += d3

	filler = "AD3EHKL6V5XY9PQRSTUGN2CJW4FM7Z"
	filler_mod = 30

	hex_digest_old = hex_digest
	for i in range(6, 16):
		if hex_digest[i] == "0" or hex_digest[i] == "1":
			if i == "6":
				ascii_sum = ord(hex_digest_old[31]) + ord(hex_digest_old[0]) + ord(hex_digest_old[1])
			else:
				ascii_sum = ord(hex_digest_old[i-7]) + ord(hex_digest_old[i-6]) + ord(hex_digest_old[i-5])
			replacement = filler[ascii_sum % filler_mod]
			hex_digest = "%s%s%s" % (hex_digest[:i], replacement, hex_digest[i+1:])
	key = hex_digest[6:16].lower()
	print(key)


parser = argparse.ArgumentParser(description='Turkey Zyxel Keygen. (Zyxel VMG3312-B10B and VGM3313-B10A)')
parser.add_argument('serial', help='Serial Number')
args = parser.parse_args()

SBG3500(args.serial)
