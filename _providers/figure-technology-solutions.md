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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Figure Technology Solutions Agentic Access
  operation_count: 36
  slug: figure-technology-solutions-agentic-access
  summary_line: 36 operations · 15 acting
api_count: 8
apis:
- description: The Encryption API from Figure Technology Solutions — 1 operation(s) for encryption.
  name: Figure Technology Solutions Encryption API
  slug: figure-technology-solutions-encryption-api
- description: The HELOC application requests API from Figure Technology Solutions — 19 operation(s) for heloc application requests.
  name: Figure Technology Solutions HELOC application requests API
  slug: figure-technology-solutions-heloc-application-requests-api
- description: The HELOC Offers API from Figure Technology Solutions — 2 operation(s) for heloc offers.
  name: Figure Technology Solutions HELOC Offers API
  slug: figure-technology-solutions-heloc-offers-api
- description: The Loan Originator requests API from Figure Technology Solutions — 1 operation(s) for loan originator requests.
  name: Figure Technology Solutions Loan Originator requests API
  slug: figure-technology-solutions-loan-originator-requests-api
- description: The Loan Tape V1 API from Figure Technology Solutions — 6 operation(s) for loan tape v1.
  name: Figure Technology Solutions Loan Tape V1 API
  slug: figure-technology-solutions-loan-tape-v1-api
- description: The Loan Tape V2 API from Figure Technology Solutions — 3 operation(s) for loan tape v2.
  name: Figure Technology Solutions Loan Tape V2 API
  slug: figure-technology-solutions-loan-tape-v2-api
- description: The Payment History V1 API from Figure Technology Solutions — 3 operation(s) for payment history v1.
  name: Figure Technology Solutions Payment History V1 API
  slug: figure-technology-solutions-payment-history-v1-api
- description: The Payment History V2 API from Figure Technology Solutions — 1 operation(s) for payment history v2.
  name: Figure Technology Solutions Payment History V2 API
  slug: figure-technology-solutions-payment-history-v2-api
artifact_total: 13
asyncapis:
- description: ''
  name: Figure Technology Solutions Webhooks
  slug: figure-technology-solutions-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/figure-technology-solutions-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/figure-technology-solutions-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/figure-technology-solutions-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.figure.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.figure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.figure.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.figure.com/heloc-inquiries/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.figure.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.figure.com/partner/success-center/
- group: company
  title: ''
  type: Blog
  url: https://www.figure.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FigureTechnologies
- group: operate
  title: ''
  type: StatusPage
  url: https://status.figure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.figure.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.figure.com/privacy/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/figure-technology-solutions-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/figure-technology-solutions-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/figure-technology-solutions-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/figure-technology-solutions-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/figure-technology-solutions-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/figure-technology-solutions-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/figure-technology-solutions-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/figure-technology-solutions-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/figure-technology-solutions-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/figure-technology-solutions-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/figure-technology-solutions-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-technology-solutions-heloc-inquiries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-technology-solutions-heloc-pre-qualification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figure-technology-solutions-portfolio-manager-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/figure-technology-solutions-run-heloc-inquiry.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/figure-technology-solutions-prequalify-heloc.md
created: '2026-07-17'
description: 'Figure Technology Solutions is a Reno, Nevada financial-technology company (founded 2018) that builds and operates blockchain-based platforms for lending, capital markets, and asset management. Its public Partner APIs let integrators originate and manage Home Equity Line of Credit (HELOC) loans end to end: non-licensed pre-qualification and offer retrieval, full HELOC inquiry lifecycle management (start inquiry, select property, add income/SSN, verify liens, select offer, documents), loan-originator directory management, and Portfolio Manager reporting over owned and pledged loan pools. Figure also runs Figure Connect, a blockchain-based loan marketplace connecting loan sellers and buyers. The REST/JSON APIs authenticate with an apikey header and protect PII in transit with JWE encryption (RSA-OAEP-256 + A256GCM).'
image: https://docs.figure.com/img/docusaurus-social-card.jpg
layout: provider
mcp_servers:
- description: ''
  name: figure-technology-solutions-mcp.yml
  slug: figure-technology-solutions-mcpyml
modified: '2026-07-19'
name: Figure Technology Solutions
nav: Providers
network: true
overview: 'Figure Technology Solutions publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Encryption API, HELOC application requests API, HELOC Offers API, and 5 more. Tagged areas include Company, Fintech, Lending, HELOC, and Home Equity.


  The Figure Technology Solutions catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Figure Technology Solutions'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 23 more developer resources.'
random_paper: 40
score:
  band: developing
  composite: 46.5
  delta: -1.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.8
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/figure-technology-solutions/refs/heads/main/screenshots/figure-technology-solutions-2026-07-25T214442.png
security:
- kind: authentication
  name: Figure Technology Solutions Authentication
  slug: figure-technology-solutions-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Figure Technology Solutions Domain Security
  slug: figure-technology-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: figure-technology-solutions
tags:
- Company
- Fintech
- Lending
- HELOC
- Home Equity
- Mortgage
- Capital Markets
- Blockchain
- Loan Origination
- Financial Services
website: https://www.figure.com/
---
