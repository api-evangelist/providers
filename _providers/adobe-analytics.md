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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.0
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 53
  human_in_the_loop: 1
  name: Adobe Analytics Agentic Access
  operation_count: 103
  slug: adobe-analytics-agentic-access
  summary_line: 103 operations · 53 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: The Livestream API is a reporting feature in Adobe Analytics that allows clients to receive traffic data processed by Adobe Analytics in real time. Hits are streamed to the client on a hit-by-hit basi
  name: Adobe Analytics Livestream API
  slug: adobe-analytics-livestream-api
- description: The Data Insertion API allows server-side data submission to Adobe Analytics one event at a time using HTTP GET or POST requests. Unlike the Bulk Data Insertion API which processes compressed CSV file
  name: Adobe Analytics Data Insertion API
  slug: adobe-analytics-data-insertion-api
- description: The Adobe Analytics 1.4 APIs provide programmatic access to reporting, classifications, data sources, and report suite configuration. This version is deprecated and scheduled for end-of-life on August
  name: Adobe Analytics 1.4 API
  slug: adobe-analytics-14-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}
  baseurl_source: spec_template
  description: Manage analytics annotations
  name: Adobe Analytics Annotations API
  phrasing_intents:
  - id: listAnnotations
    intent: List report annotations
    question: What annotations have been added to dates in my Adobe Analytics reports?
  - id: createAnnotation
    intent: Annotate a date range in reports
    question: How do I mark a campaign launch date on my analytics reports with a note?
  - id: listTags
    intent: List component tags
    question: Which tags are being used on segments, calculated metrics and projects in my company?
  phrasing_ops: 3
  slug: adobe-analytics-annotations-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}
  baseurl_source: spec_template
  description: Manage calculated metrics built from existing metrics
  name: Adobe Analytics Calculated Metrics API
  phrasing_intents:
  - id: listCalculatedMetrics
    intent: List calculated metrics
    question: What calculated metrics exist in my Adobe Analytics company?
  - id: createCalculatedMetric
    intent: Create a calculated metric
    question: How do I build a new calculated metric that combines existing metrics with a formula?
  - id: getCalculatedMetric
    intent: Get a calculated metric
    question: How do I see the formula behind one calculated metric?
  - id: updateCalculatedMetric
    intent: Update a calculated metric
    question: Can I change the formula of an existing calculated metric?
  - id: deleteCalculatedMetric
    intent: Delete a calculated metric
    question: How do I permanently remove a calculated metric?
  phrasing_ops: 5
  slug: adobe-analytics-calculated-metrics-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}
  baseurl_source: spec_template
  description: Manage saved date ranges
  name: Adobe Analytics Date Ranges API
  phrasing_intents:
  - id: listDateRanges
    intent: List saved date ranges
    question: What saved date ranges can I use in Adobe Analytics?
  phrasing_ops: 1
  slug: adobe-analytics-date-ranges-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}
  baseurl_source: spec_template
  description: Retrieve available dimensions for a report suite
  name: Adobe Analytics Dimensions API
  phrasing_intents:
  - id: listDimensions
    intent: List dimensions in a report suite
    question: Which dimensions like page or browser can I report on in a report suite?
  phrasing_ops: 1
  slug: adobe-analytics-dimensions-api
- baseURL: https://analytics-collection.adobe.io/aa/collect/v1
  baseurl_source: spec
  description: Upload and validate batched event data files
  name: Adobe Analytics Events API
  phrasing_intents:
  - id: uploadEvents
    intent: Upload a batch file of Analytics hits
    question: How do I send a gzip CSV of Analytics hits for ingestion in bulk?
  - id: validateEvents
    intent: Validate a batch events file without ingesting
    question: Can I check whether my batch events CSV is formatted correctly before uploading it?
  phrasing_ops: 2
  slug: adobe-analytics-events-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}/datarepair/v1
  baseurl_source: spec_template
  description: Create and monitor data repair jobs
  name: Adobe Analytics Jobs API
  phrasing_intents:
  - id: listJobs
    intent: List recent data repair jobs
    question: What data repair jobs have run on my report suite recently?
  - id: createRepairJob
    intent: Start a data repair job
    question: How do I start a data repair to fix or delete variables in historical data?
  - id: getRepairJob
    intent: Get a data repair job's progress
    question: How far along is my data repair job?
  phrasing_ops: 3
  slug: adobe-analytics-jobs-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}
  baseurl_source: spec_template
  description: Retrieve available metrics for a report suite
  name: Adobe Analytics Metrics API
  phrasing_intents:
  - id: listMetrics
    intent: List metrics in a report suite
    question: Which metrics, including calculated ones, are available in a report suite?
  phrasing_ops: 1
  slug: adobe-analytics-metrics-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}
  baseurl_source: spec_template
  description: Retrieve report suite information and configuration
  name: Adobe Analytics Report Suites API
  phrasing_intents:
  - id: listReportSuites
    intent: List accessible report suites
    question: Which report suites can I access in Adobe Analytics?
  - id: getReportSuite
    intent: Get a report suite
    question: What are the name, timezone and type of one report suite?
  - id: getTimezones_1
    intent: List supported report suite timezones
    question: Which timezones can I choose when creating a report suite?
  - id: userCreateReportSuite
    intent: Create a report suite
    question: How do I create a new standard report suite?
  phrasing_ops: 4
  slug: adobe-analytics-report-suites-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}
  baseurl_source: spec_template
  description: Run analytics reports and retrieve data
  name: Adobe Analytics Reports API
  phrasing_intents:
  - id: runReport
    intent: Run an Analytics report
    question: How do I pull page views by page for last month from a report suite?
  phrasing_ops: 1
  slug: adobe-analytics-reports-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}
  baseurl_source: spec_template
  description: Create, retrieve, update, and delete analytics segments
  name: Adobe Analytics Segments API
  phrasing_intents:
  - id: listSegments
    intent: List segments
    question: What segments exist in my Adobe Analytics company?
  - id: createSegment
    intent: Create a segment
    question: How do I create a segment of visitors who match certain criteria?
  - id: getSegment
    intent: Get a segment
    question: How do I see the definition of one segment?
  - id: updateSegment
    intent: Update a segment
    question: Can I change only the name of an existing segment?
  - id: deleteSegment
    intent: Delete a segment
    question: How do I permanently remove a segment?
  phrasing_ops: 5
  slug: adobe-analytics-segments-api
