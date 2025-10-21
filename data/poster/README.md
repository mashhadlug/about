این پروژه شامل سورس LaTeX برای ساخت پوستر رسمی گروه کاربران لینوکس مشهد (مشهدلاگ) است.  
پوستر شامل لوگو، تصاویر پس‌زمینه و QR کد دعوت به کانال تلگرام می‌باشد.  
ساخت پوستر با XeLaTeX انجام می‌شود و خروجی PDF تولید می‌کند.  
QR کد به صورت خودکار با ابزار `qrencode` ساخته می‌شود.
این پوشه شامل Makefile برای ساخت و مشاهده آسان پوستر است.


پوستر مشهدلاگ با XeLaTeX ساخته می‌شود.

## پیش‌نیازها
```bash
sudo apt install texlive-xetex texlive-latex-extra texlive-lang-other qrencode make evince
````

## ساخت

```bash
make
```

## نمایش

```bash
make view
```

## ساخت QR کد

```bash
make qrcode
```

