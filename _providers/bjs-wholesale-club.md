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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bjs Wholesale Club Agentic Access
  operation_count: 7
  slug: bjs-wholesale-club-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- description: The Clubs API from BJ's Wholesale Club — 1 operation(s) for clubs.
  name: BJ's Wholesale Club Clubs API
  slug: bjs-wholesale-club-clubs-api
- description: The Inventory API from BJ's Wholesale Club — 1 operation(s) for inventory.
  name: BJ's Wholesale Club Inventory API
  slug: bjs-wholesale-club-inventory-api
- description: The Membership API from BJ's Wholesale Club — 1 operation(s) for membership.
  name: BJ's Wholesale Club Membership API
  slug: bjs-wholesale-club-membership-api
- description: The Orders API from BJ's Wholesale Club — 2 operation(s) for orders.
  name: BJ's Wholesale Club Orders API
  slug: bjs-wholesale-club-orders-api
- description: The Products API from BJ's Wholesale Club — 2 operation(s) for products.
  name: BJ's Wholesale Club Products API
  slug: bjs-wholesale-club-products-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BJ's Wholesale Club Partner Clubs API
  slug: open-bjs-wholesale-club-clubs-api
- collection_type: open
  name: BJ's Wholesale Club Partner Clubs Inventory API
  slug: open-bjs-wholesale-club-inventory-api
- collection_type: open
  name: BJ's Wholesale Club Partner Clubs Membership API
  slug: open-bjs-wholesale-club-membership-api
- collection_type: open
  name: BJ's Wholesale Club Partner Clubs Orders API
  slug: open-bjs-wholesale-club-orders-api
- collection_type: open
  name: BJ's Wholesale Club Partner Clubs Products API
  slug: open-bjs-wholesale-club-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bjs-wholesale-club-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bjs-wholesale-club-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bjs-wholesale-club-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bjs-wholesale-club-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bjs.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bjs.com/content/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bjs.com/content/terms-and-conditions
- group: start
  title: ''
  type: Signup
  url: https://www.bjs.com/content/membership
- group: operate
  title: ''
  type: Support
  url: https://www.bjs.com/content/help-center
- group: design
  title: ''
  type: SpectralRules
  url: rules/bjs-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bjs-vocabulary.yaml
created: '2026-03-21'
description: BJ's Wholesale Club is a leading operator of membership warehouse clubs concentrated primarily on the eastern half of the United States. BJ's offers its members significant savings on a wide assortment of merchandise, including fresh foods, groceries, household essentials, and general merchandise. The company operates over 230 clubs and is focused on digital transformation, offering APIs to partners for product data, inventory, pricing, and order management integrations.
examples:
- key_count: 5
  name: Bjs Membership Example
  slug: bjs-membership-example
- key_count: 9
  name: Bjs Order Example
  slug: bjs-order-example
- key_count: 12
  name: Bjs Product Example
  slug: bjs-product-example
features:
- description: Supports membership-based access model for in-club and online purchasing, including membership verification and renewal.
  name: Membership Management
- description: Broad product assortment including fresh foods, groceries, household essentials, electronics, and general merchandise available via digital commerce integrations.
  name: Product Catalog
- description: Online ordering and delivery capabilities integrating with BJ's digital platform for partner fulfillment and affiliate programs.
  name: Digital Commerce
- description: Buy Online, Pick Up In Club capabilities available through BJ's digital platform for member convenience.
  name: Curbside Pickup
- description: Real-time inventory status across BJ's club locations, supporting in-club and curbside pickup fulfillment routing.
  name: Inventory Availability
- description: Find BJ's club locations by ZIP code with hours, services, and amenities including gas stations, optical, and tire centers.
  name: Club Locator
finops:
- name: Bjs Wholesale Club Finops
  service_category: API
  slug: bjs-wholesale-club-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bjs-wholesale-club.png
integrations:
- description: BJ's affiliate program is managed through CJ Affiliate (Commission Junction) for tracking and payments.
  name: Commission Junction
- description: Product feeds integrated with Google Shopping for product discovery and advertising.
  name: Google Shopping
- description: BJ's grocery delivery is available through the Instacart platform for same-day delivery to members.
  name: Instacart
json_schemas:
- name: BJS Membership
  property_count: 5
  slug: bjs-membership
- name: BJS Order
  property_count: 9
  slug: bjs-order
- name: BJS Product
  property_count: 12
  slug: bjs-product
json_structures:
- name: Bjs Membership Structure
  property_count: 0
  slug: bjs-membership-structure
- name: Bjs Order Structure
  property_count: 0
  slug: bjs-order-structure
- name: Bjs Product Structure
  property_count: 0
  slug: bjs-product-structure
jsonld:
- class_count: 5
  name: Bjs Context
  property_count: 0
  slug: bjs-context
layout: provider
modified: '2026-05-19'
name: BJ's Wholesale Club
nav: Providers
network: true
overview: 'BJ''s Wholesale Club publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Clubs API, Inventory API, Membership API, and 2 more. Tagged areas include E-Commerce, Membership, Retail, and Wholesale.


  The BJ''s Wholesale Club catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  BJ''s Wholesale Club''s developer surface includes authentication, signup flow, support, and 8 more developer resources.'
plans:
- name: Bjs Wholesale Club Plans Pricing
  plan_count: 3
  slug: bjs-wholesale-club-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Bjs Wholesale Club Rate Limits
  slug: bjs-wholesale-club-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BJ's Wholesale Club API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: bjs-spectral-rules
- effective_rule_count: 5
  extends: []
  name: BJ's Wholesale Club API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bjs-wholesale-club-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: BJ's Wholesale Club API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: bjs-wholesale-club-spectral-rules
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 38.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 69.7
    contract_quality: 70.3
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 69.7
    operational_transparency: 7.9
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Bjs Wholesale Club Authentication
  slug: bjs-wholesale-club-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bjs Wholesale Club Domain Security
  slug: bjs-wholesale-club-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bjs-wholesale-club
tags:
- E-Commerce
- Membership
- Retail
- Wholesale
use_cases:
- description: Partner programs enabling affiliate marketers to promote BJ's membership and products with commission-based compensation.
  name: Affiliate Marketing
- description: Access product catalog and pricing data to enable comparison shopping and product listing integrations.
  name: Product Data Integration
- description: Verify BJ's membership status for partner benefits and co-branded programs.
  name: Membership Verification
- description: Manage orders through BJ's digital commerce platform for dropship and fulfillment partnerships.
  name: Order Management
- description: Route orders to the nearest club with available inventory for curbside pickup or local delivery fulfillment.
  name: Inventory Routing
website: https://www.bjs.com
---
