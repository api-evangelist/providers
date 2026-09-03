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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glasspoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.glasspoint.com/
- group: company
  title: ''
  type: About
  url: https://www.glasspoint.com/about
- group: other
  title: ''
  type: Product
  url: https://www.glasspoint.com/technology
- group: other
  title: ''
  type: Customers
  url: https://www.glasspoint.com/projects
- group: company
  title: ''
  type: News
  url: https://www.glasspoint.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.glasspoint.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.glasspoint.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glasspoint-inc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/glasspointsolar
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/Glasspointsolar
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/glasspoint_stock/
coverage:
  checked: '2026-08-22'
  detail: GlassPoint sells enclosed-trough solar thermal plants and Steam-as-a-Service contracts for industrial heat, and its entire web presence is a 24-page Squarespace marketing and press site with no developer, docs, or API section in its own sitemap and no GitHub organization.
  evidence:
  - status: 200
    url: https://www.glasspoint.com/sitemap.xml
  - status: 404
    url: https://www.glasspoint.com/openapi.json
  - status: 404
    url: https://www.glasspoint.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/glasspoint
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'GlassPoint is an industrial solar process heat company founded in 2009 that designs, builds, owns and operates enclosed-trough solar thermal systems delivering steam to industrial customers under a Steam-as-a-Service model. Its enclosed trough places mirrors inside a glasshouse to cut capital cost and wind loading, and it has delivered commercial solar process steam since the Amal project in Oman went online in 2012, followed by Miraah and the Ma''aden Solar I project in Saudi Arabia. The company sells decarbonized industrial heat and energy plants, not software: it operates a marketing and press site at glasspoint.com and publishes no developer program, API, SDK, or machine-readable specification of any kind.'
image: https://static1.squarespace.com/static/622ba70eb380531fbf6cb5df/t/6a3931508a10fa02d8b47a27/1784668758101/GlassPoint-social-1200x630.jpg?format=1500w
layout: provider
modified: '2026-08-22'
name: GlassPoint
nav: Providers
network: true
overview: 'GlassPoint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Solar, Industrial, and Sustainability.


  GlassPoint''s developer surface includes product news, YouTube channel, and 10 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glasspoint/refs/heads/main/screenshots/glasspoint-2026-09-02T145605.png
security:
- kind: domain-security
  name: Glasspoint Domain Security
  slug: glasspoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glasspoint
tags:
- Company
- Energy
- Solar
- Industrial
- Sustainability
- Clean Energy
- Manufacturing
- Oil and Gas
website: https://www.glasspoint.com/
---
