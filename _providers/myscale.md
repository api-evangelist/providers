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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Myscale Agentic Access
  operation_count: 2
  slug: myscale-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: 'MyScale Cloud provisions and manages clusters (create, modify name / size / replicas / idle period, reset password, view status) through the web console at the MyScale Cloud site. As of this catalog, '
  name: MyScale Cloud / Cluster Management
  slug: myscale-cloud-management
- baseURL: https://{cluster-host}:8443
  baseurl_source: declared
  description: The Query API from MyScale — 1 operation(s) for query.
  name: MyScale Query API
  slug: myscale-query-api
artifact_total: 10
collections:
- collection_type: open
  name: MyScale SQL (ClickHouse HTTP) Interface Query API
  slug: open-myscale-query-api
- collection_type: open
  name: MyScale SQL (ClickHouse HTTP) Interface
  slug: open-myscale
common:
- group: agent
  href: https://artifacts.apis.io/myscale/agentic-access/myscale-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/myscale-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/myscale/security/myscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/myscale-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/myscale/authentication/myscale-authentication.yml
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
  href: https://artifacts.apis.io/myscale/plans/myscale-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/myscale-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/myscale/rate-limits/myscale-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/myscale-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/myscale/finops/myscale-finops.yml
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
- has_sources: true
  method: generated
  name: Myscale Finops
  primary_unit: ''
  service_category: Databases
  slug: myscale-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/myscale.png
layout: provider
modified: '2026-06-20'
name: MyScale
nav: Providers
network: true
overview: 'MyScale publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Query API, and 1 more. Tagged areas include Vector Search, SQL, ClickHouse, Full-Text Search, and RAG.


  MyScale''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Myscale Plans Pricing
  plan_count: 4
  slug: myscale-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Myscale Rate Limits
  slug: myscale-rate-limits
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 49.6
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/myscale/myscale-2026-06-20T185918.png
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
- Vector Search
- SQL
- ClickHouse
- Full-Text Search
- RAG
website: https://www.myscale.com
---
