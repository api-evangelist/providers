---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Google Sheets Agentic Access
  operation_count: 17
  slug: google-sheets-agentic-access
  summary_line: 17 operations · 13 acting
api_count: 5
apis:
- description: The built-in Google Apps Script Spreadsheet Service allows creation, access, and modification of Google Sheets files directly from Apps Script with performance bundling and numerous classes for format
  name: Google Apps Script Spreadsheet Service
  slug: google-apps-script-spreadsheet-service
- description: Operations on developer metadata
  name: Google Sheets developerMetadata API
  slug: google-sheets-developermetadata-api
- description: Operations on individual sheets within a spreadsheet
  name: Google Sheets Sheets API
  slug: google-sheets-sheets-api
- description: Operations on spreadsheet resources
  name: Google Sheets Spreadsheets API
  slug: google-sheets-spreadsheets-api
- description: Operations on spreadsheet cell values
  name: Google Sheets Values API
  slug: google-sheets-values-api
arazzos:
- description: Create a spreadsheet, append rows including a header, then bold the header row via batchUpdate.
  name: Google Sheets Append Rows and Format the Header
  slug: google-sheets-append-and-format-header-workflow
- description: Read several ranges as an archive, clear them all in one batch, then re-read to confirm they are empty.
  name: Google Sheets Archive and Clear Multiple Ranges
  slug: google-sheets-archive-and-clear-multiple-ranges-workflow
- description: Create a spreadsheet, write several ranges in one batch, then read them all back in one batch.
  name: Google Sheets Bulk Load Multiple Ranges
  slug: google-sheets-bulk-load-multiple-ranges-workflow
- description: Read a source spreadsheet, copy one of its sheets into a destination spreadsheet, then confirm the destination.
  name: Google Sheets Copy a Sheet Between Spreadsheets
  slug: google-sheets-copy-sheet-between-spreadsheets-workflow
- description: Create a new spreadsheet, append seed rows to it, then read them back.
  name: Google Sheets Create and Seed a Spreadsheet
  slug: google-sheets-create-and-seed-spreadsheet-workflow
- description: Create a spreadsheet, add a second named sheet to it, then write values into that sheet.
  name: Google Sheets Create With an Extra Sheet and Write
  slug: google-sheets-create-with-extra-sheet-and-write-workflow
- description: Create a spreadsheet, write values into a range, then read the range back to verify the write.
  name: Google Sheets Create, Write, and Verify
  slug: google-sheets-create-write-and-verify-workflow
- description: Inspect a range and branch — overwrite it in place when it already has data, otherwise append fresh rows.
  name: Google Sheets Overwrite or Append Rows
  slug: google-sheets-overwrite-or-append-rows-workflow
- description: Read the current values of a range, clear it, then write a fresh set of values into it.
  name: Google Sheets Refresh a Range
  slug: google-sheets-refresh-range-workflow
- description: Read a range and branch — write seed values only when the range has no existing data.
  name: Google Sheets Seed a Range Only If Empty
  slug: google-sheets-seed-if-empty-workflow
- description: Create a spreadsheet, attach a developer metadata tag via batchUpdate, then search for it by key.
  name: Google Sheets Tag and Find a Spreadsheet With Developer Metadata
  slug: google-sheets-tag-and-find-developer-metadata-workflow
- description: Resolve a spreadsheet via a data filter, update matching ranges by filter, then read them back by filter.
  name: Google Sheets Update and Read Values by Data Filter
  slug: google-sheets-update-and-read-by-data-filter-workflow
artifact_total: 314
collections:
- collection_type: postman
  name: Google Sheets API
  slug: postman-google-sheets
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Sheets developerMetadata API
  slug: open-google-sheets-developermetadata-api
- collection_type: open
  name: Google developerMetadata Sheets API
  slug: open-google-sheets-sheets-api
- collection_type: open
  name: Google Sheets developerMetadata Spreadsheets API
  slug: open-google-sheets-spreadsheets-api
- collection_type: open
  name: Google Sheets developerMetadata Values API
  slug: open-google-sheets-values-api
- collection_type: open
  name: Google Sheets API
  slug: open-google-sheets
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-sheets-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-sheets-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-sheets-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-sheets-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-sheets-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/google-sheets-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-sheets-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-sheets-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-sheets-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/google-sheets-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-sheets-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-sheets-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-sheets-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-sheets-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-sheets-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-sheets-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-sheets/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-append-and-format-header-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-archive-and-clear-multiple-ranges-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-bulk-load-multiple-ranges-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-copy-sheet-between-spreadsheets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-create-and-seed-spreadsheet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-create-with-extra-sheet-and-write-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-create-write-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-overwrite-or-append-rows-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-refresh-range-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-seed-if-empty-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-tag-and-find-developer-metadata-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-sheets-update-and-read-by-data-filter-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/workspace/sheets/api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/workspace/sheets/api/reference/rest
- group: company
  title: ''
  type: Blog
  url: https://workspace.google.com/blog/developers-practitioners
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/sheets/api/support
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: Signup
  url: https://console.cloud.google.com/
