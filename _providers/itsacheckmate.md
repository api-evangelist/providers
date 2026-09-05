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
  band: agent-ready
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
  score: 29.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Itsacheckmate Agentic Access
  operation_count: 6
  slug: itsacheckmate-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- baseURL: https://sandbox-api.itsacheckmate.com
  baseurl_source: declared
  description: Location activation and location detail retrieval.
  name: ItsaCheckmate Locations API
  slug: itsacheckmate-locations-api
- baseURL: https://sandbox-api.itsacheckmate.com
  baseurl_source: declared
  description: Menu retrieval per ordering platform.
  name: ItsaCheckmate Menus API
  slug: itsacheckmate-menus-api
- baseURL: https://sandbox-api.itsacheckmate.com
  baseurl_source: declared
  description: Token issuance, refresh, and introspection.
  name: ItsaCheckmate OAuth API
  slug: itsacheckmate-oauth-api
- baseURL: https://sandbox-api.itsacheckmate.com
  baseurl_source: declared
  description: Standard and group order submission into the POS.
  name: ItsaCheckmate Orders API
  slug: itsacheckmate-orders-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ItsaCheckmate Marketplace for Developers Locations API
  slug: open-itsacheckmate-locations-api
- collection_type: open
  name: ItsaCheckmate Marketplace for Developers API
  slug: open-itsacheckmate-marketplace-api
- collection_type: open
  name: ItsaCheckmate Marketplace for Developers Locations Menus API
  slug: open-itsacheckmate-menus-api
- collection_type: open
  name: ItsaCheckmate Marketplace for Developers Locations OAuth API
  slug: open-itsacheckmate-oauth-api
- collection_type: open
  name: ItsaCheckmate Marketplace for Developers Locations Orders API
  slug: open-itsacheckmate-orders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/itsacheckmate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itsacheckmate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/itsacheckmate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.itsacheckmate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.itsacheckmate.com/solutions/marketplace-for-developers
- group: docs
  title: ''
  type: APIReference
  url: https://openapi-itsacheckmate.readme.io/reference/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://support.itsacheckmate.com/hc/en-us/articles/8105450179867-Checkmate-Pricing
- group: operate
  title: ''
  type: Support
  url: https://support.itsacheckmate.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.itsacheckmate.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/itsacheckmate
- group: agent
  title: ''
  type: LlmsText
  url: https://openapi-itsacheckmate.readme.io/llms.txt
- group: design
  title: ''
  type: Rules
  url: rules/itsacheckmate-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/itsacheckmate-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/itsacheckmate-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/itsacheckmate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/itsacheckmate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/itsacheckmate-finops.yml
created: '2026-06-02'
description: ItsaCheckmate (Checkmate) is restaurant middleware that connects point-of-sale systems to delivery marketplaces and ordering channels, providing two-way integration, menu management, and consolidated reporting across 50+ POS systems and 100+ ordering platforms for tens of thousands of restaurant locations. Through its Marketplace for Developers, Checkmate offers a self-service open REST API that lets technology partners build a single integration to read and write menus, orders, and locations across many POS systems. The API uses OAuth-style token authentication with short-lived, scoped access and refresh tokens, ready-to-use Postman collections, and an llms.txt index for AI agents.
examples:
- key_count: 3
  name: Marketplace Api Activation Result Example
  slug: marketplace-api-activation-result-example
- key_count: 5
  name: Marketplace Api Address Example
  slug: marketplace-api-address-example
- key_count: 2
  name: Marketplace Api Customer Example
  slug: marketplace-api-customer-example
- key_count: 6
  name: Marketplace Api Location Example
  slug: marketplace-api-location-example
- key_count: 3
  name: Marketplace Api Menu Category Example
  slug: marketplace-api-menu-category-example
- key_count: 3
  name: Marketplace Api Menu Example
  slug: marketplace-api-menu-example
- key_count: 5
  name: Marketplace Api Menu Item Example
  slug: marketplace-api-menu-item-example
- key_count: 4
  name: Marketplace Api Order Confirmation Example
  slug: marketplace-api-order-confirmation-example
- key_count: 7
  name: Marketplace Api Order Example
  slug: marketplace-api-order-example
- key_count: 4
  name: Marketplace Api Order Item Example
  slug: marketplace-api-order-item-example
- key_count: 3
  name: Marketplace Api Order Totals Example
  slug: marketplace-api-order-totals-example
- key_count: 4
  name: Marketplace Api Token Info Example
  slug: marketplace-api-token-info-example
- key_count: 6
  name: Marketplace Api Token Request Example
  slug: marketplace-api-token-request-example
