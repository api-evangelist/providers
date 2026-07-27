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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopkeep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shopkeep.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopkeep
- group: operate
  title: ''
  type: Support
  url: https://shopkeep-support.lightspeedhq.com/
created: '2026-07-17'
description: ShopKeep was a cloud-based iPad point-of-sale (POS) platform for independent retailers, restaurants, and quick-serve businesses, offering register, inventory, employee management, payments, and analytics. Founded in 2008 and backed by Canaan Partners, ShopKeep was acquired by Lightspeed Commerce in 2020 and its product and brand have since been folded into the Lightspeed Retail (S-Series) line. The marketing domain shopkeep.com now redirects to lightspeedhq.com/shopkeep, and support has migrated to shopkeep-support.lightspeedhq.com. ShopKeep never shipped a publicly documented developer API — a private "API beta" existed circa 2015 and the app backend at api.shopkeep.com remains live as a session-authenticated, undocumented internal service. No public OpenAPI, SDKs, developer portal, or API reference are published, so this profile is identity-only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopkeep.png
layout: provider
modified: '2026-07-21'
name: Shopkeep
nav: Providers
network: true
overview: 'Shopkeep is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point of Sale, Retail, Payments, and Small Business.


  Shopkeep''s developer surface includes support and 3 more developer resources.'
random_paper: 47
score:
  band: minimal
  composite: 9.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Shopkeep Domain Security
  slug: shopkeep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopkeep
tags:
- Company
- Point of Sale
- Retail
- Payments
- Small Business
- POS
- iPad
- Lightspeed
website: https://www.shopkeep.com
---
