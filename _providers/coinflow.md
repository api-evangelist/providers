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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 116
  human_in_the_loop: 3
  name: Coinflow Agentic Access
  operation_count: 180
  slug: coinflow-agentic-access
  summary_line: 180 operations · 116 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The authentication API from Coinflow — 3 operation(s) for authentication.
  name: Coinflow Authentication API
  slug: coinflow-authentication-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The checkout API from Coinflow — 33 operation(s) for checkout.
  name: Coinflow Checkout API
  slug: coinflow-checkout-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The customers API from Coinflow — 15 operation(s) for customers.
  name: Coinflow Customers API
  slug: coinflow-customers-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The events API from Coinflow — 1 operation(s) for events.
  name: Coinflow Events API
  slug: coinflow-events-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The marketplace API from Coinflow — 11 operation(s) for marketplace.
  name: Coinflow Marketplace API
  slug: coinflow-marketplace-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The merchant API from Coinflow — 49 operation(s) for merchant.
  name: Coinflow Merchant API
  slug: coinflow-merchant-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The merchantSubscription API from Coinflow — 4 operation(s) for merchantsubscription.
  name: Coinflow Merchant Subscription API
  slug: coinflow-merchantsubscription-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The redeem API from Coinflow — 4 operation(s) for redeem.
  name: Coinflow Redeem API
  slug: coinflow-redeem-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The refund API from Coinflow — 4 operation(s) for refund.
  name: Coinflow Refund API
  slug: coinflow-refund-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The subMerchant API from Coinflow — 3 operation(s) for submerchant.
  name: Coinflow Sub Merchant API
  slug: coinflow-submerchant-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The subscription API from Coinflow — 7 operation(s) for subscription.
  name: Coinflow Subscription API
  slug: coinflow-subscription-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The utilities API from Coinflow — 3 operation(s) for utilities.
  name: Coinflow Utilities API
  slug: coinflow-utilities-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The withdraw API from Coinflow — 30 operation(s) for withdraw.
  name: Coinflow Withdraw API
  slug: coinflow-withdraw-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The merchantAccounts API from Coinflow — 5 operation(s) for merchantaccounts.
  name: Coinflow Merchant Accounts API
  slug: coinflow-merchantaccounts-api
- baseURL: https://api.coinflow.cash/api
  baseurl_source: declared
  description: The Card Tokenization API from Coinflow — 4 operation(s) for card tokenization.
  name: Coinflow Card Tokenization API
  slug: coinflow-card-tokenization-api
artifact_total: 39
asyncapis:
- description: ''
  name: Coinflow Webhooks
  slug: coinflow-webhooks
collections:
- collection_type: open
  name: API Reference authentication API
  slug: open-coinflow-authentication-api
- collection_type: open
  name: API Reference authentication cardTokenization API
  slug: open-coinflow-cardtokenization-api
- collection_type: open
  name: API Reference authentication checkout API
  slug: open-coinflow-checkout-api
- collection_type: open
  name: API Reference authentication customers API
  slug: open-coinflow-customers-api
- collection_type: open
  name: API Reference authentication events API
  slug: open-coinflow-events-api
- collection_type: open
  name: API Reference authentication marketplace API
  slug: open-coinflow-marketplace-api
- collection_type: open
  name: API Reference authentication merchant API
  slug: open-coinflow-merchant-api
- collection_type: open
  name: API Reference authentication merchantSubscription API
  slug: open-coinflow-merchantsubscription-api
- collection_type: open
  name: API Reference authentication redeem API
  slug: open-coinflow-redeem-api
- collection_type: open
  name: API Reference authentication refund API
  slug: open-coinflow-refund-api
- collection_type: open
  name: API Reference authentication subMerchant API
  slug: open-coinflow-submerchant-api
- collection_type: open
  name: API Reference authentication subscription API
  slug: open-coinflow-subscription-api
- collection_type: open
  name: API Reference authentication utilities API
  slug: open-coinflow-utilities-api
- collection_type: open
  name: API Reference authentication withdraw API
  slug: open-coinflow-withdraw-api
common:
- group: other
  href: https://artifacts.apis.io/coinflow/capabilities/coinflow-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/coinflow-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://coinflow.cash/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coinflow.cash/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coinflow.cash/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coinflow.cash/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coinflow.cash/guides/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://coinflow.cash/blog/
- group: operate
  title: ''
  type: Support
  url: https://coinflow.cash/contact/
- group: start
  title: ''
  type: SignUp
  url: https://app.coinflow.cash/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinflow.cash/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinflow.cash/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinflow.cash/
