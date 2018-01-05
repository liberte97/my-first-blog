import pyqrcode
url = pyqrcode.create('google.co.kr')
url.svg('_url.svg', scale = 8)
url.eps('_url.eps', scale = 2)
