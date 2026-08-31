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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigbasket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bigbasket.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BigBasket
- group: build
  title: ''
  type: Packages
  url: packages/bigbasket-packages.yml
created: '2026-07-17'
description: 'bigbasket is India''s largest online grocery and daily-essentials retailer, now part of the Tata Group, delivering fresh produce, packaged foods, household, and personal-care products across Indian cities via web and mobile apps (bigbasket, bbnow, and bbdaily subscription delivery). Surfaced as a Bessemer Venture Partners portfolio company and added to the API Evangelist network. bigbasket operates as a consumer app rather than an API platform: it publishes no public developer portal, API documentation, or client SDKs. Its only first-party public developer surface is the github.com/BigBasket organization and the open-source @bb-tech react-admin UI component libraries on npm.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigbasket.png
layout: provider
modified: '2026-07-18'
name: bigbasket
nav: Providers
network: true
overview: bigbasket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Grocery, and Retail.
random_paper: 16
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 3
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
  previous_composite: 5.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bigbasket/refs/heads/main/screenshots/bigbasket-2026-07-25T202926.png
security:
- kind: domain-security
  name: Bigbasket Domain Security
  slug: bigbasket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bigbasket
tags:
- Company
- Consumer
- E-Commerce
- Grocery
- Retail
- Online Grocery
- India
website: https://www.bigbasket.com/
---
