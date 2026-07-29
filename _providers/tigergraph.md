---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tigergraph Agentic Access
  operation_count: 22
  slug: tigergraph-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 5
apis:
- description: The Authentication API from TigerGraph — 1 operation(s) for authentication.
  name: TigerGraph Authentication API
  slug: tigergraph-authentication-api
- description: The Data API from TigerGraph — 5 operation(s) for data.
  name: TigerGraph Data API
  slug: tigergraph-data-api
- description: The Query API from TigerGraph — 4 operation(s) for query.
  name: TigerGraph Query API
  slug: tigergraph-query-api
- description: The Schema API from TigerGraph — 3 operation(s) for schema.
  name: TigerGraph Schema API
  slug: tigergraph-schema-api
- description: The System API from TigerGraph — 4 operation(s) for system.
  name: TigerGraph System API
  slug: tigergraph-system-api
artifact_total: 13
collections:
- collection_type: open
  name: TigerGraph REST++ API
  slug: open-tigergraph
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tigergraph-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tigergraph-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tigergraph-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tigergraph-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tigergraph
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tigergraph
- group: company
  title: ''
  type: Website
  url: https://www.tigergraph.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tigergraph.com
- group: commercial
  title: ''
  type: Plans
  url: plans/tigergraph-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tigergraph-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tigergraph-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tigergraph.com/blog/
created: '2026-06-20'
description: TigerGraph is a distributed, native parallel graph database and analytics platform. Its database server exposes a built-in REST++ API for reading and writing vertices and edges, running installed GSQL queries, managing schema, and issuing authentication tokens, alongside the GSQL server and the fully managed TigerGraph Savanna (Cloud) service.
finops:
- name: Tigergraph Finops
  service_category: Databases
  slug: tigergraph-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tigergraph.png
layout: provider
modified: '2026-06-20'
name: TigerGraph
nav: Providers
network: true
overview: 'TigerGraph publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Data API, Query API, and 2 more. Tagged areas include Graph Database, Analytics, GSQL, REST++, and Graph Analytics.


  TigerGraph''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Tigergraph Plans Pricing
  plan_count: 3
  slug: tigergraph-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 4
  name: Tigergraph Rate Limits
  slug: tigergraph-rate-limits
score:
  band: thin
  composite: 36.8
  delta: -3.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 46.9
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tigergraph/refs/heads/main/screenshots/tigergraph-2026-06-20T195352.png
security:
- kind: authentication
  name: Tigergraph Authentication
  slug: tigergraph-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tigergraph Domain Security
  slug: tigergraph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tigergraph Trust Center
  slug: tigergraph-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: tigergraph
tags:
- Graph Database
- Analytics
- GSQL
- REST++
- Graph Analytics
website: https://www.tigergraph.com
---
