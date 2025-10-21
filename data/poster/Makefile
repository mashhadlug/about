VIEWER = evince
QRCODESTR = "https://t.me/mashhadlug"

all: out out/poster.pdf

out:
	mkdir out

view:
	${VIEWER} out/*.pdf

qrcode: assets/qrcode.png
	qrencode ${QRCODESTR} -o assets/qrcode.png -s 10 --foreground=000000 --background=FFFFFF00

out/poster.pdf:
	xelatex -output-directory=out poster.tex

build-png: out/poster.pdf
	pdftoppm -png -rx 300 -ry 300 out/poster.pdf -o poster
	mv poster-1.png poster.png


