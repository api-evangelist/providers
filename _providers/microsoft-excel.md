---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Microsoft Excel Agentic Access
  operation_count: 23
  slug: microsoft-excel-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 1
apis:
- description: Office Add-ins API for building custom functionality within Excel using JavaScript and TypeScript.
  name: Excel JavaScript API
  slug: excel-javascript-api
- description: TypeScript-based automation for Excel on the web, enabling Power Automate integration for business process automation.
  name: Office Scripts API
  slug: office-scripts-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing charts within worksheets.
  name: Microsoft Excel Charts API
  slug: microsoft-excel-charts-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Workbook function operations.
  name: Microsoft Excel Functions API
  slug: microsoft-excel-functions-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing named ranges and values.
  name: Microsoft Excel Named Items API
  slug: microsoft-excel-named-items-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for reading and writing cell ranges.
  name: Microsoft Excel Ranges API
  slug: microsoft-excel-ranges-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Workbook session management operations.
  name: Microsoft Excel Sessions API
  slug: microsoft-excel-sessions-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing table columns.
  name: Microsoft Excel Table Columns API
  slug: microsoft-excel-table-columns-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing table row data.
  name: Microsoft Excel Table Rows API
  slug: microsoft-excel-table-rows-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing tables within worksheets.
  name: Microsoft Excel Tables API
  slug: microsoft-excel-tables-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations for managing worksheets within a workbook.
  name: Microsoft Excel Worksheets API
  slug: microsoft-excel-worksheets-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The drives.drive.Actions API from Microsoft Excel — 135 operation(s) for drives.drive.actions.
  name: Microsoft Excel Drives.drive.Actions API
  slug: microsoft-excel-drives-drive-actions-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The drives.drive.Functions API from Microsoft Excel — 596 operation(s) for drives.drive.functions.
  name: Microsoft Excel Drives.drive.Functions API
  slug: microsoft-excel-drives-drive-functions-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The drives.driveItem API from Microsoft Excel — 711 operation(s) for drives.driveitem.
  name: Microsoft Excel Drives.drive Item API
  slug: microsoft-excel-drives-driveitem-api
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
artifact_total: 98
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
- collection_type: open
  name: Microsoft Graph Excel Charts API
  slug: open-microsoft-excel-charts-api
- collection_type: open
  name: Microsoft Graph Excel Charts Functions API
  slug: open-microsoft-excel-functions-api
- collection_type: open
  name: Microsoft Graph Excel Charts Named Items API
  slug: open-microsoft-excel-named-items-api
- collection_type: open
  name: Microsoft Graph Excel Charts Ranges API
  slug: open-microsoft-excel-ranges-api
- collection_type: open
  name: Microsoft Graph Excel Charts Sessions API
  slug: open-microsoft-excel-sessions-api
- collection_type: open
  name: Microsoft Graph Excel Charts Table Columns API
  slug: open-microsoft-excel-table-columns-api
- collection_type: open
  name: Microsoft Graph Excel Charts Table Rows API
  slug: open-microsoft-excel-table-rows-api
- collection_type: open
  name: Microsoft Graph Excel Charts Tables API
  slug: open-microsoft-excel-tables-api
- collection_type: open
  name: Microsoft Graph Excel Charts Worksheets API
  slug: open-microsoft-excel-worksheets-api
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/excel-quickstart-jquery
- group: design
  href: https://artifacts.apis.io/microsoft-excel/rules/microsoft-excel-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-excel-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/rules/microsoft-excel-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-excel-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/rules/microsoft-excel-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-excel-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/json-ld/microsoft-excel-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-excel-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-excel/vocabulary/microsoft-excel-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-excel-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-excel/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support
- group: other
  href: https://artifacts.apis.io/microsoft-excel/hosts/microsoft-excel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-excel-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-excel/integrations/microsoft-excel-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-excel-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-excel/vendors/microsoft-excel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-excel-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://docs.microsoft.com/
- group: commercial
  href: https://artifacts.apis.io/microsoft-excel/plans/microsoft-excel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-excel-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-excel/rate-limits/microsoft-excel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-excel-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-excel/finops/microsoft-excel-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-excel-finops.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dev.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-excel/overview
- group: agent
  href: https://artifacts.apis.io/microsoft-excel/agentic-access/microsoft-excel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-excel-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-excel/security/microsoft-excel-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-excel-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-excel/security/microsoft-excel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-excel-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-excel/authentication/microsoft-excel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-excel-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-excel/scopes/microsoft-excel-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-excel-scopes.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-excel/security/microsoft-excel-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-excel-trust-center.yml
