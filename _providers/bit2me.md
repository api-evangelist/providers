---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Bit2Me Agentic Access
  operation_count: 114
  slug: bit2me-agentic-access
  summary_line: 114 operations · 48 acting
api_count: 2
apis:
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Account API from Bit2Me — 8 operation(s) for account.
  name: Bit2Me Account API
  slug: bit2me-account-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Account Deprecated Methods API from Bit2Me — 5 operation(s) for account deprecated methods.
  name: Bit2Me Account Deprecated Methods API
  slug: bit2me-account-deprecated-methods-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Auth API from Bit2Me — 5 operation(s) for auth.
  name: Bit2Me Auth API
  slug: bit2me-auth-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Blockchain Manager API from Bit2Me — 7 operation(s) for blockchain manager.
  name: Bit2Me Blockchain Manager API
  slug: bit2me-blockchain-manager-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Brokerage API from Bit2Me — 4 operation(s) for brokerage.
  name: Bit2Me Brokerage API
  slug: bit2me-brokerage-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Compliance API from Bit2Me — 3 operation(s) for compliance.
  name: Bit2Me Compliance API
  slug: bit2me-compliance-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Currency API from Bit2Me — 9 operation(s) for currency.
  name: Bit2Me Currency API
  slug: bit2me-currency-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Earn API from Bit2Me — 11 operation(s) for earn.
  name: Bit2Me Earn API
  slug: bit2me-earn-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Loan API from Bit2Me — 8 operation(s) for loan.
  name: Bit2Me Loan API
  slug: bit2me-loan-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Misc API from Bit2Me — 1 operation(s) for misc.
  name: Bit2Me Misc API
  slug: bit2me-misc-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Pay API from Bit2Me — 5 operation(s) for pay.
  name: Bit2Me Pay API
  slug: bit2me-pay-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Teller API from Bit2Me — 6 operation(s) for teller.
  name: Bit2Me Teller API
  slug: bit2me-teller-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Trading API from Bit2Me — 15 operation(s) for trading.
  name: Bit2Me Trading API
  slug: bit2me-trading-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Verifier API from Bit2Me — 2 operation(s) for verifier.
  name: Bit2Me Verifier API
  slug: bit2me-verifier-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Verifier Deprecated Methods API from Bit2Me — 2 operation(s) for verifier deprecated methods.
  name: Bit2Me Verifier Deprecated Methods API
  slug: bit2me-verifier-deprecated-methods-api
- baseURL: https://gateway.bit2me.com
  baseurl_source: declared
  description: The Wallet API from Bit2Me — 8 operation(s) for wallet.
  name: Bit2Me Wallet API
  slug: bit2me-wallet-api
artifact_total: 32
asyncapis:
- description: ''
  name: Bit2Me Webhooks
  slug: bit2me-webhooks
common:
- group: design
  href: https://artifacts.apis.io/bit2me/json-ld/bit2me-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bit2me-context.jsonld
- group: agent
  href: https://artifacts.apis.io/bit2me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bit2me/asyncapi/bit2me-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bit2me-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bit2me/data-model/bit2me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bit2me-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bit2me/well-known/bit2me-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bit2me-status-security.txt
- group: other
  href: https://artifacts.apis.io/bit2me/capabilities/bit2me-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bit2me-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bit2me/agentic-access/bit2me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bit2me-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/bit2me/rate-limits/bit2me-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bit2me-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/bit2me/rules/bit2me-rules.yml
  title: ''
  type: Spectral
  url: rules/bit2me-rules.yml
- group: design
  href: https://artifacts.apis.io/bit2me/vocabulary/bit2me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bit2me-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/bit2me/changelog/bit2me-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bit2me-changelog.yml
- group: design
  href: https://artifacts.apis.io/bit2me/conventions/bit2me-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bit2me-conventions.yml
- group: design
  href: https://artifacts.apis.io/bit2me/conventions/bit2me-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bit2me-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bit2me.safebase.us/
- group: auth
  href: https://artifacts.apis.io/bit2me/authentication/bit2me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bit2me-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bit2me/scopes/bit2me-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bit2me-scopes.yml
- group: design
  href: https://artifacts.apis.io/bit2me/lifecycle/bit2me-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bit2me-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bit2me/errors/bit2me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bit2me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bit2me/conformance/bit2me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bit2me-conformance.yml
- group: other
  href: https://artifacts.apis.io/bit2me/overlays/bit2me-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bit2me-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/bit2me/llms/bit2me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bit2me-llms.txt
