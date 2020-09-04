#Document link1:https://luma-led-matrix.readthedocs.io/en/latest/api-documentation.html
#Document link2:https://pillow.readthedocs.io/en/latest/reference/Image.html
#Document link3:https://blog.csdn.net/zyaiwmy/article/details/70224250
#Please install luma.led_matrix first.See the installation guide in Document link3 
import re
import time
import argparse
import PIL
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
im = PIL.Image.open("pro.jpg")
lim = im.convert('1')
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=7, block_orientation=-90,contrast=5)

device.display(lim)

time.sleep(5)
device.clear() 