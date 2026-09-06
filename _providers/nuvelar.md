---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuvelar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nuvelar.com
- group: start
  title: ''
  type: Login
  url: https://www.nuvelar.com/public/login
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nuvelar-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nuvelar-llms.txt
created: '2026-07-17'
description: Nuvelar is an Argentine technology solutions firm founded in 2014 that designs and builds digital experiences across consulting, hardware, software, and design. Its flagship product, Nuvelar Display, is a cloud platform for creating, distributing, and managing digital-signage content networks with content scheduling, player monitoring, dynamic templates, multi-format support, and social/weather/RSS integrations. Beyond the platform, Nuvelar builds custom interactive installations — videowalls, interactive tables, and branded experiential systems for clients such as Adidas. It was surfaced as a 500 Global portfolio company and added to the API Evangelist network. As of the latest enrichment pass Nuvelar publishes no public API, developer portal, SDK, or specification.
image: https://nuvelar.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Nuvelar
nav: Providers
network: true
overview: Nuvelar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Signage, Digital Experience, Software Development, and Consulting.
random_paper: 9
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 7.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuvelar/refs/heads/main/screenshots/nuvelar-2026-08-07T185801.png
security:
- kind: domain-security
  name: Nuvelar Domain Security
  slug: nuvelar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nuvelar
tags:
- Company
- Digital Signage
- Digital Experience
- Software Development
- Consulting
- Interactive Displays
- Argentina
website: https://nuvelar.com
---
