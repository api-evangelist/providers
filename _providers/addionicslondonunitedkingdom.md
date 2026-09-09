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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/addionicslondonunitedkingdom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://addionics.com
- group: company
  title: ''
  type: Blog
  url: https://addionics.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://addionics.com/feed.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/addionicslondonunitedkingdom-llms.txt
- group: other
  title: ''
  type: AgentInstructions
  url: llms/addionicslondonunitedkingdom-agents.md
- group: other
  title: ''
  type: Sitemap
  url: https://addionics.com/sitemap.xml
- group: operate
  title: ''
  type: Contact
  url: https://addionics.com/contact
- group: company
  title: ''
  type: Careers
  url: https://addionics.com/company#open-positions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://addionics.com/legal/terms
- group: other
  title: ''
  type: CookiePolicy
  url: https://addionics.com/legal/cookies
- group: other
  title: ''
  type: Whitepaper
  url: https://5355710.fs1.hubspotusercontent-na1.net/hubfs/5355710/Addionics%20Redefining%20Battery%20Architecture%20White%20Paper.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/addionics
- group: other
  title: ''
  type: X
  url: https://x.com/addionics
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@addionics5387/videos
- group: commercial
  title: ''
  type: Plans
  url: plans/addionicslondonunitedkingdom-plans-pricing.yml
coverage:
  checked: '2026-09-07'
  detail: 'Addionics manufactures Smart 3D porous copper and aluminium current collectors for battery cells — a physical materials product — and its complete /sitemap.xml (200) indexes 150 technology, product, industry and blog pages with no developer, docs or API page anywhere in it, while every contract probe on addionics.com and www.addionics.com (/openapi.json, /swagger.json, /api-docs, /.well-known/api-catalog, /.well-known/agent-card.json) returned 404 and npm, PyPI, crates.io and RubyGems hold no Addionics package; the only machine surface the company does publish is a site-level agent one — /llms.txt, /agents.md, markdown twins under Accept: text/markdown, and an RSS feed — which is captured in llms/.'
  evidence:
  - status: 200
    url: https://addionics.com/sitemap.xml
  - status: 404
    url: https://addionics.com/openapi.json
  - status: 404
    url: https://addionics.com/.well-known/api-catalog
  - status: 200
    url: https://addionics.com/llms.txt
  - status: 200
    url: https://addionics.com/agents.md
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'Addionics is a Smart Metals manufacturer headquartered in London, United Kingdom, with operations in Israel, Korea and the USA, building Smart 3D Porous Current Collectors that replace the flat copper and aluminium foils inside a battery cell with a porous, ion-permeable metal architecture. The technology is chemistry-agnostic and drop-in, produced roll-to-roll on existing coating lines, and is sold into robotics, defence, space and EV programmes. Addionics is a hardware and materials company: it operates no developer program and publishes no API, SDK, webhook or machine-readable API contract. It does run a deliberate agent-readable content surface on its own domain — a served /llms.txt digest, a published /agents.md agent guide, a markdown twin of every page under Accept: text/markdown, a complete /sitemap.xml and an RSS blog feed — all captured in this profile.'
image: https://addionics.com/opengraph-image.png?opengraph-image.0p88m6nhqfsnt.png
layout: provider
modified: '2026-09-07'
name: Addionics
nav: Providers
network: true
overview: 'Addionics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Batteries, Energy Storage, Advanced Materials, and Manufacturing.


  Addionics'' developer surface includes engineering blog, YouTube channel, and 14 more developer resources.'
plans:
- name: Addionicslondonunitedkingdom Plans Pricing
  plan_count: 0
  slug: addionicslondonunitedkingdom-plans-pricing
random_paper: 4
score:
  band: minimal
  composite: 7.4
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
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Addionicslondonunitedkingdom Domain Security
  slug: addionicslondonunitedkingdom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: addionicslondonunitedkingdom
tags:
- Company
- Batteries
- Energy Storage
- Advanced Materials
- Manufacturing
- Electric Vehicles
- Robotics
- Defense
- Space
- Hardware
- United Kingdom
website: https://addionics.com
---
