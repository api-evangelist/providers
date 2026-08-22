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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 11
  human_in_the_loop: 5
  name: Doku Agentic Access
  operation_count: 19
  slug: doku-agentic-access
  summary_line: 19 operations · 11 acting · 5 human-in-the-loop
api_count: 6
apis:
- description: SNAP B2B / B2B2C access-token issuance.
  name: DOKU Access Token API
  slug: doku-access-token-api
- description: DOKU-hosted checkout page (non-SNAP).
  name: DOKU Checkout API
  slug: doku-checkout-api
- description: SNAP account binding and host-to-host debit for e-wallets and bank direct debit.
  name: DOKU Direct Debit & e-Wallet API
  slug: doku-direct-debit-e-wallet-api
- description: Kirim DOKU disbursement to bank accounts.
  name: DOKU Payout API
  slug: doku-payout-api
- description: SNAP QRIS Merchant-Presented Mode.
  name: DOKU QRIS API
  slug: doku-qris-api
- description: SNAP BI-SNAP Virtual Account lifecycle.
  name: DOKU Virtual Account API
  slug: doku-virtual-account-api
artifact_total: 29
asyncapis:
- description: ''
  name: Doku Webhooks
  slug: doku-webhooks
collections:
- collection_type: postman
  name: DOKU Payment Access Token API
  slug: postman-doku-access-token-api
- collection_type: postman
  name: DOKU Payment Access Token Checkout API
  slug: postman-doku-checkout-api
- collection_type: postman
  name: DOKU Payment Access Token Direct Debit & e-Wallet API
  slug: postman-doku-direct-debit-e-wallet-api
- collection_type: postman
  name: DOKU Payment Access Token Payout API
  slug: postman-doku-payout-api
- collection_type: postman
  name: DOKU Payment Access Token QRIS API
  slug: postman-doku-qris-api
- collection_type: postman
  name: DOKU Payment Access Token Virtual Account API
  slug: postman-doku-virtual-account-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DOKU Payment Access Token API
  slug: open-doku-access-token-api
- collection_type: open
  name: DOKU Payment Access Token Checkout API
  slug: open-doku-checkout-api
- collection_type: open
  name: DOKU Payment Access Token Direct Debit & e-Wallet API
  slug: open-doku-direct-debit-e-wallet-api
- collection_type: open
  name: DOKU Payment Access Token Payout API
  slug: open-doku-payout-api
- collection_type: open
  name: DOKU Payment Access Token QRIS API
  slug: open-doku-qris-api
- collection_type: open
  name: DOKU Payment Access Token Virtual Account API
  slug: open-doku-virtual-account-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/doku/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doku-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/doku-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doku-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doku-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doku-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PTNUSASATUINTIARTHA-DOKU
- group: company
  title: ''
  type: Website
  url: https://www.doku.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.doku.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/doku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doku-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.doku.com/en-us/blog
- group: build
  title: ''
  type: Packages
  url: packages/doku-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/doku-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/doku-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doku-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/doku-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/doku-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/doku-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/doku-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/doku-decline-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/doku-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.doku.com/security/licenses
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doku-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doku.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.doku.com/miscellaneous/snap-migration
- group: start
  title: ''
  type: Sandbox
  url: sandbox/doku-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/doku-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/doku-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.doku.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.doku.com/get-started-with-doku-api/user-registration
- group: operate
  title: ''
  type: Support
  url: https://help.doku.com/en/support/home
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doku.com/en-us/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.doku.com/bo/registration
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashboard.doku.com/doku-agreement/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashboard.doku.com/doku-agreement/privacy-policy
created: '2026-07-17'
description: DOKU (PT Nusa Satu Inti Artha) is Indonesia's pioneering payment gateway, founded in 2007 and licensed by Bank Indonesia as a Category 1 Payment Service Provider. Its developer platform exposes a hosted Checkout API plus a full suite of Bank Indonesia SNAP (Standar Nasional Open API Pembayaran) endpoints for Virtual Account, e-Wallet, Direct Debit, QRIS, and Kirim (payout/disbursement), all settling in Indonesian Rupiah (IDR).
finops:
- name: Doku Finops
  service_category: Payment Processing
  slug: doku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doku.png
layout: provider
mcp_servers:
- description: ''
  name: doku-mcp.yml
  slug: doku-mcpyml
modified: '2026-07-17'
name: DOKU
nav: Providers
network: true
overview: 'DOKU publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Checkout API, Direct Debit & e-Wallet API, and 3 more. Tagged areas include Payments, Payment Gateway, Fintech, Indonesia, and SEA.


  The DOKU catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DOKU''s developer surface includes authentication, documentation, engineering blog, sandbox, getting-started guide, support, pricing, and 31 more developer resources.'
plans:
- name: Doku Plans Pricing
  plan_count: 3
  slug: doku-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Doku Rate Limits
  slug: doku-rate-limits
score:
  band: exemplar
  composite: 71.3
  delta: 2.9
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 30.3
    contract_quality: 61.1
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 68.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doku/refs/heads/main/screenshots/doku-2026-07-25T212238.png
security:
- kind: authentication
  name: Doku Authentication
  slug: doku-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Doku Domain Security
  slug: doku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Doku Vulnerability Disclosure
  slug: doku-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Doku Trust Center
  slug: doku-trust-center
  summary_line: PCI DSS Level 1 Service Provider, ISO/IEC 27001, AES-256 encryption standard
slug: doku
tags:
- Payments
- Payment Gateway
- Fintech
- Indonesia
- SEA
- SNAP
- Virtual Account
- E-Wallet
- QRIS
- Direct Debit
- Payouts
website: https://www.doku.com/
---
