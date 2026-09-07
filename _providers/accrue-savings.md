---
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-09-06'
api_count: 1
apis:
- baseURL: https://merchant-api.accruesavings.com
  baseurl_source: declared
  description: The Accrue Merchant API is a JSON:API-based REST API for embedding Accrue's stored-value wallet into a merchant experience — creating and funding wallets, running payment intents and payments (authori
  name: Accrue Merchant API
  slug: accrue-savings-merchant-api
artifact_total: 7
asyncapis:
- description: ''
  name: Accrue Savings Merchant Api Webhooks
  slug: accrue-savings-merchant-api-webhooks
common:
- group: auth
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
  title: ''
  type: Packages
  url: packages/accrue-savings-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/accrue-savings-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/accrue-savings-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accrue-savings-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/accrue-savings-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accrue-savings-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/accrue-savings-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accrue-savings-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accruesavings.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/accrue-savings-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.byaccrue.com/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/accrue-savings-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accrue-savings-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/accrue-savings-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.byaccrue.com/changelog
- group: design
  title: ''
  type: Components
  url: components/accrue-savings-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accrue-savings-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/accrue-savings-merchant-api-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accrue-savings-plans-pricing.yml
- group: operate
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
overview: 'Accrue Savings publishes 1 API on the [APIs.io](https://apis.io/) network: Accrue Merchant API. Tagged areas include Company, Payments, Loyalty, Wallets, and Stored Value.


  The Accrue Savings catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Accrue Savings'' developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 24 more developer resources.'
plans:
- name: Accrue Savings Plans Pricing
  plan_count: 0
  slug: accrue-savings-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Accrue Savings Rate Limits
  slug: accrue-savings-rate-limits
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 63.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 53.1
  schema_version: 0.19.0
  scored_at: '2026-09-06'
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
- Webhooks
website: https://www.byaccrue.com/
---
