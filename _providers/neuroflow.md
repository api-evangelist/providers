---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'The REST API behind the NeuroFlow Live web and mobile applications, served same-origin from https://neuroflowlive.com/api/ (server: gunicorn, versioned /api/v2/ routes). A Swagger document is publishe'
  name: NeuroFlow Live API
  slug: neuroflow-live-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neuroflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.neuroflow.com/
- group: company
  title: ''
  type: Blog
  url: https://www.neuroflow.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://neuroflow.zendesk.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://neuroflowlive.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neuroflow.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neuroflow.com/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.neuroflowlive.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neuroflow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neuroflow-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/neuroflow-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neuroflow-llms.txt
coverage:
  checked: '2026-08-04'
  detail: 'NeuroFlow''s application backend does publish a Swagger document at /api/swagger.json, but it answers anonymous callers with HTTP 401 {"message": "Please log in to continue", "code": 0} on production, sandbox, QA, staging and dev alike, and there is no public developer portal anywhere to read it from.'
  evidence:
  - status: 401
    url: https://neuroflowlive.com/api/swagger.json
  - status: 401
    url: https://sandbox.neuroflow.io/api/swagger.json
  - status: 200
    url: https://neuroflowlive.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-04'
description: 'NeuroFlow is a Philadelphia-based behavioral health technology company that gives payers, health systems, provider groups and federal agencies the infrastructure to identify and manage behavioral health risk at scale. Its IntegrateBH platform pairs patient-facing mobile and web applications with measurement-based care and screening workflows, clinical dashboards, care-coordination tooling and population-level behavioral health analytics. The platform reaches customers through EHR and partner integrations — including Epic (App Orchard / Epic Showroom) and the Xealth digital-health ecosystem — over a session-authenticated REST API served from neuroflowlive.com/api/. NeuroFlow publishes no public developer portal: a Swagger document exists at /api/swagger.json on every environment, but it returns HTTP 401 "Please log in to continue" to anonymous callers, so the contract is customer-only.'
image: https://neuroflowlive.com/static/img/onward-favicon.DQ5xHIN6.png
layout: provider
modified: '2026-08-04'
name: NeuroFlow
nav: Providers
network: true
overview: 'NeuroFlow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Behavioral Health, Health Care, Mental Health, and Digital Health.


  NeuroFlow''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 65
score:
  band: emerging
  composite: 22.2
  delta: 1.3
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 20.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neuroflow/refs/heads/main/screenshots/neuroflow-2026-08-07T185022.png
security:
- kind: domain-security
  name: Neuroflow Domain Security
  slug: neuroflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neuroflow
tags:
- Company
- Behavioral Health
- Health Care
- Mental Health
- Digital Health
- Care Coordination
- Health Analytics
- EHR Integration
website: https://www.neuroflow.com/
---
