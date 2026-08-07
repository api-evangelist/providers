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
    consent_identity: true
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
  score: 15.3
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Weave's developer platform API for building apps and integrations against Weave communication, scheduling, and payments data. Authorized via OpenID Connect / OAuth 2.0 (authorization_code + client_cre
  name: Weave Platform API
  slug: weave-platform-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/weave-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getweave.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dp.getweave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dp.getweave.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://www.getweave.com/demo/
- group: start
  title: ''
  type: Login
  url: https://app.getweave.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getweave.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getweave.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getweave.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.weavehelp.com/weavehelp/
- group: company
  title: ''
  type: Blog
  url: https://www.getweave.com/resource-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weave-lab
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getweave.com/
- group: auth
  title: ''
  type: Security
  url: https://www.getweave.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.getweave.com/security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/weave-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/weave-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/weave-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/weave-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weave-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/weave-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/weave-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weave-llms.txt
created: '2026-07-17'
description: 'Weave (Weave Communications, Inc., NYSE: WEAV) is an all-in-one customer communication and payments platform built for small and medium healthcare and services businesses — dental, optometry, veterinary, medical, and beyond. Weave brings together a cloud phone system (VoIP), two-way text messaging, appointment scheduling and reminders, online reviews, forms, and integrated payments so practices can automate front-office work, keep schedules full, get paid faster, and collect more reviews. For developers, Weave runs a Developer Platform at dp.getweave.com backed by an OpenID Connect / OAuth 2.0 authorization server (api.weaveconnect.com) that lets partners build apps and integrations against Weave data and events. A Y Combinator company (W14), Weave is HIPAA compliant and maintains ISO 27001 and SOC 2 Type 2 attestations.'
image: https://dp.getweave.com/weave-favicon.svg
layout: provider
modified: '2026-07-21'
name: Weave
nav: Providers
network: true
overview: 'Weave publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communication, Messaging, Payments, and Healthcare.


  Weave''s developer surface includes documentation, signup flow, pricing, support, engineering blog, authentication, and 18 more developer resources.'
random_paper: 84
scopes:
- name: Weave Scopes
  scope_count: 3
  slug: weave-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 39.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 39.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Weave Authentication
  slug: weave-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Weave Domain Security
  slug: weave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Weave Vulnerability Disclosure
  slug: weave-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Weave Trust Center
  slug: weave-trust-center
  summary_line: HIPAA, ISO 27001, SOC 2 Type 2
slug: weave
tags:
- Company
- Communication
- Messaging
- Payments
- Healthcare
- VoIP
- Telephony
- Reviews
- Scheduling
- SMB
- Developer Platform
- OAuth
website: https://www.getweave.com/
---
