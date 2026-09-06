---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  url: security/plantd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plantdmaterials.com/
- group: company
  title: ''
  type: Blog
  url: https://www.plantdmaterials.com/blog
- group: company
  title: ''
  type: About
  url: https://www.plantdmaterials.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.plantdmaterials.com/careers
- group: company
  title: ''
  type: Press
  url: https://www.plantdmaterials.com/press-media
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plantdmaterials/
coverage:
  checked: '2026-08-26'
  detail: Plantd manufactures carbon-negative structural building panels pressed from perennial grass; its entire web presence is a six-page Webflow marketing site (home, about, product, blog, careers, press) with no developer portal, no /api path, no GitHub organisation and no package on any registry.
  evidence:
  - status: 404
    url: https://www.plantdmaterials.com/openapi.json
  - status: 404
    url: https://www.plantdmaterials.com/api-docs
  - status: 404
    url: https://www.plantdmaterials.com/graphql
  - status: 404
    url: https://www.plantdmaterials.com/llms.txt
  - status: 404
    url: https://www.plantdmaterials.com/.well-known/agent-card.json
  - status: 404
    url: https://www.plantdmaterials.com/developers
  - status: 404
    url: https://api.github.com/orgs/plantd
  - status: 200
    url: https://www.plantdmaterials.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Plantd is an American advanced-materials manufacturer based in Oxford, North Carolina, founded in 2021 by former SpaceX engineers Nathan Silvernail (CEO) and Huade Tan (CTO) with Josh Dorfman (CMO). The company grows and harvests fast-growing perennial grass on farms across North Carolina and Virginia and presses it into carbon-negative structural building panels intended to replace oriented strand board (OSB), plywood and other timber-based sheathing. Production runs on a modular, all-electric, closed-loop manufacturing platform in a 150,000+ sq ft facility, with a research farm in Stovall, NC. Customers and partners include homebuilder D.R. Horton and furniture brand Studio TK. Plantd has raised roughly $47.5M across seed, Series A and a $22M Series B (October 2025). Plantd is a physical-goods manufacturer: it publishes no developer program, no public API, and no machine-readable API contract of any kind — this profile records that absence rather than an API surface.'
image: https://cdn.prod.website-files.com/625f19c458e42f47692e03b8/626c2af7a62122515767dbe0_favicon-plantd-256x256-2.png
layout: provider
modified: '2026-08-26'
name: Plantd
nav: Providers
network: true
overview: 'Plantd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Building Materials, Manufacturing, Construction, and Sustainability.


  Plantd''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 5.5
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
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plantd/refs/heads/main/screenshots/plantd-2026-09-02T151424.png
security:
- kind: domain-security
  name: Plantd Domain Security
  slug: plantd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: plantd
tags:
- Company
- Building Materials
- Manufacturing
- Construction
- Sustainability
- Carbon Removal
- Climate Tech
- Advanced Materials
- Agriculture
website: https://www.plantdmaterials.com/
---
