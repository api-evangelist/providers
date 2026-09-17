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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-09-16'
api_count: 22
apis:
- description: The CALC Labor Ceiling Rates tool is a pricing research tool located on buy.gsa.gov to support government acquisition professionals in services pricing business intelligence.
  name: Contract-Awarded Labor Category (CALC) API
  slug: calc-api
- description: GSA Fleet provides leasing services for a wide variety of vehicle and fuel types for participating federal agencies with full-service leases at all-inclusive rates.
  name: GSA Fleet Vehicles / Vehicle Leasing
  slug: fleet-vehicles-api
- description: The Federal Hierarchy For Official Use Only (FOUO) API allows U.S. Government users to obtain Federal Organization details down to the office level.
  name: SAM.gov Federal Hierarchy FOUO API
  slug: samgov-fh-fouo-api
- description: Federal Hierarchy public API allows non-federal users to obtain Federal Organization details (Departments/Ind. Agency and SubTier).
  name: SAM.gov Federal Hierarchy Public API
  slug: samgov-fh-public-api
- description: Get Opportunities API provides all the published opportunity details based on the request parameters. This API requires pagination.
  name: SAM.gov Get Opportunities Public API
  slug: samgov-get-opportunities-api
- description: PSC API provides PSC data (PSC Code, PSC Name, PSC Full Name, Status, Parent PSC Code, Start Date, End Date and updated date) based on the request parameters with pagination support.
  name: SAM.gov Product Service Codes (PSC) API
  slug: samgov-psc-api
- description: The Public Location Services API provides Location Services data (Country, State, City, ZIP) for validating location data submitted to SAM.gov. Supports United States and, with GENC updates, Foreign C
  name: SAM.gov Public Location Services API
  slug: samgov-location-services-api
- description: 'Exposes the type-ahead suggestions that can appear below your search box as searchers enter their search terms. RETIRED: probed 2026-09-12 — https://open.gsa.gov/api/searchgov-suggestions/ and its Ope'
  name: Search.gov Type-Ahead Suggestions API
  slug: searchgov-suggestions-api
- description: The Rate Query API offered by TMSS 2.0 is used to retrieve shipment cost for a regular Household Goods (HHG) shipment or for an Extended Storage (EXSTG) shipment for Federal Civilian Agencies.
  name: TMSS 2.0 Rate Query API
  slug: tmss-rate-query-api
