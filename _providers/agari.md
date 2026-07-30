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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful JSON API for the Agari Platform, secured with OAuth 2.0 Client Credentials. Provides access to Agari email-security telemetry — alerts, domain tracking, DMARC policy-enforcement reporting, and
  name: Agari Platform API
  slug: agari-platform-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://agari.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.agari.com/agari-platform
- group: docs
  title: ''
  type: Documentation
  url: https://developers.agari.com/agari-platform/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.agari.com/agari-platform/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.agari.com/agari-platform/docs/quick-start
- group: auth
  title: ''
  type: Authentication
  url: authentication/agari-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agari-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agari-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agari-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agari-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agari-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agari-llms.txt
created: '2026-07-17'
description: Agari is an email-security provider that pioneered and helped author the DMARC email-authentication standard to protect organizations from phishing, business email compromise (BEC), email spoofing, and brand impersonation. Founded in 2009, Agari was acquired by HelpSystems (now Fortra) in May 2021 and is delivered as Fortra's email-security portfolio, including DMARC Protection / Brand Protection, Phishing Defense, and Phishing Response. The Agari Platform exposes a RESTful JSON API secured with OAuth 2.0 Client Credentials for retrieving security telemetry, auditing users and domains, tracking DMARC policy enforcement, and integrating Agari data into SIEM and SOAR tooling. It was originally backed by Norwest Venture Partners and other venture investors before its acquisition.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agari.png
layout: provider
modified: '2026-07-17'
name: Agari
nav: Providers
network: true
overview: 'Agari publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email Security, Cybersecurity, DMARC, and Email Authentication.


  Agari''s developer surface includes documentation, API reference, getting-started guide, authentication, and 8 more developer resources.'
random_paper: 24
score:
  band: emerging
  composite: 18.2
  delta: -0.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agari/refs/heads/main/screenshots/agari-2026-07-25T181754.png
security:
- kind: authentication
  name: Agari Authentication
  slug: agari-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Agari Domain Security
  slug: agari-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agari
tags:
- Company
- Email Security
- Cybersecurity
- DMARC
- Email Authentication
- Phishing
- Anti-Phishing
- Brand Protection
- API
- REST
website: https://agari.com
---
