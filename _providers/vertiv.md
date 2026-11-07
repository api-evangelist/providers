---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Vertiv Agentic Access
  operation_count: 10
  slug: vertiv-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 1
apis:
- description: The Vertiv Avocent ADX Ecosystem API provides REST API access for managing IT infrastructure through the Avocent ADX Management Platform. The API supports device management, KVM session management, us
  name: Vertiv Avocent ADX Ecosystem API
  slug: avocent-adx-ecosystem-api
- description: The Vertiv Avocent DSView Solution REST API enables launching of KVM, serial, and virtual viewer sessions to managed devices. The API provides programmatic control of session management, device invent
  name: Vertiv Avocent DSView API
  slug: avocent-dsview-api
- description: The Vertiv Geist Power Distribution Unit (PDU) REST API provides programmatic control of Geist intelligent rack PDUs. The API supports outlet power control (on/off with delay), outlet configuration, d
  name: Vertiv Geist PDU REST API
  slug: geist-pdu-rest-api
- description: The Vertiv Avocent ACS800/8000 Advanced Console System native RESTful API provides programmatic access to serial console server management. The API supports device configuration, port management, user
  name: Vertiv Avocent ACS800/8000 REST API
  slug: avocent-acs-api
- baseURL_template: https://{environet-host}/api
  baseurl_source: spec_template
  description: The Alarms API from Vertiv — 1 operation(s) for alarms.
  name: Vertiv Alarms API
  slug: vertiv-alarms-api
- baseURL_template: https://{environet-host}/api
  baseurl_source: spec_template
  description: The Assets API from Vertiv — 1 operation(s) for assets.
  name: Vertiv Assets API
  slug: vertiv-assets-api
- baseURL_template: https://{environet-host}/api
  baseurl_source: spec_template
  description: The Authentication API from Vertiv — 1 operation(s) for authentication.
  name: Vertiv Authentication API
  slug: vertiv-authentication-api
- baseURL_template: https://{environet-host}/api
  baseurl_source: spec_template
  description: The Circuits API from Vertiv — 1 operation(s) for circuits.
  name: Vertiv Circuits API
  slug: vertiv-circuits-api
- baseURL_template: https://{environet-host}/api
  baseurl_source: spec_template
  description: The Devices API from Vertiv — 2 operation(s) for devices.
  name: Vertiv Devices API
  slug: vertiv-devices-api
- baseURL_template: https://{environet-host}/api
  baseurl_source: spec_template
  description: The Racks API from Vertiv — 1 operation(s) for racks.
  name: Vertiv Racks API
  slug: vertiv-racks-api
- baseURL_template: https://{environet-host}/api
  baseurl_source: spec_template
  description: The Sensors API from Vertiv — 1 operation(s) for sensors.
  name: Vertiv Sensors API
  slug: vertiv-sensors-api
- baseURL_template: https://{environet-host}/api
  baseurl_source: spec_template
  description: The Datasets API from Vertiv — 2 operation(s) for datasets.
  name: Vertiv Datasets API
  slug: vertiv-datasets-api
artifact_total: 46
collections:
- collection_type: open
  name: Vertiv Environet Alert REST Alarms API
  slug: open-vertiv-alarms-api
- collection_type: open
  name: Vertiv Environet Alert REST Alarms Assets API
  slug: open-vertiv-assets-api
- collection_type: open
  name: Vertiv Environet Alert REST Alarms Authentication API
  slug: open-vertiv-authentication-api
- collection_type: open
  name: Vertiv Environet Alert REST Alarms Circuits API
  slug: open-vertiv-circuits-api
- collection_type: open
  name: Vertiv Environet Alert REST Alarms Data Sets API
  slug: open-vertiv-data-sets-api
- collection_type: open
  name: Vertiv Environet Alert REST Alarms Devices API
  slug: open-vertiv-devices-api
- collection_type: open
  name: Vertiv Environet Alert REST API
  slug: open-vertiv-environet-alert
- collection_type: open
  name: Vertiv Environet Alert REST Alarms Racks API
  slug: open-vertiv-racks-api
- collection_type: open
  name: Vertiv Environet Alert REST Alarms Sensors API
  slug: open-vertiv-sensors-api