- description: 'Offers sustainable guidance and tools for various roles via the Sustainable Facilities Tool (SFTool). RETIRED: probed 2026-09-12 — https://sftool.gov/developers returns HTTP 200 but serves a catch-all'
  name: Sustainable Facilities Tool API
  slug: sustainable-facilities-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: CKAN's Action API is a powerful, RPC-style API that exposes all of CKAN's core features to API clients.
  name: General Services Administration Action API
  slug: general-services-administration-action-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The admin API from General Services Administration — 2 operation(s) for admin.
  name: General Services Administration Admin API
  slug: general-services-administration-admin-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The admin_group API from General Services Administration — 2 operation(s) for admin_group.
  name: General Services Administration Admin Group API
  slug: general-services-administration-admin-group-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The admin_permission API from General Services Administration — 1 operation(s) for admin_permission.
  name: General Services Administration Admin Permission API
  slug: general-services-administration-admin-permission-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Agencies API from General Services Administration — 1 operation(s) for agencies.
  name: General Services Administration Agencies API
  slug: general-services-administration-agencies-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Analysis API from General Services Administration — 1 operation(s) for analysis.
  name: General Services Administration Analysis API
  slug: general-services-administration-analysis-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The analytics API from General Services Administration — 2 operation(s) for analytics.
  name: General Services Administration Analytics API
  slug: general-services-administration-analytics-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The api API from General Services Administration — 2 operation(s) for api.
  name: General Services Administration API
  slug: general-services-administration-api-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The api_scope API from General Services Administration — 2 operation(s) for api_scope.
  name: General Services Administration API Scope API
  slug: general-services-administration-api-scope-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Assistance Bulk Upload API from General Services Administration — 2 operation(s) for assistance bulk upload.
  name: General Services Administration Assistance Bulk Upload API
  slug: general-services-administration-assistance-bulk-upload-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Assistance Listings API from General Services Administration — 1 operation(s) for assistance listings.
  name: General Services Administration Assistance Listings API
  slug: general-services-administration-assistance-listings-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The attachments API from General Services Administration — 5 operation(s) for attachments.
  name: General Services Administration Attachments API
  slug: general-services-administration-attachments-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The BudgetAccountLongitudinalReport API from General Services Administration — 1 operation(s) for budgetaccountlongitudinalreport.
  name: General Services Administration Budget Account Longitudinal Report API
  slug: general-services-administration-budgetaccountlongitudinalreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The BudgetAuthorityFeed API from General Services Administration — 1 operation(s) for budgetauthorityfeed.
  name: General Services Administration Budget Authority Feed API
  slug: general-services-administration-budgetauthorityfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Bureaus API from General Services Administration — 2 operation(s) for bureaus.
  name: General Services Administration Bureaus API
  slug: general-services-administration-bureaus-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The CioAuthority API from General Services Administration — 2 operation(s) for cioauthority.
  name: General Services Administration Cio Authority API
  slug: general-services-administration-cioauthority-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The CioRating API from General Services Administration — 2 operation(s) for ciorating.
  name: General Services Administration Cio Rating API
  slug: general-services-administration-ciorating-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The CioRatingCountReport API from General Services Administration — 1 operation(s) for cioratingcountreport.
  name: General Services Administration Cio Rating Count Report API
  slug: general-services-administration-cioratingcountreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The CioRatingsFeed API from General Services Administration — 1 operation(s) for cioratingsfeed.
  name: General Services Administration Cio Ratings Feed API
  slug: general-services-administration-cioratingsfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The comment submission utilities API from General Services Administration — 3 operation(s) for comment submission utilities.
  name: General Services Administration comment submission utilities API
  slug: general-services-administration-comment-submission-utilities-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The comments API from General Services Administration — 2 operation(s) for comments.
  name: General Services Administration Comments API
  slug: general-services-administration-comments-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The config API from General Services Administration — 2 operation(s) for config.
  name: General Services Administration Config API
  slug: general-services-administration-config-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The contact API from General Services Administration — 1 operation(s) for contact.
  name: General Services Administration Contact API
  slug: general-services-administration-contact-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Contract API from General Services Administration — 2 operation(s) for contract.
  name: General Services Administration Contract API
  slug: general-services-administration-contract-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The contract-award-controller API from General Services Administration — 2 operation(s) for contract-award-controller.
  name: General Services Administration Contract Award Controller API
  slug: general-services-administration-contract-award-controller-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Contracts Bulk Upload API from General Services Administration — 2 operation(s) for contracts bulk upload.
  name: General Services Administration Contracts Bulk Upload API
  slug: general-services-administration-contracts-bulk-upload-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The ContractsFeed API from General Services Administration — 1 operation(s) for contractsfeed.
  name: General Services Administration Contracts Feed API
  slug: general-services-administration-contractsfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The CostPoolFeed API from General Services Administration — 1 operation(s) for costpoolfeed.
  name: General Services Administration Cost Pool Feed API
  slug: general-services-administration-costpoolfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The CostPoolHistoryReport API from General Services Administration — 2 operation(s) for costpoolhistoryreport.
  name: General Services Administration Cost Pool History Report API
  slug: general-services-administration-costpoolhistoryreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The CostPoolLongitudinalReport API from General Services Administration — 1 operation(s) for costpoollongitudinalreport.
  name: General Services Administration Cost Pool Longitudinal Report API
  slug: general-services-administration-costpoollongitudinalreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The CX Collections API from General Services Administration — 3 operation(s) for cx collections.
  name: General Services Administration CX Collections API
  slug: general-services-administration-cx-collections-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Digital Registry API from General Services Administration — 1 operation(s) for digital registry.
  name: General Services Administration Digital Registry API
  slug: general-services-administration-digital-registry-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The dockets API from General Services Administration — 2 operation(s) for dockets.
  name: General Services Administration Dockets API
  slug: general-services-administration-dockets-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The documents API from General Services Administration — 2 operation(s) for documents.
  name: General Services Administration Documents API
  slug: general-services-administration-documents-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Domain API from General Services Administration — 1 operation(s) for domain.
  name: General Services Administration Domain API
  slug: general-services-administration-domain-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Download File Controller
  name: General Services Administration Download File Controller API
  slug: general-services-administration-download-file-controller-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Entity Management Controller
  name: General Services Administration Entity Management Controller API
  slug: general-services-administration-entity-management-controller-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Entity Management Controller V 2
  name: General Services Administration Entity Management Controller V 2 API
  slug: general-services-administration-entity-management-controller-v-2-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Entity Management Controller V 3
  name: General Services Administration Entity Management Controller V 3 API
  slug: general-services-administration-entity-management-controller-v-3-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Entity Management Controller V 4
  name: General Services Administration Entity Management Controller V 4 API
  slug: general-services-administration-entity-management-controller-v-4-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Operations pertaining to Entity Management Data
  name: General Services Administration Entity Management Extract Controller API
  slug: general-services-administration-entity-management-extract-controller-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Exclusions Api Controller V 4
  name: General Services Administration Exclusions API Controller V 4 API
  slug: general-services-administration-exclusions-api-controller-v-4-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Forms (also called surveys) are used to collect user feedback. With a Touchpoints account, you can create a form, publish it in one of several digital formats and view form responses submitted by your
  name: General Services Administration Forms API
  slug: general-services-administration-forms-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The FundingSourceFeed API from General Services Administration — 1 operation(s) for fundingsourcefeed.
  name: General Services Administration Funding Source Feed API
  slug: general-services-administration-fundingsourcefeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The FundingSourceHistoryReport API from General Services Administration — 2 operation(s) for fundingsourcehistoryreport.
  name: General Services Administration Funding Source History Report API
  slug: general-services-administration-fundingsourcehistoryreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The InvestmentTypeReport API from General Services Administration — 1 operation(s) for investmenttypereport.
  name: General Services Administration Investment Type Report API
  slug: general-services-administration-investmenttypereport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The ItTowerFeed API from General Services Administration — 1 operation(s) for ittowerfeed.
  name: General Services Administration It Tower Feed API
  slug: general-services-administration-ittowerfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The ITTowerHistoryReport API from General Services Administration — 2 operation(s) for ittowerhistoryreport.
  name: General Services Administration IT Tower History Report API
  slug: general-services-administration-ittowerhistoryreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The ItTowerLongitudinalReport API from General Services Administration — 1 operation(s) for ittowerlongitudinalreport.
  name: General Services Administration It Tower Longitudinal Report API
  slug: general-services-administration-ittowerlongitudinalreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The IVL API from General Services Administration — 4 operation(s) for ivl.
  name: General Services Administration IVL API
  slug: general-services-administration-ivl-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Ledger API from General Services Administration — 2 operation(s) for ledger.
  name: General Services Administration Ledger API
  slug: general-services-administration-ledger-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The LedgerHistoryFeed API from General Services Administration — 1 operation(s) for ledgerhistoryfeed.
  name: General Services Administration Ledger History Feed API
  slug: general-services-administration-ledgerhistoryfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The LongitudinalReport API from General Services Administration — 1 operation(s) for longitudinalreport.
  name: General Services Administration Longitudinal Report API
  slug: general-services-administration-longitudinalreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Metric API from General Services Administration — 2 operation(s) for metric.
  name: General Services Administration Metric API
  slug: general-services-administration-metric-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The MetricActual API from General Services Administration — 2 operation(s) for metricactual.
  name: General Services Administration Metric Actual API
  slug: general-services-administration-metricactual-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The MetricActualFeed API from General Services Administration — 1 operation(s) for metricactualfeed.
  name: General Services Administration Metric Actual Feed API
  slug: general-services-administration-metricactualfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The MetricActualsCountReport API from General Services Administration — 1 operation(s) for metricactualscountreport.
  name: General Services Administration Metric Actuals Count Report API
  slug: general-services-administration-metricactualscountreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The MetricFeed API from General Services Administration — 1 operation(s) for metricfeed.
  name: General Services Administration Metric Feed API
  slug: general-services-administration-metricfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The OperationalAnalysis API from General Services Administration — 2 operation(s) for operationalanalysis.
  name: General Services Administration Operational Analysis API
  slug: general-services-administration-operationalanalysis-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The OperationalAnalysisFeed API from General Services Administration — 1 operation(s) for operationalanalysisfeed.
  name: General Services Administration Operational Analysis Feed API
  slug: general-services-administration-operationalanalysisfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Opportunity API from General Services Administration — 14 operation(s) for opportunity.
  name: General Services Administration Opportunity API
  slug: general-services-administration-opportunity-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The PerformanceGovId API from General Services Administration — 2 operation(s) for performancegovid.
  name: General Services Administration Performance Gov ID API
  slug: general-services-administration-performancegovid-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Projects API from General Services Administration — 2 operation(s) for projects.
  name: General Services Administration Projects API
  slug: general-services-administration-projects-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The ProjectsFeed API from General Services Administration — 1 operation(s) for projectsfeed.
  name: General Services Administration Projects Feed API
  slug: general-services-administration-projectsfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Rates API from General Services Administration — 5 operation(s) for rates.
  name: General Services Administration Rates API
  slug: general-services-administration-rates-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Search submitted reports
  name: General Services Administration Report Search API
  slug: general-services-administration-report-search-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Reports API from General Services Administration — 1 operation(s) for reports.
  name: General Services Administration Reports API
  slug: general-services-administration-reports-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The search API from General Services Administration — 2 operation(s) for search.
  name: General Services Administration Search API
  slug: general-services-administration-search-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The search-result API from General Services Administration — 2 operation(s) for search-result.
  name: General Services Administration Search Result API
  slug: general-services-administration-search-result-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Services API from General Services Administration — 5 operation(s) for services.
  name: General Services Administration Services API
  slug: general-services-administration-services-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Subaward Search Module API API from General Services Administration — 1 operation(s) for subaward search module api.
  name: General Services Administration Subaward Search Module API
  slug: general-services-administration-subaward-search-module-api-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The SupplementalServicesFeed API from General Services Administration — 1 operation(s) for supplementalservicesfeed.
  name: General Services Administration Supplemental Services Feed API
  slug: general-services-administration-supplementalservicesfeed-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The UiiLongitudinalReport API from General Services Administration — 1 operation(s) for uiilongitudinalreport.
  name: General Services Administration Uii Longitudinal Report API
  slug: general-services-administration-uiilongitudinalreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The user API from General Services Administration — 2 operation(s) for user.
  name: General Services Administration User API
  slug: general-services-administration-user-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The user_role API from General Services Administration — 1 operation(s) for user_role.
  name: General Services Administration User Role API
  slug: general-services-administration-user-role-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The VarianceScoresCountReport API from General Services Administration — 1 operation(s) for variancescorescountreport.
  name: General Services Administration Variance Scores Count Report API
  slug: general-services-administration-variancescorescountreport-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The Website API from General Services Administration — 2 operation(s) for website.
  name: General Services Administration Website API
  slug: general-services-administration-website-api
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: The website_backend API from General Services Administration — 2 operation(s) for website_backend.
  name: General Services Administration Website Backend API
  slug: general-services-administration-website-backend-api