- group: start
  title: ''
  type: Login
  url: https://console.cloud.google.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-sheets-api
- group: learn
  title: ''
  type: YouTube
  url: https://developers.google.com/workspace/sheets/api/videos
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/sheets/api/guides/concepts
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/sheets/api/guides/authorizing
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/workspace/sheets/api/guides/libraries
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.google.com/workspace/sheets/release-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/workspace/sheets/api/limits
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.google.com/workspace/sheets/api/limits
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-sheets-spectral-rules.yml
created: '2024-01-01'
description: API for reading, writing, and formatting data in Google Sheets.
examples:
- key_count: 2
  name: Google Sheets Append Values Response Example
  slug: google-sheets-append-values-response-example
- key_count: 1
  name: Google Sheets Banded Range Example
  slug: google-sheets-banded-range-example
- key_count: 0
  name: Google Sheets Banding Properties Example
  slug: google-sheets-banding-properties-example
- key_count: 3
  name: Google Sheets Basic Filter Example
  slug: google-sheets-basic-filter-example
- key_count: 2
  name: Google Sheets Batch Clear Values By Data Filter Response Example
  slug: google-sheets-batch-clear-values-by-data-filter-response-example
- key_count: 2
  name: Google Sheets Batch Clear Values Response Example
  slug: google-sheets-batch-clear-values-response-example
- key_count: 2
  name: Google Sheets Batch Get Values By Data Filter Response Example
  slug: google-sheets-batch-get-values-by-data-filter-response-example
- key_count: 2
  name: Google Sheets Batch Get Values Response Example
  slug: google-sheets-batch-get-values-response-example
- key_count: 4
  name: Google Sheets Batch Update Spreadsheet Request Example
  slug: google-sheets-batch-update-spreadsheet-request-example
- key_count: 2
  name: Google Sheets Batch Update Spreadsheet Response Example
  slug: google-sheets-batch-update-spreadsheet-response-example
- key_count: 6
  name: Google Sheets Batch Update Values By Data Filter Response Example
  slug: google-sheets-batch-update-values-by-data-filter-response-example
- key_count: 2
  name: Google Sheets Batch Update Values Request Example
  slug: google-sheets-batch-update-values-request-example
- key_count: 6
  name: Google Sheets Batch Update Values Response Example
  slug: google-sheets-batch-update-values-response-example
- key_count: 3
  name: Google Sheets Big Query Data Source Spec Example
  slug: google-sheets-big-query-data-source-spec-example
- key_count: 2
  name: Google Sheets Boolean Condition Example
  slug: google-sheets-boolean-condition-example
- key_count: 2
  name: Google Sheets Border Example
  slug: google-sheets-border-example
- key_count: 0
  name: Google Sheets Borders Example
  slug: google-sheets-borders-example
- key_count: 4
  name: Google Sheets Cell Data Example
  slug: google-sheets-cell-data-example
- key_count: 5
  name: Google Sheets Cell Format Example
  slug: google-sheets-cell-format-example
- key_count: 2
  name: Google Sheets Clear Values Response Example
  slug: google-sheets-clear-values-response-example
- key_count: 4
  name: Google Sheets Color Example
  slug: google-sheets-color-example
- key_count: 1
  name: Google Sheets Color Style Example
  slug: google-sheets-color-style-example
- key_count: 2
  name: Google Sheets Condition Value Example
  slug: google-sheets-condition-value-example
- key_count: 3
  name: Google Sheets Conditional Format Rule Example
  slug: google-sheets-conditional-format-rule-example
- key_count: 4
  name: Google Sheets Data Execution Status Example
  slug: google-sheets-data-execution-status-example
- key_count: 1
  name: Google Sheets Data Filter Example
  slug: google-sheets-data-filter-example
- key_count: 1
  name: Google Sheets Data Filter Value Range Example
  slug: google-sheets-data-filter-value-range-example
- key_count: 1
  name: Google Sheets Data Source Column Example
  slug: google-sheets-data-source-column-example
- key_count: 1
  name: Google Sheets Data Source Column Reference Example
  slug: google-sheets-data-source-column-reference-example
- key_count: 3
  name: Google Sheets Data Source Example
  slug: google-sheets-data-source-example
- key_count: 1
  name: Google Sheets Data Source Formula Example
  slug: google-sheets-data-source-formula-example
- key_count: 2
  name: Google Sheets Data Source Parameter Example
  slug: google-sheets-data-source-parameter-example