- group: build
  href: https://artifacts.apis.io/microsoft-excel/packages/microsoft-excel-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-excel-packages.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-excel/well-known/microsoft-excel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-excel-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-excel/well-known/microsoft-excel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-excel-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-excel/mcp/microsoft-excel-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/microsoft-excel-mcp.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-excel/llms/microsoft-excel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-excel-llms.txt
- group: other
  href: https://artifacts.apis.io/microsoft-excel/overlays/microsoft-excel-graph-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-excel-graph-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/conformance/microsoft-excel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-excel-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/errors/microsoft-excel-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-excel-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/lifecycle/microsoft-excel-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-excel-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/conventions/microsoft-excel-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-excel-conventions.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-excel/changelog/microsoft-excel-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-excel-changelog.yml
- group: build
  href: https://artifacts.apis.io/microsoft-excel/cli/microsoft-excel-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-excel-cli.yml
- group: start
  href: https://artifacts.apis.io/microsoft-excel/sandbox/microsoft-excel-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-excel-sandbox.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/data-model/microsoft-excel-data-model.yml
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
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-append-table-row-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-append-table-row-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-build-chart-from-range-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-build-chart-from-range-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-convert-table-to-range-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-convert-table-to-range-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-create-worksheet-seed-data-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-create-worksheet-seed-data-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-discover-workbook-structure-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-discover-workbook-structure-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-named-range-write-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-named-range-write-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-prepare-table-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-prepare-table-report-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-prune-table-row-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-prune-table-row-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-session-range-update-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-session-range-update-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-table-column-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-table-column-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-workbook-function-calc-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-workbook-function-calc-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/arazzo/microsoft-excel-worksheet-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-excel-worksheet-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/rules/microsoft-excel-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/microsoft-excel-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-excel/vocabulary/microsoft-excel-vocabulary.yaml
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
- has_sources: true
  method: generated
  name: Microsoft Excel Finops
  primary_unit: ''
  service_category: Productivity
  slug: microsoft-excel-finops
  template: false
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
- name: microsoft.graph.workbookChartAxis
  property_count: 10
  slug: microsoft-excel-microsoft-graph-workbook-chart-axis
- name: microsoft.graph.workbookChart
  property_count: 14
  slug: microsoft-excel-microsoft-graph-workbook-chart
- name: microsoft.graph.workbookRangeFormat
  property_count: 11
  slug: microsoft-excel-microsoft-graph-workbook-range-format
- name: microsoft.graph.workbookRange
  property_count: 22
  slug: microsoft-excel-microsoft-graph-workbook-range
- name: microsoft.graph.workbookRangeView
  property_count: 14
  slug: microsoft-excel-microsoft-graph-workbook-range-view
- name: microsoft.graph.workbookTable
  property_count: 16
  slug: microsoft-excel-microsoft-graph-workbook-table
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
- class_count: 30
  name: Microsoft Excel Context
  property_count: 61
  slug: microsoft-excel-context
- class_count: 9
  name: Microsoft Excel Graph Api Context
  property_count: 20
  slug: microsoft-excel-graph-api-context
layout: provider
modified: '2026-06-20'
name: Microsoft Excel
nav: Providers
network: true
overview: 'Microsoft Excel publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Charts API, Functions API, Named Items API, and 11 more. Tagged areas include Automation, Data Analysis, Microsoft, Microsoft 365, and Office.


  The Microsoft Excel catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Microsoft Excel''s developer surface includes getting-started guide, documentation, authentication, changelog, CLI, sandbox, support, and 55 more developer resources.'
plans:
- name: Microsoft Excel Plans Pricing
  plan_count: 5
  slug: microsoft-excel-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Microsoft Excel Rate Limits
  slug: microsoft-excel-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Microsoft Excel — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-excel-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Microsoft Excel API Rules
  rule_count: 64
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 9
  slug: microsoft-excel-rules
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: Microsoft Excel API Rules
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
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 39
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.3
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 30.1
    developer_ergonomics: 81.5
    discoverability: 58.9
    operational_transparency: 52.6
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 76.9
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-excel/microsoft-excel-2026-06-20T185500.png
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
skill_count: 3
skills:
- name: microsoft-excel-append-table-rows
  slug: microsoft-excel-append-table-rows
- name: microsoft-excel-build-chart
  slug: microsoft-excel-build-chart
- name: microsoft-excel-read-worksheet-range
  slug: microsoft-excel-read-worksheet-range
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
website: https://www.microsoft.com/
---
