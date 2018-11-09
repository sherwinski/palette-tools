# -*- coding: utf-8 -*-

import requests as req
import ast
from constants import *

'''
	Extract the color palette of the image from the imgix-url passed in
	
'''
def extract_colors(url, responseType):
	resp = req.get(url + PALETTE_URL_PARAM + responseType)
	return ast.literal_eval(resp.text)
	
def extract_colors_css(url):
	resp = req.get(url + PALETTE_URL_PARAM + 'css')
	return resp.text

def extract_colors_json(url):
	resp = req.get(url + PALETTE_URL_PARAM + 'json')
	return ast.literal_eval(resp.text)

def overlay_text_color(url):
	resp = extract_colors(url, JSON_STRING)
	luminance = resp['average_luminance']

	if(luminance < .5):
		color = WHITE_HEX
	elif(luminance >= .5):
		color = BLACK_HEX

	return color