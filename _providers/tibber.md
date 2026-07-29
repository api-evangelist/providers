---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tibber Agentic Access
  operation_count: 5
  slug: tibber-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 4
apis:
- description: Tibber's long-standing GraphQL API. A single HTTPS endpoint serves the `viewer` query (with nested `homes`, `currentSubscription`, `priceInfo`, `consumption`, `production`, and `features`), the `liveM
  name: Tibber GraphQL API
  slug: tibber-graphql-api
- description: IoT devices linked to a home, exposed across vehicles, chargers, thermostats, inverters, and energy systems.
  name: Tibber Devices API
  slug: tibber-devices-api
- description: Historical time series at quarter-hour, hourly, daily, and monthly resolution.
  name: Tibber History API
  slug: tibber-history-api
- description: Tibber customer homes the calling client has been granted access to.
  name: Tibber Homes API
  slug: tibber-homes-api
arazzos:
- description: Discover the viewer's homes over GraphQL, then pull the most recent hourly consumption nodes with cost for the chosen home.
  name: Tibber Consumption Report
  slug: tibber-consumption-report-workflow
- description: Discover the viewer's homes over GraphQL, then fetch the current hourly Nord Pool price and price level for the chosen home.
  name: Tibber Current Price By Home
  slug: tibber-current-price-by-home-workflow
- description: List a home's connected devices and branch on the device category to read full detail for a vehicle, charger, or other linked device.
  name: Tibber Inspect Connected Device
  slug: tibber-inspect-connected-device-workflow
- description: Read the current price level over GraphQL, branch on whether power is cheap, and push a Tibber app notification when it is.
  name: Tibber Price Alert Push
  slug: tibber-price-alert-push-workflow
- description: Discover the viewer's homes over GraphQL, then pull the most recent hourly production nodes with profit for the chosen home.
  name: Tibber Production Report
  slug: tibber-production-report-workflow
- description: Discover a home, find one of its connected devices, confirm the resolution it supports, then pull a page of historical telemetry.
  name: Tibber Pull Device History
  slug: tibber-pull-device-history-workflow
- description: Resolve the WebSocket subscription URL and check whether a home has Tibber Pulse real-time consumption enabled before opening a liveMeasurement stream.
  name: Tibber Real-Time Power Readiness
  slug: tibber-realtime-power-readiness-workflow
- description: Discover the viewer's home over GraphQL, then submit a manual meter reading for that home with the sendMeterReading mutation.
  name: Tibber Submit Meter Reading
  slug: tibber-submit-meter-reading-workflow
artifact_total: 71
collections:
- collection_type: postman
  name: Tibber Data API
  slug: postman-tibber-data-api
- collection_type: postman
  name: Tibber GraphQL API
  slug: postman-tibber-graphql-api
- collection_type: open
  name: Tibber Data API
  slug: open-tibber-data-api
- collection_type: open
  name: Tibber GraphQL API
  slug: open-tibber-graphql-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tibber-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tibber-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tibber-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tibber-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tibber/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tibber-consumption-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tibber-current-price-by-home-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tibber-inspect-connected-device-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tibber-price-alert-push-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tibber-production-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tibber-pull-device-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tibber-realtime-power-readiness-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tibber-submit-meter-reading-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://tibber.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tibber.com
- group: docs
  title: ''
  type: Documentation
  url: https://data-api.tibber.com/docs/
- group: start
  title: ''
  type: Signup
  url: https://tibber.com/en
- group: other
  title: ''
  type: Store
  url: https://tibber.com/en/store
- group: commercial
  title: ''
  type: Pricing
  url: https://tibber.com/en/store
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tibber.com/
- group: operate
  title: ''
  type: Support
  url: https://support.tibber.com/en/
- group: operate
  title: ''
  type: ChangeLog
  url: https://data-api.tibber.com/docs/changelog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tibber.com/en/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tibber.com/en/terms/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tibber
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tibber/Tibber.SDK.NET
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tibber/com.tibber.athom
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tibber/homevolt-local-api-doc
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tibber/tibber-httpclient
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tibber/tibber-express-utils
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tibber/tibber-aws
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tibber/Tibber.SDK.NET
- group: build
  title: ''
  type: SDKs
  url: https://github.com/bisand/tibber-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/stefanes/PSTibber
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mkalen/tibber-graphql-client
- group: build
  title: ''
  type: Plugins
  url: https://www.home-assistant.io/integrations/tibber/
