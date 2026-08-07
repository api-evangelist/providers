---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Quix Agentic Access
  operation_count: 16
  slug: quix-agentic-access
  summary_line: 16 operations · 11 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Subscribe to live parameter data, events, definitions, active streams, topic metrics, and raw packages from Quix topics in real time over a Microsoft SignalR hub (WebSockets, with Long Polling fallbac
  name: Quix Streaming Reader API (Real-time)
  slug: streaming-reader-api
- description: Apache 2.0 open source Python library (pip install quixstreams) for building containerized stream-processing applications on Apache Kafka, using a declarative StreamingDataFrame and an Application run
  name: Quix Streams (Open Source)
  slug: quix-streams-oss
- description: Declare parameter and event metadata for a stream (Streaming Writer API).
  name: Quix Definitions API
  slug: quix-definitions-api
- description: Manage and monitor service deployments (Portal API).
  name: Quix Deployments API
  slug: quix-deployments-api
- description: Publish discrete events into a stream (Streaming Writer API).
  name: Quix Event Data API
  slug: quix-event-data-api
- description: Publish time-series parameter data into a stream (Streaming Writer API).
  name: Quix Parameter Data API
  slug: quix-parameter-data-api
- description: Create and close streams within a topic (Streaming Writer API).
  name: Quix Streams API
  slug: quix-streams-api
- description: Manage Kafka topics in a workspace (Portal API).
  name: Quix Topics API
  slug: quix-topics-api
- description: Manage Quix Cloud workspaces / environments (Portal API).
  name: Quix Workspaces API
  slug: quix-workspaces-api
artifact_total: 18
asyncapis:
- description: AsyncAPI 2.6 description of the Quix **Streaming Reader API**, a real-time, bidirectional surface delivered over a **Microsoft SignalR hub**. SignalR negotiates the best available transport and, for t
  name: Quix Streaming Reader API (SignalR / WebSocket)
  slug: quix-asyncapi
collections:
- collection_type: open
  name: Quix Cloud HTTP APIs
  slug: open-quix
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quix-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quixio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quix
- group: company
  title: ''
  type: Website
  url: https://quix.io/
- group: docs
  title: ''
  type: Documentation
  url: https://quix.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/quix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/quix-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://quix.io/blog
created: '2026-06-21'
description: Quix is a Python-native stream-processing platform for real-time data and ML. It pairs Quix Streams - an open source (Apache 2.0) Python library for building containerized stream-processing applications on Apache Kafka - with Quix Cloud, a fully managed platform offering managed Kafka, Kubernetes deployments, and a set of HTTP and SignalR/WebSocket APIs for writing data in, reading data out in real time, and managing workspaces, topics, and deployments.
finops:
- name: Quix Finops
  service_category: Analytics
  slug: quix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quix.png
layout: provider
modified: '2026-06-21'
name: Quix
nav: Providers
network: true
overview: 'Quix publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Streaming Reader API (Real-time), Definitions API, Deployments API, and 5 more. Tagged areas include Stream Processing, Real Time, Kafka, Python, and Streaming Data.


  The Quix catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Quix''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Quix Plans Pricing
  plan_count: 4
  slug: quix-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Quix Rate Limits
  slug: quix-rate-limits
rules:
- name: Quix API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: quix-asyncapi-spectral-rules
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Quix Authentication
  slug: quix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quix Domain Security
  slug: quix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quix
tags:
- Stream Processing
- Real Time
- Kafka
- Python
- Streaming Data
website: https://quix.io/
---
