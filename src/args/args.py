import argparse

def ft_args():
	parcel = argparse.ArgumentParser(description='stockholm es un ransomware', \
	epilog='version 1.0.0, author: dugonzal | Haz el mal con fines educativos.')
	parcel.add_argument('-v', '--version', action='version', version='%(prog)s | version: 1.0.0')
	parcel.add_argument('-r', '--reverse', action='store_true', help='descrypt the files')
	parcel.add_argument('-s', '--silent', action='store_true', help='descrypt the files without showing info')
	args = parcel.parse_args()
	return args
