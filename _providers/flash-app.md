---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The Integration API from Flash App — 1 operation(s) for integration.
  name: Flash App Integration API
  slug: flash-app-integration-api
- description: The Login API from Flash App — 1 operation(s) for login.
  name: Flash App Login API
  slug: flash-app-login-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flash-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flashapp.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://flashapp.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://flashapp.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://flashapp.readme.io/reference/getting-started-with-your-api-1
- group: start
  title: ''
  type: GettingStarted
  url: https://flashapp.readme.io/reference/getting-started-with-your-api
- group: operate
  title: ''
  type: Support
  url: https://faq.flashapp.com.br/kb/pt-BR
- group: operate
  title: ''
  type: HelpCenter
  url: https://faq.flashapp.com.br/kb/pt-BR
- group: company
  title: ''
  type: Blog
  url: https://flashapp.com.br/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flash-tecnologia
- group: commercial
  title: ''
  type: Pricing
  url: https://flashapp.com.br/planos
- group: start
  title: ''
  type: SignUp
  url: https://flashapp.com.br/contato
- group: start
  title: ''
  type: Login
  url: https://app.expenseon.com/admin/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flashapp.com.br/lgpd
- group: auth
  title: ''
  type: Compliance
  url: https://flashapp.com.br/etica-compliance-pld
- group: auth
  title: ''
  type: Security
  url: https://flashapp.com.br/hubfs/Pol%C3%ADtica%20de%20Seguran%C3%A7a%20da%20Informa%C3%A7%C3%A3o%20e%20Cibern%C3%A9tica%20-%20V2.0%20(Uso%20P%C3%BAblico).pdf
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flash-app-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flash-app-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flash-app-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flash-app-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flash-app-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flash-app-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flash-app-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flash-app-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flash-app-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flash-app-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flash-app-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Flash (Flash Tecnologia) is a Sao Paulo based Brazilian HR and financial management platform that centralizes three surfaces on one account: multi-benefits (the Flash prepaid benefits card and PAT-compliant meal, food, mobility and wellness balances), people management (admissions and offboarding, time and attendance, recruiting, performance and engagement, extended by its FolhaCerta acquisition), and corporate expense management (corporate cards, receipt capture and reimbursement, from its 2022 ExpenseON acquisition). Founded by Ricardo Salem, Pedro Lane and Guilherme Lane, it launched in 2019 and reports more than 60,000 client companies, 1.5 million users and over R$10 billion in processed transactions. Its public developer surface is small: a ReadMe-hosted API reference covering the Flash Expense integration API (login and user provisioning against the expenseon.com hosts), with the Flash Beneficios reference still an unfilled template.'
image: https://flashapp.com.br/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: flash-app-mcp.yml
  slug: flash-app-mcpyml
modified: '2026-07-20'
name: Flash App
nav: Providers
network: true
overview: 'Flash App publishes 2 APIs on the [APIs.io](https://apis.io/) network: Integration API and Login API. Tagged areas include Company, Human Resources, Employee Benefits, Expense Management, and Payments.


  Flash App''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 80
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 57.4
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 48.1
  provenance:
    conformance: derived
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
    score: 40.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flash-app/refs/heads/main/screenshots/flash-app-2026-07-25T214715.png
security:
- kind: authentication
  name: Flash App Authentication
  slug: flash-app-authentication
  summary_line: credential-login · 1 scheme
- kind: domain-security
  name: Flash App Domain Security
  slug: flash-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flash-app
tags:
- Company
- Human Resources
- Employee Benefits
- Expense Management
- Payments
- Corporate Cards
- Payroll
- Fintech
- Brazil
- HR Tech
website: https://flashapp.com.br/
---
