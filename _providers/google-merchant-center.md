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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Merchant Center Agentic Access
  operation_count: 7
  slug: google-merchant-center-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 5
apis:
- description: The Accounts API from Google Merchant Center — 1 operation(s) for accounts.
  name: Google Merchant Center Accounts API
  slug: google-merchant-center-accounts-api
- description: The Inventories API from Google Merchant Center — 1 operation(s) for inventories.
  name: Google Merchant Center Inventories API
  slug: google-merchant-center-inventories-api
- description: The Products API from Google Merchant Center — 2 operation(s) for products.
  name: Google Merchant Center Products API
  slug: google-merchant-center-products-api
- description: The Promotions API from Google Merchant Center — 1 operation(s) for promotions.
  name: Google Merchant Center Promotions API
  slug: google-merchant-center-promotions-api
- description: The Reports API from Google Merchant Center — 1 operation(s) for reports.
  name: Google Merchant Center Reports API
  slug: google-merchant-center-reports-api
artifact_total: 16
collections:
- collection_type: open
  name: Google Merchant Center Google Merchant API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-merchant-center-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-merchant-center-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-merchant-center-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-merchant-center-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-merchant-center-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: start
  title: ''
  type: Portal
  url: https://www.google.com/retail/solutions/merchant-center/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/shopping-content/guides/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/merchant/api
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/merchant/api/guides/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://www.google.com/retail/solutions/merchant-center/
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
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google Merchant API enables programmatic management of Merchant Center accounts including product data, inventories, promotions, reports, conversions, and order tracking. It replaces the Content API for Shopping and provides access to manage product feeds, local and regional inventory, and shopping campaign data.
finops:
- name: Google Merchant Center Finops
  service_category: API
  slug: google-merchant-center-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-merchant-center.png
layout: provider
modified: '2026-05-19'
name: Google Merchant Center
nav: Providers
network: true
overview: 'Google Merchant Center publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Inventories API, Products API, and 2 more. Tagged areas include E-Commerce, Google Shopping, Inventory, Merchant Center, and Products.


  The Google Merchant Center catalog on APIs.io includes 2 Spectral governance rulesets.


  Google Merchant Center''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Google Merchant Center Plans Pricing
  plan_count: 3
  slug: google-merchant-center-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 5
  name: Google Merchant Center Rate Limits
  slug: google-merchant-center-rate-limits
rules:
- name: Google Merchant Center API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-merchant-center-jsonschema-spectral-rules
- name: Google Merchant Center API Rules
  rule_count: 18
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 5
  slug: google-merchant-center-spectral-rules
scopes:
- name: Google Merchant Center Scopes
  scope_count: 1
  slug: google-merchant-center-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 64.1
  delta: 4.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.9
    developer_ergonomics: 43.5
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 59.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-merchant-center/refs/heads/main/screenshots/google-merchant-center-2026-06-20T182216.png
security:
- kind: authentication
  name: Google Merchant Center Authentication
  slug: google-merchant-center-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Merchant Center Domain Security
  slug: google-merchant-center-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Merchant Center Vulnerability Disclosure
  slug: google-merchant-center-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-merchant-center
tags:
- E-Commerce
- Google Shopping
- Inventory
- Merchant Center
- Products
- Promotions
- Shopping
website: https://www.google.com/retail/solutions/merchant-center/
---
