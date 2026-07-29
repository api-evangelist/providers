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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for integrating Flywire's global payment network — one-off, recurring, pre-authorization, refund and 529 payments, checkout sessions, payors, recipients, and documents, with real-time payment
  name: Flywire Payments API
  slug: flywire-payments-api
artifact_total: 7
asyncapis:
- description: ''
  name: Flywire Payments Webhooks
  slug: flywire-payments-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/flywire-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.flywire.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.flywire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.flywire.com/education/Content/home.htm
- group: docs
  title: ''
  type: APIReference
  url: https://developers.flywire.com/education/Content/api-reference.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.flywire.com/education/Content/api-basics.htm
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flywire.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flywire.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flywire.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peertransfer
- group: auth
  title: ''
  type: Compliance
  url: https://www.flywire.com/company/security
- group: auth
  title: ''
  type: Security
  url: https://app.intigriti.com/programs/flywire/flywirevulnerabilitydiscloseprogram/
- group: build
  title: ''
  type: Packages
  url: packages/flywire-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flywire-packages.yml
- group: design
  title: ''
  type: Components
  url: components/flywire-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flywire-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flywire-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flywire-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flywire-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flywire-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flywire-payments-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flywire-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flywire-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flywire-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/flywire-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flywire-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flywire-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flywire-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flywire-llms.txt
created: '2026-07-17'
description: Flywire is a global payments enablement and software company that operates a proprietary cross-border payment network spanning more than 140 currencies and 240 countries and territories, serving the education, healthcare, travel, and business-to-business verticals. The Flywire Payments API is an HTTP-based REST API (JSON request/response bodies, API-Key authorization) that lets platforms integrate Flywire's payment network directly — creating and capturing one-off, recurring, pre-authorization, refund, and 529 payments, managing payors, recipients, checkout sessions and documents, and receiving real-time payment status callbacks (webhooks) signed with an HMAC-SHA256 shared secret. Flywire also ships client-side JavaScript and React libraries (Flywire Elements, Checkout, Pay-By-Link) for embedding hosted payment experiences.
image: https://www.flywire.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: flywire-mcp.yml
  slug: flywire-mcpyml
modified: '2026-07-19'
name: Flywire
nav: Providers
network: true
overview: 'Flywire publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, FinTech, and Education Payments.


  The Flywire catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flywire''s developer surface includes documentation, API reference, getting-started guide, sandbox, authentication, and 24 more developer resources.'
random_paper: 41
score:
  band: developing
  composite: 50.9
  delta: 4.4
  facets:
    commercial_clarity: 36.8
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 46.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flywire/refs/heads/main/screenshots/flywire-2026-07-25T214857.png
security:
- kind: authentication
  name: Flywire Authentication
  slug: flywire-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flywire Domain Security
  slug: flywire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flywire Vulnerability Disclosure
  slug: flywire-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Flywire Trust Center
  slug: flywire-trust-center
  summary_line: PCI DSS Level 1, SOC 2 Type II, ISO/IEC 27001:2013, GDPR
slug: flywire
tags:
- Company
- Payments
- Cross-Border Payments
- FinTech
- Education Payments
- Healthcare Payments
- Travel Payments
- B2B Payments
- Checkout
- Webhooks
website: https://www.flywire.com
---
