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
api_count: 1
apis:
- description: Image sharing platform for anime images
  name: Waifu.pics
  slug: waifupics
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waifu-pics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waifu.pics/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Image sharing platform for anime images
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waifu-pics.png
layout: provider
modified: '2026-05-28'
name: Waifu.pics
nav: Providers
network: true
overview: Waifu.pics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anime and Public APIs.
random_paper: 8
score:
  band: minimal
  composite: 6.7
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waifu-pics/refs/heads/main/screenshots/waifu-pics-2026-06-20T201207.png
security:
- kind: domain-security
  name: Waifu Pics Domain Security
  slug: waifu-pics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: waifu-pics
tags:
- Anime
- Public APIs
website: https://waifu.pics/docs
---