- group: build
  title: ''
  type: Plugins
  url: https://marketplace.fibaro.com/items/tibber-live
- group: company
  title: ''
  type: Careers
  url: https://jobs.tibber.com/
- group: operate
  title: ''
  type: Forums
  url: https://www.facebook.com/groups/tibbergebruikers/
- group: design
  title: ''
  type: SpectralRules
  url: rules/tibber-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tibber-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tibber-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/tibber-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tibber-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tibber-finops.yml
created: '2026-05-25'
description: 'Tibber is a fully-digital Nordic and European retail electricity provider operating in Norway, Sweden, Germany, and the Netherlands. Founded in 2016 by Daniel Lindén and Edgeir Vårdal Aksnes, the company passes Nord Pool / EPEX hourly spot prices through to customers at cost and overlays software-driven optimisation for EV charging, heat pumps, and rooftop solar to shift load to cheap and clean grid hours. Tibber publishes two distinct developer APIs: the long-standing GraphQL endpoint at api.tibber.com/v1-beta/gql for customer, subscription, price, consumption, production, and real-time `liveMeasurement` data streamed from the Tibber Pulse; and the newer OAuth 2.0 Data API at data-api.tibber.com that exposes normalised time series for third-party IoT devices (vehicles, chargers, thermostats / heat pumps, inverters, home batteries) linked through the Tibber mobile app.'
examples:
- key_count: 1
  name: Tibber Consumption Example
  slug: tibber-consumption-example
- key_count: 1
  name: Tibber Current Price Example
  slug: tibber-current-price-example
- key_count: 8
  name: Tibber Device Example
  slug: tibber-device-example
- key_count: 4
  name: Tibber Device History Example
  slug: tibber-device-history-example
- key_count: 1
  name: Tibber Live Measurement Example
  slug: tibber-live-measurement-example
features:
- description: Customers are billed at the Nord Pool / EPEX hourly spot price plus a fixed monthly fee, with no margin on the energy component.
  name: Hourly Spot Pricing Pass-Through
- description: Optional hardware clipped onto a smart-meter HAN or P1 port that streams ~2 s power, voltage, and current readings into the GraphQL liveMeasurement subscription.
  name: Tibber Pulse Live Measurement
- description: Single endpoint exposing viewer, homes, currentSubscription, priceInfo, consumption, and production with hourly through annual resolution.
  name: GraphQL Customer API
- description: REST API for third-party IoT device data with PKCE-recommended Authorization Code Flow and category-scoped device access.
  name: OAuth 2.0 Data API
- description: Schedules charging into cheap and clean grid hours for connected vehicles and EVSEs.
  name: Smart EV Charging
- description: Optimisation of air-to-air, air-to-water, and ground-source heat pumps to shift load to favourable price windows.
  name: Smart Heat Pump Control
- description: sendPushNotification GraphQL mutation lets approved integrators trigger notifications inside the Tibber mobile app.
  name: Push Notification Mutation
- description: sendMeterReading lets customers and integrators submit cumulative meter readings programmatically.
  name: Meter Reading Mutation
- description: Data API serves cursor-paged device history at quarterHour, hour, day, and month resolutions with documented retention.
  name: Immutable Paginated Device History
- description: Devices only surface when the access token carries the matching scope (vehicles, chargers, thermostats, inverters, energy systems).
  name: Per-Category OAuth Scopes
finops:
- name: Tibber Finops
  service_category: Energy & Utilities
  slug: tibber-finops
graphqls:
- description: Tibber's long-standing GraphQL API. A single HTTPS endpoint serves the `viewer` query (with nested `homes`, `currentSubscription`, `priceInfo`, `consumption`, `production`, and `features`), the `liveM
  name: Tibber GraphQL API
  slug: tibber-graphql
image: https://tibber.com/favicon.ico
integrations:
- description: Official Home Assistant Tibber integration consuming the GraphQL API.
  name: Home Assistant
- description: Tibber-maintained Homey app integrating Tibber data into Homey flows.
  name: Athom Homey
- description: Tibber Live marketplace plugin for Fibaro Home Center.
  name: Fibaro
