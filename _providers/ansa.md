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
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Ansa Agentic Access
  operation_count: 53
  slug: ansa-agentic-access
  summary_line: 53 operations · 34 acting
api_count: 7
apis:
- description: The Add Incentive API from Ansa — 1 operation(s) for add incentive.
  name: Ansa Add Incentive API
  slug: ansa-add-incentive-api
- description: The Customer Segments API from Ansa — 3 operation(s) for customer segments.
  name: Ansa Customer Segments API
  slug: ansa-customer-segments-api
- description: The Customers API from Ansa — 19 operation(s) for customers.
  name: Ansa Customers API
  slug: ansa-customers-api
- description: The Initialize Payment Session API from Ansa — 1 operation(s) for initialize payment session.
  name: Ansa Initialize Payment Session API
  slug: ansa-initialize-payment-session-api
- description: The Merchants API from Ansa — 10 operation(s) for merchants.
  name: Ansa Merchants API
  slug: ansa-merchants-api
- description: The Refunds API from Ansa — 3 operation(s) for refunds.
  name: Ansa Refunds API
  slug: ansa-refunds-api
- description: The Transactions API from Ansa — 3 operation(s) for transactions.
  name: Ansa Transactions API
  slug: ansa-transactions-api
artifact_total: 21
asyncapis:
- description: ''
  name: Ansa Webhooks
  slug: ansa-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ansa Add Incentive API
  slug: open-ansa-add-incentive-api
- collection_type: open
  name: Ansa Add Incentive Customer Segments API
  slug: open-ansa-customer-segments-api
- collection_type: open
  name: Ansa Add Incentive Customers API
  slug: open-ansa-customers-api
- collection_type: open
  name: Ansa Add Incentive Initialize Payment Session API
  slug: open-ansa-initialize-payment-session-api
- collection_type: open
  name: Ansa Add Incentive Merchants API
  slug: open-ansa-merchants-api
- collection_type: open
  name: Ansa Add Incentive Refunds API
  slug: open-ansa-refunds-api
- collection_type: open
  name: Ansa Add Incentive Transactions API
  slug: open-ansa-transactions-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ansa.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ansa.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ansa.dev/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ansa.dev/docs/get-started-with-ansa
- group: company
  title: ''
  type: Blog
  url: https://www.ansa.dev/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@getansa.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetAnsa
- group: start
  title: ''
  type: Login
  url: https://portal.getansa.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ansa.dev/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ansa.dev/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getansa.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ansa-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ansa-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ansa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ansa-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/ansa-decline-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ansa-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ansa-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/ansa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ansa-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ansa-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ansa-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/ansa-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/ansa-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/ansa-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ansa-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ansa-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ansa-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ansa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ansa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ansa.dev/
created: '2026-07-17'
description: Ansa is a stored-value platform that lets businesses launch branded digital wallets — closed-loop balances, incentives, and loyalty — to turn payments into a revenue and retention driver. Its REST API and mobile SDKs (AnsaCore and AnsaUI for iOS, Android, and React Native) cover customers, payment methods, wallet funding, transactions, refunds, customer segments, incentive campaigns, promotional accounts, virtual cards, settlements, and webhooks. Authentication is via environment-scoped API keys with idempotency and cursor pagination. Ansa is backed by Bain Capital Ventures and targets marketplaces, platform businesses, and quick-service restaurants.
image: https://cdn.prod.website-files.com/64de31babb6dd82d228e90ab/66281fc1b9e68f64aa95a0e3_meta_image_ansa_home.png
layout: provider
mcp_servers:
- description: ''
  name: ansa-mcp.yml
  slug: ansa-mcpyml
modified: '2026-07-17'
name: Ansa
nav: Providers
network: true
overview: 'Ansa publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Add Incentive API, Customer Segments API, Customers API, and 4 more. Tagged areas include Company, Fintech, Payments, Stored Value, and Digital Wallet.


  The Ansa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ansa''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 25 more developer resources.'
random_paper: 20
score:
  band: strong
  composite: 54.4
  delta: 1.2
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 62.4
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ansa/refs/heads/main/screenshots/ansa-2026-07-25T200309.png
security:
- kind: authentication
  name: Ansa Authentication
  slug: ansa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ansa Domain Security
  slug: ansa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ansa Trust Center
  slug: ansa-trust-center
  summary_line: SOC 2
slug: ansa
tags:
- Company
- Fintech
- Payments
- Stored Value
- Digital Wallet
- Loyalty
- Incentives
- API
website: https://www.ansa.dev/
---