- key_count: 6
  name: Google Sheets Data Source Refresh Schedule Example
  slug: google-sheets-data-source-refresh-schedule-example
- key_count: 2
  name: Google Sheets Data Source Sheet Properties Example
  slug: google-sheets-data-source-sheet-properties-example
- key_count: 1
  name: Google Sheets Data Source Spec Example
  slug: google-sheets-data-source-spec-example
- key_count: 6
  name: Google Sheets Data Source Table Example
  slug: google-sheets-data-source-table-example
- key_count: 3
  name: Google Sheets Data Validation Rule Example
  slug: google-sheets-data-validation-rule-example
- key_count: 0
  name: Google Sheets Date Time Render Option Example
  slug: google-sheets-date-time-render-option-example
- key_count: 4
  name: Google Sheets Developer Metadata Example
  slug: google-sheets-developer-metadata-example
- key_count: 3
  name: Google Sheets Developer Metadata Location Example
  slug: google-sheets-developer-metadata-location-example
- key_count: 6
  name: Google Sheets Developer Metadata Lookup Example
  slug: google-sheets-developer-metadata-lookup-example
- key_count: 0
  name: Google Sheets Dimension Example
  slug: google-sheets-dimension-example
- key_count: 4
  name: Google Sheets Dimension Properties Example
  slug: google-sheets-dimension-properties-example
- key_count: 3
  name: Google Sheets Dimension Range Example
  slug: google-sheets-dimension-range-example
- key_count: 2
  name: Google Sheets Embedded Chart Example
  slug: google-sheets-embedded-chart-example
- key_count: 3
  name: Google Sheets Embedded Object Position Example
  slug: google-sheets-embedded-object-position-example
- key_count: 1
  name: Google Sheets Error Response Example
  slug: google-sheets-error-response-example
- key_count: 2
  name: Google Sheets Error Value Example
  slug: google-sheets-error-value-example
- key_count: 4
  name: Google Sheets Extended Value Example
  slug: google-sheets-extended-value-example
- key_count: 1
  name: Google Sheets Filter Criteria Example
  slug: google-sheets-filter-criteria-example
- key_count: 1
  name: Google Sheets Filter Spec Example
  slug: google-sheets-filter-spec-example
- key_count: 6
  name: Google Sheets Filter View Example
  slug: google-sheets-filter-view-example
- key_count: 3
  name: Google Sheets Grid Coordinate Example
  slug: google-sheets-grid-coordinate-example
- key_count: 5
  name: Google Sheets Grid Data Example
  slug: google-sheets-grid-data-example
- key_count: 7
  name: Google Sheets Grid Properties Example
  slug: google-sheets-grid-properties-example
- key_count: 5
  name: Google Sheets Grid Range Example
  slug: google-sheets-grid-range-example
- key_count: 2
  name: Google Sheets Interpolation Point Example
  slug: google-sheets-interpolation-point-example
- key_count: 2
  name: Google Sheets Iterative Calculation Settings Example
  slug: google-sheets-iterative-calculation-settings-example
- key_count: 1
  name: Google Sheets Link Example
  slug: google-sheets-link-example
- key_count: 2
  name: Google Sheets Named Range Example
  slug: google-sheets-named-range-example
- key_count: 2
  name: Google Sheets Number Format Example
  slug: google-sheets-number-format-example
- key_count: 4
  name: Google Sheets Padding Example
  slug: google-sheets-padding-example
- key_count: 2
  name: Google Sheets Pivot Filter Criteria Example
  slug: google-sheets-pivot-filter-criteria-example
- key_count: 1
  name: Google Sheets Pivot Filter Spec Example
  slug: google-sheets-pivot-filter-spec-example
- key_count: 5
  name: Google Sheets Pivot Group Example
  slug: google-sheets-pivot-group-example
- key_count: 2
  name: Google Sheets Pivot Group Limit Example
  slug: google-sheets-pivot-group-limit-example
- key_count: 3
  name: Google Sheets Pivot Group Rule Example
  slug: google-sheets-pivot-group-rule-example
- key_count: 2
  name: Google Sheets Pivot Group Sort Value Bucket Example
  slug: google-sheets-pivot-group-sort-value-bucket-example
- key_count: 7
  name: Google Sheets Pivot Table Example
  slug: google-sheets-pivot-table-example
- key_count: 5
  name: Google Sheets Pivot Value Example
  slug: google-sheets-pivot-value-example
- key_count: 7
  name: Google Sheets Protected Range Example
  slug: google-sheets-protected-range-example
- key_count: 1
  name: Google Sheets Row Data Example
  slug: google-sheets-row-data-example
- key_count: 8
  name: Google Sheets Sheet Example
  slug: google-sheets-sheet-example
- key_count: 6
  name: Google Sheets Sheet Properties Example
  slug: google-sheets-sheet-properties-example
