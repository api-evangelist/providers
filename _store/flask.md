---
aid: flask
name: Flask
description: Flask is a lightweight WSGI web application framework for Python, designed to make getting started quick and easy with the ability to scale up to complex applications. It provides a simple core with Jinja2 templating and Werkzeug WSGI toolkit, and is extensible through a rich ecosystem of extensions for database integration, form validation, authentication, and more. Flask is a popular foundation for building APIs and web services in Python.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Open Source
position: Producer
tags:
  - Frameworks
  - Lightweight
  - Microframework
  - Pallets
  - Python
  - Web Framework
  - WSGI
url: https://raw.githubusercontent.com/api-evangelist/flask/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: flask:flask
    name: Flask
    description: Flask is a lightweight WSGI web application framework for Python. It is commonly used as a foundation for building HTTP APIs and web services. While Flask itself does not expose an HTTP API, it ships with a configurable runtime whose configuration surface is captured here as a JSON Schema for tooling and validation purposes.
    humanURL: https://flask.palletsprojects.com/
    tags:
      - Frameworks
      - Lightweight
      - Microframework
      - Pallets
      - Python
      - Web Framework
      - WSGI
    properties:
      - type: Documentation
        url: https://flask.palletsprojects.com/en/stable/
      - type: GettingStarted
        url: https://flask.palletsprojects.com/en/stable/quickstart/
      - type: SourceCode
        url: https://github.com/pallets/flask
      - type: JSONSchema
        url: json-schema/flask-config.json
common:
  - type: Website
    url: https://flask.palletsprojects.com/
  - type: Documentation
    url: https://flask.palletsprojects.com/en/stable/
  - type: GettingStarted
    url: https://flask.palletsprojects.com/en/stable/quickstart/
  - type: GitHubOrganization
    url: https://github.com/pallets
  - type: SourceCode
    url: https://github.com/pallets/flask
  - type: Blog
    url: https://palletsprojects.com/blog/
  - type: PyPI
    url: https://pypi.org/project/flask/
  - type: Extensions
    url: https://flask.palletsprojects.com/en/stable/extensions/
  - type: ChangeLog
    url: https://flask.palletsprojects.com/en/stable/changes/
  - type: License
    url: https://github.com/pallets/flask/blob/main/LICENSE.txt
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