- description: Vehicle integration for smart charging and state-of-charge reporting via the Data API vehicles scope.
  name: Tesla
- description: Ford vehicle pairing surfaced through Data API vehicles scope (per May 2026 changelog).
  name: Ford
- description: Mill thermostat integration enabled in the Data API thermostats scope (2025-11-28 changelog).
  name: Mill
- description: Solar inverter integration with production analytics in the Data API.
  name: Huawei
- description: Solar inverter integration with production analytics in the Data API.
  name: SolarEdge
- description: Day-ahead price data sourced from Nord Pool for NO/SE.
  name: Nord Pool
- description: Day-ahead price data sourced from EPEX SPOT for DE-LU/NL.
  name: EPEX SPOT
json_schemas:
- name: Tibber Consumption
  property_count: 10
  slug: tibber-consumption
- name: Tibber Data API Device History Page
  property_count: 4
  slug: tibber-device-history
- name: Tibber Data API Device
  property_count: 8
  slug: tibber-device
- name: Tibber Home
  property_count: 13
  slug: tibber-home
- name: Tibber Live Measurement
  property_count: 27
  slug: tibber-live-measurement
- name: Tibber Price
  property_count: 6
  slug: tibber-price
json_structures:
- name: Tibber Device Structure
  property_count: 0
  slug: tibber-device-structure
- name: Tibber Home Structure
  property_count: 0
  slug: tibber-home-structure
- name: Tibber Live Measurement Structure
  property_count: 0
  slug: tibber-live-measurement-structure
- name: Tibber Price Structure
  property_count: 0
  slug: tibber-price-structure
jsonld:
- class_count: 28
  name: Tibber Context
  property_count: 5
  slug: tibber-context
layout: provider
modified: '2026-05-25'
name: Tibber
nav: Providers
network: true
overview: 'Tibber publishes 4 APIs on the [APIs.io](https://apis.io/) network, including GraphQL API, Devices API, History API, and 1 more. Tagged areas include Energy, SmartHome, SmartMeter, ElectricityPricing, and ElectricVehicleCharging.


  The Tibber catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tibber''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, support, changelog, and 38 more developer resources.'
plans:
- name: Tibber Plans Pricing
  plan_count: 4
  slug: tibber-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 2
  name: Tibber Rate Limits
  slug: tibber-rate-limits
rules:
- name: Tibber API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tibber-jsonschema-spectral-rules
- name: Tibber API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: tibber-rules
scopes:
- name: Tibber Scopes
  scope_count: 11
  slug: tibber-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 65.4
  delta: -6.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 76.3
    developer_ergonomics: 52.2
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 71.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tibber/refs/heads/main/screenshots/tibber-2026-06-20T195331.png
security:
- kind: authentication
  name: Tibber Authentication
  slug: tibber-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Tibber Domain Security
  slug: tibber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tibber
solutions:
- description: Hardware product line that brings live consumption to homes whose smart meters lack a customer-readable port.
  name: Tibber Pulse IR / HAN / P1
- description: Curated marketplace of compatible smart-home and EV hardware sold through tibber.com/en/store.
  name: Tibber Marketplace
- description: Aggregated demand-response and FCR-N participation visible to Tibber Sweden customers.
  name: Tibber Grid Services (Sweden)
tags:
- Energy
- SmartHome
- SmartMeter
- ElectricityPricing
- ElectricVehicleCharging
- HeatPump
- SolarInverter
- HomeBattery
- GraphQL
- OAuth2
- Nordic
use_cases:
- description: Build personal or third-party dashboards combining hourly prices, hourly consumption, and live Pulse data.
  name: Home Energy Dashboards
- description: Pull tomorrow's prices and EV state-of-charge to schedule charging windows automatically.
  name: EV Charging Schedulers
- description: Shift heat-pump duty cycles toward CHEAP and VERY_CHEAP price hours.
  name: Heat Pump Demand Response
- description: Combine inverter history with home consumption to compute self-consumption and export economics.
  name: PV Self-Consumption Reporting
- description: Use device history and Pulse live data to support virtual power plant and demand response aggregation.
  name: Aggregator / VPP Participation
- description: Surface Tibber prices and live consumption inside Home Assistant, Athom Homey, Fibaro, and SmartThings.
  name: Home Assistant / Smart Home Integration
website: https://tibber.com/en
---