- baseURL_template: https://analytics.adobe.io/api/{globalCompanyId}/datarepair/v1
  baseurl_source: spec_template
  description: Estimate the scope and cost of a repair job
  name: Adobe Analytics Server Call Estimate API
  phrasing_intents:
  - id: getServerCallEstimate
    intent: Estimate server calls for a data repair
    question: How many rows would a data repair scan for a report suite and date range?
  phrasing_ops: 1
  slug: adobe-analytics-server-call-estimate-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: Manage Data Sources accounts associated with a report suite
  name: Adobe Analytics Account API
  phrasing_intents:
  - id: getAllAccounts
    intent: List Data Sources accounts for a report suite
    question: Which Data Sources accounts are set up on my Adobe Analytics report suite?
  - id: createAccount
    intent: Create a Data Sources account
    question: How do I set up a new Data Sources account to import offline data into a report suite?
  - id: getAccount
    intent: Get one Data Sources account
    question: What are the details of a specific Data Sources account on my report suite?
  - id: deleteAccount
    intent: Delete a Data Sources account
    question: Can I remove a Data Sources account from a report suite, and is that reversible?
  phrasing_ops: 4
  slug: adobe-analytics-account-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The analytics Cloud Locations account API for user token
  name: Adobe Analytics Cloud Locations Account API
  phrasing_intents:
  - id: getS3UserArn
    intent: Get the S3 user ARN for role-based S3 accounts
    question: Which AWS user ARN do I trust when setting up an S3 role ARN cloud account for Adobe Analytics exports?
  - id: getAccounts
    intent: List cloud export location accounts
    question: What cloud storage accounts are configured for Analytics exports in my company?
  - id: createAccount
    intent: Create a cloud export location account
    question: How do I connect a new cloud storage account for delivering Analytics exports?
  - id: getAccount
    intent: Get one cloud export location account
    question: How do I view the settings of one specific cloud location account?
  - id: updateAccount
    intent: Update a cloud export location account
    question: Can I rotate the secret on an existing cloud location account?
  - id: deleteAccount
    intent: Delete a cloud export location account
    question: How do I remove a cloud storage account I no longer export Analytics data to?
  phrasing_ops: 6
  slug: adobe-analytics-analytics-cloud-locations-account-api-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The analytics Cloud Locations Location API for user token
  name: Adobe Analytics Cloud Locations Location API
  phrasing_intents:
  - id: getLocations
    intent: List cloud export locations
    question: Which cloud export locations exist for my Adobe Analytics company?
  - id: createLocation
    intent: Create a cloud export location
    question: How do I add a new export destination folder or bucket under a cloud account?
  - id: getLocation
    intent: Get one cloud export location
    question: How do I see the configuration of one particular cloud export location?
  - id: updateLocation
    intent: Update a cloud export location
    question: Can I change the properties or name of a cloud export location that already exists?
  - id: deleteLocation
    intent: Delete a cloud export location
    question: How do I remove an export location I don't send data to anymore?
  phrasing_ops: 5
  slug: adobe-analytics-analytics-cloud-locations-location-api-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The Classification Dataset API from Adobe Analytics — 3 operation(s) for classification dataset.
  name: Adobe Analytics Classification Dataset API
  phrasing_intents:
  - id: getOneDataset
    intent: Get a classification dataset
    question: How do I view the columns and settings of one classification dataset?
  - id: updateOneDataset
    intent: Update a classification dataset
    question: Can I rename a classification dataset or change its default encoding?
  - id: deleteDataset
    intent: Delete a classification dataset and its data
    question: What happens to the classification data when I delete a classification dataset?
  - id: getCompatibilityMetrics
    intent: Get classification-compatible metrics for a report suite
    question: Which metrics can be used with classifications on a given report suite?
  - id: getDatasetTemplate
    intent: Download a classification dataset template
    question: How do I get a template file to fill in classification values for a dataset?
  phrasing_ops: 5
  slug: adobe-analytics-classification-dataset-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The Classification Job API from Adobe Analytics — 10 operation(s) for classification job.
  name: Adobe Analytics Classification Job API
  phrasing_intents:
  - id: commitApiImportJob
    intent: Commit a classification import job
    question: After uploading my classification file, how do I start processing the import?
  - id: createApiJobEntity
    intent: Start a file-based classification import job
    question: How do I begin a classification import that I'll upload a file to afterwards?
  - id: createExportJob
    intent: Export classification data
    question: How do I export the classification values from a dataset?
  - id: createJsonImportJob
    intent: Import classification data as JSON
    question: Can I send classification values directly as JSON instead of uploading a file?
  - id: findJobsByDataset
    intent: List classification jobs for a dataset
    question: What import and export jobs have run on my classification dataset recently?
  - id: getJobById
    intent: Get a classification job's status
    question: Did my classification import job finish?
  - id: retrieveArtifact
    intent: Download a classification export file
    question: How do I download the file my classification export job produced?
  - id: retrieveArtifactById
    intent: Download one named classification export file
    question: If an export job produced several files, how do I download a specific one by name?
  phrasing_ops: 10
  slug: adobe-analytics-classification-job-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The Collections Suites API from Adobe Analytics — 2 operation(s) for collections suites.
  name: Adobe Analytics Collections Suites API
  phrasing_intents:
  - id: getSuite_1
    intent: Get a report suite by ID
    question: How do I look up one report suite's details by its RSID?
  - id: getSuites_1
    intent: Search report suites
    question: Which report suites does my company have?
  phrasing_ops: 2
  slug: adobe-analytics-collections-suites-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: API to create, update and retrieve column presets for datafeeds with a user token
  name: Adobe Analytics Column Preset API
  phrasing_intents:
  - id: getAllColumnNames_1
    intent: List all data feed column names
    question: What columns can I include in a raw data feed?
  - id: createColumnPresetByRsid_1
    intent: Create a data feed column preset
    question: How do I save a reusable set of data feed columns for a report suite?
  - id: getColumnPreset_1
    intent: Get a data feed column preset
    question: Which columns are in a specific column preset?
  - id: getColumnPresetByRsid_1
    intent: List column presets for a report suite
    question: What column presets can I use for data feeds on a given report suite?
  phrasing_ops: 4
  slug: adobe-analytics-column-preset-api-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: API Methods for migrating projects with components from Adobe Analytics to Customer Journey Analytics
  name: Adobe Analytics Component migration API
  phrasing_intents:
  - id: summary_1
    intent: Get a project's migration summary
    question: How do I see the component summary for a Workspace project before migrating it?
  - id: bulkMigrate_1
    intent: Migrate projects in bulk
    question: Can I migrate many Analytics projects at once?
  - id: RetrieveBulkProjectStatus_1
    intent: Check bulk project migration status
    question: Have my bulk project migrations finished?
  phrasing_ops: 3
  slug: adobe-analytics-component-migration-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The data warehouse report API
  name: Adobe Analytics Data Warehouse Report API
  phrasing_intents:
  - id: get
    intent: Get a Data Warehouse report's details
    question: How do I see the full details of one Data Warehouse report run?
  - id: updateDataWarehouseJob
    intent: Update a Data Warehouse report
    question: Can I change the metadata on a Data Warehouse report that already ran?
  - id: get_1
    intent: Find Data Warehouse reports by filter
    question: Which Data Warehouse reports were generated for a given scheduled request?
  phrasing_ops: 3
  slug: adobe-analytics-data-warehouse-report-api-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The data warehouse scheduled requests API
  name: Adobe Analytics Data Warehouse Scheduled Requests API
  phrasing_intents:
  - id: getScheduledRequest_2
    intent: Find Data Warehouse scheduled requests
    question: What Data Warehouse requests are scheduled for my report suite?
  - id: createDataWarehouseScheduledJob
    intent: Schedule a Data Warehouse request
    question: How do I schedule a Data Warehouse export to run and be delivered automatically?
  - id: getScheduledRequest_1
    intent: Get a Data Warehouse scheduled request
    question: How do I see the full definition of one scheduled Data Warehouse request?
  - id: updateDataWarehouseTemplate
    intent: Update or cancel a Data Warehouse scheduled request
    question: Can I change when a scheduled Data Warehouse request runs?
  phrasing_ops: 4
  slug: adobe-analytics-data-warehouse-scheduled-requests-api-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: API to create, update and retrieve datafeed with a user token
  name: Adobe Analytics Datafeed API
  phrasing_intents:
  - id: create_1
    intent: Create a raw data feed
    question: How do I set up a recurring raw clickstream data feed for a report suite?
  - id: get_1
    intent: Get a data feed
    question: How do I see the configuration of one data feed?
  - id: update_1
    intent: Update a data feed's settings
    question: Can I change the column preset or delivery of an existing data feed?
  - id: updateStatus_1
    intent: Pause, resume or change a data feed's status
    question: How do I pause or reactivate a data feed?
  - id: getDataFeedsForReportSuite_1
    intent: List data feeds for one report suite
    question: What data feeds are configured for a single report suite?
  - id: getDataFeedsForReportSuites_1
    intent: Search data feeds across several report suites
    question: Can I get the data feeds for many report suites in one call?
  - id: getDataFeedRequestsForFeed_1
    intent: List delivery requests for one data feed
    question: How do I see the recent delivery runs of one data feed?
  - id: getDataFeedRequests_1
    intent: Search data feed requests by criteria
    question: Which data feed requests failed across my report suites?
  phrasing_ops: 8
  slug: adobe-analytics-datafeed-api-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: Methods to map Analytics dimensions to CJA data views within an XDM schema
  name: Adobe Analytics Dimensions mappings API
  phrasing_intents:
  - id: getMappingsAsCSV_1
    intent: Download dimension mappings as CSV
    question: How do I export the dimension mappings between a report suite and a data view?
  - id: updateMappingByCSV_1
    intent: Update dimension mappings from CSV
    question: Can I edit existing dimension mappings by uploading a revised CSV?
  - id: createMappingByCSV_1
    intent: Replace dimension mappings with a CSV
    question: How do I upload a CSV that overrides all current dimension mappings?
  - id: deleteAllMappings_1
    intent: Delete all dimension mappings
    question: How do I wipe every dimension mapping for a report suite and data view?
  phrasing_ops: 4
  slug: adobe-analytics-dimensions-mappings-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: Upload and monitor data of Data Sources accounts
  name: Adobe Analytics Job API
  phrasing_intents:
  - id: getJobs
    intent: List uploads to a Data Sources account
    question: What files have been uploaded to my Data Sources account and did they process?
  - id: createJob
    intent: Upload a data file to a Data Sources account
    question: How do I upload offline data to a Data Sources account through the API?
  - id: getJob
    intent: Get one Data Sources upload job
    question: How do I check whether one specific Data Sources upload succeeded?
  phrasing_ops: 3
  slug: adobe-analytics-job-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: API for users to resend, reprocess and redo datafeed requests with a user token
  name: Adobe Analytics Manage API
  phrasing_intents:
  - id: redoDatafeed_1
    intent: Redo a data feed request
    question: How do I get a failed data feed delivery again, resending if possible and reprocessing otherwise?
  - id: reprocessDatafeed_1
    intent: Reprocess a data feed request
    question: Can I force a data feed request to be regenerated from scratch?
  - id: resendDatafeed_1
    intent: Resend a data feed request
    question: Can I re-deliver an already generated data feed file without reprocessing it?
  phrasing_ops: 3
  slug: adobe-analytics-manage-api-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The Marketing Channels API from Adobe Analytics — 1 operation(s) for marketing channels.
  name: Adobe Analytics Marketing Channels API
  phrasing_intents:
  - id: getMarketingChannels
    intent: Get marketing channel setup for report suites
    question: How are marketing channels configured on my report suites?
  phrasing_ops: 1
  slug: adobe-analytics-marketing-channels-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: Methods to map Analytics metrics to CJA data views within an XDM schema
  name: Adobe Analytics Metrics mappings API
  phrasing_intents:
  - id: getMappingsAsCSV_3
    intent: Download metric mappings as CSV
    question: How do I export the metric mappings between a report suite and a data view?
  - id: updateMappingByCSV_3
    intent: Update metric mappings from CSV
    question: Can I edit existing metric mappings by uploading a revised CSV?
  - id: createMappingByCSV_3
    intent: Replace metric mappings with a CSV
    question: How do I upload a CSV that overrides all current metric mappings?
  - id: deleteAllMappings_3
    intent: Delete all metric mappings
    question: How do I wipe every metric mapping for a report suite and data view?
  phrasing_ops: 4
  slug: adobe-analytics-metrics-mappings-api
