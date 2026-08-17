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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: OAuth2-secured REST API for consuming Dataminr real-time alerts and managing watchlists/lists. Token flow at /auth/2/token; alert polling at /api/3/alerts; account and list management at /account/2/*.
  name: Dataminr Pulse API
  slug: dataminr-pulse-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.dataminr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dataminr.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dataminr.com
- group: company
  title: ''
  type: Blog
  url: https://www.dataminr.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.dataminr.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dataminr
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dataminr.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dataminr.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dataminr.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/dataminr-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dataminr.com/v1/dataminr-trust-services/
- group: auth
  title: ''
  type: Authentication
  url: authentication/dataminr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dataminr-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dataminr-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dataminr-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dataminr-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dataminr-llms.txt
created: '2026-07-17'
description: Dataminr delivers AI-powered real-time event, threat and risk intelligence, detecting breaking events and emerging risks across more than one million public data sources using proprietary large language models and multi-modal fusion AI. Its product lines span corporate security, cyber defense, public sector (First Alert) and newsroom situational awareness, serving government agencies and a large share of the Fortune 50. The Dataminr Pulse API exposes real-time alert consumption plus watchlist and account management over an OAuth2-secured REST gateway (gateway.dataminr.com), enabling integrations with SIEM, SOAR and security operations tooling.
image: https://www.dataminr.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Dataminr
nav: Providers
network: true
overview: 'Dataminr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Threat Intelligence, Risk, and Real-Time.


  Dataminr''s developer surface includes documentation, engineering blog, support, authentication, and 13 more developer resources.'
random_paper: 103
score:
  band: emerging
  composite: 26.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 26.2
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dataminr/refs/heads/main/screenshots/dataminr-2026-07-25T211346.png
security:
- kind: authentication
  name: Dataminr Authentication
  slug: dataminr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Dataminr Domain Security
  slug: dataminr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dataminr Trust Center
  slug: dataminr-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2013, ISO/IEC 27701:2019, NIST 800-171, UK Cyber Essentials Plus, GDPR, CCPA
slug: dataminr
tags:
- Company
- Analytics
- Threat Intelligence
- Risk
- Real-Time
- Security
- Artificial Intelligence
- Alerting
website: https://www.dataminr.com
---
