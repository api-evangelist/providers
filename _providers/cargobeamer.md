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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cargobeamer/refs/heads/main/hosts/cargobeamer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cargobeamer-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cargobeamer.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cargobeamer.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.cargobeamer.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.cargobeamer.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cargobeamer/refs/heads/main/security/cargobeamer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cargobeamer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cargobeamer.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cargobeamer.com/technology
- group: company
  title: ''
  type: About
  url: https://www.cargobeamer.com/company
- group: operate
  title: ''
  type: Contact
  url: https://www.cargobeamer.com/company
- group: start
  title: ''
  type: SignUp
  url: https://www.cargobeamer.com/request-for-quotation
coverage:
  checked: '2026-10-07'
  detail: The CargoBeamer website provides no OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications despite having a technology documentation page.
  evidence:
  - status: 404
    url: https://www.cargobeamer.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: CargoBeamer provides a smart, reliable and environmentally friendly system for intermodal transport of semi‑trailers by rail across Europe. It connects logistics companies, freight forwarders and shippers with a growing network of routes and terminals, aiming to reduce road congestion and emissions while offering flexible, fast rail‑based freight solutions.
image: https://www.cargobeamer.com/files/theme/img/favicon/android-chrome-256x256.png
layout: provider
modified: '2026-10-07'
name: Cargobeamer
nav: Providers
network: true
overview: 'Cargobeamer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Intermodal, Rail, and Sustainability.


  Cargobeamer''s developer surface includes engineering blog, documentation, signup flow, and 8 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Cargobeamer Domain Security
  slug: cargobeamer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cargobeamer
tags:
- Company
- Logistics
- Intermodal
- Rail
- Sustainability
website: https://www.cargobeamer.com
---
