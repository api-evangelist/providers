---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Bol Com Agentic Access
  operation_count: 69
  slug: bol-com-agentic-access
  summary_line: 69 operations · 23 acting
api_count: 1
apis:
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Commissions resource
  name: Bol Commissions API
  slug: bol-com-commissions-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Insights resource
  name: Bol Insights API
  slug: bol-com-insights-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Inventory resource
  name: Bol Inventory API
  slug: bol-com-inventory-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Invoice resource
  name: Bol Invoices API
  slug: bol-com-invoices-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Offer resource
  name: Bol Offers API
  slug: bol-com-offers-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Order resource
  name: Bol Orders API
  slug: bol-com-orders-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Products resource
  name: Bol Products API
  slug: bol-com-products-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Promotions resource
  name: Bol Promotions API
  slug: bol-com-promotions-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Replenishments resource
  name: Bol Replenishments API
  slug: bol-com-replenishments-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Retailers resource
  name: Bol Retailers API
  slug: bol-com-retailers-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Return resource
  name: Bol Returns API
  slug: bol-com-returns-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Shipment resource
  name: Bol Shipments API
  slug: bol-com-shipments-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Shipping labels resource
  name: Bol Shipping Labels API
  slug: bol-com-shipping-labels-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Push notification subscriptions resource
  name: Bol Subscriptions API
  slug: bol-com-subscriptions-api
- baseURL: https://api.bol.com/retailer/public/
  baseurl_source: declared
  description: Transport resource
  name: Bol Transports API
  slug: bol-com-transports-api
artifact_total: 32
common:
- group: other
  href: https://artifacts.apis.io/bol-com/capabilities/bol-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bol-com-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/bol-com/well-known/bol-com-bol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bol-com-bol-security.txt
- group: agent
  href: https://artifacts.apis.io/bol-com/agentic-access/bol-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bol-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bol-com/rules/bol-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bol-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bol-com/json-ld/bol-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bol-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bol-com/vocabulary/bol-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bol-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bol-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bol-com/data-model/bol-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bol-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bol.com/nl/nl/klantenservice/a/5715110588841984/bedrijfsgegevens
- group: design
  href: https://artifacts.apis.io/bol-com/errors/bol-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bol-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bol-com/conformance/bol-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bol-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/bol-com/well-known/bol-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bol-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bol-com/well-known/bol-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bol-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bol-com/hosts/bol-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bol-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bol-com/security/bol-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bol-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bol-com/security/bol-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bol-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bol.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bol.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bol.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.bol.com/retailer/public/Retailer-API/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://api.bol.com/retailer/public/Retailer-API/retailer-getting-started.html
- group: operate
  title: ''
  type: Support
  url: https://developers.bol.com/en/contact/
- group: company
  title: ''
  type: News
  url: https://developers.bol.com/en/news/
created: '2026-10-28'
description: Bol is a leading Dutch e‑commerce platform that connects millions of consumers with a vast marketplace of products. Through its public developer portal, Bol offers Retailer and Advertising APIs that enable partners to automate product listings, order processing, inventory management, pricing, and advertising campaigns. The APIs provide comprehensive documentation, authentication mechanisms, rate‑limit details, and support resources, allowing seamless integration for retailers and advertisers looking to sell on Bol’s marketplace.
image: https://www.bol.com/favicon.ico
json_schemas:
- name: CreateOfferRequest
  property_count: 9
  slug: bol-com-create-offer-request
- name: ReplenishmentResponse
  property_count: 12
  slug: bol-com-replenishment-response
- name: RetailerOffer
  property_count: 12
  slug: bol-com-retailer-offer
- name: SubscriptionRequest
  property_count: 5
  slug: bol-com-subscription-request
- name: SubscriptionResponse
  property_count: 6
  slug: bol-com-subscription-response
- name: UpdateOfferRequest
  property_count: 5
  slug: bol-com-update-offer-request
jsonld:
- class_count: 120
  name: Bol Com Context
  property_count: 223
  slug: bol-com-context
layout: provider
modified: '2026-10-28'
name: Bol
nav: Providers
network: true
overview: 'Bol publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Commissions API, Insights API, Inventory API, and 12 more. Tagged areas include E-Commerce, Retail, Marketplace, and Netherlands.


  The Bol catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bol''s developer surface includes documentation, API reference, getting-started guide, support, product news, and 18 more developer resources.'
plans:
- name: Bol Com Plans Pricing
  plan_count: 0
  slug: bol-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Bol Com Rate Limits
  slug: bol-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Bol API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: bol-com-rules
scopes:
- name: Bol Com Scopes
  scope_count: 0
  slug: bol-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 62.9
    developer_ergonomics: 27.9
    discoverability: 58.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bol Com Authentication
  slug: bol-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bol Com Domain Security
  slug: bol-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bol Com Vulnerability Disclosure
  slug: bol-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: get-commissions
  slug: bol-com-get-commissions
- name: get-offer-insights
  slug: bol-com-get-offer-insights
slug: bol-com
tags:
- E-Commerce
- Retail
- Marketplace
- Netherlands
website: https://bol.com/
---
