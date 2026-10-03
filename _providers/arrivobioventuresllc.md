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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API surface discovered via host api.arrivobio.com but no machine-readable spec found.
  name: Arrivo Bio API
  slug: arrivo-bio-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arrivobioventuresllc/refs/heads/main/hosts/arrivobioventuresllc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arrivobioventuresllc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arrivobioventuresllc/refs/heads/main/vendors/arrivobioventuresllc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arrivobioventuresllc-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://arrivobio.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arrivobioventuresllc/refs/heads/main/security/arrivobioventuresllc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arrivobioventuresllc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arrivobio.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at api.arrivobio.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.arrivobio.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Arrivobioventuresllc, operating as Arrivo BioVentures, is a holding company overseeing Sirtsei Pharmaceuticals and Panafina Inc., developing innovative medicines such as SP-624 for major depressive disorder and RABI-767 for severe acute pancreatitis. The company focuses on delivering meaningful health outcomes through advanced drug candidates and expanded access programs.
image: https://arrivobio.com/content/uploads/2025/01/Arrivo_transparent.png
layout: provider
modified: '2026-09-26'
name: Arrivobioventuresllc
nav: Providers
network: true
overview: Arrivobioventuresllc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Pharmaceuticals, Holding Company, Clinical Trials, and Mental Health.
random_paper: 2
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arrivobioventuresllc Domain Security
  slug: arrivobioventuresllc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arrivobioventuresllc
tags:
- Biotechnology
- Pharmaceuticals
- Holding Company
- Clinical Trials
- Mental Health
website: https://arrivobio.com
---
