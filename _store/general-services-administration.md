---
aid: general-services-administration
name: General Services Administration
description: The General Services Administration (GSA) provides workplaces by constructing, managing, and preserving government buildings and by leasing and managing commercial real estate. GSA acquisition solutions offer private sector professional services, equipment, supplies, and IT to government organizations and the military. GSA also promotes management best practices and efficient government operations through the development of governmentwide policies, including a broad portfolio of public APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Federal Government
  - Procurement
  - Acquisition
  - Open Data
url: https://raw.githubusercontent.com/api-evangelist/general-services-administration/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: general-services-administration:acquisition-gateway-api
    name: Acquisition Gateway Listings API
    description: Provides programmatic access to acquisition gateway listings. Currently a placeholder; APIs are not yet available.
    humanURL: https://open.gsa.gov/api/ag-api/
    tags:
      - Acquisition
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/ag-api/
  - aid: general-services-administration:analytics-api
    name: Analytics.usa.gov API
    description: The data for this API comes from Analytics.usa.gov, a unified Google Analytics account for U.S. federal government agencies known as the Digital Analytics Program (DAP). This program helps government agencies understand how people find, access, and use government services online.
    humanURL: https://open.gsa.gov/api/dap/
    tags:
      - Analytics
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/dap/
  - aid: general-services-administration:api-datagov-admin-api
    name: api.data.gov Admin API
    description: api.data.gov is a free API management service for federal agencies. The Admin API implements the API Umbrella Admin API and can be used by agency admins to perform admin operations and to query their API analytics.
    humanURL: https://open.gsa.gov/api/apidatagov/
    tags:
      - API Management
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/apidatagov/
  - aid: general-services-administration:api-datagov-metrics-api
    name: api.data.gov Metrics API
    description: Offers access to high level metrics for the APIs that use the api.data.gov shared service.
    humanURL: https://open.gsa.gov/api/apidatagov-metrics/
    tags:
      - API Management
      - Metrics
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/apidatagov-metrics/
  - aid: general-services-administration:calc-api
    name: Contract-Awarded Labor Category (CALC) API
    description: The CALC Labor Ceiling Rates tool is a pricing research tool located on buy.gsa.gov to support government acquisition professionals in services pricing business intelligence.
    humanURL: https://open.gsa.gov/api/dx-calc-api/
    tags:
      - Acquisition
      - Pricing
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/dx-calc-api/
  - aid: general-services-administration:datagov-ckan-api
    name: Data.gov CKAN API
    description: The data.gov catalog is powered by CKAN, a powerful open source data platform that includes a robust API. The data.gov CKAN API contains metadata about datasets including URLs and descriptions.
    humanURL: https://open.gsa.gov/api/datadotgov/
    tags:
      - Open Data
      - Catalog
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/datadotgov/
  - aid: general-services-administration:fleet-vehicles-api
    name: GSA Fleet Vehicles / Vehicle Leasing
    description: GSA Fleet provides leasing services for a wide variety of vehicle and fuel types for participating federal agencies with full-service leases at all-inclusive rates.
    humanURL: https://www.gsa.gov/buy-through-us/products-and-services/transportation-and-logistics-services/fleet-management/vehicle-leasing
    tags:
      - Fleet
      - Vehicles
    properties:
      - type: Documentation
        url: https://www.gsa.gov/buy-through-us/products-and-services/transportation-and-logistics-services/fleet-management/vehicle-leasing
  - aid: general-services-administration:it-collect-api
    name: IT Collect Public API
    description: The IT Collect API provides a way for the general public to access government-wide IT Portfolio Management and other related IT data sources, presented in a visual format on itdashboard.gov.
    humanURL: https://open.gsa.gov/api/itcollect/
    tags:
      - IT
      - Open Data
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/itcollect/
  - aid: general-services-administration:per-diem-api
    name: Per Diem API
    description: GSA establishes the per diem reimbursement rates that federal agencies use to reimburse their employees for subsistence expenses incurred while on official travel within the continental United States. Includes lodging, meals, and incidental expenses.
    humanURL: https://open.gsa.gov/api/perdiem/
    tags:
      - Travel
      - Reimbursement
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/perdiem/
  - aid: general-services-administration:regulationsgov-api
    name: Regulations.gov API
    description: Regulations.gov is the place where users can find and comment on regulations. The APIs allow users to find creative ways to present regulatory data including documents, comments, and dockets.
    humanURL: https://open.gsa.gov/api/regulationsgov/
    tags:
      - Regulations
      - Open Government
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/regulationsgov/
  - aid: general-services-administration:samgov-entity-extracts-api
    name: SAM.gov Entity/Exclusions Extracts Download API
    description: The Extracts Download API allows users to request Unclassified (Public), Controlled Unclassified Information (CUI) For Official Use Only (FOUO) or CUI Sensitive entity extracts and Unclassified (Public) exclusion extracts.
    humanURL: https://open.gsa.gov/api/sam-entity-extracts-api/
    tags:
      - SAM.gov
      - Procurement
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/sam-entity-extracts-api/
  - aid: general-services-administration:samgov-entity-management-api
    name: SAM.gov Entity Management API
    description: The Entity Management API allows users to request Unclassified (Public), Controlled Unclassified Information (CUI) For Official Use Only (FOUO) or CUI Sensitive entity data.
    humanURL: https://open.gsa.gov/api/entity-api/
    tags:
      - SAM.gov
      - Procurement
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/entity-api/
  - aid: general-services-administration:samgov-exclusions-api
    name: SAM.gov Exclusions API
    description: The Exclusions API allows users to request Public Exclusion Information based on various optional request parameters. Responses are provided in JSON format with pagination.
    humanURL: https://open.gsa.gov/api/exclusions-api/
    tags:
      - SAM.gov
      - Procurement
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/exclusions-api/
  - aid: general-services-administration:samgov-fh-fouo-api
    name: SAM.gov Federal Hierarchy FOUO API
    description: The Federal Hierarchy For Official Use Only (FOUO) API allows U.S. Government users to obtain Federal Organization details down to the office level.
    humanURL: https://open.gsa.gov/api/fh-fouo-api/
    tags:
      - SAM.gov
      - Federal Hierarchy
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/fh-fouo-api/
  - aid: general-services-administration:samgov-fh-public-api
    name: SAM.gov Federal Hierarchy Public API
    description: Federal Hierarchy public API allows non-federal users to obtain Federal Organization details (Departments/Ind. Agency and SubTier).
    humanURL: https://open.gsa.gov/api/fh-public-api/
    tags:
      - SAM.gov
      - Federal Hierarchy
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/fh-public-api/
  - aid: general-services-administration:samgov-get-opportunities-api
    name: SAM.gov Get Opportunities Public API
    description: Get Opportunities API provides all the published opportunity details based on the request parameters. This API requires pagination.
    humanURL: https://open.gsa.gov/api/get-opportunities-public-api/
    tags:
      - SAM.gov
      - Opportunities
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/get-opportunities-public-api/
  - aid: general-services-administration:samgov-opportunity-management-api
    name: SAM.gov Opportunity Management API
    description: The Opportunity Management API allows authorized users to submit and request Opportunities data.
    humanURL: https://open.gsa.gov/api/opportunities-api/
    tags:
      - SAM.gov
      - Opportunities
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/opportunities-api/
  - aid: general-services-administration:samgov-psc-api
    name: SAM.gov Product Service Codes (PSC) API
    description: PSC API provides PSC data (PSC Code, PSC Name, PSC Full Name, Status, Parent PSC Code, Start Date, End Date and updated date) based on the request parameters with pagination support.
    humanURL: https://open.gsa.gov/api/PSC-Public-API/
    tags:
      - SAM.gov
      - Reference Data
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/PSC-Public-API/
  - aid: general-services-administration:samgov-location-services-api
    name: SAM.gov Public Location Services API
    description: The Public Location Services API provides Location Services data (Country, State, City, ZIP) for validating location data submitted to SAM.gov. Supports United States and, with GENC updates, Foreign Countries.
    humanURL: https://open.gsa.gov/api/location-public-api/
    tags:
      - SAM.gov
      - Reference Data
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/location-public-api/
  - aid: general-services-administration:samgov-assistance-listings-api
    name: SAM.gov Assistance Listings Public API
    description: Provides federal assistance listings data through SAM.gov.
    humanURL: https://open.gsa.gov/api/assistance-listings-api/
    tags:
      - SAM.gov
      - Assistance
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/assistance-listings-api/
  - aid: general-services-administration:samgov-acquisition-subaward-api
    name: SAM.gov Acquisition Subaward Reporting Public API
    description: Delivers federal subcontract data via SAM.gov.
    humanURL: https://open.gsa.gov/api/acquisition-subaward-reporting-api/
    tags:
      - SAM.gov
      - Procurement
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/acquisition-subaward-reporting-api/
  - aid: general-services-administration:samgov-assistance-subaward-api
    name: SAM.gov Assistance Subaward Reporting Public API
    description: Provides federal assistance subaward data via SAM.gov.
    humanURL: https://open.gsa.gov/api/assistance-subaward-reporting-api/
    tags:
      - SAM.gov
      - Assistance
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/assistance-subaward-reporting-api/
  - aid: general-services-administration:samgov-contract-awards-api
    name: SAM.gov Contract Awards API
    description: Retrieves contract listings with searchable parameters via SAM.gov.
    humanURL: https://open.gsa.gov/api/contract-awards/
    tags:
      - SAM.gov
      - Procurement
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/contract-awards/
  - aid: general-services-administration:samgov-bulkupload-api
    name: SAM.gov Subaward Reporting Bulk Upload API
    description: Publishes subcontract and subaward reports to SAM.gov.
    humanURL: https://open.gsa.gov/api/subawards-bulkupload-api/
    tags:
      - SAM.gov
      - Procurement
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/subawards-bulkupload-api/
  - aid: general-services-administration:searchgov-clicks-api
    name: Search.gov Clicks API
    description: The click tracking API endpoint lets you send click events to view click data on your Admin Click Analytics page and to strengthen the search results algorithm.
    humanURL: https://open.gsa.gov/api/searchgov-clicks/
    tags:
      - Search
      - Analytics
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/searchgov-clicks/
  - aid: general-services-administration:searchgov-results-api
    name: Search.gov Results API
    description: Search.gov is a service of the General Services Administration providing search engine capability to federal agencies for their public websites.
    humanURL: https://open.gsa.gov/api/searchgov-results/
    tags:
      - Search
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/searchgov-results/
  - aid: general-services-administration:searchgov-suggestions-api
    name: Search.gov Type-Ahead Suggestions API
    description: Exposes the type-ahead suggestions that can appear below your search box as searchers enter their search terms.
    humanURL: https://open.gsa.gov/api/searchgov-suggestions/
    tags:
      - Search
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/searchgov-suggestions/
  - aid: general-services-administration:site-scanning-api
    name: Site Scanning API
    description: Every day, the Site Scanning program runs a scanning engine to dynamically pull lists of domains from various sources and scan them with a collection of plugins to gather data on federal websites.
    humanURL: https://open.gsa.gov/api/site-scanning-api/
    tags:
      - Federal Websites
      - Scanning
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/site-scanning-api/
  - aid: general-services-administration:tmss-rate-query-api
    name: TMSS 2.0 Rate Query API
    description: The Rate Query API offered by TMSS 2.0 is used to retrieve shipment cost for a regular Household Goods (HHG) shipment or for an Extended Storage (EXSTG) shipment for Federal Civilian Agencies.
    humanURL: https://open.gsa.gov/api/ratequeryhhg/
    tags:
      - Logistics
      - Shipping
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/ratequeryhhg/
  - aid: general-services-administration:sustainable-facilities-api
    name: Sustainable Facilities Tool API
    description: Offers sustainable guidance and tools for various roles via the Sustainable Facilities Tool (SFTool).
    humanURL: https://sftool.gov/developers
    tags:
      - Sustainability
      - Facilities
    properties:
      - type: Documentation
        url: https://sftool.gov/developers
  - aid: general-services-administration:touchpoints-api
    name: Touchpoints API
    description: Programmatic access to customer feedback forms and responses managed via Touchpoints.
    humanURL: https://github.com/gsa/touchpoints/wiki/API
    tags:
      - Feedback
      - Customer Experience
    properties:
      - type: Documentation
        url: https://github.com/gsa/touchpoints/wiki/API
common:
  - type: Website
    url: https://open.gsa.gov/api/
  - type: Documentation
    url: https://open.gsa.gov/api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
