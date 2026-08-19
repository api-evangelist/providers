---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: 3Plcentral Agentic Access
  operation_count: 15
  slug: 3plcentral-agentic-access
  summary_line: 15 operations · 3 acting
api_count: 9
apis:
- description: OAuth 2.0 client-credentials token issuance.
  name: 3PL Warehouse Manager Authentication API
  slug: 3plcentral-authentication-api
- description: Customers (merchants) a 3PL fulfills for.
  name: 3PL Warehouse Manager Customers API
  slug: 3plcentral-customers-api
- description: On-hand inventory and per-receive stock details.
  name: 3PL Warehouse Manager Inventory API
  slug: 3plcentral-inventory-api
- description: Customer SKU items (catalog).
  name: 3PL Warehouse Manager Items API
  slug: 3plcentral-items-api
- description: Outbound order creation and retrieval.
  name: 3PL Warehouse Manager Orders API
  slug: 3plcentral-orders-api
- description: Packages (cartons) on a shipped order.
  name: 3PL Warehouse Manager Packages API
  slug: 3plcentral-packages-api
- description: Inbound receivers (Advance Ship Notices).
  name: 3PL Warehouse Manager Receivers API
  slug: 3plcentral-receivers-api
- description: Rolled-up on-hand / available / allocated quantities.
  name: 3PL Warehouse Manager Stock Summaries API
  slug: 3plcentral-stock-summaries-api
- description: Facilities and their bin locations.
  name: 3PL Warehouse Manager Warehouses API
  slug: 3plcentral-warehouses-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication API
  slug: open-3plcentral-authentication-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication Customers API
  slug: open-3plcentral-customers-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication Inventory API
  slug: open-3plcentral-inventory-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication Items API
  slug: open-3plcentral-items-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication Orders API
  slug: open-3plcentral-orders-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication Packages API
  slug: open-3plcentral-packages-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication Receivers API
  slug: open-3plcentral-receivers-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication Stock Summaries API
  slug: open-3plcentral-stock-summaries-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST Authentication Warehouses API
  slug: open-3plcentral-warehouses-api
- collection_type: open
  name: 3PL Warehouse Manager (SecureWMS) REST API
  slug: open-3plcentral
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/3plcentral-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/3plcentral-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3plcentral-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/3plcentral-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tpl-central
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/extensiv
- group: company
  title: ''
  type: Website
  url: https://www.extensiv.com/3pl-warehouse-manager
- group: docs
  title: ''
  type: Documentation
  url: https://developer.3plcentral.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/3plcentral-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/3plcentral-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/3plcentral-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.extensiv.com/blog
created: '2026-07-04'
description: 3PL Warehouse Manager is the flagship cloud warehouse management system (WMS) built for third-party logistics providers, now sold under Extensiv and historically known as "3PL Central". Its public integration surface is the SecureWMS REST API (base https://secure-wms.com), used to create and retrieve orders, manage items and inventory, read stock summaries and stock details, submit and track inbound receivers (ASN), and enumerate customers, warehouses/facilities, and locations. Authentication is OAuth 2.0 client-credentials against https://secure-wms.com/AuthServer/api/Token, returning a short-lived bearer token (typically valid 30-60 minutes). This entry documents the 3PL Warehouse Manager / SecureWMS API specifically; the broader Extensiv company (which also spans Order Management, Integration Manager, Fulfillment Marketplace, and Warehouse Analytics) is tracked complementarily under the all/extensiv company entry.
finops:
- name: 3Plcentral Finops
  service_category: Warehouse Management (WMS)
  slug: 3plcentral-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/3plcentral.png
layout: provider
modified: '2026-07-04'
name: 3PL Warehouse Manager
nav: Providers
network: true
overview: '3PL Warehouse Manager publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Customers API, Inventory API, and 6 more. Tagged areas include Warehouse Management, WMS, 3PL, Logistics, and Fulfillment.


  3PL Warehouse Manager''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: 3Plcentral Plans Pricing
  plan_count: 3
  slug: 3plcentral-plans-pricing
random_paper: 122
rate_limits:
- limit_count: 3
  name: 3Plcentral Rate Limits
  slug: 3plcentral-rate-limits
score:
  band: developing
  composite: 40.5
  delta: -0.8
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/3plcentral/refs/heads/main/screenshots/3plcentral-2026-07-25T181157.png
security:
- kind: authentication
  name: 3Plcentral Authentication
  slug: 3plcentral-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: 3Plcentral Domain Security
  slug: 3plcentral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: 3Plcentral Trust Center
  slug: 3plcentral-trust-center
  summary_line: SOC 2, GDPR
slug: 3plcentral
tags:
- Warehouse Management
- WMS
- 3PL
- Logistics
- Fulfillment
- Inventory
- Orders
- SecureWMS
- Extensiv
website: https://www.extensiv.com/3pl-warehouse-manager
---
