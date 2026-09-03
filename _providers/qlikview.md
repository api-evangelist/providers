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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
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
artifact_total: 30
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
- group: company
  title: ''
  type: Website
  url: https://www.qlik.com/us/products/qlikview
- group: docs
  title: ''
  type: Documentation
  url: https://help.qlik.com/en-US/qlikview/September2025/Content/QV_HelpSites/Home.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://help.qlik.com/en-US/qlikview-developer/September2025/Content/QV_HelpSites/APIsAndSDKs.htm
- group: company
  title: ''
  type: Blog
  url: https://www.qlik.com/us/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/legal/privacy-and-cookie-notice
- group: auth
  title: ''
  type: Compliance
  url: https://www.qlik.com/us/trust
- group: auth
  title: ''
  type: Security
  url: security/qlikview-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qlikview-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/qlikview-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qlikview-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qlikview-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qlikview-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qlikview-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qlikview-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qlikview-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qlikview-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/qlikview-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qlikview-llms.txt
created: '2024-01-01'
description: 'QlikView is Qlik''s guided-analytics platform for business intelligence and data visualization, installed and run on the customer''s own Windows servers rather than consumed as a hosted service. Its patented associative in-memory engine lets users explore relationships across data sets, and its developer surface is a set of on-premises APIs and SDKs: the SOAP-based QlikView Management Service (QMS) API for administration, task and document distribution, the Ticket API for custom single sign-on, the AJAX/Qva JavaScript API and Workbench ASP.NET controls for embedding, and COM/OCX plus the QVX SDK for automation and custom data connectors. Still shipping - 12.100 (September 2025) is supported to 2027-09-30.'
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
modified: '2026-08-29'
name: QlikView
nav: Providers
network: true
overview: 'QlikView publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Discovery, and Data Visualization.


  QlikView''s developer surface includes developer portal, API reference, support, training material, pricing, release notes, documentation, and 22 more developer resources.'
plans:
- name: Qlikview Plans Pricing
  plan_count: 0
  slug: qlikview-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Qlikview Rate Limits
  slug: qlikview-rate-limits
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 39.0
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qlikview/refs/heads/main/screenshots/qlikview-2026-06-20T192347.png
security:
- kind: authentication
  name: Qlikview Authentication
  slug: qlikview-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Qlikview Domain Security
  slug: qlikview-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Qlikview Vulnerability Disclosure
  slug: qlikview-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Qlikview Trust Center
  slug: qlikview-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 42001:2023, SOC 1, SOC 2 + HITRUST CSF, SOC 3, HIPAA, TISAX, IRAP, Cyber Essentials, Cyber Essentials Plus, UK G-Cloud v14, CASA Tier 3, C5 (German BSI)
slug: qlikview
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Discovery
- Data Visualization
- Embedded Analytics
- On-Premises
- SOAP
- Guided Analytics
- Reporting
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
website: https://www.qlik.com/us/products/qlikview
---
