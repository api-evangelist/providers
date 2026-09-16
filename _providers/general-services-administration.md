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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-09-15'
api_count: 32
apis:
- baseURL: https://api.gsa.gov/acquisitiongateway/api/v4.0
  baseurl_source: declared
  description: Provides programmatic access to acquisition gateway listings. Currently a placeholder; APIs are not yet available.
  name: Acquisition Gateway Listings API
  slug: acquisition-gateway-api
- baseURL: https://api.gsa.gov/analytics/dap/v2
  baseurl_source: declared
  description: 'The data for this API comes from Analytics.usa.gov, a unified Google Analytics account for U.S. federal government agencies known as the Digital Analytics Program (DAP). This program helps government '
  name: Analytics.usa.gov API
  slug: analytics-api
- baseURL: https://api.gsa.gov/operations/api-data-gov/v1
  baseurl_source: declared
  description: 'api.data.gov is a free API management service for federal agencies. The Admin API implements the API Umbrella Admin API and can be used by agency admins to perform admin operations and to query their '
  name: api.data.gov Admin API
  slug: api-datagov-admin-api
- baseURL: https://api.gsa.gov/operations/api-data-gov
  baseurl_source: declared
  description: Offers access to high level metrics for the APIs that use the api.data.gov shared service.
  name: api.data.gov Metrics API
  slug: api-datagov-metrics-api
- description: The CALC Labor Ceiling Rates tool is a pricing research tool located on buy.gsa.gov to support government acquisition professionals in services pricing business intelligence.
  name: Contract-Awarded Labor Category (CALC) API
  slug: calc-api
- baseURL: https://catalog.data.gov/api/3
  baseurl_source: declared
  description: The data.gov catalog is powered by CKAN, a powerful open source data platform that includes a robust API. The data.gov CKAN API contains metadata about datasets including URLs and descriptions.
  name: Data.gov CKAN API
  slug: datagov-ckan-api
- description: GSA Fleet provides leasing services for a wide variety of vehicle and fuel types for participating federal agencies with full-service leases at all-inclusive rates.
  name: GSA Fleet Vehicles / Vehicle Leasing
  slug: fleet-vehicles-api
- baseURL: /
  baseurl_source: spec
  description: The IT Collect API provides a way for the general public to access government-wide IT Portfolio Management and other related IT data sources, presented in a visual format on itdashboard.gov.
  name: IT Collect Public API
  slug: it-collect-api
- baseURL: https://api.gsa.gov/travel/perdiem/v2
  baseurl_source: declared
  description: GSA establishes the per diem reimbursement rates that federal agencies use to reimburse their employees for subsistence expenses incurred while on official travel within the continental United States.
  name: Per Diem API
  slug: per-diem-api
- baseURL: https://api.regulations.gov/v4
  baseurl_source: declared
  description: Regulations.gov is the place where users can find and comment on regulations. The APIs allow users to find creative ways to present regulatory data including documents, comments, and dockets.
  name: Regulations.gov API
  slug: regulationsgov-api
