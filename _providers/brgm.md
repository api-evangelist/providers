---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/brgm/security/brgm-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/brgm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/brgm/well-known/brgm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/brgm-security.txt
- group: agent
  href: https://artifacts.apis.io/brgm/well-known/brgm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brgm-well-known.yml
- group: other
  href: https://artifacts.apis.io/brgm/hosts/brgm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brgm-hosts.yml
- group: auth
  href: https://artifacts.apis.io/brgm/security/brgm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brgm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/brgm/security/brgm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brgm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.brgm.fr
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: http://www.brgm.fr
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Le BRGM (Bureau de Recherches Géologiques et Minières) is the French national geological service, a public establishment of reference in Earth sciences applications. It manages soil and subsoil resources and risks, providing research, expertise, and data for sustainable development, environmental protection, and hazard mitigation across France and internationally.
layout: provider
modified: '2026-10-23'
name: BRGM
nav: Providers
network: true
overview: BRGM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geology, EarthScience, PublicService, and France.
random_paper: 16
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brgm Domain Security
  slug: brgm-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Brgm Vulnerability Disclosure
  slug: brgm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brgm
tags:
- Company
- Geology
- EarthScience
- PublicService
- France
website: http://www.brgm.fr
---
