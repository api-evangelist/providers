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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-12'
  detail: Boost Media closed after AdLabs Technology bought its assets in April 2019; boostmedia.com is now a GoDaddy parking lander that soft-200s every path with a 114-byte HTML redirect shell, boostctr.com redirects to a HugeDomains for-sale page, the acquirer's adlabs.ai does not resolve, and the Internet Archive record of the site shows only a WordPress marketing blog with no developer or API path.
  evidence:
  - status: 200
    url: https://boostmedia.com/
  - status: 200
    url: https://boostmedia.com/.well-known/agent-card.json
  - status: 200
    url: https://boostmedia.com/openapi.json
  - status: 200
    url: https://boostctr.com/
  - status: 0
    url: https://adlabs.ai/
  reason: defunct
  state: none
created: '2026-07-17'
description: Boost Media (formerly BoostCTR) was a digital-advertising creative-optimization SaaS platform that paired machine-learning analysis with a curated marketplace of more than 1,000 human writers and designers to test and improve ad creative across paid search, social, video, and display campaigns. Its technology powered roughly $1 billion in paid-search advertising for around 100 global brands across retail, education, financial services, healthcare and insurance, gaming, auto, and travel. Backed by Battery Ventures (Series C, $19M, 2014), Founder Collective, and 500 Global, the company raised about $42.8M total before being acquired by AdLabs Technology in April 2019. The company is now closed; its former domain (boostmedia.com) has been released and now serves a GoDaddy parking lander, and the acquirer's own domain (adlabs.ai) no longer resolves. This profile is retained as a Battery Ventures portfolio record. No public API, developer portal, or specification surface exists to
  enrich — the Internet Archive record of boostmedia.com shows a WordPress marketing site and blog only, with no developer, docs, or API path ever published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boost-media.png
layout: provider
modified: '2026-08-12'
name: Boost Media
nav: Providers
network: true
overview: Boost Media is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Creative Optimization, and Paid Search.
random_paper: 16
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 0
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
slug: boost-media
tags:
- Company
- Advertising
- Marketing
- Creative Optimization
- Paid Search
- Digital Advertising
- Software-as-a-Service
- AdTech
---
