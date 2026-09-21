---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: Authenticated, read-only REST/JSON API for company search and lookup, typeahead suggestions, single-company retrieval (by id or tax number), and domain WHOIS/RDAP lookups. Static bearer API-key auth (
  name: Felhő REST API v1
  slug: felhő-rest-api-v1
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/felh-magyar-zleti-infrastrukt-ra/refs/heads/main/security/felh-magyar-zleti-infrastrukt-ra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/felh-magyar-zleti-infrastrukt-ra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://felho.hu
- group: docs
  title: ''
  type: Documentation
  url: https://felho.hu/dokumentacio
- group: commercial
  title: ''
  type: Pricing
  url: https://felho.hu/arak
- group: operate
  title: ''
  type: StatusPage
  url: https://felho.hu/statusz
- group: start
  title: ''
  type: SignUp
  url: https://felho.hu/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://felho.hu/aszf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://felho.hu/adatvedelem
created: '2026-09-17'
description: Hungarian business-infrastructure platform offering company information (registry data, financials, officers/owners, TEÁOR'25 activity codes), business verification and risk scoring, address/tax-number and bank routing lookups, and domain/WHOIS-RDAP tools. Provides an authenticated REST/JSON API and agent-native llms.txt artifacts. Operated by Verde Holding Kft.; data is drawn from the public Hungarian company register, published financial statements and the NAV VAT registry. Missing data is returned as null, never estimated.
image: https://felho.hu/og
layout: provider
mcp_servers:
- description: No MCP server is published by Felho (hosted or local). Probed https://felho.hu/mcp, https://felho.hu/api/mcp and https://mcp.felho.hu/mcp on 2026-09-18 — the first two return the SPA 404 shell, the mc
  name: Felhő — Magyar üzleti infrastruktúra MCP Server
  slug: felhő-magyar-üzleti-infrastruktúra-mcp-server
modified: '2026-09-18'
name: Felhő — Magyar üzleti infrastruktúra
nav: Providers
network: true
overview: 'Felhő — Magyar üzleti infrastruktúra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company Data, Business Verification, Domains, WHOIS/RDAP, and Hungary.


  Felhő — Magyar üzleti infrastruktúra''s developer surface includes documentation, pricing, signup flow, and 5 more developer resources.'
plans:
- name: Felh Magyar Zleti Infrastrukt Ra Plans Pricing
  plan_count: 3
  slug: felh-magyar-zleti-infrastrukt-ra-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Felh Magyar Zleti Infrastrukt Ra Rate Limits
  slug: felh-magyar-zleti-infrastrukt-ra-rate-limits
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 58.0
    catalog_earned_first_party: 24.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 70.4
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 36.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Felh Magyar Zleti Infrastrukt Ra Authentication
  slug: felh-magyar-zleti-infrastrukt-ra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Felh Magyar Zleti Infrastrukt Ra Domain Security
  slug: felh-magyar-zleti-infrastrukt-ra-domain-security
  summary_line: TLSv1.3
slug: felh-magyar-zleti-infrastrukt-ra
tags:
- Company Data
- Business Verification
- Domains
- WHOIS/RDAP
- Hungary
- Registry Data
- Financial Data
website: https://felho.hu
---
