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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-07-28'
api_count: 27
apis:
- description: The Attachments API from COR — 1 operation(s) for attachments.
  name: COR Attachments API
  slug: cor-attachments-api
- description: The Auth API from COR — 5 operation(s) for auth.
  name: COR Auth API
  slug: cor-auth-api
- description: The Brands API from COR — 2 operation(s) for brands.
  name: COR Brands API
  slug: cor-brands-api
- description: The Clients API from COR — 4 operation(s) for clients.
  name: COR Clients API
  slug: cor-clients-api
- description: The Collaborators API from COR — 2 operation(s) for collaborators.
  name: COR Collaborators API
  slug: cor-collaborators-api
- description: The Contacts API from COR — 3 operation(s) for contacts.
  name: COR Contacts API
  slug: cor-contacts-api
- description: The Contract Positions API from COR — 2 operation(s) for contract positions.
  name: COR Contract Positions API
  slug: cor-contract-positions-api
- description: The Contracts API from COR — 2 operation(s) for contracts.
  name: COR Contracts API
  slug: cor-contracts-api
- description: The Contracts Users API from COR — 1 operation(s) for contracts users.
  name: COR Contracts Users API
  slug: cor-contracts-users-api
- description: The Costs API from COR — 2 operation(s) for costs.
  name: COR Costs API
  slug: cor-costs-api
- description: The Estimates API from COR — 2 operation(s) for estimates.
  name: COR Estimates API
  slug: cor-estimates-api
- description: The Fees API from COR — 4 operation(s) for fees.
  name: COR Fees API
  slug: cor-fees-api
- description: The Hours API from COR — 6 operation(s) for hours.
  name: COR Hours API
  slug: cor-hours-api
- description: The Labels API from COR — 2 operation(s) for labels.
  name: COR Labels API
  slug: cor-labels-api
- description: The Messages API from COR — 2 operation(s) for messages.
  name: COR Messages API
  slug: cor-messages-api
- description: The Products API from COR — 2 operation(s) for products.
  name: COR Products API
  slug: cor-products-api
- description: The Project Templates API from COR — 1 operation(s) for project templates.
  name: COR Project Templates API
  slug: cor-project-templates-api
- description: The Projects API from COR — 14 operation(s) for projects.
  name: COR Projects API
  slug: cor-projects-api
- description: The Ratecards API from COR — 3 operation(s) for ratecards.
  name: COR Ratecards API
  slug: cor-ratecards-api
- description: The Resource Allocation API from COR — 4 operation(s) for resource allocation.
  name: COR Resource Allocation API
  slug: cor-resource-allocation-api
- description: The Tasks API from COR — 8 operation(s) for tasks.
  name: COR Tasks API
  slug: cor-tasks-api
- description: The Teams API from COR — 3 operation(s) for teams.
  name: COR Teams API
  slug: cor-teams-api
- description: The Transactions API from COR — 6 operation(s) for transactions.
  name: COR Transactions API
  slug: cor-transactions-api
- description: The User Leaves API from COR — 4 operation(s) for user leaves.
  name: COR User Leaves API
  slug: cor-user-leaves-api
- description: The User Positions API from COR — 4 operation(s) for user positions.
  name: COR User Positions API
  slug: cor-user-positions-api
- description: The Users API from COR — 4 operation(s) for users.
  name: COR Users API
  slug: cor-users-api
- description: The Working Time API from COR — 2 operation(s) for working time.
  name: COR Working Time API
  slug: cor-working-time-api
artifact_total: 30
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cor-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cor-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cor-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cor-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cor-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cor-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cor-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cor-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.projectcor.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.projectcor.com/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.projectcor.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.projectcor.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://projectcor.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://projectcor.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://cor.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://projectcor.com/cor-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://projectcor.com/cor-privacy-and-personal-data/
- group: start
  title: ''
  type: SignUp
  url: https://www.projectcor.com
- group: company
  title: ''
  type: Website
  url: https://projectcor.com
created: '2026-07-17'
description: COR (COR Global Ltd., projectcor.com) is an AI-powered management platform for advertising and creative agencies that calculates and forecasts project profitability while managing finances, resources, projects, tasks, and time tracking in one real-time workspace. COR publishes a REST API (JSON or XML) for projects, tasks, hours, clients, contracts, transactions, teams, users, and more, a separate Resource Allocation API, and an official hosted MCP server so AI clients can operate a workspace with natural language. Backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cor.png
layout: provider
mcp_servers:
- description: ''
  name: cor-mcp.yml
  slug: cor-mcpyml
modified: '2026-07-18'
name: COR
nav: Providers
network: true
overview: 'COR publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Auth API, Brands API, and 24 more. Tagged areas include Company, Agency Management, Project Management, Time Tracking, and Profitability.


  COR''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 15 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.5
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 45.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cor/refs/heads/main/screenshots/cor-2026-07-25T210412.png
security:
- kind: authentication
  name: Cor Authentication
  slug: cor-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cor Domain Security
  slug: cor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cor
tags:
- Company
- Agency Management
- Project Management
- Time Tracking
- Profitability
- Resource Allocation
- Professional Services
- MCP
website: https://projectcor.com
---
