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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-05'
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
  description: The Data Sets API from Vertiv — 2 operation(s) for data sets.
  name: Vertiv Data Sets API
  slug: vertiv-data-sets-api
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
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vertiv-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vertiv-domain-security.yml
- group: auth
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
- name: Vertiv Finops
  service_category: Data Center Infrastructure
  slug: vertiv-finops
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
overview: 'Vertiv publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, Assets API, Authentication API, and 5 more. Tagged areas include Critical Infrastructure, Data-Center, DCIM, Infrastructure Monitoring, and Power Management.


  The Vertiv catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vertiv''s developer surface includes authentication, documentation, support, engineering blog, and 8 more developer resources.'
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
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Vertiv API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 6
  slug: vertiv-environet-rules
- effective_rule_count: 5
  extends: []
  name: Vertiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vertiv-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.0
    catalog_earned_first_party: 0.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 54.5
    contract_quality: 65.1
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 54.5
    operational_transparency: 10.5
  previous_composite: 39.0
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
    score: 23.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vertiv/refs/heads/main/screenshots/vertiv-2026-06-20T200959.png
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
- Data-Center
- DCIM
- Infrastructure Monitoring
- Power Management
- UPS
website: https://www.vertiv.com/
---
