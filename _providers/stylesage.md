---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://stylesage.co/'', ''status'': 301, ''note'': ''declared website redirects to https://www.centricsoftware.com:443/centric-market-intelligence — a different registrable domain (stylesage.co -> centricsoftware.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stylesage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stylesage.co/
created: '2026-07-17'
description: StyleSage was a fashion and retail market-intelligence startup (Techstars-backed) that applied computer vision and data science to track apparel pricing, assortment, discounting, and trend signals across e-commerce retailers. The stylesage.co domain now redirects to Centric Software, which acquired the product and folded it into its Centric Market Intelligence platform for fashion, footwear, home, and beauty brands. As of this enrichment pass no standalone public developer API, documentation, SDK, or well-known surface is published for StyleSage.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stylesage.png
layout: provider
modified: '2026-07-21'
name: StyleSage
nav: Providers
network: true
overview: StyleSage is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, Market Intelligence, and Analytics.
random_paper: 11
score:
  band: minimal
  composite: 5.0
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
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stylesage/refs/heads/main/screenshots/stylesage-2026-09-02T161052.png
security:
- kind: domain-security
  name: Stylesage Domain Security
  slug: stylesage-domain-security
  summary_line: TLSv1.3 · HSTS
slug: stylesage
tags:
- Company
- Retail
- Fashion
- Market Intelligence
- Analytics
- Computer-Vision
- E-Commerce
website: https://stylesage.co/
---
