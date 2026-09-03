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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soda-inc.jp/
- group: company
  title: ''
  type: Website
  url: https://snkrdunk.com/
created: '2026-07-17'
description: SODA Inc. (株式会社SODA) is a Japanese consumer-technology company that operates SNKRDUNK (スニーカーダンク / スニダン), one of Japan's largest consumer-to-consumer marketplaces for sneakers, trading cards ("トレカ"), apparel, and accessories. The SNKRDUNK app lets users buy and sell collectible and secondary-market goods with professional in-house authentication (真贋鑑定 by プロ鑑定士) and a full purchase-protection / compensation guarantee, alongside a buyback service. SODA is a portfolio company of the SoftBank Vision Fund. As a consumer marketplace app, SODA publishes no public developer program or API at this time; this profile captures the company's public identity and domain-security posture for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soda.png
layout: provider
modified: '2026-07-21'
name: SODA
nav: Providers
network: true
overview: SODA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, E-Commerce, and Sneakers.
random_paper: 3
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
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soda/refs/heads/main/screenshots/soda-2026-09-02T160050.png
security:
- kind: domain-security
  name: Soda Domain Security
  slug: soda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soda
tags:
- Company
- Consumer
- Marketplace
- E-Commerce
- Sneakers
- Trading Cards
- Resale
- Japan
- Authentication
website: https://soda-inc.jp/
---
