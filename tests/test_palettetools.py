
import palettetools as pt
import json
from test_palettetools_constants import *


def test_color_black():
    assert BLACK_HEX == '000'

def test_palette_css():
	#assert pt.extract_colors_css(IMG_BLUEHAT).find('.image-fg-1 { color:#0d0c10 !important; }\n') 
	#assert CSS_BLUEHAT.find(pt.extract_colors_css(IMG_BLUEHAT))
	#assert pt.extract_colors_css(IMG_BLUEHAT) == CSS_BLUEHAT
	
	assert pt.extract_colors_css(IMG_BLUEHAT).find(CSS_BLUEHAT)
	

def test_palette_json(): 
#	print(json.loads(pt.extract_colors_json(IMG_BLUEHAT)))
#	assert json.loads(pt.extract_colors_json(IMG_BLUEHAT)) == JSON_BLUEHAT
	assert pt.extract_colors_json(IMG_BLUEHAT) == JSON_BLUEHAT