- baseURL: https://api.sam.gov/data-services/v1/extracts
  baseurl_source: declared
  description: The Extracts Download API allows users to request Unclassified (Public), Controlled Unclassified Information (CUI) For Official Use Only (FOUO) or CUI Sensitive entity extracts and Unclassified (Publi
  name: SAM.gov Entity/Exclusions Extracts Download API
  slug: samgov-entity-extracts-api
- baseURL: https://api.sam.gov/entity-information/v4
  baseurl_source: declared
  description: The Entity Management API allows users to request Unclassified (Public), Controlled Unclassified Information (CUI) For Official Use Only (FOUO) or CUI Sensitive entity data.
  name: SAM.gov Entity Management API
  slug: samgov-entity-management-api
- baseURL: https://api.sam.gov/entity-information/v4
  baseurl_source: declared
  description: The Exclusions API allows users to request Public Exclusion Information based on various optional request parameters. Responses are provided in JSON format with pagination.
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
- baseURL: https://api.sam.gov/prod/opportunity/v3
  baseurl_source: declared
  description: The Opportunity Management API allows authorized users to submit and request Opportunities data.
  name: SAM.gov Opportunity Management API
  slug: samgov-opportunity-management-api
- description: PSC API provides PSC data (PSC Code, PSC Name, PSC Full Name, Status, Parent PSC Code, Start Date, End Date and updated date) based on the request parameters with pagination support.
  name: SAM.gov Product Service Codes (PSC) API
  slug: samgov-psc-api
- description: The Public Location Services API provides Location Services data (Country, State, City, ZIP) for validating location data submitted to SAM.gov. Supports United States and, with GENC updates, Foreign C
  name: SAM.gov Public Location Services API
  slug: samgov-location-services-api
- baseURL: https://api.sam.gov/assistance-listings/v1
  baseurl_source: declared
  description: Provides federal assistance listings data through SAM.gov.
  name: SAM.gov Assistance Listings Public API
  slug: samgov-assistance-listings-api
- baseURL: https://api.sam.gov/contract/v1/subcontracts
  baseurl_source: declared
  description: Delivers federal subcontract data via SAM.gov.
  name: SAM.gov Acquisition Subaward Reporting Public API
  slug: samgov-acquisition-subaward-api
- baseURL: https://api.sam.gov/assistance/v1/subawards
  baseurl_source: declared
  description: Provides federal assistance subaward data via SAM.gov.
  name: SAM.gov Assistance Subaward Reporting Public API
  slug: samgov-assistance-subaward-api
- baseURL: https://api.sam.gov/contract-awards/v1
  baseurl_source: declared
  description: Retrieves contract listings with searchable parameters via SAM.gov.
  name: SAM.gov Contract Awards API
  slug: samgov-contract-awards-api
- baseURL: https://api-alpha.sam.gov/contract/v1/subcontracts
  baseurl_source: spec
  description: Publishes subcontract and subaward reports to SAM.gov.
  name: SAM.gov Subaward Reporting Bulk Upload API
  slug: samgov-bulkupload-api
- baseURL: https://api.gsa.gov/technology/searchgov/v2
  baseurl_source: declared
  description: The click tracking API endpoint lets you send click events to view click data on your Admin Click Analytics page and to strengthen the search results algorithm.
  name: Search.gov Clicks API
  slug: searchgov-clicks-api
- baseURL: https://api.gsa.gov/technology/searchgov/v2
  baseurl_source: declared
  description: Search.gov is a service of the General Services Administration providing search engine capability to federal agencies for their public websites.
  name: Search.gov Results API
  slug: searchgov-results-api
- description: 'Exposes the type-ahead suggestions that can appear below your search box as searchers enter their search terms. RETIRED: probed 2026-09-12 — https://open.gsa.gov/api/searchgov-suggestions/ and its Ope'
  name: Search.gov Type-Ahead Suggestions API
  slug: searchgov-suggestions-api
- baseURL: https://api.gsa.gov/technology/site-scanning/v1
  baseurl_source: declared
  description: Every day, the Site Scanning program runs a scanning engine to dynamically pull lists of domains from various sources and scan them with a collection of plugins to gather data on federal websites.
  name: Site Scanning API
  slug: site-scanning-api
- description: The Rate Query API offered by TMSS 2.0 is used to retrieve shipment cost for a regular Household Goods (HHG) shipment or for an Extended Storage (EXSTG) shipment for Federal Civilian Agencies.
  name: TMSS 2.0 Rate Query API
  slug: tmss-rate-query-api
- description: 'Offers sustainable guidance and tools for various roles via the Sustainable Facilities Tool (SFTool). RETIRED: probed 2026-09-12 — https://sftool.gov/developers returns HTTP 200 but serves a catch-all'
  name: Sustainable Facilities Tool API
  slug: sustainable-facilities-api
- baseURL: https://api.gsa.gov/analytics/touchpoints/v1
  baseurl_source: declared
  description: Programmatic access to customer feedback forms and responses managed via Touchpoints.
  name: Touchpoints API
  slug: touchpoints-api
- baseURL: https://api.sam.gov/spr/v1
  baseurl_source: declared
  description: The Subcontracting Plan Reports (SPR) API returns Individual Subcontracting Reports and Summary Subcontract Reports filed against federal subcontracting plans, searchable by contract, reporting period
  name: SAM.gov Subcontracting Plan Reporting Outbound API
  slug: samgov-spr-api
artifact_total: 39
common:
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
overview: 'General Services Administration publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Acquisition Gateway Listings API, Analytics.usa.gov API, api.data.gov Admin API, and 19 more. Tagged areas include Federal-Government, Procurement, Acquisition, Open Data, and Government.


  General Services Administration''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 28 more developer resources.'
plans:
- name: General Services Administration Plans Pricing
  plan_count: 1
  slug: general-services-administration-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 8
  name: General Services Administration Rate Limits
  slug: general-services-administration-rate-limits
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 58.0
    catalog_earned_first_party: 20.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 66.1
    discoverability: 64.8
    operational_transparency: 60.5
  previous_composite: 62.2
  provenance:
    conformance: first-party
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.22.0
  scored_at: '2026-09-15'
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
