---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Commerce Coinbase Agentic Access
  operation_count: 12
  slug: commerce-coinbase-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.commerce.coinbase.com
  baseurl_source: declared
  description: Create and retrieve crypto payment charges
  name: Coinbase Commerce Charges API
  slug: commerce-coinbase-charges-api
- baseURL: https://api.commerce.coinbase.com
  baseurl_source: declared
  description: Create and manage single-use hosted payment checkouts
  name: Coinbase Commerce Checkouts API
  slug: commerce-coinbase-checkouts-api
- baseURL: https://api.commerce.coinbase.com
  baseurl_source: declared
  description: Retrieve charge-related webhook events
  name: Coinbase Commerce Events API
  slug: commerce-coinbase-events-api
- baseURL: https://api.commerce.coinbase.com
  baseurl_source: declared
  description: Checkout lifecycle event notifications
  name: Coinbase Commerce Webhooks API
  slug: commerce-coinbase-webhooks-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coinbase Commerce Charges API
  slug: open-commerce-coinbase-charges-api
- collection_type: open
  name: Coinbase Commerce Charges Checkouts API
  slug: open-commerce-coinbase-checkouts-api
- collection_type: open
  name: Coinbase Commerce Charges Events API
  slug: open-commerce-coinbase-events-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/commerce-coinbase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/commerce-coinbase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commerce-coinbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/commerce-coinbase-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://commerce.coinbase.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cdp.coinbase.com/coinbase-business/checkout-apis/overview
- group: docs
  title: ''
  type: Documentation
  url: https://commerce.coinbase.com/docs/api
- group: company
  title: ''
  type: Blog
  url: https://www.coinbase.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://help.coinbase.com/en/commerce/getting-started/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commerce.coinbase.com/legal/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinbase.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinbase.com
- group: operate
  title: ''
  type: Support
  url: https://help.coinbase.com/en/commerce
- group: docs
  title: ''
  type: MigrationGuide
  url: https://docs.cdp.coinbase.com/coinbase-business/checkout-apis/migrate-from-commerce/api-schema-mapping
- group: docs
  title: ''
  type: WebhooksDocumentation
  url: https://docs.cdp.coinbase.com/commerce/docs/using-webhooks
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/commerce-coinbase/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/commerce-coinbase/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/commerce-coinbase/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Coinbase Commerce is a merchant crypto payment solution enabling businesses to accept cryptocurrency payments natively. The platform provides a REST API for creating payment charges, managing hosted checkouts, accessing payment metadata, configuring webhooks, and tracking crypto payment status across charge lifecycle events. Supports Bitcoin, Ethereum, USDC, and other major cryptocurrencies with 1% per-transaction fees and no monthly or setup costs.
examples:
- key_count: 1
  name: Charge Response
  slug: charge-response
- key_count: 14
  name: Checkout Response
  slug: checkout-response
- key_count: 7
  name: Create Charge Request
  slug: create-charge-request
- key_count: 7
  name: Create Checkout Request
  slug: create-checkout-request
- key_count: 15
  name: Webhook Checkout Payment Success
  slug: webhook-checkout-payment-success
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commerce-coinbase.png
json_schemas:
- name: Charge
  property_count: 18
  slug: charge
- name: Checkout
  property_count: 21
  slug: checkout
jsonld:
- class_count: 11
  name: context Context
  property_count: 38
  slug: context
layout: provider
modified: '2026-06-13'
name: Coinbase Commerce
nav: Providers
network: true
overview: 'Coinbase Commerce publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Charges API, Checkouts API, Events API, and 1 more. Tagged areas include Crypto Payments, Cryptocurrency, Payment Gateway, Commerce, and Bitcoin.


  The Coinbase Commerce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coinbase Commerce''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 2
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Coinbase Commerce API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: commerce-coinbase-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.0
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 15.8
  previous_composite: 44.0
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
    score: 42.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commerce-coinbase/refs/heads/main/screenshots/commerce-coinbase-2026-06-20T174814.png
security:
- kind: authentication
  name: Commerce Coinbase Authentication
  slug: commerce-coinbase-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Commerce Coinbase Domain Security
  slug: commerce-coinbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Commerce Coinbase Vulnerability Disclosure
  slug: commerce-coinbase-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: commerce-coinbase
tags:
- Crypto Payments
- Cryptocurrency
- Payment Gateway
- Commerce
- Bitcoin
- Ethereum
- USDC
- Webhook
- Charges
- Checkouts
website: https://commerce.coinbase.com
---
