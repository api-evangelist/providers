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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.ohmconnect.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ohmconnect.com
- group: operate
  title: ''
  type: Support
  url: https://www.ohmconnect.com/help
- group: start
  title: ''
  type: SignUp
  url: https://login.ohmconnect.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.ohmconnect.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ohmconnect.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ohmconnect.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ohmconnect
- group: auth
  title: ''
  type: Authentication
  url: authentication/ohmconnect-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ohmconnect-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ohmconnect-llms.txt
created: '2026-07-17'
description: OhmConnect is a residential demand-response and virtual power plant company that turns household electricity flexibility into grid capacity. It alerts customers during "OhmHours" — windows when grid power is most expensive or carbon-intensive — and pays them cash, gift cards, and prizes for reducing or automating down their usage, then aggregates those reductions and sells them into wholesale energy markets. It serves California utility customers (PG&E, SCE, and SDG&E) and operates as a competitive retail electricity provider in Texas through OhmConnect Energy. OhmConnect runs a login-gated developer portal (developer.ohmconnect.com) secured with AWS Cognito OAuth2, but publishes no public API specification.
image: https://cdn.prod.website-files.com/628decbd69d2a151a1bbecd2/634773439fd2754c60a4a97f_ohmconnect-save-energy-save-money-preview.jpg
layout: provider
modified: '2026-07-20'
name: Ohmconnect
nav: Providers
network: true
overview: 'Ohmconnect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Demand Response, Virtual Power Plant, and Utilities.


  Ohmconnect''s developer surface includes support, signup flow, authentication, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 17.4
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ohmconnect/refs/heads/main/screenshots/ohmconnect-2026-08-07T190040.png
security:
- kind: authentication
  name: Ohmconnect Authentication
  slug: ohmconnect-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Ohmconnect Domain Security
  slug: ohmconnect-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ohmconnect
tags:
- Company
- Energy
- Demand Response
- Virtual Power Plant
- Utilities
- Smart Home
- Sustainability
- Electricity
website: https://www.ohmconnect.com
---
