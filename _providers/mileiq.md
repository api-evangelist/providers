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
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mileiq Agentic Access
  operation_count: 6
  slug: mileiq-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: The groups API from MileIQ — 3 operation(s) for groups.
  name: MileIQ groups API
  slug: mileiq-groups-api
- description: The users API from MileIQ — 3 operation(s) for users.
  name: MileIQ users API
  slug: mileiq-users-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mileiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mileiq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mileiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mileiq.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mileiq.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mileiq.com/api-reference/getting-started
- group: company
  title: ''
  type: Blog
  url: https://mileiq.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.mileiq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mileiq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mileiq.com/en-ca/for-business/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mileiq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mileiq.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/mileiq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mileiq-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mileiq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mileiq-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mileiq-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mileiq-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mileiq-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.mileiq.com/api-reference/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/mileiq-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mileiq-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mileiq-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mileiq-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mileiq-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mileiq-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: MileIQ is an automatic mileage-tracking service for individuals and teams that logs every drive in the background, classifies each trip as business or personal, and calculates the deductible mileage value for tax and expense reporting. Its read-only OAuth 2.1 External API (external-api.mileiq.com) exposes authenticated user profiles, drive/trip records with start and end geolocation, distance, and monetary value, plus administrator access to group (team) rosters and member-reported drives — letting accounting, expense, and reimbursement platforms sync MileIQ mileage data. Originally built by Mobile Data Labs and later part of Microsoft, MileIQ now operates as an independent product. The API is currently available on a request basis.
image: https://www.mileiq.com/images/mileiq.7b54ead1.svg
layout: provider
mcp_servers:
- description: ''
  name: mileiq-mcp.yml
  slug: mileiq-mcpyml
modified: '2026-07-20'
name: MileIQ
nav: Providers
network: true
overview: 'MileIQ publishes 2 APIs on the [APIs.io](https://apis.io/) network: groups API and users API. Tagged areas include Company, Consumer, Mileage Tracking, Expense Management, and Transportation.


  MileIQ''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 20 more developer resources.'
random_paper: 76
rate_limits:
- limit_count: 0
  name: Mileiq Rate Limits
  slug: mileiq-rate-limits
scopes:
- name: Mileiq Scopes
  scope_count: 7
  slug: mileiq-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 47.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.7
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Mileiq Authentication
  slug: mileiq-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Mileiq Domain Security
  slug: mileiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mileiq
tags:
- Company
- Consumer
- Mileage Tracking
- Expense Management
- Transportation
- Tax
- Accounting
- Location
- Fleet
website: https://www.mileiq.com/
---
