VIEWER = evince
QRCODESTR = "https://t.me/mashhadlug"

all: out
	xelatex -output-directory=out poster.tex

out:
	mkdir out

view:
	${VIEWER} out/*.pdf

qrcode: assets/qrcode.png
	qrencode ${QRCODESTR} -o assets/qrcode.png -s 10 --foreground=000000 --background=FFFFFF00

