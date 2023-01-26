from flask import Flask, render_template, send_file
import datetime
import markdown
import markdown.extensions.fenced_code
from app.fetchStockService import calStockService

app = Flask(__name__)

# Scheduler Jobs
# def run_ai():
#     # subprocess.run(["python", "AITradingbot.ipynb"])
#     print("do_something is being executed.")

# # # schedule.every().day.at("10:30").do(run_ai)
# # # schedule.every(3).seconds.do(run_ai)
# sched = BackgroundScheduler(daemon=True)
# sched.add_job(run_ai,'interval',seconds=3)
# sched.start()

# Api Routes
@app.route('/')
def home():
    return '<h2>Bot</h2>'

@app.route('/stock/<stockExchange>/<stock>', methods=['GET'])
def getStock(stockExchange, stock):
    # calStockService(stockExchange + ':' + stock)
    return calStockService()
    # return 'Stock : ' + stockExchange + ':' + stock

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
    app.run(port=8000, debug=False)