- key_count: 2
  name: Google Sheets Slicer Example
  slug: google-sheets-slicer-example
- key_count: 2
  name: Google Sheets Sort Spec Example
  slug: google-sheets-sort-spec-example
- key_count: 7
  name: Google Sheets Spreadsheet Example
  slug: google-sheets-spreadsheet-example
- key_count: 5
  name: Google Sheets Spreadsheet Properties Example
  slug: google-sheets-spreadsheet-properties-example
- key_count: 2
  name: Google Sheets Spreadsheet Theme Example
  slug: google-sheets-spreadsheet-theme-example
- key_count: 6
  name: Google Sheets Text Format Example
  slug: google-sheets-text-format-example
- key_count: 1
  name: Google Sheets Text Format Run Example
  slug: google-sheets-text-format-run-example
- key_count: 2
  name: Google Sheets Text Rotation Example
  slug: google-sheets-text-rotation-example
- key_count: 5
  name: Google Sheets Update Values Response Example
  slug: google-sheets-update-values-response-example
- key_count: 0
  name: Google Sheets Value Input Option Example
  slug: google-sheets-value-input-option-example
- key_count: 2
  name: Google Sheets Value Range Example
  slug: google-sheets-value-range-example
- key_count: 0
  name: Google Sheets Value Render Option Example
  slug: google-sheets-value-render-option-example
features:
- description: Create, read, update, and delete spreadsheets programmatically with full control over properties and metadata.
  name: Spreadsheet Management
- description: Read and write individual cell values, ranges, and batch operations across multiple ranges.
  name: Cell Value Operations
- description: Apply rich formatting to cells including fonts, colors, borders, alignment, and number formats.
  name: Formatting
- description: Add, remove, copy, and configure individual sheets within a spreadsheet.
  name: Sheet Management
- description: Attach custom metadata to spreadsheets, sheets, rows, and columns for application-specific data.
  name: Developer Metadata
- description: Set validation rules on cells to enforce data quality and consistency.
  name: Data Validation
- description: Apply conditional formatting rules based on cell values and formulas.
  name: Conditional Formatting
- description: Create and manage embedded charts within spreadsheets.
  name: Charts and Graphs
- description: Define and manage named ranges for easier formula references.
  name: Named Ranges
- description: Execute multiple read and write operations in a single API call for efficiency.
  name: Batch Operations
finops:
- name: Google Sheets Finops
  service_category: API
  slug: google-sheets-finops
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Deep integration with Google Docs, Slides, Forms, and other Workspace applications.
  name: Google Workspace
- description: Extend Sheets functionality with custom functions, menus, and automation scripts.
  name: Google Apps Script
- description: Connect to BigQuery, Cloud Functions, and other GCP services for advanced data processing.
  name: Google Cloud Platform
- description: Connect Google Sheets to thousands of apps through Zapier automation workflows.
  name: Zapier
- description: Send notifications and updates to Slack channels based on spreadsheet changes.
  name: Slack
json_schemas:
- name: AppendValuesResponse
  property_count: 2
  slug: google-sheets-append-values-response
- name: BandedRange
  property_count: 1
  slug: google-sheets-banded-range
- name: BandingProperties
  property_count: 0
  slug: google-sheets-banding-properties
- name: BasicFilter
  property_count: 3
  slug: google-sheets-basic-filter
- name: BatchClearValuesByDataFilterResponse
  property_count: 2
  slug: google-sheets-batch-clear-values-by-data-filter-response
- name: BatchClearValuesResponse
  property_count: 2
  slug: google-sheets-batch-clear-values-response
- name: BatchGetValuesByDataFilterResponse
  property_count: 2
  slug: google-sheets-batch-get-values-by-data-filter-response
- name: BatchGetValuesResponse
  property_count: 2
  slug: google-sheets-batch-get-values-response
- name: BatchUpdateSpreadsheetRequest
  property_count: 4
  slug: google-sheets-batch-update-spreadsheet-request
- name: BatchUpdateSpreadsheetResponse
  property_count: 2
  slug: google-sheets-batch-update-spreadsheet-response
- name: BatchUpdateValuesByDataFilterResponse
  property_count: 6
  slug: google-sheets-batch-update-values-by-data-filter-response
- name: BatchUpdateValuesRequest
  property_count: 2
  slug: google-sheets-batch-update-values-request
- name: BatchUpdateValuesResponse
  property_count: 6
  slug: google-sheets-batch-update-values-response
- name: BigQueryDataSourceSpec
  property_count: 3
  slug: google-sheets-big-query-data-source-spec
- name: BooleanCondition
  property_count: 2
  slug: google-sheets-boolean-condition
- name: Border
  property_count: 2
  slug: google-sheets-border
