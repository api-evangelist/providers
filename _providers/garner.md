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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: The Facilities API from Garner — 1 operation(s) for facilities.
  name: Garner Facilities API
  slug: garner-facilities-api
- description: The Professionals API from Garner — 1 operation(s) for professionals.
  name: Garner Professionals API
  slug: garner-professionals-api
- description: The Provider Annotations API from Garner — 1 operation(s) for provider annotations.
  name: Garner Provider Annotations API
  slug: garner-provider-annotations-api
- description: The Providers API from Garner — 1 operation(s) for providers.
  name: Garner Providers API
  slug: garner-providers-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.getgarner.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://garnerhealth.redoc.ly
- group: docs
  title: ''
  type: Documentation
  url: https://garnerhealth.redoc.ly
- group: docs
  title: ''
  type: APIReference
  url: https://garnerhealth.redoc.ly
- group: auth
  title: ''
  type: Authentication
  url: authentication/garner-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/garner-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/garner-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/garner-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/garner-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getgarner.com/news/garner-completes-soc-2-type-ii-certification
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/garner-lifecycle.yml
- group: company
  title: ''
  type: Blog
  url: https://garnerhealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://garnerhealth.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://garnerhealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://garnerhealth.com/privacy-policy
created: '2026-07-17'
description: Garner Health is a healthcare technology company that helps members find high-quality, in-network doctors while helping employers, advisors, health plans, and providers improve care quality and lower costs. Garner analyzes more than 60 billion de-identified medical records from 320M+ patients and applies 550+ specialty-specific quality and efficiency metrics across 80+ specialties to identify Top Providers, delivered as an employer-funded benefit layered on top of existing insurance and as the Garner DataPro provider-recommendation data service. The Garner Health API (v1.x, OpenAPI 3.0.3) exposes ranked provider search, professional and facility directory detail, and provider-record annotation, authenticated with OAuth 2.0 client-credentials tokens.
image: https://cdn.prod.website-files.com/6994c8f92ae6b0d756f5e541/69b15a86b59f244f1a4d372e_Open%20graph%20img.png
layout: provider
mcp_servers:
- description: ''
  name: garner-mcp.yml
  slug: garner-mcpyml
modified: '2026-07-19'
name: Garner
nav: Providers
network: true
overview: 'Garner publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Facilities API, Professionals API, Provider Annotations API, and 1 more. Tagged areas include Company, Healthtech, Healthcare, Provider Data, and Care Navigation.


  Garner''s developer surface includes documentation, API reference, authentication, engineering blog, support, and 11 more developer resources.'
random_paper: 74
score:
  band: developing
  composite: 42.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.1
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 42.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/garner/refs/heads/main/screenshots/garner-2026-07-25T215448.png
security:
- kind: authentication
  name: Garner Authentication
  slug: garner-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Garner Domain Security
  slug: garner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: garner
tags:
- Company
- Healthtech
- Healthcare
- Provider Data
- Care Navigation
- Health Insurance
- Claims Analytics
- Provider Search
- Doctor Quality
website: https://www.getgarner.com/
---
