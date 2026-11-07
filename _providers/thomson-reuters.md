---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - finops
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 812
  human_in_the_loop: 24
  name: Thomson Reuters Agentic Access
  operation_count: 2131
  slug: thomson-reuters-agentic-access
  summary_line: 2131 operations · 812 acting · 24 human-in-the-loop
api_count: 134
apis:
- description: 'Access Westlaw legal research content including case law, statutes, regulations, and secondary sources. Includes SEC Filings API, Dockets API, and Litigation Analytics providing structured legal data '
  name: Thomson Reuters Westlaw API
  slug: westlaw-api
- description: Checkpoint Search API provides access to Thomson Reuters Checkpoint tax and accounting research content including tax regulations, guidance, and analytical tools for tax professionals and accountants.
  name: Thomson Reuters Checkpoint API
  slug: checkpoint-api
- description: Risk and Fraud APIs automate customer onboarding, identity verification, risk assessments, adverse media screening, investigations, and compliance monitoring. Includes tools for KYC, AML, and third-pa
  name: Thomson Reuters Risk and Fraud API
  slug: risk-fraud-api
- baseURL: https://api-apac.onesourcetax.com/trusts/v1/datasets
  baseurl_source: declared
  description: API for managing and accessing trusts datasets, including operations for creation, retrieval, update, and deletion.
  name: Datasets API
  slug: datasets-api
- baseURL: https://api-emea.onesourcetax.com/corporate-tax/v1/exports
  baseurl_source: declared
  description: This API provides endpoints for fetch all exports notes and queries.
  name: Exports API
  slug: exports-api
- baseURL: https://api.onesourcetax.com/income-tax/binders
  baseurl_source: declared
  description: 'This endpoint assigns groups, preparers, reviewers, managers, partners, and time tracking information to tax returns. When using the /locator/v2/assignment endpoint to assign an existing locator to a '
  name: Tax Return Import/Export API
  slug: tax-return-import-export-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/companies-api/v1
  baseurl_source: declared
  description: The Companies API provides access to offices, organizational units and practice groups in the Tracker Company database.
  name: Companies API
  slug: companies-api
- baseURL: https://api-emea.onesourcetax.com/corporate-tax/v1/prints
  baseurl_source: declared
  description: The Prints API provides endpoints for managing print jobs, including generating, downloading, and retrieving the status of prints. It also allows users to fetch print configuration metadata.
  name: Prints API
  slug: prints-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2/reports
  baseurl_source: declared
  description: The Reports API provides endpoints for retrieving a list of available reports, executing reports with specified parameters, and checking the status of report operations. It allows users to interact wi
  name: Reports API
  slug: reports-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/firms-api/v2
  baseurl_source: declared
  description: The Firms API provides access to Firms metadata in the Tracker Company and TrackerMaster databases.
  name: Firms API
  slug: firms-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/matters-api/v1
  baseurl_source: declared
  description: The Matters API exposes endpoints to create, update and retrieve a matter. Batching of matter requests is also supported through the $batch endpoint.
  name: Matters API
  slug: matters-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/users-api/v1
  baseurl_source: declared
  description: The Users API provides access to Users metadata and roles in the Tracker Company and TrackerMaster databases
  name: Users API
  slug: users-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Account API from Thomson Reuters — 5 operation(s) for account.
  name: Thomson Reuters Account API
  slug: thomson-reuters-account-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Account Tracking API from Thomson Reuters — 1 operation(s) for account tracking.
  name: Thomson Reuters Account Tracking API
  slug: thomson-reuters-account-tracking-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Accounts API from Thomson Reuters — 10 operation(s) for accounts.
  name: Thomson Reuters Accounts API
  slug: thomson-reuters-accounts-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Accounts Rollup API from Thomson Reuters — 11 operation(s) for accounts rollup.
  name: Thomson Reuters Accounts Rollup API
  slug: thomson-reuters-accounts-rollup-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The Accruals API from Thomson Reuters — 4 operation(s) for accruals.
  name: Thomson Reuters Accruals API
  slug: thomson-reuters-accruals-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Activity API from Thomson Reuters — 9 operation(s) for activity.
  name: Thomson Reuters Activity API
  slug: thomson-reuters-activity-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Adhoc Benefit API from Thomson Reuters — 1 operation(s) for adhoc benefit.
  name: Thomson Reuters Adhoc Benefit API
  slug: thomson-reuters-adhoc-benefit-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/firms-api/v2
  baseurl_source: declared
  description: Manage the firm alerts to control the firm invoice processing flow. The alerts are displayed on invoices submitted by firms or when the firm attempts to submit an invoice.
  name: Thomson Reuters Alerts API
  slug: thomson-reuters-alerts-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2
  baseurl_source: declared
  description: The Allocations API from Thomson Reuters — 2 operation(s) for allocations.
  name: Thomson Reuters Allocations API
  slug: thomson-reuters-allocations-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/ap-exchange-api/v1
  baseurl_source: declared
  description: Use the AP Batch Files AP Exchange API to view summaries and supporting files for batch runs.
  name: Thomson Reuters AP Batch Files API
  slug: thomson-reuters-ap-batch-files-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/ap-exchange-api/v1
  baseurl_source: declared
  description: Use the AP Batches AP Exchange API to view AP route batches and view and update batch runs.
  name: Thomson Reuters AP Batches API
  slug: thomson-reuters-ap-batches-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/ap-exchange-api/v1
  baseurl_source: declared
  description: Use the AP Route Email Recipients Exchange API to view the email addresses of recipients for AP route.
  name: Thomson Reuters AP Route Email Recipients API
  slug: thomson-reuters-ap-route-email-recipients-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/ap-exchange-api/v1
  baseurl_source: declared
  description: Use the AP Routes AP Exchange API to view existing AP routes in Tracker.
  name: Thomson Reuters AP Routes API
  slug: thomson-reuters-ap-routes-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Application Association API from Thomson Reuters — 1 operation(s) for application association.
  name: Thomson Reuters Application Association API
  slug: thomson-reuters-application-association-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The APRoutes API from Thomson Reuters — 3 operation(s) for aproutes.
  name: Thomson Reuters AP Routes API
  slug: thomson-reuters-aproutes-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Asset API from Thomson Reuters — 3 operation(s) for asset.
  name: Thomson Reuters Asset API
  slug: thomson-reuters-asset-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Assignments endpoints for statutory reporting. Retrieves master account assignments for a category structure in a financial period.
  name: Thomson Reuters Assignments API
  slug: thomson-reuters-assignments-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Attachment API API from Thomson Reuters — 2 operation(s) for attachment api.
  name: Thomson Reuters Attachment API
  slug: thomson-reuters-attachment-api-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Authorities API from Thomson Reuters — 1 operation(s) for authorities.
  name: Thomson Reuters Authorities API
  slug: thomson-reuters-authorities-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Authorities -📦 Version 1 Endpoints API from Thomson Reuters — 1 operation(s) for authorities -📦 version 1 endpoints.
  name: Thomson Reuters Authorities -📦 Version 1 Endpoints API
  slug: thomson-reuters-authorities-version-1-endpoints-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Authorities -📦 Version 2 Endpoints API from Thomson Reuters — 1 operation(s) for authorities -📦 version 2 endpoints.
  name: Thomson Reuters Authorities -📦 Version 2 Endpoints API
  slug: thomson-reuters-authorities-version-2-endpoints-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Operations related to authority API controller
  name: Thomson Reuters Authority API Controller API
  slug: thomson-reuters-authority-api-controller-api
- baseURL: https://api.thomsonreuters.com/gosystem
  baseurl_source: declared
  description: The Authorization API from Thomson Reuters — 6 operation(s) for authorization.
  name: Thomson Reuters Authorization API
  slug: thomson-reuters-authorization-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Authorize API from Thomson Reuters — 1 operation(s) for authorize.
  name: Thomson Reuters Authorize API
  slug: thomson-reuters-authorize-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/matters-api/v1
  baseurl_source: declared
  description: Use the Batch API to create batch request and check batch status.
  name: Thomson Reuters Batches API
  slug: thomson-reuters-batches-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The BilledToEntities API from Thomson Reuters — 3 operation(s) for billedtoentities.
  name: Thomson Reuters Billed To Entities API
  slug: thomson-reuters-billedtoentities-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Blog API API from Thomson Reuters — 3 operation(s) for blog api.
  name: Thomson Reuters Blog API
  slug: thomson-reuters-blog-api-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Blueprint CustomViews API from Thomson Reuters — 2 operation(s) for blueprint customviews.
  name: Thomson Reuters Blueprint CustomViews API
  slug: thomson-reuters-blueprint-customviews-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Blueprint Types API from Thomson Reuters — 2 operation(s) for blueprint types.
  name: Thomson Reuters Blueprint Types API
  slug: thomson-reuters-blueprint-types-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Blueprints API from Thomson Reuters — 3 operation(s) for blueprints.
  name: Thomson Reuters Blueprints API
  slug: thomson-reuters-blueprints-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Board Benefit API from Thomson Reuters — 1 operation(s) for board benefit.
  name: Thomson Reuters Board Benefit API
  slug: thomson-reuters-board-benefit-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The Budgets API from Thomson Reuters — 5 operation(s) for budgets.
  name: Thomson Reuters Budgets API
  slug: thomson-reuters-budgets-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance
  baseurl_source: declared
  description: The Calculations API from Thomson Reuters — 6 operation(s) for calculations.
  name: Thomson Reuters Calculations API
  slug: thomson-reuters-calculations-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Car Parking Benefit API from Thomson Reuters — 1 operation(s) for car parking benefit.
  name: Thomson Reuters Car Parking Benefit API
  slug: thomson-reuters-car-parking-benefit-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Categories endpoints for statutory reporting. Retrieve categories and their entries.
  name: Thomson Reuters Categories API
  slug: thomson-reuters-categories-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Certificate Service API from Thomson Reuters — 1 operation(s) for certificate service.
  name: Thomson Reuters Certificate Service API
  slug: thomson-reuters-certificate-service-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The chart-imports API from Thomson Reuters — 4 operation(s) for chart-imports.
  name: Thomson Reuters Chart Imports API
  slug: thomson-reuters-chart-imports-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Charts API from Thomson Reuters — 1 operation(s) for charts.
  name: Thomson Reuters Charts API
  slug: thomson-reuters-charts-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Charts of Accounts API from Thomson Reuters — 3 operation(s) for charts of accounts.
  name: Thomson Reuters Charts of Accounts API
  slug: thomson-reuters-charts-of-accounts-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Classifications Controller
  name: Thomson Reuters Classifications Controller API
  slug: thomson-reuters-classifications-controller-api
- baseURL: https://api.sureprep.com
  baseurl_source: declared
  description: Using V5 of our API webhooks to receive updates on your client’s records, SurePrep sends your API an automated message with real-time information as soon as it’s available. Once you receive a message,
  name: Thomson Reuters Client activity notifications - V5 API
  slug: thomson-reuters-client-activity-notifications-v5-api
- baseURL: https://api.sureprep.com
  baseurl_source: declared
  description: Using V7 of our API webhooks to receive updates on your client’s records, SurePrep sends your API an automated message with real-time information as soon as it’s available. Once you receive a message,
  name: Thomson Reuters Client activity notifications - V7 API
  slug: thomson-reuters-client-activity-notifications-v7-api
- baseURL: https://api.thomsonreuters.com/us/engagementmanager
  baseurl_source: declared
  description: Update list of clients in engagement manager
  name: Thomson Reuters Clients API
  slug: thomson-reuters-clients-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Collections API from Thomson Reuters — 10 operation(s) for collections.
  name: Thomson Reuters Collections API
  slug: thomson-reuters-collections-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Comments API API from Thomson Reuters — 2 operation(s) for comments api.
  name: Thomson Reuters Comments API
  slug: thomson-reuters-comments-api-api
