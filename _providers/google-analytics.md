---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 81
  human_in_the_loop: 0
  name: Google Analytics Agentic Access
  operation_count: 129
  slug: google-analytics-agentic-access
  summary_line: 129 operations · 81 acting
api_count: 13
apis:
- description: The accounts API from Google Analytics — 3 operation(s) for accounts.
  name: Google Analytics accounts API
  slug: google-analytics-accounts-api
- description: The accountSummaries API from Google Analytics — 1 operation(s) for accountsummaries.
  name: Google Analytics accountSummaries API
  slug: google-analytics-accountsummaries-api
- description: The data API from Google Analytics — 3 operation(s) for data.
  name: Google Analytics data API
  slug: google-analytics-data-api
- description: The Events API from Google Analytics — 1 operation(s) for events.
  name: Google Analytics Events API
  slug: google-analytics-events-api
- description: The management API from Google Analytics — 36 operation(s) for management.
  name: Google Analytics management API
  slug: google-analytics-management-api
- description: The metadata API from Google Analytics — 1 operation(s) for metadata.
  name: Google Analytics metadata API
  slug: google-analytics-metadata-api
- description: The properties API from Google Analytics — 20 operation(s) for properties.
  name: Google Analytics properties API
  slug: google-analytics-properties-api
- description: The provisioning API from Google Analytics — 2 operation(s) for provisioning.
  name: Google Analytics provisioning API
  slug: google-analytics-provisioning-api
- description: The reports API from Google Analytics — 1 operation(s) for reports.
  name: Google Analytics reports API
  slug: google-analytics-reports-api
- description: The User Deletion API from Google Analytics — 1 operation(s) for user deletion.
  name: Google Analytics User Deletion API
  slug: google-analytics-user-deletion-api
- description: The userActivity API from Google Analytics — 1 operation(s) for useractivity.
  name: Google Analytics userActivity API
  slug: google-analytics-useractivity-api
- description: The userDeletion API from Google Analytics — 1 operation(s) for userdeletion.
  name: Google Analytics userDeletion API
  slug: google-analytics-userdeletion-api
- description: The Validation API from Google Analytics — 1 operation(s) for validation.
  name: Google Analytics Validation API
  slug: google-analytics-validation-api
arazzos:
- description: List accessible accounts, then search the change history of the chosen account.
  name: Google Analytics Account Change History Audit
  slug: google-analytics-account-change-history-audit-workflow
- description: List a property's audience exports and create a new one only when none can be reused.
  name: Google Analytics Reuse or Create an Audience Export
  slug: google-analytics-audience-export-create-or-reuse-workflow
- description: List the custom dimensions and then the custom metrics defined on a GA4 property.
  name: Google Analytics Audit a Property's Custom Definitions
  slug: google-analytics-audit-custom-definitions-workflow
- description: Confirm a property exists, then run several core reports for it in a single batch.
  name: Google Analytics Batch Run Reports
  slug: google-analytics-batch-run-reports-workflow
- description: Validate a report's dimensions and metrics for compatibility before running the report.
  name: Google Analytics Check Compatibility then Run Report
  slug: google-analytics-check-compatibility-run-report-workflow
- description: Create an event-scoped custom dimension on a property, then run a report grouped by it.
  name: Google Analytics Create Custom Dimension then Run Report
  slug: google-analytics-create-custom-dimension-run-report-workflow
- description: Create an event-scoped custom metric on a property, then run a report that reads it.
  name: Google Analytics Create Custom Metric then Run Report
  slug: google-analytics-create-custom-metric-run-report-workflow
- description: Create a GA4 property under an account, then attach a web data stream to it.
  name: Google Analytics Create Property and Web Data Stream
  slug: google-analytics-create-property-data-stream-workflow
- description: Walk account summaries to find a GA4 property, list its properties, then run a core report.
  name: Google Analytics Discover Property and Run Report
  slug: google-analytics-discover-and-run-report-workflow
- description: List the properties under an account, then list the data streams for the chosen property.
  name: Google Analytics Inventory a Property's Data Streams
  slug: google-analytics-inventory-property-data-streams-workflow
- description: List GA4 properties under an account, then run a realtime report for the chosen property.
  name: Google Analytics List Properties and Run Realtime Report
  slug: google-analytics-list-properties-run-realtime-workflow
- description: Confirm an audience export is active, then page through the users it contains.
  name: Google Analytics Query Audience Export Users
  slug: google-analytics-query-audience-export-users-workflow
artifact_total: 451
collections:
- collection_type: postman
  name: Google Analytics Admin accounts API
  slug: postman-google-analytics-accounts-api
- collection_type: postman
  name: Google Analytics Admin accounts accountSummaries API
  slug: postman-google-analytics-accountsummaries-api
- collection_type: postman
  name: Google Analytics Admin API
  slug: postman-google-analytics-admin-api
- collection_type: postman
  name: Google Analytics Admin accounts data API
  slug: postman-google-analytics-data-api
- collection_type: postman
  name: Google Analytics Admin accounts Events API
  slug: postman-google-analytics-events-api
- collection_type: postman
  name: Google Analytics API
  slug: postman-google-analytics-management-api-v3
- collection_type: postman
  name: Google Analytics Admin accounts management API
  slug: postman-google-analytics-management-api
- collection_type: postman
  name: Google Analytics Measurement Protocol (GA4)
  slug: postman-google-analytics-measurement-protocol
- collection_type: postman
  name: Google Analytics Admin accounts metadata API
  slug: postman-google-analytics-metadata-api
- collection_type: postman
  name: Google Analytics Admin accounts properties API
  slug: postman-google-analytics-properties-api
- collection_type: postman
  name: Google Analytics Admin accounts provisioning API
  slug: postman-google-analytics-provisioning-api
- collection_type: postman
  name: Analytics Reporting API
  slug: postman-google-analytics-reporting-api-v4
- collection_type: postman
  name: Google Analytics Admin accounts reports API
  slug: postman-google-analytics-reports-api
- collection_type: postman
  name: Google Analytics Admin accounts User Deletion API
  slug: postman-google-analytics-user-deletion-api
- collection_type: postman
  name: Google Analytics Admin accounts userActivity API
  slug: postman-google-analytics-useractivity-api
