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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Payrails' REST API for payment orchestration — executions and payment actions (authorize, confirm, capture, cancel, refund, payout), instruments and tokens, the PCI vault, providers and workflow confi
  name: Payrails API
  slug: payrails-api
artifact_total: 7
asyncapis:
- description: ''
  name: Payrails Notifications Webhooks
  slug: payrails-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.payrails.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.payrails.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.payrails.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.payrails.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.payrails.com/docs/set-up-your-payrails-account-and-environment
- group: company
  title: ''
  type: Blog
  url: https://www.payrails.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.payrails.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payrails
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.payrails.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.payrails.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payrails.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/payrails-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/payrails-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/payrails-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/payrails-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/payrails-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payrails-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.payrails.com/docs/v6-migration-guide
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.payrails.com/docs/v6-migration-guide
- group: start
  title: ''
  type: Sandbox
  url: sandbox/payrails-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/payrails-notifications-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/payrails-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/payrails-packages.yml
- group: design
  title: ''
  type: Components
  url: components/payrails-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/payrails-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/payrails-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payrails-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.payrails.com/security
- group: agent
  title: ''
  type: WellKnown
  url: well-known/payrails-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payrails-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/payrails-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.payrails.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/payrails-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payrails-llms.txt
created: '2026-07-17'
description: Payrails is a modular payment and financial infrastructure platform — "the operating system for profitable growth" — that gives merchants unified control over payments, tokenization, and financial data. Its API and SDKs orchestrate payments across many payment service providers (Adyen, Stripe, Checkout.com, Braintree, Klarna, and 100+ local methods), with a PCI-certified token vault, network tokenization, 3D Secure, a no-code Workflow Studio for routing and decisioning, automated reconciliation, chargeback/dispute management, fraud screening, and unified analytics. Authentication is OAuth 2.0 client-credentials (plus optional mTLS); events are delivered as HMAC-signed webhooks. Used by Eneba, PUMA, Vinted, Preply, inDrive, Just Eat, and Careem.
image: https://www.payrails.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: payrails-mcp.yml
  slug: payrails-mcpyml
modified: '2026-07-20'
name: Payrails
nav: Providers
network: true
overview: 'Payrails publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Orchestration, Fintech, and Tokenization.


  The Payrails catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Payrails'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 28 more developer resources.'
random_paper: 57
score:
  band: strong
  composite: 56.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 63.2
  previous_composite: 56.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 78.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payrails/refs/heads/main/screenshots/payrails-2026-08-07T191653.png
security:
- kind: authentication
  name: Payrails Authentication
  slug: payrails-authentication
  summary_line: oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Payrails Domain Security
  slug: payrails-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Payrails Vulnerability Disclosure
  slug: payrails-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Payrails Trust Center
  slug: payrails-trust-center
  summary_line: PCI DSS, GDPR
slug: payrails
tags:
- Company
- Payments
- Payment Orchestration
- Fintech
- Tokenization
- Fraud
- Disputes
- Reconciliation
- Checkout
- Financial Infrastructure
website: https://www.payrails.com/
---
