---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Marketman Agentic Access
  operation_count: 24
  slug: marketman-agentic-access
  summary_line: 24 operations · 24 acting
api_count: 1
apis:
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Authorised buyer accounts and connected POS systems.
  name: MarketMan Accounts API
  slug: marketman-accounts-api
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Token acquisition and token status.
  name: MarketMan Authentication API
  slug: marketman-authentication-api
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Vendor delivery notes and document submission.
  name: MarketMan Deliveries API
  slug: marketman-deliveries-api
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Invoices and accounting documents.
  name: MarketMan Docs API
  slug: marketman-docs-api
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Inventory items, counts, transfers, waste, and UOM types.
  name: MarketMan Inventory API
  slug: marketman-inventory-api
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Vendors connected to a buyer account.
  name: MarketMan Items API
  slug: marketman-items-api
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Purchase orders and vendor catalog items.
  name: MarketMan Orders API
  slug: marketman-orders-api
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Menu items, availability, and menu profitability.
  name: MarketMan Recipes API
  slug: marketman-recipes-api
- baseURL: https://api.marketman.com/v3
  baseurl_source: declared
  description: Webhook subscriptions for order and account events.
  name: MarketMan Webhooks API
  slug: marketman-webhooks-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MarketMan API V3 Accounts API
  slug: open-marketman-accounts-api
- collection_type: open
  name: MarketMan API V3 Accounts Authentication API
  slug: open-marketman-authentication-api
- collection_type: open
  name: MarketMan API V3 Accounts Deliveries API
  slug: open-marketman-deliveries-api
- collection_type: open
  name: MarketMan API V3 Accounts Docs API
  slug: open-marketman-docs-api
- collection_type: open
  name: MarketMan API V3 Accounts Inventory API
  slug: open-marketman-inventory-api
- collection_type: open
  name: MarketMan API V3 Accounts Items API
  slug: open-marketman-items-api
- collection_type: open
  name: MarketMan API V3 Accounts Orders API
  slug: open-marketman-orders-api
- collection_type: open
  name: MarketMan API V3 Accounts Recipes API
  slug: open-marketman-recipes-api
- collection_type: open
  name: MarketMan API V3 Accounts Webhooks API
  slug: open-marketman-webhooks-api
- collection_type: open
  name: MarketMan API V3
  slug: open-marketman
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/marketman-capability-edges.yml
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


  MarketMan''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Marketman Plans Pricing
  plan_count: 3
  slug: marketman-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Marketman Rate Limits
  slug: marketman-rate-limits
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
