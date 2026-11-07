---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: mqtts://mqtt.aedifion.io:8883
  baseurl_source: declared
  description: MQTT 3.1.1 broker interface at mqtt.aedifion.io for streaming building telemetry into and out of the aedifion.io platform. TLS-only (ports 8883 for native MQTT, 9001 for MQTT over WebSockets), usernam
  name: aedifion MQTT API
  slug: aedifion-mqtt-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing AI related resources.
  name: Aedifion AI API
  slug: aedifion-ai-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing alerts and related resources.
  name: Aedifion Alert API
  slug: aedifion-alert-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing analytics and related resources.
  name: Aedifion Analytics API
  slug: aedifion-analytics-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing companies and related resources.
  name: Aedifion Company API
  slug: aedifion-company-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing components and related resources.
  name: Aedifion Component API
  slug: aedifion-component-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing controls apps and related resources.
  name: Aedifion Controls API
  slug: aedifion-controls-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing datapoints and related resources.
  name: Aedifion Datapoint API
  slug: aedifion-datapoint-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Meta management resources.
  name: Aedifion Meta API
  slug: aedifion-meta-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing projects and related resources.
  name: Aedifion Project API
  slug: aedifion-project-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Accessing realm-level resources.
  name: Aedifion Realm API
  slug: aedifion-realm-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing tasks and related resources.
  name: Aedifion Task API
  slug: aedifion-task-api
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: Creating, modifying, and accessing users and related resources.
  name: Aedifion User API
  slug: aedifion-user-api
- baseURL: mqtts://mqtt.aedifion.io:8883
  baseurl_source: declared
  description: The Time Series API from Aedifion — 2 operation(s) for time series.
  name: Aedifion Time Series API
  slug: aedifion-time-series-api
artifact_total: 30
asyncapis:
- description: ''
  name: Aedifion Event Surface
  slug: aedifion-event-surface
- description: Event-driven interface to the aedifion.io building operations platform. The broker carries three topic families - building timeseries observations, semantic metadata, and control commands - namespaced
  name: aedifion MQTT API
  slug: aedifion-mqtt-asyncapi
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.aedifion.io/en/products/io/quota/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aedifion.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/aedifion/capabilities/aedifion-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aedifion-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.aedifion.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aedifion.io/en/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aedifion.io/en/
- group: docs
  title: ''
  type: APIReference
  url: https://api.aedifion.io/ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aedifion.io/en/developers/http-api/
- group: operate
  title: ''
  type: Support
  url: https://www.aedifion.com/kontakt
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.aedifion.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.aedifion.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aedifion
- group: start
  title: ''
  type: SignUp
  url: https://www.aedifion.io/login
- group: start
  title: ''
  type: Login
  url: https://www.aedifion.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aedifion.com/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aedifion.com/datenschutz
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aedifion.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aedifion.io/en/changelog/
- group: auth
  title: ''
  type: Compliance
  url: https://www.aedifion.com/sicherheit
- group: docs
  href: https://artifacts.apis.io/aedifion/openapi/_original/aedifion-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/aedifion-openapi.yml
- group: docs
  href: https://artifacts.apis.io/aedifion/asyncapi/aedifion-mqtt-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/aedifion-mqtt-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/aedifion/llms/aedifion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aedifion-llms.txt
- group: agent
  href: https://artifacts.apis.io/aedifion/well-known/aedifion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aedifion-well-known.yml
- group: auth
  href: https://artifacts.apis.io/aedifion/authentication/aedifion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aedifion-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aedifion/scopes/aedifion-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aedifion-scopes.yml
- group: design
  href: https://artifacts.apis.io/aedifion/conventions/aedifion-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aedifion-conventions.yml
- group: design
  href: https://artifacts.apis.io/aedifion/conventions/aedifion-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aedifion-conventions.yml
- group: design
  href: https://artifacts.apis.io/aedifion/errors/aedifion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aedifion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aedifion/lifecycle/aedifion-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aedifion-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aedifion/conformance/aedifion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aedifion-conformance.yml
- group: auth
  href: https://artifacts.apis.io/aedifion/security/aedifion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aedifion-domain-security.yml
- group: design
  href: https://artifacts.apis.io/aedifion/data-model/aedifion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aedifion-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aedifion/changelog/aedifion-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aedifion-changelog.yml
