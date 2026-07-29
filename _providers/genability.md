---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Genability Agentic Access
  operation_count: 33
  slug: genability-agentic-access
  summary_line: 33 operations · 3 acting
api_count: 14
apis:
- description: 'Search and retrieve North American electricity tariffs, including rate structures, applicability properties, documents and the effective-dated history of a master tariff. The list endpoint exposes 33 '
  name: Genability Signal Tariff API
  slug: genability-signal-tariff-api
- description: List and retrieve Load Serving Entities (LSEs) — the investor-owned utilities, municipal utilities and cooperatives that serve electricity across the USA, Canada and Mexico — searchable by postal code
  name: Genability Signal Load Serving Entity API
  slug: genability-signal-load-serving-entity-api
- description: List and retrieve territories — the service, baseline, climate and tariff applicability geographies that a utility uses to scope which rates apply to a given premise.
  name: Genability Signal Territory API
  slug: genability-signal-territory-api
- description: On-demand bill calculation against any North American tariff. Post a usage scenario and receive a modeled cost breakdown, or use the mass calculation endpoint to price many scenarios in one request fo
  name: Genability Signal Cost Calculation API
  slug: genability-signal-cost-calculation-api
- description: Returns a single blended price signal ($/kWh) for a utility, tariff and time window, for use in dispatch logic, EV charging schedules and consumer-facing price displays.
  name: Genability Signal Smart Price API
  slug: genability-signal-smart-price-api
- description: Retrieve time-of-use (TOU) groups, TOU definitions and their interval schedules for a utility, and create private TOU definitions scoped to your own organization.
  name: Genability Signal Time of Use API
  slug: genability-signal-time-of-use-api
- description: List calendars and calendar dates — the holiday and special-day schedules that determine which rate periods apply on a given date under a tariff.
  name: Genability Signal Calendar API
  slug: genability-signal-calendar-api
- description: List season groups, the seasonal definitions a utility applies when a tariff prices summer and winter usage differently.
  name: Genability Signal Season API
  slug: genability-signal-season-api
- description: List and retrieve property keys — the typed inputs a tariff calculation accepts — along with their permitted lookup values and usage statistics, so a client can discover exactly what a given rate need
  name: Genability Signal Property and Lookup API
  slug: genability-signal-property-and-lookup-api
- description: Returns a best-fit typical usage baseline — a modeled hourly or monthly load profile — for a location and building type, used when real interval data for a customer is not available.
  name: Genability Signal Typical Baseline API
  slug: genability-signal-typical-baseline-api
- description: Retrieve details for a ZIP code, including the utilities and territories that serve it, as the entry point for identifying a customer's tariff from an address.
  name: Genability Signal ZIP Code API
  slug: genability-signal-zip-code-api
- description: List and retrieve the utility taxes that apply to an electricity bill by jurisdiction, so a modeled bill reflects the taxes a customer actually pays.
  name: Genability Signal Utility Tax API
  slug: genability-signal-utility-tax-api
- description: Reports your own organization's Signal API consumption, the metering surface behind Genability's subscription billing.
  name: Genability Signal Organization Usage API
  slug: genability-signal-organization-usage-api
- description: Testing and debugging endpoints that validate credentials, echo a hello response, simulate error codes and validate input formats before a client calls the priced endpoints.
  name: Genability Signal Echo API
  slug: genability-signal-echo-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genability-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/genability-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/genability-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/genability-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/genability-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/genability-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genability-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/genability-signal-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/genability-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/genability-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/genability-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arcadia.com
- group: design
  title: ''
  type: Conventions
  url: conventions/genability-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/genability-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.arcadia.com/v2022-12-21-Signal/changelog
- group: start
  title: ''
  type: Sandbox
  url: sandbox/genability-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/genability-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/genability-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.arcadia.com/security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://genability.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.arcadia.com/v2022-12-21-Signal/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arcadia.com/v2022-12-21-Signal/docs/welcome-to-signal
- group: docs
  title: ''
  type: APIReference
  url: https://docs.arcadia.com/v2022-12-21-Signal/reference/api-basics
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.arcadia.com/v2022-12-21-Signal/docs/quick-start
- group: auth
  title: ''
  type: Authentication
  url: https://docs.arcadia.com/v2022-12-21-Signal/reference/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.arcadia.com/v2022-12-21-Signal/docs/rate-limit-best-practices
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.arcadia.com/v2022-12-21-Signal/llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://dash.genability.com/signup
- group: start
  title: ''
  type: Login
  url: https://dash.genability.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Genability
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Genability/genability-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Genability/genability-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Genability/Genability-PHP-Library
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genability
- group: operate
  title: ''
  type: Support
  url: https://www.arcadia.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.arcadia.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://platform-legal.arcadia.com/#platform-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform-legal.arcadia.com/#arcadia-privacy-policy
created: '2026-07-27'
description: 'Genability is a United States energy-data platform, based in San Francisco and now part of Arcadia, that sells programmatic access to North American electricity tariff data and a bill-calculation engine. Its Signal API — served from api.genability.com and documented as "Arcadia Platform - Signal" — covers electricity utilities, tariffs, territories, seasons, time-of-use definitions, calendars, utility taxes and typical-usage baselines across the USA, Canada and Mexico, plus on-demand and mass cost calculations used for solar savings analysis, storage dispatch, EV charging economics, procurement and bill auditing. Genability sits in the private, commercial layer of the energy value chain: it is not a utility, not a retailer and not a designated data holder under any consumer-energy-data mandate, so no Green Button, ESPI, CDR or other energy data standard is referenced anywhere in its documentation. Its API posture is honestly "self-serve but entirely closed data": a developer
  can sign up at dash.genability.com in minutes, but every endpoint — including the ones pathed /rest/public/ — returns 401 without an appId/appKey, so none of this tariff or market reference data is openly published, and Genability exposes no individual customer''s usage or billing data at all (that consumer-data surface lives in Arcadia''s separate Plug/Arc API).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-27'
name: Genability
nav: Providers
network: true
overview: 'Genability publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Signal Tariff API, Signal Load Serving Entity API, Signal Territory API, and 11 more. Tagged areas include Energy, United States, Utilities, Electricity, and Tariffs.


  Genability''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, signup flow, and 32 more developer resources.'
random_paper: 63
score:
  band: developing
  composite: 46.1
  delta: -2.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 32.3
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 41.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Genability Authentication
  slug: genability-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Genability Domain Security
  slug: genability-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Genability Vulnerability Disclosure
  slug: genability-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: genability
tags:
- Energy
- United States
- Utilities
- Electricity
- Tariffs
- Energy Rates
- Rate Calculation
- Energy Data Platform
- Solar
- Grid
website: https://genability.com/
---