common:
- group: commercial
  href: https://artifacts.apis.io/vertiv/plans/vertiv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vertiv-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vertiv/rate-limits/vertiv-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vertiv-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/vertiv/finops/vertiv-finops.yml
  title: ''
  type: FinOps
  url: finops/vertiv-finops.yml
- group: agent
  href: https://artifacts.apis.io/vertiv/agentic-access/vertiv-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vertiv-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/vertiv/security/vertiv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vertiv-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vertiv/authentication/vertiv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vertiv-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vertiv
- group: company
  title: ''
  type: Website
  url: https://www.vertiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.vertiv.com/en-us/products-catalog/monitoring-control-and-management/
- group: company
  title: ''
  type: Website
  url: https://www.geistglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.geistglobal.com/open-api-and-software-integration
- group: other
  title: ''
  type: Downloads
  url: https://www.vertiv.com/en-us/support/software-downloads/
- group: operate
  title: ''
  type: Support
  url: https://www.vertiv.com/en-us/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enp-isit
- group: company
  title: ''
  type: Blog
  url: https://www.vertiv.com/en-us/about/news-and-insights/
created: '2026-05-03'
description: Vertiv is a global provider of critical digital infrastructure and continuity solutions for data centers and communication networks. The company delivers power management, thermal management, IT management software (DCIM), and infrastructure monitoring solutions through brands including Geist (DCIM and PDU monitoring), Avocent (IT management and KVM), and Liebert (UPS and thermal). Vertiv's software platforms expose REST APIs for integrating with third-party systems, automation workflows, and data center management platforms.
examples:
- key_count: 2
  name: Vertiv Authenticate Example
  slug: vertiv-authenticate-example
- key_count: 2
  name: Vertiv List Alarms Example
  slug: vertiv-list-alarms-example
- key_count: 2
  name: Vertiv List Devices Example
  slug: vertiv-list-devices-example
- key_count: 2
  name: Vertiv List Sensors Example
  slug: vertiv-list-sensors-example
finops:
- has_sources: true
  method: generated
  name: Vertiv Finops
  primary_unit: ''
  service_category: Data Center Infrastructure
  slug: vertiv-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vertiv.png
json_schemas:
- name: Vertiv Alarm
  property_count: 7
  slug: vertiv-alarm
- name: Asset
  property_count: 6
  slug: vertiv-asset
- name: Circuit
  property_count: 7
  slug: vertiv-circuit
- name: DataSetEntity
  property_count: 7
  slug: vertiv-datasetentity
- name: Vertiv Device
  property_count: 7
  slug: vertiv-device
- name: Error
  property_count: 3
  slug: vertiv-error
- name: Rack
  property_count: 5
  slug: vertiv-rack
- name: Vertiv Sensor
  property_count: 9
  slug: vertiv-sensor
- name: StatusSummary
  property_count: 10
  slug: vertiv-statussummary
json_structures:
- name: Vertiv Alarm Structure
  property_count: 0
  slug: vertiv-alarm-structure
- name: Vertiv Device Structure
  property_count: 0
  slug: vertiv-device-structure
- name: Vertiv Structure
  property_count: 0
  slug: vertiv-structure
jsonld:
- class_count: 7
  name: Vertiv Context
  property_count: 27
  slug: vertiv-context
layout: provider
modified: '2026-05-19'
name: Vertiv
nav: Providers
network: true
overview: 'Vertiv publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alarms API, Assets API, Authentication API, and 9 more. Tagged areas include Critical Infrastructure, Data Center, DCIM, Infrastructure Monitoring, and Power Management.


  The Vertiv catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vertiv''s developer surface includes authentication, documentation, support, engineering blog, and 11 more developer resources.'
plans:
- name: Vertiv Plans Pricing
  plan_count: 1
  slug: vertiv-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Vertiv Rate Limits
  slug: vertiv-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Vertiv — environet rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 6
  slug: vertiv-environet-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Vertiv — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vertiv-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.9
    catalog_earned_first_party: 0.0
    catalog_gap: 58.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 59.3
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 29.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vertiv/vertiv-2026-06-20T200959.png
security:
- kind: authentication
  name: Vertiv Authentication
  slug: vertiv-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vertiv Domain Security
  slug: vertiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vertiv
tags:
- Critical Infrastructure
- Data Center
- DCIM
- Infrastructure Monitoring
- Power Management
- UPS
website: https://www.vertiv.com/
---
