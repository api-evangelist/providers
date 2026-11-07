---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Breezecash Agentic Access
  operation_count: 58
  slug: breezecash-agentic-access
  summary_line: 58 operations · 28 acting
api_count: 1
apis:
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Customers API from Breeze.cash — 3 operation(s) for customers.
  name: Breeze.cash Customers API
  slug: breezecash-customers-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Direct Payment API from Breeze.cash — 5 operation(s) for direct payment.
  name: Breeze.cash Direct Payment API
  slug: breezecash-direct-payment-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Disputes API from Breeze.cash — 2 operation(s) for disputes.
  name: Breeze.cash Disputes API
  slug: breezecash-disputes-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Fraud Reports API from Breeze.cash — 2 operation(s) for fraud reports.
  name: Breeze.cash Fraud Reports API
  slug: breezecash-fraud-reports-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Headless KYC API from Breeze.cash — 6 operation(s) for headless kyc.
  name: Breeze.cash Headless KYC API
  slug: breezecash-headless-kyc-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Headless Payout API from Breeze.cash — 1 operation(s) for headless payout.
  name: Breeze.cash Headless Payout API
  slug: breezecash-headless-payout-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Invoices API from Breeze.cash — 1 operation(s) for invoices.
  name: Breeze.cash Invoices API
  slug: breezecash-invoices-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Liquidation Addresses API from Breeze.cash — 4 operation(s) for liquidation addresses.
  name: Breeze.cash Liquidation Addresses API
  slug: breezecash-liquidation-addresses-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Offramp API from Breeze.cash — 4 operation(s) for offramp.
  name: Breeze.cash Offramp API
  slug: breezecash-offramp-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Payment Pages API from Breeze.cash — 6 operation(s) for payment pages.
  name: Breeze.cash Payment Pages API
  slug: breezecash-payment-pages-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Payout Pages API from Breeze.cash — 5 operation(s) for payout pages.
  name: Breeze.cash Payout Pages API
  slug: breezecash-payout-pages-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Products API from Breeze.cash — 3 operation(s) for products.
  name: Breeze.cash Products API
  slug: breezecash-products-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Risk API from Breeze.cash — 1 operation(s) for risk.
  name: Breeze.cash Risk API
  slug: breezecash-risk-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Statements API from Breeze.cash — 2 operation(s) for statements.
  name: Breeze.cash Statements API
  slug: breezecash-statements-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Subscriptions API from Breeze.cash — 4 operation(s) for subscriptions.
  name: Breeze.cash Subscriptions API
  slug: breezecash-subscriptions-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: The Tax API from Breeze.cash — 1 operation(s) for tax.
  name: Breeze.cash Tax API
  slug: breezecash-tax-api
- baseURL: https://api.breeze.cash
  baseurl_source: declared
  description: Events Breeze sends to your configured webhook endpoint. Each delivery is an HTTP POST with a `{ type, data, signature }` body. Verify the signature before trusting the payload, and return a 2xx statu
  name: Breeze.cash Webhooks API
  slug: breezecash-webhooks-api
artifact_total: 30
asyncapis:
- description: ''
  name: Breezecash Webhooks
  slug: breezecash-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/breezecash/well-known/breezecash-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breezecash-well-known.yml
- group: other
  href: https://artifacts.apis.io/breezecash/vendors/breezecash-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breezecash-vendors.yml
- group: agent
  href: https://artifacts.apis.io/breezecash/agentic-access/breezecash-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/breezecash-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/breezecash/rules/breezecash-rules.yml
  title: ''
  type: Spectral
  url: rules/breezecash-rules.yml
- group: design
  href: https://artifacts.apis.io/breezecash/json-ld/breezecash-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/breezecash-context.jsonld
- group: design
  href: https://artifacts.apis.io/breezecash/vocabulary/breezecash-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/breezecash-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/breezecash/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/breezecash/asyncapi/breezecash-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/breezecash-webhooks.yml
