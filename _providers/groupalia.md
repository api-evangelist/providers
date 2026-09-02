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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/groupalia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.groupalia.it/
- group: company
  title: ''
  type: WebsiteInactive
  url: http://www.groupalia.com/
created: '2026-07-17'
description: Groupalia was a Spanish group-buying / daily-deals company (a Groupon-style local commerce marketplace) founded in 2010 and backed by investors including Insight Partners, operating across Spain, Italy and parts of Latin America before consolidating in the group-buying downturn. The brand's only active surface today is the Italian domain groupalia.it, a gift-card storefront whose checkout is operated by EPIPOLI S.p.A. (mygiftcard.it); the original www.groupalia.com domain no longer resolves. No public API, developer portal, SDKs, or agent-facing surface is published, so this profile remains a consumer-company identity record rather than an API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groupalia.png
layout: provider
modified: '2026-07-19'
name: Groupalia
nav: Providers
network: true
overview: Groupalia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Daily Deals, Group Buying, and E-Commerce.
random_paper: 19
score:
  band: minimal
  composite: 1.5
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
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/groupalia/refs/heads/main/screenshots/groupalia-2026-07-25T220348.png
security:
- kind: domain-security
  name: Groupalia Domain Security
  slug: groupalia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: groupalia
tags:
- Company
- Consumer
- Daily Deals
- Group Buying
- E-Commerce
- Gift Cards
- Retail
- Spain
website: https://www.groupalia.it/
---
