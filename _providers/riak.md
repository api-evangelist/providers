---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Riak Agentic Access
  operation_count: 25
  slug: riak-agentic-access
  summary_line: 25 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: RESTful HTTP API for Riak KV providing GET, PUT, POST, and DELETE access to buckets, objects, secondary indexes, search, MapReduce, and CRDT data types. Default port is 8098. Authentication and author
  name: Riak KV HTTP API
  slug: http-api
- description: Higher-performance binary client API for Riak KV using Protocol Buffers messages encoded over a long-lived TCP connection. Default port is 8087. Each request message produces one or more response mess
  name: Riak Protocol Buffers Client API
  slug: protocol-buffers
- baseURL: http://<your-riak-host>:8098
  baseurl_source: declared
  description: The Mapred API from Riak KV — 1 operation(s) for mapred.
  name: Riak KV Mapred API
  slug: riak-mapred-api
- baseURL: http://<your-riak-host>:8098
  baseurl_source: declared
  description: The Ping API from Riak KV — 1 operation(s) for ping.
  name: Riak KV Ping API
  slug: riak-ping-api
- baseURL: http://<your-riak-host>:8098
  baseurl_source: declared
  description: The Riak KV HTTP API API from Riak KV — 1 operation(s) for riak kv http api.
  name: Riak KV Riak KV HTTP API API
  slug: riak-riak-kv-http-api-api
- baseURL: http://<your-riak-host>:8098
  baseurl_source: declared
  description: The Search API from Riak KV — 4 operation(s) for search.
  name: Riak KV Search API
  slug: riak-search-api
- baseURL: http://<your-riak-host>:8098
  baseurl_source: declared
  description: The Stats API from Riak KV — 1 operation(s) for stats.
  name: Riak KV Stats API
  slug: riak-stats-api
- baseURL: http://<your-riak-host>:8098
  baseurl_source: declared
  description: The Types API from Riak KV — 7 operation(s) for types.
  name: Riak KV Types API
  slug: riak-types-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Riak KV HTTP Mapred API
  slug: open-riak-mapred-api
- collection_type: open
  name: Riak KV HTTP Mapred Ping API
  slug: open-riak-ping-api
- collection_type: open
  name: Riak KV HTTP Mapred Riak KV HTTP API API
  slug: open-riak-riak-kv-http-api-api
- collection_type: open
  name: Riak KV HTTP Mapred Search API
  slug: open-riak-search-api
- collection_type: open
  name: Riak KV HTTP Mapred Stats API
  slug: open-riak-stats-api
- collection_type: open
  name: Riak KV HTTP Mapred Types API
  slug: open-riak-types-api
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
overview: 'Riak KV publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Mapred API, Ping API, Riak KV HTTP API API, and 3 more. Tagged areas include Database, NoSQL, Key-Value Store, Distributed Systems, and Open-Source.


  Riak KV''s developer surface includes authentication, documentation, and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
- Basho
- CRDT
website: https://riak.com
---
