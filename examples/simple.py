#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>


"""

import os
from flask import Flask
from flask_tat.engine import TATClient

os.environ.setdefault('TAT_URL', 'http://127.0.0.1')
os.environ.setdefault('TAT_USERNAME', 'test')
os.environ.setdefault('TAT_PASSWORD', 'test')
os.environ.setdefault("TAT_TOPIC", "MyTopic")

app = Flask(__name__)
app.config.update(dict(
    TAT_URL=os.getenv('TAT_URL'),
    TAT_USERNAME=os.getenv('TAT_USERNAME'),
    TAT_PASSWORD=os.getenv('TAT_PASSWORD'),
))
app.app_context().push()

tat_client = TATClient(app)
print(tat_client.message_list(
    topic=os.getenv('TAT_TOPIC'),
    limit=5
))