- name: Borders
  property_count: 0
  slug: google-sheets-borders
- name: CellData
  property_count: 4
  slug: google-sheets-cell-data
- name: CellFormat
  property_count: 5
  slug: google-sheets-cell-format
- name: ClearValuesResponse
  property_count: 2
  slug: google-sheets-clear-values-response
- name: Color
  property_count: 4
  slug: google-sheets-color
- name: ColorStyle
  property_count: 1
  slug: google-sheets-color-style
- name: ConditionValue
  property_count: 2
  slug: google-sheets-condition-value
- name: ConditionalFormatRule
  property_count: 3
  slug: google-sheets-conditional-format-rule
- name: DataExecutionStatus
  property_count: 4
  slug: google-sheets-data-execution-status
- name: DataFilter
  property_count: 1
  slug: google-sheets-data-filter
- name: DataFilterValueRange
  property_count: 1
  slug: google-sheets-data-filter-value-range
- name: DataSourceColumnReference
  property_count: 1
  slug: google-sheets-data-source-column-reference
- name: DataSourceColumn
  property_count: 1
  slug: google-sheets-data-source-column
- name: DataSourceFormula
  property_count: 1
  slug: google-sheets-data-source-formula
- name: DataSourceParameter
  property_count: 2
  slug: google-sheets-data-source-parameter
- name: DataSourceRefreshSchedule
  property_count: 6
  slug: google-sheets-data-source-refresh-schedule
- name: DataSource
  property_count: 3
  slug: google-sheets-data-source
- name: DataSourceSheetProperties
  property_count: 2
  slug: google-sheets-data-source-sheet-properties
- name: DataSourceSpec
  property_count: 1
  slug: google-sheets-data-source-spec
- name: DataSourceTable
  property_count: 6
  slug: google-sheets-data-source-table
- name: DataValidationRule
  property_count: 3
  slug: google-sheets-data-validation-rule
- name: DateTimeRenderOption
  property_count: 0
  slug: google-sheets-date-time-render-option
- name: DeveloperMetadataLocation
  property_count: 3
  slug: google-sheets-developer-metadata-location
- name: DeveloperMetadataLookup
  property_count: 6
  slug: google-sheets-developer-metadata-lookup
- name: DeveloperMetadata
  property_count: 4
  slug: google-sheets-developer-metadata
- name: DimensionProperties
  property_count: 4
  slug: google-sheets-dimension-properties
- name: DimensionRange
  property_count: 3
  slug: google-sheets-dimension-range
- name: Dimension
  property_count: 0
  slug: google-sheets-dimension
- name: EmbeddedChart
  property_count: 2
  slug: google-sheets-embedded-chart
- name: EmbeddedObjectPosition
  property_count: 3
  slug: google-sheets-embedded-object-position
- name: ErrorResponse
  property_count: 1
  slug: google-sheets-error-response
- name: ErrorValue
  property_count: 2
  slug: google-sheets-error-value
- name: ExtendedValue
  property_count: 4
  slug: google-sheets-extended-value
- name: FilterCriteria
  property_count: 1
  slug: google-sheets-filter-criteria
- name: FilterSpec
  property_count: 1
  slug: google-sheets-filter-spec
- name: FilterView
  property_count: 6
  slug: google-sheets-filter-view
- name: GridCoordinate
  property_count: 3
  slug: google-sheets-grid-coordinate
- name: GridData
  property_count: 5
  slug: google-sheets-grid-data
- name: GridProperties
  property_count: 7
  slug: google-sheets-grid-properties
- name: GridRange
  property_count: 5
  slug: google-sheets-grid-range
- name: InterpolationPoint
  property_count: 2
  slug: google-sheets-interpolation-point
- name: IterativeCalculationSettings
  property_count: 2
  slug: google-sheets-iterative-calculation-settings
- name: Link
  property_count: 1
  slug: google-sheets-link
- name: NamedRange
  property_count: 2
  slug: google-sheets-named-range
- name: NumberFormat
  property_count: 2
  slug: google-sheets-number-format
- name: Padding
  property_count: 4
  slug: google-sheets-padding
- name: PivotFilterCriteria
  property_count: 2
  slug: google-sheets-pivot-filter-criteria
- name: PivotFilterSpec
  property_count: 1
  slug: google-sheets-pivot-filter-spec
- name: PivotGroupLimit
  property_count: 2
  slug: google-sheets-pivot-group-limit
- name: PivotGroupRule
  property_count: 3
  slug: google-sheets-pivot-group-rule
- name: PivotGroup
  property_count: 5
  slug: google-sheets-pivot-group
- name: PivotGroupSortValueBucket
  property_count: 2
  slug: google-sheets-pivot-group-sort-value-bucket
- name: PivotTable
  property_count: 7
  slug: google-sheets-pivot-table