- baseURL: https://analytics.adobe.io/api
  baseurl_source: spec
  description: The Virtual Report Suites API from Adobe Analytics — 4 operation(s) for virtual report suites.
  name: Adobe Analytics Virtual Report Suites API
  phrasing_intents:
  - id: userGetVirtualReportSuites
    intent: List virtual report suites
    question: What virtual report suites exist in my company?
  - id: userCreateVirtualReportSuite
    intent: Create a virtual report suite
    question: How do I create a virtual report suite filtered by segments from a parent report suite?
  - id: userGetVirtualReportSuite
    intent: Get a virtual report suite
    question: How do I see the segments and parent of one virtual report suite?
  - id: userUpdateVirtualReportSuite
    intent: Update a virtual report suite
    question: Can I change the segments applied to an existing virtual report suite?
  - id: userDeleteVirtualReportSuite
    intent: Delete a virtual report suite
    question: How do I delete or disable a virtual report suite?
  - id: userValidateVirtualReportSuite
    intent: Validate a virtual report suite definition
    question: Can I check a virtual report suite definition is valid before creating it?
  - id: searchAll
    intent: Search virtual report suites with a request body
    question: Can I search virtual report suites by sending the criteria in a POST body?
  phrasing_ops: 7
  slug: adobe-analytics-virtual-report-suites-api
