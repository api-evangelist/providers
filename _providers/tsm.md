---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.tsm.gg/'', ''status'': 301, ''note'': ''declared website redirects to https://tsmshop.com/ — a different registrable domain (tsm.gg -> tsmshop.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/tsm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tsm.gg/
- group: other
  title: ''
  type: Store
  url: https://tsmshop.com/
created: '2026-07-17'
description: 'TSM (Team SoloMid) is a North American esports and gaming lifestyle organization, surfaced as a portfolio company of Bessemer Venture Partners in the consumer sector. Its public web presence at tsm.gg redirects to the official TSM Store (tsmshop.com), a Shopify-hosted storefront selling TSM apparel and accessories. An enrichment pass on 2026-07-21 found no first-party developer API surface: no developer portal, no API documentation, no OpenAPI, no resolving developer/api/docs subdomains, and no real /.well-known/ discovery documents (every probed path returned the storefront catch-all page). This profile is retained as a consumer-brand lead with only domain-security signals captured.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tsm.png
layout: provider
modified: '2026-07-21'
name: TSM
nav: Providers
network: true
overview: TSM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Esports, Gaming, and E-Commerce.
random_paper: 4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/tsm/refs/heads/main/screenshots/tsm-2026-09-02T164445.png
security:
- kind: domain-security
  name: Tsm Domain Security
  slug: tsm-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tsm
tags:
- Company
- Consumer
- Esports
- Gaming
- E-Commerce
- Merchandise
- Retail
website: https://www.tsm.gg/
---
