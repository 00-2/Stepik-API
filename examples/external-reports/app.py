from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import item_report as itr
DEBUG = True

app = Flask(__name__,  template_folder='templates')
contest_table = itr.ContestTable(111634)
# if DEBUG:
#     df = []
#     for i in range(7):
#         step = pd.read_csv(f'test{i}.csv')
#         df.append(step)
#     contest_table._step_submissions = df
df = contest_table.get_step_submissions()
contesters = contest_table.get_contesters()
# if DEBUG:
#     for i, step in enumerate(df):
#         step.to_csv(f'test{i}.csv', encoding='utf-8')
df = [ step[['score']].to_dict() for step in df]
marks = dict()
for contestant in contesters:
    marks[contestant[0]] = []
for contestant in contesters:
    contestant = contestant[0]
    for step in df:
        if 'score' in step:
            if contestant in step['score']:
                marks[contestant].append(step['score'][contestant])
            else:
                marks[contestant].append(0)
# for contestant in marks:
#     print(contestant)
#     print(marks[contestant])
@app.route('/contesters', methods=("POST", "GET"))
def show_constesters():
    return render_template('table.html',  contesters = contesters, count_tasks = len(df), marks = marks)
if __name__ == '__main__':
    app.run(host='0.0.0.0')