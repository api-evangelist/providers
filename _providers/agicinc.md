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
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agicinc/refs/heads/main/security/agicinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agicinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elephantech.com/en/
- group: company
  title: ''
  type: Blog
  url: https://elephantech.com/en/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://elephantech.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elephantech
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elephantech.com/en/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://elephantech.com/en/inquiry/
coverage:
  checked: '2026-09-12'
  detail: Elephantech (the current name of AgIC Inc.) manufactures inkjet printing equipment, conductive materials and flexible printed circuit boards — physical goods — and its 64-page WordPress marketing site has no developer, API or reference section at all; every probed contract path redirects to the site root.
  evidence:
  - status: 302
    url: https://elephantech.com/openapi.json
  - status: 302
    url: https://elephantech.com/.well-known/agent-card.json
  - status: 302
    url: https://elephantech.com/llms.txt
  - status: 200
    url: https://elephantech.com/sitemap.xml
  - status: 200
    url: https://elephantech.com/en/
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: Elephantech Inc. (founded January 2014 in Tokyo as AgIC Inc., renamed Elephantech in September 2017) develops, manufactures and sells precision metal inkjet printing equipment, advanced conductive materials, and flexible printed circuit board products, including its SustainaCircuits multilayer PCB line and NeuralJet printing technology. The company positions itself as decarbonizing electronics manufacturing by replacing subtractive copper etching with additive inkjet deposition. It is a hardware and materials manufacturer with roughly 150 employees, headquartered at 4-3-8 Hatchobori, Chuo-ku, Tokyo; it publishes no developer program, public API, SDK or machine-readable API contract.
image: https://elephantech.com/cms/wp-content/uploads/2024/08/elephantech_corpweb_ptc_topview.png
layout: provider
modified: '2026-09-12'
name: Elephantech
nav: Providers
network: true
overview: 'Elephantech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Electronics, Hardware, and Printed Circuit Boards.


  Elephantech''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 7.9
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agicinc Domain Security
  slug: agicinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agicinc
tags:
- Company
- Manufacturing
- Electronics
- Hardware
- Printed Circuit Boards
- Materials
- Sustainability
- Japan
website: https://elephantech.com/en/
---
