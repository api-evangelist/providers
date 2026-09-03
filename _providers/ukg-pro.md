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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ukg Pro Agentic Access
  operation_count: 6
  slug: ukg-pro-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: REST API for the UKG Pro HCM suite covering people, benefits, payroll, talent, recruiting, onboarding, and HR data. Hosted on tenant-specific hostnames with OAuth 2.0 Bearer token authentication obtai
  name: UKG Pro HCM API
  slug: hcm-api
- description: REST API for the UKG Pro Workforce Management product (Dimensions), covering punches, shifts, scheduling, accruals, timekeeping, attendance, and labor data.
  name: UKG Pro WFM API
  slug: wfm-api
- description: Unified data fabric API that exposes consolidated person, employment, and workforce data across UKG Pro and connected systems for analytics and integration use cases.
  name: UKG People Fabric API
  slug: people-fabric-api
- baseURL: https://<<tenantHostName>>/api
  baseurl_source: declared
  description: Benefits enrollment and election data
  name: UKG Pro Benefits API
  slug: ukg-pro-benefits-api
- baseURL: https://<<tenantHostName>>/api
  baseurl_source: declared
  description: Employment history and changes
  name: UKG Pro Employment API
  slug: ukg-pro-employment-api
- baseURL: https://<<tenantHostName>>/api
  baseurl_source: declared
  description: Pay statements, earnings, and payroll data
  name: UKG Pro Pay API
  slug: ukg-pro-pay-api
- baseURL: https://<<tenantHostName>>/api
  baseurl_source: declared
  description: Personnel and employee records
  name: UKG Pro People API
  slug: ukg-pro-people-api
- baseURL: https://<<tenantHostName>>/api
  baseurl_source: declared
  description: Recruiting and applicant tracking
  name: UKG Pro Recruiting API
  slug: ukg-pro-recruiting-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UKG Pro HCM Benefits API
  slug: open-ukg-pro-benefits-api
- collection_type: open
  name: UKG Pro HCM Benefits Employment API
  slug: open-ukg-pro-employment-api
- collection_type: open
  name: UKG Pro HCM Benefits Pay API
  slug: open-ukg-pro-pay-api
- collection_type: open
  name: UKG Pro HCM Benefits People API
  slug: open-ukg-pro-people-api
- collection_type: open
  name: UKG Pro HCM Benefits Recruiting API
  slug: open-ukg-pro-recruiting-api
- collection_type: open
  name: UKG Pro HCM API
  slug: open-ukg-pro
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ukg-pro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ukg-pro-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ukg-pro-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ultimatesoftware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ukg
- group: company
  title: ''
  type: Website
  url: https://www.ukg.com/solutions/ukg-pro
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ukg.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ukg.com
- group: auth
  title: ''
  type: Authentication
  url: https://developer.ukg.com/general/docs/authentication-and-authorization
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ukg.com/solutions/ukg-pro
- group: operate
  title: ''
  type: Support
  url: https://www.ukg.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.ukg.com/
- group: other
  title: ''
  type: Parent Company
  url: https://www.ukg.com/
created: '2026-05-11'
description: UKG Pro (formerly UltiPro) is an enterprise human capital management (HCM) suite from UKG that delivers payroll, core HR, benefits administration, talent management, recruiting, onboarding, performance, learning, and people analytics for mid-to-large organizations. The platform combines the legacy UltiPro HR/payroll product with UKG's workforce management capabilities and is positioned for HR teams that need a unified system of record. The UKG Pro REST API exposes HCM resources (people, benefits, payroll, talent) via tenant-specific endpoints authenticated with OAuth 2.0 Bearer tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ukg-pro.png
layout: provider
modified: '2026-05-11'
name: UKG Pro
nav: Providers
network: true
overview: 'UKG Pro publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Benefits API, Employment API, Pay API, and 2 more. Tagged areas include HCM, HR, Payroll, Benefits Administration, and Talent Management.


  UKG Pro''s developer surface includes authentication, documentation, pricing, support, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 51.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ukg-pro/refs/heads/main/screenshots/ukg-pro-2026-06-20T200008.png
security:
- kind: authentication
  name: Ukg Pro Authentication
  slug: ukg-pro-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ukg Pro Domain Security
  slug: ukg-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ukg-pro
tags:
- HCM
- HR
- Payroll
- Benefits Administration
- Talent Management
- Workforce Management
- HRIS
website: https://www.ukg.com/solutions/ukg-pro
---