arazzos:
- description: Review saved date ranges, create an annotation for a period, then run a report over it.
  name: Adobe Analytics Annotate a Date Range and Run a Report
  slug: adobe-analytics-annotate-and-run-report-workflow
- description: Read an existing calculated metric and create a copy of it under a new name.
  name: Adobe Analytics Clone a Calculated Metric
  slug: adobe-analytics-clone-calculated-metric-workflow
- description: Read an existing segment and create a copy of it under a new name.
  name: Adobe Analytics Clone a Segment
  slug: adobe-analytics-clone-segment-workflow
- description: List a report suite's metrics, create a calculated metric, then run a report using it.
  name: Adobe Analytics Create a Calculated Metric and Run a Report
  slug: adobe-analytics-create-calculated-metric-and-run-report-workflow
- description: Inspect a report suite's dimensions, create a new segment, then run a report filtered by that segment.
  name: Adobe Analytics Create a Segment and Run a Segmented Report
  slug: adobe-analytics-create-segment-and-run-report-workflow
- description: List the dimensions and metrics in a report suite, then run a report built from them.
  name: Adobe Analytics Discover Components and Run a Report
  slug: adobe-analytics-discover-components-and-run-report-workflow
- description: Estimate the scope of a data repair, submit the repair job with the validation token, then check its status.
  name: Adobe Analytics Estimate and Run a Data Repair Job
  slug: adobe-analytics-estimate-and-run-data-repair-workflow
- description: Inventory report suites, dimensions, and metrics, then run a report in a single chained pass.
  name: Adobe Analytics Full Component Inventory and Report
  slug: adobe-analytics-full-component-inventory-and-report-workflow
- description: List the company segments, fetch a chosen segment's details, then run a report filtered by it.
  name: Adobe Analytics Report on an Existing Segment
  slug: adobe-analytics-report-on-existing-segment-workflow
- description: List accessible report suites, confirm one by ID, then run a report against it.
  name: Adobe Analytics Select a Report Suite and Run a Report
  slug: adobe-analytics-select-report-suite-and-run-report-workflow
- description: Look up a segment by ID and update it if it exists, otherwise create a new one.
  name: Adobe Analytics Upsert a Segment
  slug: adobe-analytics-upsert-segment-workflow
- description: Validate a gzip-compressed events file and upload it only when validation passes.
  name: Adobe Analytics Validate then Upload a Batch Events File
  slug: adobe-analytics-validate-then-upload-events-workflow
artifact_total: 201
asyncapis:
- description: The Adobe Analytics Livestream API delivers real-time analytics hit data to a connected client as each hit is processed by Adobe Analytics servers. Data is streamed in line-delimited JSON format compr
  name: Adobe Analytics Livestream API
  slug: adobe-analytics-livestream-asyncapi
collections:
- collection_type: postman
  name: Adobe Analytics API
  slug: postman-adobe-analytics-api
- collection_type: postman
  name: Adobe Analytics Bulk Data Insertion API
  slug: postman-adobe-analytics-bulk-data-insertion-api
- collection_type: postman
  name: Adobe Analytics Data Repair API
  slug: postman-adobe-analytics-data-repair-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe Analytics Annotations API
  slug: open-adobe-analytics-annotations-api
- collection_type: open
  name: Adobe Analytics API
  slug: open-adobe-analytics-api
- collection_type: open
  name: Adobe Analytics Bulk Data Insertion API
  slug: open-adobe-analytics-bulk-data-insertion-api
- collection_type: open
  name: Adobe Analytics Annotations Calculated Metrics API
  slug: open-adobe-analytics-calculated-metrics-api
- collection_type: open
  name: Adobe Analytics Data Repair API
  slug: open-adobe-analytics-data-repair-api
- collection_type: open
  name: Adobe Analytics Annotations Date Ranges API
  slug: open-adobe-analytics-date-ranges-api
- collection_type: open
  name: Adobe Analytics Annotations Dimensions API
  slug: open-adobe-analytics-dimensions-api
- collection_type: open
  name: Adobe Analytics Annotations Events API
  slug: open-adobe-analytics-events-api
- collection_type: open
  name: Adobe Analytics Annotations Jobs API
  slug: open-adobe-analytics-jobs-api
- collection_type: open
  name: Adobe Analytics Annotations Metrics API
  slug: open-adobe-analytics-metrics-api