- name: PivotValue
  property_count: 5
  slug: google-sheets-pivot-value
- name: ProtectedRange
  property_count: 7
  slug: google-sheets-protected-range
- name: RowData
  property_count: 1
  slug: google-sheets-row-data
- name: SheetProperties
  property_count: 6
  slug: google-sheets-sheet-properties
- name: Sheet
  property_count: 8
  slug: google-sheets-sheet
- name: Slicer
  property_count: 2
  slug: google-sheets-slicer
- name: SortSpec
  property_count: 2
  slug: google-sheets-sort-spec
- name: SpreadsheetProperties
  property_count: 5
  slug: google-sheets-spreadsheet-properties
- name: Spreadsheet
  property_count: 7
  slug: google-sheets-spreadsheet
- name: SpreadsheetTheme
  property_count: 2
  slug: google-sheets-spreadsheet-theme
- name: TextFormatRun
  property_count: 1
  slug: google-sheets-text-format-run
- name: TextFormat
  property_count: 6
  slug: google-sheets-text-format
- name: TextRotation
  property_count: 2
  slug: google-sheets-text-rotation
- name: UpdateValuesResponse
  property_count: 5
  slug: google-sheets-update-values-response
- name: ValueInputOption
  property_count: 0
  slug: google-sheets-value-input-option
- name: ValueRange
  property_count: 2
  slug: google-sheets-value-range
- name: ValueRenderOption
  property_count: 0
  slug: google-sheets-value-render-option
json_structures:
- name: Google Sheets Append Values Response Structure
  property_count: 2
  slug: google-sheets-append-values-response-structure
- name: Google Sheets Banded Range Structure
  property_count: 1
  slug: google-sheets-banded-range-structure
- name: Google Sheets Banding Properties Structure
  property_count: 0
  slug: google-sheets-banding-properties-structure
- name: Google Sheets Basic Filter Structure
  property_count: 3
  slug: google-sheets-basic-filter-structure
- name: Google Sheets Batch Clear Values By Data Filter Response Structure
  property_count: 2
  slug: google-sheets-batch-clear-values-by-data-filter-response-structure
- name: Google Sheets Batch Clear Values Response Structure
  property_count: 2
  slug: google-sheets-batch-clear-values-response-structure
- name: Google Sheets Batch Get Values By Data Filter Response Structure
  property_count: 2
  slug: google-sheets-batch-get-values-by-data-filter-response-structure
- name: Google Sheets Batch Get Values Response Structure
  property_count: 2
  slug: google-sheets-batch-get-values-response-structure
- name: Google Sheets Batch Update Spreadsheet Request Structure
  property_count: 4
  slug: google-sheets-batch-update-spreadsheet-request-structure
- name: Google Sheets Batch Update Spreadsheet Response Structure
  property_count: 2
  slug: google-sheets-batch-update-spreadsheet-response-structure
- name: Google Sheets Batch Update Values By Data Filter Response Structure
  property_count: 6
  slug: google-sheets-batch-update-values-by-data-filter-response-structure
- name: Google Sheets Batch Update Values Request Structure
  property_count: 2
  slug: google-sheets-batch-update-values-request-structure
- name: Google Sheets Batch Update Values Response Structure
  property_count: 6
  slug: google-sheets-batch-update-values-response-structure
- name: Google Sheets Big Query Data Source Spec Structure
  property_count: 3
  slug: google-sheets-big-query-data-source-spec-structure
- name: Google Sheets Boolean Condition Structure
  property_count: 2
  slug: google-sheets-boolean-condition-structure
- name: Google Sheets Border Structure
  property_count: 2
  slug: google-sheets-border-structure
- name: Google Sheets Borders Structure
  property_count: 0
  slug: google-sheets-borders-structure
- name: Google Sheets Cell Data Structure
  property_count: 4
  slug: google-sheets-cell-data-structure
- name: Google Sheets Cell Format Structure
  property_count: 5
  slug: google-sheets-cell-format-structure
- name: Google Sheets Clear Values Response Structure
  property_count: 2
  slug: google-sheets-clear-values-response-structure
- name: Google Sheets Color Structure
  property_count: 4
  slug: google-sheets-color-structure
- name: Google Sheets Color Style Structure
  property_count: 1
  slug: google-sheets-color-style-structure
- name: Google Sheets Condition Value Structure
  property_count: 2
  slug: google-sheets-condition-value-structure
- name: Google Sheets Conditional Format Rule Structure
  property_count: 3
  slug: google-sheets-conditional-format-rule-structure
- name: Google Sheets Data Execution Status Structure
  property_count: 4
  slug: google-sheets-data-execution-status-structure
- name: Google Sheets Data Filter Structure
  property_count: 1
  slug: google-sheets-data-filter-structure
