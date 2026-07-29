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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Activtrak Agentic Access
  operation_count: 23
  slug: activtrak-agentic-access
  summary_line: 23 operations · 10 acting
api_count: 4
apis:
- description: Administer the ActivTrak account (clients, consumers). Beta.
  name: ActivTrak Administration API
  slug: activtrak-administration-api
- description: SCIM 2.0 user and group management. Beta.
  name: ActivTrak Administration - SCIM API
  slug: activtrak-administration-scim-api
- description: HR Data Connector - submit CSV bulk user data.
  name: ActivTrak Bulk Import API
  slug: activtrak-bulk-import-api
- description: Live Data API - query activity reports (Working Hours, Activity Log).
  name: ActivTrak Reports API
  slug: activtrak-reports-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/activtrak-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/activtrak-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/activtrak-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/activtrak-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/activtrak-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activtrak-domain-security.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/activtrak-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.activtrak.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.activtrak.com/changelog/activtrak/activtrak-public-apis
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.activtrak.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.activtrak.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.activtrak.com/
- group: operate
  title: ''
  type: Support
  url: https://support.activtrak.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.activtrak.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.activtrak.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.activtrak.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.activtrak.com/
- group: company
  title: ''
  type: Website
  url: https://www.activtrak.com/
created: '2026-07-17'
description: 'ActivTrak is a workforce analytics and productivity-monitoring SaaS platform. Its Public APIs (v2) expose REST endpoints across three surfaces: the Live Data / Reports API (Working Hours and Activity Log), account administration (Clients, Consumers, and full SCIM 2.0 user and group management), and a Bulk Import HR Data Connector for CSV-driven user provisioning. Authentication is via an API key sent in the x-api-key header (a Bearer form is also accepted on some endpoints). Regional hosts are available for the United States, European Union, United Kingdom, Canada, and Australia. ActivTrak is backed by Sapphire Ventures and is profiled in the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/activtrak.png
layout: provider
modified: '2026-07-17'
name: ActivTrak
nav: Providers
network: true
overview: 'ActivTrak publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Administration - SCIM API, Bulk Import API, and 1 more. Tagged areas include Company, Saas, Workforce Analytics, Productivity, and Employee Monitoring.


  ActivTrak''s developer surface includes authentication, changelog, documentation, API reference, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 45
score:
  band: developing
  composite: 50.1
  delta: 1.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.9
    developer_ergonomics: 41.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/activtrak/refs/heads/main/screenshots/activtrak-2026-07-25T181531.png
security:
- kind: authentication
  name: Activtrak Authentication
  slug: activtrak-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Activtrak Domain Security
  slug: activtrak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Activtrak Vulnerability Disclosure
  slug: activtrak-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Activtrak Trust Center
  slug: activtrak-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: activtrak
tags:
- Company
- Saas
- Workforce Analytics
- Productivity
- Employee Monitoring
- Workforce Management
- SCIM
- Reporting
website: https://www.activtrak.com/
---
