import pytest
import palettetools as pt
import json
from test_palettetools_constants import *


def test_img1_palette_css():
	assert pt.extract_colors_css(IMG_BLUEHAT).find(CSS_BLUEHAT)

def test_img1_palette_json(): 
	assert pt.extract_colors_json(IMG_BLUEHAT) == JSON_BLUEHAT

def test_img1_color_overlay_BLACK():
	assert pt.overlay_text_color(IMG_BLUEHAT) == BLACK_HEX

def test_img2_palette_css():
	assert pt.extract_colors_css(IMG_PINE).find(CSS_PINE)

def test_img2_palette_json(): 
	assert pt.extract_colors_json(IMG_PINE) == JSON_PINE

def test_img2_color_overlay_WHITE():
	assert pt.overlay_text_color(IMG_PINE) == WHITE_HEX

def test_json_404_error():
	with pytest.raises(Exception):
		pt.extract_colors_json(BROKEN_URL)

def test_json_non_imgix_url():
	with pytest.raises(Exception):
		pt.extract_colors_json(INVALID_URL)

def test_css_404_error():
	with pytest.raises(Exception):
		pt.extract_colors_css(BROKEN_URL)

def test_css_non_imgix_url():
	with pytest.raises(Exception):
		pt.extract_colors_css(INVALID_URL)