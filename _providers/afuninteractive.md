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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afuninteractive/refs/heads/main/security/afuninteractive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afuninteractive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.afun-interactive.com/
- group: company
  title: ''
  type: About
  url: https://www.afun-interactive.com/about/sub01.html
- group: company
  title: ''
  type: Blog
  url: https://www.afun-interactive.com/news/sub01.html
- group: operate
  title: ''
  type: ContactUs
  url: https://www.afun-interactive.com/contact/sub01.html
- group: company
  title: ''
  type: Careers
  url: https://www.afun-interactive.com/career/sub01.html
- group: other
  title: ''
  type: CaseStudies
  url: https://www.afun-interactive.com/works/sub01.html
- group: other
  title: ''
  type: x-secondary-market-listing
  url: https://equityzen.com/company/afuninteractive
coverage:
  checked: '2026-09-12'
  detail: AFUN Interactive is a work-for-hire real-time 3D content studio and virtual-artist management business whose entire public web presence is a six-page Korean corporate brochure (About, Business Area, Our Works, News, Career, Contact) behind a Cafe24 CUPID bot challenge; the challenge was solved and there is no developers, docs, API or downloads section anywhere behind it, no GitHub organization under any AFUN/APOKI/VV name, and no first-party package on npm, PyPI, crates.io or RubyGems.
  evidence:
  - status: 200
    url: https://www.afun-interactive.com/business/sub01.html
  - status: 200
    url: https://www.afun-interactive.com/openapi.json
  - status: 200
    url: https://www.afun-interactive.com/zzz-control-does-not-exist-98765
  - status: 404
    url: https://api.github.com/orgs/afun-interactive
  - status: 404
    url: https://apoki.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: AFUN Interactive (에이펀인터렉티브) is a Seoul-based real-time 3D content production studio founded in 2017 that builds digital humans, virtual celebrities and high-quality real-time 3D media. Its four stated service lines are Digital Celebrity Management, Digital Human (photoreal CG characters and live avatars for hologram, VR, AR and AI concierge use), Ganimation (a real-time animation/game hybrid genre that won at the 2018 Venice International Film Festival), and High Quality Realtime 3D Contents (AR content, car configurators and high-end MR for automotive, entertainment and telecom clients). Through its subsidiary VV Entertainment it produces and manages the virtual K-pop artist APOKI. It is a work-for-hire production and artist-management business that sells finished 3D content, not developer access, and publishes no public API, SDK, developer portal or machine-readable specification.
image: https://www.afun-interactive.com/images/common/linkkakao_bar.jpg
layout: provider
modified: '2026-09-12'
name: AFUN Interactive
nav: Providers
network: true
overview: 'AFUN Interactive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Content Production, Digital Human, Virtual Artists, and Real-Time Rendering.


  AFUN Interactive''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 5.0
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afuninteractive Domain Security
  slug: afuninteractive-domain-security
  summary_line: TLSv1.2
slug: afuninteractive
tags:
- Company
- 3D Content Production
- Digital Human
- Virtual Artists
- Real-Time Rendering
- Entertainment
- Augmented Reality
- Virtual Reality
- South Korea
website: https://www.afun-interactive.com/
---
