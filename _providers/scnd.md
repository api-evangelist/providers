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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.scnd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://features.scnd.com/
- group: docs
  title: ''
  type: APIReference
  url: https://features.scnd.com/v2.0/superadmin/oauth
- group: company
  title: ''
  type: Blog
  url: https://www.scnd.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.scnd.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.scnd.com/booking-engine-marketplace-specialist
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scnd.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scnd-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scnd-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scnd-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/scnd-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scnd-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/scnd-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/scnd-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scnd-conventions.yml
created: '2026-07-17'
description: Second (scnd) is a France-based SaaS platform for launching and scaling online service marketplaces, partner-discovery networks, and service-procurement solutions. Evolved from the open-source Cocorico marketplace project, Second helps companies buy, sell, and manage services online with native calendaring (when services are available), geolocation and geofencing (where services are available), and vendor management (with whom services are available). The platform covers KYC/KYB, escrow, pay-in and payouts, split payments, dynamic pricing and yield management, AI-driven search and vendor matching, and a headless, composable, RESTful API-driven architecture. It powers marketplaces for customers such as Accor, Allianz, Intersport, Siemens Energy, and Suez across dozens of countries, and is SOC 2 Type 2, ISO 27001, and GDPR compliant. Backed by Partech and 42CAP (EUR 4M raise).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scnd.png
layout: provider
modified: '2026-07-21'
name: Second (scnd)
nav: Providers
network: true
overview: 'Second (scnd) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Services, Vendor Management, and Payments.


  Second (scnd)''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, and 9 more developer resources.'
random_paper: 16
scopes:
- name: Scnd Scopes
  scope_count: 2
  slug: scnd-scopes
  summary_line: 2 scopes · clientCredentials/password/authorizationCode
score:
  band: emerging
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 28.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Scnd Authentication
  slug: scnd-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Scnd Domain Security
  slug: scnd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: scnd
tags:
- Company
- Marketplace
- Services
- Vendor Management
- Payments
- OAuth
- SaaS
- Procurement
website: https://www.scnd.com/
---
