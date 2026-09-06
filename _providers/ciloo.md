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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-05'
api_count: 4
apis:
- baseURL: https://{store_domain}/wp-json/ciloo/v1
  baseurl_source: declared
  description: OAuth 1.0a (HMAC-SHA1) REST API on the ciloo/v1 namespace of a Ciloo brand store. Read, add, update and remove cart items; mint per-customer OAuth credentials from admin credentials; and issue one-hou
  name: Ciloo Cart API
  slug: ciloo-cart-api
- description: Bidirectional order integration between Ciloo and its production partners. Ciloo POSTs a print order — items, print components with artwork paths and substrate attributes, and shipments with carrier a
  name: Ciloo Printer API Integration
  slug: ciloo-printer-api
- baseURL: https://{store_domain}/wp-json/ciloo/v1
  baseurl_source: declared
  description: OAuth key provisioning and auto-login token issuance.
  name: Ciloo Authentication API
  slug: ciloo-authentication-api
- baseURL: https://{store_domain}/wp-json/ciloo/v1
  baseurl_source: declared
  description: Customer lifecycle via the WooCommerce REST API v3 namespace, as documented by Ciloo.
  name: Ciloo Customers API
  slug: ciloo-customers-api
artifact_total: 10
asyncapis:
- description: ''
  name: Ciloo Printer Webhooks
  slug: ciloo-printer-webhooks
collections:
- collection_type: open
  name: Ciloo Cart API
  slug: open-ciloo-cart-api
common:
- group: company
  title: ''
  type: Website
  url: https://ciloo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cilooprint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.cilooprint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.cilooprint.com/ciloo-cart-api-documentation/#api-endpoints-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.cilooprint.com/ciloo-cart-api-documentation/#authentication-setup
- group: operate
  title: ''
  type: Support
  url: https://support.ciloo.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://ciloo.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://ciloo.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ciloo.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ciloo.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://ciloo.com/contact/
- group: other
  title: ''
  type: CaseStudies
  url: https://ciloo.com/case-studies/
- group: build
  title: ''
  type: Postman
  url: collections/ciloo-cart-api.postman_collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/ciloo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ciloo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ciloo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ciloo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ciloo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ciloo-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ciloo-printer-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ciloo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ciloo-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ciloo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ciloo-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ciloo-domain-security.yml
created: '2026-08-12'
description: 'Ciloo is a Rotterdam-headquartered global platform for branded products and promotional merchandise. Enterprises run a branded Ciloo store — business cards, apparel, stationery, signage, corporate gifts and sales collateral — and every order placed in it is produced on demand by a vetted production partner near the recipient, which Ciloo positions as cutting cost, waste and shipping distance while keeping brand control central. The platform is used by manufacturing, medical-device, professional- services and franchise organisations, and integrates with digital asset management (Frontify, Bynder, Canto, Aprimo, Papirfly, Brandfolder, Marvia), procurement and ERP (SAP Ariba, S/4HANA, Proactis, Proqura, Exact), SSO, and WooCommerce. Ciloo documents two APIs on its own knowledge centre at api.cilooprint.com: a per-brand-store Cart API secured with OAuth 1.0a, and a bidirectional Printer API integration that pushes orders to production partners and receives production and shipping
  status callbacks in return.'
image: https://ciloo.com/wp-content/uploads/2022/01/Ciloo-Logo-2021.png
layout: provider
modified: '2026-08-12'
name: Ciloo
nav: Providers
network: true
overview: 'Ciloo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cart API, Authentication API, and Customers API. Tagged areas include Company, Printing, Branded Merchandise, Promotional Products, and Print on Demand.


  The Ciloo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ciloo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 20 more developer resources.'
plans:
- name: Ciloo Plans Pricing
  plan_count: 0
  slug: ciloo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Ciloo Rate Limits
  slug: ciloo-rate-limits
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 21.8
    developer_ergonomics: 55.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 29.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ciloo/refs/heads/main/screenshots/ciloo-2026-08-17T080820.png
security:
- kind: authentication
  name: Ciloo Authentication
  slug: ciloo-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ciloo Domain Security
  slug: ciloo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ciloo
tags:
- Company
- Printing
- Branded Merchandise
- Promotional Products
- Print on Demand
- E-Commerce
- Digital Asset Management
- Procurement
- Fulfillment
- Marketing
website: https://ciloo.com/
---
