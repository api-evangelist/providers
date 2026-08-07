---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 256
  human_in_the_loop: 6
  name: Harri Agentic Access
  operation_count: 385
  slug: harri-agentic-access
  summary_line: 385 operations · 256 acting · 6 human-in-the-loop
api_count: 2
apis:
- description: 'The Harri Employee API is the core of the Harri Open API Hub. It manages and retrieves employee data across the Harri platform: employee create/read/update, employee profiles, location attachment and '
  name: Harri Employee API
  slug: employee-api
- description: The Harri Employer (External Brand Management) API creates and manages Harri above-store admin users and employer/brand records. It provides v1 user CRUD keyed on an external user id, v2 employer CRUD
  name: Harri External Brand Management API
  slug: employer-api
artifact_total: 9
asyncapis:
- description: ''
  name: Harri Webhooks
  slug: harri-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harri-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harri-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/harri-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://harri.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.harri.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.harri.com/about-api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.harri.com/employees/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.harri.com/authentication/
- group: auth
  title: ''
  type: Authentication
  url: authentication/harri-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://developer.harri.com/sign-up/
- group: operate
  title: ''
  type: Support
  url: https://harri.com/request-a-demo/
- group: company
  title: ''
  type: Blog
  url: https://resources.harri.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HarriLLC
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harri.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harri.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harri.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.harri.com/api-release-notes/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harri-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/harri-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/harri-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/harri-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/harri-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/harri-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harri-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/harri-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/harri-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/harri-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harri-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harri-llms.txt
created: '2026-08-04'
description: Harri is a hospitality-first human capital management (HCM) and workforce management platform used by enterprise restaurants, hotels, retailers, grocers and care operators to run the full employee lifecycle — talent acquisition and onboarding, scheduling and demand forecasting, time and attendance, labor compliance, payroll data export and workforce analytics. Harri exposes a public Open API Hub through its developer portal at developer.harri.com, secured with OAuth 2.0 client credentials and fronted by an API gateway at gateway.harri.com. The published surface covers employee records, locations, positions, job titles, pay types, hourly and annual rates, tronc and tip distribution, employment periods, absences, max weekly hours and working patterns, external-system ID mappings, platform events and webhook subscriptions, plus an employer/brand-management surface for above-store admin users. A parallel franchisee-scoped path set mirrors the corporate endpoints for multi-brand
  and franchise operators.
image: https://cdn.harri.com/10c3cd15-ec51-41c0-ba18-3227e664ad83/images/icons/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: harri-mcp.yml
  slug: harri-mcpyml
modified: '2026-08-04'
name: Harri
nav: Providers
network: true
overview: 'Harri publishes 2 APIs on the [APIs.io](https://apis.io/) network: Employee API and External Brand Management API. Tagged areas include Human Resources, Workforce Management, Hospitality, Restaurants, and Scheduling.


  The Harri catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Harri''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, engineering blog, and 23 more developer resources.'
random_paper: 82
rate_limits:
- limit_count: 1
  name: Harri Rate Limits
  slug: harri-rate-limits
scopes:
- name: Harri Scopes
  scope_count: 0
  slug: harri-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.9
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 65.8
  previous_composite: 53.1
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
  name: Harri Authentication
  slug: harri-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Harri Domain Security
  slug: harri-domain-security
  summary_line: TLSv1.3 · DMARC
slug: harri
tags:
- Human Resources
- Workforce Management
- Hospitality
- Restaurants
- Scheduling
- Time and Attendance
- Payroll
- Talent Acquisition
- Labor Compliance
- HCM
website: https://harri.com/
---
