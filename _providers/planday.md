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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Planday's REST API secured by OAuth2 bearer tokens, separated into domains (HR, Absence, Pay, Payroll, Portal, Punchclock, Reports, Revenue, Schedule, Contract Rules, Security Group Membership). Reque
  name: Planday API
  slug: planday-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planday-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openapi.planday.com/
- group: docs
  title: ''
  type: Documentation
  url: https://openapi.planday.com/gettingstarted/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.planday.com/api/absence/
- group: start
  title: ''
  type: GettingStarted
  url: https://openapi.planday.com/gettingstarted/overview/
- group: operate
  title: ''
  type: Support
  url: https://help.planday.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.planday.com/
- group: company
  title: ''
  type: Blog
  url: https://www.planday.com/resources/articles/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.planday.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.planday.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://signup.planday.com/
- group: start
  title: ''
  type: Login
  url: https://id.planday.com/findCompanyUrl
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.planday.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.planday.com/legal/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/planday-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/planday-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/planday-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/planday-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.planday.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/planday-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/planday-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/planday-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/planday-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/planday-llms.txt
created: '2026-07-17'
description: Planday is a workforce management platform for shift-based businesses in hospitality, retail, healthcare, hotels, entertainment, and fitness, offering employee scheduling, time tracking and punch clock, absence and leave management, payroll reporting, staff communication, and HR. Planday (part of Xero) publishes a public REST/OAuth2 developer API at openapi.planday.com, organized into domains such as HR, Absence, Pay, Payroll, Portal, Punchclock, Reports, Revenue, Schedule, Contract Rules, and Security Group Membership, so partners and customers can sync employees, shifts, timesheets, pay rates, and cost data with external systems.
image: https://www.planday.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Planday
nav: Providers
network: true
overview: 'Planday publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Workforce Management, Scheduling, and Time Tracking.


  Planday''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 10
scopes:
- name: Planday Scopes
  scope_count: 78
  slug: planday-scopes
  summary_line: 78 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 33.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/planday/refs/heads/main/screenshots/planday-2026-09-02T151402.png
security:
- kind: authentication
  name: Planday Authentication
  slug: planday-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Planday Domain Security
  slug: planday-domain-security
  summary_line: TLSv1.3 · DMARC
slug: planday
tags:
- Company
- Software-as-a-Service
- Workforce Management
- Scheduling
- Time Tracking
- Payroll
- Human Resources
- Hospitality
- Retail
- REST
- Authentication
website: https://openapi.planday.com/
---
