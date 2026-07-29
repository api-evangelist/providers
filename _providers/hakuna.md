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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Hakuna Agentic Access
  operation_count: 33
  slug: hakuna-agentic-access
  summary_line: 33 operations · 15 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Absence records and absence categories
  name: Hakuna Absences API
  slug: hakuna-absences-api
- description: Account-wide settings
  name: Hakuna Company API
  slug: hakuna-company-api
- description: Admin-only management of projects, clients and tasks
  name: Hakuna Management API
  slug: hakuna-management-api
- description: Organization-wide presence and absence status
  name: Hakuna Organization API
  slug: hakuna-organization-api
- description: Aggregate metrics for the authenticated user
  name: Hakuna Overview API
  slug: hakuna-overview-api
- description: Active and archived projects
  name: Hakuna Projects API
  slug: hakuna-projects-api
- description: Categorization tasks
  name: Hakuna Tasks API
  slug: hakuna-tasks-api
- description: Recorded blocks of worked time
  name: Hakuna Time Entries API
  slug: hakuna-time-entries-api
- description: The single running timer for the authenticated user
  name: Hakuna Timer API
  slug: hakuna-timer-api
- description: Users of the account
  name: Hakuna Users API
  slug: hakuna-users-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hakuna-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hakuna-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/hakuna-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hakuna-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hakuna-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hakuna-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hakuna-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hakuna-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hakuna-rate-limits.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hakuna-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hakuna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hakuna-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.hakuna.ch/api_docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.hakuna.ch/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.hakuna.ch/api_docs
- group: start
  title: ''
  type: SignUp
  url: https://app.hakuna.ch/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.hakuna.ch/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hakuna.ch/preise
- group: operate
  title: ''
  type: Support
  url: https://www.hakuna.ch/kontakt
- group: company
  title: ''
  type: Blog
  url: https://www.hakuna.ch/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hakuna.ch/rechtliches/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hakuna.ch/rechtliches/datenschutz
- group: company
  title: ''
  type: Website
  url: https://www.hakuna.ch
created: '2026-07-17'
description: 'hakuna AG is a Swiss digital time-tracking and personnel-management platform for SMEs. The browser- and mobile-based product centralizes workforce administration: time recording with a running timer, absence and vacation management, expense processing, project and client tracking, task categorization, shift planning, personnel records, and compliance monitoring against Swiss labor-law requirements. hakuna is "100% Swiss" — all data is stored in Switzerland under Swiss data-protection law (DSG) — and requires no additional hardware terminals or badges. It exposes a token-authenticated REST API (X-Auth-Token) over JSON at app.hakuna.ch/api/v1 covering the timer, time entries, absences, projects, tasks, clients, users, company settings, and an organization-wide presence status endpoint, with admin-only management endpoints and a documented 100 requests/minute rate limit.'
image: https://www.hakuna.ch/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: hakuna-mcp.yml
  slug: hakuna-mcpyml
modified: '2026-07-19'
name: Hakuna
nav: Providers
network: true
overview: 'Hakuna publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Company API, Management API, and 7 more. Tagged areas include Company, Time Tracking, HR, Workforce Management, and Absence Management.


  Hakuna''s developer surface includes authentication, documentation, API reference, signup flow, pricing, support, engineering blog, and 17 more developer resources.'
random_paper: 65
rate_limits:
- limit_count: 1
  name: Hakuna Rate Limits
  slug: hakuna-rate-limits
score:
  band: developing
  composite: 46.0
  delta: -1.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.6
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hakuna/refs/heads/main/screenshots/hakuna-2026-07-25T220533.png
security:
- kind: authentication
  name: Hakuna Authentication
  slug: hakuna-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hakuna Domain Security
  slug: hakuna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hakuna
tags:
- Company
- Time Tracking
- HR
- Workforce Management
- Absence Management
- Project Tracking
- SaaS
- Switzerland
- SME
website: https://www.hakuna.ch
---
