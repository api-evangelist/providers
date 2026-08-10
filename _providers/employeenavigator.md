---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The Employee Navigator OpenID Connect / OAuth 2.0 authorization server that fronts every Employee Navigator API service. Its discovery document is served anonymously and advertises authorization code,
  name: Employee Navigator Identity (OpenID Connect)
  slug: employee-navigator-identity-openid-connect
- description: 'The Employee Navigator partner REST API program — the Company Integration API and the Company Benefit Details API announced in 2022 — used by insurance carriers, benefit providers, payroll companies, '
  name: Employee Navigator Partner API
  slug: employee-navigator-partner-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.employeenavigator.com/
- group: company
  title: ''
  type: Blog
  url: https://www.employeenavigator.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.employeenavigator.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.employeenavigator.com/benefits/Account/Login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.employeenavigator.com/master-terms
- group: operate
  title: ''
  type: Support
  url: https://support.employeenavigator.com/hc/en-us
- group: auth
  title: ''
  type: Compliance
  url: https://www.employeenavigator.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/employeenavigator-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/employeenavigator-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/employeenavigator-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/employeenavigator-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/employeenavigator-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/employeenavigator-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/employeenavigator-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/employeenavigator-llms.txt
created: '2026-08-06'
description: Employee Navigator is a Bethesda, Maryland benefits administration and HR software platform used by insurance brokers, agencies and employers to run open enrollment, new hire onboarding, ACA reporting, HR management, PTO tracking and integrated payroll. Its integration layer connects employer benefit data to more than 600 insurance carriers, payroll providers, TPAs and agency management systems through EDI ANSI 834 files, data-exchange feeds and a partner REST API program. Employee Navigator published a Company Integration API and a Company Benefit Details API for carriers and benefit providers, secured by an OpenID Connect / OAuth 2.0 authorization server that publicly advertises a per-service scope surface covering company integration, plan configuration and management, employee profile, payroll, quoting, agency management, evidence of insurability, COBRA, data audit, data sync, notifications and webhooks. The API reference itself is partner-gated; the platform runs on Microsoft
  Azure and is audited annually for SOC 2 Type II, HITRUST, NIST, GDPR, CCPA and 23 NYCRR 500.
image: https://www.employeenavigator.com/uploads/2021/10/OG-image-employee-navigator.png
layout: provider
modified: '2026-08-06'
name: Employee Navigator
nav: Providers
network: true
overview: 'Employee Navigator publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Benefits Administration, Human Resources, Insurance, and Employee Benefits.


  Employee Navigator''s developer surface includes engineering blog, pricing, support, authentication, and 11 more developer resources.'
random_paper: 95
scopes:
- name: Employeenavigator Scopes
  scope_count: 66
  slug: employeenavigator-scopes
  summary_line: 66 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 29.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 29.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 65.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/employeenavigator/refs/heads/main/screenshots/employeenavigator-2026-08-07T164835.png
security:
- kind: authentication
  name: Employeenavigator Authentication
  slug: employeenavigator-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Employeenavigator Domain Security
  slug: employeenavigator-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Employeenavigator Trust Center
  slug: employeenavigator-trust-center
  summary_line: SOC 2 Type II, HITRUST, HIPAA, GDPR, CCPA, 23 NYCRR 500 (NYDFS), NIST
slug: employeenavigator
tags:
- Company
- Benefits Administration
- Human Resources
- Insurance
- Employee Benefits
- Payroll
- Health Insurance
- HRIS
- Open Enrollment
- ACA Compliance
- Identity
- OpenID Connect
website: https://www.employeenavigator.com/
---
