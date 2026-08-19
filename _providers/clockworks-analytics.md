---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: The Base container of the Clockworks REST API. Serves static asset information — clients, buildings, building types and variables, equipment, equipment classes / types / variables, points, point class
  name: Clockworks Base API
  slug: clockworks-base-api
- description: The core-diag container. POST /diagnostics returns the diagnostic records produced by the Clockworks analysis engine for a set of client IDs, building IDs, a date range and an analysis interval, inclu
  name: Clockworks Diagnostics API
  slug: clockworks-diagnostics-api
- description: The core-kpis container. POST /AggregatedData accepts a Kusto Query Language (KQL) expression plus a dataset list and returns server-side aggregated results across the Clockworks datasets (Diagnostics
  name: Clockworks Key Performance Indicators API
  slug: clockworks-key-performance-indicators-api
- description: The workorders container. Carries the Task records Clockworks users create from diagnostic results and synchronizes them to work orders in a CMMS. Uses a bearer token obtained from POST /workorders/au
  name: Clockworks Work Orders API
  slug: clockworks-work-orders-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://clockworksanalytics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clockworks.developer.azure-api.net/
- group: docs
  title: ''
  type: Documentation
  url: https://cw.clockworksanalytics.com/APIDocumentation.aspx
- group: docs
  title: ''
  type: APIReference
  url: https://cw.clockworksanalytics.com/APIDocumentation.aspx
- group: start
  title: ''
  type: GettingStarted
  url: https://clockworksanalytics.atlassian.net/wiki/spaces/ClockworksAnalyticsUM/pages/5742297089/CMMS+Integration+Developer+Guide+version+2
- group: operate
  title: ''
  type: Support
  url: https://kgsbuildings.atlassian.net/servicedesk/customer/portals
- group: company
  title: ''
  type: Blog
  url: https://clockworksanalytics.com/blog/
- group: start
  title: ''
  type: Login
  url: https://portal.clockworksanalytics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clockworksanalytics.com/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clockworksanalytics.com/website-terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clockworksanalytics.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://clockworksanalytics.com/product-updates/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.clockworksanalytics.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/clockworks-analytics-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clockworks-analytics-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clockworks-analytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clockworks-analytics-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clockworks-analytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clockworks-analytics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clockworks-analytics-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/clockworks-analytics-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clockworks-analytics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clockworks-analytics-llms.txt
created: '2026-08-09'
description: Clockworks Analytics is a Boston-area building-analytics company whose cloud platform performs automated fault detection and diagnostics (FDD) on HVAC and building systems. It ingests interval data from Building Management Systems through the Clockworks Connect gateway, runs a curated library of root-cause diagnostics, and quantifies each performance issue by avoidable energy cost plus energy, comfort and maintenance priority on a 0-10 scale. Its public REST API is delivered through Azure API Management on rest.buildingsapi.net as four containers — core-base (clients, buildings, equipment, points, users), core-diag (diagnostic records), core-kpis (KQL-driven aggregated datasets) and workorders (Tasks / CMMS work-order sync) — and is documented publicly at cw.clockworksanalytics.com plus a public Confluence developer guide set for CMMS and KPI integration.
image: https://clockworksanalytics.com/wp-content/themes/Clockworks/images/clockworks-logo.svg
layout: provider
modified: '2026-08-09'
name: Clockworks Analytics
nav: Providers
network: true
overview: 'Clockworks Analytics publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Building Analytics, Fault Detection and Diagnostics, HVAC, and Energy Management.


  Clockworks Analytics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 16 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 38.7
  delta: 2.9
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 35.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Clockworks Analytics Authentication
  slug: clockworks-analytics-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Clockworks Analytics Domain Security
  slug: clockworks-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clockworks Analytics Trust Center
  slug: clockworks-analytics-trust-center
  summary_line: trust center published
slug: clockworks-analytics
tags:
- Company
- Building Analytics
- Fault Detection and Diagnostics
- HVAC
- Energy Management
- Facilities Management
- Smart Buildings
- CMMS Integration
- Analytics
- Internet of Things
website: https://clockworksanalytics.com/
---
