---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Blockout dates
  name: Happy Cabbage Analytics Blockout Dates API
  slug: happy-cabbage-analytics-blockout-dates-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Daily product sales and stock metadata
  name: Happy Cabbage Analytics Daily Sales Metadata API
  slug: happy-cabbage-analytics-daily-sales-metadata-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: API key identity and organization context
  name: Happy Cabbage Analytics Identity API
  slug: happy-cabbage-analytics-identity-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Inventory health data
  name: Happy Cabbage Analytics Inventory Health API
  slug: happy-cabbage-analytics-inventory-health-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Orders
  name: Happy Cabbage Analytics Orders API
  slug: happy-cabbage-analytics-orders-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Package-level product inventory
  name: Happy Cabbage Analytics Packages API
  slug: happy-cabbage-analytics-packages-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Organization POS brand metadata and mappings
  name: Happy Cabbage Analytics POS Brands API
  slug: happy-cabbage-analytics-pos-brands-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Organization POS category metadata and mappings
  name: Happy Cabbage Analytics POS Categories API
  slug: happy-cabbage-analytics-pos-categories-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Product-level inventory, sales, and demand metrics
  name: Happy Cabbage Analytics Product Inventory API
  slug: happy-cabbage-analytics-product-inventory-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Product-line inventory, demand, and replenishment metrics
  name: Happy Cabbage Analytics Product Line Inventory API
  slug: happy-cabbage-analytics-product-line-inventory-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Product-lines
  name: Happy Cabbage Analytics Product Lines API
  slug: happy-cabbage-analytics-product-lines-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Organization location metadata
  name: Happy Cabbage Analytics Stores API
  slug: happy-cabbage-analytics-stores-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Canonical brand metadata across POS systems
  name: Happy Cabbage Analytics Universal Brands API
  slug: happy-cabbage-analytics-universal-brands-api
- baseURL: https://api.happycabbage.ai
  baseurl_source: declared
  description: Canonical product category metadata across POS systems
  name: Happy Cabbage Analytics Universal Categories API
  slug: happy-cabbage-analytics-universal-categories-api
artifact_total: 18
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/happy-cabbage-analytics-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.happycabbage.io/
- group: docs
  title: ''
  type: Documentation
  url: https://cabbage.pub/swagger-ui/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://cabbage.pub/swagger-ui/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.happycabbage.io/the-patch
- group: operate
  title: ''
  type: Support
  url: https://www.happycabbage.io/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.happycabbage.io/buyers-free-trial
- group: start
  title: ''
  type: Login
  url: https://restock.happycabbage.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lrn.mobi/hca_privacy_policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/happycabbage
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.happycabbage.io/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/happy-cabbage-analytics-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/happy-cabbage-analytics-happy-buyers-external-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/happy-cabbage-analytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/happy-cabbage-analytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/happy-cabbage-analytics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/happy-cabbage-analytics-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/happy-cabbage-analytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/happy-cabbage-analytics-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/happy-cabbage-analytics-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/happy-cabbage-analytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/happy-cabbage-analytics-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/happy-cabbage-analytics-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/happy-cabbage-analytics-happy-buyers-external-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/happy-cabbage-analytics-domain-security.yml
created: '2026-08-22'
description: Happy Cabbage Analytics is a cannabis retail software company founded in 2019 and headquartered in San Francisco, California, whose Happy Buyers platform gives dispensary buyers AI-assisted inventory management, demand forecasting, replenishment and purchase-order workflows on top of data pulled from their point-of-sale system. The platform reads live sell-through from POS integrations (Dutchie, Flowhub, Blaze, Treez, Meadow) and wholesale menus (Distru, Apex Trading), then scores inventory health by store, category and brand, predicts days-on-hand, groups SKUs into product lines, and drafts vendor orders with invoices attached. Happy Cabbage sold its Happy Marketers text-marketing suite to Alpine IQ in June 2025 and now focuses on Happy Buyers. A public Happy Buyers External API entered beta in June 2026 and is documented with a Swagger UI, exposing organization metadata, inventory health, product/product-line inventory, packages, daily sales metadata and full order management
  to API-key holders — the same API the company's own published AI-agent workflows are built on.
image: https://cdn.prod.website-files.com/5d46254e52d2932dcbc10ee9/65cba367661e3aebedb84daf_HCA_Logo_primary.png
layout: provider
modified: '2026-08-22'
name: Happy Cabbage Analytics
nav: Providers
network: true
overview: 'Happy Cabbage Analytics publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Blockout Dates API, Daily Sales Metadata API, Identity API, and 11 more. Tagged areas include Cannabis, Retail, Inventory Management, Analytics, and Purchasing.


  Happy Cabbage Analytics'' developer surface includes documentation, API reference, engineering blog, support, signup flow, changelog, authentication, and 19 more developer resources.'
plans:
- name: Happy Cabbage Analytics Plans Pricing
  plan_count: 0
  slug: happy-cabbage-analytics-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Happy Cabbage Analytics Rate Limits
  slug: happy-cabbage-analytics-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 58.6
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 36.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/happy-cabbage-analytics/refs/heads/main/screenshots/happy-cabbage-analytics-2026-09-02T145659.png
security:
- kind: authentication
  name: Happy Cabbage Analytics Authentication
  slug: happy-cabbage-analytics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Happy Cabbage Analytics Domain Security
  slug: happy-cabbage-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: happy-cabbage-analytics
tags:
- Cannabis
- Retail
- Inventory Management
- Analytics
- Purchasing
- Point-of-Sale
- Wholesale
- Demand Forecasting
- Supply Chain
- agent-native
website: https://www.happycabbage.io/
---
