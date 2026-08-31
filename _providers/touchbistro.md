---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 47
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/touchbistro-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/touchbistro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.touchbistro.com/
- group: other
  title: ''
  type: Developer
  url: https://www.touchbistro.com/features/integrations/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TouchBistro
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/touchbistro
- group: commercial
  title: ''
  type: Pricing
  url: https://www.touchbistro.com/pricing/
- group: operate
  title: ''
  type: Help
  url: https://www.touchbistro.com/help/
- group: commercial
  title: ''
  type: Plans
  url: plans/touchbistro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/touchbistro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/touchbistro-finops.yml
created: '2026-05-08'
description: TouchBistro is an iPad-based restaurant point-of-sale (POS) and management platform covering payments, online ordering, reservations, loyalty, gift cards, marketing, inventory, labor, and reporting. TouchBistro does not publish an open, self-serve developer API or a public developer portal; it exposes a private, partner-only integration API. The CEO has publicly confirmed an API exists but is not openly promoted. Third-party software providers must apply to the integration partner program, be approved, and are issued monitored API keys under negotiated commercial terms (contact integratedpartners@touchbistro.com).
features:
- description: Cloud-based iPad POS that is the core engine of restaurant operations.
  name: Point of Sale
- description: TouchBistro Payments plus integrated processing via Chase, Worldpay, and Moneris.
  name: Payment Processing
- description: Mobile POS for capturing orders, upsells, and split checks at the table.
  name: Tableside Ordering
- description: Connects front and back of house for timely order fulfillment.
  name: Kitchen Display System
- description: Direct online ordering through the restaurant's own channels.
  name: Online Ordering
- description: Capacity management, waitlists, and VIP guest handling.
  name: Reservations
- description: Rewards program and modern digital gift cards to drive repeat business.
  name: Loyalty and Gift Cards
- description: Automated, data-driven guest marketing campaigns.
  name: Marketing
- description: Stock tracking to minimize waste and reduce food costs.
  name: Inventory Management
- description: Staff scheduling and payroll cost monitoring.
  name: Labor Management
- description: Cloud reports accessible remotely for data-driven decisions.
  name: Reporting and Analytics
- description: Build menus and design floor layouts, sections, and table status.
  name: Menu and Floor Plan Management
finops:
- name: Touchbistro Finops
  service_category: Payments & POS
  slug: touchbistro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/touchbistro.png
integrations:
- description: Payment processing partner.
  name: Chase
- description: Payment processing partner.
  name: Worldpay
- description: Payment processing partner.
  name: Moneris
- description: Accounting integration.
  name: QuickBooks
- description: Accounting integration.
  name: Xero
- description: Accounting integration.
  name: Sage Intacct
- description: Accounting and inventory integration.
  name: Restaurant365
- description: Accounting, analytics, and inventory integration.
  name: MarginEdge
- description: Accounting automation integration.
  name: Shogo
- description: Sales tax automation integration.
  name: DAVO by Avalara
- description: Business analytics integration.
  name: Avero
- description: Inventory management integration.
  name: WISK.ai
- description: Inventory management integration.
  name: MarketMan
- description: Inventory management integration.
  name: Optimum Control
- description: Inventory management integration.
  name: Craftable
- description: Staff scheduling and labor management integration.
  name: 7shifts
- description: Scheduling and payroll integration.
  name: Push Operations
- description: Online ordering integration.
  name: DoorDash
- description: Delivery aggregator integration.
  name: Deliverect
- description: Delivery aggregator integration.
  name: UrbanPiper
- description: Business insurance integration.
  name: Coverdash
layout: provider
modified: '2026-07-25'
name: TouchBistro
nav: Providers
network: true
overview: 'TouchBistro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include POS, Restaurant, Hospitality, Payments, and Integration.


  TouchBistro''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Touchbistro Plans Pricing
  plan_count: 1
  slug: touchbistro-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Touchbistro Rate Limits
  slug: touchbistro-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/touchbistro/refs/heads/main/screenshots/touchbistro-2026-06-20T195504.png
security:
- kind: domain-security
  name: Touchbistro Domain Security
  slug: touchbistro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Touchbistro Vulnerability Disclosure
  slug: touchbistro-vulnerability-disclosure
  summary_line: disclosure policy published
slug: touchbistro
solutions:
- description: POS and management for full-service dining.
  name: Full-Service Restaurants
- description: Fast ordering and payment for QSR and counter formats.
  name: Quick-Service and Counter Service
- description: Tab management, fast reorders, and floor management for bars.
  name: Bars and Breweries
- description: Quick checkout and loyalty for cafes.
  name: Cafes and Coffee Shops
tags:
- POS
- Restaurant
- Hospitality
- Payments
- Integration
use_cases:
- description: Process in-person and online card payments through integrated processors.
  name: Payment Acceptance
- description: Push sales and labor data to accounting platforms for reconciliation.
  name: Accounting Sync
- description: Sync menu and sales data with inventory tools to manage food cost and waste.
  name: Inventory and Cost Control
- description: Route third-party delivery and online orders into the POS.
  name: Delivery and Online Ordering
- description: Connect labor data to scheduling and payroll providers.
  name: Staff Scheduling and Payroll
website: https://www.touchbistro.com/
---