- group: design
  href: https://artifacts.apis.io/breezecash/data-model/breezecash-data-model.yml
  title: ''
  type: DataModel
  url: data-model/breezecash-data-model.yml
- group: design
  href: https://artifacts.apis.io/breezecash/errors/breezecash-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/breezecash-problem-types.yml
- group: design
  href: https://artifacts.apis.io/breezecash/conformance/breezecash-conformance.yml
  title: ''
  type: Conformance
  url: conformance/breezecash-conformance.yml
- group: other
  href: https://artifacts.apis.io/breezecash/overlays/breezecash-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/breezecash-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/breezecash/llms/breezecash-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breezecash-llms.txt
- group: other
  href: https://artifacts.apis.io/breezecash/hosts/breezecash-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breezecash-hosts.yml
- group: build
  href: https://artifacts.apis.io/breezecash/packages/breezecash-packages.yml
  title: ''
  type: SDKs
  url: packages/breezecash-packages.yml
- group: build
  href: https://artifacts.apis.io/breezecash/packages/breezecash-packages.yml
  title: ''
  type: Packages
  url: packages/breezecash-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breeze.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.breeze.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breeze.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.breeze.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.breeze.com/docs/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.breeze.cash/
- group: company
  title: ''
  type: Website
  url: https://breeze.cash/
- group: auth
  href: https://artifacts.apis.io/breezecash/authentication/breezecash-authentication.yml
  title: ''
  type: Authentication
  url: authentication/breezecash-authentication.yml
- group: auth
  href: https://artifacts.apis.io/breezecash/security/breezecash-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breezecash-domain-security.yml
created: '2026-10-28'
description: 'Breeze.cash is a venture‑backed startup listed in the API Evangelist harvest backlog (source: vc‑portfolio; backed by Sequoia Capital). No public website, API documentation, or developer portal could be verified; attempts to resolve https://breeze.cash/ redirected to an unrelated payments platform. The company remains a stub pending further evidence.'
image: https://cdn.prod.website-files.com/69fd484633023d85dc4e556d/6a8f49079ad1fa61d283598e_OG%20Image.jpg
json_schemas:
- name: CreateGatewayPaymentRequest
  property_count: 11
  slug: breezecash-create-gateway-payment-request
- name: CreateGatewayPaymentResponse
  property_count: 17
  slug: breezecash-create-gateway-payment-response
- name: CreatePaymentPageResponse
  property_count: 25
  slug: breezecash-create-payment-page-response
- name: CreateSubscriptionRequest
  property_count: 12
  slug: breezecash-create-subscription-request
- name: ExpirePaymentPageResponse
  property_count: 25
  slug: breezecash-expire-payment-page-response
- name: GetAllPaymentAttemptsResponse
  property_count: 2
  slug: breezecash-get-all-payment-attempts-response
jsonld:
- class_count: 76
  name: Breezecash Context
  property_count: 191
  slug: breezecash-context
layout: provider
modified: '2026-10-28'
name: Breeze.cash
nav: Providers
network: true
overview: 'Breeze.cash publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customers API, Direct Payment API, Disputes API, and 14 more. Tagged areas include Company, Fintech, Payments, Cryptocurrency, and Startups.


  The Breeze.cash catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Breeze.cash''s developer surface includes support, getting-started guide, documentation, authentication, and 21 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Breeze.cash API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: breezecash-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 73.4
    developer_ergonomics: 43.3
    discoverability: 64.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 17
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/breezecash/breezecash-2026-11-03T122537.png
security:
- kind: authentication
  name: Breezecash Authentication
  slug: breezecash-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Breezecash Domain Security
  slug: breezecash-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: breezecash-create-customer
  slug: breezecash-create-customer
slug: breezecash
tags:
- Company
- Fintech
- Payments
- Cryptocurrency
- Startups
website: https://breeze.cash/
---
