---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 8
apis:
- description: Core API for defining and executing distributed tasks in Celery. Supports task decorators, retries, timeouts, rate limiting, and custom task classes.
  name: Celery Task API
  slug: celery-task-api
- description: Application configuration and initialization API for Celery, used to configure brokers, result backends, serialization, routing, and task discovery.
  name: Celery Application API
  slug: celery-application-api
- description: Canvas is Celery's workflow composition API for building complex task orchestrations using signatures, chains, groups, chords, maps, starmaps, and chunks.
  name: Celery Canvas API
  slug: celery-canvas-api
- description: Celery Beat is the scheduler for periodic tasks, supporting crontab-style schedules, interval schedules, and solar schedules. It can also be backed by a database scheduler for dynamic schedules.
  name: Celery Beat API
  slug: celery-beat-api
- description: Worker API for executing distributed tasks with configurable concurrency (prefork, gevent, eventlet, solo, threads), autoscaling, remote control, and signal handling.
  name: Celery Worker API
  slug: celery-worker-api
- description: Result backend API for storing and retrieving task results and state using backends such as Redis, RPC, database, Memcached, Cassandra, and S3.
  name: Celery Result Backend API
  slug: celery-result-api
- description: Signals API for hooking into Celery lifecycle events including task, worker, beat, and consumer signals to build extensions and observability.
  name: Celery Signals API
  slug: celery-signals-api
- description: Event streaming and monitoring API for inspecting workers, tasks, and queues. Supports the curses-based celery events monitor and third-party tools such as Flower.
  name: Celery Monitoring and Events API
  slug: celery-monitoring-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.celeryq.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.celeryq.dev/en/stable/
- group: docs
  title: ''
  type: Reference
  url: https://docs.celeryq.dev/en/stable/reference/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.celeryq.dev/en/stable/getting-started/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/celery/celery
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/celery/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.celeryq.dev/en/stable/changelog.html
- group: operate
  title: ''
  type: Community
  url: https://github.com/celery/celery/discussions
- group: operate
  title: ''
  type: Issues
  url: https://github.com/celery/celery/issues
- group: other
  title: ''
  type: Contributing
  url: https://docs.celeryq.dev/en/stable/contributing.html
- group: commercial
  title: ''
  type: License
  url: https://github.com/celery/celery/blob/main/LICENSE
created: '2024-01-15'
description: Celery is an open-source distributed task queue for Python. It allows you to run tasks asynchronously in the background, enabling scalable distributed systems with support for multiple message brokers (RabbitMQ, Redis, Amazon SQS) and result backends. Celery provides a rich set of Python programming APIs for defining tasks, composing workflows, scheduling periodic work, executing on workers, and monitoring execution.
finops:
- name: Celery Finops
  service_category: API
  slug: celery-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/celery.png
layout: provider
modified: '2026-04-23'
name: Celery
nav: Providers
network: true
overview: 'Celery publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Asynchronous, Distributed Systems, Message Queue, Open Source, and Python.


  Celery''s developer surface includes documentation, getting-started guide, GitHub presence, changelog, and 8 more developer resources.'
plans:
- name: Celery Plans Pricing
  plan_count: 3
  slug: celery-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Celery Rate Limits
  slug: celery-rate-limits
score:
  band: emerging
  composite: 27.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 27.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/celery/refs/heads/main/screenshots/celery-2026-06-20T174110.png
security:
- kind: domain-security
  name: Celery Domain Security
  slug: celery-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: celery
tags:
- Asynchronous
- Distributed Systems
- Message Queue
- Open Source
- Python
- Task Queue
website: https://docs.celeryq.dev/
---
