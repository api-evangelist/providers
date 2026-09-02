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
    agentic_commerce: false
    auth_clarity: negotiable
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
  score: 26.4
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 11
asyncapis:
- description: ''
  name: Funding Circle Webhooks
  slug: funding-circle-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Funding Circle Introducer Decisions API
  slug: open-funding-circle-decisions-api
- collection_type: open
  name: Funding Circle Introducer Decisions Documents API
  slug: open-funding-circle-documents-api
- collection_type: open
  name: Funding Circle Introducer Decisions Loan Applications API
  slug: open-funding-circle-loan-applications-api
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
  name: Funding Circle MCP Server
  slug: funding-circle-mcp-server
modified: '2026-07-19'
name: Funding Circle
nav: Providers
network: true
overview: 'Funding Circle publishes 3 APIs on the [APIs.io](https://apis.io/) network: Decisions API, Documents API, and Loan Applications API. Tagged areas include Company, Consumer, Lending, Small Business, and Fintech.


  The Funding Circle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Funding Circle''s developer surface includes documentation, API reference, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 21.6
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 31.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/funding-circle/refs/heads/main/screenshots/funding-circle-2026-08-17T123438.png
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
- Financial-Services
- Payments
website: http://www.fundingcircle.com
---
