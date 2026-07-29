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
api_count: 1
apis:
- description: RESTful API v2 exposing Eightfold's core talent entities (profiles, positions, ATS positions/candidates, demands, bookings, offers, succession plans, courses, campaigns, messages, insights) plus a SCI
  name: Eightfold API v2
  slug: eightfold-api-v2
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eightfold-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/eightfold-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://eightfold.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.eightfold.ai
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.eightfold.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.eightfold.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.eightfold.ai/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://eightfold.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EightfoldAI
- group: start
  title: ''
  type: Login
  url: https://app.eightfold.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eightfold.ai/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://eightfold.ai/security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.eightfold.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.eightfold.ai/changelog/eightfold-api-release-notes
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eightfold-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/eightfold-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eightfold-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eightfold-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eightfold-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eightfold-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eightfold-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eightfold-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eightfold-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/eightfold-packages.yml
- group: design
  title: ''
  type: Components
  url: packages/eightfold-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eightfold-vulnerability-disclosure.yml
created: '2026-07-17'
description: Eightfold AI operates an agentic Talent Intelligence Platform that pairs an enterprise's own HR data with a deep-learning talent graph built from more than a billion career profiles to power talent acquisition, talent management, internal mobility, workforce and resource planning, succession planning, and AI-assisted interviewing. Eightfold exposes these capabilities to customers and certified ATS/HRIS/LMS partners through a RESTful API v2 (apiv2.eightfold.ai) and a SCIM 2.0 provisioning API, covering profiles, positions, ATS positions and candidates, demands, bookings, offers, succession plans, courses, campaigns, messaging, and org-wide diversity insights. Authentication is OAuth 2.0 (password grant) fronted by Basic-auth API-key credentials, with fine-grained READ/WRITE permission scopes assigned per API key and regional token endpoints for US/EU/CA/ME/AP/WU/Gov deployments.
image: https://logo.clearbit.com/eightfold.ai
layout: provider
mcp_servers:
- description: ''
  name: eightfold-mcp.yml
  slug: eightfold-mcpyml
modified: '2026-07-19'
name: Eightfold
nav: Providers
network: true
overview: 'Eightfold publishes 1 API on the [APIs.io](https://apis.io/) network: API v2. Tagged areas include Company, Talent Intelligence, Talent Acquisition, Talent Management, and Recruiting.


  Eightfold''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, and 21 more developer resources.'
random_paper: 26
scopes:
- name: Eightfold Scopes
  scope_count: 0
  slug: eightfold-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 40.6
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 51.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 43.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eightfold/refs/heads/main/screenshots/eightfold-2026-07-25T213004.png
security:
- kind: authentication
  name: Eightfold Authentication
  slug: eightfold-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Eightfold Domain Security
  slug: eightfold-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eightfold Vulnerability Disclosure
  slug: eightfold-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Eightfold Trust Center
  slug: eightfold-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO 27001, ISO 27701, ISO 27017, ISO 42001, FedRAMP Moderate
slug: eightfold
tags:
- Company
- Talent Intelligence
- Talent Acquisition
- Talent Management
- Recruiting
- Human Resources
- Workforce Planning
- HRIS
- ATS
- Artificial Intelligence
- SCIM
- REST
website: https://eightfold.ai
---
