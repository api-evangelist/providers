---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'A REST/JSON API hosted on Azure API Management for pairing and driving takepayments card machines (Move5000, PAX A920 Pro) from an integrated app or POS. Documented operations include Authentication, '
  name: takepayments Terminal API
  slug: takepayments-terminal-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/takepayments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.takepayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.takepayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.takepayments.com/developer-support/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.takepayments.com/apis
- group: build
  title: ''
  type: SDK
  url: https://developer.takepayments.com/online-sdk
- group: build
  title: ''
  type: Plugins
  url: https://www.takepayments.com/developer-support/shopping-carts/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/takepayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/takepayments-limited/
- group: company
  title: ''
  type: Blog
  url: https://www.takepayments.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.takepayments.com/partner-support/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.takepayments.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.takepayments.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.takepayments.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.takepayments.com/card-machines/
- group: auth
  title: ''
  type: Authentication
  url: authentication/takepayments-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/takepayments-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/takepayments-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/takepayments-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/takepayments-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/takepayments-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/takepayments-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.takepayments.com/pci-compliance/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/takepayments-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/takepayments-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/takepayments-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/takepayments-llms.txt
created: '2026-07-24'
description: takepayments (a trading name of Payzone UK Limited) is a United Kingdom payment gateway and merchant-services provider that lets businesses accept card payments online, in person, and over the phone. Its online payment gateway offers Hosted (redirect) and Direct (server-to-server) integrations for e-commerce checkouts, delivered as SOAP v1.1 XML and HTTPS form-POST requests authenticated with a merchant ID and a pre-shared-key signature hash, alongside ready-made shopping-cart plugins and backend SDK code packs. Its newer Terminal API is a modern REST/JSON surface hosted on Azure API Management, secured with OAuth 2.0 client-credentials via Microsoft Azure AD, that pairs and drives card machines (Move5000, PAX A920 Pro) for Start-Transaction, Pairing, Split Bill & Gratuity, and Pay at Table flows. takepayments runs a real public developer portal at developer.takepayments.com but does not publish a downloadable OpenAPI/Swagger definition; its API reference is documentation-only,
  and merchant onboarding is sales-led rather than open self-serve.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: takepayments-mcp.yml
  slug: takepayments-mcpyml
modified: '2026-07-25'
name: takepayments
nav: Providers
network: true
overview: 'takepayments publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United Kingdom, Payment Gateway, Payment Processing, and Card Payments.


  takepayments'' developer surface includes documentation, API reference, SDKs, engineering blog, support, pricing, authentication, and 20 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 34.5
  delta: -1.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 35.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Takepayments Authentication
  slug: takepayments-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Takepayments Domain Security
  slug: takepayments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: takepayments
tags:
- Payments
- United Kingdom
- Payment Gateway
- Payment Processing
- Card Payments
- Card Machines
- In-Person Payments
- Ecommerce
- PSP
- Acquiring
website: https://www.takepayments.com/
---
