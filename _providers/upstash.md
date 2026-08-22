---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Upstash Agentic Access
  operation_count: 10
  slug: upstash-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 7
apis:
- description: Management API for creating and administering Upstash Redis, Kafka, and Vector databases, teams, and account resources. Uses HTTP Basic authentication with email and API key credentials.
  name: Upstash Developer API
  slug: developer-api
- description: Per-database REST API for executing Redis commands over HTTPS from edge and serverless runtimes. Uses Bearer token authentication scoped to individual Redis databases.
  name: Upstash Redis REST API
  slug: redis-rest-api
- description: Kafka cluster and topic management
  name: Upstash Kafka API
  slug: upstash-kafka-api
- description: Redis database management
  name: Upstash Redis API
  slug: upstash-redis-api
- description: Per-database Redis command execution
  name: Upstash RedisCommand API
  slug: upstash-rediscommand-api
- description: Team and member management
  name: Upstash Teams API
  slug: upstash-teams-api
- description: Vector index management
  name: Upstash Vector API
  slug: upstash-vector-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Upstash APIs Kafka API
  slug: open-upstash-kafka-api
- collection_type: open
  name: Upstash APIs Kafka Redis API
  slug: open-upstash-redis-api
- collection_type: open
  name: Upstash APIs Kafka RedisCommand API
  slug: open-upstash-rediscommand-api
- collection_type: open
  name: Upstash APIs Kafka Teams API
  slug: open-upstash-teams-api
- collection_type: open
  name: Upstash APIs Kafka Vector API
  slug: open-upstash-vector-api
- collection_type: open
  name: Upstash APIs
  slug: open-upstash
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upstash-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upstash-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upstash-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upstash
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upstash
- group: company
  title: ''
  type: Website
  url: https://upstash.com
- group: docs
  title: ''
  type: Documentation
  url: https://upstash.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://upstash.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://console.upstash.com
- group: agent
  title: ''
  type: LlmsText
  url: https://upstash.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://upstash.com/blog/feed.xml
created: '2026-05-11'
description: Upstash provides serverless data platforms including managed Redis, Kafka, QStash messaging, and Vector databases optimized for serverless and edge applications with per-request pricing. The platform offers low-latency global replication, REST APIs for stateless access from edge runtimes, and SDKs for popular serverless frameworks. The Upstash Developer API enables programmatic management of databases, teams, and account resources using HTTP Basic authentication (email + API key).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upstash.png
layout: provider
modified: '2026-05-11'
name: Upstash
nav: Providers
network: true
overview: 'Upstash publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Kafka API, Redis API, RedisCommand API, and 2 more. Tagged areas include Serverless, Redis, Kafka, Messaging, and Vector Database.


  Upstash''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 31.1
  delta: -0.8
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 52.3
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upstash/refs/heads/main/screenshots/upstash-2026-06-20T200514.png
security:
- kind: authentication
  name: Upstash Authentication
  slug: upstash-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Upstash Domain Security
  slug: upstash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upstash
tags:
- Serverless
- Redis
- Kafka
- Messaging
- Vector Database
- Edge Computing
website: https://upstash.com
---
