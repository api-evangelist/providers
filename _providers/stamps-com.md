---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-11-06'
api_count: 7
apis:
- description: REST and SOAP APIs for USPS shipping services, including rates, label creation, tracking, and address verification.
  name: Stamps.com Shipping API
  slug: stamps-com-shipping-api
- baseURL: https://api.stampsendicia.com/sera
  baseurl_source: declared
  description: The Account API from Stamps.com — 2 operation(s) for account.
  name: Stamps.com Account API
  slug: stamps-com-account-api
- baseURL: https://api.stampsendicia.com/sera
  baseurl_source: declared
  description: The Addresses API from Stamps.com — 1 operation(s) for addresses.
  name: Stamps.com Addresses API
  slug: stamps-com-addresses-api
- baseURL: https://api.stampsendicia.com/sera
  baseurl_source: declared
  description: The Balance API from Stamps.com — 1 operation(s) for balance.
  name: Stamps.com Balance API
  slug: stamps-com-balance-api
- baseURL: https://api.stampsendicia.com/sera
  baseurl_source: declared
  description: The Labels API from Stamps.com — 1 operation(s) for labels.
  name: Stamps.com Labels API
  slug: stamps-com-labels-api
- baseURL: https://api.stampsendicia.com/sera
  baseurl_source: declared
  description: The Stamps.com API API from Stamps.com — 1 operation(s) for stamps.com api.
  name: Stamps.com Stamps.com API
  slug: stamps-com-stamps-com-api-api
- baseURL: https://api.stampsendicia.com/sera
  baseurl_source: declared
  description: The Tracking API from Stamps.com — 1 operation(s) for tracking.
  name: Stamps.com Tracking API
  slug: stamps-com-tracking-api
artifact_total: 16
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stamps.com/privacy-policy/
- group: design
  href: https://artifacts.apis.io/stamps-com/rules/stamps-com-rules.yml
  title: ''
  type: Spectral
  url: rules/stamps-com-rules.yml
- group: design
  href: https://artifacts.apis.io/stamps-com/json-ld/stamps-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stamps-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/stamps-com/vocabulary/stamps-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stamps-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stamps-com/data-model/stamps-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stamps-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/stamps-com/conformance/stamps-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stamps-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stamps-com/llms/stamps-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stamps-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/stamps-com/well-known/stamps-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stamps-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/stamps-com/well-known/stamps-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stamps-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/stamps-com/hosts/stamps-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stamps-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/stamps-com/vendors/stamps-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stamps-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stamps.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.stamps.com/media/
- group: auth
  href: https://artifacts.apis.io/stamps-com/security/stamps-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stamps-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stamps.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.stamps.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.stamps.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.stamps.com/rest-api/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.stamps.com/
- group: operate
  title: ''
  type: Support
  url: https://help.stamps.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: http://blog.stamps.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stamps.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.stamps.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stamps.com/terms/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.stamps.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Stamps.com provides online postage and shipping services, enabling businesses and individuals to print postage, compare rates, and manage shipments directly from their computers. The platform integrates with major e‑commerce solutions, offers API access for automating label creation, tracking, and address verification, and supports bulk mailing, international shipping, and customs documentation. As a leading provider in the mailing industry, Stamps.com continuously expands its features to simplify logistics and reduce shipping costs for its customers.
image: https://www.stamps.com/wp-content/uploads/2024/10/Stamps-Open-Graph-1200x1200-1.png
json_schemas:
- name: GetV1V1IdResponse
  property_count: 3
  slug: stamps-com-get-v1-v1-id-response
- name: PostAddressesAddresseidResponse
  property_count: 8
  slug: stamps-com-post-addresses-addresseid-response
- name: PostV1BalanceAddFundsResponse
  property_count: 3
  slug: stamps-com-post-v1-balance-add-funds-response
- name: PostV1V1IdRequest
  property_count: 7
  slug: stamps-com-post-v1-v1-id-request
- name: PostV1V1IdResponse
  property_count: 10
  slug: stamps-com-post-v1-v1-id-response
- name: PutV1AccountSecurityQuestionsRequest
  property_count: 4
  slug: stamps-com-put-v1-account-security-questions-request
jsonld:
- class_count: 11
  name: Stamps Com Context
  property_count: 35
  slug: stamps-com-context
layout: provider
modified: '2026-10-13'
name: Stamps.com
nav: Providers
network: true
overview: 'Stamps.com is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Addresses API, Balance API, and 4 more. Tagged areas include Company, Shipping, E-Commerce, and Logistics.


  The Stamps.com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stamps.com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Stamps.com API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 1
  slug: stamps-com-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 24.5
    developer_ergonomics: 22.6
    discoverability: 70.5
    operational_transparency: 18.4
  previous_composite: 37.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stamps-com/stamps-com-2026-11-03T143724.png
security:
- kind: domain-security
  name: Stamps Com Domain Security
  slug: stamps-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stamps-com
tags:
- Company
- Shipping
- E-Commerce
- Logistics
website: https://www.stamps.com
---
