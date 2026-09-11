---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: A set of ~37 static JSON/CSV endpoints under /data/public/ covering daily market digest, T+1 quotes, disclosures, rankings, screening, earnings, per-stock data and history, plus dated archives. Docume
  name: 한국주식데이터 공개 데이터 API
  slug: 한국주식데이터-공개-데이터-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://aikstockdata.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aikstockdata-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aikstockdata-well-known.yml
- group: other
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/na77tech-creator/aikstockdata
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
  slug: 한국주식데이터-aikstockdata-mcp-server
modified: '2026-09-10'
name: 한국주식데이터 (aikstockdata)
nav: Providers
network: true
overview: '한국주식데이터 (aikstockdata) publishes 1 API on the [APIs.io](https://apis.io/) network: 한국주식데이터 공개 데이터 API. Tagged areas include korea, stock-market, financial-data, open-data, and dart.


  한국주식데이터 (aikstockdata)''s developer surface includes changelog, documentation, engineering blog, support, and 11 more developer resources.'
plans:
- name: Aikstockdata Plans Pricing
  plan_count: 1
  slug: aikstockdata-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Aikstockdata Rate Limits
  slug: aikstockdata-rate-limits
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 34.7
    developer_ergonomics: 58.9
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 34.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Aikstockdata Authentication
  slug: aikstockdata-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aikstockdata Domain Security
  slug: aikstockdata-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aikstockdata
tags:
- korea
- stock-market
- financial-data
- open-data
- dart
- kospi
- kosdaq
- konex
- filings
- equities
- mcp
- llms-txt
- openapi
website: https://aikstockdata.com/
---
