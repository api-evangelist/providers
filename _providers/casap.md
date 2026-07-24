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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Casap Agentic Access
  operation_count: 6
  slug: casap-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- description: The Auth API from Casap — 1 operation(s) for auth.
  name: Casap Auth API
  slug: casap-auth-api
- description: The Disputes API from Casap — 4 operation(s) for disputes.
  name: Casap Disputes API
  slug: casap-disputes-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/casap-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/casap-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/casap-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/casap-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/casap-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/casap-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/casap-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/casap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/casap-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/casap-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/casap-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/casap-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.casaphq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.casaphq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.casaphq.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.casaphq.com/casap-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.casaphq.com
- group: operate
  title: ''
  type: Support
  url: https://www.casaphq.com/get-in-touch
- group: company
  title: ''
  type: Blog
  url: https://www.casaphq.com/news
- group: operate
  title: ''
  type: StatusPage
  url: https://www.casaphq.com/status
- group: start
  title: ''
  type: Login
  url: https://disputes.casaphq.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.casaphq.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.casaphq.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.casaphq.com
created: '2026-07-17'
description: Casap is an award-winning agentic-AI dispute automation platform for banks, credit unions, and fintechs. It automates payment dispute (chargeback) intake, investigation, and resolution end to end, reducing operational cost and manual work while improving regulatory compliance and consumer satisfaction. The Casap REST API lets financial institutions programmatically create disputes, check dispute status, upload evidence files, and reopen disputes, backed by a hosted disputes dashboard, PCI-DSS and SOC 2 (AICPA) controls, and integrations with card networks (Visa, Mastercard) and core banking systems (Symitar/Jack Henry, STAR). Casap won Best of Show at FinovateFall 2025.
image: https://cdn.prod.website-files.com/6670a4d559962296d4e052c9/669eb1e52506764a3f5fbef6_Casap%20Website%20Group%2018.webp
layout: provider
mcp_servers:
- description: ''
  name: casap-mcp.yml
  slug: casap-mcpyml
modified: '2026-07-18'
name: Casap
nav: Providers
network: true
overview: 'Casap publishes 2 APIs on the [APIs.io](https://apis.io/) network: Auth API and Disputes API. Tagged areas include Company, Fintech, Disputes, Chargebacks, and Fraud.


  Casap''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 48.2
  delta: 3.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 47.8
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 45.2
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Casap Authentication
  slug: casap-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Casap Domain Security
  slug: casap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: casap
tags:
- Company
- Fintech
- Disputes
- Chargebacks
- Fraud
- Payments
- Banking
- Dispute Resolution
- Agentic AI
website: https://www.casaphq.com
---