- group: auth
  title: ''
  type: Security
  url: https://coinflow.cash/bug-bounty
- group: auth
  title: ''
  type: Compliance
  url: https://docs.coinflow.cash/guides/product-overview/key-concepts
- group: docs
  href: https://artifacts.apis.io/coinflow/openapi/_original/coinflow-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/coinflow-openapi-original.json
- group: agent
  href: https://artifacts.apis.io/coinflow/llms/coinflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinflow-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinflow/well-known/coinflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinflow-well-known.yml
- group: auth
  href: https://artifacts.apis.io/coinflow/well-known/coinflow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinflow-security.txt
- group: build
  href: https://artifacts.apis.io/coinflow/packages/coinflow-packages.yml
  title: ''
  type: Packages
  url: packages/coinflow-packages.yml
- group: build
  href: https://artifacts.apis.io/coinflow/packages/coinflow-packages.yml
  title: ''
  type: SDKs
  url: packages/coinflow-packages.yml
- group: design
  href: https://artifacts.apis.io/coinflow/components/coinflow-components.yml
  title: ''
  type: Components
  url: components/coinflow-components.yml
- group: agent
  href: https://artifacts.apis.io/coinflow/mcp/coinflow-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/coinflow-mcp.yml
- group: start
  href: https://artifacts.apis.io/coinflow/sandbox/coinflow-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/coinflow-sandbox.yml
- group: design
  href: https://artifacts.apis.io/coinflow/conventions/coinflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coinflow-conventions.yml
- group: design
  href: https://artifacts.apis.io/coinflow/conventions/coinflow-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/coinflow-conventions.yml
- group: design
  href: https://artifacts.apis.io/coinflow/lifecycle/coinflow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coinflow-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/coinflow/errors/coinflow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinflow-problem-types.yml
- group: build
  href: https://artifacts.apis.io/coinflow/errors/coinflow-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/coinflow-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/coinflow/conformance/coinflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinflow-conformance.yml
- group: design
  href: https://artifacts.apis.io/coinflow/data-model/coinflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coinflow-data-model.yml
- group: design
  href: https://artifacts.apis.io/coinflow/asyncapi/coinflow-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coinflow-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/coinflow/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/coinflow/overlays/coinflow-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/coinflow-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/coinflow/security/coinflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinflow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coinflow/security/coinflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinflow-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/coinflow/agentic-access/coinflow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coinflow-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/coinflow/authentication/coinflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coinflow-authentication.yml
created: '2026-07-17'
description: Coinflow is a stablecoin-native payments platform (backed by Pantera Capital) that lets software companies and marketplaces accept card, ACH, and crypto/USDC payments and send instant payouts across Solana, EVM, and Stellar rails. Its API covers checkout / pay-ins, PCI-compliant tokenized card-on-file, subscriptions, marketplace sub-merchant onboarding with KYC/KYB, refunds, withdrawals and merchant payouts, and HMAC-signed webhooks. Coinflow ships pre-built UI SDKs for React, React Native, Swift, Android, and Flutter, plus a sandbox environment with published test cards and 3DS triggers.
image: https://coinflow.cash/coinflow-og-image.jpg
layout: provider
modified: '2026-07-18'
name: Coinflow
nav: Providers
network: true
overview: 'Coinflow publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Checkout API, Customers API, and 12 more. Tagged areas include Company, Cryptocurrency, Payments, Stablecoins, and USDC.


  The Coinflow catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Coinflow''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, sandbox, and 30 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Coinflow API Rules
  rule_count: 51
  severity_counts:
    error: 37
    hint: 0
    info: 3
    warn: 11
  slug: coinflow-rules
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 73.2
    discoverability: 71.7
    operational_transparency: 34.2
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/coinflow/coinflow-2026-07-25T210028.png
security:
- kind: authentication
  name: Coinflow Authentication
  slug: coinflow-authentication
  summary_line: apiKey · 7 schemes
- kind: domain-security
  name: Coinflow Domain Security
  slug: coinflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinflow Vulnerability Disclosure
  slug: coinflow-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: Create a customer and subscribe them to a plan
  slug: coinflow-create-subscription
- name: Quote and execute a merchant payout
  slug: coinflow-merchant-payout
- name: Refund a payment and reconcile via webhooks
  slug: coinflow-refund-and-webhooks
- name: Take a card payment with Coinflow
  slug: coinflow-take-card-payment
slug: coinflow
tags:
- Company
- Cryptocurrency
- Payments
- Stablecoins
- USDC
- Checkout
- Payouts
- Marketplace
- Web3
- Fintech
website: https://coinflow.cash/
---
