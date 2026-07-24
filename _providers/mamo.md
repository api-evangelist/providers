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
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 37.5
  scored_at: '2026-07-23'
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
artifact_total: 17
asyncapis:
- description: Webhook event surface for the Mamo Business API. Merchants register a webhook URL via POST /webhooks with a set of enabled_events; Mamo POSTs a JSON event payload to that URL when the corresponding ev
  name: Mamo Business Webhooks
  slug: mamo-webhooks-asyncapi
common:
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
modified: '2026-07-20'
name: Mamo
nav: Providers
network: true
overview: 'Mamo publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Business Details API, Cards API, Expenses API, and 9 more. Tagged areas include Company, Payments, Fintech, Payment Links, and Subscriptions.


  The Mamo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mamo''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 20 more developer resources.'
random_paper: 18
score:
  band: strong
  composite: 60.0
  delta: 1.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.8
    developer_ergonomics: 65.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 58.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 67.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
