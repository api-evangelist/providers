---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 3
  name: Telr Agentic Access
  operation_count: 5
  slug: telr-agentic-access
  summary_line: 5 operations · 4 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: Marketplace / split-payment Service API for sub-merchant onboarding, multi-split payments, debit/credit of sub-merchant accounts, payouts, and transaction reconciliation. Authenticated with HTTP Basic
  name: Telr Accounts and Split Payments API
  slug: telr-accounts-split-payments-api
- description: Remote creation of QuickLink payment links and e-invoices with extra data fields, for merchants who collect payment without a full checkout integration.
  name: Telr QuickLink and E-Invoicing API
  slug: telr-quicklink-einvoicing-api
- description: EMV Secure Remote Commerce (Click to Pay) checkout, available as a seamless integration or through the remote JSON API for tokenized card-on-file payments.
  name: Telr Click to Pay (C2P) API
  slug: telr-click-to-pay-api
- description: Repeat billing / recurring agreement management.
  name: Telr Agreements API
  slug: telr-agreements-api
- description: Redirect-based hosted checkout (order.json).
  name: Telr Hosted Payment Page API
  slug: telr-hosted-payment-page-api
- description: Newer REST order API with HTTP Basic auth.
  name: Telr Payments API API
  slug: telr-payments-api-api
- description: Direct server-to-server card and wallet transactions (remote.json).
  name: Telr Remote API
  slug: telr-remote-api
artifact_total: 17
asyncapis:
- description: ''
  name: Telr Webhooks
  slug: telr-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/telr-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/telr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telr-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://telr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telr.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/telr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/telr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/telr-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telr
- group: company
  title: ''
  type: Blog
  url: https://telr.com/blog/
- group: build
  title: ''
  type: Packages
  url: packages/telr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/telr-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telr-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/telr-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/telr-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/telr-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://telr.com/secure
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telr-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/telr-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telr-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telr-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/telr-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/telr-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/telr-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: collections/telr.postman_collection.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Telr-PG
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.telr.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.telr.com/reference/get-started
- group: operate
  title: ''
  type: Support
  url: https://telr.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://telr.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://telr.com/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://telr.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://telr.com/privacy-policy/
created: '2026-07-17'
description: Telr is a Dubai-headquartered online payment gateway operating across the MENA region (UAE, Saudi Arabia, Bahrain, Jordan), supporting 120+ currencies and 30 languages. Its HTTPS/JSON gateway exposes a Hosted Payment Page, a Remote (direct) card and wallet API, repeat-billing agreements, mobile SDKs, and a newer REST Payments API - all PCI DSS v4.0 Level 1 and NESA certified.
finops:
- name: Telr Finops
  service_category: Financial Services
  slug: telr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telr.png
layout: provider
mcp_servers:
- description: ''
  name: telr-mcp.yml
  slug: telr-mcpyml
modified: '2026-07-18'
name: Telr
nav: Providers
network: true
overview: 'Telr publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agreements API, Hosted Payment Page API, Payments API API, and 1 more. Tagged areas include Payments, Payment Gateway, FinTech, MENA, and UAE.


  The Telr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Telr''s developer surface includes authentication, documentation, engineering blog, sandbox, getting-started guide, support, pricing, and 29 more developer resources.'
plans:
- name: Telr Plans Pricing
  plan_count: 7
  slug: telr-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 4
  name: Telr Rate Limits
  slug: telr-rate-limits
score:
  band: exemplar
  composite: 70.2
  delta: 0.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 69.0
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 70.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Telr Authentication
  slug: telr-authentication
  summary_line: http/custom · 2 schemes
- kind: domain-security
  name: Telr Domain Security
  slug: telr-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Telr Vulnerability Disclosure
  slug: telr-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Telr Trust Center
  slug: telr-trust-center
  summary_line: PCI DSS v4.0 Level 1, NESA, Central Bank of the UAE Retail Payment Services License, 3-D Secure, GDPR
slug: telr
tags:
- Payments
- Payment Gateway
- FinTech
- MENA
- UAE
website: https://telr.com/
---
