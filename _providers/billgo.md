---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The GraphQL API behind the BillGO Exchange biller portal. A live graphql-java server answers POST requests at https://exchange.billgo.com/graphql; schema introspection is disabled by the server, so no
  name: BillGO Exchange GraphQL API
  slug: billgo-exchange-graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/billgo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/billgo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billgo.com/
- group: company
  title: ''
  type: Blog
  url: https://billgo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://billgo.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://start.billgo.com/
- group: start
  title: ''
  type: Login
  url: https://exchange.billgo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://billgo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://billgo.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://billgo.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://billgo.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://billgo.statuspage.io/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/billgo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/billgo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/billgo-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/billgo-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/billgo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/billgo-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/billgo-llms.txt
coverage:
  checked: '2026-08-07'
  detail: docs.billgo.com — the only BillGO developer reference — is a private ReadMe project that answers every path, including /reference and /openapi.json, with an HTTP 302 to https://dash.readme.com/to/billgo-group, so no contract, endpoint list or auth guide is readable without a BillGO account; the live GraphQL endpoint at exchange.billgo.com/graphql confirms the API exists but returns "Introspection has been disabled for this request".
  evidence:
  - status: 302
    url: https://docs.billgo.com/reference
  - status: 302
    url: https://docs.billgo.com/openapi.json
  - status: 200
    url: https://exchange.billgo.com/graphql
  - status: 404
    url: https://billgo.com/developers
  reason: partner-login
  state: gated
created: '2026-08-07'
description: BillGO is a Fort Collins, Colorado bill-payment technology company founded in 2015 that operates a real-time payments network connecting financial institutions, fintechs and billers. Its BillGO Exchange platform lets billers of any size receive electronic payments over ACH and one-time-use virtual cards instead of paper checks, and lets banks and credit unions embed real-time bill pay into their own applications. The Exchange web application at exchange.billgo.com is driven by a live GraphQL API with Okta-hosted OpenID Connect sign-in; the developer reference at docs.billgo.com is a private ReadMe project that redirects anonymous visitors to a login.
image: https://billgo.com/hubfs/raw_assets/public/Billgo_January2023/images/Logo_Deep_Full.svg
layout: provider
modified: '2026-08-07'
name: BillGO
nav: Providers
network: true
overview: 'BillGO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Bill Pay, Financial-Services, Banking, and ACH.


  BillGO''s developer surface includes engineering blog, support, signup flow, authentication, and 15 more developer resources.'
random_paper: 3
scopes:
- name: Billgo Scopes
  scope_count: 8
  slug: billgo-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 29.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/billgo/refs/heads/main/screenshots/billgo-2026-08-07T162429.png
security:
- kind: authentication
  name: Billgo Authentication
  slug: billgo-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Billgo Domain Security
  slug: billgo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Billgo Trust Center
  slug: billgo-trust-center
  summary_line: SOC 2 Type II, SOC 1 Type I, PCI DSS Level 1 (via service providers)
slug: billgo
tags:
- Payments
- Bill Pay
- Financial-Services
- Banking
- ACH
- Virtual Cards
- Fintech
- GraphQL
website: https://billgo.com/
---
