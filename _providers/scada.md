---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 5
apis:
- description: OPC-UA (IEC 62541) is the industrial interoperability standard for secure, reliable data exchange in industrial automation and IoT environments. It provides a platform-independent, service-oriented ar
  name: OPC Unified Architecture (OPC-UA)
  slug: opc-ua
- description: MQTT (Message Queuing Telemetry Transport, ISO/IEC 20922) is a lightweight pub/sub messaging protocol widely used in SCADA and IIoT applications for sensor data collection and device control. MQTT bro
  name: MQTT Protocol
  slug: mqtt
- description: Modbus is a serial communication protocol widely used in industrial automation and SCADA systems for connecting electronic devices. Modbus TCP/IP enables integration over standard Ethernet networks, m
  name: Modbus Protocol
  slug: modbus
- description: Inductive Automation's Ignition SCADA platform provides a REST API for reading and writing tag values, managing alarms, retrieving historical data, and controlling system resources. Ignition is one of
  name: Ignition SCADA REST API
  slug: ignition-api
- description: SCADA historians store time-series process data for analysis, reporting, and compliance. Major historian vendors (OSIsoft PI, Aspen InfoPlus.21, GE Proficy Historian) expose REST APIs for querying his
  name: Historian and Alarm Data APIs
  slug: had-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.isa.org/
- group: other
  title: ''
  type: Standards Body
  url: https://opcfoundation.org/
- group: other
  title: ''
  type: Standards Body
  url: https://www.iec.ch/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cisa.gov/topics/industrial-control-systems
- group: build
  title: ''
  type: GitHub
  url: https://github.com/topics/scada
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/scada-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/scada-context.jsonld
created: '2025-01-01'
description: SCADA (Supervisory Control and Data Acquisition) is an industrial control system architecture used to monitor and control industrial processes, infrastructure, and facility-based equipment. It is widely used in manufacturing, energy, water treatment, oil and gas, transportation, and other critical infrastructure sectors to collect real-time data from remote sensors and control equipment. Modern SCADA systems increasingly expose REST APIs, OPC-UA endpoints, and MQTT brokers for integration with enterprise systems, cloud platforms, and AI/ML workloads.
examples:
- key_count: 4
  name: Scada Tag Reading Example
  slug: scada-tag-reading-example
finops:
- name: Scada Finops
  service_category: API
  slug: scada-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scada.png
json_schemas:
- name: ScadaAlarm
  property_count: 16
  slug: scada-alarm
- name: ScadaTag
  property_count: 12
  slug: scada-tag
json_structures:
- name: Scada Tag Structure
  property_count: 0
  slug: scada-tag-structure
jsonld:
- class_count: 6
  name: Scada Context
  property_count: 23
  slug: scada-context
layout: provider
modified: '2026-05-02'
name: SCADA
nav: Providers
network: true
overview: 'SCADA publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Critical Infrastructure, ICS, Industrial Automation, Industrial IoT, and OT Security.


  The SCADA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SCADA''s developer surface includes documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Scada Plans Pricing
  plan_count: 3
  slug: scada-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Scada Rate Limits
  slug: scada-rate-limits
rules:
- name: SCADA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: scada-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.8
  delta: -7.8
  facets:
    commercial_clarity: 15.8
    contract_quality: 17.7
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 33.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/scada/refs/heads/main/screenshots/scada-2026-06-20T193448.png
security:
- kind: domain-security
  name: Scada Domain Security
  slug: scada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scada
tags:
- Critical Infrastructure
- ICS
- Industrial Automation
- Industrial IoT
- OT Security
- SCADA
website: https://www.isa.org/
---