- collection_type: open
  name: Adobe Analytics Annotations Report Suites API
  slug: open-adobe-analytics-report-suites-api
- collection_type: open
  name: Adobe Analytics Annotations Reports API
  slug: open-adobe-analytics-reports-api
- collection_type: open
  name: Adobe Analytics Annotations Segments API
  slug: open-adobe-analytics-segments-api
- collection_type: open
  name: Adobe Analytics Annotations Server Call Estimate API
  slug: open-adobe-analytics-server-call-estimate-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/capabilities/adobe-analytics-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/adobe-analytics-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/AdobeDocs/analytics-1.4-apis/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/AdobeDocs/analytics-1.4-apis/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/AdobeDocs/analytics-1.4-apis/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/AdobeDocs/analytics-1.4-apis/blob/main/LICENSE
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/packages/adobe-analytics-packages.yml
  title: ''
  type: Packages
  url: packages/adobe-analytics-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/well-known/adobe-analytics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adobe-analytics-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/mcp/adobe-analytics-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adobe-analytics-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/llms/adobe-analytics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adobe-analytics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/overlays/adobe-analytics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adobe-analytics-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/overlays/adobe-analytics-bulk-data-insertion-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adobe-analytics-bulk-data-insertion-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/overlays/adobe-analytics-data-repair-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adobe-analytics-data-repair-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/conformance/adobe-analytics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adobe-analytics-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/errors/adobe-analytics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adobe-analytics-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/lifecycle/adobe-analytics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adobe-analytics-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/conventions/adobe-analytics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adobe-analytics-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/changelog/adobe-analytics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adobe-analytics-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/data-model/adobe-analytics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adobe-analytics-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/agentic-access/adobe-analytics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-analytics-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/security/adobe-analytics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-analytics-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/security/adobe-analytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adobe-analytics-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/authentication/adobe-analytics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adobe-analytics-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-analytics/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-annotate-and-run-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-annotate-and-run-report-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-clone-calculated-metric-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-clone-calculated-metric-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-clone-segment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-clone-segment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-create-calculated-metric-and-run-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-create-calculated-metric-and-run-report-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-create-segment-and-run-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-create-segment-and-run-report-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-discover-components-and-run-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-discover-components-and-run-report-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-estimate-and-run-data-repair-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-estimate-and-run-data-repair-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-full-component-inventory-and-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-full-component-inventory-and-report-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-report-on-existing-segment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-report-on-existing-segment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-select-report-suite-and-run-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-select-report-suite-and-run-report-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-upsert-segment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-upsert-segment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/arazzo/adobe-analytics-validate-then-upload-events-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-analytics-validate-then-upload-events-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/analytics-apis/docs/2.0/
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/docs/analytics.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.adobe.com/analytics-apis/docs/2.0/guides/authentication/
- group: operate
  title: ''
  type: Support
  url: https://developer.adobe.com/analytics-apis/docs/2.0/support/
- group: operate
  title: ''
  type: Support
  url: https://experienceleaguecommunities.adobe.com/t5/adobe-analytics/ct-p/adobe-analytics-community
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/adobe-analytics
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdobeDocs
- group: operate
  title: ''
  type: ChangeLog
  url: https://experienceleague.adobe.com/en/docs/analytics/release-notes/latest
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.adobe.com/en/topics/analytics
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AdobeDocs/analytics-2.0-apis
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/json-schema/adobe-analytics-report-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/adobe-analytics-report-request-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/json-ld/adobe-analytics-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adobe-analytics-context.jsonld
- group: build
  title: Analytics MCP Servers Documentation
  type: GitHubRepository
  url: https://github.com/AdobeDocs/analytics-mcp
- group: build
  title: Analytics 1.4 APIs Documentation
  type: GitHubRepository
  url: https://github.com/AdobeDocs/analytics-1.4-apis
- group: learn
  title: ''
  type: Training
  url: https://experienceleague.adobe.com/docs/analytics-learn/tutorials/overview.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/json-ld/adobe-analytics-bulk-data-insertion-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adobe-analytics-bulk-data-insertion-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/json-ld/adobe-analytics-data-repair-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adobe-analytics-data-repair-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/rules/adobe-analytics-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/adobe-analytics-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/vocabulary/adobe-analytics-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/adobe-analytics-vocabulary.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/packages/adobe-analytics-packages.yml
  title: Official and community client libraries (7 first-party packages)
  type: SDKs
  url: packages/adobe-analytics-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/rate-limits/adobe-analytics-rate-limits.yml
  title: Published rate limits — 12 requests / 6 seconds per user
  type: RateLimits
  url: rate-limits/adobe-analytics-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/plans/adobe-analytics-plans-pricing.yml
  title: Enterprise packages (contact sales; no list pricing published)
  type: Plans
  url: plans/adobe-analytics-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/finops/adobe-analytics-finops.yml
  title: ''
  type: FinOps
  url: finops/adobe-analytics-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/lifecycle/adobe-analytics-lifecycle.yml
  title: Adobe Analytics 1.4 API end-of-life policy (EOL 2026-08-12)
  type: Deprecation
  url: lifecycle/adobe-analytics-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/security/adobe-analytics-vulnerability-disclosure.yml
  title: Adobe PSIRT vulnerability disclosure + HackerOne program
  type: Security
  url: security/adobe-analytics-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/security/adobe-analytics-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adobe-analytics-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/security/adobe-analytics-trust-center.yml
  title: Adobe Experience Cloud certifications (FedRAMP Tailored, SOC 2 Type 2, ISO 27001:2022, CSA STAR L2)
  type: Compliance
  url: security/adobe-analytics-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/scopes/adobe-analytics-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adobe-analytics-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/mcp/adobe-analytics-tool-crosswalk.yml
  title: MCP tool to REST operation crosswalk
  type: ToolCrosswalk
  url: mcp/adobe-analytics-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/skills/_index.yml
  title: Five Adobe-published Agent Skills for the Adobe Analytics MCP server
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/llms/adobe-analytics-experienceleague-llms.txt
  title: Adobe-published llms.txt for the Experience League documentation host (verbatim)
  type: LLMsTxt
  url: llms/adobe-analytics-experienceleague-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/collections/adobe-analytics-api.opencollection.json
  title: ''
  type: OpenCollection
  url: collections/adobe-analytics-api.opencollection.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/postman/adobe-analytics-api.postman_collection.json
  title: ''
  type: PostmanCollection
  url: postman/adobe-analytics-api.postman_collection.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/rules/adobe-analytics-asyncapi-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/adobe-analytics-asyncapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/rules/adobe-analytics-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/adobe-analytics-jsonschema-spectral-rules.yml
