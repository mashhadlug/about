VIEWER = evince
QRCODESTR = "https://nshn.ir/e8sb1-tP2JFB8u"
EVENT_NUMBER =

all: build build-png

out:
	mkdir out

build: out out/poster.pdf

view:
	${VIEWER} out/*.pdf

qrcode: assets/qrcode.png
	qrencode ${QRCODESTR} -o assets/qrcode.png -s 10 --foreground=000000 --background=FFFFFF00

out/poster.pdf: poster.tex qrcode
	xelatex -output-directory=out poster.tex

build-png: out/poster.pdf
	pdftoppm -png -rx 300 -ry 300 out/poster.pdf -o poster
	mv poster-1.png poster-${EVENT_NUMBER}.png