- baseURL: https://api-emea.onesourcetax.com/einvoicing/document/v1
  baseurl_source: declared
  description: Get Companies.
  name: Thomson Reuters Company API
  slug: thomson-reuters-company-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Compare Controller
  name: Thomson Reuters Compare Controller API
  slug: thomson-reuters-compare-controller-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrives line-items details from the Tax Provision & Trial Balance reports for component-detail and State Tax Provision for component-detail-state.
  name: Thomson Reuters Componentdetail API
  slug: thomson-reuters-componentdetail-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Configuration API from Thomson Reuters — 3 operation(s) for configuration.
  name: Thomson Reuters Configuration API
  slug: thomson-reuters-configuration-api
- baseURL: https://api.thomsonreuters.com/openbanking/v1
  baseurl_source: declared
  description: The consent the client gives to share their information.
  name: Thomson Reuters Consent API
  slug: thomson-reuters-consent-api
- baseURL: https://api-apac.onesourcetax.com/trusts/v1/imports
  baseurl_source: declared
  description: The CorporateTaxImports API from Thomson Reuters — 6 operation(s) for corporatetaximports.
  name: Thomson Reuters Corporate Tax Imports API
  slug: thomson-reuters-corporatetaximports-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/administration
  baseurl_source: declared
  description: The Cost Center API from Thomson Reuters — 1 operation(s) for cost center.
  name: Thomson Reuters Cost Center API
  slug: thomson-reuters-cost-center-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The Countries API from Thomson Reuters — 8 operation(s) for countries.
  name: Thomson Reuters Countries API
  slug: thomson-reuters-countries-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Currencies API from Thomson Reuters — 2 operation(s) for currencies.
  name: Thomson Reuters Currencies API
  slug: thomson-reuters-currencies-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Currencies-📦 Version 1 Endpoints API from Thomson Reuters — 1 operation(s) for currencies-📦 version 1 endpoints.
  name: Thomson Reuters Currencies-📦 Version 1 Endpoints API
  slug: thomson-reuters-currencies-version-1-endpoints-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Currencies-📦 Version 2 Endpoints API from Thomson Reuters — 1 operation(s) for currencies-📦 version 2 endpoints.
  name: Thomson Reuters Currencies-📦 Version 2 Endpoints API
  slug: thomson-reuters-currencies-version-2-endpoints-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrieve all currency links within a specified financial period.
  name: Thomson Reuters Currency Links API
  slug: thomson-reuters-currency-links-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Custom fields API from Thomson Reuters — 1 operation(s) for custom fields.
  name: Thomson Reuters Custom fields API
  slug: thomson-reuters-custom-fields-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Data Fields can be used to create Master Trial Balance that reconcile Trial Balance. ONESOURCE General Ledger Manager Data Fields APIs provides access to the pre-defined Data Fields for Standard Trial
  name: Thomson Reuters Data Fields API
  slug: thomson-reuters-data-fields-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Manage ingests, upload files, extensions, extract data from integrations. ONESOURCE General Ledger Manager Data Queue APIs enables the users to upload the trial balance data from multiple disparate so
  name: Thomson Reuters Data Queue API
  slug: thomson-reuters-data-queue-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Debt Waiver Benefit API from Thomson Reuters — 1 operation(s) for debt waiver benefit.
  name: Thomson Reuters Debt Waiver Benefit API
  slug: thomson-reuters-debt-waiver-benefit-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Provides APIs to retrieve various types of deferred balances data including Pretax, Federal, State, FBOS, and Tax-Effected balances.
  name: Thomson Reuters Deferredbalances API
  slug: thomson-reuters-deferredbalances-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrieves temporary difference beginning and ending balances.
  name: Thomson Reuters Deferredworkpaper API
  slug: thomson-reuters-deferredworkpaper-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: The Deliverable API from Thomson Reuters — 4 operation(s) for deliverable.
  name: Thomson Reuters Deliverable API
  slug: thomson-reuters-deliverable-api
- baseURL: https://api-emea.onesourcetax.com/einvoicing/document/v1
  baseurl_source: declared
  description: Perform an action on a document.
  name: Thomson Reuters Document API
  slug: thomson-reuters-document-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Document Controller
  name: Thomson Reuters Document Controller API
  slug: thomson-reuters-document-controller-api
- baseURL: https://api-emea.onesourcetax.com/einvoicing/document/v1
  baseurl_source: declared
  description: Operations on document payloads
  name: Thomson Reuters Document payloads API
  slug: thomson-reuters-document-payloads-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Document Resource APIs API from Thomson Reuters — 30 operation(s) for document resource apis.
  name: Thomson Reuters Document Resource APIs API
  slug: thomson-reuters-document-resource-apis-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/documents-api/v1
  baseurl_source: declared
  description: Use the Documents endpoint to get and manage document details.
  name: Thomson Reuters Documents API
  slug: thomson-reuters-documents-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Domains API from Thomson Reuters — 3 operation(s) for domains.
  name: Thomson Reuters Domains API
  slug: thomson-reuters-domains-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Domains-📦 Version 1 Endpoints API from Thomson Reuters — 1 operation(s) for domains-📦 version 1 endpoints.
  name: Thomson Reuters Domains-📦 Version 1 Endpoints API
  slug: thomson-reuters-domains-version-1-endpoints-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Domains-📦 Version 2 Endpoints API from Thomson Reuters — 2 operation(s) for domains-📦 version 2 endpoints.
  name: Thomson Reuters Domains-📦 Version 2 Endpoints API
  slug: thomson-reuters-domains-version-2-endpoints-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/documents-api/v1
  baseurl_source: declared
  description: Use the DownloadLinks endpoint to get a link to download an existing document.
  name: Thomson Reuters Download Links API
  slug: thomson-reuters-downloadlinks-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: Drawer
  name: Thomson Reuters Drawer API
  slug: thomson-reuters-drawer-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Due Dates API from Thomson Reuters — 4 operation(s) for due dates.
  name: Thomson Reuters Due Dates API
  slug: thomson-reuters-due-dates-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The E-file Document Lifecycle API from Thomson Reuters — 5 operation(s) for e-file document lifecycle.
  name: Thomson Reuters E-file Document Lifecycle API
  slug: thomson-reuters-e-file-document-lifecycle-api
- baseURL: https://api.thomsonreuters.com/gosystem/e-files
  baseurl_source: declared
  description: The E-file Document Lifecycle V1 API from Thomson Reuters — 3 operation(s) for e-file document lifecycle v1.
  name: Thomson Reuters E-file Document Lifecycle V1 API
  slug: thomson-reuters-e-file-document-lifecycle-v1-api
- baseURL: https://api.thomsonreuters.com/gosystem/e-files
  baseurl_source: declared
  description: The E-file Document Lifecycle V2 API from Thomson Reuters — 2 operation(s) for e-file document lifecycle v2.
  name: Thomson Reuters E-file Document Lifecycle V2 API
  slug: thomson-reuters-e-file-document-lifecycle-v2-api
- baseURL: https://api.thomsonreuters.com/gosystem/e-files
  baseurl_source: declared
  description: The E-file Document V1 API from Thomson Reuters — 5 operation(s) for e-file document v1.
  name: Thomson Reuters E-file Document V1 API
  slug: thomson-reuters-e-file-document-v1-api
- baseURL: https://api.thomsonreuters.com/gosystem/e-files
  baseurl_source: declared
  description: The E-file Document V2 API from Thomson Reuters — 1 operation(s) for e-file document v2.
  name: Thomson Reuters E-file Document V2 API
  slug: thomson-reuters-e-file-document-v2-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The E-file Documents API from Thomson Reuters — 2 operation(s) for e-file documents.
  name: Thomson Reuters E-file Documents API
  slug: thomson-reuters-e-file-documents-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The E-file IRS Lifecycle API from Thomson Reuters — 6 operation(s) for e-file irs lifecycle.
  name: Thomson Reuters E-file IRS Lifecycle API
  slug: thomson-reuters-e-file-irs-lifecycle-api
- baseURL: https://api.thomsonreuters.com/gosystem/e-files
  baseurl_source: declared
  description: The E-file IRS Lifecycle V1 API from Thomson Reuters — 5 operation(s) for e-file irs lifecycle v1.
  name: Thomson Reuters E-file IRS Lifecycle V1 API
  slug: thomson-reuters-e-file-irs-lifecycle-v1-api
- baseURL: https://api.thomsonreuters.com/gosystem/e-files
  baseurl_source: declared
  description: The E-file IRS Lifecycle V2 API from Thomson Reuters — 3 operation(s) for e-file irs lifecycle v2.
  name: Thomson Reuters E-file IRS Lifecycle V2 API
  slug: thomson-reuters-e-file-irs-lifecycle-v2-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The E-file Reference API from Thomson Reuters — 2 operation(s) for e-file reference.
  name: Thomson Reuters E-file Reference API
  slug: thomson-reuters-e-file-reference-api
- baseURL: https://api.thomsonreuters.com/gosystem/e-files
  baseurl_source: declared
  description: The E-file Reference V1 API from Thomson Reuters — 1 operation(s) for e-file reference v1.
  name: Thomson Reuters E-file Reference V1 API
  slug: thomson-reuters-e-file-reference-v1-api
- baseURL: https://api.thomsonreuters.com/gosystem/e-files
  baseurl_source: declared
  description: The E-file Reference V2 API from Thomson Reuters — 1 operation(s) for e-file reference v2.
  name: Thomson Reuters E-file Reference V2 API
  slug: thomson-reuters-e-file-reference-v2-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Effective Rate – for every entity, group, and jurisdiction selected, this report provides an effective tax rate derived by multiplying the apportionment percentage and tax rate. You can select which t
  name: Thomson Reuters Effective Rate Data API
  slug: thomson-reuters-effective-rate-data-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The EffectiveTaxRate API from Thomson Reuters — 1 operation(s) for effectivetaxrate.
  name: Thomson Reuters Effective Tax Rate API
  slug: thomson-reuters-effectivetaxrate-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Efile Attachments API from Thomson Reuters — 5 operation(s) for efile attachments.
  name: Thomson Reuters Efile Attachments API
  slug: thomson-reuters-efile-attachments-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance
  baseurl_source: declared
  description: The Efiling API from Thomson Reuters — 3 operation(s) for efiling.
  name: Thomson Reuters Efiling API
  slug: thomson-reuters-efiling-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/employee
  baseurl_source: declared
  description: The Employee API from Thomson Reuters — 4 operation(s) for employee.
  name: Thomson Reuters Employee API
  slug: thomson-reuters-employee-api
