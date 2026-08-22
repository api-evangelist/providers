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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 8
  name: Overflow Agentic Access
  operation_count: 38
  slug: overflow-agentic-access
  summary_line: 38 operations · 8 acting · 8 human-in-the-loop
api_count: 13
apis:
- description: The Campaigns API from Overflow — 2 operation(s) for campaigns.
  name: Overflow Campaigns API
  slug: overflow-campaigns-api
- description: The Chargebacks API from Overflow — 2 operation(s) for chargebacks.
  name: Overflow Chargebacks API
  slug: overflow-chargebacks-api
- description: The Contributions API from Overflow — 3 operation(s) for contributions.
  name: Overflow Contributions API
  slug: overflow-contributions-api
- description: The Deposits API from Overflow — 3 operation(s) for deposits.
  name: Overflow Deposits API
  slug: overflow-deposits-api
- description: The Donors API from Overflow — 2 operation(s) for donors.
  name: Overflow Donors API
  slug: overflow-donors-api
- description: The Locations API from Overflow — 2 operation(s) for locations.
  name: Overflow Locations API
  slug: overflow-locations-api
- description: The Payment Methods API from Overflow — 1 operation(s) for payment methods.
  name: Overflow Payment Methods API
  slug: overflow-payment-methods-api
- description: The Payments API from Overflow — 1 operation(s) for payments.
  name: Overflow Payments API
  slug: overflow-payments-api
- description: The Refunds API from Overflow — 2 operation(s) for refunds.
  name: Overflow Refunds API
  slug: overflow-refunds-api
- description: The Status API from Overflow — 1 operation(s) for status.
  name: Overflow Status API
  slug: overflow-status-api
- description: The Subscriptions API from Overflow — 3 operation(s) for subscriptions.
  name: Overflow Subscriptions API
  slug: overflow-subscriptions-api
- description: The Tap API from Overflow — 7 operation(s) for tap.
  name: Overflow Tap API
  slug: overflow-tap-api
- description: The Webhooks API from Overflow — 3 operation(s) for webhooks.
  name: Overflow Webhooks API
  slug: overflow-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Overflow Webhooks
  slug: overflow-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Overflow Open Campaigns API
  slug: open-overflow-campaigns-api
- collection_type: open
  name: Overflow Open Campaigns Chargebacks API
  slug: open-overflow-chargebacks-api
- collection_type: open
  name: Overflow Open Campaigns Contributions API
  slug: open-overflow-contributions-api
- collection_type: open
  name: Overflow Open Campaigns Deposits API
  slug: open-overflow-deposits-api
- collection_type: open
  name: Overflow Open Campaigns Donors API
  slug: open-overflow-donors-api
- collection_type: open
  name: Overflow Open Campaigns Locations API
  slug: open-overflow-locations-api
- collection_type: open
  name: Overflow Open Campaigns Payment Methods API
  slug: open-overflow-payment-methods-api
- collection_type: open
  name: Overflow Open Campaigns Payments API
  slug: open-overflow-payments-api
- collection_type: open
  name: Overflow Open Campaigns Refunds API
  slug: open-overflow-refunds-api
- collection_type: open
  name: Overflow Open Campaigns Status API
  slug: open-overflow-status-api
- collection_type: open
  name: Overflow Open Campaigns Subscriptions API
  slug: open-overflow-subscriptions-api
- collection_type: open
  name: Overflow Open Campaigns Tap API
  slug: open-overflow-tap-api
- collection_type: open
  name: Overflow Open Campaigns Webhooks API
  slug: open-overflow-webhooks-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.overflow.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.overflow.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.overflow.co/api-reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.overflow.co/api-reference/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/overflow-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.overflow.co/api-reference/rate-limiting
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/overflow-webhooks.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.overflow.co
- group: company
  title: ''
  type: Blog
  url: https://www.overflow.co/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/overflow-co
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.overflow.co/login
- group: start
  title: ''
  type: Login
  url: https://dashboard.overflow.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.overflow.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.overflow.co/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/overflow-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/overflow-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/overflow-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/overflow-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/overflow-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/overflow-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overflow-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/overflow-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/overflow-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/overflow-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/overflow-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Overflow is a fintech giving platform for churches and nonprofits that lets organizations accept and reconcile donations across many asset types — card and ACH, Apple Pay and Google Pay, stock, cryptocurrency, RoundUps, and Donor Advised Funds (DAFs) — through a single unified platform. Overflow also offers Overflow Tap (NFC tap-to-give hardware) and Generosity University donor education. Its public Overflow Open API (v3) is a REST interface over contributions, donors, subscriptions (recurring gifts), payments, campaigns, deposits, refunds, chargebacks, locations, tap devices/events, and webhooks, authenticated with header API keys and used to sync giving data into CRMs and accounting/reconciliation workflows. Overflow is backed by Uncork Capital.
image: https://cdn.prod.website-files.com/661982b7ce6b433411c6e0c8/661986ff805671631abc51f8_Open%20Graph%20Image.webp
layout: provider
mcp_servers:
- description: ''
  name: overflow-mcp.yml
  slug: overflow-mcpyml
modified: '2026-07-20'
name: Overflow
nav: Providers
network: true
overview: 'Overflow publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Chargebacks API, Contributions API, and 10 more. Tagged areas include Company, Fintech, Payments, Donations, and Fundraising.


  The Overflow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Overflow''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, sandbox, and 19 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 49.4
  delta: 2.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 63.0
    developer_ergonomics: 61.3
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/overflow/refs/heads/main/screenshots/overflow-2026-08-07T191125.png
security:
- kind: authentication
  name: Overflow Authentication
  slug: overflow-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Overflow Domain Security
  slug: overflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: overflow
tags:
- Company
- Fintech
- Payments
- Donations
- Fundraising
- Nonprofit
- Giving
- Recurring Payments
- Webhooks
- Cryptocurrency
website: https://docs.overflow.co
---
