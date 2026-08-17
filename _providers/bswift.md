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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: bswift's partner-facing REST API, served from an AWS API Gateway at api.bswift.com. bswift publicly describes API coverage for demographics and employment data, with lifecycle domains (plan, rate, enr
  name: bswift Partner API
  slug: bswift-partner-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.bswift.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bswift.com/research-insights/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bswift.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.bswift.com/bswift-vulnerability-disclosure-program/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bswift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bswift-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bswift.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bswift-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bswift-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bswift-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bswift.com/research-insights/product-updates/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bswift-llms.txt
- group: company
  title: ''
  type: Partners
  url: https://www.bswift.com/connectivity-hub/
coverage:
  checked: '2026-08-06'
  detail: api.bswift.com is a live AWS API Gateway whose /ping route returns 200 "healthy", but every functional route answers MISSING_AUTHENTICATION_TOKEN and the only public path to the OpenAPI specs, sandbox and webhook topics bswift says it ships is the Partnership Opportunities contact form — bswift runs no developer portal, docs host or API reference anywhere on bswift.com.
  evidence:
  - status: 200
    url: https://api.bswift.com/ping
  - status: 400
    url: https://api.bswift.com/openapi.json
  - status: 403
    url: https://api.bswift.com/v1/openapi.json
  - status: 200
    url: https://www.bswift.com/connectivity-hub/
  reason: sales-gate
  state: gated
created: '2026-08-06'
description: 'bswift is a benefits administration platform used by employers, brokers and channel partners to run health and welfare benefits — eligibility, annual enrollment, life events, COBRA, billing and ACA compliance — with an AI assistant (Emma) layered over the employee experience. Founded in Chicago in 2000, bswift was acquired by Aetna in 2014, moved into CVS Health, and has operated as an independent company backed by Francisco Partners since the 2022 carve-out. It runs a large connectivity estate: 450+ active carrier file feeds, 300+ pre-built and API integrations, and 150+ API and SSO connections into HCM and payroll platforms including ADP, UKG, Paylocity and Workday. Its production API gateway is live at api.bswift.com, but the REST contract — along with the OpenAPI specs, sandbox environments and webhook event topics bswift describes publicly — is issued only to alliance, integration and channel partners; there is no public developer portal or API reference.'
image: https://www.bswift.com/wp-content/uploads/2024/10/header-logo.svg
layout: provider
modified: '2026-08-06'
name: bswift
nav: Providers
network: true
overview: 'bswift publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Benefits Administration, Human Resources, Insurance, and Health Insurance.


  bswift''s developer surface includes engineering blog, changelog, and 11 more developer resources.'
random_paper: 59
score:
  band: emerging
  composite: 21.4
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 21.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 39.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Bswift Domain Security
  slug: bswift-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bswift Vulnerability Disclosure
  slug: bswift-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Bswift Trust Center
  slug: bswift-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, SOC 3, HIPAA, HITRUST
slug: bswift
tags:
- Company
- Benefits Administration
- Human Resources
- Insurance
- Health Insurance
- Employee Benefits
- HR Technology
- COBRA
- Enrollment
- Payroll
- Health and Welfare
- Compliance
website: https://www.bswift.com/
---
