---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Authenticated REST surface of the Kevala platform, mounted at https://api.kevala.com/der/ and implemented with Django REST Framework. Kevala's September 2024 platform release notes describe a "DER Met
  name: Kevala Platform API — DER Metering
  slug: kevala-platform-api-der-metering
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kevala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kevala.com
- group: start
  title: ''
  type: SignUp
  url: https://www.kevala.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.kevala.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kevala.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kevala.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.kevala.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KevalaAnalytics
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.kevala.com/release-notes
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kevalaanalytics/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/kevalaanalytics
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kevala-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kevala-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kevala-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kevala-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kevala-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kevala-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kevala-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/kevala-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kevala-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kevala-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kevala-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kevala-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Kevala's DER service does publish an OpenAPI document and a ReDoc reference at https://api.kevala.com/der/openapi/ and /der/redoc/, but both return HTTP 403 "Authentication credentials were not provided." to anonymous callers, and the platform behind them is reachable only with an Auth0 token issued to an active subscription.
  evidence:
  - status: 403
    url: https://api.kevala.com/der/openapi/
  - status: 403
    url: https://api.kevala.com/der/redoc/
  - status: 403
    url: https://api.kevala.com/der/
  - status: 404
    url: https://www.kevala.com/llms.txt
  - status: 302
    url: https://app.kevala.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-23'
description: Kevala Inc. is a San Francisco based grid intelligence company, founded in 2014, that builds a cloud-based electric-grid data and analytics platform for utilities, regulators and government agencies, renewable energy developers, and transportation electrification planners. The platform merges address-specific geospatial data, utility network models and hyper-granular time-series data into map-based analytics for integrated grid planning, distributed energy resource (DER) adoption forecasting, project siting, power flow analysis, locational carbon accounting, production cost modeling, and predictive interconnection siting metrics, with exports compatible with CYME, Synergi, PSS/E and OpenDSS. Kevala licenses its data and analysis by subscription and operates an authenticated platform API at api.kevala.com; the DER metering surface publishes an OpenAPI document and a ReDoc reference, but both require platform credentials and no public developer portal, API reference or machine-readable
  specification is served anonymously.
image: https://cdn.prod.website-files.com/62a236e9692c48e1d16898b3/6359863c0193ad9598083d1c_kevala-logo-copy.png
layout: provider
modified: '2026-08-23'
name: Kevala
nav: Providers
network: true
overview: 'Kevala publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Electric Grid, and Grid Analytics.


  Kevala''s developer surface includes signup flow, engineering blog, release notes, changelog, authentication, and 18 more developer resources.'
plans:
- name: Kevala Plans Pricing
  plan_count: 0
  slug: kevala-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Kevala Rate Limits
  slug: kevala-rate-limits
scopes:
- name: Kevala Scopes
  scope_count: 0
  slug: kevala-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 30.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Kevala Authentication
  slug: kevala-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Kevala Domain Security
  slug: kevala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kevala
tags:
- Company
- Energy
- Electricity
- Electric Grid
- Grid Analytics
- Distributed Energy Resources
- Utilities
- Geospatial
- Analytics
- Carbon Accounting
- Electric Vehicles
- Sustainability
website: https://www.kevala.com
---