- baseURL: https://api.thomsonreuters.com/us/engagementmanager
  baseurl_source: declared
  description: Get list of engagements
  name: Thomson Reuters Engagements API
  slug: thomson-reuters-engagements-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Entertainment Benefit API from Thomson Reuters — 1 operation(s) for entertainment benefit.
  name: Thomson Reuters Entertainment Benefit API
  slug: thomson-reuters-entertainment-benefit-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Entities API from Thomson Reuters — 11 operation(s) for entities.
  name: Thomson Reuters Entities API
  slug: thomson-reuters-entities-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Entity Rollup API from Thomson Reuters — 5 operation(s) for entity rollup.
  name: Thomson Reuters Entity Rollup API
  slug: thomson-reuters-entity-rollup-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2
  baseurl_source: declared
  description: The EntityHierarchy API from Thomson Reuters — 1 operation(s) for entityhierarchy.
  name: Thomson Reuters Entity Hierarchy API
  slug: thomson-reuters-entityhierarchy-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2
  baseurl_source: declared
  description: The EntityMappings API from Thomson Reuters — 2 operation(s) for entitymappings.
  name: Thomson Reuters Entity Mappings API
  slug: thomson-reuters-entitymappings-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/matters-api/v1
  baseurl_source: declared
  description: Use the Events API to retrive events of a matter.
  name: Thomson Reuters Events API
  slug: thomson-reuters-events-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Events APIs API from Thomson Reuters — 5 operation(s) for events apis.
  name: Thomson Reuters Events APIs API
  slug: thomson-reuters-events-apis-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Operations for querying everywhere data
  name: Thomson Reuters Everywhere Data API
  slug: thomson-reuters-everywhere-data-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Exceptiondomains API from Thomson Reuters — 2 operation(s) for exceptiondomains.
  name: Thomson Reuters Exceptiondomains API
  slug: thomson-reuters-exceptiondomains-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Exchange Rate Charts (2024+) API from Thomson Reuters — 10 operation(s) for exchange rate charts (2024+).
  name: Thomson Reuters Exchange Rate Charts (2024+) API
  slug: thomson-reuters-exchange-rate-charts-2024-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2
  baseurl_source: declared
  description: The ExchangeRateMappings API from Thomson Reuters — 2 operation(s) for exchangeratemappings.
  name: Thomson Reuters Exchange Rate Mappings API
  slug: thomson-reuters-exchangeratemappings-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2
  baseurl_source: declared
  description: The ExchangeRateSources API from Thomson Reuters — 2 operation(s) for exchangeratesources.
  name: Thomson Reuters Exchange Rate Sources API
  slug: thomson-reuters-exchangeratesources-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Expense Benefit API from Thomson Reuters — 1 operation(s) for expense benefit.
  name: Thomson Reuters Expense Benefit API
  slug: thomson-reuters-expense-benefit-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The External API from Thomson Reuters — 2 operation(s) for external.
  name: Thomson Reuters External API
  slug: thomson-reuters-external-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The external-licensing-api API from Thomson Reuters — 3 operation(s) for external-licensing-api.
  name: Thomson Reuters External Licensing API
  slug: thomson-reuters-external-licensing-api-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Extractions API from Thomson Reuters — 2 operation(s) for extractions.
  name: Thomson Reuters Extractions API
  slug: thomson-reuters-extractions-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Favourites API API from Thomson Reuters — 1 operation(s) for favourites api.
  name: Thomson Reuters Favourites API
  slug: thomson-reuters-favourites-api-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The FCOA Cross Reference API from Thomson Reuters — 3 operation(s) for fcoa cross reference.
  name: Thomson Reuters FCOA Cross Reference API
  slug: thomson-reuters-fcoa-cross-reference-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Federal Chart of Accounts (FCOA) API from Thomson Reuters — 6 operation(s) for federal chart of accounts (fcoa).
  name: Thomson Reuters Federal Chart of Accounts (FCOA) API
  slug: thomson-reuters-federal-chart-of-accounts-fcoa-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Federal Chart of Adjustments API from Thomson Reuters — 5 operation(s) for federal chart of adjustments.
  name: Thomson Reuters Federal Chart of Adjustments API
  slug: thomson-reuters-federal-chart-of-adjustments-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Fields API from Thomson Reuters — 1 operation(s) for fields.
  name: Thomson Reuters Fields API
  slug: thomson-reuters-fields-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Files API from Thomson Reuters — 4 operation(s) for files.
  name: Thomson Reuters Files API
  slug: thomson-reuters-files-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: The Filing API from Thomson Reuters — 1 operation(s) for filing.
  name: Thomson Reuters Filing API
  slug: thomson-reuters-filing-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Financial Hierarchy Service API from Thomson Reuters — 4 operation(s) for financial hierarchy service.
  name: Thomson Reuters Financial Hierarchy Service API
  slug: thomson-reuters-financial-hierarchy-service-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: The FirmFlow API from Thomson Reuters — 3 operation(s) for firmflow.
  name: Thomson Reuters Firm Flow API
  slug: thomson-reuters-firmflow-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: FirmFlowReports
  name: Thomson Reuters Firm Flow Reports API
  slug: thomson-reuters-firmflowreports-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The FiscalCalendar API from Thomson Reuters — 2 operation(s) for fiscalcalendar.
  name: Thomson Reuters Fiscal Calendar API
  slug: thomson-reuters-fiscalcalendar-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/documents-api/v1
  baseurl_source: declared
  description: Use the Folders endpoint to get information about folders that are used to organize documents.
  name: Thomson Reuters Folders API
  slug: thomson-reuters-folders-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Operations related to retrieving document status
  name: Thomson Reuters Get Document Status API
  slug: thomson-reuters-get-document-status-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Get Locator and Binder ID API from Thomson Reuters — 1 operation(s) for get locator and binder id.
  name: Thomson Reuters Get Locator and Binder ID API
  slug: thomson-reuters-get-locator-and-binder-id-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Get Template API from Thomson Reuters — 1 operation(s) for get template.
  name: Thomson Reuters Get Template API
  slug: thomson-reuters-get-template-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The group-controller API from Thomson Reuters — 1 operation(s) for group-controller.
  name: Thomson Reuters Group Controller API
  slug: thomson-reuters-group-controller-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Groups Management API from Thomson Reuters — 1 operation(s) for groups management.
  name: Thomson Reuters Groups Management API
  slug: thomson-reuters-groups-management-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Health Check Controller
  name: Thomson Reuters Health Check Controller API
  slug: thomson-reuters-health-check-controller-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Housing Benefit API from Thomson Reuters — 1 operation(s) for housing benefit.
  name: Thomson Reuters Housing Benefit API
  slug: thomson-reuters-housing-benefit-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Housing Detail API from Thomson Reuters — 1 operation(s) for housing detail.
  name: Thomson Reuters Housing Detail API
  slug: thomson-reuters-housing-detail-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Img API from Thomson Reuters — 1 operation(s) for img.
  name: Thomson Reuters Img API
  slug: thomson-reuters-img-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: Index
  name: Thomson Reuters Index API
  slug: thomson-reuters-index-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2/imports
  baseurl_source: declared
  description: The IndirectTaxImports API from Thomson Reuters — 5 operation(s) for indirecttaximports.
  name: Thomson Reuters Indirect Tax Imports API
  slug: thomson-reuters-indirecttaximports-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Ingest Extension Service API from Thomson Reuters — 6 operation(s) for ingest extension service.
  name: Thomson Reuters Ingest Extension Service API
  slug: thomson-reuters-ingest-extension-service-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Ingestions API from Thomson Reuters — 2 operation(s) for ingestions.
  name: Thomson Reuters Ingestions API
  slug: thomson-reuters-ingestions-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Instances API from Thomson Reuters — 1 operation(s) for instances.
  name: Thomson Reuters Instances API
  slug: thomson-reuters-instances-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Integrations API from Thomson Reuters — 2 operation(s) for integrations.
  name: Thomson Reuters Integrations API
  slug: thomson-reuters-integrations-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The International 5471 Schedule C (2018+) API from Thomson Reuters — 2 operation(s) for international 5471 schedule c (2018+).
  name: Thomson Reuters International 5471 Schedule C (2018+) API
  slug: thomson-reuters-international-5471-schedule-c-2018-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The International 5471 Schedule M (2018+) API from Thomson Reuters — 2 operation(s) for international 5471 schedule m (2018+).
  name: Thomson Reuters International 5471 Schedule M (2018+) API
  slug: thomson-reuters-international-5471-schedule-m-2018-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The International Chart of Accounts Cross Reference (2018+) API from Thomson Reuters — 2 operation(s) for international chart of accounts cross reference (2018+).
  name: Thomson Reuters International Chart of Accounts Cross Reference (2018+) API
  slug: thomson-reuters-international-chart-of-accounts-cross-reference-2018-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The International Sourcing Charts (2018+) API from Thomson Reuters — 6 operation(s) for international sourcing charts (2018+).
  name: Thomson Reuters International Sourcing Charts (2018+) API
  slug: thomson-reuters-international-sourcing-charts-2018-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The International Summary Chart (2018+) API from Thomson Reuters — 6 operation(s) for international summary chart (2018+).
  name: Thomson Reuters International Summary Chart (2018+) API
  slug: thomson-reuters-international-summary-chart-2018-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The InvoiceAllocations API from Thomson Reuters — 4 operation(s) for invoiceallocations.
  name: Thomson Reuters Invoice Allocations API
  slug: thomson-reuters-invoiceallocations-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The InvoiceLines API from Thomson Reuters — 5 operation(s) for invoicelines.
  name: Thomson Reuters Invoice Lines API
  slug: thomson-reuters-invoicelines-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The InvoiceReductions API from Thomson Reuters — 5 operation(s) for invoicereductions.
  name: Thomson Reuters Invoice Reductions API
  slug: thomson-reuters-invoicereductions-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/ap-exchange-api/v1
  baseurl_source: declared
  description: Use the Invoices AP Exchange API to view available for payment invoices, its files and spreadsheets and update payment information.
  name: Thomson Reuters Invoices API
  slug: thomson-reuters-invoices-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The InvoiceTaxes API from Thomson Reuters — 5 operation(s) for invoicetaxes.
  name: Thomson Reuters Invoice Taxes API
  slug: thomson-reuters-invoicetaxes-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The ISheet Admin API API from Thomson Reuters — 28 operation(s) for isheet admin api.
  name: Thomson Reuters ISheet Admin API
  slug: thomson-reuters-isheet-admin-api-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The ISheet API API from Thomson Reuters — 11 operation(s) for isheet api.
  name: Thomson Reuters ISheet API
  slug: thomson-reuters-isheet-api-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The ISheet Module API from Thomson Reuters — 15 operation(s) for isheet module.
  name: Thomson Reuters ISheet Module API
  slug: thomson-reuters-isheet-module-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The ISheet System Admin API from Thomson Reuters — 1 operation(s) for isheet system admin.
  name: Thomson Reuters ISheet System Admin API
  slug: thomson-reuters-isheet-system-admin-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Documentation for jobs. ONESOURCE General Ledger Manager Jobs APIs enables the users to stage and process the trial balance.
  name: Thomson Reuters Job Service API
  slug: thomson-reuters-job-service-api
