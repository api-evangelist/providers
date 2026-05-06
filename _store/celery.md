---
aid: celery
url: https://raw.githubusercontent.com/api-evangelist/celery/refs/heads/main/apis.yml
name: Celery
tags:
  - Asynchronous
  - Distributed Systems
  - Message Queue
  - Open Source
  - Python
  - Task Queue
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Open Source
created: '2024-01-15'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: Celery is an open-source distributed task queue for Python. It allows you to run tasks asynchronously in the background, enabling scalable distributed systems with support for multiple message brokers (RabbitMQ, Redis, Amazon SQS) and result backends. Celery provides a rich set of Python programming APIs for defining tasks, composing workflows, scheduling periodic work, executing on workers, and monitoring execution.
apis:
  - aid: celery:celery-task-api
    name: Celery Task API
    tags:
      - Python
      - Task Queue
      - Tasks
    humanURL: https://docs.celeryq.dev/en/stable/userguide/tasks.html
    properties:
      - url: https://docs.celeryq.dev/en/stable/userguide/tasks.html
        type: Documentation
      - url: https://docs.celeryq.dev/en/stable/reference/celery.app.task.html
        type: Reference
      - url: https://docs.celeryq.dev/en/stable/getting-started/
        type: GettingStarted
    description: Core API for defining and executing distributed tasks in Celery. Supports task decorators, retries, timeouts, rate limiting, and custom task classes.
  - aid: celery:celery-application-api
    name: Celery Application API
    tags:
      - Application
      - Configuration
    humanURL: https://docs.celeryq.dev/en/stable/userguide/application.html
    properties:
      - url: https://docs.celeryq.dev/en/stable/userguide/application.html
        type: Documentation
      - url: https://docs.celeryq.dev/en/stable/reference/celery.html
        type: Reference
      - url: https://docs.celeryq.dev/en/stable/userguide/configuration.html
        type: Configuration
    description: Application configuration and initialization API for Celery, used to configure brokers, result backends, serialization, routing, and task discovery.
  - aid: celery:celery-canvas-api
    name: Celery Canvas API
    tags:
      - Workflows
      - Chains
      - Groups
      - Chords
    humanURL: https://docs.celeryq.dev/en/stable/userguide/canvas.html
    properties:
      - url: https://docs.celeryq.dev/en/stable/userguide/canvas.html
        type: Documentation
    description: Canvas is Celery's workflow composition API for building complex task orchestrations using signatures, chains, groups, chords, maps, starmaps, and chunks.
  - aid: celery:celery-beat-api
    name: Celery Beat API
    tags:
      - Scheduling
      - Periodic Tasks
    humanURL: https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
    properties:
      - url: https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html
        type: Documentation
      - url: https://docs.celeryq.dev/en/stable/reference/celery.beat.html
        type: Reference
    description: Celery Beat is the scheduler for periodic tasks, supporting crontab-style schedules, interval schedules, and solar schedules. It can also be backed by a database scheduler for dynamic schedules.
  - aid: celery:celery-worker-api
    name: Celery Worker API
    tags:
      - Worker
      - Execution
      - Concurrency
    humanURL: https://docs.celeryq.dev/en/stable/userguide/workers.html
    properties:
      - url: https://docs.celeryq.dev/en/stable/userguide/workers.html
        type: Documentation
      - url: https://docs.celeryq.dev/en/stable/reference/celery.worker.html
        type: Reference
    description: Worker API for executing distributed tasks with configurable concurrency (prefork, gevent, eventlet, solo, threads), autoscaling, remote control, and signal handling.
  - aid: celery:celery-result-api
    name: Celery Result Backend API
    tags:
      - Results
      - State
      - Storage
    humanURL: https://docs.celeryq.dev/en/stable/userguide/tasks.html#result-backends
    properties:
      - url: https://docs.celeryq.dev/en/stable/userguide/tasks.html#result-backends
        type: Documentation
      - url: https://docs.celeryq.dev/en/stable/reference/celery.result.html
        type: Reference
    description: Result backend API for storing and retrieving task results and state using backends such as Redis, RPC, database, Memcached, Cassandra, and S3.
  - aid: celery:celery-signals-api
    name: Celery Signals API
    tags:
      - Signals
      - Events
      - Extensions
    humanURL: https://docs.celeryq.dev/en/stable/userguide/signals.html
    properties:
      - url: https://docs.celeryq.dev/en/stable/userguide/signals.html
        type: Documentation
      - url: https://docs.celeryq.dev/en/stable/reference/celery.signals.html
        type: Reference
    description: Signals API for hooking into Celery lifecycle events including task, worker, beat, and consumer signals to build extensions and observability.
  - aid: celery:celery-monitoring-api
    name: Celery Monitoring and Events API
    tags:
      - Monitoring
      - Events
      - Observability
    humanURL: https://docs.celeryq.dev/en/stable/userguide/monitoring.html
    properties:
      - url: https://docs.celeryq.dev/en/stable/userguide/monitoring.html
        type: Documentation
      - url: https://docs.celeryq.dev/en/stable/reference/celery.events.html
        type: Reference
    description: Event streaming and monitoring API for inspecting workers, tasks, and queues. Supports the curses-based celery events monitor and third-party tools such as Flower.
common:
  - type: Website
    url: https://docs.celeryq.dev/
  - type: Documentation
    url: https://docs.celeryq.dev/en/stable/
  - type: Reference
    url: https://docs.celeryq.dev/en/stable/reference/index.html
  - type: GettingStarted
    url: https://docs.celeryq.dev/en/stable/getting-started/
  - type: GitHub
    url: https://github.com/celery/celery
  - type: PyPI
    url: https://pypi.org/project/celery/
  - type: ChangeLog
    url: https://docs.celeryq.dev/en/stable/changelog.html
  - type: Community
    url: https://github.com/celery/celery/discussions
  - type: Issues
    url: https://github.com/celery/celery/issues
  - type: Contributing
    url: https://docs.celeryq.dev/en/stable/contributing.html
  - type: License
    url: https://github.com/celery/celery/blob/main/LICENSE
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
