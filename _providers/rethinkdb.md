---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: ReQL (RethinkDB Query Language) is the expressive query language exposed by RethinkDB through official client drivers. Drivers communicate with the RethinkDB server using a native JSON protocol over T
  name: RethinkDB ReQL Driver API
  slug: reql
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rethinkdb-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rethinkdb
- group: company
  title: ''
  type: Website
  url: https://rethinkdb.com
- group: docs
  title: ''
  type: Documentation
  url: https://rethinkdb.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rethinkdb.com/api
- group: other
  title: ''
  type: Download
  url: https://rethinkdb.com/docs/install/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rethinkdb
- group: build
  title: ''
  type: Source Code
  url: https://github.com/rethinkdb/rethinkdb
- group: docs
  title: ''
  type: Documentation Source
  url: https://github.com/rethinkdb/docs
- group: operate
  title: ''
  type: Community
  url: https://rethinkdb.com/community/
- group: commercial
  title: ''
  type: License
  url: https://github.com/rethinkdb/rethinkdb/blob/next/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://rethinkdb.com/blog
created: '2026-05-11'
description: RethinkDB is an open source, distributed document-oriented NoSQL database designed for real-time applications, with push-based change feeds, native JSON storage, and an expressive query language called ReQL. Applications interact with RethinkDB through official client drivers (JavaScript, Python, Java, Ruby) that speak the native JSON driver protocol over TCP, rather than through an HTTP REST API. ReQL also includes an r.http command that lets queries pull data from external HTTP APIs directly.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rethinkdb.png
layout: provider
modified: '2026-05-11'
name: RethinkDB
nav: Providers
network: true
overview: 'RethinkDB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, NoSQL, Document Database, Real-Time, and Open-Source.


  RethinkDB''s developer surface includes documentation, API reference, engineering blog, and 9 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rethinkdb/refs/heads/main/screenshots/rethinkdb-2026-06-20T193037.png
security:
- kind: domain-security
  name: Rethinkdb Domain Security
  slug: rethinkdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rethinkdb
tags:
- Database
- NoSQL
- Document Database
- Real-Time
- Open-Source
- Change Feeds
- ReQL
website: https://rethinkdb.com
---
