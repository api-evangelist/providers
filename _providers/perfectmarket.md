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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-13'
  detail: Perfect Market was acquired by Taboola in August 2014 and absorbed into the Taboola-X publisher product; perfectmarket.com still has delegated nameservers and Google Workspace mail but publishes no A or CNAME record on the apex, www, api, developer or docs names, so every HTTP request fails at DNS and no web host, developer portal or API contract survives anywhere under the name.
  evidence:
  - status: 0
    url: https://perfectmarket.com/
  - status: 0
    url: https://api.perfectmarket.com/
  - status: 0
    url: https://developer.perfectmarket.com/
  - status: 404
    url: https://perfectmarket.ai/.well-known/agent-card.json
  - status: 404
    url: https://perfectmarket.ai/openapi.json
  - status: 404
    url: https://pypi.org/pypi/perfectmarket/json
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Perfect Market, Inc. was a digital publishing technology company founded by Idealab in 2007 and backed by Trinity Ventures, building on the Idealab/Overture paid-search lineage. It sold software for driving traffic, engagement and advertising revenue to premium publishers, and claimed more than 200 customers including LATimes.com, ChicagoTribune.com, NBCNews.com, Mediaite.com and BusinessInsider.com. Taboola acquired Perfect Market in August 2014 for cash and stock and folded its programmatic advertising technology into the Taboola-X publisher monetization product. The company no longer operates independently and publishes no API surface: perfectmarket.com retains delegated nameservers and Google Workspace mail but resolves to no web host on the apex, www, api, developer or docs names, so there is no website, developer portal, documentation, or contract to profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perfectmarket.png
layout: provider
modified: '2026-08-13'
name: PerfectMarket
nav: Providers
network: true
overview: PerfectMarket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, Publishing, and Content Monetization.
random_paper: 3
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
slug: perfectmarket
tags:
- Company
- Marketing
- Advertising
- Publishing
- Content Monetization
- Programmatic Advertising
- Acquired
---
