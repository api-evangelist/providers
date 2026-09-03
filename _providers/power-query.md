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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: API and language reference for the M formula language used in Power Query for data transformation expressions and custom functions.
  name: Power Query M Formula Language
  slug: m-language
- description: API for building and managing custom data connectors for Power Query using the M language and Connector SDK.
  name: Power Query Connectors API
  slug: connectors-api
- description: API for managing and executing Power Query dataflows in Power Platform and Power BI for self-service ETL workflows.
  name: Power Query Dataflows API
  slug: dataflows-api
- description: Development toolkit for building custom Power Query connectors using Visual Studio Code, including project scaffolding, testing, and packaging of .mez connector files.
  name: Power Query SDK
  slug: sdk
- baseURL: https://api.fabric.microsoft.com/v1
  baseurl_source: declared
  description: REST API for the Microsoft Fabric Dataflow item - the productized Power Query mashup engine. Creates, reads, updates and deletes dataflows, publishes and retrieves their Power Query definitions, disco
  name: Fabric Dataflow REST API (Power Query)
  slug: fabric-api
artifact_total: 31
common:
- group: company
  title: ''
  type: Website
  url: https://powerquery.microsoft.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/power-query-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Microsoft/DataConnectors/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Microsoft/DataConnectors/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/microsoft/DataConnectors/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/microsoft/DataConnectors/blob/master/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Microsoft/DataConnectors/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power-query-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://app.powerbi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-query/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.microsoft.com/en-us/power-platform/products/power-bi/getting-started-with-power-bi
- group: company
  title: ''
  type: Blog
  url: https://powerbi.microsoft.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: operate
  title: ''
  type: Support
  url: https://powerbi.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://powerbi.microsoft.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://support.fabric.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: Signup
  url: https://www.microsoft.com/en-us/power-platform/products/power-bi/landing/free-account
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/powerquery
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCFp1vaKzpfvoGai0vE5VJ0w
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-change-log
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/rest/api/fabric/dataflow/items
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/powerquery-m/power-query-m-function-reference
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.fabric.microsoft.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/power-query-fabric-dataflow-swagger.json
- group: build
  title: ''
  type: Examples
  url: examples/fabric-dataflow/
- group: other
  title: ''
  type: Overlay
  url: overlays/power-query-fabric-dataflow-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/power-query-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/power-query-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/power-query-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/power-query-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/power-query-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/power-query-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/power-query-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/power-query-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/power-query-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/power-query-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/power-query-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/power-query-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/power-query-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/power-query-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/power-query-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/power-query-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/power-query-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/power-query-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/power-query-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/power-query-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/power-query-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/power-query-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/power-query-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/power-query-vocabulary.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/power-query-changelog.yml
created: '2024-01-01'
description: 'Power Query is Microsoft''s data connectivity and transformation engine, driven by the M formula language. It ships inside Excel, Power BI Desktop, Analysis Services, Azure Data Factory and Microsoft Fabric, and reaches 300+ data sources through built-in and custom connectors built with the MIT-licensed Power Query SDK. Its programmatic surface is the Microsoft Fabric Dataflow REST API on api.fabric.microsoft.com: thirteen Swagger-documented operations that create, read, update and delete dataflows, publish and retrieve their Power Query definitions, discover their parameters, schedule execute and applyChanges jobs, and execute an M query against a dataflow on demand. Authentication is Microsoft Entra ID OAuth 2.0 with delegated Dataflow.* and Item.* scopes layered on top of Fabric workspace roles.'
features:
- description: Powerful M formula language for complex data transformations including filtering, pivoting, merging, and custom functions.
  name: Data Transformation Engine
- description: Build custom data connectors using the Power Query SDK for connecting to any data source.
  name: Custom Connector Development
- description: Dataflows provide self-service ETL capabilities for business users without IT dependency.
  name: Self-Service ETL
- description: Pre-built connectors for databases, cloud services, files, and web APIs.
  name: 300+ Built-In Connectors
