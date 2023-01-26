from flask import Flask
from fetchStockService import calStockService
from dbService import DbConnection
import json

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

app = Flask(__name__)

# Scheduler Jobs
def runScheduler():
    data = json.load(open('stockList.json'))
    for stock in data['stocks']:
        print(stock)
        doc = calStockService(data['stocks'][stock])
        DbConnection().saveToDatabaseByBatch(doc['Time Series (5min)'], doc['Time Series (5min)'].keys(), data['stocks'][stock])

sched = BackgroundScheduler(daemon=True)
# trigger = CronTrigger(
#         year="*", month="*", day="*", hour="*", minute="*", second="*"
#     )
sched.add_job(runScheduler, 'interval', seconds=5)
sched.start()

if __name__ == '__main__':
    app.run(port=5000, debug=False)