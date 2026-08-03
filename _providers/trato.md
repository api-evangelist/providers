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
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Create, configure, send, sign and manage contracts.
  name: Trato Contracts API
  slug: trato-contracts-api
- description: Attach custom metadata properties to a contract.
  name: Trato Custom Properties API
  slug: trato-custom-properties-api
- description: Manage participants (signers) on a contract.
  name: Trato Participants API
  slug: trato-participants-api
- description: Manage read-only observers of a contract.
  name: Trato Spectators API
  slug: trato-spectators-api
- description: List reusable contract templates.
  name: Trato Templates API
  slug: trato-templates-api
artifact_total: 9
asyncapis:
- description: TRATO delivers contract and milestone lifecycle events to subscriber URLs as HTTP POST callbacks. Webhooks are configured in the user profile per event type. Each request carries an `X-Trato-Secret` h
  name: TRATO Webhooks
  slug: trato-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://trato.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.trato.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.trato.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.trato.io/contracts
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.trato.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.trato.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trato.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contratosapp
- group: operate
  title: ''
  type: Support
  url: https://trato.io/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://trato.io/#pricing
- group: start
  title: ''
  type: Login
  url: https://clm.trato.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trato.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trato.io/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tratolegaltech/
- group: auth
  title: ''
  type: Authentication
  url: authentication/trato-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trato-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/trato-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trato-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/trato-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trato-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trato-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trato-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trato-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trato-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trato-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trato-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trato-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/trato-openapi-overlay.yaml
created: '2026-07-17'
description: TRATO is an AI-powered Contract Lifecycle Management (CLM) and electronic signature platform used by more than 180,000 users to centralize, draft, approve, sign and track contracts. It offers template-based smart drafting, automated approval routing, real-time contract tracking, and secure e-signatures, with multi-jurisdiction legal expertise across Mexico, Spain and Germany and support for Mexican NOM-151 advanced electronic signatures. TRATO exposes a JWT-authenticated REST API (Contracts, Templates, Milestones) and webhook events for programmatic contract generation and integration with CRM, document management and payment systems. Founded in 2014 in Mexico City and backed by 500 Global.
image: https://trato.io
layout: provider
mcp_servers:
- description: ''
  name: trato-mcp.yml
  slug: trato-mcpyml
modified: '2026-07-21'
name: Trato
nav: Providers
network: true
overview: 'Trato publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contracts API, Custom Properties API, Participants API, and 2 more. Tagged areas include Company, Contract Management, Contract Lifecycle Management, Electronic Signature, and Legaltech.


  The Trato catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trato''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 22 more developer resources.'
random_paper: 79
score:
  band: developing
  composite: 52.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 65.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 52.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Trato Authentication
  slug: trato-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trato Domain Security
  slug: trato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trato
tags:
- Company
- Contract Management
- Contract Lifecycle Management
- Electronic Signature
- Legaltech
- Document Management
- Workflow Automation
- Legal
website: https://trato.io
---