- name: Google Sheets Data Filter Value Range Structure
  property_count: 1
  slug: google-sheets-data-filter-value-range-structure
- name: Google Sheets Data Source Column Reference Structure
  property_count: 1
  slug: google-sheets-data-source-column-reference-structure
- name: Google Sheets Data Source Column Structure
  property_count: 1
  slug: google-sheets-data-source-column-structure
- name: Google Sheets Data Source Formula Structure
  property_count: 1
  slug: google-sheets-data-source-formula-structure
- name: Google Sheets Data Source Parameter Structure
  property_count: 2
  slug: google-sheets-data-source-parameter-structure
- name: Google Sheets Data Source Refresh Schedule Structure
  property_count: 6
  slug: google-sheets-data-source-refresh-schedule-structure
- name: Google Sheets Data Source Sheet Properties Structure
  property_count: 2
  slug: google-sheets-data-source-sheet-properties-structure
- name: Google Sheets Data Source Spec Structure
  property_count: 1
  slug: google-sheets-data-source-spec-structure
- name: Google Sheets Data Source Structure
  property_count: 3
  slug: google-sheets-data-source-structure
- name: Google Sheets Data Source Table Structure
  property_count: 6
  slug: google-sheets-data-source-table-structure
- name: Google Sheets Data Validation Rule Structure
  property_count: 3
  slug: google-sheets-data-validation-rule-structure
- name: Google Sheets Date Time Render Option Structure
  property_count: 0
  slug: google-sheets-date-time-render-option-structure
- name: Google Sheets Developer Metadata Location Structure
  property_count: 3
  slug: google-sheets-developer-metadata-location-structure
- name: Google Sheets Developer Metadata Lookup Structure
  property_count: 6
  slug: google-sheets-developer-metadata-lookup-structure
- name: Google Sheets Developer Metadata Structure
  property_count: 4
  slug: google-sheets-developer-metadata-structure
- name: Google Sheets Dimension Properties Structure
  property_count: 4
  slug: google-sheets-dimension-properties-structure
- name: Google Sheets Dimension Range Structure
  property_count: 3
  slug: google-sheets-dimension-range-structure
- name: Google Sheets Dimension Structure
  property_count: 0
  slug: google-sheets-dimension-structure
- name: Google Sheets Embedded Chart Structure
  property_count: 2
  slug: google-sheets-embedded-chart-structure
- name: Google Sheets Embedded Object Position Structure
  property_count: 3
  slug: google-sheets-embedded-object-position-structure
- name: Google Sheets Error Response Structure
  property_count: 1
  slug: google-sheets-error-response-structure
- name: Google Sheets Error Value Structure
  property_count: 2
  slug: google-sheets-error-value-structure
- name: Google Sheets Extended Value Structure
  property_count: 4
  slug: google-sheets-extended-value-structure
- name: Google Sheets Filter Criteria Structure
  property_count: 1
  slug: google-sheets-filter-criteria-structure
- name: Google Sheets Filter Spec Structure
  property_count: 1
  slug: google-sheets-filter-spec-structure
- name: Google Sheets Filter View Structure
  property_count: 6
  slug: google-sheets-filter-view-structure
- name: Google Sheets Grid Coordinate Structure
  property_count: 3
  slug: google-sheets-grid-coordinate-structure
- name: Google Sheets Grid Data Structure
  property_count: 5
  slug: google-sheets-grid-data-structure
- name: Google Sheets Grid Properties Structure
  property_count: 7
  slug: google-sheets-grid-properties-structure
- name: Google Sheets Grid Range Structure
  property_count: 5
  slug: google-sheets-grid-range-structure
- name: Google Sheets Interpolation Point Structure
  property_count: 2
  slug: google-sheets-interpolation-point-structure
- name: Google Sheets Iterative Calculation Settings Structure
  property_count: 2
  slug: google-sheets-iterative-calculation-settings-structure
- name: Google Sheets Link Structure
  property_count: 1
  slug: google-sheets-link-structure
- name: Google Sheets Named Range Structure
  property_count: 2
  slug: google-sheets-named-range-structure
- name: Google Sheets Number Format Structure
  property_count: 2
  slug: google-sheets-number-format-structure
- name: Google Sheets Padding Structure
  property_count: 4
  slug: google-sheets-padding-structure
- name: Google Sheets Pivot Filter Criteria Structure
  property_count: 2
  slug: google-sheets-pivot-filter-criteria-structure
- name: Google Sheets Pivot Filter Spec Structure
  property_count: 1
  slug: google-sheets-pivot-filter-spec-structure
- name: Google Sheets Pivot Group Limit Structure
  property_count: 2
  slug: google-sheets-pivot-group-limit-structure
- name: Google Sheets Pivot Group Rule Structure
  property_count: 3
  slug: google-sheets-pivot-group-rule-structure