- description: Efficient data loading with incremental refresh policies for large datasets.
  name: Incremental Refresh
- description: Execute Power Query transformations programmatically in Microsoft Fabric pipelines.
  name: Microsoft Fabric Integration
finops:
- name: Power Query Finops
  service_category: API
  slug: power-query-finops
image: /assets/icons/power-query.png
integrations:
- description: Native integration with Power BI for data preparation and visualization workflows.
  name: Power BI
- description: Built-in Power Query editor in Excel for spreadsheet-based data transformation.
  name: Microsoft Excel
- description: Mapping data flows using Power Query transformations in Azure Data Factory.
  name: Azure Data Factory
- description: Programmatic execution of Power Query in Fabric notebooks and pipelines.
  name: Microsoft Fabric
- description: Direct connectivity and query folding optimization for SQL Server databases.
  name: SQL Server
jsonld:
- class_count: 35
  name: Power Query Context
  property_count: 12
  slug: power-query-context
layout: provider
mcp_servers:
- description: Microsoft does not publish a Power Query-specific or Fabric-specific MCP server. It does operate one official, anonymous, remote MCP server — the Microsoft Learn MCP Server — which indexes the whole o
  name: Microsoft Learn MCP Server
  slug: microsoft-learn-mcp-server
modified: '2026-08-29'
name: Power Query
nav: Providers
network: true
overview: 'Power Query publishes 1 API on the [APIs.io](https://apis.io/) network: Fabric Dataflow REST API (Power Query). Tagged areas include Business Intelligence, Data Integration, Data Transformation, ETL, and Microsoft.


  The Power Query catalog on APIs.io includes 1 JSON-LD context.


  Power Query''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, support, pricing, signup flow, and 47 more developer resources.'
plans:
- name: Power Query Plans Pricing
  plan_count: 6
  slug: power-query-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Power Query Rate Limits
  slug: power-query-rate-limits
scopes:
- name: Power Query Scopes
  scope_count: 0
  slug: power-query-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 80.1
  coverage:
    artifact_dirs: 26
    catalog_gap: 32.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 19.7
    contract_quality: 54.9
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 19.7
    operational_transparency: 89.5
  open_source:
    applies: true
    score: 75.0
  previous_composite: 80.1
  provenance:
    conformance: derived
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 71.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/power-query/refs/heads/main/screenshots/power-query-2026-06-20T192025.png
security:
- kind: authentication
  name: Power Query Authentication
  slug: power-query-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Power Query Domain Security
  slug: power-query-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Power Query Vulnerability Disclosure
  slug: power-query-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Power Query Trust Center
  slug: power-query-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO/IEC 42001, ISO 22301, ISO 9001, SOC 1, SOC 2, SOC 3, CSA STAR (attestation, certification, self-assessment), FedRAMP, FIPS 140-2, DoD IL2 / IL5, NIST 800-171, HIPAA / HITECH, HITRUST, PCI DSS, PCI 3DS, GxP / FDA CFR Title 21 Part 11, GDPR, DORA (EU), C5 (Germany), IRAP (Australia), ISMAP (Japan)
slug: power-query
tags:
- Business Intelligence
- Data Integration
- Data Transformation
- ETL
- Microsoft
- Microsoft Fabric
- Power BI
- Dataflows
- M Language
- Data Connectors
- Self-Service ETL
use_cases:
- description: Clean, transform, and shape data from multiple sources for analytics and reporting.
  name: Data Preparation
- description: Build reusable connectors for proprietary or specialized data sources.
  name: Custom Data Connectors
- description: Create scheduled dataflows for automated data refresh and transformation workflows.
  name: Automated Data Pipelines
- description: Integrate data across Power BI, Excel, Azure Data Factory, and Microsoft Fabric.
  name: Cross-Platform Data Integration
- description: Implement data quality rules and transformations for consistent enterprise data.
  name: Data Quality Management
website: https://powerquery.microsoft.com/
---
