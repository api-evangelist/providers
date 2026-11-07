---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Boss Insights platform (no public OpenAPI spec found)
  name: Boss Insights API
  slug: boss-insights-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/bossinsights/well-known/bossinsights-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bossinsights-well-known.yml
- group: other
  href: https://artifacts.apis.io/bossinsights/vendors/bossinsights-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bossinsights-vendors.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bossinsights.com/
- group: other
  href: https://artifacts.apis.io/bossinsights/hosts/bossinsights-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bossinsights-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://bossinsights.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://bossinsights.com/news/51523/
- group: start
  title: ''
  type: Login
  url: https://bossinsights.com/sign-in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bossinsights.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bossinsights.com/
- group: auth
  href: https://artifacts.apis.io/bossinsights/security/bossinsights-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bossinsights-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bossinsights/security/bossinsights-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bossinsights-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bossinsights.com/
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec discovered on api.bossinsights.com or docs.bossinsights.com.
  evidence:
  - status: 0
    url: https://api.bossinsights.com/openapi.json
  - status: 0
    url: https://api.bossinsights.com/openapi.yaml
  - status: 0
    url: https://api.bossinsights.com/swagger.json
  - status: 404
    url: https://docs.bossinsights.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Boss Insights provides advanced business intelligence solutions that help companies unlock actionable insights from their data. Their platform aggregates, analyzes, and visualizes key performance metrics, enabling decision makers to track growth, optimize operations, and identify market trends. With a focus on user-friendly dashboards, customizable reporting, and seamless integration with existing data sources, Boss Insights empowers organizations to make data-driven strategies and improve overall performance.
layout: provider
modified: '2026-10-19'
name: Boss Insights
nav: Providers
network: true
overview: 'Boss Insights is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Intelligence, Data Analytics, Dashboards, and Reporting.


  Boss Insights'' developer surface includes documentation and 11 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 54.5
    operational_transparency: 5.3
  previous_composite: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 8.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bossinsights/bossinsights-2026-11-03T122320.png
security:
- kind: domain-security
  name: Bossinsights Domain Security
  slug: bossinsights-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bossinsights Trust Center
  slug: bossinsights-trust-center
  summary_line: SOC 2
slug: bossinsights
tags:
- Company
- Business Intelligence
- Data Analytics
- Dashboards
- Reporting
website: https://bossinsights.com/
---
