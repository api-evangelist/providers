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
api_count: 1
apis:
- description: Ground station reservation service API for ArkEdge Space satellites.
  name: Clover API
  slug: clover-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arkedgespace/refs/heads/main/llms/arkedgespace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arkedgespace-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arkedgespace/refs/heads/main/well-known/arkedgespace-careers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arkedgespace-careers-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arkedgespace/refs/heads/main/well-known/arkedgespace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arkedgespace-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arkedgespace/refs/heads/main/hosts/arkedgespace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arkedgespace-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arkedgespace/refs/heads/main/vendors/arkedgespace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arkedgespace-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arkedgespace.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://arkedgespace.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arkedge
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arkedgespace/refs/heads/main/security/arkedgespace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkedgespace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arkedgespace.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://arkedgespace.com/mcp
  - status: 403
    url: https://equityzen.com/company/arkedgespace
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: ArkEdge Space is a Japanese satellite technology company developing low‑Earth‑orbit positioning, navigation and timing (LEO‑PNT) services, maritime communication, lunar infrastructure and deep‑space exploration capabilities. It builds its own satellites, onboard computers and ground‑segment solutions to empower safe, connected futures for people and industries worldwide.
image: https://arkedgespace.com/wp-content/uploads/2023/11/eyecatch_common_1-1-1.png
layout: provider
modified: '2026-09-26'
name: Arkedgespace
nav: Providers
network: true
overview: Arkedgespace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, SpaceTech, LEO, and Navigation.
random_paper: 15
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arkedgespace Domain Security
  slug: arkedgespace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arkedgespace
tags:
- Company
- Satellite
- SpaceTech
- LEO
- Navigation
website: https://arkedgespace.com
---
