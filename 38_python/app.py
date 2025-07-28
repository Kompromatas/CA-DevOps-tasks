from flask import Flask, render_template
import datetime
import logging
import sys

# Setup logging configuration
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

setup_logging()

app = Flask(__name__)

@app.route('/')
def show_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Accessed / route. Returned date: {current_date}")
    return render_template("index.html", current_date=current_date)

@app.route('/health')
def health():
    logging.info("Health check accessed.")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
