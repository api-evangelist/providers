---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API for accessing Paycor employees, payroll, benefits, time, and organizational data. Uses OAuth 2.0 authorization code flow with authorization at secure.paycor.com/connect/authorize and tokens i
  name: Paycor Public API v1
  slug: public-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paycor-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paycor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paycor
- group: company
  title: ''
  type: Website
  url: https://www.paycor.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.paycor.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paycor.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://developers.paycor.com/register
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.paycor.com/llms.txt
created: '2026-05-11'
description: Paycor is a cloud-based human capital management (HCM) platform that provides payroll, HR, benefits administration, talent management, time and attendance, and workforce analytics for small and mid-sized businesses. The platform serves HR and finance teams with a unified system of record for employees, pay, time, and benefits data. Paycor exposes a Public REST API authenticated via OAuth 2.0 with authorization at secure.paycor.com and resource endpoints at apis.paycor.com (production) and apis-sandbox.paycor.com (sandbox).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paycor.png
layout: provider
modified: '2026-05-11'
name: Paycor
nav: Providers
network: true
overview: 'Paycor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HCM, Payroll, Human Resources, Benefits Administration, and Time and Attendance.


  Paycor''s developer surface includes documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paycor/refs/heads/main/screenshots/paycor-2026-06-20T191452.png
security:
- kind: domain-security
  name: Paycor Domain Security
  slug: paycor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paycor
tags:
- HCM
- Payroll
- Human Resources
- Benefits Administration
- Time and Attendance
website: https://www.paycor.com
---
