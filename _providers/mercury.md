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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Mercury Agentic Access
  operation_count: 19
  slug: mercury-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 16
apis:
- description: Read access to all Mercury accounts (checking, savings, treasury) opened under the authenticated organization. Returns account ID, name, type, status, current and available balances, account number, r
  name: Mercury Accounts API
  slug: accounts
- description: Lists and retrieves transactions for a given Mercury account. Supports filtering by date range, status (pending, sent, cancelled, failed), and amount, plus pagination. Returns counterparty information
  name: Mercury Transactions API
  slug: transactions
- description: Retrieves monthly account statements for a Mercury account. Each statement returns the start and end dates and a downloadable PDF URL.
  name: Mercury Statements API
  slug: statements
- description: Manages payment recipients (counterparties for outbound ACH and wire payments). Supports creating, retrieving, listing, updating, archiving, and approving recipients. Read-and-write access to this end
  name: Mercury Recipients API
  slug: recipients
- description: Sends outbound ACH and domestic wire payments from a Mercury account to a recipient. Includes operations for requesting a send-money payment, retrieving its status, and cancelling pending payments. Re
  name: Mercury Payments API
  slug: payments
- description: Read access to corporate card metadata - status, last four digits, the linked account, the card holder, and spending limits.
  name: Mercury Cards API
  slug: cards
- description: Surfaces treasury account details for organizations enrolled in Mercury Treasury, including yield, allocation across underlying money-market and Treasury bill portfolios, and current balance.
  name: Mercury Treasury API
  slug: treasury
- description: Subscribes a partner application to event notifications such as transaction created/updated, payment status change, and account balance threshold events. Mercury signs each delivery so receivers can v
  name: Mercury Webhooks API
  slug: webhooks
- description: The Accounts API from Mercury — 2 operation(s) for accounts.
  name: Mercury Accounts API
  slug: mercury-accounts-api
- description: The Cards API from Mercury — 1 operation(s) for cards.
  name: Mercury Cards API
  slug: mercury-cards-api
- description: The Payments API from Mercury — 2 operation(s) for payments.
  name: Mercury Payments API
  slug: mercury-payments-api
- description: The Recipients API from Mercury — 2 operation(s) for recipients.
  name: Mercury Recipients API
  slug: mercury-recipients-api
- description: The Statements API from Mercury — 1 operation(s) for statements.
  name: Mercury Statements API
  slug: mercury-statements-api
- description: The Transactions API from Mercury — 2 operation(s) for transactions.
  name: Mercury Transactions API
  slug: mercury-transactions-api
- description: The Treasury API from Mercury — 1 operation(s) for treasury.
  name: Mercury Treasury API
  slug: mercury-treasury-api
- description: The Webhooks API from Mercury — 2 operation(s) for webhooks.
  name: Mercury Webhooks API
  slug: mercury-webhooks-api
artifact_total: 35
asyncapis:
- description: AsyncAPI description of Mercury Banking's outbound webhook surface. Mercury delivers event notifications by issuing HTTP POST requests with a JSON body to a subscriber HTTPS endpoint that is registere
  name: Mercury Webhooks
  slug: mercury-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mercury Accounts API
  slug: open-mercury-accounts-api
- collection_type: open
  name: Mercury Accounts Cards API
  slug: open-mercury-cards-api
- collection_type: open
  name: Mercury Accounts Payments API
  slug: open-mercury-payments-api
- collection_type: open
  name: Mercury Accounts Recipients API
  slug: open-mercury-recipients-api
- collection_type: open
  name: Mercury Accounts Statements API
  slug: open-mercury-statements-api
- collection_type: open
  name: Mercury Accounts Transactions API
  slug: open-mercury-transactions-api
- collection_type: open
  name: Mercury Accounts Treasury API
  slug: open-mercury-treasury-api
- collection_type: open
  name: Mercury Accounts Webhooks API
  slug: open-mercury-webhooks-api
- collection_type: open
  name: Mercury API
  slug: open-mercury
common:
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mercury.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mercury.com/docs/getting-started
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mercury-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercury-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mercury-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MercuryTechnologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercuryhq
- group: company
  title: ''
  type: Website
  url: https://mercury.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mercury.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/mercury-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mercury-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mercury-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mercury.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://mercury.com/blog
created: '2026-05-08'
description: Mercury is a banking platform built for startups and tech companies, offering checking, savings, treasury, and corporate-card services. The Mercury REST API exposes accounts, transactions, statements, recipients, ACH and wire payments, treasury yield, and webhooks.
finops:
- name: Mercury Finops
  service_category: Banking
  slug: mercury-finops
graphqls:
- description: Mercury is a banking platform for startups and growth-stage companies. The API covers accounts, transactions, wire transfers, ACH payments, checks, debit cards, account statements, and treasury manage
  name: Mercury GraphQL API
  slug: mercury-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercury.png
layout: provider
modified: '2026-05-30'
name: Mercury
nav: Providers
network: true
overview: 'Mercury publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Accounts API, Cards API, and 6 more. Tagged areas include Banking, Fintech, Startups, Treasury, and Payments.


  The Mercury catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mercury''s developer surface includes changelog, getting-started guide, authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Mercury Plans Pricing
  plan_count: 3
  slug: mercury-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Mercury Rate Limits
  slug: mercury-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Mercury API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: mercury-asyncapi-spectral-rules
score:
  band: thin
  composite: 36.2
  delta: -3.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 65.2
    developer_ergonomics: 29.8
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mercury/refs/heads/main/screenshots/mercury-2026-06-20T185218.png
security:
- kind: authentication
  name: Mercury Authentication
  slug: mercury-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mercury Domain Security
  slug: mercury-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mercury
tags:
- Banking
- Fintech
- Startups
- Treasury
- Payments
website: https://mercury.com/
---
