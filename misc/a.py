from s import *
import argparse

parser = argparse.ArgumentParser(description='Automate our class')

parser.add_argument('--path', help='The path that is to be scrapped')
parser.add_argument('-p', type=bool, default=False, help='Flag the controls if the class should print or not')

args = parser.parse_args()
x = dirScrapper()
x.setPath(args.path)
x.scrap()
if(args.p):
	print(x)