- collection_type: postman
  name: Google Analytics Admin accounts userDeletion API
  slug: postman-google-analytics-userdeletion-api
- collection_type: postman
  name: Google Analytics Admin accounts Validation API
  slug: postman-google-analytics-validation-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-analytics-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-analytics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-analytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-analytics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-analytics-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-analytics/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-account-change-history-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-audience-export-create-or-reuse-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-audit-custom-definitions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-batch-run-reports-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-check-compatibility-run-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-create-custom-dimension-run-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-create-custom-metric-run-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-create-property-data-stream-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-discover-and-run-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-inventory-property-data-streams-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-list-properties-run-realtime-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-analytics-query-audience-export-users-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-analytics
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/analytics/get-started
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/analytics
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/apis/library/analytics.googleapis.com
- group: start
  title: ''
  type: Signup
  url: https://analytics.google.com/analytics/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/analytics/devguides/config/admin/v1/client-libraries
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/googleanalytics/google-analytics-mcp
- group: build
  title: GA Dev Tools
  type: Tools
  url: https://ga-dev-tools.google/ga4/
- group: build
  title: E-commerce Migration Helper
  type: Tools
  url: https://github.com/googleanalytics/ecommerce-migration-helper
- group: learn
  title: GA4 Tutorials
  type: Tutorials
  url: https://github.com/googleanalytics/ga4-tutorials
- group: build
  title: Consent Mode Examples
  type: CodeExamples
  url: https://github.com/googleanalytics/gtm-consent-mode-examples
- group: commercial
  title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/analytics/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/analytics/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.google.com/analytics/devguides/collection/protocol/ga4/policy
- group: company
  title: ''
  type: Blog
  url: https://analytics.googleblog.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/analytics/support
- group: operate
  title: ''
  type: FAQ
  url: https://support.google.com/analytics
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.google.com/analytics/answer/9164320
- group: operate
  title: ''
  type: ChangeLog
  url: https://groups.google.com/forum/#!forum/google-analytics-api-notify
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleanalytics/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-analytics
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/googleanalytics
- group: learn
  title: ''
  type: Training
  url: https://goo.gle/ga-courses
- group: learn
  title: ''
  type: Academy
  url: https://marketingplatformacademy.withgoogle.com/google-analytics-360
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/googleanalytics/google-analytics-mcp
created: '2024-01-01'
description: Google Analytics provides data and insights about website and app usage, enabling businesses to understand their audience and optimize their digital properties through customer-centric measurement, machine learning insights, and cross-platform attribution.
examples:
- key_count: 6
  name: Admin Api Account Example
  slug: admin-api-account-example
- key_count: 6
  name: Admin Api Change History Event Example
  slug: admin-api-change-history-event-example
- key_count: 7
  name: Admin Api Conversion Event Example
  slug: admin-api-conversion-event-example
- key_count: 6
  name: Admin Api Custom Dimension Example
  slug: admin-api-custom-dimension-example
- key_count: 7
  name: Admin Api Custom Metric Example
  slug: admin-api-custom-metric-example
- key_count: 8
  name: Admin Api Data Stream Example
  slug: admin-api-data-stream-example
- key_count: 3
  name: Admin Api Firebase Link Example
  slug: admin-api-firebase-link-example
- key_count: 7
  name: Admin Api Google Ads Link Example
  slug: admin-api-google-ads-link-example
- key_count: 3
  name: Admin Api Measurement Protocol Secret Example
  slug: admin-api-measurement-protocol-secret-example
- key_count: 10
  name: Admin Api Property Example
  slug: admin-api-property-example
- key_count: 10
  name: Data Api Audience Export Example
  slug: data-api-audience-export-example
- key_count: 3
  name: Data Api Date Range Example
  slug: data-api-date-range-example
- key_count: 2
  name: Data Api Dimension Example
  slug: data-api-dimension-example
- key_count: 4
  name: Data Api Filter Expression Example
  slug: data-api-filter-expression-example
- key_count: 3
  name: Data Api Metric Example
  slug: data-api-metric-example
- key_count: 4
  name: Data Api Order By Example
  slug: data-api-order-by-example
- key_count: 5
  name: Data Api Pivot Example
  slug: data-api-pivot-example
- key_count: 2
  name: Data Api Row Example
  slug: data-api-row-example
- key_count: 10
  name: Data Api Run Report Request Example
  slug: data-api-run-report-request-example
- key_count: 10
  name: Data Api Run Report Response Example
  slug: data-api-run-report-response-example
- key_count: 2
  name: Measurement Protocol Consent Example
  slug: measurement-protocol-consent-example
- key_count: 9
  name: Measurement Protocol Device Example
  slug: measurement-protocol-device-example
- key_count: 2
  name: Measurement Protocol Event Example
  slug: measurement-protocol-event-example
- key_count: 10
  name: Measurement Protocol Measurement Payload Example
  slug: measurement-protocol-measurement-payload-example
- key_count: 5
  name: Measurement Protocol User Location Example
  slug: measurement-protocol-user-location-example
- key_count: 3
  name: Measurement Protocol Validation Message Example
  slug: measurement-protocol-validation-message-example
- key_count: 1
  name: Measurement Protocol Validation Response Example
  slug: measurement-protocol-validation-response-example
- key_count: 2
  name: User Deletion Api User Deletion Id Example
  slug: user-deletion-api-user-deletion-id-example
- key_count: 6
  name: User Deletion Api User Deletion Request Example
  slug: user-deletion-api-user-deletion-request-example
features:
- description: Machine learning models that predict future actions users may take, like purchasing or churning.
  name: Predictive Capabilities
- description: Automatically detects and surfaces actionable insights from your data.
  name: Proactive Insights
- description: Monitor user activity on your site or app as it happens.
  name: Real-Time Reporting
- description: Machine learning to understand how each touchpoint contributes to conversions.
  name: Data-Driven Attribution
- description: Drag-and-drop analysis with instant visualizations for custom reporting.
  name: Free-Form Exploration
- description: Visualize user steps through conversion funnels and identify optimization opportunities.
  name: Funnel Exploration
- description: Visualize user navigation paths to understand how users reach conversions.
  name: Path Exploration
