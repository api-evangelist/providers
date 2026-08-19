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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for the Mosyle Business Apple device management platform. Requests are POSTed to operation endpoints under https://businessapi.mosyle.com/v1 (e.g. listdevices, listusers) with a JSON body and
  name: Mosyle Business API
  slug: mosyle-business-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mosyle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mosyle.com/
- group: start
  title: ''
  type: Portal
  url: https://business.mosyle.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://business.mosyle.com/#pricing
- group: company
  title: ''
  type: Blog
  url: https://business.mosyle.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://mybusiness.mosyle.com/signup/
- group: start
  title: ''
  type: Login
  url: https://mybusiness.mosyle.com/
- group: operate
  title: ''
  type: Support
  url: https://business.mosyle.com/#support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mosyle.com/
- group: auth
  title: ''
  type: Compliance
  url: https://business.mosyle.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/mosyle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mosyle-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mosyle-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mosyle-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mosyle-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mosyle-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/mosyle-packages.yml
created: '2026-07-17'
description: Mosyle is an Apple-focused unified endpoint management and endpoint security company that helps organizations deploy, manage, and protect Mac, iPhone, iPad, Apple TV, Apple Watch, and Vision Pro devices at work. Its cloud-native platform combines enterprise-grade Apple MDM, next-generation endpoint security (automated hardening & compliance, purpose-built Mac antivirus, AI-based automated Zero Trust, and Admin On-Demand privilege management), Apple-specific encrypted-DNS online privacy & security, macOS identity management & SSO (Mosyle Auth 2), and best-in-market apps & patch management. The Mosyle Business REST API (businessapi.mosyle.com/v1) lets IT teams programmatically query and act on managed devices and users using an accessToken (JWT) credential. Mosyle serves 65,000+ organizations worldwide.
image: https://business.mosyle.com/images/logos/mosyle_logo.png
layout: provider
modified: '2026-07-20'
name: Mosyle
nav: Providers
network: true
overview: 'Mosyle publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Apple, Device Management, MDM, and Endpoint Security.


  Mosyle''s developer surface includes developer portal, pricing, engineering blog, signup flow, support, authentication, and 11 more developer resources.'
random_paper: 69
score:
  band: emerging
  composite: 21.6
  delta: -1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 23.5
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mosyle/refs/heads/main/screenshots/mosyle-2026-08-07T184321.png
security:
- kind: authentication
  name: Mosyle Authentication
  slug: mosyle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mosyle Domain Security
  slug: mosyle-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Mosyle Trust Center
  slug: mosyle-trust-center
  summary_line: SOC 2 Type II
slug: mosyle
tags:
- Company
- Apple
- Device Management
- MDM
- Endpoint Security
- Identity
- SSO
- macOS
- iOS
- IT Operations
- Security
website: https://mosyle.com/
---