- group: docs
  title: Adobe Analytics MCP server documentation
  type: Documentation
  url: https://developer.adobe.com/analytics-mcp/docs/aa/
- group: commercial
  title: ''
  type: Pricing
  url: https://business.adobe.com/products/analytics/pricing.html
- group: docs
  title: Adobe Analytics 2.0 API reference
  type: APIReference
  url: https://developer.adobe.com/analytics-apis/docs/2.0/apis/
- group: start
  title: Adobe Developer Console — create the project and OAuth credentials
  type: SignUp
  url: https://developer.adobe.com/console/
created: 2024-01-01 00:00:00+00:00
description: Adobe Analytics provides real-time analytics and detailed segmentation capabilities across all marketing channels, enabling organizations to discover high-value audiences and power customer intelligence.
examples:
- key_count: 5
  name: Adobe Analytics Annotation Create Example
  slug: adobe-analytics-annotation-create-example
- key_count: 6
  name: Adobe Analytics Annotation Example
  slug: adobe-analytics-annotation-example
- key_count: 2
  name: Adobe Analytics Bulk Data Insertion Error Response Example
  slug: adobe-analytics-bulk-data-insertion-error-response-example
- key_count: 3
  name: Adobe Analytics Bulk Data Insertion Upload Response Example
  slug: adobe-analytics-bulk-data-insertion-upload-response-example
- key_count: 5
  name: Adobe Analytics Calculated Metric Create Example
  slug: adobe-analytics-calculated-metric-create-example
- key_count: 8
  name: Adobe Analytics Calculated Metric Example
  slug: adobe-analytics-calculated-metric-example
- key_count: 3
  name: Adobe Analytics Calculated Metric List Example
  slug: adobe-analytics-calculated-metric-list-example
- key_count: 2
  name: Adobe Analytics Data Repair Error Response Example
  slug: adobe-analytics-data-repair-error-response-example
- key_count: 3
  name: Adobe Analytics Data Repair Repair Action Example
  slug: adobe-analytics-data-repair-repair-action-example
- key_count: 2
  name: Adobe Analytics Data Repair Repair Filter Example
  slug: adobe-analytics-data-repair-repair-filter-example
- key_count: 1
  name: Adobe Analytics Data Repair Repair Job Definition Example
  slug: adobe-analytics-data-repair-repair-job-definition-example
- key_count: 10
  name: Adobe Analytics Data Repair Repair Job Example
  slug: adobe-analytics-data-repair-repair-job-example
- key_count: 5
  name: Adobe Analytics Data Repair Server Call Estimate Example
  slug: adobe-analytics-data-repair-server-call-estimate-example
- key_count: 4
  name: Adobe Analytics Date Range Example
  slug: adobe-analytics-date-range-example
- key_count: 6
  name: Adobe Analytics Dimension Example
  slug: adobe-analytics-dimension-example
- key_count: 3
  name: Adobe Analytics Error Response Example
  slug: adobe-analytics-error-response-example
- key_count: 2
  name: Adobe Analytics Metric Container Example
  slug: adobe-analytics-metric-container-example
- key_count: 7
  name: Adobe Analytics Metric Example
  slug: adobe-analytics-metric-example
- key_count: 3
  name: Adobe Analytics Owner Example
  slug: adobe-analytics-owner-example
- key_count: 5
  name: Adobe Analytics Report Filter Example
  slug: adobe-analytics-report-filter-example
- key_count: 4
  name: Adobe Analytics Report Metric Example
  slug: adobe-analytics-report-metric-example
- key_count: 7
  name: Adobe Analytics Report Request Example
  slug: adobe-analytics-report-request-example
- key_count: 5
  name: Adobe Analytics Report Response Example
  slug: adobe-analytics-report-response-example
- key_count: 3
  name: Adobe Analytics Report Row Example
  slug: adobe-analytics-report-row-example
- key_count: 3
  name: Adobe Analytics Report Settings Example
  slug: adobe-analytics-report-settings-example
- key_count: 4
  name: Adobe Analytics Report Suite Example
  slug: adobe-analytics-report-suite-example
- key_count: 3
  name: Adobe Analytics Report Suite List Example
  slug: adobe-analytics-report-suite-list-example
- key_count: 4
  name: Adobe Analytics Segment Create Example
  slug: adobe-analytics-segment-create-example
- key_count: 8
  name: Adobe Analytics Segment Example
  slug: adobe-analytics-segment-example
- key_count: 4
  name: Adobe Analytics Segment List Example
  slug: adobe-analytics-segment-list-example
- key_count: 4
  name: Adobe Analytics Tag Example
  slug: adobe-analytics-tag-example
features:
- description: Access and analyze data in real time as visitors interact with digital properties.
  name: Real-Time Analytics
- description: Build custom segments to isolate and analyze specific visitor groups and behaviors.
  name: Custom Segmentation
- description: Create derived metrics combining existing metrics with mathematical formulas.
  name: Calculated Metrics
- description: Organize and partition data collection across multiple sites and business units.
  name: Report Suites
- description: Mark specific dates or ranges in reports with notes for contextual analysis.
  name: Annotations
- description: Upload server-side event data in compressed CSV batches for high-volume collection.
  name: Bulk Data Insertion
- description: Permanently delete or transform previously ingested data for privacy compliance.
  name: Data Repair
- description: Receive real-time streaming hit data as each event is processed by Adobe servers.
  name: Livestream
- description: Programmatically discover all available dimensions and metrics in report suites.
  name: Dimension And Metric Exploration
- description: Apply tags to segments, metrics, and other components for organization and discovery.
  name: Component Tagging
finops:
- name: Adobe Analytics Finops
  service_category: Analytics
  slug: adobe-analytics-finops
