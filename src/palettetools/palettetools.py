# -*- coding: utf-8 -*-

import requests as req
import ast
from constants import *

'''
	Tools for extracting/analyzing the color palette of an image hosted through imgix
	General usage: 

'''
def extract_colors_css(url):
	resp = req.get(url + PALETTE_URL_PARAM + 'css')
	resp.raise_for_status()
	css_str = resp.text

	for word in CSS_STRINGS:
		if(word not in css_str):
			raise Exception('Invalid imgix-url used, did not return an expected value')
			sys.exit(1)

	return css_str


def extract_colors_json(url):
	resp = req.get(url + PALETTE_URL_PARAM + 'json')
	resp.raise_for_status()

	try:
		json_obj = ast.literal_eval(resp.text)
	except Exception as err:
		raise Exception('Invalid imgix-url used, did not return an expected value')
		sys.exit(1)

	return json_obj

def overlay_text_color(url):
	resp = extract_colors_json(url)
	luminance = resp['average_luminance']

	if(luminance < .5):
		color = WHITE_HEX
	elif(luminance >= .5):
		color = BLACK_HEX

	return color