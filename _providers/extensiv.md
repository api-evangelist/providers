---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Extensiv Agentic Access
  operation_count: 14
  slug: extensiv-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 7
apis:
- description: OAuth2-style token endpoint (endpointsConfirmed).
  name: Extensiv Authentication API
  slug: extensiv-authentication-api
- description: Customer/tenant accounts (endpointsModeled).
  name: Extensiv Customers API
  slug: extensiv-customers-api
- description: On-hand inventory and stock summaries (endpointsModeled).
  name: Extensiv Inventory API
  slug: extensiv-inventory-api
- description: Customer SKU/item master (endpointsModeled).
  name: Extensiv Items API
  slug: extensiv-items-api
- description: Sales/fulfillment orders (endpointsModeled).
  name: Extensiv Orders API
  slug: extensiv-orders-api
- description: Inbound receivers / ASNs (endpointsModeled).
  name: Extensiv Receivers API
  slug: extensiv-receivers-api
- description: Physical facilities (endpointsModeled).
  name: Extensiv Warehouses API
  slug: extensiv-warehouses-api
artifact_total: 15
collections:
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled)
  slug: open-extensiv
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/extensiv-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/extensiv-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/extensiv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/extensiv-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/extensiv
- group: company
  title: ''
  type: Website
  url: https://www.extensiv.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.extensiv.com/en_US/rest-api
- group: commercial
  title: ''
  type: Plans
  url: plans/extensiv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/extensiv-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/extensiv-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.extensiv.com/blog
created: '2026-07-04'
description: Extensiv (formerly 3PL Central, rebranded in 2022) is a cloud-native omnichannel fulfillment software company for third-party logistics providers (3PLs) and brands. Its platform combines warehouse management (3PL Warehouse Manager and Warehouse Manager), order management, inventory management, and integration tooling - built from the combination of 3PL Central, Skubana, Scout, and CartRover. The flagship developer surface is the 3PL Warehouse Manager REST API (auth server at secure-wms.com/AuthServer), which exposes orders, inventory, items, customers, receivers/ASN, stock summaries, and warehouses to external integrators. Access is provisioned with Client ID / Client Secret credentials that mint short-lived bearer tokens. NOTE - the SecureWMS/3PL Warehouse Manager REST API itself is documented in more detail in the sibling all/3plcentral entry; this entry profiles the Extensiv company and platform and its relationship to that API.
finops:
- name: Extensiv Finops
  service_category: Supply Chain and Logistics Software
  slug: extensiv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/extensiv.png
layout: provider
modified: '2026-07-04'
name: Extensiv
nav: Providers
network: true
overview: 'Extensiv publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Customers API, Inventory API, and 4 more. Tagged areas include 3PL, Warehouse Management, WMS, Order Management, and Inventory Management.


  Extensiv''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Extensiv Plans Pricing
  plan_count: 4
  slug: extensiv-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 3
  name: Extensiv Rate Limits
  slug: extensiv-rate-limits
score:
  band: thin
  composite: 38.0
  delta: -2.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 50.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/extensiv/refs/heads/main/screenshots/extensiv-2026-07-25T213952.png
security:
- kind: authentication
  name: Extensiv Authentication
  slug: extensiv-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Extensiv Domain Security
  slug: extensiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Extensiv Trust Center
  slug: extensiv-trust-center
  summary_line: SOC 2, GDPR
slug: extensiv
tags:
- 3PL
- Warehouse Management
- WMS
- Order Management
- Inventory Management
- Fulfillment
- Logistics
- Supply Chain
website: https://www.extensiv.com
---