- baseURL: https://api.thomsonreuters.com/us/engagementmanager
  baseurl_source: declared
  description: Get/Add/Edit/Delete Journal Entries
  name: Thomson Reuters Journal Entry API
  slug: thomson-reuters-journal-entry-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Jurisdictions API from Thomson Reuters — 2 operation(s) for jurisdictions.
  name: Thomson Reuters Jurisdictions API
  slug: thomson-reuters-jurisdictions-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Jurisdictions-📦 Version 1 Endpoints API from Thomson Reuters — 1 operation(s) for jurisdictions-📦 version 1 endpoints.
  name: Thomson Reuters Jurisdictions-📦 Version 1 Endpoints API
  slug: thomson-reuters-jurisdictions-version-1-endpoints-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Jurisdictions-📦 Version 2 Endpoints API from Thomson Reuters — 2 operation(s) for jurisdictions-📦 version 2 endpoints.
  name: Thomson Reuters Jurisdictions-📦 Version 2 Endpoints API
  slug: thomson-reuters-jurisdictions-version-2-endpoints-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Lafha Benefit API from Thomson Reuters — 1 operation(s) for lafha benefit.
  name: Thomson Reuters Lafha Benefit API
  slug: thomson-reuters-lafha-benefit-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: The LargeDocument API from Thomson Reuters — 10 operation(s) for largedocument.
  name: Thomson Reuters Large Document API
  slug: thomson-reuters-largedocument-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The LeadCompanyPersons API from Thomson Reuters — 3 operation(s) for leadcompanypersons.
  name: Thomson Reuters Lead Company Persons API
  slug: thomson-reuters-leadcompanypersons-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The LeadOutsideCounsels API from Thomson Reuters — 3 operation(s) for leadoutsidecounsels.
  name: Thomson Reuters Lead Outside Counsels API
  slug: thomson-reuters-leadoutsidecounsels-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/reports
  baseurl_source: declared
  description: The Letter Generation API from Thomson Reuters — 3 operation(s) for letter generation.
  name: Thomson Reuters Letter Generation API
  slug: thomson-reuters-letter-generation-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Library Controller
  name: Thomson Reuters Library Controller API
  slug: thomson-reuters-library-controller-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The License API from Thomson Reuters — 1 operation(s) for license.
  name: Thomson Reuters License API
  slug: thomson-reuters-license-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Likes API API from Thomson Reuters — 1 operation(s) for likes api.
  name: Thomson Reuters Likes API
  slug: thomson-reuters-likes-api-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Load Statuses API from Thomson Reuters — 1 operation(s) for load statuses.
  name: Thomson Reuters Load Statuses API
  slug: thomson-reuters-load-statuses-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Loan Benefit API from Thomson Reuters — 1 operation(s) for loan benefit.
  name: Thomson Reuters Loan Benefit API
  slug: thomson-reuters-loan-benefit-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Location Service API from Thomson Reuters — 1 operation(s) for location service.
  name: Thomson Reuters Location Service API
  slug: thomson-reuters-location-service-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Locator API from Thomson Reuters — 5 operation(s) for locator.
  name: Thomson Reuters Locator API
  slug: thomson-reuters-locator-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: LookupLists
  name: Thomson Reuters Lookup Lists API
  slug: thomson-reuters-lookuplists-api
- baseURL: https://api-apac.onesourcetax.com/trusts/v1/tax-account-mappings
  baseurl_source: declared
  description: The Mappings API from Thomson Reuters — 2 operation(s) for mappings.
  name: Thomson Reuters Mappings API
  slug: thomson-reuters-mappings-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: An aggregated set of one or more Trial Balances which are based on the same Data Fields. ONESOURCE General Ledger Manager Master Trial Balance APIs enables the users to group the trial balance data th
  name: Thomson Reuters Master Trial Balance API
  slug: thomson-reuters-master-trial-balance-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterAllocations API from Thomson Reuters — 3 operation(s) for matterallocations.
  name: Thomson Reuters Matter Allocations API
  slug: thomson-reuters-matterallocations-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCreators API from Thomson Reuters — 3 operation(s) for mattercreators.
  name: Thomson Reuters Matter Creators API
  slug: thomson-reuters-mattercreators-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCustomCurrencyFields API from Thomson Reuters — 3 operation(s) for mattercustomcurrencyfields.
  name: Thomson Reuters Matter Custom Currency Fields API
  slug: thomson-reuters-mattercustomcurrencyfields-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCustomDateFields API from Thomson Reuters — 3 operation(s) for mattercustomdatefields.
  name: Thomson Reuters Matter Custom Date Fields API
  slug: thomson-reuters-mattercustomdatefields-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCustomDropdownFields API from Thomson Reuters — 3 operation(s) for mattercustomdropdownfields.
  name: Thomson Reuters Matter Custom Dropdown Fields API
  slug: thomson-reuters-mattercustomdropdownfields-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCustomNumberFields API from Thomson Reuters — 3 operation(s) for mattercustomnumberfields.
  name: Thomson Reuters Matter Custom Number Fields API
  slug: thomson-reuters-mattercustomnumberfields-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCustomRichTextAreaFields API from Thomson Reuters — 3 operation(s) for mattercustomrichtextareafields.
  name: Thomson Reuters Matter Custom Rich Text Area Fields API
  slug: thomson-reuters-mattercustomrichtextareafields-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCustomTextAreaFields API from Thomson Reuters — 3 operation(s) for mattercustomtextareafields.
  name: Thomson Reuters Matter Custom Text Area Fields API
  slug: thomson-reuters-mattercustomtextareafields-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCustomTextFields API from Thomson Reuters — 3 operation(s) for mattercustomtextfields.
  name: Thomson Reuters Matter Custom Text Fields API
  slug: thomson-reuters-mattercustomtextfields-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterCustomTreeNodeFields API from Thomson Reuters — 3 operation(s) for mattercustomtreenodefields.
  name: Thomson Reuters Matter Custom Tree Node Fields API
  slug: thomson-reuters-mattercustomtreenodefields-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/documents-api/v1
  baseurl_source: declared
  description: Use the MatterDocuments endpoint to get a list of documents associated with a matter.
  name: Thomson Reuters Matter Documents API
  slug: thomson-reuters-matterdocuments-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterFirms API from Thomson Reuters — 4 operation(s) for matterfirms.
  name: Thomson Reuters Matter Firms API
  slug: thomson-reuters-matterfirms-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/matters-api/v1
  baseurl_source: declared
  description: Use the MatterIntakes API to upload matterIntakes into Tracker.
  name: Thomson Reuters Matter Intakes API
  slug: thomson-reuters-matterintakes-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterParticipants API from Thomson Reuters — 4 operation(s) for matterparticipants.
  name: Thomson Reuters Matter Participants API
  slug: thomson-reuters-matterparticipants-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The MatterTypes API from Thomson Reuters — 3 operation(s) for mattertypes.
  name: Thomson Reuters Matter Types API
  slug: thomson-reuters-mattertypes-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Media Metadata Controller
  name: Thomson Reuters Media Metadata Controller API
  slug: thomson-reuters-media-metadata-controller-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Metadata API from Thomson Reuters — 9 operation(s) for metadata.
  name: Thomson Reuters Metadata API
  slug: thomson-reuters-metadata-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Metadata Controller
  name: Thomson Reuters Metadata Controller API
  slug: thomson-reuters-metadata-controller-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: MultiDocExport
  name: Thomson Reuters Multi Doc Export API
  slug: thomson-reuters-multidocexport-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Navigation API from Thomson Reuters — 3 operation(s) for navigation.
  name: Thomson Reuters Navigation API
  slug: thomson-reuters-navigation-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The No2CompanyPersons API from Thomson Reuters — 3 operation(s) for no2companypersons.
  name: Thomson Reuters No2 Company Persons API
  slug: thomson-reuters-no2companypersons-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: The Note API from Thomson Reuters — 1 operation(s) for note.
  name: Thomson Reuters Note API
  slug: thomson-reuters-note-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Numerator Denominator – provides a high-level view of numerators, denominators, and apportionment percentages for every entity, group, and jurisdiction selected. Can be set to filter out entities with
  name: Thomson Reuters Numerator Denominator Data API
  slug: thomson-reuters-numerator-denominator-data-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Obligations API from Thomson Reuters — 2 operation(s) for obligations.
  name: Thomson Reuters Obligations API
  slug: thomson-reuters-obligations-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The OData Service (adheres to OData 4.0) API from Thomson Reuters — 18 operation(s) for odata service (adheres to odata 4.0).
  name: Thomson Reuters OData Service  (adheres to OData 4.0) API
  slug: thomson-reuters-odata-service-adheres-to-odata-4-0-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/companies-api/v1
  baseurl_source: declared
  description: Use the Offices endpoint to get company offices details.
  name: Thomson Reuters Offices API
  slug: thomson-reuters-offices-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Provides data refresh capabilities for the ONESOURCE™ Tax Provision Data Query-Reporting tile and OData, allowing users to access the most current data without having to wait for scheduled updates.
  name: Thomson Reuters On-Demand Data Refersh API
  slug: thomson-reuters-on-demand-data-refersh-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Options and Overrides API from Thomson Reuters — 1 operation(s) for options and overrides.
  name: Thomson Reuters Options and Overrides API
  slug: thomson-reuters-options-and-overrides-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Orgaddress API from Thomson Reuters — 2 operation(s) for orgaddress.
  name: Thomson Reuters Orgaddress API
  slug: thomson-reuters-orgaddress-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Organisation API from Thomson Reuters — 4 operation(s) for organisation.
  name: Thomson Reuters Organisation API
  slug: thomson-reuters-organisation-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/administration
  baseurl_source: declared
  description: The Organization API from Thomson Reuters — 1 operation(s) for organization.
  name: Thomson Reuters Organization API
  slug: thomson-reuters-organization-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/companies-api/v1
  baseurl_source: declared
  description: Use the organizational-units endpoint to get and manage organizational units details.
  name: Thomson Reuters Organizational Units API
  slug: thomson-reuters-organizationalunits-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrieves taxes payable for units configured for datsets within an instance.
  name: Thomson Reuters Payable API
  slug: thomson-reuters-payable-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/reports
  baseurl_source: declared
  description: The Payroll Tax Figure API from Thomson Reuters — 2 operation(s) for payroll tax figure.
  name: Thomson Reuters Payroll Tax Figure API
  slug: thomson-reuters-payroll-tax-figure-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/administration
  baseurl_source: declared
  description: The Period API from Thomson Reuters — 1 operation(s) for period.
  name: Thomson Reuters Period API
  slug: thomson-reuters-period-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Platform API from Thomson Reuters — 2 operation(s) for platform.
  name: Thomson Reuters Platform API
  slug: thomson-reuters-platform-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/firms-api/v2
  baseurl_source: declared
  description: Manage firm matter portfolios to track combined financial spending on all the matters assigned to a portfolio.
  name: Thomson Reuters Portfolios API
  slug: thomson-reuters-portfolios-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/companies-api/v1
  baseurl_source: declared
  description: Use the practice-groups endpoint to get and manage practice groups details.
  name: Thomson Reuters Practice Groups API
  slug: thomson-reuters-practicegroups-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: API for predicting financial hierarchy
  name: Thomson Reuters Predictive Financial Mapping API
  slug: thomson-reuters-predictive-financial-mapping-api-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Private Message API from Thomson Reuters — 5 operation(s) for private message.
  name: Thomson Reuters Private Message API
  slug: thomson-reuters-private-message-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Documentation for Processing Instructions Service. ONESOURCE General Ledger Manager Processing Instructions APIs enables the definition of the expected data format and related information that is used
  name: Thomson Reuters Processing Instructions API
  slug: thomson-reuters-processing-instructions-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Proforma API from Thomson Reuters — 2 operation(s) for proforma.
  name: Thomson Reuters Proforma API
  slug: thomson-reuters-proforma-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Property Benefit API from Thomson Reuters — 1 operation(s) for property benefit.
  name: Thomson Reuters Property Benefit API
  slug: thomson-reuters-property-benefit-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Query Comparisons Service API from Thomson Reuters — 4 operation(s) for query comparisons service.
  name: Thomson Reuters Query Comparisons Service API
  slug: thomson-reuters-query-comparisons-service-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Query Odata Service API from Thomson Reuters — 3 operation(s) for query odata service.
  name: Thomson Reuters Query Odata Service API
  slug: thomson-reuters-query-odata-service-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Query Service API from Thomson Reuters — 15 operation(s) for query service.
  name: Thomson Reuters Query Service API
  slug: thomson-reuters-query-service-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrieves questions and answers associated with various questionnaires configured for datasets within a specific instance.
  name: Thomson Reuters Questionnaire API
  slug: thomson-reuters-questionnaire-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Recipients API from Thomson Reuters — 2 operation(s) for recipients.
  name: Thomson Reuters Recipients API
  slug: thomson-reuters-recipients-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Reconciliation - shows state-wide totals alongside Per Return amounts, helping users identify and reconcile variances.
  name: Thomson Reuters Reconciliation Data API
  slug: thomson-reuters-reconciliation-data-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Recordsets API from Thomson Reuters — 3 operation(s) for recordsets.
  name: Thomson Reuters Recordsets API
  slug: thomson-reuters-recordsets-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Related Documents Controller
  name: Thomson Reuters Related Documents Controller API
  slug: thomson-reuters-related-documents-controller-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The report-controller API from Thomson Reuters — 2 operation(s) for report-controller.
  name: Thomson Reuters Report Controller API
  slug: thomson-reuters-report-controller-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/reports-api/v2
  baseurl_source: declared
  description: The Report definitions API from Thomson Reuters — 2 operation(s) for report definitions.
  name: Thomson Reuters Report definitions API
  slug: thomson-reuters-report-definitions-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/reports-api/v2
  baseurl_source: declared
  description: The Report filter definitions API from Thomson Reuters — 1 operation(s) for report filter definitions.
  name: Thomson Reuters Report filter definitions API
  slug: thomson-reuters-report-filter-definitions-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/administration
  baseurl_source: declared
  description: The Reporting Entity API from Thomson Reuters — 2 operation(s) for reporting entity.
  name: Thomson Reuters Reporting Entity API
  slug: thomson-reuters-reporting-entity-api
