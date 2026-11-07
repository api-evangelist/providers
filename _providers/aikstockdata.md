---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aikstockdata Agentic Access
  operation_count: 37
  slug: aikstockdata-agentic-access
  summary_line: 37 operations
api_count: 2
apis:
- baseURL: https://aikstockdata.com/data/public
  baseurl_source: declared
  description: The Data API from 한국주식데이터 (aikstockdata) — 37 operation(s) for data.
  name: 한국주식데이터 (aikstockdata) Data API
  slug: aikstockdata-data-api
artifact_total: 20
common:
- group: commercial
  href: https://artifacts.apis.io/aikstockdata/finops/aikstockdata-finops.yml
  title: ''
  type: FinOps
  url: finops/aikstockdata-finops.yml
- group: design
  href: https://artifacts.apis.io/aikstockdata/vocabulary/aikstockdata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aikstockdata-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/aikstockdata/integrations/aikstockdata-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/aikstockdata-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/aikstockdata/plans/aikstockdata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aikstockdata-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aikstockdata/rate-limits/aikstockdata-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aikstockdata-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/aikstockdata/changelog/aikstockdata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aikstockdata-changelog.yml
- group: agent
  href: https://artifacts.apis.io/aikstockdata/agentic-access/aikstockdata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aikstockdata-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aikstockdata/rules/aikstockdata-rules.yml
  title: ''
  type: Spectral
  url: rules/aikstockdata-rules.yml
- group: design
  href: https://artifacts.apis.io/aikstockdata/lifecycle/aikstockdata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aikstockdata-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/aikstockdata/llms/aikstockdata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aikstockdata-llms.txt
- group: other
  href: https://artifacts.apis.io/aikstockdata/hosts/aikstockdata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aikstockdata-hosts.yml
- group: other
  href: https://artifacts.apis.io/aikstockdata/vendors/aikstockdata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aikstockdata-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://aikstockdata.com/press
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.aikstockdata.com/mcp
- group: other
  href: https://artifacts.apis.io/aikstockdata/overlays/aikstockdata-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aikstockdata-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://aikstockdata.com/
- group: auth
  href: https://artifacts.apis.io/aikstockdata/security/aikstockdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aikstockdata-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/aikstockdata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aikstockdata/well-known/aikstockdata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aikstockdata-well-known.yml
- group: other
  href: https://artifacts.apis.io/aikstockdata/well-known/aikstockdata-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/aikstockdata-api-catalog.json
- group: operate
  title: ''
  type: StatusPage
  url: https://aikstockdata.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://aikstockdata.com/notices
- group: design
  href: https://artifacts.apis.io/aikstockdata/conformance/aikstockdata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aikstockdata-conformance.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aikstockdata.com/ai
- group: docs
  title: ''
  type: Documentation
  url: https://aikstockdata.com/ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aikstockdata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aikstockdata.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://aikstockdata.com/feed.xml
- group: operate
  title: ''
  type: Support
  url: https://aikstockdata.com/about
created: '2026-09-10'
description: An automated Korean equities open-data publisher. Each trading day it compiles DART filings and T+1 (previous-session) closing prices for KOSPI/KOSDAQ/KONEX names and re-publishes them as machine-readable JSON/CSV files, refreshed once per trading day at 18:10 KST. Free, keyless, and unauthenticated, with a REST/static-file API (OpenAPI 3.1), a hosted MCP server, and an llms.txt.
finops:
- has_sources: true
  method: derived
  name: Aikstockdata Finops
  primary_unit: ''
  service_category: ''
  slug: aikstockdata-finops
  template: true
image: https://aikstockdata.com/og.png
json_schemas:
- name: post-filing price paths (/data/public/disclosure_impact.json)
  property_count: 30
  slug: aikstockdata-disclosure_impact.schema
- name: disclosure briefing (/data/public/disclosures.json)
  property_count: 28
  slug: aikstockdata-disclosures.schema
- name: earnings ledger (/data/public/earnings.json)
  property_count: 25
  slug: aikstockdata-earnings.schema
- name: excluded stocks (/data/public/excluded.json)
  property_count: 24
  slug: aikstockdata-excluded.schema
- name: slim quotes (/data/public/quotes_slim.json)
  property_count: 24
  slug: aikstockdata-quotes_slim.schema
- name: rankings (/data/public/rankings.json)
  property_count: 33
  slug: aikstockdata-rankings.schema
- name: screening rows (/data/public/screen.json)
  property_count: 21
  slug: aikstockdata-screen.schema
- name: per-stock JSON (/data/public/s/{code}.json)
  property_count: 35
  slug: aikstockdata-stock.schema
- name: daily digest (/data/public/today.json)
  property_count: 40
  slug: aikstockdata-today.schema
layout: provider
mcp_servers:
- description: ''
  name: 한국주식데이터 (aikstockdata) MCP Server
  slug: mcp
modified: '2026-09-10'
name: 한국주식데이터 (aikstockdata)
nav: Providers
network: true
overview: '한국주식데이터 (aikstockdata) publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Data API. Tagged areas include South Korea, Stock Market, Financial Data, Open Data, and Dart.


  The 한국주식데이터 (aikstockdata) catalog on APIs.io includes 1 Spectral governance ruleset.


  한국주식데이터 (aikstockdata)''s developer surface includes changelog, documentation, engineering blog, support, and 25 more developer resources.'
plans:
- name: Aikstockdata Plans Pricing
  plan_count: 1
  slug: aikstockdata-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Aikstockdata Rate Limits
  slug: aikstockdata-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: 한국주식데이터 (aikstockdata) API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: aikstockdata-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.2
    catalog_earned_first_party: 8.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 56.1
    developer_ergonomics: 58.9
    discoverability: 70.8
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/aikstockdata/aikstockdata-2026-10-11T093311.png
security:
- kind: authentication
  name: Aikstockdata Authentication
  slug: aikstockdata-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aikstockdata Domain Security
  slug: aikstockdata-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: korean-market-digest-and-disclosures
  slug: aikstockdata-market-digest
- name: korean-stock-lookup
  slug: aikstockdata-stock-lookup
slug: aikstockdata
tags:
- South Korea
- Stock Market
- Financial Data
- Open Data
- Dart
- kospi
- kosdaq
- konex
- Filings
- Stocks
- MCP
- Llms.txt
- OpenAPI
website: https://aikstockdata.com/
---
