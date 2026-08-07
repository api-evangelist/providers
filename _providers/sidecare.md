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
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.sidecare.com/
- group: start
  title: ''
  type: Login
  url: https://www.sidecare.com/connexion-hub
- group: operate
  title: ''
  type: Support
  url: https://support.sidecare.com
- group: company
  title: ''
  type: Blog
  url: https://www.sidecare.com/articles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sidecare.com/cgu-rgpd
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sidecare.com/cgu-rgpd
- group: auth
  title: ''
  type: Authentication
  url: authentication/sidecare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sidecare-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.sidecare.com/.well-known/openid-configuration
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sidecare-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sidecare-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sidecare-domain-security.yml
created: '2026-07-17'
description: SideCare is a French insurtech and HR-benefits platform (operated by Hoggo) that helps companies build, deploy, and manage their employee health policy. It brokers and administers collective health insurance (mutuelle) and disability cover (prévoyance), comparing more than 15,500 contracts, and adds a free SIRH/HR and quality-of-life (QVT) layer, a digital clinic with telemedicine, and the SideCard prepaid health-expense card that advances up to €1,500/month. Over 7,800 companies and 100,000+ insured individuals use the platform. SideCare runs a "Sign in with SideCare" OpenID Connect identity provider and integrates with payroll/HRIS tools such as PayFit, Lucca, and Nibelis. Backed by Partech.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sidecare.png
layout: provider
modified: '2026-07-21'
name: SideCare
nav: Providers
network: true
overview: 'SideCare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Insurance, Insurtech, and Health Insurance.


  SideCare''s developer surface includes support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 41
scopes:
- name: Sidecare Scopes
  scope_count: 4
  slug: sidecare-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 61.1
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 24.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Sidecare Authentication
  slug: sidecare-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Sidecare Domain Security
  slug: sidecare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sidecare
tags:
- Company
- Financial Services
- Insurance
- Insurtech
- Health Insurance
- Employee Benefits
- Human Resources
- HRIS
- France
- OpenID Connect
website: https://www.sidecare.com/
---