- baseURL: https://api.gsa.gov/acquisition/calc/v3
  baseurl_source: declared
  description: The Funding Sources API from General Services Administration — 2 operation(s) for funding sources.
  name: General Services Administration Funding Sources API
  slug: general-services-administration-funding-sources-api
artifact_total: 96
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-acquisition-gateway-listings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-acquisition-gateway-listings-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-analytics-dap-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-analytics-dap-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-apidatagov-admin-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-apidatagov-admin-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-apidatagov-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-apidatagov-metrics-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-datagov-ckan-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-datagov-ckan-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-it-collect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-it-collect-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-per-diem-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-per-diem-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-regulations-gov-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-regulations-gov-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-sam-entity-extracts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-sam-entity-extracts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-sam-entity-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-sam-entity-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-sam-exclusions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-sam-exclusions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-sam-opportunity-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-sam-opportunity-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-assistance-listings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-assistance-listings-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-acquisition-subaward-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-acquisition-subaward-reporting-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-assistance-subaward-reporting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-assistance-subaward-reporting-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-contract-awards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-contract-awards-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-sam-subaward-bulkupload-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-sam-subaward-bulkupload-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-searchgov-clicks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-searchgov-clicks-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-searchgov-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-searchgov-results-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-site-scanning-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-site-scanning-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-touchpoints-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-touchpoints-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/overlays/general-services-administration-sam-subcontracting-plan-reports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/general-services-administration-sam-subcontracting-plan-reports-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/authentication/general-services-administration-authentication.yml
  title: ''
  type: Authentication
  url: authentication/general-services-administration-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/security/general-services-administration-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/general-services-administration-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/security/general-services-administration-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/general-services-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gsa