- baseURL: https://api.thomsonreuters.com/openbanking/v1
  baseurl_source: declared
  description: Seeks to validate/get information about the client.
  name: Thomson Reuters Requester API
  slug: thomson-reuters-requester-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Research Controller
  name: Thomson Reuters Research Controller API
  slug: thomson-reuters-research-controller-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Residual Benefit API from Thomson Reuters — 1 operation(s) for residual benefit.
  name: Thomson Reuters Residual Benefit API
  slug: thomson-reuters-residual-benefit-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/reports
  baseurl_source: declared
  description: The RFBA Figure API from Thomson Reuters — 2 operation(s) for rfba figure.
  name: Thomson Reuters RFBA Figure API
  slug: thomson-reuters-rfba-figure-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrieves rollups defining how the data should be tiered.
  name: Thomson Reuters Rollups API
  slug: thomson-reuters-rollups-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: The Route API from Thomson Reuters — 1 operation(s) for route.
  name: Thomson Reuters Route API
  slug: thomson-reuters-route-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Sales API from Thomson Reuters — 3 operation(s) for sales.
  name: Thomson Reuters Sales API
  slug: thomson-reuters-sales-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Schedule M3 Line Code API from Thomson Reuters — 1 operation(s) for schedule m3 line code.
  name: Thomson Reuters Schedule M3 Line Code API
  slug: thomson-reuters-schedule-m3-line-code-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Schedule M3 Line Mapping API from Thomson Reuters — 2 operation(s) for schedule m3 line mapping.
  name: Thomson Reuters Schedule M3 Line Mapping API
  slug: thomson-reuters-schedule-m3-line-mapping-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The ScheduleK1 API from Thomson Reuters — 4 operation(s) for schedulek1.
  name: Thomson Reuters Schedule K1 API
  slug: thomson-reuters-schedulek1-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Schematics API from Thomson Reuters — 4 operation(s) for schematics.
  name: Thomson Reuters Schematics API
  slug: thomson-reuters-schematics-api
- baseURL: https://api.thomsonreuters.com/checkpoint
  baseurl_source: declared
  description: Execute searches across the extensive collection of tax and accounting content offered by Checkpoint.
  name: Thomson Reuters Search API V1 API
  slug: thomson-reuters-search-api-v1-api
- baseURL: https://api.thomsonreuters.com/checkpoint
  baseurl_source: declared
  description: 'The Search API for Checkpoint Edge provides the most accurate and up-to-date guidance about the ever-changing tax law and accounting standards. The API is powered by AI and machine-learning tools, to '
  name: Thomson Reuters Search API V2 API
  slug: thomson-reuters-search-api-v2-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Search Controller
  name: Thomson Reuters Search Controller API
  slug: thomson-reuters-search-controller-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The Service Operations API from Thomson Reuters — 2 operation(s) for service operations.
  name: Thomson Reuters Service Operations API
  slug: thomson-reuters-service-operations-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Shipments API from Thomson Reuters — 2 operation(s) for shipments.
  name: Thomson Reuters Shipments API
  slug: thomson-reuters-shipments-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: 'Retrieves Sign-Off Status for user across three distinct views: Sign-Off, Unit and Status.'
  name: Thomson Reuters Sign Off Status API
  slug: thomson-reuters-signoffstatus-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Site Resource APIs API from Thomson Reuters — 30 operation(s) for site resource apis.
  name: Thomson Reuters Site Resource APIs API
  slug: thomson-reuters-site-resource-apis-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Sitecategories API from Thomson Reuters — 1 operation(s) for sitecategories.
  name: Thomson Reuters Sitecategories API
  slug: thomson-reuters-sitecategories-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Sitetemplates API from Thomson Reuters — 2 operation(s) for sitetemplates.
  name: Thomson Reuters Sitetemplates API
  slug: thomson-reuters-sitetemplates-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/administration
  baseurl_source: declared
  description: The Standard Category API from Thomson Reuters — 1 operation(s) for standard category.
  name: Thomson Reuters Standard Category API
  slug: thomson-reuters-standard-category-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The State AA Categories API from Thomson Reuters — 1 operation(s) for state aa categories.
  name: Thomson Reuters State AA Categories API
  slug: thomson-reuters-state-aa-categories-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The State AA Forms Cross Reference Charts API from Thomson Reuters — 4 operation(s) for state aa forms cross reference charts.
  name: Thomson Reuters State AA Forms Cross Reference Charts API
  slug: thomson-reuters-state-aa-forms-cross-reference-charts-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The State AA Jurisdictions API from Thomson Reuters — 2 operation(s) for state aa jurisdictions.
  name: Thomson Reuters State AA Jurisdictions API
  slug: thomson-reuters-state-aa-jurisdictions-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The State AA Logic Charts API from Thomson Reuters — 7 operation(s) for state aa logic charts.
  name: Thomson Reuters State AA Logic Charts API
  slug: thomson-reuters-state-aa-logic-charts-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: State Data - shows state data for the entities, jurisdictions, and groups selected.
  name: Thomson Reuters State Data API
  slug: thomson-reuters-state-data-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The State Ti Category Groups API from Thomson Reuters — 1 operation(s) for state ti category groups.
  name: Thomson Reuters State Ti Category Groups API
  slug: thomson-reuters-state-ti-category-groups-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The State Ti Forms Mapping Charts API from Thomson Reuters — 5 operation(s) for state ti forms mapping charts.
  name: Thomson Reuters State Ti Forms Mapping Charts API
  slug: thomson-reuters-state-ti-forms-mapping-charts-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The State Ti Jurisdictions API from Thomson Reuters — 1 operation(s) for state ti jurisdictions.
  name: Thomson Reuters State Ti Jurisdictions API
  slug: thomson-reuters-state-ti-jurisdictions-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrieves state tax provision broken out by states.
  name: Thomson Reuters State Provision API
  slug: thomson-reuters-stateprovision-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The States API from Thomson Reuters — 4 operation(s) for states.
  name: Thomson Reuters States API
  slug: thomson-reuters-states-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Statuses API from Thomson Reuters — 3 operation(s) for statuses.
  name: Thomson Reuters Statuses API
  slug: thomson-reuters-statuses-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrieves subconsolidations assigned within a specific instance.
  name: Thomson Reuters Subconsolidation API
  slug: thomson-reuters-subconsolidation-api
- baseURL: https://api-emea.onesourcetax.com/corporate-tax/v1/e-filing-manager
  baseurl_source: declared
  description: The Submissions API from Thomson Reuters — 7 operation(s) for submissions.
  name: Thomson Reuters Submissions API
  slug: thomson-reuters-submissions-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Operations related to submitting documents
  name: Thomson Reuters Submit Document API
  slug: thomson-reuters-submit-document-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The SubstantiveLaws API from Thomson Reuters — 3 operation(s) for substantivelaws.
  name: Thomson Reuters Substantive Laws API
  slug: thomson-reuters-substantivelaws-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Super lock API from Thomson Reuters — 2 operation(s) for super lock.
  name: Thomson Reuters Super lock API
  slug: thomson-reuters-super-lock-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Support API from Thomson Reuters — 1 operation(s) for support.
  name: Thomson Reuters Support API
  slug: thomson-reuters-support-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The system-controller API from Thomson Reuters — 2 operation(s) for system-controller.
  name: Thomson Reuters System Controller API
  slug: thomson-reuters-system-controller-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The System Groups API from Thomson Reuters — 6 operation(s) for system groups.
  name: Thomson Reuters System Groups API
  slug: thomson-reuters-system-groups-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The System Reports APIs API from Thomson Reuters — 1 operation(s) for system reports apis.
  name: Thomson Reuters System Reports APIs API
  slug: thomson-reuters-system-reports-apis-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The System Resource API from Thomson Reuters — 6 operation(s) for system resource.
  name: Thomson Reuters System Resource API
  slug: thomson-reuters-system-resource-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/matters-api/v1
  baseurl_source: declared
  description: The TaskCodeAlerts API from Thomson Reuters — 1 operation(s) for taskcodealerts.
  name: Thomson Reuters Task Code Alerts API
  slug: thomson-reuters-taskcodealerts-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Tasks API from Thomson Reuters — 1 operation(s) for tasks.
  name: Thomson Reuters Tasks API
  slug: thomson-reuters-tasks-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Tasks APIs API from Thomson Reuters — 9 operation(s) for tasks apis.
  name: Thomson Reuters Tasks APIs API
  slug: thomson-reuters-tasks-apis-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Tax Combination Code (TCC) Charts API from Thomson Reuters — 6 operation(s) for tax combination code (tcc) charts.
  name: Thomson Reuters Tax Combination Code (TCC) Charts API
  slug: thomson-reuters-tax-combination-code-tcc-charts-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Tax Documents(Print) API from Thomson Reuters — 4 operation(s) for tax documents(print).
  name: Thomson Reuters Tax Documents(Print) API
  slug: thomson-reuters-tax-documents-print-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: ⚠️ We recommend using V2 Print instead of V1 Print. V1 Print will be deprecated in a future release.
  name: Thomson Reuters Tax Documents V1 (Print) API
  slug: thomson-reuters-tax-documents-v1-print-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: ⚠️ We recommend using V2 Print instead of V1 Print. V1 Print will be deprecated in a future release.
  name: Thomson Reuters Tax Documents V2 (Print) API
  slug: thomson-reuters-tax-documents-v2-print-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Tax Returns API from Thomson Reuters — 2 operation(s) for tax returns.
  name: Thomson Reuters Tax Returns API
  slug: thomson-reuters-tax-returns-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Tax Returns (Import/Export) API from Thomson Reuters — 5 operation(s) for tax returns (import/export).
  name: Thomson Reuters Tax Returns (Import/Export) API
  slug: thomson-reuters-tax-returns-import-export-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Thomson Reuters Tax REST API
  name: Thomson Reuters Tax Service API
  slug: thomson-reuters-tax-service-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2
  baseurl_source: declared
  description: The TaxCodeMappings API from Thomson Reuters — 3 operation(s) for taxcodemappings.
  name: Thomson Reuters Tax Code Mappings API
  slug: thomson-reuters-taxcodemappings-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Retrieves provision calculations and includes supporting calculations.
  name: Thomson Reuters Tax Provision API
  slug: thomson-reuters-taxprovision-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The TaxReturn (beta) API from Thomson Reuters — 9 operation(s) for taxreturn (beta).
  name: Thomson Reuters TaxReturn (beta) API
  slug: thomson-reuters-taxreturn-beta-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The TaxReturn (V1) API from Thomson Reuters — 3 operation(s) for taxreturn (v1).
  name: Thomson Reuters TaxReturn (V1) API
  slug: thomson-reuters-taxreturn-v1-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The TBB Import API from Thomson Reuters — 1 operation(s) for tbb import.
  name: Thomson Reuters TBB Import API
  slug: thomson-reuters-tbb-import-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2
  baseurl_source: declared
  description: The TemplateFamilies API from Thomson Reuters — 2 operation(s) for templatefamilies.
  name: Thomson Reuters Template Families API
  slug: thomson-reuters-templatefamilies-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Templates API from Thomson Reuters — 4 operation(s) for templates.
  name: Thomson Reuters Templates API
  slug: thomson-reuters-templates-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Ten99 Controls API from Thomson Reuters — 1 operation(s) for ten99 controls.
  name: Thomson Reuters Ten99 Controls API
  slug: thomson-reuters-ten99-controls-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The TimekeeperClassifications API from Thomson Reuters — 3 operation(s) for timekeeperclassifications.
  name: Thomson Reuters Timekeeper Classifications API
  slug: thomson-reuters-timekeeperclassifications-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The TimekeeperRateSheets API from Thomson Reuters — 7 operation(s) for timekeeperratesheets.
  name: Thomson Reuters Timekeeper Rate Sheets API
  slug: thomson-reuters-timekeeperratesheets-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The Timekeepers API from Thomson Reuters — 7 operation(s) for timekeepers.
  name: Thomson Reuters Timekeepers API
  slug: thomson-reuters-timekeepers-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Toc Novus Controller
  name: Thomson Reuters Toc Novus Controller API
  slug: thomson-reuters-toc-novus-controller-api
