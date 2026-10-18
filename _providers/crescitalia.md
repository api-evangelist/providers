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
- description: CrescItalia provides financial solutions for SMEs but no public developer program or API documentation is available.
  name: CrescItalia API
  slug: crescitalia-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crescitalia/refs/heads/main/hosts/crescitalia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crescitalia-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crescitalia/refs/heads/main/security/crescitalia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crescitalia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crescitalia-mctech.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://crescitalia-mctech.com
  - status: 403
    url: https://equityzen.com/company/crescitalia
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Crescitalia is a stub entry in the API Evangelist catalog, originating from a secondary-market harvest. The company’s public presence is currently limited, with no verified corporate website or detailed public documentation. This placeholder entry awaits further discovery of official resources, such as a corporate domain, API specifications, or developer portals, to enrich its profile for API consumers and integrators.
layout: provider
modified: '2026-10-11'
name: Crescitalia
nav: Providers
network: true
overview: Crescitalia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Investment, Technology, and Startups.
random_paper: 12
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crescitalia Domain Security
  slug: crescitalia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crescitalia
tags:
- Company
- Finance
- Investment
- Technology
- Startups
- Europe
website: https://crescitalia-mctech.com
---
