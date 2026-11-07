---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://spectrumoutage.us/api/v1
  baseurl_source: declared
  description: City, state, and ZIP lookup
  name: SpectrumOutage API Locations API
  slug: spectrumoutage-api-locations-api
- baseURL: https://spectrumoutage.us/api/v1
  baseurl_source: declared
  description: Map pin and cluster data
  name: SpectrumOutage API Map API
  slug: spectrumoutage-api-map-api
- baseURL: https://spectrumoutage.us/api/v1
  baseurl_source: declared
  description: Outage report listing and submission
  name: SpectrumOutage API Reports API
  slug: spectrumoutage-api-reports-api
- baseURL: https://spectrumoutage.us/api/v1
  baseurl_source: declared
  description: Dashboard and aggregate statistics
  name: SpectrumOutage API Stats API
  slug: spectrumoutage-api-stats-api
artifact_total: 14
collections:
- collection_type: open
  name: SpectrumOutage API
  slug: open-spectrumoutage-api
common:
- group: company
  title: ''
  type: Blog
  url: https://spectrumoutage.us/blog
- group: company
  title: ''
  type: Website
  url: https://www.spectrumoutage.us/
- group: agent
  href: https://artifacts.apis.io/spectrumoutage-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/spectrumoutage-api/overlays/spectrumoutage-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/spectrumoutage-api-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/spectrumoutage-api/security/spectrumoutage-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spectrumoutage-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/spectrumoutage-api/authentication/spectrumoutage-api-authentication.yml
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
  href: https://artifacts.apis.io/spectrumoutage-api/changelog/spectrumoutage-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/spectrumoutage-api-changelog.yml
- group: design
  href: https://artifacts.apis.io/spectrumoutage-api/conventions/spectrumoutage-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/spectrumoutage-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/spectrumoutage-api/errors/spectrumoutage-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spectrumoutage-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spectrumoutage-api/lifecycle/spectrumoutage-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/spectrumoutage-api-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/spectrumoutage-api/conformance/spectrumoutage-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spectrumoutage-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/spectrumoutage-api/data-model/spectrumoutage-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/spectrumoutage-api-data-model.yml
- group: operate
  href: https://artifacts.apis.io/spectrumoutage-api/rate-limits/spectrumoutage-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/spectrumoutage-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/spectrumoutage-api/plans/spectrumoutage-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/spectrumoutage-api-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/spectrumoutage-api/packages/spectrumoutage-api-packages.yml
  title: ''
  type: Packages
  url: packages/spectrumoutage-api-packages.yml
created: '2026-07-17'
description: 'Community-powered REST API for live Spectrum internet, TV, and phone outage data across the United States, published by SpectrumOutage.us — an independent outage tracker with no affiliation to Charter Communications or Spectrum. The v1 API exposes eight operations over crowdsourced outage reports: national dashboard statistics with an hourly timeline and service breakdown, a paginated report feed, outage submission, city and state lookups by slug, ZIP-code status (issues_reported / all_clear) with the reports behind it, and map pin/cluster data over a 1h, 24h or 48h window. Access is a bearer API key issued manually by email, or through a free RapidAPI plan; the provider also publishes an OpenAPI 3.0.3 specification, an agent-facing llm.txt on both hosts, a Postman collection, and an open outage dataset mirrored to GitHub, Hugging Face, Kaggle and Figshare.'
finops:
- has_sources: true
  method: derived
  name: Spectrumoutage Api Finops
  primary_unit: subscription
  service_category: ''
  slug: spectrumoutage-api-finops
  template: false
image: https://spectrumoutage.us/icons/icon-192.png
layout: provider
modified: '2026-10-06'
name: SpectrumOutage API
nav: Providers
network: true
overview: 'SpectrumOutage API publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Locations API, Map API, Reports API, and 1 more. Tagged areas include Spectrum, Outage, Internet, TV, and Phone.


  The SpectrumOutage API catalog on APIs.io includes 1 Spectral governance ruleset.


  SpectrumOutage API''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, support, pricing, and 21 more developer resources.'
plans:
- name: Spectrumoutage Api Plans Pricing
  plan_count: 1
  slug: spectrumoutage-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Spectrumoutage Api Rate Limits
  slug: spectrumoutage-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: SpectrumOutage API API Rules
  rule_count: 64
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 1
  slug: spectrumoutage-api-rules
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 60.5
    catalog_earned_first_party: 16.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 57.7
    developer_ergonomics: 57.7
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 51.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/spectrumoutage-api/spectrumoutage-api-2026-08-17T082021.png
security:
- kind: authentication
  name: Spectrumoutage Api Authentication
  slug: spectrumoutage-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spectrumoutage Api Domain Security
  slug: spectrumoutage-api-domain-security
  summary_line: TLSv1.2
skill_count: 3
skills:
- name: Check Spectrum outage status for a location
  slug: spectrumoutage-api-check-outage-status
- name: Map and trend Spectrum outage activity
  slug: spectrumoutage-api-map-outage-activity
- name: Submit a Spectrum outage report
  slug: spectrumoutage-api-submit-outage-report
slug: spectrumoutage-api
tags:
- Spectrum
- Outage
- Internet
- TV
- Phone
- Monitoring
- Status
- ZIP Code
- Telecommunications
- ISP
- Network Status
- Crowdsourced
website: https://www.spectrumoutage.us/
---
