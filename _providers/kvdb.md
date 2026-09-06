---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Kvdb Agentic Access
  operation_count: 10
  slug: kvdb-agentic-access
  summary_line: 10 operations · 7 acting
api_count: 1
apis:
- baseURL: https://kvdb.io
  baseurl_source: spec
  description: Bucket lifecycle operations
  name: KVdb Buckets API
  slug: kvdb-buckets-api
- baseURL: https://kvdb.io
  baseurl_source: spec
  description: Key-value operations within a bucket
  name: KVdb Keys API
  slug: kvdb-keys-api
- baseURL: https://kvdb.io
  baseurl_source: spec
  description: Custom Lua script management and execution
  name: KVdb Scripts API
  slug: kvdb-scripts-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KVdb Buckets API
  slug: open-kvdb-buckets-api
- collection_type: open
  name: KVdb Buckets Keys API
  slug: open-kvdb-keys-api
- collection_type: open
  name: KVdb Buckets Scripts API
  slug: open-kvdb-scripts-api
- collection_type: open
  name: KVdb API
  slug: open-kvdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kvdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kvdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kvdb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://kvdb.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kvdb.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.kvdb.io/feed.rss
created: '2025-02-08'
description: Stop wasting time setting up NoSQL databases. KVdb is a hosted serverless key-value database with a simple HTTPS REST API. Buckets act as namespaces for keys, with built-in access control via secret, read, and write keys, custom Lua scripts, and per-bucket TTLs.
finops:
- name: Kvdb Finops
  service_category: API
  slug: kvdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kvdb.png
layout: provider
modified: '2026-05-19'
name: KVdb
nav: Providers
network: true
overview: 'KVdb publishes 3 APIs on the [APIs.io](https://apis.io/) network: Buckets API, Keys API, and Scripts API. Tagged areas include Databases, Key-Value, NoSQL, and Serverless.


  KVdb''s developer surface includes authentication, documentation, engineering blog, and 3 more developer resources.'
plans:
- name: Kvdb Plans Pricing
  plan_count: 3
  slug: kvdb-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Kvdb Rate Limits
  slug: kvdb-rate-limits
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 35.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kvdb/refs/heads/main/screenshots/kvdb-2026-06-20T184222.png
security:
- kind: authentication
  name: Kvdb Authentication
  slug: kvdb-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kvdb Domain Security
  slug: kvdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kvdb
tags:
- Databases
- Key-Value
- NoSQL
- Serverless
website: https://kvdb.io/
---
