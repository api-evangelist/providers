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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/whisperaero-com/hosts/whisperaero-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whisperaero-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/whisperaero-com/vendors/whisperaero-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/whisperaero-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.whisper.aero/news
- group: auth
  href: https://artifacts.apis.io/whisperaero-com/security/whisperaero-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whisperaero-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.whisper.aero/
- group: docs
  title: ''
  type: Documentation
  url: https://www.whisper.aero/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.whisper.aero/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.whisper.aero/legal/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.whisper.aero/legal/cookie-policy
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 0
    url: https://api.whisper.aero/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Whisper Aero is a Tennessee‑based aerospace company developing ultra‑quiet, efficient electric propulsion systems for aviation, defense, and commercial applications. Founded in 2020, Whisper Aero builds scalable thrust solutions that reduce noise by up to 20 dB while improving fuel efficiency, aiming to decarbonize air travel and enable silent drones and aircraft. The company operates a flight‑test center in Crossville, partners with state agencies, and offers propulsion technology for a range of customers.
image: https://cdn.prod.website-files.com/64745e1481158ec9ca7d8b69/647af16f393afebb090e1291_Open%20graph.jpg
layout: provider
modified: '2026-10-25'
name: Whisper Aero
nav: Providers
network: true
overview: 'Whisper Aero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Electric Propulsion, Aviation, and Defense.


  Whisper Aero''s developer surface includes documentation and 8 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Whisperaero Com Domain Security
  slug: whisperaero-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: whisperaero-com
tags:
- Company
- Aerospace
- Electric Propulsion
- Aviation
- Defense
website: https://www.whisper.aero/
---
