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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nugit
- group: build
  title: ''
  type: Packages
  url: packages/nugit-packages.yml
coverage:
  checked: '2026-08-13'
  detail: Nugit is dead and its domain has been taken over — https://nugit.co/ now returns 200 serving an Indonesian online-gambling doorway page (ALEXISTOGEL), www.nugit.co redirects cross-site to an unrelated German business, and nugit.io is parked for sale, leaving the dormant github.com/nugit org (45 repos, no API contract, last substantive commit 2023) as the company's only surviving public surface.
  evidence:
  - status: 200
    url: https://nugit.co/
  - status: 200
    url: https://www.nugit.co/
  - status: 404
    url: https://nugit.co/openapi.json
  - status: 404
    url: https://nugit.co/.well-known/agent-card.json
  - status: 404
    url: https://nugit.co/llms.txt
  - status: 403
    url: https://nugit.io/
  - status: 200
    url: https://api.github.com/orgs/nugit
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Nugit was a Singapore-based data-storytelling and marketing-analytics company, founded in 2013 and backed by 500 Global. Its product pulled marketing, advertising and web-analytics data from multiple sources and used natural language generation to turn it into automated narrative reports and visual "data stories" for brand and agency teams. Nugit never published a public developer API, portal, reference or machine-readable specification, and the company is now defunct: the nugit.co domain has been lost to an unrelated registrant and serves an online gambling / SEO-spam site. The only surviving first-party surface is the dormant github.com/nugit engineering organization.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nugit.png
layout: provider
modified: '2026-08-13'
name: Nugit
nav: Providers
network: true
overview: Nugit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Data Storytelling, Marketing Analytics, and Reporting.
random_paper: 5
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 2
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
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nugit/refs/heads/main/screenshots/nugit-2026-08-07T185721.png
slug: nugit
tags:
- Company
- Analytics
- Data Storytelling
- Marketing Analytics
- Reporting
- Singapore
---
