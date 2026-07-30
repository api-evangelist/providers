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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'REST API for the Ermeo connected-operator platform. Authenticated with OAuth 2.0 (Bearer access tokens), it lets external systems read and write equipment, forms, reports, and field data so customers '
  name: Ermeo API
  slug: ermeo-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.ermeo.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://ermeo.stoplight.io/
- group: docs
  title: ''
  type: Documentation
  url: https://support.en.ermeo.com/login-to-ermeo-api-and-send-requests
- group: start
  title: ''
  type: GettingStarted
  url: https://support.en.ermeo.com/getting-started-with-ermeo
- group: operate
  title: ''
  type: Support
  url: https://support.en.ermeo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ermeo.com/en/blog/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ermeo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ermeo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ermeo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ermeo-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ermeo-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ermeo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ermeo-llms.txt
created: '2026-07-17'
description: Ermeo (rebranded Causeway Field) is a French connected-operator / field-operations SaaS platform that lets industrial and field teams digitize paper procedures into dynamic, interactive workflows for inspections, maintenance, and interventions. Operators complete pre-built interactive forms on mobile, capture equipment and report data in the field in real time, and operational managers monitor all field work from a central console. Ermeo exposes a REST API secured with OAuth 2.0 so customers can connect their information systems (CMMS, MES, EDM) to import and synchronize equipment, forms, and reports and enrich the data collected in the field.
image: https://www.ermeo.com/en/
layout: provider
modified: '2026-07-19'
name: Ermeo
nav: Providers
network: true
overview: 'Ermeo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Field Service Management, Connected Operator, Field Operations, and Industrial.


  Ermeo''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, authentication, and 7 more developer resources.'
random_paper: 44
score:
  band: emerging
  composite: 17.8
  delta: -0.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    conformance: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ermeo/refs/heads/main/screenshots/ermeo-2026-07-25T213610.png
security:
- kind: authentication
  name: Ermeo Authentication
  slug: ermeo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ermeo Domain Security
  slug: ermeo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ermeo
tags:
- Company
- Field Service Management
- Connected Operator
- Field Operations
- Industrial
- Maintenance
- Inspections
- SaaS
website: https://www.ermeo.com/en/
---
