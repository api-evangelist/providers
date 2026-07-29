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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Retrieve credit decisions
  name: Funding Circle Decisions API
  slug: funding-circle-decisions-api
- description: Upload supporting documents
  name: Funding Circle Documents API
  slug: funding-circle-documents-api
- description: Create and manage business loan applications
  name: Funding Circle Loan Applications API
  slug: funding-circle-loan-applications-api
artifact_total: 7
asyncapis:
- description: ''
  name: Funding Circle Webhooks
  slug: funding-circle-webhooks
common:
- group: company
  title: ''
  type: Website
  url: http://www.fundingcircle.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fundingcircle.com/uk/partners/developer/api-doc/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fundingcircle.com/uk/partners/developer/api-doc/
- group: docs
  title: ''
  type: APIReference
  url: https://www.fundingcircle.com/uk/partners/developer/api-doc/
- group: operate
  title: ''
  type: Support
  url: https://www.fundingcircle.com/uk/support/
- group: start
  title: ''
  type: Login
  url: https://www.fundingcircle.com/uk/auth/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fundingcircle.com/uk/legal/platform-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fundingcircle.com/uk/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FundingCircle
- group: auth
  title: ''
  type: Authentication
  url: authentication/funding-circle-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/funding-circle-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/funding-circle-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/funding-circle-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/funding-circle-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/funding-circle-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/funding-circle-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/funding-circle-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/funding-circle-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/funding-circle-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/funding-circle-introducer-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/funding-circle-domain-security.yml
created: '2026-07-17'
description: 'Funding Circle is a UK small-business lending marketplace providing term business loans, the FlexiPay revolving line of credit, a cashback business credit card, government-backed Growth Guarantee Scheme loans, and asset finance. For partners and brokers it publishes the Funding Circle Introducer API, which lets platforms submit and manage business loan applications programmatically: create term or FlexiPay applications, poll application status, retrieve credit decisions, and upload supporting documents. The API uses OAuth 2.0 client-credentials authentication, RFC 7807 problem-detail errors, callback-URL webhooks, and a sandbox environment with documented test values.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/funding-circle.png
layout: provider
mcp_servers:
- description: ''
  name: funding-circle-mcp.yml
  slug: funding-circle-mcpyml
modified: '2026-07-19'
name: Funding Circle
nav: Providers
network: true
overview: 'Funding Circle publishes 3 APIs on the [APIs.io](https://apis.io/) network: Decisions API, Documents API, and Loan Applications API. Tagged areas include Company, Consumer, Lending, Small Business, and Fintech.


  The Funding Circle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Funding Circle''s developer surface includes documentation, API reference, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 41
score:
  band: developing
  composite: 45.9
  delta: -3.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 72.0
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 49.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Funding Circle Authentication
  slug: funding-circle-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Funding Circle Domain Security
  slug: funding-circle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: funding-circle
tags:
- Company
- Consumer
- Lending
- Small Business
- Fintech
- Loans
- Financial Services
- Payments
website: http://www.fundingcircle.com
---
