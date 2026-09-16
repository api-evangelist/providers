---
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-09-15'
api_count: 1
apis:
- baseURL: https://api.agrology.ag/v2
  baseurl_source: declared
  description: The Agrology Public API v2 exposes site and node configuration, GeoJSON geometry, historical ground-truth sensor telemetry, historical and forecast weather service data, ML-derived synthetic microclim
  name: Agrology Public API v2
  slug: agrology-public-api-v2
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://agrology.ag
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/agrology/public-api-docs/blob/main/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/agrology/public-api-docs/blob/main/openapi.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agrology
- group: company
  title: ''
  type: Blog
  url: https://agrology.ag/blog
- group: operate
  title: ''
  type: Support
  url: https://agrology.ag/contact
- group: start
  title: ''
  type: Login
  url: https://grower.agrology.ag/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agrology.ag/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agrology.ag/privacy
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agrology/refs/heads/main/packages/agrology-packages.yml
  title: ''
  type: Packages
  url: packages/agrology-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrology/refs/heads/main/security/agrology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrology-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrology/refs/heads/main/llms/agrology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrology-llms.txt
created: '2026-09-13'
description: Agrology is a Delaware Public Benefit Corporation building a predictive agriculture platform for specialty crops, vineyards and regenerative row-crop operations. Its patented in-field sensor nodes capture ground-truth agronomic telemetry — soil moisture and tension, soil and air temperature, humidity, vapor pressure deficit, barometric pressure, total VOCs, CO2 and nitrous-oxide flux — and feed machine-learning models that produce microclimate predictions, synthetic metrics and threshold alerts for frost, extreme heat, irrigation and smoke taint. The company publishes a first-party Agrology Public API v2 (OpenAPI 3.0.1, 90 operations at https://api.agrology.ag/v2) from its own GitHub organization, covering site and node topology, GeoJSON geometry, historical ground-truth and weather data, microclimate and weather predictions, alerts, reports, dashboards, charts and field experiments.
image: https://avatars.githubusercontent.com/u/55110899?v=4
layout: provider
modified: '2026-09-13'
name: Agrology
nav: Providers
network: true
overview: 'Agrology publishes 1 API on the [APIs.io](https://apis.io/) network: Public API v2. Tagged areas include Company, Agriculture, AgTech, Climate, and Sensors.


  Agrology''s developer surface includes documentation, API reference, engineering blog, support, and 8 more developer resources.'
plans:
- name: Agrology Plans Pricing
  plan_count: 0
  slug: agrology-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Agrology Rate Limits
  slug: agrology-rate-limits
scopes:
- name: Agrology Scopes
  scope_count: 0
  slug: agrology-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 44.9
    developer_ergonomics: 37.5
    discoverability: 68.5
    operational_transparency: 5.3
  previous_composite: 32.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agrology Authentication
  slug: agrology-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Agrology Domain Security
  slug: agrology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agrology
tags:
- Company
- Agriculture
- AgTech
- Climate
- Sensors
- Internet of Things
- Weather
- Soil
- Carbon
- Predictive Analytics
- Geospatial
- Time Series
- Machine-Learning
- Viticulture
- Sustainability
- Environmental Monitoring
website: https://agrology.ag
---
