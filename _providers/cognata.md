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
api_count: 1
apis:
- description: Public API endpoints are not publicly documented; no OpenAPI spec was found.
  name: Cognata API
  slug: cognata-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognata/refs/heads/main/well-known/cognata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cognata-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cognata/refs/heads/main/hosts/cognata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cognata-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cognata.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cognata.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cognata.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.cognata.com/jp/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognata/refs/heads/main/security/cognata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cognata.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cognata.com
  - status: 403
    url: https://forgeglobal.com/cognata_stock/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cognata provides a comprehensive autonomy platform for developing, testing, and validating autonomous vehicle software. Their simulation tools enable large‑scale scenario generation, hardware‑in‑the‑loop testing, and sensor simulation across automotive, drone, and industrial use cases. Cognata serves automotive OEMs, defense, smart‑city, and logistics sectors, offering datasets, validation white‑papers, and a cloud‑based development environment to accelerate safe deployment of autonomous systems.
image: https://www.cognata.com/wp-content/uploads/2022/07/preview-image.png
layout: provider
modified: '2026-10-09'
name: Cognata
nav: Providers
network: true
overview: 'Cognata is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Vehicles, Simulation, Defense, Off‑Road, and Hardware Retrofit.


  Cognata''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cognata Domain Security
  slug: cognata-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cognata
tags:
- Autonomous Vehicles
- Simulation
- Defense
- Off‑Road
- Hardware Retrofit
- AI Data Augmentation
- Sensor Fusion
website: https://www.cognata.com
---
