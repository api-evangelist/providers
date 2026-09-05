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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Merchant Center Agentic Access
  operation_count: 7
  slug: google-merchant-center-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 1
apis:
- baseURL: https://merchantapi.googleapis.com
  baseurl_source: declared
  description: The Accounts API from Google Merchant Center — 1 operation(s) for accounts.
  name: Google Merchant Center Accounts API
  slug: google-merchant-center-accounts-api
- baseURL: https://merchantapi.googleapis.com
  baseurl_source: declared
  description: The Inventories API from Google Merchant Center — 1 operation(s) for inventories.
  name: Google Merchant Center Inventories API
  slug: google-merchant-center-inventories-api
- baseURL: https://merchantapi.googleapis.com
  baseurl_source: declared
  description: The Products API from Google Merchant Center — 2 operation(s) for products.
  name: Google Merchant Center Products API
  slug: google-merchant-center-products-api
- baseURL: https://merchantapi.googleapis.com
  baseurl_source: declared
  description: The Promotions API from Google Merchant Center — 1 operation(s) for promotions.
  name: Google Merchant Center Promotions API
  slug: google-merchant-center-promotions-api
- baseURL: https://merchantapi.googleapis.com
  baseurl_source: declared
  description: The Reports API from Google Merchant Center — 1 operation(s) for reports.
  name: Google Merchant Center Reports API
  slug: google-merchant-center-reports-api
artifact_total: 27
collections:
- collection_type: postman
  name: Google Merchant Center Google Merchant Accounts API
  slug: postman-google-merchant-center-accounts-api
- collection_type: postman
  name: Google Merchant Center Google Merchant Accounts Inventories API
  slug: postman-google-merchant-center-inventories-api
- collection_type: postman
  name: Google Merchant Center Google Merchant Accounts Products API
  slug: postman-google-merchant-center-products-api
- collection_type: postman
  name: Google Merchant Center Google Merchant Accounts Promotions API
  slug: postman-google-merchant-center-promotions-api
- collection_type: postman
  name: Google Merchant Center Google Merchant Accounts Reports API
  slug: postman-google-merchant-center-reports-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Merchant Center Google Merchant Accounts API
  slug: open-google-merchant-center-accounts-api
- collection_type: open
  name: Google Merchant Center Google Merchant Accounts Inventories API
  slug: open-google-merchant-center-inventories-api
- collection_type: open
  name: Google Merchant Center Google Merchant Accounts Products API
  slug: open-google-merchant-center-products-api
- collection_type: open
  name: Google Merchant Center Google Merchant Accounts Promotions API
  slug: open-google-merchant-center-promotions-api
- collection_type: open
  name: Google Merchant Center Google Merchant Accounts Reports API
  slug: open-google-merchant-center-reports-api
- collection_type: open
  name: Google Merchant Center Google Merchant API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-merchant-center/overview
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
overview: 'Google Merchant Center publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Inventories API, Products API, and 2 more. Tagged areas include E-Commerce, Google Shopping, Inventory, Merchant Center, and Product.


  The Google Merchant Center catalog on APIs.io includes 2 Spectral governance rulesets.


  Google Merchant Center''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Merchant Center Plans Pricing
  plan_count: 3
  slug: google-merchant-center-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Google Merchant Center Rate Limits
  slug: google-merchant-center-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Merchant Center API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-merchant-center-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Google Merchant Center API Rules
  rule_count: 17
  severity_counts:
    error: 10
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
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 56.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 58.5
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Product
- Promotions
- Shopping
website: https://www.google.com/retail/solutions/merchant-center/
---
