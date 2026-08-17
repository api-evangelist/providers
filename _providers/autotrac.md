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
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: 'The AutoTrac Supervisor Web platform provides fleet management capabilities for monitoring vehicle locations, managing fleet operations, generating reports, and coordinating driver assignments across '
  name: AutoTrac Supervisor Web API
  slug: supervisor-web-api
- description: The AutoTrac Telemetria platform provides real-time vehicle telemetry data including speed, fuel consumption, engine diagnostics, tire pressure, temperature sensors (for refrigerated cargo), and drive
  name: AutoTrac Telemetria API
  slug: telemetria-api
- description: The AutoTrac Jornada platform manages driver journey logs and compliance with Brazilian driving hour regulations, tracking driving time, rest periods, and journey records for long-distance transport c
  name: AutoTrac Jornada Driver Journey API
  slug: jornada-api
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autotrac-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autotrac.com.br
created: '2024-01-01'
description: AutoTrac is a Brazilian fleet management and vehicle tracking technology company with over 30 years of experience. As the national market leader, AutoTrac provides satellite and cellular fleet tracking solutions, real-time telemetry, driver journey management, and management intelligence platforms for logistics, agriculture, maritime, and insurance sectors. The company operates its own terrestrial satellite communication station and data center for nationwide coverage.
features:
- description: AutoTrac operates its own terrestrial satellite communication station and integrated data center, providing coverage in areas with limited cellular connectivity across Brazil.
  name: Proprietary Satellite Communication
- description: Real-time monitoring of vehicle parameters including location, speed, fuel consumption, engine diagnostics, and cargo temperature for refrigerated transport.
  name: Real-Time Vehicle Telemetry
- description: Jornada platform for tracking driver hours, rest periods, and journey compliance with Brazilian transportation regulations.
  name: Driver Journey Management
- description: Informacoes Gerenciais business intelligence dashboards for fleet performance analytics, cost analysis, and operational reporting.
  name: Fleet Intelligence Reporting
- description: Specialized tracking solutions for agricultural machinery including harvesters, tractors, and implements with field operation monitoring.
  name: Agricultural Equipment Tracking
finops:
- name: Autotrac Finops
  service_category: API
  slug: autotrac-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autotrac.png
integrations:
- description: Integration with transportation management systems for freight dispatch, route optimization, and delivery confirmation workflows.
  name: TMS Systems
- description: Connect AutoTrac fleet data with ERP systems (SAP, TOTVS) for fleet cost accounting, maintenance scheduling, and asset management.
  name: ERP Systems
- description: API integration with insurance carriers for vehicle recovery, claims verification, and telematics-based premium calculation.
  name: Insurance Platforms
layout: provider
modified: '2026-04-19'
name: AutoTrac
nav: Providers
network: true
overview: AutoTrac publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fleet Management, GPS Tracking, Telematics, Vehicle Tracking, and Logistics.
plans:
- name: Autotrac Plans Pricing
  plan_count: 3
  slug: autotrac-plans-pricing
random_paper: 122
rate_limits:
- limit_count: 5
  name: Autotrac Rate Limits
  slug: autotrac-rate-limits
score:
  band: minimal
  composite: 10.7
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autotrac/refs/heads/main/screenshots/autotrac-2026-06-20T172710.png
security:
- kind: domain-security
  name: Autotrac Domain Security
  slug: autotrac-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: autotrac
tags:
- Fleet Management
- GPS Tracking
- Telematics
- Vehicle Tracking
- Logistics
- Brazil
- Satellite Communication
use_cases:
- description: Track trucks and cargo across Brazil using satellite and cellular communication for nationwide visibility of logistics operations.
  name: Long-Distance Logistics Tracking
- description: Monitor temperature-controlled cargo transport with real-time telemetry alerts for temperature deviations in refrigerated vehicles.
  name: Refrigerated Cargo Monitoring
- description: Ensure compliance with Brazilian driver hour regulations by tracking journey logs and rest periods automatically via Jornada.
  name: Driver Compliance Management
- description: Track agricultural equipment, monitor field operations, and manage harvest logistics for agribusiness operations.
  name: Agricultural Fleet Management
- description: Provide vehicle behavior and location data to insurance companies for usage-based insurance and stolen vehicle recovery programs.
  name: Insurance Telematics
website: https://www.autotrac.com.br
---