- key_count: 5
  name: Marketplace Api Token Response Example
  slug: marketplace-api-token-response-example
finops:
- name: Itsacheckmate Finops
  service_category: Restaurant Technology + Order Integration
  slug: itsacheckmate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/itsacheckmate.png
json_schemas:
- name: ActivationResult
  property_count: 3
  slug: marketplace-api-activation-result
- name: Address
  property_count: 5
  slug: marketplace-api-address
- name: Customer
  property_count: 2
  slug: marketplace-api-customer
- name: Location
  property_count: 6
  slug: marketplace-api-location
- name: MenuCategory
  property_count: 3
  slug: marketplace-api-menu-category
- name: MenuItem
  property_count: 5
  slug: marketplace-api-menu-item
- name: Menu
  property_count: 3
  slug: marketplace-api-menu
- name: OrderConfirmation
  property_count: 4
  slug: marketplace-api-order-confirmation
- name: OrderItem
  property_count: 4
  slug: marketplace-api-order-item
- name: Order
  property_count: 7
  slug: marketplace-api-order
- name: OrderTotals
  property_count: 3
  slug: marketplace-api-order-totals
- name: TokenInfo
  property_count: 4
  slug: marketplace-api-token-info
- name: TokenRequest
  property_count: 6
  slug: marketplace-api-token-request
- name: TokenResponse
  property_count: 5
  slug: marketplace-api-token-response
json_structures:
- name: Marketplace Api Activation Result Structure
  property_count: 3
  slug: marketplace-api-activation-result-structure
- name: Marketplace Api Address Structure
  property_count: 5
  slug: marketplace-api-address-structure
- name: Marketplace Api Customer Structure
  property_count: 2
  slug: marketplace-api-customer-structure
- name: Marketplace Api Location Structure
  property_count: 6
  slug: marketplace-api-location-structure
- name: Marketplace Api Menu Category Structure
  property_count: 3
  slug: marketplace-api-menu-category-structure
- name: Marketplace Api Menu Item Structure
  property_count: 5
  slug: marketplace-api-menu-item-structure
- name: Marketplace Api Menu Structure
  property_count: 3
  slug: marketplace-api-menu-structure
- name: Marketplace Api Order Confirmation Structure
  property_count: 4
  slug: marketplace-api-order-confirmation-structure
- name: Marketplace Api Order Item Structure
  property_count: 4
  slug: marketplace-api-order-item-structure
- name: Marketplace Api Order Structure
  property_count: 7
  slug: marketplace-api-order-structure
- name: Marketplace Api Order Totals Structure
  property_count: 3
  slug: marketplace-api-order-totals-structure
- name: Marketplace Api Token Info Structure
  property_count: 4
  slug: marketplace-api-token-info-structure
- name: Marketplace Api Token Request Structure
  property_count: 6
  slug: marketplace-api-token-request-structure
- name: Marketplace Api Token Response Structure
  property_count: 5
  slug: marketplace-api-token-response-structure
jsonld:
- class_count: 25
  name: Itsacheckmate Context
  property_count: 35
  slug: itsacheckmate-context
layout: provider
modified: '2026-06-02'
name: ItsaCheckmate
nav: Providers
network: true
overview: 'ItsaCheckmate publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Locations API, Menus API, OAuth API, and 1 more. Tagged areas include Restaurant, Point-of-Sale, Online Ordering, Delivery, and Menus.


  The ItsaCheckmate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ItsaCheckmate''s developer surface includes authentication, documentation, API reference, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Itsacheckmate Plans Pricing
  plan_count: 3
  slug: itsacheckmate-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Itsacheckmate Rate Limits
  slug: itsacheckmate-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ItsaCheckmate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: itsacheckmate-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: ItsaCheckmate API Rules
  rule_count: 38
  severity_counts:
    error: 10
    hint: 0
    info: 10
    warn: 18
  slug: itsacheckmate-spectral-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 87.5
    catalog_earned_first_party: 0.0
    catalog_gap: 27.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.8
    contract_quality: 22.3
    developer_ergonomics: 40.5
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 35.5
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/itsacheckmate/refs/heads/main/screenshots/itsacheckmate-2026-06-20T183633.png
security:
- kind: authentication
  name: Itsacheckmate Authentication
  slug: itsacheckmate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Itsacheckmate Domain Security
  slug: itsacheckmate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: itsacheckmate
tags:
- Restaurant
- Point-of-Sale
- Online Ordering
- Delivery
- Menus
- Order
- Integration
website: https://www.itsacheckmate.com/
---
