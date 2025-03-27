# 🎓 Dong Hwa University GPA Converter: 4.5 Scale → 4.0 Scale

Follow these steps to run the GPA conversion tool locally on your machine:

## 🚀 Getting Started

### 📌 Clone the Repository
First, clone this repo:
```bash
git clone https://github.com/wilsonchang17/WES_GPA
```

### 📦 Install Dependencies
Navigate into the cloned directory and install required packages:
```bash
pip install -r requirements.txt
```

### 🌐 Set Up ChromeDriver
- Download ChromeDriver [here](https://chromedriver.chromium.org/).
- Ensure your ChromeDriver version matches your Chrome browser version.

### ⚙️ Configure `gpa.py`
- Open `gpa.py` and comment out (disable) the following code block:

```python
"""
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
"""
```

- Then, remove the comment from the following line and update the path with your ChromeDriver location:

```python
#browser = webdriver.Chrome("D:/google_download/chromedriver_win32/chromedriver.exe")
```
Change it to:
```python
browser = webdriver.Chrome("your_chromedriver_path")
```

Replace `your_chromedriver_path` with the actual path where your ChromeDriver executable is located.

### ▶️ Run the Application
- Open `app.py` and run the script.
```bash
python app.py
```
- After execution, you'll see a message similar to:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

- Click on the provided URL to open the application locally in your browser. 🌟

## 🌍 Live Demo on Heroku
- You can also use the deployed version of this GPA converter [here on Heroku](https://wesgpa.herokuapp.com/) 🚀✨



# 幫助東華的學生將學校4.5 Scale的GPA轉換為 4.0 的Scale
## 本地端使用方法如下
- 先把這個repo clone下來
```
git clone https://github.com/wilsonchang17/WES_GPA
```
- 安裝套件
```
pip install -r requirements.txt
```
- 安裝ChromeDriver，記得確認ChromeDriver的版本要跟你目前的Chrome一樣，[這裡下載](https://chromedriver.chromium.org/)
- 打開gpa.py，把以下程式碼像下方這樣註解掉
```python
"""
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
"""
```
- 繼續在gpa.py裡面，移除以下註解，並將路徑更改成剛剛下載ChromeDriver的路徑
```python
#browser = webdriver.Chrome("D:/google_download/chromedriver_win32/chromedriver.exe")
變成
browser = webdriver.Chrome("你的路徑")
```
- 打開app.py並執行
- 執行後會出現* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)，點及該網址打開本地端網頁(詳細網址可能不同)
## 部屬到Heroku的網站在這:[點我](https://wesgpa.herokuapp.com/)