- baseURL: https://api.thomsonreuters.com/us/engagementmanager
  baseurl_source: declared
  description: Get authorization for all api's
  name: Thomson Reuters Token API
  slug: thomson-reuters-token-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Topics API from Thomson Reuters — 8 operation(s) for topics.
  name: Thomson Reuters Topics API
  slug: thomson-reuters-topics-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Transactions API from Thomson Reuters — 3 operation(s) for transactions.
  name: Thomson Reuters Transactions API
  slug: thomson-reuters-transactions-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance/v2
  baseurl_source: declared
  description: The TransactionTypeMappings API from Thomson Reuters — 2 operation(s) for transactiontypemappings.
  name: Thomson Reuters Transaction Type Mappings API
  slug: thomson-reuters-transactiontypemappings-api
- baseURL: https://api.thomsonreuters.com/us/engagementmanager
  baseurl_source: declared
  description: Get/Add/Edit/Delete Trial Balance accounts
  name: Thomson Reuters Trial Balance API
  slug: thomson-reuters-trial-balance-api
- baseURL: https://api.thomsonreuters.com/gosystem/tax-returns
  baseurl_source: declared
  description: The Trial Balance Compute API from Thomson Reuters — 3 operation(s) for trial balance compute.
  name: Thomson Reuters Trial Balance Compute API
  slug: thomson-reuters-trial-balance-compute-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Trust Users API from Thomson Reuters — 2 operation(s) for trust users.
  name: Thomson Reuters Trust Users API
  slug: thomson-reuters-trust-users-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Operations related to updating documents
  name: Thomson Reuters Update Document API
  slug: thomson-reuters-update-document-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/efiles-api/v1
  baseurl_source: declared
  description: Use the UploadLinks endpoint to get a link to upload eFile content.
  name: Thomson Reuters Upload Links API
  slug: thomson-reuters-uploadlinks-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: The User API from Thomson Reuters — 21 operation(s) for user.
  name: Thomson Reuters User API
  slug: thomson-reuters-user-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The user-controller API from Thomson Reuters — 9 operation(s) for user-controller.
  name: Thomson Reuters User Controller API
  slug: thomson-reuters-user-controller-api
- baseURL: https://api.thomsonreuters.com/us/engagementmanager
  baseurl_source: declared
  description: Get/Add/Edit/Delete user and manage permissions
  name: Thomson Reuters User Management API
  slug: thomson-reuters-user-management-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: UserGroupAdministration
  name: Thomson Reuters User Group Administration API
  slug: thomson-reuters-usergroupadministration-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Validate Registration numbers (VAT) with authorities like VIES, eVatR and HMRC.
  name: Thomson Reuters Vat Service API
  slug: thomson-reuters-vat-service-api
- baseURL: https://api-apac.onesourcetax.com/fringe-benefits-tax/eap/benefits
  baseurl_source: declared
  description: The Vehicle Detail API from Thomson Reuters — 1 operation(s) for vehicle detail.
  name: Thomson Reuters Vehicle Detail API
  slug: thomson-reuters-vehicle-detail-api
- baseURL: https://api.thomsonreuters.com/regulatory-intelligence
  baseurl_source: declared
  description: Version Controller
  name: Thomson Reuters Version Controller API
  slug: thomson-reuters-version-controller-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: The Versions API from Thomson Reuters — 9 operation(s) for versions.
  name: Thomson Reuters Versions API
  slug: thomson-reuters-versions-api
- baseURL: https://api-emea.onesourcetax.com/indirect-tax-compliance
  baseurl_source: declared
  description: The WorkbookImports API from Thomson Reuters — 4 operation(s) for workbookimports.
  name: Thomson Reuters Workbook Imports API
  slug: thomson-reuters-workbookimports-api
- baseURL: https://api.thomsonreuters.com/gofileroom
  baseurl_source: declared
  description: The Workflow API from Thomson Reuters — 13 operation(s) for workflow.
  name: Thomson Reuters Workflow API
  slug: thomson-reuters-workflow-api
- baseURL: https://api.thomsonreuters.com/us/engagementmanager
  baseurl_source: declared
  description: Get/Add/Edit/Move workpapers and manage documents
  name: Thomson Reuters Workpapers API
  slug: thomson-reuters-workpapers-api
- baseURL: https://api.onesourcetax.com/administration/v1/financial-hierarchies
  baseurl_source: declared
  description: Operations related to zones API controller
  name: Thomson Reuters Zones API Controller API
  slug: thomson-reuters-zones-api-controller-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/user-info-api/v1
  baseurl_source: declared
  description: Use the ActionItems endpoint to get the action items of a user in Legal Tracker.
  name: Thomson Reuters Action Items API
  slug: thomson-reuters-action-items-api
- baseURL: https://api.thomsonreuters.com/legal-tracker/datawarehouse-api/odata/v1
  baseurl_source: declared
  description: The Org Units API from Thomson Reuters — 3 operation(s) for org units.
  name: Thomson Reuters Org Units API
  slug: thomson-reuters-org-units-api
artifact_total: 513
asyncapis:
- description: ''
  name: Thomson Reuters Webhooks
  slug: thomson-reuters-webhooks
common:
- group: other
  href: https://artifacts.apis.io/thomson-reuters/capabilities/thomson-reuters-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thomson-reuters-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/thomson-reuters/agentic-access/thomson-reuters-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thomson-reuters-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/thomson-reuters/rules/thomson-reuters-rules.yml
  title: ''
  type: Spectral
  url: rules/thomson-reuters-rules.yml
- group: design
  href: https://artifacts.apis.io/thomson-reuters/json-ld/thomson-reuters-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/thomson-reuters-context.jsonld
- group: design
  href: https://artifacts.apis.io/thomson-reuters/vocabulary/thomson-reuters-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thomson-reuters-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/thomson-reuters/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/thomson-reuters/asyncapi/thomson-reuters-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thomson-reuters-webhooks.yml
- group: design
  href: https://artifacts.apis.io/thomson-reuters/data-model/thomson-reuters-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thomson-reuters-data-model.yml
- group: design
  href: https://artifacts.apis.io/thomson-reuters/conventions/thomson-reuters-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thomson-reuters-conventions.yml
- group: start
  href: https://artifacts.apis.io/thomson-reuters/sandbox/thomson-reuters-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thomson-reuters-sandbox.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.thomsonreuters.com/pages/api-catalog/04c760fa-1cfc-51cc-94a2-661f2d266acc
- group: design
  href: https://artifacts.apis.io/thomson-reuters/lifecycle/thomson-reuters-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thomson-reuters-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/thomson-reuters/errors/thomson-reuters-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thomson-reuters-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thomson-reuters/conformance/thomson-reuters-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thomson-reuters-conformance.yml
- group: other
  href: https://artifacts.apis.io/thomson-reuters/hosts/thomson-reuters-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thomson-reuters-hosts.yml
- group: build
  href: https://artifacts.apis.io/thomson-reuters/integrations/thomson-reuters-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/thomson-reuters-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/thomson-reuters/vendors/thomson-reuters-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thomson-reuters-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.thomsonreuters.com/en/trust-center
- group: auth
  href: https://artifacts.apis.io/thomson-reuters/scopes/thomson-reuters-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/thomson-reuters-scopes.yml
- group: auth
  href: https://artifacts.apis.io/thomson-reuters/authentication/thomson-reuters-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thomson-reuters-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/thomson-reuters/plans/thomson-reuters-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thomson-reuters-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/thomson-reuters/rate-limits/thomson-reuters-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thomson-reuters-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/thomson-reuters/finops/thomson-reuters-finops.yml
  title: ''
  type: FinOps
  url: finops/thomson-reuters-finops.yml
- group: auth
  href: https://artifacts.apis.io/thomson-reuters/security/thomson-reuters-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thomson-reuters-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thomson-reuters
- group: company
  title: ''
  type: Website
  url: https://www.thomsonreuters.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thomsonreuters.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.thomsonreuters.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thomsonreuters
- group: company
  title: ''
  type: Blog
  url: https://legal.thomsonreuters.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.thomsonreuters.com/pages/api-catalog
- group: start
  title: ''
  type: Login
  url: https://community.thomsonreuters.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://sales.legalsolutions.thomsonreuters.com/en-us/products/westlaw-edge/plans-pricing?segment=lawfirm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thomsonreuters.com/en/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thomsonreuters.com/en/terms-of-use.html
- group: operate
  title: ''
  type: Support
  url: https://developers.thomsonreuters.com/pages/sales-and-support
- group: operate
  title: ''
  type: Community
  url: https://community.thomsonreuters.com/
created: '2026-03-16'
description: Thomson Reuters provides over 137 APIs across legal, tax and accounting, risk and fraud, and trade and supply industries through their global developer portal. APIs cover Westlaw legal research, Checkpoint tax content, ONESOURCE tax software, HighQ document management, Legal Tracker matter management, and risk and fraud solutions including identity verification and adverse media screening.
finops:
- has_sources: false
  method: generated
  name: Thomson Reuters Finops
  primary_unit: request
  service_category: API
  slug: thomson-reuters-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thomson-reuters.png
json_schemas:
- name: AccountModel
  property_count: 23
  slug: thomson-reuters-account-model
- name: AccountResponseModel
  property_count: 3
  slug: thomson-reuters-account-response-model
- name: ApiCollectionCollectionDTO
  property_count: 2
  slug: thomson-reuters-api-collection-collection-dto
- name: ApiCollectionCollectionItem
  property_count: 2
  slug: thomson-reuters-api-collection-collection-item
- name: ApiCollectionComparisonsResponse
  property_count: 2
  slug: thomson-reuters-api-collection-comparisons-response
