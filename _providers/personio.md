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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Personio Agentic Access
  operation_count: 9
  slug: personio-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 6
apis:
- description: Next-generation REST API with OAuth 2.0 Client Credentials Grant authentication. Token endpoint POST /v2/auth/token returns access tokens used as Bearer credentials on subsequent calls.
  name: Personio Public API v2
  slug: public-api-v2
- description: Manage absence periods.
  name: Personio Absence Periods API
  slug: personio-absence-periods-api
- description: OAuth 2.0 token exchange.
  name: Personio Auth API
  slug: personio-auth-api
- description: Manage person (employee) records.
  name: Personio Persons API
  slug: personio-persons-api
- description: Read project definitions.
  name: Personio Projects API
  slug: personio-projects-api
- description: Manage event webhook subscriptions.
  name: Personio Webhooks API
  slug: personio-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Personio Public API v2 Absence Periods API
  slug: open-personio-absence-periods-api
- collection_type: open
  name: Personio Public API v2 Absence Periods Auth API
  slug: open-personio-auth-api
- collection_type: open
  name: Personio Public API v2 Absence Periods Persons API
  slug: open-personio-persons-api
- collection_type: open
  name: Personio Public API v2 Absence Periods Projects API
  slug: open-personio-projects-api
- collection_type: open
  name: Personio Public API v2 Absence Periods Webhooks API
  slug: open-personio-webhooks-api
- collection_type: open
  name: Personio Public API v2
  slug: open-personio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/personio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/personio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/personio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/personio-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/personio
- group: company
  title: ''
  type: Website
  url: https://www.personio.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.personio.de/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.personio.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.personio.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/personio
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.personio.de/llms.txt
created: '2026-05-11'
description: Personio is a European HR management and recruiting platform serving small and mid-sized businesses with a unified HRIS covering employee records, absence management, time tracking, payroll preparation, performance, and applicant tracking. The platform is headquartered in Munich and is widely adopted across Germany, Austria, Switzerland, the UK, the Netherlands, and Spain. Personio exposes a Public API at api.personio.de that supports Bearer token authentication via Client ID/Secret (v1 token endpoint and v2 OAuth 2.0 client credentials flow), with webhooks now available for Person entity events.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/personio.png
layout: provider
modified: '2026-05-11'
name: Personio
nav: Providers
network: true
overview: 'Personio publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Absence Periods API, Auth API, Persons API, and 2 more. Tagged areas include Human Resources, HRIS, Recruiting, Applicant Tracking, and Absence Management.


  Personio''s developer surface includes authentication, documentation, pricing, signup flow, and 7 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 29.9
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 10.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/personio/refs/heads/main/screenshots/personio-2026-06-20T191622.png
security:
- kind: authentication
  name: Personio Authentication
  slug: personio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Personio Domain Security
  slug: personio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Personio Trust Center
  slug: personio-trust-center
  summary_line: ISO 27001, ISO 27017, GDPR
slug: personio
tags:
- Human Resources
- HRIS
- Recruiting
- Applicant Tracking
- Absence Management
- Time Tracking
- Europe HR
website: https://www.personio.com
---
