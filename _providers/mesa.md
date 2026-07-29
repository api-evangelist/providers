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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Exchange API keys for a session token.
  name: Mesa Authentication API
  slug: mesa-authentication-api
- description: Retrieve invoices for the authenticated user.
  name: Mesa Invoices API
  slug: mesa-invoices-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.joinmesa.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partners.joinmesa.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinmesa.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joinmesa.com/partner-api/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinmesa.com/embedded-ui/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/mesa-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://partners.joinmesa.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@joinmesa.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinmesa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinmesa.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.joinmesa.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.joinmesa.com
- group: design
  title: ''
  type: Conventions
  url: conventions/mesa-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/mesa-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mesa-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mesa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mesa-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mesa-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mesa-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mesa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mesa-domain-security.yml
created: '2026-07-17'
description: Mesa is a Boulder, Colorado fintech that provides embedded electronic-invoicing, payments, and invoice-financing (early-payment) infrastructure for B2B supplier networks. Suppliers get paid early via ACH while Mesa automates repayment once the buyer settles. Mesa ships as drop-in embedded UI — a JavaScript SDK (MesaClient) that renders Mesa's onboarding, dashboard, and instant-payout flows in an origin-pinned iframe inside a partner's web app — backed by a Partner REST API for user authentication and invoice retrieval. Auth is via API keys (clientId/clientSecret) exchanged for a short-lived JWT, with optional OIDC (Okta, Azure AD, Google). Backed by Matrix Partners; SOC 2.
image: https://www.joinmesa.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: mesa-mcp.yml
  slug: mesa-mcpyml
modified: '2026-07-20'
name: Mesa
nav: Providers
network: true
overview: 'Mesa publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Invoices API. Tagged areas include Company, Fintech, Payments, Invoice Financing, and Embedded Finance.


  Mesa''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, and 16 more developer resources.'
random_paper: 37
score:
  band: developing
  composite: 45.7
  delta: -3.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.6
    developer_ergonomics: 53.8
    discoverability: 70.4
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 49.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Mesa Authentication
  slug: mesa-authentication
  summary_line: apiKey/http/openIdConnect · 3 schemes
- kind: domain-security
  name: Mesa Domain Security
  slug: mesa-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Mesa Trust Center
  slug: mesa-trust-center
  summary_line: SOC 2
slug: mesa
tags:
- Company
- Fintech
- Payments
- Invoice Financing
- Embedded Finance
- Early Payment
- ACH
- Supplier Payments
- B2B
website: https://www.joinmesa.com
---
