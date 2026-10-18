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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Byrd Agentic Access
  operation_count: 69
  slug: byrd-agentic-access
  summary_line: 69 operations · 30 acting
api_count: 2
apis:
- baseURL: https://api.getbyrd.com
  baseurl_source: declared
  description: The warehouses and B2B templates available to your account, and CSV exports of your shipments, returns and inventory.
  name: Byrd Account API
  slug: byrd-account-api
- baseURL: https://api.getbyrd.com
  baseurl_source: declared
  description: Log in with your API key to get an access token, refresh it, and read or update your account.
  name: Byrd Authentication API
  slug: byrd-authentication-api
- baseURL: https://api.getbyrd.com
  baseurl_source: declared
  description: Products and bundles, their lots, serial numbers and stock, and the dangerous goods limits that apply to them.
  name: Byrd Catalog API
  slug: byrd-catalog-api
- baseURL: https://api.getbyrd.com
  baseurl_source: declared
  description: 'Deliveries of your stock to a warehouse: announce them, follow them in, and manage their documents.'
  name: Byrd Inbound API
  slug: byrd-inbound-api
- baseURL: https://api.getbyrd.com
  baseurl_source: declared
  description: 'Orders shipped to your customers: create and release them, follow their units and picks, and handle their returns.'
  name: Byrd Shipments API
  slug: byrd-shipments-api
artifact_total: 19
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/agentic-access/byrd-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/byrd-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/rules/byrd-rules.yml
  title: ''
  type: Spectral
  url: rules/byrd-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/json-ld/byrd-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/byrd-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/vocabulary/byrd-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/byrd-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/data-model/byrd-data-model.yml
  title: ''
  type: DataModel
  url: data-model/byrd-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/security/byrd-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/byrd-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/errors/byrd-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/byrd-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/hosts/byrd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/byrd-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/vendors/byrd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/byrd-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.getbyrd.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.getbyrd.com/team
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/rate-limits/byrd-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/byrd-rate-limits.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.getbyrd.com/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/security/byrd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/byrd-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/security/byrd-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/byrd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getbyrd.com/en/vulnerability-disclosure-program
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getbyrd.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getbyrd.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getbyrd.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.getbyrd.com/docs/integration-overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/authentication/byrd-authentication.yml
  title: ''
  type: Authentication
  url: authentication/byrd-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.getbyrd.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.getbyrd.com/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://blog.getbyrd.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getbyrd.com/preise
- group: start
  title: ''
  type: SignUp
  url: https://www.getbyrd.com/kontakt
- group: start
  title: ''
  type: Login
  url: https://developers.getbyrd.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getbyrd.com/agbs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getbyrd.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.getbyrd.com/en/security-startpage
- group: company
  title: ''
  type: Website
  url: https://www.getbyrd.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/llms/byrd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/byrd-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: byrd is a European e-commerce fulfillment and third-party logistics (3PL) provider operating a network of 25+ fulfillment warehouses across Europe and the UK. It offers multichannel order fulfillment with integrations to the major shop and marketplace platforms (Shopify, Amazon, eBay, WooCommerce, Shopware, PlentyONE, Mirakl and more), inventory and warehouse management, carrier shipping, returns handling, and analytics. byrd exposes a developer REST API (developers.getbyrd.com) for programmatically managing products, deliveries, shipments, and returns, secured with JWT bearer authentication. byrd is a Speedinvest portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/byrd.png
json_schemas:
- name: Delivery create request
  property_count: 57
  slug: byrd-delivery-create-request
- name: Delivery create
  property_count: 57
  slug: byrd-delivery-create
- name: Delivery
  property_count: 56
  slug: byrd-delivery
- name: Delivery with metrics
  property_count: 63
  slug: byrd-delivery-with-metrics
- name: Product
  property_count: 55
  slug: byrd-product
- name: Shipment
  property_count: 35
  slug: byrd-shipment
jsonld:
- class_count: 120
  name: Byrd Context
  property_count: 450
  slug: byrd-context
layout: provider
modified: '2026-10-06'
name: Byrd
nav: Providers
network: true
overview: 'Byrd publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Catalog API, and 2 more. Tagged areas include Company, E-Commerce, Fulfillment, Logistics, and 3PL.


  The Byrd catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Byrd''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 26 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Byrd Rate Limits
  slug: byrd-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Byrd API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: byrd-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.6
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 67.2
    developer_ergonomics: 39.9
    discoverability: 76.8
    operational_transparency: 39.5
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/screenshots/byrd-2026-07-25T204138.png
security:
- kind: authentication
  name: Byrd Authentication
  slug: byrd-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Byrd Domain Security
  slug: byrd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Byrd Vulnerability Disclosure
  slug: byrd-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Byrd Trust Center
  slug: byrd-trust-center
  summary_line: trust center published
slug: byrd
tags:
- Company
- E-Commerce
- Fulfillment
- Logistics
- 3PL
- Shipping
- Warehousing
- Order Management
- Inventory
- Returns
- Supply Chain
website: https://www.getbyrd.com
---
