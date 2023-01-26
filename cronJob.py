from flask import Flask, render_template, send_file
import subprocess
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

import markdown
import markdown.extensions.fenced_code

app = Flask(__name__)

# Scheduler Jobs
def run_ai():
    # subprocess.run(["python", "AITradingbot.ipynb"])
    print("do_something is being executed.")

# # schedule.every().day.at("10:30").do(run_ai)
# # schedule.every(3).seconds.do(run_ai)
sched = BackgroundScheduler(daemon=True)
sched.add_job(run_ai,'interval',seconds=3)
sched.start()

# Api Routes
@app.route('/')
def home():
    readme_file = open('README.md', 'r')
    md_template_string = markdown.markdown(readme_file.read(), extensions=["fenced_code"])
    return md_template_string

@app.route('/time', methods=['GET'])
def getCurrentTime():
    return '<h2> TimeStamp: '+str(datetime.datetime.now())+'</h2>'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
    app.run()