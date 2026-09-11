---
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
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-09-10'
api_count: 1
apis:
- baseURL: https://api.aedifion.io
  baseurl_source: declared
  description: 'Versioned REST API (v2) for the aedifion.io building operations platform. Covers company, realm, project and user administration; datapoint and timeseries read/write; virtual datapoints; the semantic '
  name: aedifion HTTP API
  slug: aedifion-http-api
- baseURL: mqtts://mqtt.aedifion.io:8883
  baseurl_source: declared
  description: MQTT 3.1.1 broker interface at mqtt.aedifion.io for streaming building telemetry into and out of the aedifion.io platform. TLS-only (ports 8883 for native MQTT, 9001 for MQTT over WebSockets), usernam
  name: aedifion MQTT API
  slug: aedifion-mqtt-api
artifact_total: 10
asyncapis:
- description: ''
  name: Aedifion Event Surface
  slug: aedifion-event-surface
- description: Event-driven interface to the aedifion.io building operations platform. The broker carries three topic families - building timeseries observations, semantic metadata, and control commands - namespaced
  name: aedifion MQTT API
  slug: aedifion-mqtt-asyncapi
common:
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
  title: ''
  type: OpenAPI
  url: openapi/aedifion-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/aedifion-mqtt-asyncapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aedifion-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aedifion-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aedifion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aedifion-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aedifion-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aedifion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aedifion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aedifion-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aedifion-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aedifion-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aedifion-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aedifion-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aedifion-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aedifion-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/aedifion-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aedifion-http-api-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aedifion-trust-center.yml
- group: start
  title: ''
  type: Console
  url: https://api.aedifion.io/ui/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aedifion-event-surface.yml
- group: design
  title: ''
  type: Components
  url: components/aedifion-components.yml
created: '2026-09-09'
description: aedifion GmbH is a Cologne-based PropTech founded in 2017 that operates a vendor-neutral, patented cloud platform for the optimized operation of non-residential buildings. The platform ingests real-time operating data from all building trades via plug-and-play edge devices, applies analytics and AI to detect faults and inefficiencies, and autonomously controls HVAC and building services based on weather forecasts, occupancy and electricity prices - cutting energy use, CO2 emissions and operating costs by up to 40% without structural retrofits. Products span aedifion.io (connectivity and monitoring), aedifion.analytics, aedifion.controls, aedifion.dynamics (demand-side management) and aedifion.smartkit. Developers get a documented HTTP API (OpenAPI 3.0, 208 operations across projects, datapoints, timeseries, analytics, controls, alerts and tasks), an MQTT broker and a Kafka interface for streaming building telemetry. The company serves owners, operators and asset managers of
  commercial real estate and supports decarbonization, ESG reporting and DGNB, ISO 50001 and GEG certification.
image: https://cdn.prod.website-files.com/6942a43e5bcce46ebe9f73a1/6942a43e5bcce46ebe9f7529_65f998eafa61f2995943d60d_favicon-32x32.png
layout: provider
modified: '2026-09-09'
name: Aedifion
nav: Providers
network: true
overview: 'Aedifion publishes 2 APIs on the [APIs.io](https://apis.io/) network: HTTP API and MQTT API. Tagged areas include Building Automation, Smart Buildings, Energy Management, Internet of Things, and Real Estate.


  The Aedifion catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Aedifion''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 32 more developer resources.'
plans:
- name: Aedifion Plans Pricing
  plan_count: 3
  slug: aedifion-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Aedifion Rate Limits
  slug: aedifion-rate-limits
scopes:
- name: Aedifion Scopes
  scope_count: 13
  slug: aedifion-scopes
  summary_line: 13 scopes · implicit/authorizationCode/password/clientCredentials
score:
  band: strong
  composite: 65.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 55.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 63.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: true
    score: 11.1
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
slug: aedifion
tags:
- Building Automation
- Smart Buildings
- Energy Management
- Internet of Things
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
website: https://www.aedifion.com/
---
