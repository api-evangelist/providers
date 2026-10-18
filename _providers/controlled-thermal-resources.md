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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlled-thermal-resources/refs/heads/main/well-known/controlled-thermal-resources-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/controlled-thermal-resources-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/controlled-thermal-resources/refs/heads/main/well-known/controlled-thermal-resources-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/controlled-thermal-resources-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlled-thermal-resources/refs/heads/main/hosts/controlled-thermal-resources-hosts.yml
  title: ''
  type: Hosts
  url: hosts/controlled-thermal-resources-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/controlled-thermal-resources/refs/heads/main/vendors/controlled-thermal-resources-vendors.yml
  title: ''
  type: Vendors
  url: vendors/controlled-thermal-resources-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.cthermal.com/register-your-interest
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cthermal.com/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.cthermal.com/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlled-thermal-resources/refs/heads/main/security/controlled-thermal-resources-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/controlled-thermal-resources-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/controlled-thermal-resources/refs/heads/main/security/controlled-thermal-resources-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/controlled-thermal-resources-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cthermal.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cthermal.com/
  - status: 200
    url: https://www.hiive.com/securities/controlled-thermal-resources-stock
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Controlled Thermal Resources develops the Hell’s Kitchen project, an integrated geothermal power plant that generates renewable baseload electricity and extracts critical minerals such as lithium carbonate, zinc, manganese and potash. The company refines these minerals on‑site into battery‑grade products and supplies clean energy to advanced manufacturers, data centers and battery producers. Its vertically integrated model aims to reduce U.S. supply‑chain risk and support domestic energy and mineral needs.
image: http://static1.squarespace.com/static/5bbc837993a6324308c97e9c/t/66879562a6a70b14c1fee281/1720161634522/CTR+Logo+2023+White_CMYK_background+removed.png?format=1500w
layout: provider
modified: '2026-10-10'
name: Controlled Thermal Resources
nav: Providers
network: true
overview: 'Controlled Thermal Resources is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Geothermal Energy, Critical Minerals, Renewable Energy, Energy Infrastructure, and Energy Security.


  Controlled Thermal Resources'' developer surface includes signup flow and 10 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Controlled Thermal Resources Domain Security
  slug: controlled-thermal-resources-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Controlled Thermal Resources Vulnerability Disclosure
  slug: controlled-thermal-resources-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: controlled-thermal-resources
tags:
- Geothermal Energy
- Critical Minerals
- Renewable Energy
- Energy Infrastructure
- Energy Security
website: https://www.cthermal.com/
---
