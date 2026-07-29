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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Riak Agentic Access
  operation_count: 25
  slug: riak-agentic-access
  summary_line: 25 operations · 11 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: RESTful HTTP API for Riak KV providing GET, PUT, POST, and DELETE access to buckets, objects, secondary indexes, search, MapReduce, and CRDT data types. Default port is 8098. Authentication and author
  name: Riak KV HTTP API
  slug: http-api
- description: Higher-performance binary client API for Riak KV using Protocol Buffers messages encoded over a long-lived TCP connection. Default port is 8087. Each request message produces one or more response mess
  name: Riak Protocol Buffers Client API
  slug: protocol-buffers
- description: The Mapred API from Riak KV — 1 operation(s) for mapred.
  name: Riak KV Mapred API
  slug: riak-mapred-api
- description: The Ping API from Riak KV — 1 operation(s) for ping.
  name: Riak KV Ping API
  slug: riak-ping-api
- description: The Riak KV HTTP API API from Riak KV — 1 operation(s) for riak kv http api.
  name: Riak KV Riak KV HTTP API API
  slug: riak-riak-kv-http-api-api
- description: The Search API from Riak KV — 4 operation(s) for search.
  name: Riak KV Search API
  slug: riak-search-api
- description: The Stats API from Riak KV — 1 operation(s) for stats.
  name: Riak KV Stats API
  slug: riak-stats-api
- description: The Types API from Riak KV — 7 operation(s) for types.
  name: Riak KV Types API
  slug: riak-types-api
artifact_total: 12
collections:
- collection_type: open
  name: Riak KV HTTP API
  slug: open-riak
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/riak-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riak-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/riak-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://riak.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.riak.com/riak/kv/latest/
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.riak.com/riak/kv/latest/developing/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/basho
- group: build
  title: ''
  type: Source Code
  url: https://github.com/basho/riak
- group: other
  title: ''
  type: Protocol Buffers Repo
  url: https://github.com/basho/riak_pb
- group: build
  title: ''
  type: Client Libraries
  url: https://docs.riak.com/riak/kv/latest/developing/client-libraries/
- group: other
  title: ''
  type: Download
  url: https://docs.riak.com/riak/kv/latest/setup/installing/
- group: commercial
  title: ''
  type: License
  url: https://github.com/basho/riak/blob/develop/LICENSE
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.riak.com/llms.txt
created: '2026-05-11'
description: 'Riak KV is a distributed NoSQL key-value database originally developed by Basho Technologies, designed for high availability, fault tolerance, and horizontal scalability across commodity hardware. Riak exposes two client-facing APIs: a RESTful HTTP API for basic GET, PUT, POST, and DELETE operations, and a higher-performance Protocol Buffers (PBC) API spoken over TCP. Both APIs support buckets, objects, secondary indexes, search, MapReduce, and CRDT data types.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riak.png
layout: provider
modified: '2026-05-11'
name: Riak KV
nav: Providers
network: true
overview: 'Riak KV publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Mapred API, Ping API, Riak KV HTTP API API, and 3 more. Tagged areas include Database, NoSQL, Key-Value Store, Distributed Systems, and Open Source.


  Riak KV''s developer surface includes authentication, documentation, and 11 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 25.0
  delta: -3.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 46.6
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/riak/refs/heads/main/screenshots/riak-2026-06-20T193107.png
security:
- kind: authentication
  name: Riak Authentication
  slug: riak-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Riak Domain Security
  slug: riak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: riak
tags:
- Database
- NoSQL
- Key-Value Store
- Distributed Systems
- Open Source
- Basho
- CRDT
website: https://riak.com
---
