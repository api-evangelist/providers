---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Shopping Agentic Access
  operation_count: 7
  slug: google-shopping-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://shoppingcontent.googleapis.com/content/v2.1
  baseurl_source: declared
  description: Manage merchant accounts
  name: Google Content API for Shopping Accounts API
  slug: google-shopping-accounts-api
- baseURL: https://shoppingcontent.googleapis.com/content/v2.1
  baseurl_source: declared
  description: Manage data feeds
  name: Google Content API for Shopping Datafeeds API
  slug: google-shopping-datafeeds-api
- baseURL: https://shoppingcontent.googleapis.com/content/v2.1
  baseurl_source: declared
  description: Manage orders
  name: Google Content API for Shopping Orders API
  slug: google-shopping-orders-api
- baseURL: https://shoppingcontent.googleapis.com/content/v2.1
  baseurl_source: declared
  description: Manage product listings
  name: Google Content API for Shopping Products API
  slug: google-shopping-products-api
artifact_total: 23
collections:
- collection_type: postman
  name: Google Content API for Shopping Accounts API
  slug: postman-google-shopping-accounts-api
- collection_type: postman
  name: Google Content API for Shopping Accounts Datafeeds API
  slug: postman-google-shopping-datafeeds-api
- collection_type: postman
  name: Google Content API for Shopping Accounts Orders API
  slug: postman-google-shopping-orders-api
- collection_type: postman
  name: Google Content API for Shopping Accounts Products API
  slug: postman-google-shopping-products-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Content API for Shopping Accounts API
  slug: open-google-shopping-accounts-api
- collection_type: open
  name: Google Content API for Shopping Accounts Datafeeds API
  slug: open-google-shopping-datafeeds-api
- collection_type: open
  name: Google Content API for Shopping Accounts Orders API
  slug: open-google-shopping-orders-api
- collection_type: open
  name: Google Content API for Shopping Accounts Products API
  slug: open-google-shopping-products-api
- collection_type: open
  name: Google Content API for Shopping
  slug: open-openapi
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/google-shopping-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-content-api-for-shopping/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-shopping-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-shopping-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-shopping-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-shopping
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/shopping-content
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/shopping-content/guides/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/shopping-content
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/shopping-content/guides/how-tos/authorizing
- group: commercial
  title: ''
  type: Pricing
  url: https://support.google.com/merchants/answer/188493
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/shopping-content/guides/support
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-shopping/refs/heads/main/json-ld/google-shopping.jsonld
created: '2026-03-13'
description: The Content API for Shopping allows apps to interact directly with the Google Merchant Center platform, enabling management of product listings, account information, data feeds, inventory, orders, and promotions. It provides programmatic access to create, update, and delete products, manage shipping and tax settings, handle order workflows, and access reporting data for Google Shopping.
finops:
- name: Google Shopping Finops
  service_category: API
  slug: google-shopping-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-shopping.png
json_schemas:
- name: Google Content API for Shopping Schema
  property_count: 0
  slug: google-shopping
jsonld:
- class_count: 0
  name: Google Shopping Context
  property_count: 11
  slug: google-shopping
layout: provider
modified: '2026-05-19'
name: Google Content API for Shopping
nav: Providers
network: true
overview: 'Google Content API for Shopping publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Datafeeds API, Orders API, and 1 more. Tagged areas include E-Commerce, Google Shopping, Merchant Center, Product Listings, and Retail.


  The Google Content API for Shopping catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Content API for Shopping''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, and 10 more developer resources.'
plans:
- name: Google Shopping Plans Pricing
  plan_count: 3
  slug: google-shopping-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Google Shopping Rate Limits
  slug: google-shopping-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Content API for Shopping API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-shopping-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-shopping/refs/heads/main/screenshots/google-shopping-2026-06-20T182233.png
security:
- kind: domain-security
  name: Google Shopping Domain Security
  slug: google-shopping-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Shopping Vulnerability Disclosure
  slug: google-shopping-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-shopping
tags:
- E-Commerce
- Google Shopping
- Merchant Center
- Product Listings
- Retail
- Shopping
website: https://developers.google.com/shopping-content
---
