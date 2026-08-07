---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-08-06'
api_count: 14
apis:
- description: The Customer Links API from Imprint — 1 operation(s) for customer links.
  name: Imprint Customer Links API
  slug: imprint-customer-links-api
- description: The Customer Sessions API from Imprint — 2 operation(s) for customer sessions.
  name: Imprint Customer Sessions API
  slug: imprint-customer-sessions-api
- description: The Customers API from Imprint — 7 operation(s) for customers.
  name: Imprint Customers API
  slug: imprint-customers-api
- description: The Keys API from Imprint — 1 operation(s) for keys.
  name: Imprint Keys API
  slug: imprint-keys-api
- description: The Offers API from Imprint — 1 operation(s) for offers.
  name: Imprint Offers API
  slug: imprint-offers-api
- description: The Order Events API from Imprint — 2 operation(s) for order events.
  name: Imprint Order Events API
  slug: imprint-order-events-api
- description: The Orders API from Imprint — 2 operation(s) for orders.
  name: Imprint Orders API
  slug: imprint-orders-api
- description: The Payment Methods API from Imprint — 2 operation(s) for payment methods.
  name: Imprint Payment Methods API
  slug: imprint-payment-methods-api
- description: The Rewards API from Imprint — 2 operation(s) for rewards.
  name: Imprint Rewards API
  slug: imprint-rewards-api
- description: The Simulate Reward API from Imprint — 1 operation(s) for simulate reward.
  name: Imprint Simulate Reward API
  slug: imprint-simulate-reward-api
- description: The Simulate Statement Reward API from Imprint — 1 operation(s) for simulate statement reward.
  name: Imprint Simulate Statement Reward API
  slug: imprint-simulate-statement-reward-api
- description: The Simulate Transaction Event API from Imprint — 1 operation(s) for simulate transaction event.
  name: Imprint Simulate Transaction Event API
  slug: imprint-simulate-transaction-event-api
- description: The Transaction Intents API from Imprint — 2 operation(s) for transaction intents.
  name: Imprint Transaction Intents API
  slug: imprint-transaction-intents-api
- description: The Transactions API from Imprint — 1 operation(s) for transactions.
  name: Imprint Transactions API
  slug: imprint-transactions-api
artifact_total: 19
asyncapis:
- description: ''
  name: Imprint Webhooks
  slug: imprint-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://imprint.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.imprint.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.imprint.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.imprint.co/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.imprint.co/welcome
- group: operate
  title: ''
  type: Support
  url: https://imprint.co/support
- group: company
  title: ''
  type: Blog
  url: https://tech.imprint.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Imprint-Tech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imprint.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imprint.co/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.imprint.co/partners
- group: auth
  title: ''
  type: TrustCenter
  url: security/imprint-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.imprint.co/
- group: auth
  title: ''
  type: Authentication
  url: authentication/imprint-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/imprint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/imprint-packages.yml
- group: design
  title: ''
  type: Components
  url: components/imprint-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/imprint-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imprint-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/imprint-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/imprint-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/imprint-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/imprint-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/imprint-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/imprint-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/imprint-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/imprint-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/imprint-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imprint-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Imprint is a financial technology company that builds bespoke co-branded credit cards, deposit accounts, and installment loans for consumer brands such as Shell, Rakuten, and Booking.com. Its Imprint Core platform powers the full lifecycle of a co-branded program - application, card issuance, transactions, rewards, and account management. The public Imprint API (v2) lets partners create customer sessions that hand a client_secret to embeddable Web/iOS/Android SDKs, manage customers and payment methods, track transaction intents and transactions, run reward programs, manage orders, and receive HMAC-signed webhook event notifications. Authentication is via environment-specific API keys (HTTP Basic or Bearer), with separate sandbox and production environments.
image: https://framerusercontent.com/assets/CVGaxWn2JW3mV5KWWXmkzXVM.png
layout: provider
mcp_servers:
- description: ''
  name: imprint-mcp.yml
  slug: imprint-mcpyml
modified: '2026-07-19'
name: Imprint
nav: Providers
network: true
overview: 'Imprint publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Customer Links API, Customer Sessions API, Customers API, and 11 more. Tagged areas include Company, Financial Services, Fintech, Credit Cards, and Co-Branded Cards.


  The Imprint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Imprint''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 23 more developer resources.'
random_paper: 93
score:
  band: developing
  composite: 54.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 70.6
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 54.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imprint/refs/heads/main/screenshots/imprint-2026-07-25T222200.png
security:
- kind: authentication
  name: Imprint Authentication
  slug: imprint-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Imprint Domain Security
  slug: imprint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Imprint Trust Center
  slug: imprint-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: imprint
tags:
- Company
- Financial Services
- Fintech
- Credit Cards
- Co-Branded Cards
- Payments
- Loans
- Rewards
- Loyalty
- Embedded Finance
website: https://imprint.co/
---
