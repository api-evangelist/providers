---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Finch Agentic Access
  operation_count: 9
  slug: finch-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- description: The Auth API from Finch — 1 operation(s) for auth.
  name: Finch Auth API
  slug: finch-auth-api
- description: The Connect API from Finch — 1 operation(s) for connect.
  name: Finch Connect API
  slug: finch-connect-api
- description: The Employer API from Finch — 7 operation(s) for employer.
  name: Finch Employer API
  slug: finch-employer-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Finch Auth API
  slug: open-finch-auth-api
- collection_type: open
  name: Finch Auth Connect API
  slug: open-finch-connect-api
- collection_type: open
  name: Finch Auth Employer API
  slug: open-finch-employer-api
- collection_type: open
  name: Finch API
  slug: open-finch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/finch-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/finch-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Finch-API
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finchapi
- group: company
  title: ''
  type: Website
  url: https://www.tryfinch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tryfinch.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tryfinch.com/api-reference/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.tryfinch.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryfinch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.tryfinch.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.tryfinch.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryfinch.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.tryfinch.com/llms.txt
created: '2026-03-16'
description: Finch is a unified employment API providing standardized read and write access to HRIS, payroll, and benefits systems. Through a single integration, developers can pull company directory data, individual PII, employment records, payments, pay statements, and benefits across hundreds of providers (ADP, Gusto, Paylocity, Workday, BambooHR, Rippling, Justworks, TriNet, and more). Finch Connect handles end-user authorization via OAuth.
finops:
- name: Finch Finops
  service_category: API
  slug: finch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finch.png
layout: provider
modified: '2026-05-19'
name: Finch
nav: Providers
network: true
overview: 'Finch publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Connect API, and Employer API. Tagged areas include Employment, HRIS, Payroll, Benefits, and HR.


  Finch''s developer surface includes authentication, documentation, API reference, signup flow, pricing, engineering blog, changelog, and 8 more developer resources.'
plans:
- name: Finch Plans Pricing
  plan_count: 3
  slug: finch-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Finch Rate Limits
  slug: finch-rate-limits
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finch/refs/heads/main/screenshots/finch-2026-06-20T181218.png
security:
- kind: authentication
  name: Finch Authentication
  slug: finch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Finch Domain Security
  slug: finch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Finch Trust Center
  slug: finch-trust-center
  summary_line: SOC 2
slug: finch
tags:
- Employment
- HRIS
- Payroll
- Benefits
- HR
- Unified-API
- Workforce
website: https://www.tryfinch.com/
---
