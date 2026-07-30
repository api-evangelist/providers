---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Microsoft Excel Agentic Access
  operation_count: 23
  slug: microsoft-excel-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 11
apis:
- description: Office Add-ins API for building custom functionality within Excel using JavaScript and TypeScript.
  name: Excel JavaScript API
  slug: excel-javascript-api
- description: TypeScript-based automation for Excel on the web, enabling Power Automate integration for business process automation.
  name: Office Scripts API
  slug: office-scripts-api
- description: Operations for managing charts within worksheets.
  name: Microsoft Excel Charts API
  slug: microsoft-excel-charts-api
- description: Workbook function operations.
  name: Microsoft Excel Functions API
  slug: microsoft-excel-functions-api
- description: Operations for managing named ranges and values.
  name: Microsoft Excel Named Items API
  slug: microsoft-excel-named-items-api
- description: Operations for reading and writing cell ranges.
  name: Microsoft Excel Ranges API
  slug: microsoft-excel-ranges-api
- description: Workbook session management operations.
  name: Microsoft Excel Sessions API
  slug: microsoft-excel-sessions-api
- description: Operations for managing table columns.
  name: Microsoft Excel Table Columns API
  slug: microsoft-excel-table-columns-api
- description: Operations for managing table row data.
  name: Microsoft Excel Table Rows API
  slug: microsoft-excel-table-rows-api
- description: Operations for managing tables within worksheets.
  name: Microsoft Excel Tables API
  slug: microsoft-excel-tables-api
- description: Operations for managing worksheets within a workbook.
  name: Microsoft Excel Worksheets API
  slug: microsoft-excel-worksheets-api
arazzos:
- description: Resolve a table on a worksheet, confirm its column shape, append a row, and read it back.
  name: Microsoft Excel Append a Row to a Table
  slug: microsoft-excel-append-table-row-workflow
- description: Verify a source range has data, create a chart over it, and confirm the chart exists.
  name: Microsoft Excel Build a Chart from a Data Range
  slug: microsoft-excel-build-chart-from-range-workflow
- description: Snapshot a table's rows and columns, convert it to a static range, and read the flattened cells.
  name: Microsoft Excel Flatten a Table into a Plain Range
  slug: microsoft-excel-convert-table-to-range-workflow
- description: Add a new worksheet to a workbook, write a header and data block into it, and read it back.
  name: Microsoft Excel Create a Worksheet and Seed It with Data
  slug: microsoft-excel-create-worksheet-seed-data-workflow
- description: Open a session and inventory a workbook's worksheets, tables, named items, and charts.
  name: Microsoft Excel Discover Workbook Structure
  slug: microsoft-excel-discover-workbook-structure-workflow
- description: Resolve a workbook's named items, read the range a name points at, and write values through it.
  name: Microsoft Excel Write Through a Named Range
  slug: microsoft-excel-named-range-write-workflow
- description: Resolve a table's columns, sort it, filter a column, and switch on the totals row.
  name: Microsoft Excel Sort, Filter, and Total a Table for Reporting
  slug: microsoft-excel-prepare-table-report-workflow
- description: Read a table's rows, delete one by its zero-based index, and confirm the removal.
  name: Microsoft Excel Delete a Table Row by Index
  slug: microsoft-excel-prune-table-row-workflow
- description: Open a persisting session, read a range, write new values, and read the range back.
  name: Microsoft Excel Read, Write, and Verify a Cell Range
  slug: microsoft-excel-session-range-update-workflow
- description: Inspect a table's columns, insert a new column at a position, verify it, then remove it.
  name: Microsoft Excel Add and Retire a Table Column
  slug: microsoft-excel-table-column-lifecycle-workflow
- description: Read input cells, invoke an Excel function as a calculation engine, and write the result back.
  name: Microsoft Excel Calculate with a Workbook Function and Write the Result
  slug: microsoft-excel-workbook-function-calc-workflow
- description: Create a temporary worksheet, read it, rename and reposition it, then delete it.
  name: Microsoft Excel Scratch Worksheet Lifecycle
  slug: microsoft-excel-worksheet-lifecycle-workflow
artifact_total: 76
collections:
- collection_type: postman
  name: Microsoft Graph Excel Charts API
  slug: postman-microsoft-excel-charts-api
- collection_type: postman
  name: Microsoft Graph Excel Charts Functions API
  slug: postman-microsoft-excel-functions-api
- collection_type: postman
  name: Microsoft Graph Excel Charts Named Items API
  slug: postman-microsoft-excel-named-items-api
- collection_type: postman
  name: Microsoft Graph Excel Charts Ranges API
  slug: postman-microsoft-excel-ranges-api
- collection_type: postman
  name: Microsoft Graph Excel Charts Sessions API
  slug: postman-microsoft-excel-sessions-api
- collection_type: postman
  name: Microsoft Graph Excel Charts Table Columns API
  slug: postman-microsoft-excel-table-columns-api
- collection_type: postman
  name: Microsoft Graph Excel Charts Table Rows API
  slug: postman-microsoft-excel-table-rows-api
- collection_type: postman
  name: Microsoft Graph Excel Charts Tables API
  slug: postman-microsoft-excel-tables-api
- collection_type: postman
  name: Microsoft Graph Excel Charts Worksheets API
  slug: postman-microsoft-excel-worksheets-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-excel/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-excel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-excel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-excel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-excel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-excel-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-excel-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-excel-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-excel-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-excel-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-excel-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-excel-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-excel-graph-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-excel-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-excel-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-excel-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-excel-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-excel-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-excel-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-excel-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-excel-data-model.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/excel
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/excel
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/excel-blog/bg-p/ExcelBlog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-append-table-row-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-build-chart-from-range-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-convert-table-to-range-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-create-worksheet-seed-data-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-discover-workbook-structure-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-named-range-write-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-prepare-table-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-prune-table-row-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-session-range-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-table-column-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-workbook-function-calc-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-worksheet-lifecycle-workflow.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-excel-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-excel-vocabulary.yaml
created: '2024'
description: APIs for automating, integrating, and extending Microsoft Excel functionality including workbook management, data manipulation, charting, and formula execution through Microsoft Graph REST APIs.
examples:
- key_count: 6
  name: Excel Graph Api Chart Example
  slug: excel-graph-api-chart-example
