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
  href: https://raw.githubusercontent.com/api-evangelist/skatteverket/refs/heads/main/security/skatteverket-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/skatteverket-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skatteverket/refs/heads/main/well-known/skatteverket-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/skatteverket-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/skatteverket/refs/heads/main/well-known/skatteverket-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skatteverket-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/skatteverket/refs/heads/main/hosts/skatteverket-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skatteverket-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skatteverket/refs/heads/main/security/skatteverket-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/skatteverket-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/skatteverket/refs/heads/main/security/skatteverket-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skatteverket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skatteverket.se/
coverage:
  checked: '2026-10-15'
  detail: The API host https://api.skatteverket.se returned HTTP 400 for OpenAPI endpoints and no documentation pages were found.
  evidence:
  - status: 400
    url: https://api.skatteverket.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Skatteverket is Sweden’s national tax authority, responsible for tax collection, registration, and enforcement for individuals and businesses. It provides a wide range of e‑services, including tax filing, personal identification numbers, and information on duties and benefits. The agency aims to simplify tax processes through digital services and transparent communication with the public.
image: https://skatteverket.se/images/18.35c34f651660af3747c16d7/1538124880511/skv-fb-liggande.png
layout: provider
modified: '2026-10-15'
name: Skatteverket
nav: Providers
network: true
overview: Skatteverket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Taxation, Sweden, Public Services, and Finance.
random_paper: 11
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 7
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
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Skatteverket Domain Security
  slug: skatteverket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Skatteverket Vulnerability Disclosure
  slug: skatteverket-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: skatteverket
tags:
- Government
- Taxation
- Sweden
- Public Services
- Finance
website: https://skatteverket.se/
---
