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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Printful Agentic Access
  operation_count: 31
  slug: printful-agentic-access
  summary_line: 31 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Browse the Printful product catalog, variants, prices, sizes, images, and availability.
  name: Printful Catalog API
  slug: printful-catalog-api
- description: Upload and retrieve print files in the file library.
  name: Printful Files API
  slug: printful-files-api
- description: Generate product mockup images via asynchronous tasks.
  name: Printful Mockup Generator API
  slug: printful-mockup-generator-api
- description: Create, confirm, and manage on-demand fulfillment orders and order items.
  name: Printful Orders API
  slug: printful-orders-api
- description: Calculate shipping rates for a set of items and destination.
  name: Printful Shipping Rates API
  slug: printful-shipping-rates-api
- description: Manage products synced into a connected store.
  name: Printful Store Products API
  slug: printful-store-products-api
- description: List and retrieve merchant-owned warehouse products.
  name: Printful Warehouse API
  slug: printful-warehouse-api
- description: Configure webhook endpoints and per-event subscriptions.
  name: Printful Webhooks API
  slug: printful-webhooks-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Printful Catalog API
  slug: open-printful-catalog-api
- collection_type: open
  name: Printful Catalog Files API
  slug: open-printful-files-api
- collection_type: open
  name: Printful Catalog Mockup Generator API
  slug: open-printful-mockup-generator-api
- collection_type: open
  name: Printful Catalog Orders API
  slug: open-printful-orders-api
- collection_type: open
  name: Printful Catalog Shipping Rates API
  slug: open-printful-shipping-rates-api
- collection_type: open
  name: Printful Catalog Store Products API
  slug: open-printful-store-products-api
- collection_type: open
  name: Printful Catalog Warehouse API
  slug: open-printful-warehouse-api
- collection_type: open
  name: Printful Catalog Webhooks API
  slug: open-printful-webhooks-api
- collection_type: open
  name: Printful API
  slug: open-printful
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/printful-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/printful-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/printful-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/printful-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/printful-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.printful.com/blog/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/printful
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/printful
- group: company
  title: ''
  type: Website
  url: https://www.printful.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.printful.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/printful-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/printful-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/printful-finops.yml
created: '2026-06-25'
description: Printful is a print-on-demand and order-fulfillment platform that lets merchants design custom products and have them produced and shipped on demand. The Printful API (v2 and v1) exposes the product catalog, store products, order management, file library, mockup generator, shipping rates, warehouse products, and webhooks over a REST interface authenticated with OAuth 2.0 / Bearer tokens.
finops:
- name: Printful Finops
  service_category: Commerce and Fulfillment
  slug: printful-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/printful.png
layout: provider
modified: '2026-06-25'
name: Printful
nav: Providers
network: true
overview: 'Printful publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Files API, Mockup Generator API, and 5 more. Tagged areas include Print on Demand, Fulfillment, E-Commerce, Dropshipping, and Merchandise.


  Printful''s developer surface includes authentication, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Printful Plans Pricing
  plan_count: 2
  slug: printful-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Printful Rate Limits
  slug: printful-rate-limits
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Printful Authentication
  slug: printful-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Printful Domain Security
  slug: printful-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Printful Vulnerability Disclosure
  slug: printful-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: printful
tags:
- Print on Demand
- Fulfillment
- E-Commerce
- Dropshipping
- Merchandise
website: https://www.printful.com
---