- group: agent
  href: https://artifacts.apis.io/bit2me/well-known/bit2me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bit2me-well-known.yml
- group: other
  href: https://artifacts.apis.io/bit2me/hosts/bit2me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bit2me-hosts.yml
- group: other
  href: https://artifacts.apis.io/bit2me/vendors/bit2me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bit2me-vendors.yml
- group: build
  href: https://artifacts.apis.io/bit2me/packages/bit2me-packages.yml
  title: ''
  type: SDKs
  url: packages/bit2me-packages.yml
- group: build
  href: https://artifacts.apis.io/bit2me/packages/bit2me-packages.yml
  title: ''
  type: Packages
  url: packages/bit2me-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bit2me.com
- group: auth
  title: ''
  type: Security
  url: https://bit2me.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://bit2me.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.bit2me.com/docs/wallet/changelog
- group: auth
  href: https://artifacts.apis.io/bit2me/security/bit2me-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bit2me-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bit2me/security/bit2me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bit2me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bit2me.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.bit2me.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.bit2me.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.bit2me.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.bit2me.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.bit2me.com
- group: company
  title: ''
  type: Blog
  url: https://blog.bit2me.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bit2me
- group: start
  title: ''
  type: SignUp
  url: https://app.bit2me.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.bit2me.com/en/support/solutions/articles/35000292850-general-terms-and-conditions-for-bit2me-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.bit2me.com/en/support/solutions/articles/35000291559-privacy-policy
created: '2026-10-28'
description: Bit2Me is a Spanish fintech founded in 2014 that offers a comprehensive cryptocurrency platform, including a regulated exchange, wallet services, merchant payments, and a public RESTful API for developers. The company provides tools for buying, selling, earning, and managing crypto assets, supports MiCA licensing, and serves individuals, businesses, and institutions across Europe. Its API enables access to wallets, trading, payments, custody, and compliance features, documented at https://api.bit2me.com/docs.
image: https://bit2me.com/assets/img/header/brand/bit2me-logo-light.svg
json_schemas:
- name: GetV1CurrencyRateResponse
  property_count: 2
  slug: bit2me-get-v1-currency-rate-response
- name: GetV1WalletPocketResponse
  property_count: 4
  slug: bit2me-get-v1-wallet-pocket-response
- name: GetV1WalletTransactionIdResponse
  property_count: 10
  slug: bit2me-get-v1-wallet-transaction-id-response
- name: PostV1WalletTransactionProformaRequest
  property_count: 4
  slug: bit2me-post-v1-wallet-transaction-proforma-request
- name: PostV1WalletTransactionResponse
  property_count: 6
  slug: bit2me-post-v1-wallet-transaction-response
- name: PostV2BlockchainManagerTravelRuleOrder550E8400E29B41D4A71644
  property_count: 7
  slug: bit2me-post-v2-blockchain-manager-travel-rule-order550-e8400-e29-b41-d4-a71644
jsonld:
- class_count: 13
  name: Bit2Me Context
  property_count: 35
  slug: bit2me-context
layout: provider
modified: '2026-10-28'
name: Bit2Me
nav: Providers
network: true
overview: 'Bit2Me publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account Deprecated Methods API, Auth API, and 13 more. Tagged areas include Company, Cryptocurrency, Fintech, Exchange, and Payments.


  The Bit2Me catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bit2Me''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 36 more developer resources.'
plans:
- name: Bit2Me Plans Pricing
  plan_count: 0
  slug: bit2me-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Bit2Me Rate Limits
  slug: bit2me-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Bit2Me API Rules
  rule_count: 52
  severity_counts:
    error: 39
    hint: 0
    info: 3
    warn: 10
  slug: bit2me-rules
scopes:
- name: Bit2Me Scopes
  scope_count: 3
  slug: bit2me-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 38
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.5
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 54.1
    developer_ergonomics: 48.1
    discoverability: 74.1
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 20.0
      derived: 4
      marker_coverage: 20.0
      total: 20
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bit2me/bit2me-2026-11-03T121746.png
security:
- kind: authentication
  name: Bit2Me Authentication
  slug: bit2me-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Bit2Me Domain Security
  slug: bit2me-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Bit2Me Trust Center
  slug: bit2me-trust-center
  summary_line: ISO 27001, GDPR
slug: bit2me
tags:
- Company
- Cryptocurrency
- Fintech
- Exchange
- Payments
website: https://bit2me.com/
---