- group: company
  title: ''
  type: Website
  url: https://open.gsa.gov/api/
- group: docs
  title: ''
  type: Documentation
  url: https://open.gsa.gov/api/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.gsa.gov/
- group: docs
  title: ''
  type: APIReference
  url: https://open.gsa.gov/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.data.gov/docs/developer-manual/
- group: start
  title: ''
  type: SignUp
  url: https://api.data.gov/signup/
- group: operate
  title: ''
  type: Support
  url: https://open.gsa.gov/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GSA
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gsa.gov/website-information/website-policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gsa.gov/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.gsa.gov/blog
- group: auth
  title: ''
  type: Security
  url: https://gsa.gov/vulnerability-disclosure-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/well-known/general-services-administration-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/general-services-administration-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/well-known/general-services-administration-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/general-services-administration-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/conformance/general-services-administration-conformance.yml
  title: ''
  type: Conformance
  url: conformance/general-services-administration-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/conformance/general-services-administration-conformance.yml
  title: ''
  type: Compliance
  url: conformance/general-services-administration-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/packages/general-services-administration-packages.yml
  title: ''
  type: Packages
  url: packages/general-services-administration-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/components/general-services-administration-components.yml
  title: ''
  type: Components
  url: components/general-services-administration-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/mcp/general-services-administration-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/general-services-administration-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/mcp/general-services-administration-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/general-services-administration-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/llms/general-services-administration-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/general-services-administration-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/lifecycle/general-services-administration-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/general-services-administration-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/changelog/general-services-administration-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/general-services-administration-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/errors/general-services-administration-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/general-services-administration-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/conventions/general-services-administration-conventions.yml
  title: ''
  type: Conventions
  url: conventions/general-services-administration-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/sandbox/general-services-administration-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/general-services-administration-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/rate-limits/general-services-administration-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/general-services-administration-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/plans/general-services-administration-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/general-services-administration-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/data-model/general-services-administration-data-model.yml
  title: ''
  type: DataModel
  url: data-model/general-services-administration-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/finops/general-services-administration-finops.yml
  title: ''
  type: FinOps
  url: finops/general-services-administration-finops.yml