image: /assets/icons/adobe-analytics.png
integrations:
- description: Send Analytics data to Experience Platform for unified customer profiles and journey orchestration.
  name: Adobe Experience Platform
- description: Use Analytics segments to power personalization and A/B testing in Adobe Target.
  name: Adobe Target
- description: Share audience segments between Analytics and Audience Manager for cross-channel activation.
  name: Adobe Audience Manager
- description: Integrate campaign data with Analytics for end-to-end campaign performance measurement.
  name: Adobe Campaign
- description: Extend Analytics data into CJA for cross-channel analysis with Experience Platform data.
  name: Adobe Customer Journey Analytics
- description: Deploy and manage Analytics tags via Adobe Experience Platform Launch tag management.
  name: Adobe Launch
- description: Import Google Ads cost and click data for integrated paid search analytics.
  name: Google Ads
- description: Connect Analytics data to Power BI dashboards for enterprise reporting and visualization.
  name: Microsoft Power BI
json_schemas:
- name: AnnotationCreate
  property_count: 5
  slug: adobe-analytics-annotation-create
- name: Annotation
  property_count: 6
  slug: adobe-analytics-annotation
- name: ErrorResponse
  property_count: 2
  slug: adobe-analytics-bulk-data-insertion-error-response
- name: UploadResponse
  property_count: 3
  slug: adobe-analytics-bulk-data-insertion-upload-response
- name: ValidationError
  property_count: 3
  slug: adobe-analytics-bulk-data-insertion-validation-error
- name: ValidationResponse
  property_count: 3
  slug: adobe-analytics-bulk-data-insertion-validation-response
- name: CalculatedMetricCreate
  property_count: 5
  slug: adobe-analytics-calculated-metric-create
- name: CalculatedMetricList
  property_count: 3
  slug: adobe-analytics-calculated-metric-list
- name: CalculatedMetric
  property_count: 8
  slug: adobe-analytics-calculated-metric
- name: ErrorResponse
  property_count: 2
  slug: adobe-analytics-data-repair-error-response
- name: RepairAction
  property_count: 3
  slug: adobe-analytics-data-repair-repair-action
- name: RepairFilter
  property_count: 2
  slug: adobe-analytics-data-repair-repair-filter
- name: RepairJobDefinition
  property_count: 1
  slug: adobe-analytics-data-repair-repair-job-definition
- name: RepairJob
  property_count: 10
  slug: adobe-analytics-data-repair-repair-job
- name: ServerCallEstimate
  property_count: 5
  slug: adobe-analytics-data-repair-server-call-estimate
- name: DateRange
  property_count: 4
  slug: adobe-analytics-date-range
- name: Dimension
  property_count: 6
  slug: adobe-analytics-dimension
- name: ErrorResponse
  property_count: 3
  slug: adobe-analytics-error-response
- name: MetricContainer
  property_count: 2
  slug: adobe-analytics-metric-container
- name: Metric
  property_count: 7
  slug: adobe-analytics-metric
- name: Owner
  property_count: 3
  slug: adobe-analytics-owner
- name: ReportFilter
  property_count: 5
  slug: adobe-analytics-report-filter
- name: ReportMetric
  property_count: 4
  slug: adobe-analytics-report-metric
- name: ReportRequest
  property_count: 7
  slug: adobe-analytics-report-request
- name: ReportResponse
  property_count: 5
  slug: adobe-analytics-report-response
- name: ReportRow
  property_count: 3
  slug: adobe-analytics-report-row
- name: ReportSettings
  property_count: 3
  slug: adobe-analytics-report-settings
- name: ReportSuiteList
  property_count: 3
  slug: adobe-analytics-report-suite-list
- name: ReportSuite
  property_count: 4
  slug: adobe-analytics-report-suite
- name: SegmentCreate
  property_count: 4
  slug: adobe-analytics-segment-create
- name: SegmentList
  property_count: 4
  slug: adobe-analytics-segment-list
- name: Segment
  property_count: 8
  slug: adobe-analytics-segment
- name: Tag
  property_count: 4
  slug: adobe-analytics-tag
json_structures:
- name: Adobe Analytics Annotation Create Structure
  property_count: 5
  slug: adobe-analytics-annotation-create-structure
- name: Adobe Analytics Annotation Structure
  property_count: 6
  slug: adobe-analytics-annotation-structure
- name: Adobe Analytics Bulk Data Insertion Error Response Structure
  property_count: 2
  slug: adobe-analytics-bulk-data-insertion-error-response-structure
- name: Adobe Analytics Bulk Data Insertion Upload Response Structure
  property_count: 3
  slug: adobe-analytics-bulk-data-insertion-upload-response-structure
- name: Adobe Analytics Bulk Data Insertion Validation Error Structure
  property_count: 3
  slug: adobe-analytics-bulk-data-insertion-validation-error-structure
- name: Adobe Analytics Bulk Data Insertion Validation Response Structure
  property_count: 3
  slug: adobe-analytics-bulk-data-insertion-validation-response-structure
- name: Adobe Analytics Calculated Metric Create Structure
  property_count: 5
  slug: adobe-analytics-calculated-metric-create-structure
- name: Adobe Analytics Calculated Metric List Structure
  property_count: 3
  slug: adobe-analytics-calculated-metric-list-structure
- name: Adobe Analytics Calculated Metric Structure
  property_count: 8
  slug: adobe-analytics-calculated-metric-structure
- name: Adobe Analytics Data Repair Error Response Structure
  property_count: 2
  slug: adobe-analytics-data-repair-error-response-structure
- name: Adobe Analytics Data Repair Repair Action Structure
  property_count: 3
  slug: adobe-analytics-data-repair-repair-action-structure
- name: Adobe Analytics Data Repair Repair Filter Structure
  property_count: 2
  slug: adobe-analytics-data-repair-repair-filter-structure
- name: Adobe Analytics Data Repair Repair Job Definition Structure
  property_count: 1
  slug: adobe-analytics-data-repair-repair-job-definition-structure
- name: Adobe Analytics Data Repair Repair Job Structure
  property_count: 10
  slug: adobe-analytics-data-repair-repair-job-structure
- name: Adobe Analytics Data Repair Server Call Estimate Structure
  property_count: 5
  slug: adobe-analytics-data-repair-server-call-estimate-structure
