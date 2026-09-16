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
  scored_at: '2026-09-15'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aillis/refs/heads/main/security/aillis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aillis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aillis.jp/
- group: company
  title: ''
  type: Blog
  url: https://aillis.jp/en/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aillis.jp/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://aillis.jp/en/contact
- group: company
  title: ''
  type: About
  url: https://aillis.jp/about
- group: company
  title: ''
  type: Careers
  url: https://aillis.jp/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aillis-inc/
coverage:
  checked: '2026-09-14'
  detail: Aillis ships nodoca as a finished AI medical device to Japanese clinics, not as a platform — its entire web presence is a STUDIO-built marketing site whose sitemap lists only about, technology, news, careers, privacy, presskit and contact, with no developer, API or docs path anywhere, and contract discovery against aillis.jp, www.aillis.jp and nodoca.aillis.jp found no OpenAPI, GraphQL, MCP, agent card, llms.txt or .well-known document.
  evidence:
  - status: 200
    url: https://aillis.jp/sitemap-static.xml
  - status: 200
    url: https://aillis.jp/openapi.json
  - status: 404
    url: https://nodoca.aillis.jp/openapi.json
  - status: 404
    url: https://nodoca.aillis.jp/.well-known/agent-card.json
  - status: 200
    url: https://aillis.jp/bogus-does-not-exist-xyz
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: 'Aillis, Inc. (アイリス株式会社) is a Tokyo-based medical technology company founded in 2017 that applies machine learning to the diagnosis of infectious disease. Its flagship product, nodoca, is an AI-equipped pharyngeal camera cleared in Japan as an AI-based new medical device for influenza screening: it photographs the posterior pharyngeal wall, detects influenza follicles in the image, and combines those findings with body temperature and reported symptoms to support a physician''s diagnosis. nodoca is sold to clinics and hospitals as a finished end-user medical device; Aillis publishes no public developer portal, API reference, SDK or machine-readable contract of any kind, and its corporate site is a marketing site built on the STUDIO no-code platform.'
image: https://storage.googleapis.com/production-os-assets/assets/b6fd5289-9033-4b4c-8983-676f44998135
layout: provider
modified: '2026-09-14'
name: Aillis
nav: Providers
network: true
overview: 'Aillis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Artificial Intelligence, and Machine-Learning.


  Aillis'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aillis Domain Security
  slug: aillis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aillis
tags:
- Company
- Healthcare
- Medical Devices
- Artificial Intelligence
- Machine-Learning
- Diagnostics
- Medical Imaging
- Japan
website: https://aillis.jp/
---
