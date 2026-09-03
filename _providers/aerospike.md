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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aerospike Agentic Access
  operation_count: 3
  slug: aerospike-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: HTTP/JSON gateway that exposes Aerospike database operations including key-value reads/writes, batch, operate, scan, query, info, secondary indexes, and user-defined functions. Authentication is via H
  name: Aerospike REST Gateway
  slug: rest-gateway
- baseURL: http://localhost:8080/v1
  baseurl_source: declared
  description: Cluster topology and information operations
  name: Aerospike Cluster API
  slug: aerospike-cluster-api
- baseURL: http://localhost:8080/v1
  baseurl_source: declared
  description: Built-in interactive documentation and OpenAPI specification
  name: Aerospike Documentation API
  slug: aerospike-documentation-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aerospike REST Gateway Cluster API
  slug: open-aerospike-cluster-api
- collection_type: open
  name: Aerospike REST Gateway Cluster Documentation API
  slug: open-aerospike-documentation-api
- collection_type: open
  name: Aerospike REST Gateway
  slug: open-aerospike
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aerospike-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerospike-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aerospike-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aerospike-inc-
- group: company
  title: ''
  type: Website
  url: https://aerospike.com
- group: docs
  title: ''
  type: Documentation
  url: https://aerospike.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.aerospike.com
- group: commercial
  title: ''
  type: Pricing
  url: https://aerospike.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://aerospike.com/lp/try-now/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aerospike
- group: operate
  title: ''
  type: Community
  url: https://discuss.aerospike.com
- group: operate
  title: ''
  type: Support
  url: https://aerospike.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aerospike.com/blog/
created: '2026-05-11'
description: Aerospike is a real-time, high-throughput, low-latency NoSQL database platform built on a hybrid memory architecture that powers operational systems handling petabytes of data at sub-millisecond latency. The platform supports key-value, document, graph, vector, and JSON workloads with strong consistency, cross-datacenter replication, and tiered storage on flash. The Aerospike REST Gateway exposes the full database API (info, scan, query, operate, batch, UDFs, secondary indexes) over HTTP/JSON with Basic authentication forwarded to the Aerospike security subsystem.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aerospike.png
layout: provider
modified: '2026-05-11'
name: Aerospike
nav: Providers
network: true
overview: 'Aerospike publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cluster API and Documentation API. Tagged areas include Database, NoSQL, Real-Time, Key-Value, and In-Memory.


  Aerospike''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 36.7
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 25.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aerospike/refs/heads/main/screenshots/aerospike-2026-06-20T165533.png
security:
- kind: authentication
  name: Aerospike Authentication
  slug: aerospike-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aerospike Domain Security
  slug: aerospike-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aerospike
tags:
- Database
- NoSQL
- Real-Time
- Key-Value
- In-Memory
- Vector Database
- High Performance
website: https://aerospike.com
---
