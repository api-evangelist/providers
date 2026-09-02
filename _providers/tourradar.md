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
    agentic_commerce: false
    auth_clarity: served
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
  score: 6.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Unified B2B API giving platforms, travel agencies, airlines, and GDSs access to TourRadar's network of 2,500+ organized adventure operators and 50,000+ experiences. Offered in three tiers - a Search &
  name: TourRadar Distribution API
  slug: distribution-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tourradar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tourradar.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.api.b2b.tourradar.com
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.api.b2b.tourradar.com/docs
- group: start
  title: ''
  type: Login
  url: https://dashboard.api.b2b.tourradar.com/signin
- group: operate
  title: ''
  type: Support
  url: https://customer.help.tourradar.com/wiki/spaces/CS/overview
- group: company
  title: ''
  type: Blog
  url: https://www.daystocome.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TourRadar
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tourradar.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tourradar.com/privacy
- group: company
  title: ''
  type: About
  url: https://www.tourradar.com/about
- group: auth
  title: ''
  type: Authentication
  url: authentication/tourradar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tourradar-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/tourradar-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tourradar-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tourradar-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tourradar-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tourradar-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/tourradar-components.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tourradar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tourradar.com/.well-known/security.txt
created: '2026-07-17'
description: TourRadar is the world's largest online marketplace for multi-day organized adventures, connecting travelers with more than 50,000 tours, safaris, and river cruises from over 2,500 vetted operators worldwide. Headquartered in Vienna, Austria, the company also operates a B2B Distribution API that lets OTAs, airlines, GDSs, and travel agencies search tour content and book departures through a unified API, alongside embeddable booking widgets and an affiliate program (RISE) for creators and publishers.
image: https://cdn.tourradar.com/s3/content-pages/391/1200x630/j705A8.png
layout: provider
modified: '2026-07-21'
name: TourRadar
nav: Providers
network: true
overview: 'TourRadar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Tours, Booking, Marketplace, and Adventure Travel.


  TourRadar''s developer surface includes documentation, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 14
scopes:
- name: Tourradar Scopes
  scope_count: 24
  slug: tourradar-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 20.1
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Tourradar Authentication
  slug: tourradar-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Tourradar Domain Security
  slug: tourradar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tourradar Vulnerability Disclosure
  slug: tourradar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tourradar
tags:
- Travel
- Tours
- Booking
- Marketplace
- Adventure Travel
- Distribution
- Affiliates
website: https://www.tourradar.com
---
