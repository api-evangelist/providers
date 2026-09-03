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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arrivetech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arrivetech-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.arriveai.com/
- group: company
  title: ''
  type: About
  url: https://www.arriveai.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.arriveai.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.arriveai.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arriveai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.termsfeed.com/live/a14c73d9-ad66-4fd9-aa7f-a4b0f0f3b0dc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.termsfeed.com/live/129c7035-bb28-4c6d-b463-87264126bb07
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.arriveai.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.arriveai.com/press-releases
- group: other
  title: ''
  type: MediaCoverage
  url: https://www.arriveai.com/media-coverage
- group: other
  title: ''
  type: IntellectualProperty
  url: https://www.arriveai.com/intellectual-property
- group: company
  title: ''
  type: Careers
  url: https://www.arriveai.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arriveai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/arrive_ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Arrive_AI
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ArriveAI/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/arrive_ai/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/arrivetech_stock/
coverage:
  checked: '2026-08-06'
  detail: Arrive AI sells a smart-mailbox network but publishes nothing for developers — the word "API" appears nowhere on www.arriveai.com, /developers, /docs, /api, /graphql and /openapi.json all 404, every api./docs./developer./partners. subdomain fails to resolve, and the only integration route is an "integrating with or building on Arrive AI's network" option on the marketing contact form.
  evidence:
  - status: 404
    url: https://www.arriveai.com/developers
  - status: 404
    url: https://www.arriveai.com/openapi.json
  - status: 404
    url: https://www.arriveai.com/.well-known/agent-card.json
  - status: 200
    url: https://www.arriveai.com/solution
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Arrive AI (Nasdaq: ARAI) is an autonomous last-mile delivery company headquartered in Fishers, Indiana, founded by Dan O''Toole and originally operating as DroneDek. Its patented Autonomous Last Mile (ALM) platform is anchored by the Arrive Point, an AI-powered smart mailbox that accepts and dispatches parcels to and from drones, ground robots and human couriers, with temperature-controlled compartments, real-time tracking, smart logistics alerts and chain-of-custody controls aimed at healthcare, pharmacy and e-commerce logistics. The company markets hardware plus a network service; as of this profile it publishes no public developer program, API reference or machine-readable specification.'
image: https://cdn.prod.website-files.com/67c5de33fe42ad3c82b5dbd6/69c56c61748119558955dff3_ArriveAI_Logo.png
layout: provider
modified: '2026-08-06'
name: Arrive AI
nav: Providers
network: true
overview: 'Arrive AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Last Mile Delivery, Autonomous Delivery, and Drones.


  Arrive AI''s developer surface includes engineering blog, support, YouTube channel, and 17 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arrivetech/refs/heads/main/screenshots/arrivetech-2026-08-07T161735.png
security:
- kind: domain-security
  name: Arrivetech Domain Security
  slug: arrivetech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arrivetech
tags:
- Company
- Logistics
- Last Mile Delivery
- Autonomous Delivery
- Drones
- Robotics
- Smart Lockers
- Healthcare Logistics
- Supply Chain
- Internet of Things
website: https://www.arriveai.com/
---
