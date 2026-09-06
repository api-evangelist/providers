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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-05'
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
artifact_total: 15
asyncapis:
- description: 'Celery workers publish a monitoring event stream over the configured broker. This document is a faithful transcription of the published Event Reference in the Celery Monitoring and Management Guide — '
  name: Celery Worker Event Stream
  slug: celery-events-asyncapi
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/celery
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/celery/ceps
- group: auth
  title: ''
  type: Security
  url: https://github.com/celery/celery/security/policy
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.celeryq.dev/en/stable/internals/deprecation.html
- group: build
  title: ''
  type: Packages
  url: packages/celery-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/celery-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/celery-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/celery-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/celery-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/celery-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/celery-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/celery-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/celery-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/celery-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/celery-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/celery-events-asyncapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/celery-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/celery-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/celery-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/celery-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/celery-finops.yml
created: '2024-01-15'
description: Celery is an open-source distributed task queue for Python. It allows you to run tasks asynchronously in the background, enabling scalable distributed systems with support for multiple message brokers (RabbitMQ, Redis, Amazon SQS) and result backends. Celery provides a rich set of Python programming APIs for defining tasks, composing workflows, scheduling periodic work, executing on workers, and monitoring execution.
finops:
- name: Celery Finops
  service_category: API
  slug: celery-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/celery.png
layout: provider
modified: '2026-09-05'
name: Celery
nav: Providers
network: true
overview: 'Celery publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Asynchronous, Distributed Systems, Message Queue, Open-Source, and Python.


  The Celery catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Celery''s developer surface includes documentation, getting-started guide, GitHub presence, changelog, CLI, authentication, sandbox, and 26 more developer resources.'
plans:
- name: Celery Plans Pricing
  plan_count: 0
  slug: celery-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Celery Rate Limits
  slug: celery-rate-limits
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.4
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 19.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/celery/refs/heads/main/screenshots/celery-2026-06-20T174110.png
security:
- kind: authentication
  name: Celery Authentication
  slug: celery-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Celery Domain Security
  slug: celery-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Celery Vulnerability Disclosure
  slug: celery-vulnerability-disclosure
  summary_line: Hackerone
slug: celery
tags:
- Asynchronous
- Distributed Systems
- Message Queue
- Open-Source
- Python
- Task Queue
website: https://docs.celeryq.dev/
---
