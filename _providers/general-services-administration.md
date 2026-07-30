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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 31
apis:
- description: Provides programmatic access to acquisition gateway listings. Currently a placeholder; APIs are not yet available.
  name: Acquisition Gateway Listings API
  slug: acquisition-gateway-api
- description: 'The data for this API comes from Analytics.usa.gov, a unified Google Analytics account for U.S. federal government agencies known as the Digital Analytics Program (DAP). This program helps government '
  name: Analytics.usa.gov API
  slug: analytics-api
- description: 'api.data.gov is a free API management service for federal agencies. The Admin API implements the API Umbrella Admin API and can be used by agency admins to perform admin operations and to query their '
  name: api.data.gov Admin API
  slug: api-datagov-admin-api
- description: Offers access to high level metrics for the APIs that use the api.data.gov shared service.
  name: api.data.gov Metrics API
  slug: api-datagov-metrics-api
- description: The CALC Labor Ceiling Rates tool is a pricing research tool located on buy.gsa.gov to support government acquisition professionals in services pricing business intelligence.
  name: Contract-Awarded Labor Category (CALC) API
  slug: calc-api
- description: The data.gov catalog is powered by CKAN, a powerful open source data platform that includes a robust API. The data.gov CKAN API contains metadata about datasets including URLs and descriptions.
  name: Data.gov CKAN API
  slug: datagov-ckan-api
- description: GSA Fleet provides leasing services for a wide variety of vehicle and fuel types for participating federal agencies with full-service leases at all-inclusive rates.
  name: GSA Fleet Vehicles / Vehicle Leasing
  slug: fleet-vehicles-api
- description: The IT Collect API provides a way for the general public to access government-wide IT Portfolio Management and other related IT data sources, presented in a visual format on itdashboard.gov.
  name: IT Collect Public API
  slug: it-collect-api
- description: GSA establishes the per diem reimbursement rates that federal agencies use to reimburse their employees for subsistence expenses incurred while on official travel within the continental United States.
  name: Per Diem API
  slug: per-diem-api
- description: Regulations.gov is the place where users can find and comment on regulations. The APIs allow users to find creative ways to present regulatory data including documents, comments, and dockets.
  name: Regulations.gov API
  slug: regulationsgov-api
- description: The Extracts Download API allows users to request Unclassified (Public), Controlled Unclassified Information (CUI) For Official Use Only (FOUO) or CUI Sensitive entity extracts and Unclassified (Publi
  name: SAM.gov Entity/Exclusions Extracts Download API
  slug: samgov-entity-extracts-api
- description: The Entity Management API allows users to request Unclassified (Public), Controlled Unclassified Information (CUI) For Official Use Only (FOUO) or CUI Sensitive entity data.
  name: SAM.gov Entity Management API
  slug: samgov-entity-management-api
- description: The Exclusions API allows users to request Public Exclusion Information based on various optional request parameters. Responses are provided in JSON format with pagination.
  name: SAM.gov Exclusions API
  slug: samgov-exclusions-api
- description: The Federal Hierarchy For Official Use Only (FOUO) API allows U.S. Government users to obtain Federal Organization details down to the office level.
  name: SAM.gov Federal Hierarchy FOUO API
  slug: samgov-fh-fouo-api
- description: Federal Hierarchy public API allows non-federal users to obtain Federal Organization details (Departments/Ind. Agency and SubTier).
  name: SAM.gov Federal Hierarchy Public API
  slug: samgov-fh-public-api
- description: Get Opportunities API provides all the published opportunity details based on the request parameters. This API requires pagination.
  name: SAM.gov Get Opportunities Public API
  slug: samgov-get-opportunities-api
- description: The Opportunity Management API allows authorized users to submit and request Opportunities data.
  name: SAM.gov Opportunity Management API
  slug: samgov-opportunity-management-api
- description: PSC API provides PSC data (PSC Code, PSC Name, PSC Full Name, Status, Parent PSC Code, Start Date, End Date and updated date) based on the request parameters with pagination support.
  name: SAM.gov Product Service Codes (PSC) API
  slug: samgov-psc-api
- description: The Public Location Services API provides Location Services data (Country, State, City, ZIP) for validating location data submitted to SAM.gov. Supports United States and, with GENC updates, Foreign C
  name: SAM.gov Public Location Services API
  slug: samgov-location-services-api
- description: Provides federal assistance listings data through SAM.gov.
  name: SAM.gov Assistance Listings Public API
  slug: samgov-assistance-listings-api
- description: Delivers federal subcontract data via SAM.gov.
  name: SAM.gov Acquisition Subaward Reporting Public API
  slug: samgov-acquisition-subaward-api
- description: Provides federal assistance subaward data via SAM.gov.
  name: SAM.gov Assistance Subaward Reporting Public API
  slug: samgov-assistance-subaward-api
- description: Retrieves contract listings with searchable parameters via SAM.gov.
  name: SAM.gov Contract Awards API
  slug: samgov-contract-awards-api
- description: Publishes subcontract and subaward reports to SAM.gov.
  name: SAM.gov Subaward Reporting Bulk Upload API
  slug: samgov-bulkupload-api
- description: The click tracking API endpoint lets you send click events to view click data on your Admin Click Analytics page and to strengthen the search results algorithm.
  name: Search.gov Clicks API
  slug: searchgov-clicks-api
- description: Search.gov is a service of the General Services Administration providing search engine capability to federal agencies for their public websites.
  name: Search.gov Results API
  slug: searchgov-results-api
- description: Exposes the type-ahead suggestions that can appear below your search box as searchers enter their search terms.
  name: Search.gov Type-Ahead Suggestions API
  slug: searchgov-suggestions-api
- description: Every day, the Site Scanning program runs a scanning engine to dynamically pull lists of domains from various sources and scan them with a collection of plugins to gather data on federal websites.
  name: Site Scanning API
  slug: site-scanning-api
- description: The Rate Query API offered by TMSS 2.0 is used to retrieve shipment cost for a regular Household Goods (HHG) shipment or for an Extended Storage (EXSTG) shipment for Federal Civilian Agencies.
  name: TMSS 2.0 Rate Query API
  slug: tmss-rate-query-api
- description: Offers sustainable guidance and tools for various roles via the Sustainable Facilities Tool (SFTool).
  name: Sustainable Facilities Tool API
  slug: sustainable-facilities-api
- description: Programmatic access to customer feedback forms and responses managed via Touchpoints.
  name: Touchpoints API
  slug: touchpoints-api
artifact_total: 36
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/general-services-administration-vulnerability-disclosure.yml
- group: auth
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
created: '2024-12-03'
description: The General Services Administration (GSA) provides workplaces by constructing, managing, and preserving government buildings and by leasing and managing commercial real estate. GSA acquisition solutions offer private sector professional services, equipment, supplies, and IT to government organizations and the military. GSA also promotes management best practices and efficient government operations through the development of governmentwide policies, including a broad portfolio of public APIs.
finops:
- name: General Services Administration Finops
  service_category: API
  slug: general-services-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/general-services-administration.png
layout: provider
modified: '2026-04-28'
name: General Services Administration
nav: Providers
network: true
overview: 'General Services Administration publishes 31 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Procurement, Acquisition, and Open Data.


  General Services Administration''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: General Services Administration Plans Pricing
  plan_count: 3
  slug: general-services-administration-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: General Services Administration Rate Limits
  slug: general-services-administration-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 22.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/screenshots/general-services-administration-2026-06-20T181728.png
security:
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
- Federal Government
- Procurement
- Acquisition
- Open Data
website: https://open.gsa.gov/api/
---
