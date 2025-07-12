import webbrowser

html_content = """
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <title>مهلا جون 🤍</title>
    <style>
        body {
            direction: rtl;
            text-align: center;
            background-color: white;
            font-family: Tahoma, sans-serif;
            color: #333;
            padding-top: 100px;
        }
        .box {
            background: rgba(255, 255, 255, 0.8);
            padding: 30px;
            border-radius: 20px;
            display: inline-block;
            box-shadow: 0 0 10px #ccc;
        }
        h1 {
            color: #d81b60;
            font-size: 36px;
        }
        p {
            font-size: 20px;
        }
        button {
            margin-top: 20px;
            font-size: 18px;
            padding: 10px 20px;
            border: none;
            background-color: #f8bbd0;
            border-radius: 10px;
            cursor: pointer;
        }
        button:hover {
            background-color: #f48fb1;
        }
        #secret {
            display: none;
            margin-top: 20px;
            font-size: 22px;
            color: #c2185b;
        }
    </style>
</head>
<body>

    <audio autoplay loop>
        <source src="sezen_aksu_sen_aglama.mp3" type="audio/mpeg">
        مرورگرت از پخش موزیک پشتیبانی نمی‌کند.
    </audio>

    <div class="box">
        <h1>مهلا خانومممممممم 🤍</h1>
        <p>تو مثل گل سفید پاک و نابی... همیشه توی دلمی 💕</p>

        <button onclick="document.getElementById('secret').style.display='block'">👀 فشار بده</button>
        <p id="secret">مهلا جون، اگه بدونی چقدر خوشگلی و خیلی خوبی (چشمات خیلی خوشگله)... ❤️</p>
    </div>

</body>
</html>
"""

# فایل HTML رو می‌سازیم
with open("mahlas_love.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# فایل رو با مرورگر باز می‌کنیم
webbrowser.open("mahlas_love.html")
