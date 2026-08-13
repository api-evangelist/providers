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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Myscale Agentic Access
  operation_count: 2
  slug: myscale-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: 'MyScale Cloud provisions and manages clusters (create, modify name / size / replicas / idle period, reset password, view status) through the web console at the MyScale Cloud site. As of this catalog, '
  name: MyScale Cloud / Cluster Management
  slug: myscale-cloud-management
- description: The Query API from MyScale — 1 operation(s) for query.
  name: MyScale Query API
  slug: myscale-query-api
artifact_total: 9
collections:
- collection_type: open
  name: MyScale SQL (ClickHouse HTTP) Interface
  slug: open-myscale
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/myscale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/myscale-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myscale
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/myscale
- group: company
  title: ''
  type: Website
  url: https://www.myscale.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.myscale.com/en/overview/
- group: commercial
  title: ''
  type: Plans
  url: plans/myscale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/myscale-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/myscale-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.myscale.com/blog/rss.xml
created: '2026-06-20'
description: MyScale is a SQL vector database built on a ClickHouse fork (MyScaleDB), combining high-performance vector search, full-text search, and analytical SQL in a single engine. Its primary interface is SQL executed over the ClickHouse-compatible HTTP interface (HTTPS on port 8443), where vector similarity search is expressed with SQL functions like distance() against VECTOR INDEX columns. A managed MyScale Cloud console provisions clusters, and the underlying MyScaleDB is open source under Apache-2.0.
finops:
- name: Myscale Finops
  service_category: Databases
  slug: myscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/myscale.png
layout: provider
modified: '2026-06-20'
name: MyScale
nav: Providers
network: true
overview: 'MyScale publishes 1 API on the [APIs.io](https://apis.io/) network: Query API. Tagged areas include Vector Database, SQL, ClickHouse, Vector Search, and Full-Text Search.


  MyScale''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Myscale Plans Pricing
  plan_count: 4
  slug: myscale-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 4
  name: Myscale Rate Limits
  slug: myscale-rate-limits
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.4
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/myscale/refs/heads/main/screenshots/myscale-2026-06-20T185918.png
security:
- kind: authentication
  name: Myscale Authentication
  slug: myscale-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Myscale Domain Security
  slug: myscale-domain-security
  summary_line: TLSv1.3 · HSTS
slug: myscale
tags:
- Vector Database
- SQL
- ClickHouse
- Vector Search
- Full-Text Search
- RAG
website: https://www.myscale.com
---
