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
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: Real-time GET query to authenticate a LeadiD token against an account code, confirming lead capture provenance. Credentials are passed as query parameters (lac account code, id LeadiD token).
  name: InfutorData Authentication API
  slug: infutordata-authentication-api
- description: 'Real-time GET query (SingleQuery) returning a lead audit object with authentication status, data-integrity checks, device/IP/frequency metrics, TCPA compliance data, consumer scoring, and demographic '
  name: InfutorData Intelligence / Lead Audit API
  slug: infutordata-intelligence-lead-audit-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infutor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infutor.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.infutor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.infutor.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.infutor.com/docs/infutor-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.infutor.com/docs/intelligence-getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.infutor.com/
- group: company
  title: ''
  type: Blog
  url: https://infutor.com/category/resources/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infutor.com/privacy-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infutor.com/terms-and-conditions/
- group: auth
  title: ''
  type: Authentication
  url: authentication/infutor-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infutor-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/infutor-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infutor-llms.txt
created: '2026-07-17'
description: InfutorData (part of ActiveProspect, formerly Infutor / Jornaya / LeadiD) is a consumer identity and data-solutions provider that helps marketers identify, understand, and reach consumers while maintaining privacy and compliance. Its platform delivers identity resolution and completion, identity scoring, consumer data enrichment and attributes, audience activation, and lead-quality and TCPA compliance tooling (TCPA Guardian, LeadiD tokens). Real-time query APIs on api.leadid.com support authentication, lead audit, intelligence, and privacy-guardian lookups, documented in the InfutorData help center. Backed by Norwest Venture Partners.
image: https://infutor.com/wp-content/uploads/2026/04/ID_primary_logo.png
layout: provider
modified: '2026-07-19'
name: Infutor
nav: Providers
network: true
overview: 'Infutor publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity Resolution, Consumer Data, Data Enrichment, and Lead Verification.


  Infutor''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 7 more developer resources.'
random_paper: 79
score:
  band: emerging
  composite: 23.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infutor/refs/heads/main/screenshots/infutor-2026-07-25T222430.png
security:
- kind: authentication
  name: Infutor Authentication
  slug: infutor-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Infutor Domain Security
  slug: infutor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: infutor
tags:
- Company
- Identity Resolution
- Consumer Data
- Data Enrichment
- Lead Verification
- TCPA Compliance
- Marketing
- Identity
website: https://infutor.com
---
