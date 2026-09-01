---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The open-source core. SQL statements embedded in Markdown files run against configured data sources and render charts and components into a static BI website (Svelte/Vite). The interface is a Node CLI
  name: Evidence Framework (SQL + Markdown)
  slug: evidence-framework
- description: 'Universal SQL, the query engine built into Evidence core and powered by DuckDB''s WebAssembly distribution. It extracts data sources to Parquet and lets you query across multiple sources with a single '
  name: Evidence USQL / Query Layer
  slug: usql-query-layer
- description: The managed hosting and deployment platform for Evidence projects. Adds a managed query engine, multi-level caching, row-level security, scheduled data syncs, a browser-based IDE, and AI authoring ass
  name: Evidence Cloud
  slug: evidence-cloud
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Evidence (Framework - not a REST API)
  slug: open-evidence-dev
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/evidence-dev-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evidence-dev-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evidence-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evidence-dev
- group: company
  title: ''
  type: Website
  url: https://evidence.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evidence.dev/
- group: commercial
  title: ''
  type: Plans
  url: plans/evidence-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evidence-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/evidence-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://evidence.dev/blog
created: '2026-06-20'
description: Evidence is an open-source (MIT) business-intelligence-as-code framework that turns SQL queries plus Markdown into fast, version-controlled static data apps and dashboards. It is built on Svelte/Vite, runs queries through a DuckDB-WASM "Universal SQL" engine, and is consumed as a framework/CLI rather than a hosted REST API. Evidence Cloud adds managed hosting, a managed query engine, scheduled data syncs, and AI authoring assistance.
finops:
- name: Evidence Dev Finops
  service_category: Analytics and Business Intelligence
  slug: evidence-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evidence-dev.png
layout: provider
modified: '2026-06-20'
name: Evidence
nav: Providers
network: true
overview: 'Evidence publishes 3 APIs on the [APIs.io](https://apis.io/) network: Framework (SQL + Markdown), USQL / Query Layer, and Cloud. Tagged areas include Business Intelligence, BI-as-Code, SQL, Markdown, and Data Apps.


  Evidence''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Evidence Dev Plans Pricing
  plan_count: 5
  slug: evidence-dev-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Evidence Dev Rate Limits
  slug: evidence-dev-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 30.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evidence-dev/refs/heads/main/screenshots/evidence-dev-2026-06-20T180912.png
security:
- kind: domain-security
  name: Evidence Dev Domain Security
  slug: evidence-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Evidence Dev Trust Center
  slug: evidence-dev-trust-center
  summary_line: SOC 2
slug: evidence-dev
tags:
- Business Intelligence
- BI-as-Code
- SQL
- Markdown
- Data Apps
- Open-Source
website: https://evidence.dev/
---
