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
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Memgraph Agentic Access
  operation_count: 1
  slug: memgraph-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'MAGE (Memgraph Advanced Graph Extensions) is an open-source library of graph algorithms and query modules - traditional, dynamic, and ML-driven - invoked as Cypher procedures (CALL ...) over the same '
  name: Memgraph MAGE Algorithms
  slug: memgraph-mage-algorithms
- description: Memgraph Lab is a lightweight visual interface for writing Cypher queries, visualizing graph results, importing data, and inspecting query modules. The Lab application itself connects to Memgraph over
  name: Memgraph Lab
  slug: memgraph-lab
- baseURL: bolt://localhost:7687
  baseurl_source: declared
  description: The Monitoring API from Memgraph — 1 operation(s) for monitoring.
  name: Memgraph Monitoring API
  slug: memgraph-monitoring-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Memgraph HTTP Metrics Monitoring API
  slug: open-memgraph-monitoring-api
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
random_paper: 9
rate_limits:
- limit_count: 4
  name: Memgraph Rate Limits
  slug: memgraph-rate-limits
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
