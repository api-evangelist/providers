---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Vertiv Agentic Access
  operation_count: 10
  slug: vertiv-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 12
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
- description: The Alarms API from Vertiv — 1 operation(s) for alarms.
  name: Vertiv Alarms API
  slug: vertiv-alarms-api
- description: The Assets API from Vertiv — 1 operation(s) for assets.
  name: Vertiv Assets API
  slug: vertiv-assets-api
- description: The Authentication API from Vertiv — 1 operation(s) for authentication.
  name: Vertiv Authentication API
  slug: vertiv-authentication-api
- description: The Circuits API from Vertiv — 1 operation(s) for circuits.
  name: Vertiv Circuits API
  slug: vertiv-circuits-api
- description: The Data Sets API from Vertiv — 2 operation(s) for data sets.
  name: Vertiv Data Sets API
  slug: vertiv-data-sets-api
- description: The Devices API from Vertiv — 2 operation(s) for devices.
  name: Vertiv Devices API
  slug: vertiv-devices-api
- description: The Racks API from Vertiv — 1 operation(s) for racks.
  name: Vertiv Racks API
  slug: vertiv-racks-api
- description: The Sensors API from Vertiv — 1 operation(s) for sensors.
  name: Vertiv Sensors API
  slug: vertiv-sensors-api
artifact_total: 38
collections:
- collection_type: open
  name: Vertiv Environet Alert REST API
  slug: open-vertiv-environet-alert
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
overview: 'Vertiv publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, Assets API, Authentication API, and 5 more. Tagged areas include Critical Infrastructure, Data Center, DCIM, Infrastructure Monitoring, and Power Management.


  The Vertiv catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vertiv''s developer surface includes authentication, documentation, support, engineering blog, and 8 more developer resources.'
plans:
- name: Vertiv Plans Pricing
  plan_count: 1
  slug: vertiv-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Vertiv Rate Limits
  slug: vertiv-rate-limits
rules:
- name: Vertiv API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 6
  slug: vertiv-environet-rules
- name: Vertiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vertiv-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 69.6
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 60.5
    operational_transparency: 26.3
  previous_composite: 45.8
  schema_version: 0.5
  scored_at: '2026-07-23'
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
- Data Center
- DCIM
- Infrastructure Monitoring
- Power Management
- UPS
website: https://www.vertiv.com/
---
