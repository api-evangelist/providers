---
access_model:
  confidence: medium
  label: Freemium (free trial) · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Mercedes Me Agentic Access
  operation_count: 39
  slug: mercedes-me-agentic-access
  summary_line: 39 operations · 5 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: The Vehicle Status API delivers real-time vehicle state — doors, windows, deck lid, sunroof, tire pressure, and overall lock state — for a customer-consented Mercedes-Benz vehicle by VIN. Returns last
  name: Mercedes-Benz Vehicle Status API
  slug: mercedes-me-vehicle-status-api
- description: 'The Vehicle Lock Status API returns the current door-lock, deck-lid, and position-lock state of a Mercedes-Benz vehicle by VIN. Designed for parking, insurance, and security-monitoring use cases that '
  name: Mercedes-Benz Vehicle Lock Status API
  slug: mercedes-me-vehicle-lock-status-api
- description: The Fuel Status API exposes a Mercedes-Benz combustion vehicle's current tank level, remaining fuel range in km, and last-update timestamp by VIN. Targeted at fueling, fleet, and concierge integration
  name: Mercedes-Benz Fuel Status API
  slug: mercedes-me-fuel-status-api
- description: The Electric Vehicle Status API (currently at v3) provides charge state, state-of-charge percent, remaining electric range in km, charging-active flag, and time-to-full estimates for Mercedes-EQ and E
  name: Mercedes-Benz Electric Vehicle Status API
  slug: mercedes-me-electric-vehicle-status-api
- description: The Pay As You Drive 2.0 API supplies precise odometer readings and geographical position for a consented Mercedes-Benz vehicle, designed for usage-based insurance, mileage-based subscriptions, and PA
  name: Mercedes-Benz Pay As You Drive 2.0 API
  slug: mercedes-me-pay-as-you-drive-insurance-api