- name: Google Sheets Pivot Group Sort Value Bucket Structure
  property_count: 2
  slug: google-sheets-pivot-group-sort-value-bucket-structure
- name: Google Sheets Pivot Group Structure
  property_count: 5
  slug: google-sheets-pivot-group-structure
- name: Google Sheets Pivot Table Structure
  property_count: 7
  slug: google-sheets-pivot-table-structure
- name: Google Sheets Pivot Value Structure
  property_count: 5
  slug: google-sheets-pivot-value-structure
- name: Google Sheets Protected Range Structure
  property_count: 7
  slug: google-sheets-protected-range-structure
- name: Google Sheets Row Data Structure
  property_count: 1
  slug: google-sheets-row-data-structure
- name: Google Sheets Sheet Properties Structure
  property_count: 6
  slug: google-sheets-sheet-properties-structure
- name: Google Sheets Sheet Structure
  property_count: 8
  slug: google-sheets-sheet-structure
- name: Google Sheets Slicer Structure
  property_count: 2
  slug: google-sheets-slicer-structure
- name: Google Sheets Sort Spec Structure
  property_count: 2
  slug: google-sheets-sort-spec-structure
- name: Google Sheets Spreadsheet Properties Structure
  property_count: 5
  slug: google-sheets-spreadsheet-properties-structure
- name: Google Sheets Spreadsheet Structure
  property_count: 7
  slug: google-sheets-spreadsheet-structure
- name: Google Sheets Spreadsheet Theme Structure
  property_count: 2
  slug: google-sheets-spreadsheet-theme-structure
- name: Google Sheets Text Format Run Structure
  property_count: 1
  slug: google-sheets-text-format-run-structure
- name: Google Sheets Text Format Structure
  property_count: 6
  slug: google-sheets-text-format-structure
- name: Google Sheets Text Rotation Structure
  property_count: 2
  slug: google-sheets-text-rotation-structure
- name: Google Sheets Update Values Response Structure
  property_count: 5
  slug: google-sheets-update-values-response-structure
- name: Google Sheets Value Input Option Structure
  property_count: 0
  slug: google-sheets-value-input-option-structure
- name: Google Sheets Value Range Structure
  property_count: 2
  slug: google-sheets-value-range-structure
- name: Google Sheets Value Render Option Structure
  property_count: 0
  slug: google-sheets-value-render-option-structure
jsonld:
- class_count: 0
  name: Google Sheets Context
  property_count: 0
  slug: google-sheets-context
layout: provider
mcp_servers:
- description: ''
  name: google-sheets-mcp.yml
  slug: google-sheets-mcpyml
modified: '2026-06-20'
name: Google Sheets
nav: Providers
network: true
overview: 'Google Sheets publishes 4 APIs on the [APIs.io](https://apis.io/) network, including developerMetadata API, Sheets API, Spreadsheets API, and 1 more. Tagged areas include Google Workspace, Productivity, and Spreadsheets.


  The Google Sheets catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Sheets'' developer surface includes authentication, changelog, developer portal, documentation, engineering blog, support, signup flow, and 41 more developer resources.'
plans:
- name: Google Sheets Plans Pricing
  plan_count: 3
  slug: google-sheets-plans-pricing
random_paper: 142
rate_limits:
- limit_count: 5
  name: Google Sheets Rate Limits
  slug: google-sheets-rate-limits
rules:
- name: Google Sheets API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-sheets-jsonschema-spectral-rules
- name: Google Sheets API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 11
  slug: google-sheets-spectral-rules
scopes:
- name: Google Sheets Scopes
  scope_count: 5
  slug: google-sheets-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 62.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 71.6
    developer_ergonomics: 58.7
    discoverability: 61.1
    governance: 69.8
    operational_transparency: 44.7
  previous_composite: 62.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-sheets/refs/heads/main/screenshots/google-sheets-2026-06-20T182233.png
security:
- kind: authentication
  name: Google Sheets Authentication
  slug: google-sheets-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Google Sheets Domain Security
  slug: google-sheets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Sheets Vulnerability Disclosure
  slug: google-sheets-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-sheets
tags:
- Google Workspace
- Productivity
- Spreadsheets
use_cases:
- description: Collect data from various sources and generate automated reports in Google Sheets.
  name: Data Collection and Reporting
- description: Use Google Sheets as a lightweight database for web applications and prototypes.
  name: Database Backend
- description: Automate data entry, processing, and distribution workflows using the API.
  name: Workflow Automation
- description: Synchronize data between Google Sheets and other business applications.
  name: Data Integration
- description: Build interactive dashboards and visualizations from spreadsheet data.
  name: Dashboard Creation
website: https://developers.google.com/workspace/sheets/api
---
