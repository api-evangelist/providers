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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-01'
api_count: 4
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
- description: SAP Information Access (InA) is the REST/HTTP JSON protocol SAP Analytics Cloud and SAP Analysis for Microsoft Office use to query SAP BW data sources in real time over a live connection. SAP document
  name: SAP BW InA API
  slug: ina-api
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/data-cloud/business-warehouse.html
- group: docs
  title: ''
  type: APIReference
  url: https://help.sap.com/docs/SAP_BW4HANA/107a6e8a38b74ede94c833ca3b7b6f51/4c22135610cc5791e10000000a15822b.html
- group: build
  title: ''
  type: Packages
  url: packages/sap-bw-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sap-bw-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sap-bw-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sap-bw-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.sap.com/about/trust-center/security/incident-management.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/sap-bw-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.sap.com/about/trust-center/certification-compliance.html
- group: design
  title: ''
  type: Conformance
  url: conformance/sap-bw-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-bw-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sap-bw-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sap-bw-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sap-bw-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: operate
  title: ''
  type: Deprecation
  url: https://help.sap.com/doc/16e3352bd6c342ec9fb1cd90adb9fbf4/2.0/en-US/SAP_BW4HANA_20_Simplification_List.pdf
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sap-bw-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sap-bw-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/sap-bw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sap-bw-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sap-bw-finops.yml
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
  url: https://pages.community.sap.com/topics/bw4-hana
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
modified: '2026-08-29'
name: SAP BW
nav: Providers
network: true
overview: 'SAP BW publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Business Intelligence, Data Warehousing, Enterprise, ETL, and SAP.


  SAP BW''s developer surface includes API reference, authentication, changelog, developer portal, documentation, getting-started guide, support, and 26 more developer resources.'
plans:
- name: Sap Bw Plans Pricing
  plan_count: 0
  slug: sap-bw-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Sap Bw Rate Limits
  slug: sap-bw-rate-limits
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 34.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-bw/refs/heads/main/screenshots/sap-bw-2026-06-20T193419.png
security:
- kind: authentication
  name: Sap Bw Authentication
  slug: sap-bw-authentication
  summary_line: http/apiKey/oauth2/mutualTLS · 6 schemes
- kind: domain-security
  name: Sap Bw Domain Security
  slug: sap-bw-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Bw Vulnerability Disclosure
  slug: sap-bw-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Sap Bw Trust Center
  slug: sap-bw-trust-center
  summary_line: SOC 1, SOC 2, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO 22301, ISO 9001, PCI DSS, FedRAMP, CSA STAR, TISAX, BSI C5, IRAP, ENS, GDPR
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
website: https://www.sap.com/products/data-cloud/business-warehouse.html
---
