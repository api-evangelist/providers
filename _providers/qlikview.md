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
  scored_at: '2026-08-17'
api_count: 10
apis:
- description: Server-side API for managing QlikView Server operations, documents, and sessions.
  name: QlikView Server API
  slug: qlikview-server-api
- description: SOAP-based API for QlikView management and administration tasks.
  name: QlikView Management API (QMS API)
  slug: qlikview-management-api-qms-api
- description: Web-based API for QlikView AccessPoint portal functionality.
  name: QlikView AccessPoint API
  slug: qlikview-accesspoint-api
- description: API for integrating QlikView objects into web applications and portals.
  name: QlikView Workbench API
  slug: qlikview-workbench-api
- description: COM-based API for creating custom objects and extensions in QlikView.
  name: QlikView Plugin API
  slug: qlikview-plugin-api
- description: ActiveX/COM API for automating QlikView Desktop operations.
  name: QlikView OCX API (Automation API)
  slug: qlikview-ocx-api-automation-api
- description: The Qlik data eXchange (QVX) SDK enables developers to build custom connectors for integrating external data sources into QlikView, using a high-performance file and stream format for data input.
  name: QlikView QVX SDK API
  slug: qlikview-qvx-sdk-api
- description: JavaScript API library for building websites containing QlikView content and for developing custom extension objects that extend QlikView visualization capabilities.
  name: QlikView JavaScript API
  slug: qlikview-javascript-api
- description: Authentication API providing Custom Ticket Exchange (CTE) for secure single sign-on access to QlikView Server, allowing third-party systems to request authentication tokens on behalf of users.
  name: QlikView Authentication API (Ticket API)
  slug: qlikview-authentication-api-ticket-api
- description: API interface for the QlikView Distribution Service, providing programmatic access to document distribution, task management, and scheduled reload operations including External Document Exchange (EDX)
  name: QlikView Distribution Service API (IQDS)
  slug: qlikview-distribution-service-api-iqds
artifact_total: 28
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/qlikview-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qlikview-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://help.qlik.com/en-US/qlikview-developer/
- group: docs
  title: ''
  type: APIReference
  url: https://help.qlik.com/en-US/qlikview-developer/September2025/Subsystems/QMSAPIref/Content/Home.htm
- group: operate
  title: ''
  type: Support
  url: https://community.qlik.com/
- group: learn
  title: ''
  type: Training
  url: https://www.qlik.com/us/services/training
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qlik.com/us/pricing
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://community.qlik.com/t5/Release-Notes/tkb-p/ReleaseNotes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qlik.dev/
created: '2024-01-01'
description: QlikView is a business intelligence and data visualization platform that enables users to create guided analytics applications and dashboards for data discovery.
features:
- description: Explore data relationships dynamically with QlikView's patented associative engine.
  name: Associative Data Model
- description: Fast analytics with in-memory data compression and calculation.
  name: In-Memory Processing
- description: Build guided analytics applications with interactive dashboards and drill-down capabilities.
  name: Guided Analytics
- description: Rich set of chart types and visualization objects for data exploration and presentation.
  name: Data Visualization
- description: Extend QlikView with custom objects, connectors, and plugins using the Plugin and QVX APIs.
  name: Custom Extensions
- description: Web-based access to QlikView documents through the AJAX Zero Footprint Client.
  name: AJAX Client
- description: Schedule and distribute QlikView documents and reports via the Distribution Service.
  name: Document Distribution
- description: Integrate single sign-on with custom authentication systems using the Ticket API.
  name: Custom Ticket Authentication
finops:
- name: Qlikview Finops
  service_category: API
  slug: qlikview-finops
image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo-2x.png
layout: provider
modified: '2026-04-18'
name: QlikView
nav: Providers
network: true
overview: 'QlikView publishes 1 API on the [APIs.io](https://apis.io/) network: Server API. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Discovery, and Data Visualization.


  QlikView''s developer surface includes developer portal, API reference, support, training material, pricing, release notes, and 4 more developer resources.'
plans:
- name: Qlikview Plans Pricing
  plan_count: 3
  slug: qlikview-plans-pricing
random_paper: 131
rate_limits:
- limit_count: 5
  name: Qlikview Rate Limits
  slug: qlikview-rate-limits
score:
  band: thin
  composite: 29.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 32.3
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 29.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qlikview/refs/heads/main/screenshots/qlikview-2026-06-20T192347.png
security:
- kind: domain-security
  name: Qlikview Domain Security
  slug: qlikview-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Qlikview Trust Center
  slug: qlikview-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP
slug: qlikview
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Discovery
- Data Visualization
use_cases:
- description: Build interactive BI dashboards for sales, finance, and operations analytics.
  name: Business Intelligence Dashboards
- description: Embed QlikView analytics objects into existing web applications and portals.
  name: Embedded Analytics
- description: Schedule and distribute data-driven reports to stakeholders across the organization.
  name: Automated Reporting
- description: Enable self-service data discovery and exploration for business users.
  name: Data Discovery
- description: Build custom connectors to integrate QlikView with proprietary data sources.
  name: Custom Data Connectors
website: https://qlik.dev/
---
