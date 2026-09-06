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
  url: security/propagate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://propagatebrands.com
coverage:
  checked: '2026-08-13'
  detail: propagatebrands.com and www.propagatebrands.com still resolve to Webflow's shared proxy but abort every TLS handshake with an internal error, so not one HTTP response came back — and the Wayback record shows the site 403/404ing since July 2024 and serving a 545-byte parked lander by August 2025, with no api/app/docs/developers subdomain, GitHub org, or package-registry presence anywhere.
  evidence:
  - status: 0
    url: https://propagatebrands.com/
  - status: 0
    url: https://www.propagatebrands.com/
  - status: 301
    url: http://propagatebrands.com/
  - status: 0
    url: https://propagatebrands.com/openapi.json
  - status: 0
    url: https://propagatebrands.com/.well-known/agent-card.json
  - status: 200
    url: http://web.archive.org/web/20250806030036/http://propagatebrands.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: Propagate (Propagate Brands) is an e-commerce accelerator and equity syndication platform founded by JD Jernigan and backed by 500 Global. It partners with early-stage direct-to-consumer brands selling on Shopify and Amazon — typically those under $1M in annual revenue and overlooked by larger aggregators — providing working capital plus growth marketing, branding, data collection, customer service, and supply-chain support to help them scale and reach acquisition-ready exits. It simultaneously lets individual investors take equity stakes in these growing private commerce brands to earn passive income. Propagate operates as a services-and-investment business rather than a software company and publishes no public developer API, SDK, or technical platform surface. As of August 2026 its website is also no longer reachable — propagatebrands.com and its www host resolve to Webflow's shared proxy but abort the TLS handshake, and archived captures show the site returning 403/404 since
  mid-2024 and a parked lander page by August 2025.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/propagate.png
layout: provider
modified: '2026-08-13'
name: Propagate
nav: Providers
network: true
overview: Propagate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Direct to Consumer, Shopify, and Accelerator.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Propagate Domain Security
  slug: propagate-domain-security
  summary_line: no transport/DNS hardening detected
slug: propagate
tags:
- Company
- E-Commerce
- Direct to Consumer
- Shopify
- Accelerator
- Investment
- Growth Marketing
website: https://propagatebrands.com
---
