---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: Keep a retailer's Weedmaps menu in sync with their point-of-sale. Retrieve menus and menu items, and create, retrieve, update, delete, and upsert-by-external-ID menu items to publish real-time product
  name: Weedmaps Menu API
  slug: weedmaps-menu-api
- description: Sync or map the Weedmaps catalog of Brands and Brand Products to an internal catalog to improve menu-item search relevance and discoverability. Retrieve all brands, a single brand, the brand product c
  name: Weedmaps Brand Catalog API
  slug: weedmaps-brand-catalog-api
- description: Read-only reference taxonomy used to enrich menu items - retrieve cannabinoids, categories (flat and tree), strains, terpenes, and discovery tags. Linking menu items to these taxonomy entries increase
  name: Weedmaps Taxonomy API
  slug: weedmaps-taxonomy-api
- description: Receive and manage online Weedmaps orders directly in a partner POS. Update order status, retrieve applicable discounts, retrieve order schedule time windows, and retrieve document URLs (e.g. complian
  name: Weedmaps Orders API
  slug: weedmaps-orders-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weedmaps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weedmaps.com
- group: other
  title: ''
  type: Business
  url: https://weedmaps.com/business
- group: docs
  title: ''
  type: Documentation
  url: https://developer.weedmaps.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developer.weedmaps.com/docs/oauth
- group: start
  title: ''
  type: Onboarding
  url: https://developer.weedmaps.com/docs/onboarding-process
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weedmaps
- group: commercial
  title: ''
  type: Plans
  url: plans/weedmaps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weedmaps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weedmaps-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://news.weedmaps.com/feed/
created: '2026-07-03'
description: Weedmaps is a cannabis discovery and ordering marketplace connecting consumers with dispensaries, delivery services, and brands. For its business customers it publishes a partner integration API suite - a Menu API for keeping a retailer's product menu, pricing, and availability in sync with their point-of-sale, a Brand Catalog API for mapping and enriching menu items against the Weedmaps brand and product taxonomy, a Taxonomy API for categories, cannabinoids, strains, terpenes, and discovery tags, and an Orders API for receiving and updating online orders in a partner POS. The developer documentation is public, but production access is partner-gated - integrators apply by email, receive OAuth2 client-credentials credentials and a test listing, and a Listing Owner must grant access. New integrations are noted as not currently being onboarded, so the endpoints below are documented but modeled from the public reference rather than exercised against a live account.
finops:
- name: Weedmaps Finops
  service_category: Marketplace and Listings
  slug: weedmaps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weedmaps.png
layout: provider
modified: '2026-07-03'
name: Weedmaps
nav: Providers
network: true
overview: 'Weedmaps publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cannabis, Dispensary, Marketplace, Menu Sync, and Point-of-Sale.


  Weedmaps'' developer surface includes documentation, authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Weedmaps Plans Pricing
  plan_count: 4
  slug: weedmaps-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Weedmaps Rate Limits
  slug: weedmaps-rate-limits
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Weedmaps Domain Security
  slug: weedmaps-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: weedmaps
tags:
- Cannabis
- Dispensary
- Marketplace
- Menu Sync
- Point-of-Sale
- Order
- Brands
- Partner API
website: https://weedmaps.com
---
