---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Marketman Agentic Access
  operation_count: 24
  slug: marketman-agentic-access
  summary_line: 24 operations · 24 acting
api_count: 9
apis:
- description: Authorised buyer accounts and connected POS systems.
  name: MarketMan Accounts API
  slug: marketman-accounts-api
- description: Token acquisition and token status.
  name: MarketMan Authentication API
  slug: marketman-authentication-api
- description: Vendor delivery notes and document submission.
  name: MarketMan Deliveries API
  slug: marketman-deliveries-api
- description: Invoices and accounting documents.
  name: MarketMan Docs API
  slug: marketman-docs-api
- description: Inventory items, counts, transfers, waste, and UOM types.
  name: MarketMan Inventory API
  slug: marketman-inventory-api
- description: Vendors connected to a buyer account.
  name: MarketMan Items API
  slug: marketman-items-api
- description: Purchase orders and vendor catalog items.
  name: MarketMan Orders API
  slug: marketman-orders-api
- description: Menu items, availability, and menu profitability.
  name: MarketMan Recipes API
  slug: marketman-recipes-api
- description: Webhook subscriptions for order and account events.
  name: MarketMan Webhooks API
  slug: marketman-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: MarketMan API V3
  slug: open-marketman
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marketman-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marketman-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marketman-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marketman
- group: company
  title: ''
  type: Website
  url: https://www.marketman.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.marketman.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/marketman-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marketman-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/marketman-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.marketman.com/blog
created: '2026-06-21'
description: MarketMan is a cloud-based restaurant inventory and purchasing management platform (part of the Meal Ticket portfolio) for back-of-house operations - inventory counts, supplier catalogs, purchase orders, deliveries, invoices, recipes/menu costing, and POS sales. The MarketMan API V3 is a JSON REST API with separate Buyer and Vendor surfaces, token authentication, and webhooks for order events.
finops:
- name: Marketman Finops
  service_category: Management and Governance
  slug: marketman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marketman.png
layout: provider
modified: '2026-06-21'
name: MarketMan
nav: Providers
network: true
overview: 'MarketMan publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Deliveries API, and 6 more. Tagged areas include Restaurant, Inventory, Purchasing, Supply Chain, and Food Service.


  MarketMan''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Marketman Plans Pricing
  plan_count: 3
  slug: marketman-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Marketman Rate Limits
  slug: marketman-rate-limits
score:
  band: thin
  composite: 36.8
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marketman/refs/heads/main/screenshots/marketman-2026-07-25T230236.png
security:
- kind: authentication
  name: Marketman Authentication
  slug: marketman-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marketman Domain Security
  slug: marketman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marketman
tags:
- Restaurant
- Inventory
- Purchasing
- Supply Chain
- Food Service
website: https://www.marketman.com
---
