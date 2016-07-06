#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>

"""
import json

import requests
import requests.exceptions

from flask_tat.exceptions import InternalServerError, MisdirectedRequest, \
    from_response


class HTTPClient(object):
    """RestClient"""

    def __init__(
            self, server, timeout=10, headers=None, username=None,
            password=None):
        self.server = server
        self.timeout = timeout
        self.headers = headers if headers else dict()
        self.auth = (username, password) if username and password else None

    def __repr__(self):
        return 'Connection: %s' % self.server

    def do_request(self, method, path, params=None, data=None):
        try:
            url = ''.join([self.server.rstrip('/'), path])
            response = requests.request(
                method=method,
                url=url,
                params=params,
                data=json.dumps(data) if data else None,
                auth=self.auth,
                headers=self.headers,
                timeout=self.timeout
            )
        except requests.exceptions.RequestException as e:
            raise InternalServerError(
                message=getattr(e, 'message', "Internal Server Error"),
                extra=dict(url=url)
            )

        if response is None:
            raise MisdirectedRequest(extra=dict(url=url))

        if response.status_code >= 300:
            raise from_response(response, url)

        try:
            return response.json()
        except:
            return response.text