- description: The Mercedes-Benz Fleet API integrates vehicle data into fleet management systems without retrofit hardware. It splits into a REST Management API (add vehicles, activate/deactivate per-vehicle data pa
  name: Mercedes-Benz Fleet API
  slug: mercedes-benz-fleet-api
- description: The Components API from Mercedes-Benz Mercedes me — 7 operation(s) for components.
  name: Mercedes-Benz Mercedes me Components API
  slug: mercedes-me-components-api
- description: Select equipment and configure a car
  name: Mercedes-Benz Mercedes me Configurations API
  slug: mercedes-me-configurations-api
- description: Resources that provide search functions for dealers (dealer, garage, retailer, etc.) based on given attributes.
  name: Mercedes-Benz Mercedes me Dealer search API
  slug: mercedes-me-dealer-search-api
- description: Remote Diagnostic Support service for view dtc snapshot List.
  name: Mercedes-Benz Mercedes me Diagnostic Trouble Code (DTC) Snapshots API
  slug: mercedes-me-diagnostic-trouble-code-dtc-snapshots-api
- description: Remote Diagnostic Support service for view dtc List.
  name: Mercedes-Benz Mercedes me Diagnostic Trouble Codes (DTC's) API
  slug: mercedes-me-diagnostic-trouble-codes-dtc-s-api
- description: Remote Diagnostic Support services for view ecu List.
  name: Mercedes-Benz Mercedes me Electronical Control Units (ECU's) API
  slug: mercedes-me-electronical-control-units-ecu-s-api
- description: Get images for the vehicle configuration and its components
  name: Mercedes-Benz Mercedes me Images API
  slug: mercedes-me-images-api
- description: The Perspectives API from Mercedes-Benz Mercedes me — 1 operation(s) for perspectives.
  name: Mercedes-Benz Mercedes me Perspectives API
  slug: mercedes-me-perspectives-api
- description: Provide static reference data about cars like markets, bodies, classes, etc.
  name: Mercedes-Benz Mercedes me References API
  slug: mercedes-me-references-api
- description: Remote Diagnostic Support service for view all resources.
  name: Mercedes-Benz Mercedes me Resources API
  slug: mercedes-me-resources-api
- description: Store and load configurations with an onlinecode
  name: Mercedes-Benz Mercedes me Saved configurations API
  slug: mercedes-me-saved-configurations-api
artifact_total: 36
collections:
- collection_type: open
  name: Car Configurator
  slug: open-mercedes-me-configurator-api
- collection_type: open
  name: Dealer
  slug: open-mercedes-me-dealer-api
- collection_type: open
  name: Remote Diagnostic Support
  slug: open-mercedes-me-remote-diagnostic-support-api
- collection_type: open
  name: Vehicle Image
  slug: open-mercedes-me-vehicle-images-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mercedes-me-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mercedes-me-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercedes-me-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.mercedes-benz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mercedes-benz.com/products
- group: build
  title: ''
  type: SDKs
  url: https://developer.mercedes-benz.com/sdks
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mercedes-benz/MBSDK-Mobile-Android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mercedes-benz/MBSDK-Mobile-iOS
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mercedes-benz/MBSDK-community-support
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mercedes-benz/kafka-integration-samples
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mercedes-benz
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mercedes-benz/foss
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mercedes-benz/mercedes-benz-foss-manifesto
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/mbdevelopers/mercedes-benz/overview
- group: other
  title: ''
  type: Connectivity
  url: https://connectivity.mercedes-benz.com/
- group: other
  title: ''
  type: Connectivity
  url: https://data.mercedes-benz.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercedes-benz-ag/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MercedesBenz
- group: other
  title: ''
  type: ConsumerApp
  url: https://www.mbusa.com/en/mercedes-benz-app
- group: other
  title: ''
  type: Payments
  url: https://group.mercedes-benz.com/innovations/digitalisation/connectivity/mercedes-pay.html
- group: other
  title: ''
  type: Payments
  url: https://www.mercedes-benz-mobility.com/en/what-we-do/payment-services/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mercedes-me-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/mercedes-me-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mercedes-me-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mercedes-me-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mercedes-me-finops.yml
examples:
- key_count: 2
  name: Mercedes Me Create Dtc Readout Example
  slug: mercedes-me-create-dtc-readout-example
- key_count: 2
  name: Mercedes Me List Dealers Example
  slug: mercedes-me-list-dealers-example
- key_count: 2
  name: Mercedes Me List Markets Example
  slug: mercedes-me-list-markets-example
finops:
- name: Mercedes Me Finops
  service_category: ''
  slug: mercedes-me-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercedes-me.png
json_schemas:
- name: Mercedes-Benz DTC Readout
  property_count: 7
  slug: mercedes-me-dtc-readout
- name: Mercedes-Benz Vehicle Configuration
  property_count: 10
  slug: mercedes-me-vehicle-configuration
json_structures:
- name: Mercedes Me Vehicle Configuration Structure
  property_count: 0
  slug: mercedes-me-vehicle-configuration-structure
jsonld:
- class_count: 23
  name: Mercedes Me Context
  property_count: 32
  slug: mercedes-me-context
layout: provider
name: Mercedes-Benz Mercedes me
nav: Providers
network: true
overview: 'Mercedes-Benz Mercedes me publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Components API, Configurations API, Dealer search API, and 8 more. Tagged areas include Automotive, Connected Car, Connected Vehicle, Daimler, and Fleet Management.


  The Mercedes-Benz Mercedes me catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mercedes-Benz Mercedes me''s developer surface includes developer portal, documentation, GitHub presence, and 23 more developer resources.'
plans:
- name: Mercedes Me Plans Pricing
  plan_count: 4
  slug: mercedes-me-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Mercedes Me Rate Limits
  slug: mercedes-me-rate-limits
rules:
- name: Mercedes-Benz Mercedes me API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mercedes-me-jsonschema-spectral-rules
- name: Mercedes-Benz Mercedes me API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: mercedes-me-rules
score:
  band: developing
  composite: 45.8
  delta: -6.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.1
    developer_ergonomics: 37.0
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/mercedes-me/refs/heads/main/screenshots/mercedes-me-2026-06-20T185206.png
security:
- kind: domain-security
  name: Mercedes Me Domain Security
  slug: mercedes-me-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mercedes Me Vulnerability Disclosure
  slug: mercedes-me-vulnerability-disclosure
  summary_line: disclosure policy published
slug: mercedes-me
tags:
- Automotive
- Connected Car
- Connected Vehicle
- Daimler
- Fleet Management
- Mercedes me
- Mercedes-Benz
- OEM
- Telematics
- Vehicle Data
website: https://developer.mercedes-benz.com/
---
