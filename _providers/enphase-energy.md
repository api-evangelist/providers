---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 3
  name: Enphase Energy Agentic Access
  operation_count: 56
  slug: enphase-energy-agentic-access
  summary_line: 56 operations · 6 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: The Commissioning API is the installer-facing companion to the Monitoring API. Available to Partner-plan customers (qualifying installers with 10+ installations), it allows activation creation and upd
  name: Enphase Enlighten Commissioning API
  slug: enphase-enlighten-commissioning-api
- description: The Virtual Power Plant (VPP) API allows energy aggregators and utilities to create and manage VPPs that monitor, forecast, and control large fleets of distributed energy resources (DERs) including PV
  name: Enphase VPP API
  slug: enphase-enlighten-vpp-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The Device Level Production Monitoring API from Enphase Energy — 3 operation(s) for device level production monitoring.
  name: Enphase Energy Device Level Production Monitoring API
  slug: enphase-energy-device-level-production-monitoring-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The EV Charger Control API from Enphase Energy — 2 operation(s) for ev charger control.
  name: Enphase Energy EV Charger Control API
  slug: enphase-energy-ev-charger-control-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The EV Charger Monitoring API from Enphase Energy — 6 operation(s) for ev charger monitoring.
  name: Enphase Energy EV Charger Monitoring API
  slug: enphase-energy-ev-charger-monitoring-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The Site Level Consumption Monitoring API from Enphase Energy — 9 operation(s) for site level consumption monitoring.
  name: Enphase Energy Site Level Consumption Monitoring API
  slug: enphase-energy-site-level-consumption-monitoring-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The Site Level Production Monitoring API from Enphase Energy — 5 operation(s) for site level production monitoring.
  name: Enphase Energy Site Level Production Monitoring API
  slug: enphase-energy-site-level-production-monitoring-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The Streaming APIs API from Enphase Energy — 1 operation(s) for streaming apis.
  name: Enphase Energy Streaming APIs API
  slug: enphase-energy-streaming-apis-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The System Configurations API from Enphase Energy — 4 operation(s) for system configurations.
  name: Enphase Energy System Configurations API
  slug: enphase-energy-system-configurations-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The System Details API from Enphase Energy — 10 operation(s) for system details.
  name: Enphase Energy System Details API
  slug: enphase-energy-system-details-api
- baseURL: https://api.enphaseenergy.com/api/v4
  baseurl_source: declared
  description: The Systems API from Enphase Energy — 13 operation(s) for systems.
  name: Enphase Energy Systems API
  slug: enphase-energy-systems-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: The Enlighten Systems Device Level Production Monitoring API
  slug: open-enphase-energy-device-level-production-monitoring-api
- collection_type: open
  name: The Enlighten Systems Device Level Production Monitoring EV Charger Control API
  slug: open-enphase-energy-ev-charger-control-api
- collection_type: open
  name: The Enlighten Systems Device Level Production Monitoring EV Charger Monitoring API
  slug: open-enphase-energy-ev-charger-monitoring-api
- collection_type: open
  name: The Enlighten Systems Device Level Production Monitoring Site Level Consumption Monitoring API
  slug: open-enphase-energy-site-level-consumption-monitoring-api
- collection_type: open
  name: The Enlighten Systems Device Level Production Monitoring Site Level Production Monitoring API
  slug: open-enphase-energy-site-level-production-monitoring-api
- collection_type: open
  name: The Enlighten Systems Device Level Production Monitoring Streaming APIs API
  slug: open-enphase-energy-streaming-apis-api
- collection_type: open
  name: The Enlighten Systems Device Level Production Monitoring System Configurations API
  slug: open-enphase-energy-system-configurations-api
- collection_type: open
  name: The Enlighten Systems Device Level Production Monitoring System Details API
  slug: open-enphase-energy-system-details-api
- collection_type: open
  name: The Enlighten Device Level Production Monitoring Systems API
  slug: open-enphase-energy-systems-api
