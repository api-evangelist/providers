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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-19'
api_count: 12
apis:
- description: The Business Details API from Mamo — 2 operation(s) for business details.
  name: Mamo Business Details API
  slug: mamo-business-details-api
- description: The Cards API from Mamo — 5 operation(s) for cards.
  name: Mamo Cards API
  slug: mamo-cards-api
- description: The Expenses API from Mamo — 1 operation(s) for expenses.
  name: Mamo Expenses API
  slug: mamo-expenses-api
- description: The Getting Started API from Mamo — 1 operation(s) for getting started.
  name: Mamo Getting Started API
  slug: mamo-getting-started-api
- description: The Invoices API from Mamo — 1 operation(s) for invoices.
  name: Mamo Invoices API
  slug: mamo-invoices-api
- description: The Payment Links API from Mamo — 2 operation(s) for payment links.
  name: Mamo Payment Links API
  slug: mamo-payment-links-api
- description: The Payouts API from Mamo — 2 operation(s) for payouts.
  name: Mamo Payouts API
  slug: mamo-payouts-api
- description: The Receipts API from Mamo — 2 operation(s) for receipts.
  name: Mamo Receipts API
  slug: mamo-receipts-api
- description: The Recipients API from Mamo — 2 operation(s) for recipients.
  name: Mamo Recipients API
  slug: mamo-recipients-api
- description: The Subscriptions API from Mamo — 6 operation(s) for subscriptions.
  name: Mamo Subscriptions API
  slug: mamo-subscriptions-api
- description: The Transactions API from Mamo — 7 operation(s) for transactions.
  name: Mamo Transactions API
  slug: mamo-transactions-api
- description: The Webhooks API from Mamo — 2 operation(s) for webhooks.
  name: Mamo Webhooks API
  slug: mamo-webhooks-api
artifact_total: 43
asyncapis:
- description: Webhook event surface for the Mamo Business API. Merchants register a webhook URL via POST /webhooks with a set of enabled_events; Mamo POSTs a JSON event payload to that URL when the corresponding ev
  name: Mamo Business Webhooks
  slug: mamo-webhooks-asyncapi
collections:
- collection_type: postman
  name: Mamo Business Business Details API
  slug: postman-mamo-business-details-api
- collection_type: postman
  name: Mamo Business Business Details Cards API
  slug: postman-mamo-cards-api
- collection_type: postman
  name: Mamo Business Business Details Expenses API
  slug: postman-mamo-expenses-api
- collection_type: postman
  name: Mamo Business Business Details Getting Started API
  slug: postman-mamo-getting-started-api
- collection_type: postman
  name: Mamo Business Business Details Invoices API
  slug: postman-mamo-invoices-api
- collection_type: postman
  name: Mamo Business Business Details Payment Links API
  slug: postman-mamo-payment-links-api
- collection_type: postman
  name: Mamo Business Business Details Payouts API
  slug: postman-mamo-payouts-api
- collection_type: postman
  name: Mamo Business Business Details Receipts API
  slug: postman-mamo-receipts-api
- collection_type: postman
  name: Mamo Business Business Details Recipients API
  slug: postman-mamo-recipients-api
- collection_type: postman
  name: Mamo Business Business Details Subscriptions API
  slug: postman-mamo-subscriptions-api
- collection_type: postman
  name: Mamo Business Business Details Transactions API
  slug: postman-mamo-transactions-api
- collection_type: postman
  name: Mamo Business Business Details Webhooks API
  slug: postman-mamo-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mamo Business Business Details API
  slug: open-mamo-business-details-api
- collection_type: open
  name: Mamo Business Business Details Cards API
  slug: open-mamo-cards-api
- collection_type: open
  name: Mamo Business Business Details Expenses API
  slug: open-mamo-expenses-api
- collection_type: open
  name: Mamo Business Business Details Getting Started API
  slug: open-mamo-getting-started-api
