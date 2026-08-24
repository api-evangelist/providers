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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: Packages
  url: packages/convertro-inc-packages.yml
coverage:
  checked: '2026-08-12'
  detail: Convertro was acquired by AOL in 2014 and fully absorbed into the Verizon Media / Yahoo ad stack; its last remaining asset, convertro.com, is a bare 301 to verizonmedia.com that lands on the Yahoo Inc. corporate homepage, and no api., docs., developer. or www. subdomain resolves to a live service.
  evidence:
  - status: 301
    url: https://convertro.com/
  - status: 200
    url: https://www.yahooinc.com/
  - status: 301
    url: https://convertro.com/openapi.json
  - status: 301
    url: https://convertro.com/.well-known/api-catalog
  - status: 0
    url: https://api.convertro.com/
  - status: 0
    url: https://docs.convertro.com/
  - status: 0
    url: https://developer.convertro.com/
  - status: 404
    url: https://pypi.org/pypi/convertro/json
  - status: 404
    url: https://rubygems.org/api/v1/gems/convertro.json
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Convertro, Inc. was a marketing analytics company based in Santa Monica, California, providing a multi-touch attribution platform that measured the ROI of marketing touchpoints across online and offline media using algorithmic attribution models. Backed by Bessemer Venture Partners, Convertro was acquired by AOL in 2014 and folded into the AOL/Verizon (now Yahoo) advertising stack. It no longer operates an independent public developer surface: convertro.com redirects to yahooinc.com, and no developer portal, documentation, API, or reachable API host was found during enrichment. This profile is retained as a network record; there is no live provider API surface to enrich.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convertro-inc.png
layout: provider
modified: '2026-08-12'
name: Convertro, Inc.
nav: Providers
network: true
overview: Convertro, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Attribution, Analytics, and Advertising.
random_paper: 9
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
slug: convertro-inc
tags:
- Company
- Marketing
- Attribution
- Analytics
- Advertising
- Marketing Technology
---