- collection_type: open
  name: The Enlighten Systems API
  slug: open-enphase-enlighten-v2
- collection_type: open
  name: Monitoring API
  slug: open-enphase-enlighten-v4-monitoring
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/enphase-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enphase-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enphase-energy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://enphase.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer-v4.enphase.com/docs/quickstart.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/enphase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enphase-energy
- group: company
  title: ''
  type: Blog
  url: https://enphase.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://developer-v4.enphase.com/developer-plans
- group: other
  title: ''
  type: X
  url: https://x.com/Enphase
- group: commercial
  title: ''
  type: Plans
  url: plans/enphase-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enphase-energy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/enphase-energy-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer-v4.enphase.com/docs/release_notes
- group: operate
  title: ''
  type: Support
  url: https://developer-v4.enphase.com/docs/support
- group: start
  title: ''
  type: Signup
  url: https://developer-v4.enphase.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enphase.com/api-license-agreement-v4
created: 2026-06-13
description: Enphase Energy is a solar microinverter and energy management company that provides the Enlighten Systems API, a REST API enabling access to solar production, battery storage, grid usage, and home energy data. The API supports monitoring at the fleet, site, and device level across Enphase IQ Microinverters and IQ Batteries via OAuth 2.0 secured endpoints. Developers can retrieve real-time and historical energy telemetry, manage commissioning workflows, and operate Virtual Power Plant fleets of distributed energy resources including PV, batteries, EV chargers, heat pumps, and HVAC units. The Enlighten API v4 launched in February 2022, replacing legacy v2 with microinverter-level telemetry, battery-level data, and fine-grained access controls for installers and partners.
examples:
- key_count: 6
  name: Enphase Battery Settings Example
  slug: enphase-battery-settings-example
- key_count: 6
  name: Enphase Production Meter Telemetry Example
  slug: enphase-production-meter-telemetry-example
- key_count: 12
  name: Enphase System Summary Example
  slug: enphase-system-summary-example
finops:
- name: Enphase Energy Finops
  service_category: Internet of Things
  slug: enphase-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enphase-energy.png
json_schemas:
- name: EnphaseBatterySettings
  property_count: 5
  slug: enphase-battery
- name: EnphaseSystem
  property_count: 15
  slug: enphase-system
- name: EnphaseTelemetryInterval
  property_count: 7
  slug: enphase-telemetry
json_structures:
- name: Enphase System Structure
  property_count: 0
  slug: enphase-system-structure
jsonld:
- class_count: 18
  name: Enphase Energy Context
  property_count: 11
  slug: enphase-energy-context
layout: provider
modified: 2026-06-13
name: Enphase Energy
nav: Providers
network: true
overview: 'Enphase Energy publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Device Level Production Monitoring API, EV Charger Control API, EV Charger Monitoring API, and 6 more. Tagged areas include Solar, Energy, Microinverters, Battery Storage, and IQ Battery.


  The Enphase Energy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Enphase Energy''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, support, signup flow, and 10 more developer resources.'
plans:
- name: Enphase Energy Plans Pricing
  plan_count: 5
  slug: enphase-energy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Enphase Energy Rate Limits
  slug: enphase-energy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Enphase Energy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: enphase-energy-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Enphase Energy API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 3
  slug: enphase-energy-rules
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 13.6
    contract_quality: 63.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 52.6
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enphase-energy/refs/heads/main/screenshots/enphase-energy-2026-06-20T180721.png
security:
- kind: authentication
  name: Enphase Energy Authentication
  slug: enphase-energy-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Enphase Energy Domain Security
  slug: enphase-energy-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: enphase-energy
tags:
- Solar
- Energy
- Microinverters
- Battery Storage
- IQ Battery
- IQ Microinverter
- IQ EV Charger
- Enlighten
- Home Energy Management
- Renewable Energy
- Grid Services
- Cleantech
- IoT
- Telemetry
website: https://enphase.com
---