- description: Analyze behavior of users grouped by common attributes over time.
  name: Cohort Exploration
- description: Export raw event data to BigQuery for advanced analysis and data warehousing.
  name: BigQuery Export
- description: Customer-centric measurement across websites and apps throughout the entire customer lifecycle.
  name: Cross-Platform Measurement
- description: Machine learning models that provide a complete picture of the customer journey while respecting privacy.
  name: Privacy-Safe Modeling
- description: Define custom dimensions and metrics to capture data specific to your business needs.
  name: Custom Dimensions and Metrics
finops:
- name: Google Analytics Finops
  service_category: Web Analytics
  slug: google-analytics-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Google Analytics 4 (GA4) APIs. The schema is derived from the [Google Analytics Data API v1](https://developers.google.com/analytics/devguid
  name: Google Analytics GraphQL Schema
  slug: google-analytics-graphql
image: https://www.google.com/analytics/images/google-analytics-logo.png
integrations:
- description: Link Google Ads accounts to analyze campaign performance and optimize ad spend with Analytics data.
  name: Google Ads
- description: Export raw Analytics data to BigQuery for advanced SQL-based analysis and data warehousing.
  name: Google BigQuery
- description: Connect Search Console to see organic search queries, impressions, and click data alongside Analytics.
  name: Google Search Console
- description: Integrate with Firebase for comprehensive mobile and web app analytics and event tracking.
  name: Firebase
- description: Link DV360 for programmatic advertising measurement and attribution.
  name: Display & Video 360
- description: Connect SA360 for unified search advertising measurement across engines.
  name: Search Ads 360
- description: Use Tag Manager to deploy and manage Analytics tags without modifying website code.
  name: Google Tag Manager
- description: Integrate publisher ad serving data with Analytics for holistic content and ad performance analysis.
  name: Google Ad Manager
- description: Leverage Google Cloud services for advanced data processing, ML models, and storage with Analytics data.
  name: Google Cloud
- description: Connect Salesforce Marketing Cloud for cross-platform marketing measurement and audience activation.
  name: Salesforce Marketing Cloud
json_schemas:
- name: Account
  property_count: 6
  slug: admin-api-account
- name: ChangeHistoryEvent
  property_count: 6
  slug: admin-api-change-history-event
- name: ConversionEvent
  property_count: 7
  slug: admin-api-conversion-event
- name: CustomDimension
  property_count: 6
  slug: admin-api-custom-dimension
- name: CustomMetric
  property_count: 7
  slug: admin-api-custom-metric
- name: DataStream
  property_count: 8
  slug: admin-api-data-stream
- name: FirebaseLink
  property_count: 3
  slug: admin-api-firebase-link
- name: GoogleAdsLink
  property_count: 7
  slug: admin-api-google-ads-link
- name: MeasurementProtocolSecret
  property_count: 3
  slug: admin-api-measurement-protocol-secret
- name: Property
  property_count: 13
  slug: admin-api-property
- name: AudienceExport
  property_count: 10
  slug: data-api-audience-export
- name: DateRange
  property_count: 3
  slug: data-api-date-range
- name: Dimension
  property_count: 2
  slug: data-api-dimension
- name: FilterExpression
  property_count: 4
  slug: data-api-filter-expression
- name: Metric
  property_count: 3
  slug: data-api-metric
- name: OrderBy
  property_count: 4
  slug: data-api-order-by
- name: Pivot
  property_count: 5
  slug: data-api-pivot
- name: Row
  property_count: 2
  slug: data-api-row
- name: RunReportRequest
  property_count: 14
  slug: data-api-run-report-request
- name: RunReportResponse
  property_count: 10
  slug: data-api-run-report-response
- name: Account
  property_count: 9
  slug: google-analytics-account
- name: AccountRef
  property_count: 4
  slug: google-analytics-accountref
- name: Accounts
  property_count: 8
  slug: google-analytics-accounts
- name: AccountSummaries
  property_count: 8
  slug: google-analytics-accountsummaries
- name: AccountSummary
  property_count: 5
  slug: google-analytics-accountsummary
- name: AccountTicket
  property_count: 6
  slug: google-analytics-accountticket
- name: AccountTreeRequest
  property_count: 6
  slug: google-analytics-accounttreerequest
- name: AccountTreeResponse
  property_count: 4
  slug: google-analytics-accounttreeresponse
- name: ActiveMetricRestriction
  property_count: 2
  slug: google-analytics-activemetricrestriction
- name: Activity
  property_count: 15
  slug: google-analytics-activity
- name: AdWordsAccount
  property_count: 3
  slug: google-analytics-adwordsaccount
- name: AnalyticsDataimportDeleteUploadDataRequest
  property_count: 1
  slug: google-analytics-analyticsdataimportdeleteuploaddatarequest
- name: AudienceExport
  property_count: 10
  slug: google-analytics-audienceexport
- name: AudienceListMetadata
  property_count: 0
  slug: google-analytics-audiencelistmetadata
- name: BatchRunPivotReportsRequest
  property_count: 1
  slug: google-analytics-batchrunpivotreportsrequest
- name: BatchRunPivotReportsResponse
  property_count: 2
  slug: google-analytics-batchrunpivotreportsresponse
- name: BatchRunReportsRequest
  property_count: 1
  slug: google-analytics-batchrunreportsrequest
- name: BatchRunReportsResponse
  property_count: 2
  slug: google-analytics-batchrunreportsresponse
- name: BetweenFilter
  property_count: 2
  slug: google-analytics-betweenfilter
- name: CaseExpression
  property_count: 1
  slug: google-analytics-caseexpression
- name: CheckCompatibilityRequest
  property_count: 5
  slug: google-analytics-checkcompatibilityrequest
- name: CheckCompatibilityResponse
  property_count: 2
  slug: google-analytics-checkcompatibilityresponse
- name: Cohort
  property_count: 3
  slug: google-analytics-cohort
- name: CohortGroup
  property_count: 2
  slug: google-analytics-cohortgroup
- name: CohortReportSettings
  property_count: 1
  slug: google-analytics-cohortreportsettings
- name: CohortSpec
  property_count: 3
  slug: google-analytics-cohortspec
- name: CohortsRange
  property_count: 3
  slug: google-analytics-cohortsrange
- name: Column
  property_count: 3
  slug: google-analytics-column
- name: ColumnHeader
  property_count: 2
  slug: google-analytics-columnheader
- name: Columns
  property_count: 5
  slug: google-analytics-columns
- name: ConcatenateExpression
  property_count: 2
  slug: google-analytics-concatenateexpression
- name: Consent
  property_count: 2
  slug: google-analytics-consent
- name: CustomDataSource
  property_count: 16
  slug: google-analytics-customdatasource
- name: CustomDataSources
  property_count: 8
  slug: google-analytics-customdatasources
- name: CustomDimension
  property_count: 12
  slug: google-analytics-customdimension
- name: CustomDimensions
  property_count: 8
  slug: google-analytics-customdimensions
- name: CustomMetric
  property_count: 15
  slug: google-analytics-custommetric
- name: CustomMetrics
  property_count: 8
  slug: google-analytics-custommetrics
- name: DateRange
  property_count: 3
  slug: google-analytics-daterange
- name: DateRangeValues
  property_count: 2
  slug: google-analytics-daterangevalues
- name: Device
  property_count: 9
  slug: google-analytics-device
- name: Dimension
  property_count: 2
  slug: google-analytics-dimension
- name: DimensionCompatibility
  property_count: 2
  slug: google-analytics-dimensioncompatibility
- name: DimensionExpression
  property_count: 3
  slug: google-analytics-dimensionexpression
- name: DimensionFilter
  property_count: 5
  slug: google-analytics-dimensionfilter
- name: DimensionFilterClause
  property_count: 2
  slug: google-analytics-dimensionfilterclause
- name: DimensionHeader
  property_count: 1
  slug: google-analytics-dimensionheader
- name: DimensionMetadata
  property_count: 6
  slug: google-analytics-dimensionmetadata
- name: DimensionOrderBy
  property_count: 2
  slug: google-analytics-dimensionorderby
- name: DimensionValue
  property_count: 1
  slug: google-analytics-dimensionvalue
- name: DynamicSegment
  property_count: 3
  slug: google-analytics-dynamicsegment
- name: EcommerceData
  property_count: 4
  slug: google-analytics-ecommercedata
- name: EntityAdWordsLink
  property_count: 7
  slug: google-analytics-entityadwordslink
- name: EntityAdWordsLinks
  property_count: 7
  slug: google-analytics-entityadwordslinks
- name: EntityUserLink
  property_count: 6
  slug: google-analytics-entityuserlink
- name: EntityUserLinks
  property_count: 7
  slug: google-analytics-entityuserlinks
- name: Event
  property_count: 2
  slug: google-analytics-event
- name: EventData
  property_count: 5
  slug: google-analytics-eventdata
- name: Experiment
  property_count: 28
  slug: google-analytics-experiment
- name: Experiments
  property_count: 8
  slug: google-analytics-experiments
- name: Filter
  property_count: 5
  slug: google-analytics-filter
- name: FilterExpression
  property_count: 4
  slug: google-analytics-filterexpression
- name: FilterExpressionList
  property_count: 1
  slug: google-analytics-filterexpressionlist
- name: FilterRef
  property_count: 5
  slug: google-analytics-filterref
- name: Filters
  property_count: 8
  slug: google-analytics-filters
- name: GaData
  property_count: 17
  slug: google-analytics-gadata
- name: GetReportsRequest
  property_count: 2
  slug: google-analytics-getreportsrequest
- name: GetReportsResponse
  property_count: 3
  slug: google-analytics-getreportsresponse
- name: Goal
  property_count: 18
  slug: google-analytics-goal
- name: GoalData
  property_count: 8
  slug: google-analytics-goaldata
- name: Goals
  property_count: 8
  slug: google-analytics-goals
- name: GoalSetData
  property_count: 1
  slug: google-analytics-goalsetdata
- name: GoogleAnalyticsAdminV1betaAccessBetweenFilter
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaaccessbetweenfilter
- name: GoogleAnalyticsAdminV1betaAccessDateRange
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaaccessdaterange
- name: GoogleAnalyticsAdminV1betaAccessDimension
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaaccessdimension
- name: GoogleAnalyticsAdminV1betaAccessDimensionHeader
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaaccessdimensionheader
- name: GoogleAnalyticsAdminV1betaAccessDimensionValue
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaaccessdimensionvalue
- name: GoogleAnalyticsAdminV1betaAccessFilter
  property_count: 5
  slug: google-analytics-googleanalyticsadminv1betaaccessfilter
- name: GoogleAnalyticsAdminV1betaAccessFilterExpression
  property_count: 4
  slug: google-analytics-googleanalyticsadminv1betaaccessfilterexpression
- name: GoogleAnalyticsAdminV1betaAccessFilterExpressionList
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaaccessfilterexpressionlist
- name: GoogleAnalyticsAdminV1betaAccessInListFilter
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaaccessinlistfilter
- name: GoogleAnalyticsAdminV1betaAccessMetric
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaaccessmetric
- name: GoogleAnalyticsAdminV1betaAccessMetricHeader
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaaccessmetricheader
- name: GoogleAnalyticsAdminV1betaAccessMetricValue
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaaccessmetricvalue
- name: GoogleAnalyticsAdminV1betaAccessNumericFilter
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaaccessnumericfilter
- name: GoogleAnalyticsAdminV1betaAccessOrderBy
  property_count: 3
  slug: google-analytics-googleanalyticsadminv1betaaccessorderby
- name: GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaaccessorderbydimensionorderby
- name: GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaaccessorderbymetricorderby
- name: GoogleAnalyticsAdminV1betaAccessQuota
  property_count: 5
  slug: google-analytics-googleanalyticsadminv1betaaccessquota
- name: GoogleAnalyticsAdminV1betaAccessQuotaStatus
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaaccessquotastatus
- name: GoogleAnalyticsAdminV1betaAccessRow
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaaccessrow
- name: GoogleAnalyticsAdminV1betaAccessStringFilter
  property_count: 3
  slug: google-analytics-googleanalyticsadminv1betaaccessstringfilter
- name: GoogleAnalyticsAdminV1betaAccount
  property_count: 6
  slug: google-analytics-googleanalyticsadminv1betaaccount
- name: GoogleAnalyticsAdminV1betaAccountSummary
  property_count: 4
  slug: google-analytics-googleanalyticsadminv1betaaccountsummary
- name: GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaacknowledgeuserdatacollectionreque
- name: GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse
  property_count: 0
  slug: google-analytics-googleanalyticsadminv1betaacknowledgeuserdatacollectionrespo
- name: GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest
  property_count: 0
  slug: google-analytics-googleanalyticsadminv1betaarchivecustomdimensionrequest
- name: GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest
  property_count: 0
  slug: google-analytics-googleanalyticsadminv1betaarchivecustommetricrequest
- name: GoogleAnalyticsAdminV1betaChangeHistoryChange
  property_count: 4
  slug: google-analytics-googleanalyticsadminv1betachangehistorychange
- name: GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource
  property_count: 8
  slug: google-analytics-googleanalyticsadminv1betachangehistorychangechangehistoryre
- name: GoogleAnalyticsAdminV1betaChangeHistoryEvent
  property_count: 6
  slug: google-analytics-googleanalyticsadminv1betachangehistoryevent
- name: GoogleAnalyticsAdminV1betaConversionEvent
  property_count: 7
  slug: google-analytics-googleanalyticsadminv1betaconversionevent
- name: GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaconversioneventdefaultconversionva
- name: GoogleAnalyticsAdminV1betaCustomDimension
  property_count: 6
  slug: google-analytics-googleanalyticsadminv1betacustomdimension
- name: GoogleAnalyticsAdminV1betaCustomMetric
  property_count: 7
  slug: google-analytics-googleanalyticsadminv1betacustommetric
- name: GoogleAnalyticsAdminV1betaDataRetentionSettings
  property_count: 3
  slug: google-analytics-googleanalyticsadminv1betadataretentionsettings
- name: GoogleAnalyticsAdminV1betaDataSharingSettings
  property_count: 6
  slug: google-analytics-googleanalyticsadminv1betadatasharingsettings
- name: GoogleAnalyticsAdminV1betaDataStream
  property_count: 8
  slug: google-analytics-googleanalyticsadminv1betadatastream
- name: GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betadatastreamandroidappstreamdata
- name: GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betadatastreamiosappstreamdata
- name: GoogleAnalyticsAdminV1betaDataStreamWebStreamData
  property_count: 3
  slug: google-analytics-googleanalyticsadminv1betadatastreamwebstreamdata
- name: GoogleAnalyticsAdminV1betaFirebaseLink
  property_count: 3
  slug: google-analytics-googleanalyticsadminv1betafirebaselink
- name: GoogleAnalyticsAdminV1betaGoogleAdsLink
  property_count: 7
  slug: google-analytics-googleanalyticsadminv1betagoogleadslink
- name: GoogleAnalyticsAdminV1betaListAccountsResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistaccountsresponse
- name: GoogleAnalyticsAdminV1betaListAccountSummariesResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistaccountsummariesresponse
- name: GoogleAnalyticsAdminV1betaListConversionEventsResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistconversioneventsresponse
- name: GoogleAnalyticsAdminV1betaListCustomDimensionsResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistcustomdimensionsresponse
- name: GoogleAnalyticsAdminV1betaListCustomMetricsResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistcustommetricsresponse
- name: GoogleAnalyticsAdminV1betaListDataStreamsResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistdatastreamsresponse
- name: GoogleAnalyticsAdminV1betaListFirebaseLinksResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistfirebaselinksresponse
- name: GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistgoogleadslinksresponse
- name: GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistmeasurementprotocolsecretsresp
- name: GoogleAnalyticsAdminV1betaListPropertiesResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betalistpropertiesresponse
- name: GoogleAnalyticsAdminV1betaMeasurementProtocolSecret
  property_count: 3
  slug: google-analytics-googleanalyticsadminv1betameasurementprotocolsecret
- name: GoogleAnalyticsAdminV1betaNumericValue
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betanumericvalue
- name: GoogleAnalyticsAdminV1betaProperty
  property_count: 13
  slug: google-analytics-googleanalyticsadminv1betaproperty
- name: GoogleAnalyticsAdminV1betaPropertySummary
  property_count: 4
  slug: google-analytics-googleanalyticsadminv1betapropertysummary
- name: GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betaprovisionaccountticketrequest
- name: GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse
  property_count: 1
  slug: google-analytics-googleanalyticsadminv1betaprovisionaccountticketresponse
- name: GoogleAnalyticsAdminV1betaRunAccessReportRequest
  property_count: 12
  slug: google-analytics-googleanalyticsadminv1betarunaccessreportrequest
- name: GoogleAnalyticsAdminV1betaRunAccessReportResponse
  property_count: 5
  slug: google-analytics-googleanalyticsadminv1betarunaccessreportresponse
- name: GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest
  property_count: 8
  slug: google-analytics-googleanalyticsadminv1betasearchchangehistoryeventsrequest
- name: GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse
  property_count: 2
  slug: google-analytics-googleanalyticsadminv1betasearchchangehistoryeventsresponse
- name: GoogleProtobufEmpty
  property_count: 0
  slug: google-analytics-googleprotobufempty
- name: HashClientIdRequest
  property_count: 3
  slug: google-analytics-hashclientidrequest
- name: HashClientIdResponse
  property_count: 4
  slug: google-analytics-hashclientidresponse
- name: IncludeConditions
  property_count: 5
  slug: google-analytics-includeconditions
- name: InListFilter
  property_count: 2
  slug: google-analytics-inlistfilter
- name: LinkedForeignAccount
  property_count: 10
  slug: google-analytics-linkedforeignaccount
- name: ListAudienceExportsResponse
  property_count: 2
  slug: google-analytics-listaudienceexportsresponse
- name: McfData
  property_count: 15
  slug: google-analytics-mcfdata
- name: MeasurementPayload
  property_count: 13
  slug: google-analytics-measurementpayload
- name: Metadata
  property_count: 3
  slug: google-analytics-metadata
- name: Metric
  property_count: 3
  slug: google-analytics-metric
- name: MetricCompatibility
  property_count: 2
  slug: google-analytics-metriccompatibility
- name: MetricFilter
  property_count: 4
  slug: google-analytics-metricfilter
- name: MetricFilterClause
  property_count: 2
  slug: google-analytics-metricfilterclause
- name: MetricHeader
  property_count: 2
  slug: google-analytics-metricheader
- name: MetricHeaderEntry
  property_count: 2
  slug: google-analytics-metricheaderentry
- name: MetricMetadata
  property_count: 9
  slug: google-analytics-metricmetadata
- name: MetricOrderBy
  property_count: 1
  slug: google-analytics-metricorderby
- name: MetricValue
  property_count: 1
  slug: google-analytics-metricvalue
- name: MinuteRange
  property_count: 3
  slug: google-analytics-minuterange
- name: NumericFilter
  property_count: 2
  slug: google-analytics-numericfilter
- name: NumericValue
  property_count: 2
  slug: google-analytics-numericvalue
- name: Operation
  property_count: 5
  slug: google-analytics-operation
- name: OrderBy
  property_count: 4
  slug: google-analytics-orderby
- name: OrFiltersForSegment
  property_count: 1
  slug: google-analytics-orfiltersforsegment
- name: PageviewData
  property_count: 2
  slug: google-analytics-pageviewdata
- name: Pivot
  property_count: 5
  slug: google-analytics-pivot
- name: PivotDimensionHeader
  property_count: 1
  slug: google-analytics-pivotdimensionheader
- name: PivotHeader
  property_count: 2
  slug: google-analytics-pivotheader
- name: PivotHeaderEntry
  property_count: 3
  slug: google-analytics-pivotheaderentry
- name: PivotOrderBy
  property_count: 2
  slug: google-analytics-pivotorderby
- name: PivotSelection
  property_count: 2
  slug: google-analytics-pivotselection
- name: PivotValueRegion
  property_count: 1
  slug: google-analytics-pivotvalueregion
- name: ProductData
  property_count: 4
  slug: google-analytics-productdata
- name: Profile
  property_count: 26
  slug: google-analytics-profile
- name: ProfileFilterLink
  property_count: 6
  slug: google-analytics-profilefilterlink
- name: ProfileFilterLinks
  property_count: 8
  slug: google-analytics-profilefilterlinks
- name: ProfileRef
  property_count: 7
  slug: google-analytics-profileref
- name: Profiles
  property_count: 8
  slug: google-analytics-profiles
- name: ProfileSummary
  property_count: 5
  slug: google-analytics-profilesummary
- name: PropertyQuota
  property_count: 6
  slug: google-analytics-propertyquota
- name: QueryAudienceExportRequest
  property_count: 2
  slug: google-analytics-queryaudienceexportrequest
- name: QueryAudienceExportResponse
  property_count: 3
  slug: google-analytics-queryaudienceexportresponse
- name: QuotaStatus
  property_count: 2
  slug: google-analytics-quotastatus
- name: RealtimeData
  property_count: 9
  slug: google-analytics-realtimedata
- name: RemarketingAudience
  property_count: 14
  slug: google-analytics-remarketingaudience
- name: RemarketingAudiences
  property_count: 8
  slug: google-analytics-remarketingaudiences
- name: Report
  property_count: 3
  slug: google-analytics-report
- name: ReportData
  property_count: 10
  slug: google-analytics-reportdata
- name: ReportRequest
  property_count: 17
  slug: google-analytics-reportrequest
- name: ReportRow
  property_count: 2
  slug: google-analytics-reportrow
- name: ResourceQuotasRemaining
  property_count: 2
  slug: google-analytics-resourcequotasremaining
- name: ResponseMetaData
  property_count: 7
  slug: google-analytics-responsemetadata
- name: Row
  property_count: 2
  slug: google-analytics-row
- name: RunPivotReportRequest
  property_count: 11
  slug: google-analytics-runpivotreportrequest
- name: RunPivotReportResponse
  property_count: 8
  slug: google-analytics-runpivotreportresponse
- name: RunRealtimeReportRequest
  property_count: 9
  slug: google-analytics-runrealtimereportrequest
- name: RunRealtimeReportResponse
  property_count: 9
  slug: google-analytics-runrealtimereportresponse
- name: RunReportRequest
  property_count: 14
  slug: google-analytics-runreportrequest
- name: RunReportResponse
  property_count: 10
  slug: google-analytics-runreportresponse
- name: SamplingMetadata
  property_count: 2
  slug: google-analytics-samplingmetadata
- name: SchemaRestrictionResponse
  property_count: 1
  slug: google-analytics-schemarestrictionresponse
- name: ScreenviewData
  property_count: 4
  slug: google-analytics-screenviewdata
- name: SearchUserActivityRequest
  property_count: 6
  slug: google-analytics-searchuseractivityrequest
- name: SearchUserActivityResponse
  property_count: 4
  slug: google-analytics-searchuseractivityresponse
- name: Segment
  property_count: 9
  slug: google-analytics-segment
- name: SegmentDefinition
  property_count: 1
  slug: google-analytics-segmentdefinition
- name: SegmentDimensionFilter
  property_count: 6
  slug: google-analytics-segmentdimensionfilter
- name: SegmentFilter
  property_count: 3
  slug: google-analytics-segmentfilter
- name: SegmentFilterClause
  property_count: 3
  slug: google-analytics-segmentfilterclause
- name: SegmentMetricFilter
  property_count: 5
  slug: google-analytics-segmentmetricfilter
- name: Segments
  property_count: 8
  slug: google-analytics-segments
- name: SegmentSequenceStep
  property_count: 2
  slug: google-analytics-segmentsequencestep
- name: SequenceSegment
  property_count: 2
  slug: google-analytics-sequencesegment
- name: SimpleSegment
  property_count: 1
  slug: google-analytics-simplesegment
- name: Status
  property_count: 3
  slug: google-analytics-status
- name: StringFilter
  property_count: 3
  slug: google-analytics-stringfilter
- name: TransactionData
  property_count: 4
  slug: google-analytics-transactiondata
- name: UnsampledReport
  property_count: 19
  slug: google-analytics-unsampledreport
- name: UnsampledReports
  property_count: 8
  slug: google-analytics-unsampledreports
- name: Upload
  property_count: 7
  slug: google-analytics-upload
- name: Uploads
  property_count: 7
  slug: google-analytics-uploads
- name: User
  property_count: 2
  slug: google-analytics-user
- name: UserActivitySession
  property_count: 6
  slug: google-analytics-useractivitysession
- name: UserDeletionId
  property_count: 2
  slug: google-analytics-userdeletionid
- name: UserDeletionRequest
  property_count: 6
  slug: google-analytics-userdeletionrequest
- name: UserLocation
  property_count: 5
  slug: google-analytics-userlocation
- name: UserPropertyValue
  property_count: 1
  slug: google-analytics-userpropertyvalue
- name: UserRef
  property_count: 3
  slug: google-analytics-userref
- name: V1betaAudienceDimension
  property_count: 1
  slug: google-analytics-v1betaaudiencedimension
- name: V1betaAudienceDimensionValue
  property_count: 1
  slug: google-analytics-v1betaaudiencedimensionvalue
- name: V1betaAudienceRow
  property_count: 1
  slug: google-analytics-v1betaaudiencerow
- name: ValidationMessage
  property_count: 3
  slug: google-analytics-validationmessage
- name: ValidationResponse
  property_count: 1
  slug: google-analytics-validationresponse
- name: Webproperties
  property_count: 8
  slug: google-analytics-webproperties
- name: Webproperty
  property_count: 19
  slug: google-analytics-webproperty
- name: WebPropertyRef
  property_count: 6
  slug: google-analytics-webpropertyref
- name: WebPropertySummary
  property_count: 8
  slug: google-analytics-webpropertysummary
- name: Consent
  property_count: 2
  slug: measurement-protocol-consent
- name: Device
  property_count: 9
  slug: measurement-protocol-device
- name: Event
  property_count: 2
  slug: measurement-protocol-event
- name: MeasurementPayload
  property_count: 13
  slug: measurement-protocol-measurement-payload
- name: UserLocation
  property_count: 5
  slug: measurement-protocol-user-location
- name: ValidationMessage
  property_count: 3
  slug: measurement-protocol-validation-message
- name: ValidationResponse
  property_count: 1
  slug: measurement-protocol-validation-response
- name: UserDeletionId
  property_count: 2
  slug: user-deletion-api-user-deletion-id
- name: UserDeletionRequest
  property_count: 6
  slug: user-deletion-api-user-deletion-request
json_structures:
- name: Admin Api Account Structure
  property_count: 6
  slug: admin-api-account-structure
- name: Admin Api Change History Event Structure
  property_count: 6
  slug: admin-api-change-history-event-structure
- name: Admin Api Conversion Event Structure
  property_count: 7
  slug: admin-api-conversion-event-structure
- name: Admin Api Custom Dimension Structure
  property_count: 6
  slug: admin-api-custom-dimension-structure
- name: Admin Api Custom Metric Structure
  property_count: 7
  slug: admin-api-custom-metric-structure
- name: Admin Api Data Stream Structure
  property_count: 8
  slug: admin-api-data-stream-structure
- name: Admin Api Firebase Link Structure
  property_count: 3
  slug: admin-api-firebase-link-structure
- name: Admin Api Google Ads Link Structure
  property_count: 7
  slug: admin-api-google-ads-link-structure
- name: Admin Api Measurement Protocol Secret Structure
  property_count: 3
  slug: admin-api-measurement-protocol-secret-structure
- name: Admin Api Property Structure
  property_count: 13
  slug: admin-api-property-structure
- name: Data Api Audience Export Structure
  property_count: 10
  slug: data-api-audience-export-structure
- name: Data Api Date Range Structure
  property_count: 3
  slug: data-api-date-range-structure
- name: Data Api Dimension Structure
  property_count: 2
  slug: data-api-dimension-structure
- name: Data Api Filter Expression Structure
  property_count: 4
  slug: data-api-filter-expression-structure
- name: Data Api Metric Structure
  property_count: 3
  slug: data-api-metric-structure
- name: Data Api Order By Structure
  property_count: 4
  slug: data-api-order-by-structure
- name: Data Api Pivot Structure
  property_count: 5
  slug: data-api-pivot-structure
- name: Data Api Row Structure
  property_count: 2
  slug: data-api-row-structure
- name: Data Api Run Report Request Structure
  property_count: 14
  slug: data-api-run-report-request-structure
- name: Data Api Run Report Response Structure
  property_count: 10
  slug: data-api-run-report-response-structure
- name: Google Analytics Structure
  property_count: 0
  slug: google-analytics-structure
- name: Measurement Protocol Consent Structure
  property_count: 2
  slug: measurement-protocol-consent-structure
- name: Measurement Protocol Device Structure
  property_count: 9
  slug: measurement-protocol-device-structure
- name: Measurement Protocol Event Structure
  property_count: 2
  slug: measurement-protocol-event-structure
- name: Measurement Protocol Measurement Payload Structure
  property_count: 13
  slug: measurement-protocol-measurement-payload-structure
- name: Measurement Protocol User Location Structure
  property_count: 5
  slug: measurement-protocol-user-location-structure
- name: Measurement Protocol Validation Message Structure
  property_count: 3
  slug: measurement-protocol-validation-message-structure
- name: Measurement Protocol Validation Response Structure
  property_count: 1
  slug: measurement-protocol-validation-response-structure
- name: User Deletion Api User Deletion Id Structure
  property_count: 2
  slug: user-deletion-api-user-deletion-id-structure
- name: User Deletion Api User Deletion Request Structure
  property_count: 6
  slug: user-deletion-api-user-deletion-request-structure
jsonld:
- class_count: 10
  name: Google Analytics Admin Api Context
  property_count: 48
  slug: google-analytics-admin-api-context
- class_count: 10
  name: Google Analytics Data Api Context
  property_count: 92
  slug: google-analytics-data-api-context
- class_count: 7
  name: Google Analytics Measurement Protocol Context
  property_count: 37
  slug: google-analytics-measurement-protocol-context
- class_count: 2
  name: Google Analytics User Deletion Api Context
  property_count: 8
  slug: google-analytics-user-deletion-api-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Google Analytics
nav: Providers
network: true
overview: 'Google Analytics publishes 13 APIs on the [APIs.io](https://apis.io/) network, including accounts API, accountSummaries API, data API, and 10 more. Tagged areas include Analytics, Data, Google, Metrics, and Reporting.


  The Google Analytics catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Google Analytics'' developer surface includes authentication, getting-started guide, developer portal, developer console, signup flow, tooling, code examples, and 38 more developer resources.'
plans:
- name: Google Analytics Plans Pricing
  plan_count: 2
  slug: google-analytics-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 10
  name: Google Analytics Rate Limits
  slug: google-analytics-rate-limits
rules:
- name: Google Analytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-analytics-jsonschema-spectral-rules
- name: Google Analytics API Rules
  rule_count: 67
  severity_counts:
    error: 18
    hint: 0
    info: 26
    warn: 23
  slug: google-analytics-spectral-rules
scopes:
- name: Google Analytics Scopes
  scope_count: 7
  slug: google-analytics-scopes
  summary_line: 7 scopes · implicit/authorizationCode
score:
  band: strong
  composite: 64.6
  delta: -2.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.5
    developer_ergonomics: 63.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/screenshots/google-analytics-2026-07-25T220105.png
security:
- kind: authentication
  name: Google Analytics Authentication
  slug: google-analytics-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Google Analytics Domain Security
  slug: google-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Analytics Vulnerability Disclosure
  slug: google-analytics-vulnerability-disclosure
  summary_line: security.txt · contact published
skills:
- name: Run Report
  url: skills/run-report/SKILL.md
- name: Run Realtime Report
  url: skills/run-realtime-report/SKILL.md
- name: Run Pivot Report
  url: skills/run-pivot-report/SKILL.md
- name: Batch Run Reports
  url: skills/batch-run-reports/SKILL.md
- name: Batch Run Pivot Reports
  url: skills/batch-run-pivot-reports/SKILL.md
- name: Check Compatibility
  url: skills/check-compatibility/SKILL.md
- name: Create Audience Export
  url: skills/create-audience-export/SKILL.md
- name: Get Audience Export
  url: skills/get-audience-export/SKILL.md
- name: List Audience Exports
  url: skills/list-audience-exports/SKILL.md
- name: Query Audience Export
  url: skills/query-audience-export/SKILL.md
- name: List Account Summaries
  url: skills/list-account-summaries/SKILL.md
- name: List Accounts
  url: skills/list-accounts/SKILL.md
- name: Provision Account Ticket
  url: skills/provision-account-ticket/SKILL.md
- name: List Properties
  url: skills/list-properties/SKILL.md
- name: Create Property
  url: skills/create-property/SKILL.md
- name: Search Change History Events
  url: skills/search-change-history-events/SKILL.md
- name: Run Access Report
  url: skills/run-access-report/SKILL.md
- name: Delete Google Ads Link
  url: skills/delete-google-ads-link/SKILL.md
- name: Get Measurement Protocol Secret
  url: skills/get-measurement-protocol-secret/SKILL.md
- name: Update Google Ads Link
  url: skills/update-google-ads-link/SKILL.md
- name: Archive Custom Metric
  url: skills/archive-custom-metric/SKILL.md
- name: List Conversion Events
  url: skills/list-conversion-events/SKILL.md
- name: Create Conversion Event
  url: skills/create-conversion-event/SKILL.md
- name: List Custom Dimensions
  url: skills/list-custom-dimensions/SKILL.md
- name: Create Custom Dimension
  url: skills/create-custom-dimension/SKILL.md
- name: List Custom Metrics
  url: skills/list-custom-metrics/SKILL.md
- name: Create Custom Metric
  url: skills/create-custom-metric/SKILL.md
- name: List Data Streams
  url: skills/list-data-streams/SKILL.md
- name: Create Data Stream
  url: skills/create-data-stream/SKILL.md
- name: List Firebase Links
  url: skills/list-firebase-links/SKILL.md
- name: Create Firebase Link
  url: skills/create-firebase-link/SKILL.md
- name: List Google Ads Links
  url: skills/list-google-ads-links/SKILL.md
- name: Create Google Ads Link
  url: skills/create-google-ads-link/SKILL.md
- name: List Measurement Protocol Secrets
  url: skills/list-measurement-protocol-secrets/SKILL.md
- name: Create Measurement Protocol Secret
  url: skills/create-measurement-protocol-secret/SKILL.md
- name: Acknowledge User Data Collection
  url: skills/acknowledge-user-data-collection/SKILL.md
- name: Send Events
  url: skills/send-events/SKILL.md
- name: Validate Events
  url: skills/validate-events/SKILL.md
- name: Upsert User Deletion Request
  url: skills/upsert-user-deletion-request/SKILL.md
slug: google-analytics
solutions:
- description: Full-featured web and app analytics solution available at no charge for businesses of all sizes.
  name: Google Analytics Free
- description: Enterprise-grade analytics with advanced features including intraday data, sub-properties, roll-up reporting, and higher limits.
  name: Analytics 360
- description: Integrated advertising and analytics platform combining Analytics 360 with advertising products for enterprise marketing.
  name: Google Marketing Platform
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
- Machine Learning
- Attribution
use_cases:
- description: Understand where visitors come from, what pages they view, and how they interact with your website.
  name: Website Traffic Analysis
- description: Track conversion events, analyze funnels, and identify drop-off points to improve conversion rates.
  name: Conversion Optimization
- description: Segment users by demographics, behavior, technology, and custom attributes for targeted analysis.
  name: Audience Segmentation
- description: Measure the effectiveness of advertising campaigns across channels with attribution modeling.
  name: Marketing Campaign Measurement
- description: Track purchase activity, revenue, product performance, and shopping behavior.
  name: E-commerce Analytics
- description: Measure user engagement, retention, and in-app actions for mobile and web applications.
  name: App Analytics
- description: Send events from your server using the Measurement Protocol for offline and backend interactions.
  name: Server-Side Event Tracking
- description: Manage user data deletion requests and privacy compliance using the User Deletion API.
  name: Compliance and Data Privacy
- description: Build custom reports and dashboards programmatically using the Data API.
  name: Custom Reporting and Dashboards
- description: Monitor live user activity for time-sensitive campaigns, launches, and events.
  name: Real-Time Monitoring
website: https://developers.google.com/analytics
---