- name: ApiCollectionCurrencyViewItem
  property_count: 2
  slug: thomson-reuters-api-collection-currency-view-item
- name: ApiCollectionFinancialHierarchyBranchResponse
  property_count: 2
  slug: thomson-reuters-api-collection-financial-hierarchy-branch-response
- name: ApiCollectionFinancialHierarchyNodeResponse
  property_count: 2
  slug: thomson-reuters-api-collection-financial-hierarchy-node-response
- name: ApiCollectionJobResponse
  property_count: 2
  slug: thomson-reuters-api-collection-job-response
- name: ApiCollectionTemplateMeta
  property_count: 2
  slug: thomson-reuters-api-collection-template-meta
- name: ApiCollectionTopicDTO
  property_count: 2
  slug: thomson-reuters-api-collection-topic-dto
- name: ApiCollectionTopicRecordDTO
  property_count: 2
  slug: thomson-reuters-api-collection-topic-record-dto
- name: ApiInfoResponse
  property_count: 3
  slug: thomson-reuters-api-info-response
- name: ApplicationResponse
  property_count: 9
  slug: thomson-reuters-application-response
- name: AssignGroupResponse
  property_count: 3
  slug: thomson-reuters-assign-group-response
- name: AuthTokenResponse
  property_count: 0
  slug: thomson-reuters-auth-token-response
- name: BlueprintId
  property_count: 2
  slug: thomson-reuters-blueprint-id
- name: BusinessResponse
  property_count: 2
  slug: thomson-reuters-business-response
- name: CalculateDueDateRequest
  property_count: 8
  slug: thomson-reuters-calculate-due-date-request
- name: CalculateRequest
  property_count: 5
  slug: thomson-reuters-calculate-request
- name: CalculateResponse
  property_count: 7
  slug: thomson-reuters-calculate-response
- name: CalculatedDueDateResponse
  property_count: 4
  slug: thomson-reuters-calculated-due-date-response
- name: ChartImportProcessResponse
  property_count: 3
  slug: thomson-reuters-chart-import-process-response
- name: CollectionDTO
  property_count: 6
  slug: thomson-reuters-collection-dto
- name: CollectionPatchRequestDTO
  property_count: 5
  slug: thomson-reuters-collection-patch-request-dto
- name: CollectionRecordsColumnDTO
  property_count: 1
  slug: thomson-reuters-collection-records-column-dto
- name: CollectionVersionDTO
  property_count: 12
  slug: thomson-reuters-collection-version-dto
- name: CommitRequest
  property_count: 7
  slug: thomson-reuters-commit-request
- name: CommitResponse
  property_count: 7
  slug: thomson-reuters-commit-response
- name: CompanyInfoCollection
  property_count: 1
  slug: thomson-reuters-company-info-collection
- name: CompanyOffice
  property_count: 11
  slug: thomson-reuters-company-office
- name: ComparisonDownloadResponse
  property_count: 1
  slug: thomson-reuters-comparison-download-response
- name: ComparisonsResponse
  property_count: 9
  slug: thomson-reuters-comparisons-response
- name: CountryCollection
  property_count: 1
  slug: thomson-reuters-country-collection
- name: CreateCollectionRequest
  property_count: 5
  slug: thomson-reuters-create-collection-request
- name: CreateComparisonsRequest
  property_count: 3
  slug: thomson-reuters-create-comparisons-request
- name: CreateOrUpdateJobRequest
  property_count: 6
  slug: thomson-reuters-create-or-update-job-request
- name: CreateOrganizationalUnitModel
  property_count: 3
  slug: thomson-reuters-create-organizational-unit-model
- name: CreatePracticeGroupModel
  property_count: 3
  slug: thomson-reuters-create-practice-group-model
- name: CurrencyResponse
  property_count: 3
  slug: thomson-reuters-currency-response
- name: CustomLevel4NodeRequest
  property_count: 1
  slug: thomson-reuters-custom-level4-node-request
- name: CustomLevel4NodeResponse
  property_count: 3
  slug: thomson-reuters-custom-level4-node-response
- name: CustomViewDTO
  property_count: 3
  slug: thomson-reuters-custom-view-dto
- name: CustomViewResponseDTO
  property_count: 5
  slug: thomson-reuters-custom-view-response-dto
- name: DeleteGroupResponse
  property_count: 3
  slug: thomson-reuters-delete-group-response
- name: DocumentAction
  property_count: 1
  slug: thomson-reuters-document-action
- name: DocumentFileStatus
  property_count: 22
  slug: thomson-reuters-document-file-status
- name: EDocument
  property_count: 42
  slug: thomson-reuters-edocument
- name: EffectiveTaxRate
  property_count: 22
  slug: thomson-reuters-effective-tax-rate
- name: EfileAttachmentFormData
  property_count: 14
  slug: thomson-reuters-efile-attachment-form-data
- name: EfileAttachmentMetadata
  property_count: 10
  slug: thomson-reuters-efile-attachment-metadata
- name: EfileAttachmentUpdateFormData
  property_count: 9
  slug: thomson-reuters-efile-attachment-update-form-data
- name: EFileJurisdictionsRepresentation
  property_count: 1
  slug: thomson-reuters-efile-jurisdictions-representation
- name: EFileJurisdictionsSubmissionResponse
  property_count: 2
  slug: thomson-reuters-efile-jurisdictions-submission-response
- name: EFileJurisdictionsWrapperV2
  property_count: 1
  slug: thomson-reuters-efile-jurisdictions-wrapper-v2
- name: EFileRepresentation
  property_count: 2
  slug: thomson-reuters-efile-representation
- name: EFileRequest
  property_count: 5
  slug: thomson-reuters-efile-request
- name: EFileRequestV2
  property_count: 5
  slug: thomson-reuters-efile-request-v2
- name: EFileStatusAcknowledgementRepresentation
  property_count: 20
  slug: thomson-reuters-efile-status-acknowledgement-representation
- name: EFileStatusDetailsRepresentation
  property_count: 6
  slug: thomson-reuters-efile-status-details-representation
- name: EFileStatusQuery
  property_count: 4
  slug: thomson-reuters-efile-status-query
- name: EFileStatusesRepresentation
  property_count: 1
  slug: thomson-reuters-efile-statuses-representation
- name: EFileSubmissionDetails
  property_count: 1
  slug: thomson-reuters-efile-submission-details
- name: EFilesGenerationResponse
  property_count: 2
  slug: thomson-reuters-efiles-generation-response
- name: ExtractionResponse
  property_count: 12
  slug: thomson-reuters-extraction-response
- name: federalAdjustmentListRepresentation
  property_count: 1
  slug: thomson-reuters-federal-adjustment-list-representation
- name: Field
  property_count: 15
  slug: thomson-reuters-field
- name: FileRequest
  property_count: 4
  slug: thomson-reuters-file-request
- name: FileResponse
  property_count: 15
  slug: thomson-reuters-file-response
- name: FirmFlowReportRequestNewV2
  property_count: 42
  slug: thomson-reuters-firm-flow-report-request-new-v2
- name: FirmFlowReportRequestNewV3
  property_count: 42
  slug: thomson-reuters-firm-flow-report-request-new-v3
- name: FirmFlowReportRequest
  property_count: 33
  slug: thomson-reuters-firm-flow-report-request
- name: FirmFlowReportRequestV2
  property_count: 34
  slug: thomson-reuters-firm-flow-report-request-v2
- name: GetUserGroupResponseWraper
  property_count: 0
  slug: thomson-reuters-get-user-group-response-wraper
- name: GetUserResponse
  property_count: 9
  slug: thomson-reuters-get-user-response
- name: IdResponseString
  property_count: 1
  slug: thomson-reuters-id-response-string
- name: IngestionResponse
  property_count: 10
  slug: thomson-reuters-ingestion-response
- name: InvoicePaymentModel
  property_count: 20
  slug: thomson-reuters-invoice-payment-model
- name: JobResponse
  property_count: 10
  slug: thomson-reuters-job-response
- name: JurisdictionAttachmentCodeDetail
  property_count: 13
  slug: thomson-reuters-jurisdiction-attachment-code-detail
- name: InvoiceLine
  property_count: 32
  slug: thomson-reuters-legal-tracker-datawarehouse-invoice-line
- name: Invoice
  property_count: 52
  slug: thomson-reuters-legal-tracker-datawarehouse-invoice
- name: MatterCustomCurrencyField
  property_count: 43
  slug: thomson-reuters-legal-tracker-datawarehouse-matter-custom-currency-field
- name: MatterCustomDateField
  property_count: 23
  slug: thomson-reuters-legal-tracker-datawarehouse-matter-custom-date-field
- name: MatterCustomDropdownField
  property_count: 43
  slug: thomson-reuters-legal-tracker-datawarehouse-matter-custom-dropdown-field
- name: Matter
  property_count: 85
  slug: thomson-reuters-legal-tracker-datawarehouse-matter
- name: LoadStatus
  property_count: 46
  slug: thomson-reuters-load-status
- name: MetadataDTO
  property_count: 6
  slug: thomson-reuters-metadata-dto
- name: MetadataMinimalDTO
  property_count: 3
  slug: thomson-reuters-metadata-minimal-dto
- name: MultiStatusResponse
  property_count: 8
  slug: thomson-reuters-multi-status-response
- name: ObligationSearchResponse
  property_count: 2
  slug: thomson-reuters-obligation-search-response
- name: OpenTaxReturnResponseDto
  property_count: 5
  slug: thomson-reuters-open-tax-return-response-dto
- name: OperationModel
  property_count: 5
  slug: thomson-reuters-operation-model
- name: Option
  property_count: 10
  slug: thomson-reuters-option
- name: OrganizationalUnit
  property_count: 4
  slug: thomson-reuters-organizational-unit
- name: ParametersResponse
  property_count: 3
  slug: thomson-reuters-parameters-response
- name: PartnershipK1
  property_count: 13
  slug: thomson-reuters-partnership-k1
- name: PatchBluePrintNameDTO
  property_count: 2
  slug: thomson-reuters-patch-blue-print-name-dto
- name: PatchComparisonsRequest
  property_count: 1
  slug: thomson-reuters-patch-comparisons-request
- name: PatchIngestFileRequest
  property_count: 4
  slug: thomson-reuters-patch-ingest-file-request
- name: PatchTemplateRequest
  property_count: 4
  slug: thomson-reuters-patch-template-request
- name: Payable
  property_count: 25
  slug: thomson-reuters-payable
- name: PaymentModel
  property_count: 6
  slug: thomson-reuters-payment-model
- name: PermissionResponse
  property_count: 2
  slug: thomson-reuters-permission-response
- name: PostTemplatesResponse
  property_count: 1
  slug: thomson-reuters-post-templates-response
- name: PostUserGroupsRequestWrapper
  property_count: 1
  slug: thomson-reuters-post-user-groups-request-wrapper
- name: PredictiveFeedbackRequest
  property_count: 3
  slug: thomson-reuters-predictive-feedback-request
- name: PredictiveMappingRequest
  property_count: 3
  slug: thomson-reuters-predictive-mapping-request
- name: PredictiveMappingResponseFinancialHierarchyDto
  property_count: 2
  slug: thomson-reuters-predictive-mapping-response-financial-hierarchy-dto
- name: PrintLocatorRequest
  property_count: 13
  slug: thomson-reuters-print-locator-request
- name: PrintOptionsResponse
  property_count: 1
  slug: thomson-reuters-print-options-response
- name: PrintStatusResponse
  property_count: 1
  slug: thomson-reuters-print-status-response
