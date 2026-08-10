---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Memgraph Agentic Access
  operation_count: 1
  slug: memgraph-agentic-access
  summary_line: 1 operation
api_count: 3
apis:
- description: 'MAGE (Memgraph Advanced Graph Extensions) is an open-source library of graph algorithms and query modules - traditional, dynamic, and ML-driven - invoked as Cypher procedures (CALL ...) over the same '
  name: Memgraph MAGE Algorithms
  slug: memgraph-mage-algorithms
- description: Memgraph Lab is a lightweight visual interface for writing Cypher queries, visualizing graph results, importing data, and inspecting query modules. The Lab application itself connects to Memgraph over
  name: Memgraph Lab
  slug: memgraph-lab
- description: The Monitoring API from Memgraph — 1 operation(s) for monitoring.
  name: Memgraph Monitoring API
  slug: memgraph-monitoring-api
artifact_total: 9
collections:
- collection_type: open
  name: Memgraph
  slug: open-memgraph
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/memgraph-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memgraph-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/memgraph
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/memgraph
- group: company
  title: ''
  type: Website
  url: https://memgraph.com
- group: docs
  title: ''
  type: Documentation
  url: https://memgraph.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/memgraph-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/memgraph-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/memgraph-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://memgraph.com/blog
created: '2026-06-20'
description: Memgraph is an open-source, high-performance in-memory graph database built in C++ for real-time graph analytics, GraphRAG, and agentic AI. Its primary interface is Cypher executed over the Bolt wire protocol (TCP port 7687) via standard graph drivers - it is not a REST API. Memgraph also ships MAGE graph algorithms, the GQLAlchemy Python OGM, the Memgraph Lab visual interface, a WebSocket log-monitoring channel, and an Enterprise Prometheus-style metrics HTTP endpoint.
finops:
- name: Memgraph Finops
  service_category: Databases
  slug: memgraph-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/memgraph.png
layout: provider
modified: '2026-06-20'
name: Memgraph
nav: Providers
network: true
overview: 'Memgraph publishes 1 API on the [APIs.io](https://apis.io/) network: Monitoring API. Tagged areas include Graph Database, In-Memory, Cypher, Bolt, and Real-Time.


  Memgraph''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Memgraph Plans Pricing
  plan_count: 3
  slug: memgraph-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 4
  name: Memgraph Rate Limits
  slug: memgraph-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memgraph/refs/heads/main/screenshots/memgraph-2026-06-20T185201.png
security:
- kind: domain-security
  name: Memgraph Domain Security
  slug: memgraph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: memgraph
tags:
- Graph Database
- In-Memory
- Cypher
- Bolt
- Real-Time
website: https://memgraph.com
---