- key_count: 4
  name: Excel Graph Api Named Item Example
  slug: excel-graph-api-named-item-example
- key_count: 12
  name: Excel Graph Api Range Example
  slug: excel-graph-api-range-example
- key_count: 4
  name: Excel Graph Api Table Column Example
  slug: excel-graph-api-table-column-example
- key_count: 5
  name: Excel Graph Api Table Example
  slug: excel-graph-api-table-example
- key_count: 2
  name: Excel Graph Api Table Row Example
  slug: excel-graph-api-table-row-example
- key_count: 4
  name: Excel Graph Api Worksheet Example
  slug: excel-graph-api-worksheet-example
features:
- description: Persistent and non-persistent sessions for efficient API operations.
  name: Workbook Sessions
- description: Read, write, and format individual cells or ranges of cells.
  name: Cell Range Operations
- description: Create, update, sort, and filter structured tables.
  name: Table Management
- description: Create and manage charts with customizable source data.
  name: Chart Generation
- description: Invoke Excel functions programmatically via the API.
  name: Workbook Functions
- description: Define and manage named ranges for reusable cell references.
  name: Named Ranges
finops:
- name: Microsoft Excel Finops
  service_category: Productivity
  slug: microsoft-excel-finops
image: https://learn.microsoft.com/en-us/graph/images/excel-logo.png
json_schemas:
- name: Chart
  property_count: 6
  slug: excel-graph-api-chart
- name: NamedItem
  property_count: 4
  slug: excel-graph-api-named-item
- name: Range
  property_count: 13
  slug: excel-graph-api-range
- name: TableColumn
  property_count: 4
  slug: excel-graph-api-table-column
- name: TableRow
  property_count: 2
  slug: excel-graph-api-table-row
- name: Table
  property_count: 5
  slug: excel-graph-api-table
- name: Worksheet
  property_count: 4
  slug: excel-graph-api-worksheet
json_structures:
- name: Excel Graph Api Chart Structure
  property_count: 6
  slug: excel-graph-api-chart-structure
- name: Excel Graph Api Named Item Structure
  property_count: 4
  slug: excel-graph-api-named-item-structure
- name: Excel Graph Api Range Structure
  property_count: 8
  slug: excel-graph-api-range-structure
- name: Excel Graph Api Table Column Structure
  property_count: 4
  slug: excel-graph-api-table-column-structure
- name: Excel Graph Api Table Row Structure
  property_count: 2
  slug: excel-graph-api-table-row-structure
- name: Excel Graph Api Table Structure
  property_count: 5
  slug: excel-graph-api-table-structure
- name: Excel Graph Api Worksheet Structure
  property_count: 4
  slug: excel-graph-api-worksheet-structure
jsonld:
- class_count: 9
  name: Microsoft Excel Graph Api Context
  property_count: 20
  slug: microsoft-excel-graph-api-context
layout: provider
mcp_servers:
- description: ''
  name: microsoft-excel-mcp.yml
  slug: microsoft-excel-mcpyml
modified: '2026-06-20'
name: Microsoft Excel
nav: Providers
network: true
overview: 'Microsoft Excel publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Charts API, Functions API, Named Items API, and 6 more. Tagged areas include Automation, Data Analysis, Microsoft, Microsoft 365, and Office.


  The Microsoft Excel catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Excel''s developer surface includes authentication, changelog, CLI, sandbox, support, pricing, engineering blog, and 35 more developer resources.'
plans:
- name: Microsoft Excel Plans Pricing
  plan_count: 5
  slug: microsoft-excel-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 3
  name: Microsoft Excel Rate Limits
  slug: microsoft-excel-rate-limits
rules:
- name: Microsoft Excel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-excel-jsonschema-spectral-rules
- name: Microsoft Excel API Rules
  rule_count: 29
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 11
  slug: microsoft-excel-spectral-rules
scopes:
- name: Microsoft Excel Scopes
  scope_count: 6
  slug: microsoft-excel-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: exemplar
  composite: 66.7
  delta: -4.8
  facets:
    commercial_clarity: 78.9
    contract_quality: 68.1
    developer_ergonomics: 45.7
    discoverability: 83.3
    governance: 80.2
    operational_transparency: 52.6
  previous_composite: 71.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-excel/refs/heads/main/screenshots/microsoft-excel-2026-06-20T185500.png
security:
- kind: authentication
  name: Microsoft Excel Authentication
  slug: microsoft-excel-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Excel Domain Security
  slug: microsoft-excel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Excel Vulnerability Disclosure
  slug: microsoft-excel-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Excel Trust Center
  slug: microsoft-excel-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 27701, PCI DSS, HIPAA / HITRUST, FedRAMP, GDPR, CSA STAR
slug: microsoft-excel
tags:
- Automation
- Data Analysis
- Microsoft
- Microsoft 365
- Office
- Spreadsheets
use_cases:
- description: Generate and update Excel reports from external data sources.
  name: Automated Reporting
- description: Programmatically insert and update data in spreadsheets.
  name: Data Entry Automation
- description: Use Excel functions API for financial calculations.
  name: Financial Modeling
- description: Create charts and visualizations from data.
  name: Dashboard Generation
website: https://developer.microsoft.com/en-us/microsoft-365
---
