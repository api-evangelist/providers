---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.4
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resynergi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://resynergi.com/
- group: company
  title: ''
  type: About
  url: https://resynergi.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://resynergi.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://resynergi.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://resynergi.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://resynergi.com/faqs/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/resynergi-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/resynergi-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/resynergi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/resynergi-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/resynergi-conformance.yml
coverage:
  checked: '2026-08-26'
  detail: Resynergi sells physical Continuous Microwave Assisted Pyrolysis modules through Lummus Technology, and resynergi.com is an eight-page WordPress marketing site with no developer section at all — the only machine-readable surfaces on the domain are WordPress.com platform defaults (the /wp-json/ REST index and an OAuth-gated MCP adapter at /wp-json/mcp/mcp-oauth-server), while every OpenAPI, GraphQL, llms.txt and agent-card path returns 404 and api./docs./developer.resynergi.com do not resolve.
  evidence:
  - status: 404
    url: https://resynergi.com/openapi.json
  - status: 404
    url: https://resynergi.com/graphql
  - status: 404
    url: https://resynergi.com/llms.txt
  - status: 404
    url: https://resynergi.com/.well-known/agent-card.json
  - status: 0
    url: https://api.resynergi.com/
  - status: 200
    url: https://resynergi.com/wp-json/
  - status: 401
    url: https://resynergi.com/wp-json/mcp/mcp-oauth-server
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Resynergi is an advanced plastic recycling technology company that builds modular Continuous Microwave Assisted Pyrolysis (CMAP) systems, marketed as AMP Modules, which convert hard-to-recycle waste plastics (HDPE, LDPE, polypropylene and polystyrene) into circular pyrolysis oil (PyOil) and other petrochemical feedstocks. Each 440 sq ft module is designed to process roughly 5 tons of plastic waste per day and produce about 1,000 gallons of PyOil per day, and the company claims a conversion roughly twenty times faster than conventional pyrolysis with a large reduction in CO2-equivalent emissions. Founded in 2015 by Jason Tanne and Brian Bauer around microwave pyrolysis research from the University of Minnesota, Resynergi commercializes its modules in partnership with Lummus Technology, which sells the AMP Modules, and also operates plants near the source of waste under a partner model. This is an industrial process-equipment business; it is not a software vendor and publishes
  no developer program, API, SDK or machine-readable API contract.
image: https://resynergi.com/wp-content/uploads/2026/04/cropped-resynergi-colors-logo-ball-192x192.png
layout: provider
modified: '2026-08-26'
name: Resynergi
nav: Providers
network: true
overview: 'Resynergi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advanced Recycling, Plastics, Pyrolysis, and Circular Economy.


  Resynergi''s developer surface includes engineering blog, support, FAQ, and 9 more developer resources.'
plans:
- name: Resynergi Plans Pricing
  plan_count: 0
  slug: resynergi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Resynergi Rate Limits
  slug: resynergi-rate-limits
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 9.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/resynergi/refs/heads/main/screenshots/resynergi-2026-09-02T153612.png
security:
- kind: domain-security
  name: Resynergi Domain Security
  slug: resynergi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: resynergi
tags:
- Company
- Advanced Recycling
- Plastics
- Pyrolysis
- Circular Economy
- Sustainability
- Waste Management
- Energy
- Industrial Equipment
- Climate Tech
website: https://resynergi.com/
---
