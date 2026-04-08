---
aid: celery
url: https://raw.githubusercontent.com/api-evangelist/celery/refs/heads/main/apis.yml
apis:
- aid: celery:celery-task-api
  name: Celery Task API
  tags:
  - Python
  - Task Queue
  humanURL: https://docs.celeryq.dev/en/stable/userguide/tasks.html
  properties:
  - url: https://docs.celeryq.dev/en/stable/
    type: Documentation
  - url: https://docs.celeryq.dev/en/stable/getting-started/
    type: Getting Started
  description: Core API for defining and executing distributed tasks in Celery.
name: Celery
tags:
- Asynchronous
- Distributed Systems
- Message Queue
- Python
- Task Queue
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Celery is a distributed task queue for Python. It allows you to run tasks asynchronously in the background, enabling you to build scalable distributed systems with ease. Celery supports multiple message brokers including RabbitMQ and Redis.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

