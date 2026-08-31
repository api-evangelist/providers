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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lumilens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lumilens.com/
- group: company
  title: ''
  type: Blog
  url: https://lumilens.com/news-insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lumilens.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lumilens.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lumilens-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/lumilens-plans-pricing.yml
coverage:
  checked: '2026-08-25'
  detail: Lumilens sells physical co-packaged and near-packaged optics silicon direct to hyperscalers under negotiated supply agreements, and eleven months after registering a GitHub org it has published zero repositories and lumilens.com is still a five-page Webflow recruiting site whose own footer Blog link is hidden and 404s.
  evidence:
  - status: 404
    url: https://lumilens.com/developers
  - status: 404
    url: https://lumilens.com/openapi.json
  - status: 404
    url: https://lumilens.com/.well-known/agent-card.json
  - status: 0
    url: https://api.lumilens.com/
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: Lumilens is a San Jose, California photonics company building optical interconnect silicon for AI data centers. Founded in 2024 by Ankur Singla (previously Contrail Systems and Volterra) with Ted Schmidt, Samuel Liu, Ritesh Kapahi and Dave Friedman, it designs co-packaged optics (CPO) and near-packaged optics (NPO) devices that let hyperscalers replace copper interconnect with fiber at 800Gb/s, 1.6Tb/s and beyond, attacking the connectivity bottleneck that now limits GPU cluster scaling more than compute does. The company emerged from stealth in August 2026 with more than $900M raised — including a $700M Series C at a $5.51B valuation led by Atreides Management, Bain Capital Ventures, Meritech, Seligman Ventures and Spark Capital — and says it is already shipping production optical interconnect into hyperscale AI data centers under a multi-billion-dollar customer agreement. Its product is physical silicon sold direct to a small set of very large buyers; as of this profile it
  publishes no developer program, API, SDK or machine-readable contract of any kind, and lumilens.com is still an interim recruiting and news site.
image: https://cdn.prod.website-files.com/68aa10a8e6f4d59001f9f05d/68b6c01786ae316e23307b57_Favicon-256x256.png
layout: provider
modified: '2026-08-25'
name: Lumilens
nav: Providers
network: true
overview: 'Lumilens is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Photonics, Optical Networking, Interconnects, and Semiconductors.


  Lumilens'' developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Lumilens Plans Pricing
  plan_count: 0
  slug: lumilens-plans-pricing
random_paper: 12
score:
  band: minimal
  composite: 10.4
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
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Lumilens Domain Security
  slug: lumilens-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lumilens
tags:
- Company
- Photonics
- Optical Networking
- Interconnects
- Semiconductors
- Silicon Photonics
- Data Centers
- Artificial Intelligence
- Hardware
website: https://lumilens.com/
---
