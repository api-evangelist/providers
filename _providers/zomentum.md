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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for the Zomentum revenue platform, documented as public Postman documentation. Uses Bearer token authentication (Auth0-issued access and refresh tokens) via an API User provisioned in the das
  name: Zomentum API
  slug: zomentum-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://zomentum.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.zomentum.com
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.zomentum.com
- group: build
  title: ''
  type: Postman
  url: https://api-docs.zomentum.com
- group: start
  title: ''
  type: GettingStarted
  url: https://help.zomentum.com/support/solutions/articles/44002337023-generating-an-api-user
- group: operate
  title: ''
  type: Support
  url: https://help.zomentum.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.zomentum.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zomentum.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accounts.zomentum.com/
- group: start
  title: ''
  type: Login
  url: https://accounts.zomentum.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zomentum.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zomentum.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zomentum.com
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.zomentum.com
- group: auth
  title: ''
  type: Security
  url: https://www.zomentum.com/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/zomentum-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zomentum-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zomentum-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zomentum-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zomentum-llms.txt
created: '2026-07-17'
description: Zomentum is an AI-powered revenue platform built for managed service providers (MSPs) and IT service businesses, unifying proposal and quote creation, contracts and e-signatures, an MSP-focused CRM, workflow automation, and integrated payment collection into a single "Turn Every Proposal Into Revenue" workflow. Founded in 2018 (legal entity Pactora Inc) and headquartered in San Francisco, Zomentum connects to 50+ PSA, accounting, and distributor systems — including Autotask, ConnectWise Manage, HaloPSA, Syncro, QuickBooks, and Xero — and exposes a REST API, documented via Postman at api-docs.zomentum.com and served from api.zomentum.com, that uses Bearer token authentication (Auth0-issued access and refresh tokens) provisioned through an API User in the dashboard and available on the Growth plan.
image: https://www.zomentum.com/wp-content/uploads/2019/09/Logo_Color_Black.png
layout: provider
modified: '2026-07-21'
name: Zomentum
nav: Providers
network: true
overview: 'Zomentum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, MSP, CRM, and Sales.


  Zomentum''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 31.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Zomentum Authentication
  slug: zomentum-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Zomentum Domain Security
  slug: zomentum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zomentum Vulnerability Disclosure
  slug: zomentum-vulnerability-disclosure
  summary_line: disclosure policy published
slug: zomentum
tags:
- Company
- Enterprise
- MSP
- CRM
- Sales
- Proposals
- Payments
- Revenue Platform
- PSA Integration
website: https://zomentum.com
---
