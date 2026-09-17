---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: 'Banking APIs provide KYC (Know Your Customer) verification functionality to enable users to comply with financial regulations when using banking features. These endpoints manage identity verification '
  name: Accrue Savings Banking API
  slug: accrue-savings-banking-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Counterparties define bank accounts where funds are settled for captured payments. Settlement details live on `externalBankAccount`. There can be multiple counterparties.
  name: Accrue Savings Counterparties API
  slug: accrue-savings-counterparties-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Counterparty Transfers represent movements of funds between two counterparties owned by the same partner. Use these endpoints to initiate, list, and retrieve counterparty-to-counterparty transfers.
  name: Accrue Savings Counterparty Transfers API
  slug: accrue-savings-counterpartytransfers-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: External transactions are records of transfers that happened outside the Accrue system. E.g. purchases in an online shop using a non-Accrue payment method.
  name: Accrue Savings External Transactions API
  slug: accrue-savings-externaltransactions-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Gifts expose remaining spendable balance for a scanned lookUpId. Point-of-sale remaining lookup is GET /api/v1/gifts/{lookUpId}. Spend still uses payment intents with the same scanned string as lookUp
  name: Accrue Savings Gifts API
  slug: accrue-savings-gifts-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Identity Verification provides knowledge-based authentication for sensitive account changes. Use these endpoints to challenge a user with profile and wallet questions, then apply verified phone or ema
  name: Accrue Savings Identity Verification API
  slug: accrue-savings-identity-verification-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Payments are the realization of payment intents, representing the actual transfer or authorization of funds. This resource encapsulates the details of completed transactions, including the payment sta
  name: Accrue Savings Payments API
  slug: accrue-savings-payments-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Partner-issued rewards let trusted integrations credit customer wallets or create pre-issued rewards for recipients identified by phone number. When a recipient has an active wallet, rewards are depos
  name: Accrue Savings Rewards API
  slug: accrue-savings-rewards-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Simulations are used to simulate payments authorizations and captures for Card Rails (Virtual Debit Cards).
  name: Accrue Savings Simulations API
  slug: accrue-savings-simulations-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Sweepstakes campaigns give users the chance to win prizes by participating in merchant-sponsored promotions. Each campaign is linked to a specific merchant and tracks user entries. Users can earn entr
  name: Accrue Savings Sweepstakes API
  slug: accrue-savings-sweepstakes-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Users represent the end users and are the parent container of Wallets. A user is automatically created when the end-user signs into the Accrue product through various different methods using their pho
  name: Accrue Savings Users API
  slug: accrue-savings-users-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Wallets are where users save money and collect rewards for future payments to merchants. Each wallet is linked to a specific merchant and tracks the balance of deposits and rewards. Users can contribu
  name: Accrue Savings Wallets API
  slug: accrue-savings-wallets-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Webhook Topics
  name: Accrue Savings Webhook Topics API
  slug: accrue-savings-webhook-topics-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Webhook management APIs
  name: Accrue Savings Webhooks API
  slug: accrue-savings-webhooks-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: <p>Widgets are components that are embedded into applications to enrich the user experience. Some of those require additional data loaded through API endpoints.</p><p>Learn more about the different wi
  name: Accrue Savings Widgets API
  slug: accrue-savings-widgets-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Linked Accounts represent payment methods that users have connected to their Accrue account. These accounts can be used for funding payments or topping up the wallet.
  name: Accrue Savings Linked Accounts API
  slug: accrue-savings-linked-accounts-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Payment Intents represent a commitment to pay a specified amount, allowing for a structured process to handle payments from initiation to completion.
  name: Accrue Savings Payment Intents API
  slug: accrue-savings-payment-intents-api
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: Webhook Event management APIs
  name: Accrue Savings Webhook Events API
  slug: accrue-savings-webhook-events-api