- collection_type: open
  name: Mamo Business Business Details Invoices API
  slug: open-mamo-invoices-api
- collection_type: open
  name: Mamo Business Business Details Payment Links API
  slug: open-mamo-payment-links-api
- collection_type: open
  name: Mamo Business Business Details Payouts API
  slug: open-mamo-payouts-api
- collection_type: open
  name: Mamo Business Business Details Receipts API
  slug: open-mamo-receipts-api
- collection_type: open
  name: Mamo Business Business Details Recipients API
  slug: open-mamo-recipients-api
- collection_type: open
  name: Mamo Business Business Details Subscriptions API
  slug: open-mamo-subscriptions-api
- collection_type: open
  name: Mamo Business Business Details Transactions API
  slug: open-mamo-transactions-api
- collection_type: open
  name: Mamo Business Business Details Webhooks API
  slug: open-mamo-webhooks-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mamo-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mamo-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mamo/overview
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mamo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.mamopay.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mamo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mamopay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mamopay.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://mamopay.readme.io/reference/get_
- group: docs
  title: ''
  type: APIReference
  url: https://mamopay.readme.io/reference/get_
- group: start
  title: ''
  type: GettingStarted
  url: https://mamopay.readme.io/reference/get_
- group: auth
  title: ''
  type: Authentication
  url: https://mamopay.readme.io/reference/authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://mamopay.readme.io/reference/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://mamo.instatus.com/
- group: operate
  title: ''
  type: Support
  url: https://help.mamopay.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.mamopay.com/en/collections/7614470-developers
- group: company
  title: ''
  type: Blog
  url: https://mamopay.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://mamopay.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.mamopay.com/onboarding/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.mamopay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mamopay.com/legal/terms-business
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mamopay.com/legal/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mamo-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mamo-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mamo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mamo-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mamopay
- group: auth
  title: ''
  type: TrustCenter
  url: security/mamo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mamopay.com/security
created: '2026-07-17'
description: Mamo is a UAE-based fintech platform (Mamo Pay / Mamo Business) offering integrated payment solutions for businesses across the Gulf. Its products include hosted payment links and checkout, subscriptions and recurring billing, merchant-initiated charges with saved cards, refunds/captures/holds, invoicing, global payouts and disbursements to recipients, virtual and physical corporate cards with expense management, and partner cards for instant payouts. The Mamo Business API is a REST/JSON API hosted on readme.io that lets merchants automate payment link generation, charges, subscriptions, disbursements, recipients, card transactions, expenses, and webhooks. The platform serves 4,000+ businesses and has processed over AED 12 billion in total payment volume.
image: https://cdn.prod.website-files.com/62662ec945767b19355b5c00/695f9da901d5bfde3a81193b_Website%20thumbnail2.png
layout: provider
mcp_servers:
- description: ''
  name: mamo-mcp.yml
  slug: mamo-mcpyml
modified: '2026-07-20'
name: Mamo
nav: Providers
network: true
overview: 'Mamo publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Business Details API, Cards API, Expenses API, and 9 more. Tagged areas include Company, Payments, Fintech, Payment Links, and Subscriptions.


  The Mamo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mamo''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 23 more developer resources.'
random_paper: 6
score:
  band: strong
  composite: 57.6
  delta: -2.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 30.3
    contract_quality: 71.6
    developer_ergonomics: 45.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 21.1
  previous_composite: 59.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 67.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mamo/refs/heads/main/screenshots/mamo-2026-07-25T230010.png
security:
- kind: authentication
  name: Mamo Authentication
  slug: mamo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mamo Domain Security
  slug: mamo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mamo Vulnerability Disclosure
  slug: mamo-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Mamo Trust Center
  slug: mamo-trust-center
  summary_line: PCI DSS
slug: mamo
tags:
- Company
- Payments
- Fintech
- Payment Links
- Subscriptions
- Corporate Cards
- Payouts
- Expense Management
- UAE
- Middle East
website: https://mamopay.com
---
