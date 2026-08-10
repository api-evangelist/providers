---
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
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Recuro Health's member and provider identity surface, an Auth0-hosted OpenID Connect / OAuth 2.0 authorization server. The OIDC discovery document, the RFC 8414 authorization-server metadata and the J
  name: Recuro Health Identity (OpenID Connect)
  slug: recuro-health-identity-openid-connect
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://recurohealth.com/
- group: company
  title: ''
  type: Blog
  url: https://recurohealth.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://recurohealth.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://recurohealth.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://member.recurohealth.com/
- group: start
  title: ''
  type: Login
  url: https://member.recurohealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recurohealth.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recurohealth.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recurohealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recuro-health
- group: auth
  title: ''
  type: Compliance
  url: https://recurohealth.com/hitrust/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/recuro-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/recuro-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/recuro-health-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/recuro-health-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/recuro-health-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recuro-health-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/recuro-health-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recuro-health-llms.txt
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/recuro-health_stock/
coverage:
  checked: '2026-08-05'
  detail: Recuro Health runs a real but entirely private developer surface — docs.recurohealth.com is a GitHub Pages site that 302s to a GitHub login, developer.recurohealth.com is CNAMEd to a ReadMe hub that returns 404, and api.recurohealth.com answers every path with a zero-length 404 — so the only machine-readable contract reachable without credentials is the Auth0 OpenID Connect discovery document at auth.recurohealth.com.
  evidence:
  - status: 302
    url: https://docs.recurohealth.com/
  - status: 404
    url: https://developer.recurohealth.com/
  - status: 404
    url: https://api.recurohealth.com/openapi.json
  - status: 200
    url: https://auth.recurohealth.com/.well-known/openid-configuration
  reason: partner-login
  state: gated
created: '2026-08-05'
description: 'Recuro Health is an integrated digital health company operating a virtual-first care delivery platform — a "Digital Medical Home" — sold to employers, health plans, TPAs and diagnostics companies rather than to individual developers. Its configurable SaaS platform bundles core virtual care services (virtual primary care, virtual urgent care, virtual behavioral health) with supplemental benefits including on-demand counseling, pediatric behavioral health, health advocacy, prescription benefit, wellness programs and virtual MSK therapy, plus at-home lab and genomic diagnostics. Members reach care through the Recuro Care iOS/Android apps and the member.recurohealth.com web app, with identity handled by an Auth0-hosted OpenID Connect authorization server at auth.recurohealth.com. Recuro Health is HITRUST certified and absorbed WellVia Solutions. The company markets platform integration (SSO, APIs, eligibility and reporting) to its enterprise clients, but publishes no public developer
  program: its documentation host requires a GitHub login and its ReadMe developer hub is not publicly served.'
image: https://recurohealth.com/wp-content/uploads/2023/11/Logo-RecuroHealth.png
layout: provider
modified: '2026-08-05'
name: Recuro Health
nav: Providers
network: true
overview: 'Recuro Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telehealth, and Virtual Care.


  Recuro Health''s developer surface includes engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 55
scopes:
- name: Recuro Health Scopes
  scope_count: 14
  slug: recuro-health-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 29.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Recuro Health Authentication
  slug: recuro-health-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Recuro Health Domain Security
  slug: recuro-health-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Recuro Health Trust Center
  slug: recuro-health-trust-center
  summary_line: HITRUST CSF, HIPAA
slug: recuro-health
tags:
- Company
- Health
- Healthcare
- Telehealth
- Virtual Care
- Digital Health
- Behavioral Health
- Primary Care
- Employee Benefits
- Health Plans
- Identity
- OpenID Connect
website: https://recurohealth.com/
---
