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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artin-energy/refs/heads/main/well-known/artin-energy-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/artin-energy-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/artin-energy/refs/heads/main/well-known/artin-energy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/artin-energy-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artin-energy/refs/heads/main/hosts/artin-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artin-energy-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artinenergy.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artin-energy/refs/heads/main/security/artin-energy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/artin-energy-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artin-energy/refs/heads/main/security/artin-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artin-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artinenergy.com
coverage:
  checked: 2026-09-26
  detail: No public API specifications were found for Artin Energy; attempts to fetch OpenAPI files from api.artinenergy.com and artinenergy.com returned errors or HTML pages.
  evidence:
  - status: error
    url: https://api.artinenergy.com/openapi.json
  - status: 404
    url: https://artinenergy.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-09-26'
description: Artin Energy provides solar and renewable energy solutions for businesses, including solar modules, green hydrogen, energy storage, EV charging stations, and hydroponics powered by AI. The company offers engineering, procurement, and construction services, power purchase agreements, and consulting to optimize energy use for commercial clients.
layout: provider
modified: '2026-09-26'
name: Artin Energy
nav: Providers
network: true
overview: Artin Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Renewables, Solar, Green Hydrogen, and Storage.
random_paper: 5
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artin Energy Domain Security
  slug: artin-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Artin Energy Vulnerability Disclosure
  slug: artin-energy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: artin-energy
tags:
- Energy
- Renewables
- Solar
- Green Hydrogen
- Storage
- EV Charging
website: https://artinenergy.com
---
