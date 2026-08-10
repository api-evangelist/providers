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
api_count: 4
apis:
- description: Core Redis commands and data structure operations. Redis supports strings, hashes, lists, sets, sorted sets, streams, and more. The primary interface is the Redis Serialization Protocol (RESP) over TC
  name: Redis Core
  slug: redis-core
- description: The Redis Cloud REST API for managing subscriptions, databases, cloud accounts, access control, and logs on the Redis Cloud platform. Available at api.redislabs.com/v1 with API key authentication.
  name: Redis Cloud API
  slug: redis-cloud-api
- description: REST API for managing Redis Enterprise Software clusters. Provides endpoints for cluster configuration, database creation and management, user access control, and monitoring. Available at the cluster'
  name: Redis Enterprise API
  slug: redis-enterprise-api
- description: Redis Insight is a free GUI management tool for Redis. Provides database browsing, query execution, memory analysis, slow log inspection, and Redis Streams visualization. Available as a desktop app an
  name: Redis Insight
  slug: redis-insight
artifact_total: 36
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/redis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/redis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redis.io/
- group: docs
  title: ''
  type: Documentation
  url: https://redis.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/redis
- group: company
  title: ''
  type: Blog
  url: https://redis.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://redis.io/community/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redis/
- group: other
  title: ''
  type: X
  url: https://twitter.com/redisinc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Redisinc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redis.com/
- group: operate
  title: ''
  type: Support
  url: https://redis.io/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redis.io/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redis.io/legal/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://redis.io/docs/latest/commands/
- group: build
  title: ''
  type: SDKs
  url: https://redis.io/docs/latest/develop/connect/clients/
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/redis
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/redis/
- group: agent
  title: ''
  type: LlmsText
  url: https://redis.io/llms.txt
created: '2024-01-01'
description: Redis is an open source, in-memory data structure store used as a database, cache, message broker, and streaming engine. It supports strings, hashes, lists, sets, sorted sets, streams, JSON, and more. Redis is used by millions of developers for caching, session management, leaderboards, pub/sub messaging, real-time analytics, and event streaming. The Redis project is governed by the Redis Community and maintained by Redis Inc.
examples:
- key_count: 2
  name: Redis Hash Example
  slug: redis-hash-example
- key_count: 2
  name: Redis Set Get Example
  slug: redis-set-get-example
- key_count: 2
  name: Redis Sorted Set Example
  slug: redis-sorted-set-example
features:
- 'Free: 30 MB shared cloud DB'
- 'Essentials from $0.007/hr ($5/mo min): 250 MB-100 GB DB, SSO/RBAC'
- 'Pro from $0.014/hr ($200/mo min): dedicated, multi-region active-active'
- 'Enterprise: self-managed Redis Enterprise Software, hybrid, on-prem'
- 'Multi-cloud: AWS, GCP, Azure'
- Cloud API for cluster management at 60 req/min
- 'Redis Stack modules: RediSearch, RedisJSON, RedisGraph, RedisTimeSeries, RedisBloom'
- Vector similarity search (RediSearch)
- Redis Flex (RAM:Flash ratio for cost reduction)
- Auto-tiering for hot/cold data
- Active-active geo-distribution (Pro)
- Up to 99.999% uptime (Pro)
- Encryption in transit and at rest (Essentials+)
- Private connectivity (Pro)
- OAuth + API keys
- Open-source self-managed Redis OSS alternative
finops:
- name: Redis Finops
  service_category: Database / Cache
  slug: redis-finops
image: https://redis.io/images/redis-logo.png
json_schemas:
- name: Redis Command
  property_count: 8
  slug: redis-command
- name: Redis Key-Value Entry
  property_count: 5
  slug: redis-key-value
- name: Redis Server Info
  property_count: 19
  slug: redis-server-info
json_structures:
- name: Redis Key Value Structure
  property_count: 0
  slug: redis-key-value-structure
- name: Redis Server Info Structure
  property_count: 0
  slug: redis-server-info-structure
jsonld:
- class_count: 0
  name: Redis Context
  property_count: 3
  slug: redis-context
layout: provider
modified: '2026-05-04'
name: Redis
nav: Providers
network: true
overview: 'Redis publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cache, Database, In-Memory, Key-Value Store, and NoSQL.


  The Redis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Redis'' developer surface includes documentation, engineering blog, YouTube channel, support, and 16 more developer resources.'
plans:
- name: Redis Plans Pricing
  plan_count: 4
  slug: redis-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 4
  name: Redis Rate Limits
  slug: redis-rate-limits
rules:
- name: Redis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: redis-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.4
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 24.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 44.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/screenshots/redis-2026-06-20T192736.png
security:
- kind: domain-security
  name: Redis Domain Security
  slug: redis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Redis Vulnerability Disclosure
  slug: redis-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Redis Trust Center
  slug: redis-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR, CSA STAR
slug: redis
tags:
- Cache
- Database
- In-Memory
- Key-Value Store
- NoSQL
- Open Source
- Streaming
website: https://redis.io/
---