created: '2024-12-03'
description: The General Services Administration (GSA) provides workplaces by constructing, managing, and preserving government buildings and by leasing and managing commercial real estate. GSA acquisition solutions offer private sector professional services, equipment, supplies, and IT to government organizations and the military. GSA also promotes management best practices and efficient government operations through the development of governmentwide policies, including a broad portfolio of public APIs.
finops:
- name: General Services Administration Finops
  service_category: API
  slug: general-services-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/general-services-administration.png
layout: provider
mcp_servers:
- description: 'GSA''s Technology Transformation Services (GSA-TTS) is one of the few federal publishers shipping MCP servers, and two of them wrap GSA''s OWN APIs: the GSA Per Diem API and the Regulations.gov API. Bot'
  name: General Services Administration MCP Server
  slug: general-services-administration-mcp-server
modified: '2026-09-12'
name: General Services Administration
nav: Providers
network: true
overview: 'General Services Administration publishes 79 APIs on the [APIs.io](https://apis.io/) network, including Action API, Admin API, Admin Group API, and 76 more. Tagged areas include Federal-Government, Procurement, Acquisition, Open Data, and Government.


  General Services Administration''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 50 more developer resources.'
plans:
- name: General Services Administration Plans Pricing
  plan_count: 1
  slug: general-services-administration-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 8
  name: General Services Administration Rate Limits
  slug: general-services-administration-rate-limits
score:
  band: strong
  composite: 62.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 53.9
    developer_ergonomics: 66.1
    discoverability: 59.3
    operational_transparency: 60.5
  previous_composite: 62.2
  provenance:
    conformance: first-party
    contracts:
      callable: 36.8
      derived: 0
      marker_coverage: 0.0
      total: 79
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/screenshots/general-services-administration-2026-06-20T181728.png
security:
- kind: authentication
  name: General Services Administration Authentication
  slug: general-services-administration-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: General Services Administration Domain Security
  slug: general-services-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: General Services Administration Vulnerability Disclosure
  slug: general-services-administration-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: general-services-administration
tags:
- Federal-Government
- Procurement
- Acquisition
- Open Data
- Government
- SAM.gov
- Travel
- Analytics
- API Management
website: https://open.gsa.gov/api/
---
