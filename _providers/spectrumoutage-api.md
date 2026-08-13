---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: REST API for live Spectrum internet, TV, and phone outage data across the US. Bearer API key required on all endpoints. Endpoints include /stats, /reports, /cities/{slug}, /states, /zip/{zip}, and /ma
  name: SpectrumOutage API v1
  slug: spectrumoutage-api-v1
artifact_total: 5
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/spectrumoutage-api-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spectrumoutage-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spectrumoutage-api-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.spectrumoutage.us
- group: docs
  title: ''
  type: Documentation
  url: https://api.spectrumoutage.us
- group: docs
  title: ''
  type: APIReference
  url: https://api.spectrumoutage.us
- group: start
  title: ''
  type: GettingStarted
  url: https://api.spectrumoutage.us/#introduction
- group: operate
  title: ''
  type: Support
  url: https://spectrumoutage.us/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usspectrumoutage-us
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/usspectrumoutage-us/spectrum-outage-api
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/56702125/2sBY4PMzPS
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/usspectrumoutageus/api/spectrumoutage
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spectrumoutage.us/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spectrumoutage.us/privacy-policy
- group: commercial
  title: ''
  type: License
  url: https://spectrumoutage.us/disclaimer
- group: operate
  title: ''
  type: ChangeLog
  url: https://spectrumoutage.us/support-us
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spectrumoutage-api-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spectrumoutage-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spectrumoutage-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spectrumoutage-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spectrumoutage-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spectrumoutage-api-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spectrumoutage-api-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spectrumoutage-api-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/spectrumoutage-api-packages.yml
created: '2026-07-17'
description: 'Community-powered REST API for live Spectrum internet, TV, and phone outage data across the United States, published by SpectrumOutage.us — an independent outage tracker with no affiliation to Charter Communications or Spectrum. The v1 API exposes eight operations over crowdsourced outage reports: national dashboard statistics with an hourly timeline and service breakdown, a paginated report feed, outage submission, city and state lookups by slug, ZIP-code status (issues_reported / all_clear) with the reports behind it, and map pin/cluster data over a 1h, 24h or 48h window. Access is a bearer API key issued manually by email, or through a free RapidAPI plan; the provider also publishes an OpenAPI 3.0.3 specification, an agent-facing llm.txt on both hosts, a Postman collection, and an open outage dataset mirrored to GitHub, Hugging Face, Kaggle and Figshare.'
image: https://spectrumoutage.us/icons/icon-192.png
layout: provider
modified: '2026-08-11'
name: SpectrumOutage API
nav: Providers
network: true
overview: 'SpectrumOutage API publishes 1 API on the [APIs.io](https://apis.io/) network: v1. Tagged areas include spectrum, outage, internet, tv, and phone.


  SpectrumOutage API''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, changelog, and 19 more developer resources.'
plans:
- name: Spectrumoutage Api Plans Pricing
  plan_count: 1
  slug: spectrumoutage-api-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 1
  name: Spectrumoutage Api Rate Limits
  slug: spectrumoutage-api-rate-limits
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 32.3
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 42.1
  previous_composite: 44.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Spectrumoutage Api Authentication
  slug: spectrumoutage-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spectrumoutage Api Domain Security
  slug: spectrumoutage-api-domain-security
  summary_line: TLSv1.2
slug: spectrumoutage-api
tags:
- spectrum
- outage
- internet
- tv
- phone
- monitoring
- status
- zip-code
- telecom
- isp
- network-status
- crowdsourced
website: https://api.spectrumoutage.us
---