- name: PrintV1Request
  property_count: 4
  slug: thomson-reuters-print-v1-request
- name: RecordsDTO
  property_count: 2
  slug: thomson-reuters-records-dto
- name: RecordsResponse
  property_count: 2
  slug: thomson-reuters-records-response
- name: ResultsDownloadDTO
  property_count: 1
  slug: thomson-reuters-results-download-dto
- name: ResultsDTO
  property_count: 2
  slug: thomson-reuters-results-dto
- name: ResultsResponse
  property_count: 2
  slug: thomson-reuters-results-response
- name: ReverseRequest
  property_count: 7
  slug: thomson-reuters-reverse-request
- name: ReverseResponse
  property_count: 8
  slug: thomson-reuters-reverse-response
- name: SingleCollectionDTO
  property_count: 11
  slug: thomson-reuters-single-collection-dto
- name: SingleScriptedIntegrationResponse
  property_count: 6
  slug: thomson-reuters-single-scripted-integration-response
- name: StateCollection
  property_count: 1
  slug: thomson-reuters-state-collection
- name: StateProvisionDetail
  property_count: 74
  slug: thomson-reuters-state-provision-detail
- name: StateProvision
  property_count: 72
  slug: thomson-reuters-state-provision
- name: StatusResponse
  property_count: 8
  slug: thomson-reuters-status-response
- name: StatusWrapper
  property_count: 1
  slug: thomson-reuters-status-wrapper
- name: TaxProvisionDetail
  property_count: 107
  slug: thomson-reuters-tax-provision-detail
- name: TaxProvision
  property_count: 106
  slug: thomson-reuters-tax-provision
- name: TemplatePipeline
  property_count: 4
  slug: thomson-reuters-template-pipeline
- name: Template
  property_count: 11
  slug: thomson-reuters-template
- name: Ten99Control
  property_count: 8
  slug: thomson-reuters-ten99-control
- name: TopicDownloadDTO
  property_count: 4
  slug: thomson-reuters-topic-download-dto
- name: TopicDownloadListDTO
  property_count: 2
  slug: thomson-reuters-topic-download-list-dto
- name: TopicDTO
  property_count: 11
  slug: thomson-reuters-topic-dto
- name: TopicRecordValuesDTO
  property_count: 2
  slug: thomson-reuters-topic-record-values-dto
- name: TrackerODataResponseOfAPBatchModel
  property_count: 3
  slug: thomson-reuters-tracker-odata-response-of-apbatch-model
- name: TrackerODataResponseOfAPBatchRunModel
  property_count: 3
  slug: thomson-reuters-tracker-odata-response-of-apbatch-run-model
- name: TrackerODataResponseOfAPRouteModel
  property_count: 3
  slug: thomson-reuters-tracker-odata-response-of-aproute-model
- name: TrackerODataResponseOfInvoicePaymentModel
  property_count: 3
  slug: thomson-reuters-tracker-odata-response-of-invoice-payment-model
- name: TransactionExtractRequest
  property_count: 27
  slug: thomson-reuters-transaction-extract-request
- name: TransactionExtractResponse
  property_count: 2
  slug: thomson-reuters-transaction-extract-response
- name: TRTA.Athena.Models.Api.V4.Calculations.CalcSourceFieldDataResponse
  property_count: 3
  slug: thomson-reuters-trta-athena-models-api-v4-calculations-calc-source-field-data-response
- name: TRTA.Athena.Models.Api.V4.Calculations.CalculationSheetdataResponse
  property_count: 6
  slug: thomson-reuters-trta-athena-models-api-v4-calculations-calculation-sheetdata-response
- name: TRTA.Athena.Models.Api.V4.Calculations.CellSourceValueExportRequest
  property_count: 2
  slug: thomson-reuters-trta-athena-models-api-v4-calculations-cell-source-value-export-request
- name: TRTA.Athena.Models.Api.V4.Calculations.EfiledCalculationResult
  property_count: 22
  slug: thomson-reuters-trta-athena-models-api-v4-calculations-efiled-calculation-result
- name: TRTA.Athena.Models.Api.V4.Calculations.GetInsertSheet
  property_count: 9
  slug: thomson-reuters-trta-athena-models-api-v4-calculations-get-insert-sheet
- name: TRTA.Athena.Models.Api.V4.ChartOfAccounts.ChartOfAccountsCreateRequest
  property_count: 2
  slug: thomson-reuters-trta-athena-models-api-v4-chart-of-accounts-chart-of-accounts-create-request
- name: TRTA.Athena.Models.Api.V4.ChartOfAccounts.ChartOfAccountsPutRequest
  property_count: 2
  slug: thomson-reuters-trta-athena-models-api-v4-chart-of-accounts-chart-of-accounts-put-request
- name: TRTA.Athena.Models.Api.V4.ChartOfAccounts.ChartOfAccountsReponse
  property_count: 3
  slug: thomson-reuters-trta-athena-models-api-v4-chart-of-accounts-chart-of-accounts-reponse
- name: TRTA.Athena.Models.Api.V4.Common.OpertaionsResponse
  property_count: 2
  slug: thomson-reuters-trta-athena-models-api-v4-common-opertaions-response
- name: TRTA.Athena.Models.Api.V4.Datasets.DatasetDetail
  property_count: 9
  slug: thomson-reuters-trta-athena-models-api-v4-datasets-dataset-detail
- name: TRTA.Athena.Models.Api.V4.Datasets.Dataset
  property_count: 6
  slug: thomson-reuters-trta-athena-models-api-v4-datasets-dataset
- name: TRTA.Athena.Models.Api.V4.Datasets.NotesRequest
  property_count: 5
  slug: thomson-reuters-trta-athena-models-api-v4-datasets-notes-request
- name: TRTA.Athena.Models.Api.V4.Imports.CorporateTax.ImportTypeListReponse
  property_count: 1
  slug: thomson-reuters-trta-athena-models-api-v4-imports-corporate-tax-import-type-list-reponse
- name: TRTA.Athena.Models.Api.V4.Imports.CorporateTax.ImportTypeMetaDataListReponse
  property_count: 1
  slug: thomson-reuters-trta-athena-models-api-v4-imports-corporate-tax-import-type-meta-data-list-reponse
- name: TRTA.Athena.Models.Api.V4.Imports.CorporateTax.JournalsListResponse
  property_count: 1
  slug: thomson-reuters-trta-athena-models-api-v4-imports-corporate-tax-journals-list-response
- name: TRTA.Athena.Models.Api.V4.Imports
  property_count: 5
  slug: thomson-reuters-trta-athena-models-api-v4-imports
- name: TRTA.Athena.Models.Api.V4.Mappings.MappingCreateRequest
  property_count: 7
  slug: thomson-reuters-trta-athena-models-api-v4-mappings-mapping-create-request
- name: TRTA.Athena.Models.Api.V4.Mappings.MappingPutRequest
  property_count: 1
  slug: thomson-reuters-trta-athena-models-api-v4-mappings-mapping-put-request
- name: TRTA.Athena.Models.Api.V4.Mappings.Mapping
  property_count: 8
  slug: thomson-reuters-trta-athena-models-api-v4-mappings-mapping
- name: TRTA.Athena.Models.Api.V4.notes.ExportNotesRequest
  property_count: 18
  slug: thomson-reuters-trta-athena-models-api-v4-notes-export-notes-request
- name: TRTA.Athena.Models.Api.V4.notes.ExportNotesResponse
  property_count: 23
  slug: thomson-reuters-trta-athena-models-api-v4-notes-export-notes-response
- name: TRTA.Athena.Models.Api.V4.Queries.RollforwardRequest
  property_count: 4
  slug: thomson-reuters-trta-athena-models-api-v4-queries-rollforward-request
- name: TRTA.Athena.Models.Api.V4.Reports.ReportInput
  property_count: 2
  slug: thomson-reuters-trta-athena-models-api-v4-reports-report-input
- name: TRTA.Athena.Models.Api.V4.Reports.ReportListResponse
  property_count: 1
  slug: thomson-reuters-trta-athena-models-api-v4-reports-report-list-response
- name: TRTA.Athena.Models.Api.V4.Reports.ReportMetadata
  property_count: 4
  slug: thomson-reuters-trta-athena-models-api-v4-reports-report-metadata
- name: TRTA.Athena.Models.Api.V4.Reports.ReportOutput
  property_count: 7
  slug: thomson-reuters-trta-athena-models-api-v4-reports-report-output
- name: UpdateOrganizationalUnitModel
  property_count: 3
  slug: thomson-reuters-update-organizational-unit-model
- name: UpdatePracticeGroupModel
  property_count: 3
  slug: thomson-reuters-update-practice-group-model
- name: UserDetailsV3
  property_count: 37
  slug: thomson-reuters-user-details-v3
- name: User
  property_count: 17
  slug: thomson-reuters-user
- name: Workflow.Wrapper.Model.Contract.External.InstanceSearchRequest
  property_count: 11
  slug: thomson-reuters-workflow-wrapper-model-contract-external-instance-search-request
- name: Workflow.Wrapper.Model.Contract.External.InstanceSearchResponse
  property_count: 2
  slug: thomson-reuters-workflow-wrapper-model-contract-external-instance-search-response
- name: Workflow.Wrapper.Model.Contract.External.TaskSearchRequest
  property_count: 10
  slug: thomson-reuters-workflow-wrapper-model-contract-external-task-search-request
- name: Workflow.Wrapper.Model.Contract.External.TaskSearchResponse
  property_count: 2
  slug: thomson-reuters-workflow-wrapper-model-contract-external-task-search-response
jsonld:
- class_count: 22
  name: Thomson Reuters Context
  property_count: 0
  slug: thomson-reuters-context
layout: provider
mcp_servers:
- description: ''
  name: Thomson Reuters MCP Server
  slug: thomson-reuters-mcp-yml
modified: '2026-10-20'
name: Thomson Reuters
nav: Providers
network: true
overview: 'Thomson Reuters publishes 324 API contracts indexed on the [APIs.io](https://apis.io/) network, including Datasets API, Exports API, Tax Return Import/Export API, and 321 more. Tagged areas include Legal, Tax, Finance, Risk Management, and Fraud Prevention.


  The Thomson Reuters catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Thomson Reuters'' developer surface includes sandbox, authentication, documentation, engineering blog, API reference, pricing, support, and 30 more developer resources.'
plans:
- name: Thomson Reuters Plans Pricing
  plan_count: 0
  slug: thomson-reuters-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Thomson Reuters Rate Limits
  slug: thomson-reuters-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Thomson Reuters API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 3
  slug: thomson-reuters-rules
scopes:
- name: Thomson Reuters Scopes
  scope_count: 1
  slug: thomson-reuters-scopes
  summary_line: 1 scope · clientCredentials/authorizationCode
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 33
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 26.3
    contract_governance: 35.6
    contract_quality: 73.9
    developer_ergonomics: 28.0
    discoverability: 69.6
    operational_transparency: 46.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 90.3
      derived: 0
      marker_coverage: 91.3
      total: 321
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/thomson-reuters/thomson-reuters-2026-06-20T195310.png
security:
- kind: authentication
  name: Thomson Reuters Authentication
  slug: thomson-reuters-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Thomson Reuters Domain Security
  slug: thomson-reuters-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: indirect-tax-compliance-imports
  slug: thomson-reuters-indirect-tax-compliance-imports
- name: indirect-tax-compliance-reports
  slug: thomson-reuters-indirect-tax-compliance-reports
slug: thomson-reuters
tags:
- Legal
- Tax
- Finance
- Risk Management
- Fraud Prevention
- Compliance
- Data
website: https://www.thomsonreuters.com/
---
