
from app import app
from app import r
from app import q

from flask import render_template, request

from app.tasks import count_words
from time import strftime

@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    jobs = q.jobs  # Get a list of jobs in the queue
    message = None

    if request.args:  # Only run if a query string is sent in the request

        url = request.args.get("url")  # Gets the URL coming in as a query string

        task = q.enqueue(count_words, url)  # Send a job to the task queue

        jobs = q.jobs  # Get a list of jobs in the queue

        q_len = len(q)  # Get the queue length

        message = f"Task queued at {task.enqueued_at.strftime('%a, %d %b %Y %H:%M:%S')}. {q_len} jobs queued"

    return render_template("add_task.html", message=message, jobs=jobs)