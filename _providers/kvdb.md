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
