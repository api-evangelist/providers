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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Puro.Earth carbon removal registry and tools. Documentation is hosted at the Help Center but no machine‑readable contract was found.
  name: Puro.Earth API
  slug: puro-earth-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/puro-earth/refs/heads/main/vendors/puro-earth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/puro-earth-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/puro-earth/refs/heads/main/well-known/puro-earth-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/puro-earth-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/puro-earth/refs/heads/main/well-known/puro-earth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/puro-earth-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/puro-earth/refs/heads/main/hosts/puro-earth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/puro-earth-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://puro.earth/legal-notice/
- group: operate
  title: ''
  type: Support
  url: https://help.puro.earth/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://puro.earth/legal-notice/privacy-notice/
- group: start
  title: ''
  type: Login
  url: https://my.puro.earth/web/login/
- group: docs
  title: ''
  type: Documentation
  url: https://help.puro.earth/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/puro-earth/refs/heads/main/security/puro-earth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/puro-earth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://puro.earth
coverage:
  checked: '2026-10-14'
  detail: Help Center pages provide documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://help.puro.earth/en/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Puro.earth provides a certification infrastructure for carbon removal, turning durable carbon removal into a global, investment‑grade market. It offers a registry, standards, and tools for issuing, trading, and verifying carbon removal credits, supporting transparency and trust in the emerging CDR sector.
image: https://puro.earth/wp-content/uploads/2026/03/ksp-pattern.svg
layout: provider
modified: '2026-10-14'
name: Puro.earth
nav: Providers
network: true
overview: 'Puro.earth is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CarbonRemoval, Climate Tech, Registry, and Sustainability.


  Puro.earth''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Puro Earth Domain Security
  slug: puro-earth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: puro-earth
tags:
- Company
- CarbonRemoval
- Climate Tech
- Registry
- Sustainability
website: https://puro.earth
---
