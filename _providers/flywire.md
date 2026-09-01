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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-01'
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
- group: company
  title: ''
  type: Blog
  url: https://www.flywire.com/company/news
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
  name: Flywire MCP Server
  slug: flywire-mcp-server
modified: '2026-07-19'
name: Flywire
nav: Providers
network: true
overview: 'Flywire publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Fintech, and Education Payments.


  The Flywire catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flywire''s developer surface includes engineering blog, documentation, API reference, getting-started guide, sandbox, authentication, and 24 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 48.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Fintech
- Education Payments
- Healthcare Payments
- Travel Payments
- B2B Payments
- Checkout
- Webhook
website: https://www.flywire.com
---
