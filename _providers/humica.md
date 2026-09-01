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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for the Employment Hero platform (behind humi.ca) — employees, organisations, payroll, leave, timesheets, rostering, documents, and webhooks. OAuth 2.0 authorization-code with PKCE; Bearer to
  name: Employment Hero API
  slug: employment-hero-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/humica-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://employmenthero.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://employmenthero.com/en-ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.employmenthero.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.employmenthero.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.employmenthero.com/api-references
- group: auth
  title: ''
  type: Authentication
  url: authentication/humica-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/humica-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/humica-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/humica-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.employmenthero.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/humica-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/humica-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/humica-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/humica-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: data-model/humica-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/humica-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/humica-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/humica-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://help.employmenthero.info/hc/en-ca/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.humi.ca/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://employmenthero.com/en-ca/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://employmenthero.com/en-ca/legals/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://employmenthero.com/en-ca/legals/privacy-policy/
created: '2026-07-17'
description: humi.ca is the Canadian HR, payroll, benefits, and hiring platform originally built as Humi and now operating as Employment Hero Canada (humi.ca redirects to employmenthero.com/en-ca). The platform is an all-in-one Employment Operating System covering HR management, payroll processing, applicant tracking (ATS), employee experience, learning, and Employer-of-Record hiring across 180+ countries. Employment Hero exposes a public REST API at api.employmenthero.com, secured with OAuth 2.0 authorization-code plus PKCE (mandatory from 2026-09-14), with documented resources spanning employees, organisations, payroll, leave, timesheets, rostering, documents, and webhooks, plus a partner integration marketplace (Xero, QuickBooks, Slack, Google Workspace, Microsoft 365, Square, Indeed, LinkedIn and more).
image: https://employmenthero.com/favicon.ico
layout: provider
mcp_servers:
- description: Candidate MCP server surface derived from the documented resource groups of the Employment Hero API (the platform behind humi.ca). No official hosted / remote MCP server was found. Tools below are a c
  name: humi.ca MCP Server
  slug: humica-mcp-server
modified: '2026-07-19'
name: humi.ca
nav: Providers
network: true
overview: 'humi.ca publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Payroll, HR Tech, and Benefits.


  humi.ca''s developer surface includes documentation, API reference, authentication, changelog, support, engineering blog, and 19 more developer resources.'
random_paper: 1
scopes:
- name: Humica Scopes
  scope_count: 2
  slug: humica-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 28.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humica/refs/heads/main/screenshots/humica-2026-07-25T221713.png
security:
- kind: authentication
  name: Humica Authentication
  slug: humica-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Humica Domain Security
  slug: humica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Humica Vulnerability Disclosure
  slug: humica-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: humica
tags:
- Company
- Human Resources
- Payroll
- HR Tech
- Benefits
- Applicant Tracking
- Employer of Record
- Canada
- Software-as-a-Service
website: https://employmenthero.com/en-ca/
---
