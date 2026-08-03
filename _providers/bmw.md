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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 6
apis:
- description: The BMW Vehicle Identification API allows users to access detailed information about BMW vehicles by inputting their unique vehicle identification number (VIN). Provides essential data about a vehicle
  name: BMW Vehicle Identification API
  slug: vehicle-identification-api
- description: The BMW Repair and Maintenance API provides access to maintenance schedules, diagnostic information, and technical specifications for BMW vehicles. Enables automotive technicians and repair shops to a
  name: BMW Repair and Maintenance API
  slug: repair-and-maintenance-api
- description: The BMW Technical Campaign and Map Status API provides real-time data on the status of technical campaigns and software map updates related to BMW vehicles, including campaign progress, completion tim
  name: BMW Technical Campaign and Map Status API
  slug: technical-campaign-and-map-status-api
- description: The BMW Flat Rates API provides access to a database of fixed prices for specific services and repairs on BMW vehicles, enabling transparent and standardized pricing for vehicle maintenance and repair
  name: BMW Flat Rates API
  slug: flat-rates-api
- description: The BMW Smart Maintenance API provides real-time vehicle health and maintenance need information by connecting to the vehicle's onboard diagnostic system, monitoring engine performance, tire pressure,
  name: BMW Smart Maintenance API
  slug: smart-maintenance-api
- description: The BMW Open Data Platform provides developers, researchers, and innovators with access to vehicle data including performance metrics, sensor data, and diagnostic information. The platform supports de
  name: BMW Open Data Platform
  slug: bmw-open-data-platform
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bmw-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bmwgroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bmw-group
- group: company
  title: ''
  type: Website
  url: https://www.bmw.com
- group: start
  title: ''
  type: Portal
  url: https://aos.bmwgroup.com/bmw-api
- group: start
  title: ''
  type: GettingStarted
  url: https://aos.bmwgroup.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://aos.bmwgroup.com/help/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://aos.bmwgroup.com/price-list
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aos.bmwgroup.com/conditions-of-use
- group: company
  title: ''
  type: Blog
  url: https://www.press.bmwgroup.com/global/rss
created: '2025-02-08'
description: BMW is a German multinational company specializing in manufacturing luxury vehicles and motorcycles. BMW provides automotive data APIs through the Aftersales Online System (AOS) portal and the BMW Open Data Platform, enabling dealers, repair shops, and developers to access vehicle identification, maintenance, technical campaign, pricing, and diagnostic data.
finops:
- name: Bmw Finops
  service_category: API
  slug: bmw-finops
graphqls:
- description: BMW provides connected vehicle APIs through the BMW Connected Drive platform. The API covers vehicle status, remote services (locking, horn, lights), navigation destinations, charging management for E
  name: BMW GraphQL API
  slug: bmw-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bmw.png
layout: provider
modified: '2026-04-21'
name: BMW
nav: Providers
network: true
overview: 'BMW publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Cars, Vehicles, Automotive, and Connected Car.


  BMW''s developer surface includes developer portal, getting-started guide, support, pricing, engineering blog, and 5 more developer resources.'
plans:
- name: Bmw Plans Pricing
  plan_count: 3
  slug: bmw-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Bmw Rate Limits
  slug: bmw-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 48.1
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bmw/refs/heads/main/screenshots/bmw-2026-06-20T173545.png
security:
- kind: domain-security
  name: Bmw Domain Security
  slug: bmw-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bmw
tags:
- Automobiles
- Cars
- Vehicles
- Automotive
- Connected Car
website: https://www.bmw.com
---
