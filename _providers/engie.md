---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://vdp.engie.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/engie/refs/heads/main/well-known/engie-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/engie-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/engie/refs/heads/main/well-known/engie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/engie-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/engie/refs/heads/main/hosts/engie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/engie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/engie/refs/heads/main/vendors/engie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/engie-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.engie.com/en/explore/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/engie/refs/heads/main/security/engie-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/engie-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/engie/refs/heads/main/security/engie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/engie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.engie.com
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at the API host (api.engie.com) – all probe URLs returned 404 SOAP fault pages.
  evidence:
  - status: 404
    url: https://api.engie.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: ENGIE is a global energy player headquartered in France, providing electricity, natural gas, and energy services to millions of customers worldwide. The company focuses on sustainable development, renewable energy projects, and digital transformation of its operations. ENGIE’s portfolio includes power generation, distribution, and innovative solutions for energy efficiency, electric mobility, and smart grids, positioning it as a leader in the transition to low‑carbon economies.
image: https://www.engie.com/app/uploads/2026/05/Opengraph.jpg
layout: provider
modified: '2026-10-13'
name: ENGIE
nav: Providers
network: true
overview: ENGIE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Renewables, Sustainability, and France.
random_paper: 14
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
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
    score: 14.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Engie Domain Security
  slug: engie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Engie Vulnerability Disclosure
  slug: engie-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: engie
tags:
- Energy
- Utilities
- Renewables
- Sustainability
- France
- Company
website: https://www.engie.com
---
