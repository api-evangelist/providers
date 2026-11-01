---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Cibo Labs provides agricultural data APIs for pasture biomass, feed monitoring, land condition reports, and assessments.
  name: Cibo Labs API
  slug: cibo-labs-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/cibo-labs/plans/cibo-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cibo-labs-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/cibo-labs/well-known/cibo-labs-cibolabs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cibo-labs-cibolabs-security.txt
- group: auth
  href: https://artifacts.apis.io/cibo-labs/well-known/cibo-labs-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cibo-labs-api-security.txt
- group: agent
  href: https://artifacts.apis.io/cibo-labs/well-known/cibo-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cibo-labs-well-known.yml
- group: other
  href: https://artifacts.apis.io/cibo-labs/hosts/cibo-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cibo-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/cibo-labs/vendors/cibo-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cibo-labs-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.cibolabs.com.au/team
- group: start
  title: ''
  type: GettingStarted
  url: https://support.cibolabs.com.au/en/knowledge/cibo-labs-forage-budget-calculator-quick-start-guide
- group: auth
  href: https://artifacts.apis.io/cibo-labs/security/cibo-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cibo-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cibolabs.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.cibolabs.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://support.cibolabs.com.au/en/knowledge
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cibolabs.com.au/products
- group: start
  title: ''
  type: SignUp
  url: https://app.cibolabs.com.au/authentication/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cibolabs.atlassian.net/l/c/d8K4zAbN
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cibolabs.atlassian.net/l/c/d8K4zAbN
- group: company
  title: ''
  type: Blog
  url: https://blog.cibolabs.com.au/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cibolabs
- group: other
  title: ''
  type: Image
  url: https://www.cibolabs.com.au/hubfs/cibolabs.png
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or gRPC specifications were found.
  evidence:
  - status: 200
    url: https://www.cibolabs.com.au/products?hsLang=en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Cibo Labs Pty Ltd is an Australian agricultural data analytics company that provides satellite‑derived insights for farms, including pasture biomass, feed monitoring, land condition reports, and compliance assessments, empowering producers to make data‑driven decisions for profitability and sustainability.
layout: provider
modified: '2026-10-28'
name: Cibo Labs
nav: Providers
network: true
overview: 'Cibo Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, DataAnalytics, Geospatial, SatelliteImagery, and FarmManagement.


  Cibo Labs'' developer surface includes getting-started guide, documentation, pricing, signup flow, engineering blog, and 14 more developer resources.'
plans:
- name: Cibo Labs Plans Pricing
  plan_count: 4
  slug: cibo-labs-plans-pricing
random_paper: 12
scopes:
- name: Cibo Labs Scopes
  scope_count: 0
  slug: cibo-labs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cibo Labs Authentication
  slug: cibo-labs-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cibo Labs Domain Security
  slug: cibo-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cibo-labs
tags:
- Agriculture
- DataAnalytics
- Geospatial
- SatelliteImagery
- FarmManagement
website: https://www.cibolabs.com.au/
---