- group: operate
  href: https://artifacts.apis.io/aedifion/rate-limits/aedifion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aedifion-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aedifion/plans/aedifion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aedifion-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/aedifion/packages/aedifion-packages.yml
  title: ''
  type: Packages
  url: packages/aedifion-packages.yml
- group: agent
  href: https://artifacts.apis.io/aedifion/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/aedifion/overlays/aedifion-http-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aedifion-http-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/aedifion/security/aedifion-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aedifion-trust-center.yml
- group: start
  title: ''
  type: Console
  url: https://api.aedifion.io/ui/
- group: design
  href: https://artifacts.apis.io/aedifion/asyncapi/aedifion-event-surface.yml
  title: ''
  type: Webhooks
  url: asyncapi/aedifion-event-surface.yml
- group: design
  href: https://artifacts.apis.io/aedifion/components/aedifion-components.yml
  title: ''
  type: Components
  url: components/aedifion-components.yml
created: '2026-09-09'
description: aedifion GmbH is a Cologne-based PropTech founded in 2017 that operates a vendor-neutral, patented cloud platform for the optimized operation of non-residential buildings. The platform ingests real-time operating data from all building trades via plug-and-play edge devices, applies analytics and AI to detect faults and inefficiencies, and autonomously controls HVAC and building services based on weather forecasts, occupancy and electricity prices - cutting energy use, CO2 emissions and operating costs by up to 40% without structural retrofits. Products span aedifion.io (connectivity and monitoring), aedifion.analytics, aedifion.controls, aedifion.dynamics (demand-side management) and aedifion.smartkit. Developers get a documented HTTP API (OpenAPI 3.0, 208 operations across projects, datapoints, timeseries, analytics, controls, alerts and tasks), an MQTT broker and a Kafka interface for streaming building telemetry. The company serves owners, operators and asset managers of
  commercial real estate and supports decarbonization, ESG reporting and DGNB, ISO 50001 and GEG certification.
finops:
- has_sources: true
  method: derived
  name: Aedifion Finops
  primary_unit: ''
  service_category: ''
  slug: aedifion-finops
  template: true
image: https://cdn.prod.website-files.com/6942a43e5bcce46ebe9f73a1/6942a43e5bcce46ebe9f7529_65f998eafa61f2995943d60d_favicon-32x32.png
layout: provider
modified: '2026-10-06'
name: Aedifion
nav: Providers
network: true
overview: 'Aedifion publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including MQTT API, AI API, Alert API, and 11 more. Tagged areas include Building Automation, Smart Buildings, Energy Management, IoT, and Real Estate.


  The Aedifion catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Aedifion''s developer surface includes pricing, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 35 more developer resources.'
plans:
- name: Aedifion Plans Pricing
  plan_count: 0
  slug: aedifion-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Aedifion Rate Limits
  slug: aedifion-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Aedifion API Rules
  rule_count: 60
  severity_counts:
    error: 37
    hint: 0
    info: 3
    warn: 20
  slug: aedifion-rules
scopes:
- name: Aedifion Scopes
  scope_count: 13
  slug: aedifion-scopes
  summary_line: 13 scopes · implicit/authorizationCode/password/clientCredentials
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 59.2
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 60.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 38.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/aedifion/aedifion-2026-10-11T092907.png
security:
- kind: authentication
  name: Aedifion Authentication
  slug: aedifion-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Aedifion Domain Security
  slug: aedifion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aedifion Trust Center
  slug: aedifion-trust-center
  summary_line: DIN EN ISO/IEC 27001, GDPR / DSGVO
skill_count: 6
skills:
- name: Configure alerts and notification channels
  slug: aedifion-alerts-and-monitoring
- name: Run analytics and act on optimization findings
  slug: aedifion-analytics-and-tasks
- name: Authenticate and discover a building
  slug: aedifion-authenticate-and-discover
- name: Deploy and supervise autonomous controls apps
  slug: aedifion-controls-apps
- name: Read and import building timeseries
  slug: aedifion-read-timeseries
- name: Write a setpoint to building equipment safely
  slug: aedifion-write-setpoint-safely
slug: aedifion
tags:
- Building Automation
- Smart Buildings
- Energy Management
- IoT
- Real Estate
- HVAC
- Sustainability
- Time Series
- Analytics
- MQTT
- Building Operations
- ESG
- PropTech
- Germany
- Real-Time
website: https://www.aedifion.com/
---
