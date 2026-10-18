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
- description: CDMO Services page describing Chime Biologics contract development and manufacturing offerings.
  name: CDMO Services
  slug: cdmo-services
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chimebiologics/refs/heads/main/hosts/chimebiologics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chimebiologics-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chimebiologics.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://chimebiologics.com/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chimebiologics/refs/heads/main/security/chimebiologics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chimebiologics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chimebiologics.com
- group: docs
  title: ''
  type: Documentation
  url: https://chimebiologics.com/cdmo-services/
- group: operate
  title: ''
  type: Contact
  url: https://chimebiologics.com/contact-us/
coverage:
  checked: '2026-10-08'
  detail: The CDMO Services documentation provides human‑readable API information but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract.
  evidence:
  - status: 200
    url: https://chimebiologics.com/cdmo-services/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chime Biologics is a contract development and manufacturing organization (CDMO) specializing in cell line development, process development, protein science, technology transfer, and drug substance and product manufacturing. The company offers comprehensive services including quality systems, regulatory support, project management, data integrity, and client confidential information protection, serving biotech and pharmaceutical clients worldwide.
layout: provider
modified: '2026-10-08'
name: Chimebiologics
nav: Providers
network: true
overview: 'Chimebiologics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CDMO, Biologics, Cell Line Development, Process Development, and Protein Science.


  Chimebiologics'' developer surface includes documentation and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chimebiologics Domain Security
  slug: chimebiologics-domain-security
  summary_line: TLSv1.3
slug: chimebiologics
tags:
- CDMO
- Biologics
- Cell Line Development
- Process Development
- Protein Science
- Technology-Transfer
website: https://chimebiologics.com
---