artifact_total: 24
asyncapis:
- description: ''
  name: Accrue Savings Merchant Api Webhooks
  slug: accrue-savings-merchant-api-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/overlays/accrue-savings-merchant-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/accrue-savings-merchant-api-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/security/accrue-savings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accrue-savings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.byaccrue.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.byaccrue.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.byaccrue.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.byaccrue.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.byaccrue.com/getting-started-api
- group: operate
  title: ''
  type: Support
  url: https://www.byaccrue.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accrue-savings
- group: commercial
  title: ''
  type: TermsOfService
  url: https://files.byaccrue.com/048c1405-0e96-4033-af8f-ad353e48646f.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://files.byaccrue.com/61d09791-95f0-4030-8490-d7e7d061592c.pdf
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/packages/accrue-savings-packages.yml
  title: ''
  type: Packages
  url: packages/accrue-savings-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/packages/accrue-savings-packages.yml
  title: ''
  type: SDKs
  url: packages/accrue-savings-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/mcp/accrue-savings-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/accrue-savings-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/llms/accrue-savings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accrue-savings-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/conformance/accrue-savings-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accrue-savings-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/errors/accrue-savings-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accrue-savings-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/errors/accrue-savings-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/accrue-savings-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/lifecycle/accrue-savings-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/accrue-savings-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accruesavings.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/authentication/accrue-savings-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accrue-savings-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.byaccrue.com/
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/sandbox/accrue-savings-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/accrue-savings-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/conventions/accrue-savings-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accrue-savings-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/conventions/accrue-savings-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/accrue-savings-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.byaccrue.com/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/components/accrue-savings-components.yml
  title: ''
  type: Components
  url: components/accrue-savings-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/data-model/accrue-savings-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accrue-savings-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/asyncapi/accrue-savings-merchant-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/accrue-savings-merchant-api-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/plans/accrue-savings-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accrue-savings-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/accrue-savings/refs/heads/main/rate-limits/accrue-savings-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/accrue-savings-rate-limits.yml
created: '2026-09-06'
description: Accrue Savings (legally Accrue Money, Inc., now trading as Accrue at byaccrue.com) is a New York fintech that powers customer loyalty at the payment layer with a branded stored-value wallet merchants embed in their own checkout. Its platform lets brands hold customer funds in a wallet, accept payments over wallet and bank rails, run a rules-driven reward engine, return refunds as closed-loop credit, and let shoppers pre-fund or crowdfund a future purchase. The Accrue Merchant API is a public, JSON:API-shaped OpenAPI 3.1 contract covering wallets, payment intents, payments, users, KYC and identity verification, counterparties and payouts, linked accounts, rewards, gifts, sweepstakes, external transactions and webhooks, with a sandbox environment, mobile SDKs for iOS/Android/React Native/Expo, and embeddable web wallet widgets. Banking services are provided by Cross River Bank, Member FDIC.
image: https://docs.byaccrue.com/img/accrue-logo.svg
layout: provider
modified: '2026-09-06'
name: Accrue Savings
nav: Providers
network: true
overview: 'Accrue Savings publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Banking API, Counterparties API, Counterparty Transfers API, and 15 more. Tagged areas include Company, Payments, Loyalty, Wallets, and Stored Value.


  The Accrue Savings catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Accrue Savings'' developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 25 more developer resources.'
plans:
- name: Accrue Savings Plans Pricing
  plan_count: 0
  slug: accrue-savings-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Accrue Savings Rate Limits
  slug: accrue-savings-rate-limits
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 57.1
    developer_ergonomics: 70.8
    discoverability: 75.9
    operational_transparency: 55.3
  previous_composite: 56.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 53.1
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Accrue Savings Authentication
  slug: accrue-savings-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Accrue Savings Domain Security
  slug: accrue-savings-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Accrue Savings Trust Center
  slug: accrue-savings-trust-center
  summary_line: trust center published
slug: accrue-savings
tags:
- Company
- Payments
- Loyalty
- Wallets
- Stored Value
- Rewards
- Banking
- Fintech
- Webhook
website: https://www.byaccrue.com/
---
