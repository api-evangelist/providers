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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Sap Successfactors Agentic Access
  operation_count: 9
  slug: sap-successfactors-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 10
apis:
- description: OData V4 REST API for HXM Suite providing CRUD access to Employee Central, talent management, learning, and platform entities. Authentication uses OAuth 2.0 SAML bearer assertion or HTTP Basic.
  name: SAP SuccessFactors OData V4 API
  slug: odata-v4-api
- description: OData V2 REST API for HXM Suite covering Employee Central, Recruiting, Onboarding, Compensation, Learning, and platform foundation objects. Authentication uses OAuth 2.0 or HTTP Basic.
  name: SAP SuccessFactors OData V2 API
  slug: odata-v2-api
- description: The EmpEmployment API from SAP SuccessFactors — 1 operation(s) for empemployment.
  name: SAP SuccessFactors EmpEmployment API
  slug: sap-successfactors-empemployment-api
- description: The EmpJob API from SAP SuccessFactors — 1 operation(s) for empjob.
  name: SAP SuccessFactors EmpJob API
  slug: sap-successfactors-empjob-api
- description: The FOCompany API from SAP SuccessFactors — 1 operation(s) for focompany.
  name: SAP SuccessFactors FOCompany API
  slug: sap-successfactors-focompany-api
- description: The Oauth API from SAP SuccessFactors — 1 operation(s) for oauth.
  name: SAP SuccessFactors Oauth API
  slug: sap-successfactors-oauth-api
- description: The PerPerson API from SAP SuccessFactors — 1 operation(s) for perperson.
  name: SAP SuccessFactors PerPerson API
  slug: sap-successfactors-perperson-api
- description: The Upsert API from SAP SuccessFactors — 1 operation(s) for upsert.
  name: SAP SuccessFactors Upsert API
  slug: sap-successfactors-upsert-api
- description: The User API from SAP SuccessFactors — 1 operation(s) for user.
  name: SAP SuccessFactors User API
  slug: sap-successfactors-user-api
- description: The User('{userId}') API from SAP SuccessFactors — 1 operation(s) for user('{userid}').
  name: SAP SuccessFactors User('{userId}') API
  slug: sap-successfactors-user-userid-api
artifact_total: 16
collections:
- collection_type: open
  name: SAP SuccessFactors HXM Suite OData API
  slug: open-sap-successfactors
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-successfactors-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-successfactors-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-successfactors-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-successfactors-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-successfactors-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sapsuccessfactors
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/hcm.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM
- group: start
  title: ''
  type: SAP Help Portal
  url: https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM
- group: other
  title: ''
  type: SAP API Hub
  url: https://api.sap.com/package/SAPSuccessFactors
created: '2026-05-11'
description: SAP SuccessFactors is a cloud-based human capital management (HCM) suite that covers core HR, payroll, talent management, learning, recruiting, performance, and workforce analytics for enterprises. The SuccessFactors HXM Suite OData APIs (v2 and v4) provide CRUD access to Employee Central, Recruiting, Onboarding, Learning, and other HCM modules using OAuth 2.0 or HTTP Basic authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sap-successfactors.png
layout: provider
modified: '2026-05-11'
name: SAP SuccessFactors
nav: Providers
network: true
overview: 'SAP SuccessFactors publishes 8 APIs on the [APIs.io](https://apis.io/) network, including EmpEmployment API, EmpJob API, FOCompany API, and 5 more. Tagged areas include HCM, HR, Human Resources, Talent Management, and Payroll.


  SAP SuccessFactors'' developer surface includes authentication, documentation, and 9 more developer resources.'
random_paper: 76
scopes:
- name: Sap Successfactors Scopes
  scope_count: 0
  slug: sap-successfactors-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-successfactors/refs/heads/main/screenshots/sap-successfactors-2026-06-20T193430.png
security:
- kind: authentication
  name: Sap Successfactors Authentication
  slug: sap-successfactors-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sap Successfactors Domain Security
  slug: sap-successfactors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Successfactors Vulnerability Disclosure
  slug: sap-successfactors-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-successfactors
tags:
- HCM
- HR
- Human Resources
- Talent Management
- Payroll
- Enterprise
- SAP
website: https://www.sap.com/products/hcm.html
---
