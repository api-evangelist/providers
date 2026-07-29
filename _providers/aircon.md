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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: The Nest Device Access API (Google Smart Device Management API) provides programmatic control over Nest thermostats, cameras, and doorbells. Supports reading thermostat state, setting target temperatu
  name: Google Nest Device Access API
  slug: nest-device-access
- description: The Ecobee API provides access to ecobee smart thermostats for reading and writing thermostat data, managing schedules, reading sensor data, and implementing custom home automation. Supports OAuth2 au
  name: Ecobee API
  slug: ecobee
- description: The Resideo API (formerly Honeywell Home API) provides access to Honeywell and Resideo smart thermostats and home security systems. Supports reading and controlling thermostat setpoints, modes, schedu
  name: Resideo (Honeywell Home) API
  slug: resideo-honeywell
- description: The Sensibo API provides control over Sensibo Sky and Air devices that add smart functionality to existing mini-split and window AC units. Supports reading AC state, setting temperature and mode, sche
  name: Sensibo API
  slug: sensibo
- description: OpenWeatherMap provides weather data APIs used in HVAC automation to adapt cooling/heating based on outdoor conditions. Offers current weather, forecasts, historical data, and air quality data relevan
  name: OpenWeatherMap API
  slug: openweathermap
- description: 'The Home Assistant REST API provides access to all home automation entities including climate/HVAC entities. Supports reading thermostat state, setting temperature, changing HVAC mode, and triggering '
  name: Home Assistant REST API
  slug: home-assistant
artifact_total: 44
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aircon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aircon-domain-security.yml
- group: design
  title: Aircon Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/aircon/refs/heads/main/vocabulary/aircon-vocabulary.yaml
created: '2024-01-15'
description: A curated index of APIs, data sources, and developer resources related to air conditioning, HVAC (Heating, Ventilation, and Air Conditioning), and climate control systems. This topic collection covers smart thermostat APIs, building automation protocols, IoT climate APIs, and environmental data APIs used in residential, commercial, and industrial HVAC applications.
examples:
- key_count: 9
  name: Aircon Energy Report Example
  slug: aircon-energy-report-example
- key_count: 9
  name: Aircon Hvac Schedule Example
  slug: aircon-hvac-schedule-example
- key_count: 7
  name: Aircon Sensor Reading Example
  slug: aircon-sensor-reading-example
- key_count: 15
  name: Aircon Thermostat Example
  slug: aircon-thermostat-example
features:
- description: APIs for reading and setting thermostat temperature, mode, and schedule.
  name: Thermostat Control
- description: Switch between heating, cooling, auto, and fan-only modes programmatically.
  name: HVAC Mode Management
- description: Create and manage time-based HVAC schedules and programs.
  name: Schedule Automation
- description: Read temperature, humidity, and occupancy sensor data from smart thermostats.
  name: Sensor Data Access
- description: Track HVAC runtime, energy consumption, and efficiency metrics.
  name: Energy Monitoring
- description: Combine outdoor weather data with HVAC control for predictive conditioning.
  name: Weather Integration
- description: Integrate HVAC control with broader smart home platforms (Google Home, Apple HomeKit, SmartThings).
  name: Smart Home Integration
finops:
- name: Aircon Finops
  service_category: API
  slug: aircon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aircon.png
integrations:
- description: Integration with Google Home and Google Assistant for voice control.
  name: Google Home
- description: Integration with Apple HomeKit for iOS smart home control.
  name: Apple HomeKit
- description: Voice control via Amazon Alexa smart home skills.
  name: Amazon Alexa
- description: Open-source home automation platform with broad HVAC device support.
  name: Home Assistant
- description: Automation via IFTTT applets for condition-based HVAC control.
  name: IFTTT
- description: Samsung SmartThings integration for HVAC devices.
  name: SmartThings
json_schemas:
- name: EnergyReport
  property_count: 9
  slug: aircon-energy-report
- name: HvacSchedule
  property_count: 9
  slug: aircon-hvac-schedule
- name: SensorReading
  property_count: 7
  slug: aircon-sensor-reading
- name: Thermostat
  property_count: 15
  slug: aircon-thermostat
json_structures:
- name: Aircon Energy Report Structure
  property_count: 9
  slug: aircon-energy-report-structure
- name: Aircon Hvac Schedule Structure
  property_count: 9
  slug: aircon-hvac-schedule-structure
- name: Aircon Sensor Reading Structure
  property_count: 7
  slug: aircon-sensor-reading-structure
- name: Aircon Thermostat Structure
  property_count: 15
  slug: aircon-thermostat-structure
jsonld:
- class_count: 6
  name: Aircon Context
  property_count: 22
  slug: aircon-context
layout: provider
modified: '2026-04-19'
name: Aircon
nav: Providers
network: true
overview: 'Aircon publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Air Conditioning, HVAC, Climate Control, IoT, and Smart Home.


  The Aircon catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Aircon Plans Pricing
  plan_count: 3
  slug: aircon-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Aircon Rate Limits
  slug: aircon-rate-limits
rules:
- name: Aircon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aircon-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.1
  delta: -5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 37.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/aircon/refs/heads/main/screenshots/aircon-2026-06-20T171431.png
security:
- kind: domain-security
  name: Aircon Domain Security
  slug: aircon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aircon Vulnerability Disclosure
  slug: aircon-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aircon
tags:
- Air Conditioning
- HVAC
- Climate Control
- IoT
- Smart Home
- Thermostat
- Building Automation
- Energy Management
use_cases:
- description: Automate AC/heating based on occupancy, time, and weather conditions.
  name: Smart Home Automation
- description: Reduce energy costs by dynamically adjusting HVAC based on occupancy and utility pricing.
  name: Energy Optimization
- description: Commercial HVAC monitoring and control across multiple zones and buildings.
  name: Building Management
- description: Track and maintain optimal temperature and humidity levels.
  name: Comfort Monitoring
- description: Control air conditioning remotely via mobile apps and API integrations.
  name: Remote Control
- description: Pre-cool or pre-heat based on weather forecasts and schedules.
  name: Predictive Conditioning
---
