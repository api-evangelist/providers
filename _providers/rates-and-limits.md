---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: Keyless, unauthenticated REST-style JSON API serving US tax, payroll, benefits, and wage figures with bundled provenance. Includes a self-describing catalog (index.json) and a bulk current-figures end
  name: Rates and Limits JSON API
  slug: rates-and-limits-json-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://ratesandlimits.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rates-and-limits/refs/heads/main/security/rates-and-limits-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rates-and-limits-domain-security.yml
created: '2026-09-14'
description: 'A free, keyless open-data publisher exposing US federal and state tax, payroll, benefits, and wage figures as JSON. Every figure ships bundled with provenance: the exact quoted sentence from the governing government document, byte offsets, sha256-stamped source snapshots, and last-verified dates.'
layout: provider
mcp_servers:
- description: ''
  name: Rates and Limits MCP Server
  slug: rates-and-limits-mcp-server
modified: '2026-09-14'
name: Rates and Limits
nav: Providers
network: true
overview: Rates and Limits publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tax, Payroll, Benefits, IRS, and minimum-wage.
plans:
- name: Rates And Limits Plans Pricing
  plan_count: 0
  slug: rates-and-limits-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Rates And Limits Rate Limits
  slug: rates-and-limits-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 19.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rates And Limits Authentication
  slug: rates-and-limits-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rates And Limits Domain Security
  slug: rates-and-limits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rates-and-limits
tags:
- Tax
- Payroll
- Benefits
- IRS
- minimum-wage
- Open Data
- Government
- Compliance
- Fintech
- Human Resources
- Reference Data
- JSON
- llms-txt
website: https://ratesandlimits.com/
---
