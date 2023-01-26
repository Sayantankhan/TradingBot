from flask import Flask
from app.fetchStockService import calStockService
from json

app = Flask(__name__)

# Scheduler Jobs
def runScheduler():
    data = json.load(open('stockList.json'))
    for stock in data[stock]:
        calStockService(stock)

# # schedule.every().day.at("10:30").do(run_ai)
# # schedule.every(3).seconds.do(run_ai)
sched = BackgroundScheduler(daemon=True)
sched.add_job(runScheduler,'interval',minutes=3)
sched.start()

if __name__ == '__main__':
    app.run(port=5000, debug=False)