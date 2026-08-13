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
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: OData-based REST API for querying SAP BW data, executing BEx queries, and accessing InfoProviders. Supports analytical queries with filtering, aggregation, and hierarchical navigation.
  name: SAP BW OData API
  slug: odata-api
- description: Business Application Programming Interfaces (BAPIs) and Remote Function Call (RFC) interfaces for SAP BW providing access to metadata management, data loading, process chain execution, and administrat
  name: SAP BW BAPI/RFC API
  slug: bapi-api
- description: API for SAP Analysis for Microsoft Office providing programmatic control of analytical workbooks, data source connections, and report automation within Excel and PowerPoint.
  name: SAP Analysis for Office API
  slug: analysis-office-api
artifact_total: 21
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-bw-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-bw-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP
- group: start
  title: ''
  type: Portal
  url: https://help.sap.com/docs/SAP_BW4HANA
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_BW4HANA
- group: start
  title: ''
  type: GettingStarted
  url: https://learning.sap.com/
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com/
- group: company
  title: ''
  type: Blog
  url: https://community.sap.com/topics/bw
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: learn
  title: ''
  type: Training
  url: https://learning.sap.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/sap-bw
created: '2024-01-01'
description: SAP Business Warehouse (SAP BW) and SAP BW/4HANA provide enterprise data warehousing capabilities with APIs for data extraction, query execution, metadata management, and integration with SAP and non-SAP systems. The platform offers OData services, BAPI/RFC interfaces, and Analysis Office APIs for programmatic access to data warehouse operations.
features:
- description: Centralized data warehousing with support for structured and unstructured data across SAP and non-SAP sources.
  name: Enterprise Data Warehousing
- description: Execute Business Explorer queries programmatically with filtering, hierarchies, and key figure calculations.
  name: BEx Query Execution
- description: Access SAP BW data through standard OData REST services for modern application integration.
  name: OData Query Access
- description: Automate and monitor ETL process chains for scheduled data loading and transformation.
  name: Process Chain Management
- description: Programmatic access to InfoProvider metadata, hierarchies, and data model definitions.
  name: Metadata Services
finops:
- name: Sap Bw Finops
  service_category: API
  slug: sap-bw-finops
image: /assets/icons/sap-bw.png
integrations:
- description: Integration with SAP Analytics Cloud for modern analytics and planning on BW data.
  name: SAP Analytics Cloud
- description: Native HANA optimization for SAP BW/4HANA with in-memory data processing.
  name: SAP HANA
- description: Analysis for Office integration for enterprise reporting directly in Excel.
  name: Microsoft Excel
- description: Data pipeline integration for connecting BW with data lakes and machine learning workloads.
  name: SAP Data Intelligence
layout: provider
modified: '2026-04-18'
name: SAP BW
nav: Providers
network: true
overview: 'SAP BW publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Business Intelligence, Data Warehousing, Enterprise, ETL, and SAP.


  SAP BW''s developer surface includes developer portal, documentation, getting-started guide, support, engineering blog, training material, Stack Overflow tag, and 5 more developer resources.'
plans:
- name: Sap Bw Plans Pricing
  plan_count: 3
  slug: sap-bw-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 5
  name: Sap Bw Rate Limits
  slug: sap-bw-rate-limits
score:
  band: emerging
  composite: 23.4
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 23.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-bw/refs/heads/main/screenshots/sap-bw-2026-06-20T193419.png
security:
- kind: domain-security
  name: Sap Bw Domain Security
  slug: sap-bw-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Bw Vulnerability Disclosure
  slug: sap-bw-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-bw
tags:
- Business Intelligence
- Data Warehousing
- Enterprise
- ETL
- SAP
use_cases:
- description: Build enterprise reports and dashboards connecting to SAP BW data through OData and BAPI interfaces.
  name: Enterprise Reporting
- description: Extract and load data between SAP BW and external systems using API-based integration.
  name: Data Integration
- description: Automate data warehouse loading processes with API-triggered process chain execution.
  name: Automated ETL Workflows
- description: Enable business users to access BW data through Analysis for Office API integrations.
  name: Self-Service Analytics
website: https://help.sap.com/docs/SAP_BW4HANA
---
