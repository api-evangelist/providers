---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.shopkeep.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.lightspeedhq.com/shopkeep/ — a different registrable domain (shopkeep.com -> lightspeedhq.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/lightspeed/
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
overview: 'Shopkeep is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Retail, Payments, and Small Business.


  Shopkeep''s developer surface includes support and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 2.8
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 2.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopkeep/refs/heads/main/screenshots/shopkeep-2026-09-02T155300.png
security:
- kind: domain-security
  name: Shopkeep Domain Security
  slug: shopkeep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopkeep
tags:
- Company
- Point-of-Sale
- Retail
- Payments
- Small Business
- iPad
- Lightspeed
website: https://www.shopkeep.com
---
