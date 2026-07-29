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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Payment gateway API for accepting credit card and eCheck.Net payments, storing customer payment profiles (CIM), recurring billing (ARB), hosted/tokenized card capture (Accept.js / Accept Hosted), tran
  name: Authorize.net API
  slug: authorizenet-api
artifact_total: 5
asyncapis:
- description: ''
  name: Authorizenet Webhooks
  slug: authorizenet-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authorizenet-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.authorize.net/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.authorize.net/api/reference/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.authorize.net/api/reference/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.authorize.net/hello_world.html
- group: operate
  title: ''
  type: Support
  url: https://developer.authorize.net/support.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AuthorizeNet
- group: company
  title: ''
  type: Website
  url: https://www.authorize.net/
- group: start
  title: ''
  type: SignUp
  url: https://www.authorize.net/sign-up.html
- group: start
  title: ''
  type: Login
  url: https://account.authorize.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.authorize.net/sign-up/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.authorize.net/about-us/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.authorize.net/about-us/privacy.html
- group: build
  title: ''
  type: Postman
  url: https://github.com/AuthorizeNet/webhooks-postman-collection
- group: operate
  title: ''
  type: StatusPage
  url: https://status.authorize.net/
- group: build
  title: ''
  type: Packages
  url: packages/authorizenet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/authorizenet-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/authorizenet-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/authorizenet-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/authorizenet-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/authorizenet-webhooks.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/authorizenet-decline-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/authorizenet-decline-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/authorizenet-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/authorizenet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/authorizenet-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/authorizenet-conventions.yml
created: '2026-07-17'
description: Authorize.net is a payment gateway operated by Visa (Visa Acceptance Solutions) that lets merchants and platforms accept credit card and eCheck.Net payments online, in person, and through mobile apps. Its developer platform exposes a transaction API (the XML/JSON gateway at /xml/v1 and a REST surface at /rest/v1) for one-time and recurring payments, the Customer Information Manager (CIM) for stored payment profiles, Accept.js and Accept Hosted for tokenized/hosted card capture, Automated Recurring Billing (ARB), transaction reporting, fraud detection (Advanced Fraud Detection Suite), and webhooks for asynchronous event notifications. Official server SDKs ship for PHP, .NET, Java, Python, Node.js, and Ruby, plus Accept mobile SDKs for iOS and Android. Authentication uses merchant API Login ID + Transaction Key, with OAuth 2.0 available for partner/Accept integrations. Added to the API Evangelist network from an Insight Partners portfolio lead and enriched from Authorize.net's
  public developer surface.
image: https://www.authorize.net/content/dam/authorize/images/logos/anet-logo.png
layout: provider
mcp_servers:
- description: ''
  name: authorizenet-mcp.yml
  slug: authorizenet-mcpyml
modified: '2026-07-18'
name: Authorize.net
nav: Providers
network: true
overview: 'Authorize.net publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Gateway, Credit Cards, and eCommerce.


  The Authorize.net catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Authorize.net''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, sandbox, and 20 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 48.4
  delta: 3.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 69.6
    discoverability: 79.6
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 44.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authorizenet/refs/heads/main/screenshots/authorizenet-2026-07-25T201810.png
security:
- kind: authentication
  name: Authorizenet Authentication
  slug: authorizenet-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Authorizenet Domain Security
  slug: authorizenet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: authorizenet
tags:
- Company
- Payments
- Payment Gateway
- Credit Cards
- eCommerce
- Recurring Billing
- Fraud Detection
- Webhooks
- Financial Services
website: https://www.authorize.net/
---