- name: Adobe Analytics Date Range Structure
  property_count: 4
  slug: adobe-analytics-date-range-structure
- name: Adobe Analytics Dimension Structure
  property_count: 6
  slug: adobe-analytics-dimension-structure
- name: Adobe Analytics Error Response Structure
  property_count: 3
  slug: adobe-analytics-error-response-structure
- name: Adobe Analytics Metric Container Structure
  property_count: 2
  slug: adobe-analytics-metric-container-structure
- name: Adobe Analytics Metric Structure
  property_count: 7
  slug: adobe-analytics-metric-structure
- name: Adobe Analytics Owner Structure
  property_count: 3
  slug: adobe-analytics-owner-structure
- name: Adobe Analytics Report Filter Structure
  property_count: 5
  slug: adobe-analytics-report-filter-structure
- name: Adobe Analytics Report Metric Structure
  property_count: 4
  slug: adobe-analytics-report-metric-structure
- name: Adobe Analytics Report Request Structure
  property_count: 7
  slug: adobe-analytics-report-request-structure
- name: Adobe Analytics Report Response Structure
  property_count: 5
  slug: adobe-analytics-report-response-structure
- name: Adobe Analytics Report Row Structure
  property_count: 3
  slug: adobe-analytics-report-row-structure
- name: Adobe Analytics Report Settings Structure
  property_count: 3
  slug: adobe-analytics-report-settings-structure
- name: Adobe Analytics Report Suite List Structure
  property_count: 3
  slug: adobe-analytics-report-suite-list-structure
- name: Adobe Analytics Report Suite Structure
  property_count: 4
  slug: adobe-analytics-report-suite-structure
- name: Adobe Analytics Segment Create Structure
  property_count: 4
  slug: adobe-analytics-segment-create-structure
- name: Adobe Analytics Segment List Structure
  property_count: 4
  slug: adobe-analytics-segment-list-structure
- name: Adobe Analytics Segment Structure
  property_count: 8
  slug: adobe-analytics-segment-structure
- name: Adobe Analytics Tag Structure
  property_count: 4
  slug: adobe-analytics-tag-structure
jsonld:
- class_count: 0
  name: Adobe Analytics Bulk Data Insertion Context
  property_count: 4
  slug: adobe-analytics-bulk-data-insertion-context
- class_count: 0
  name: Adobe Analytics Context
  property_count: 23
  slug: adobe-analytics-context
- class_count: 0
  name: Adobe Analytics Data Repair Context
  property_count: 6
  slug: adobe-analytics-data-repair-context
layout: provider
mcp_servers:
- description: Adobe publishes an official, Adobe-hosted (remote) Model Context Protocol server for Adobe Analytics. It lets MCP clients (Claude, ChatGPT, Cursor) discover components (report suites, dimensions, metr
  name: Adobe Analytics MCP Server
  slug: adobe-analytics-mcp
modified: '2026-09-16'
name: Adobe Analytics
nav: Providers
network: true
overview: 'Adobe Analytics publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Livestream API, Annotations API, Calculated Metrics API, and 28 more. Tagged areas include Adobe, Analytics, Business Intelligence, Customer Intelligence, and Digital Marketing.


  The Adobe Analytics catalog on APIs.io includes 1 event-driven AsyncAPI specification, 3 JSON-LD contexts, and 3 Spectral governance rulesets.


  Adobe Analytics'' developer surface includes changelog, authentication, developer portal, documentation, getting-started guide, developer console, support, and 73 more developer resources.'
plans:
- name: Adobe Analytics Plans Pricing
  plan_count: 3
  slug: adobe-analytics-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Adobe Analytics Rate Limits
  slug: adobe-analytics-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Adobe Analytics API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: adobe-analytics-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Adobe Analytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adobe-analytics-jsonschema-spectral-rules
- effective_rule_count: 21
  extends: []
  name: Adobe Analytics API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: adobe-analytics-spectral-rules
scopes:
- name: Adobe Analytics Scopes
  scope_count: 3
  slug: adobe-analytics-scopes
  summary_line: 3 scopes
score:
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 37
    catalog_earned: 66.0
    catalog_earned_first_party: 8.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 61.7
    developer_ergonomics: 66.7
    discoverability: 71.7
    operational_transparency: 65.8
  open_source:
    applies: true
    score: 40.0
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/screenshots/adobe-analytics-2026-06-20T164808.png
security:
- kind: authentication
  name: Adobe Analytics Authentication
  slug: adobe-analytics-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Adobe Analytics Domain Security
  slug: adobe-analytics-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Analytics Vulnerability Disclosure
  slug: adobe-analytics-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Adobe Analytics Trust Center
  slug: adobe-analytics-trust-center
  summary_line: FedRAMP Tailored, SOC 2 Type 2, SOC 3, ISO 9001:2015, ISO 27001:2022, ISO 27017:2015, ISO 27018:2019, ISO 22301:2019, CSA STAR Level 2, IRAP Assessed, HIPAA ready, GLBA ready, FERPA ready, TrustArc GDPR Privacy Practices Management Compliance Validation, TrustArc APEC Privacy Recognition for Processors (PRP)
slug: adobe-analytics
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
use_cases:
- description: Measure effectiveness of marketing campaigns across channels with attribution and conversion tracking.
  name: Marketing Campaign Analysis
- description: Analyze multi-touch customer journeys to identify drop-off points and optimize conversion paths.
  name: Customer Journey Optimization
- description: Evaluate which content resonates most with audiences and drives engagement.
  name: Content Performance Tracking
- description: Discover high-value audience segments for personalized marketing and advertising.
  name: Audience Discovery And Targeting
- description: Delete or repair PII and sensitive data to comply with GDPR, CCPA, and other regulations.
  name: Privacy Compliance Data Management
- description: Monitor live traffic and KPIs with streaming data for immediate anomaly detection.
  name: Real-Time Monitoring And Alerting
- description: Collect analytics data from backend systems, IoT devices, and server-side applications.
  name: Server-Side Data Collection
- description: Combine web, mobile, and offline data for unified cross-channel analytics reporting.
  name: Cross-Channel Reporting
website: https://www.adobe.com/
---
