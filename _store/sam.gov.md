---
aid: sam.gov
url: https://raw.githubusercontent.com/api-evangelist/sam.gov/refs/heads/main/apis.yml
name: SAM.gov
description: SAM.gov (System for Award Management) is the official US government system for vendor registration and federal procurement. Operated by the General Services Administration (GSA), SAM.gov consolidates multiple legacy acquisition systems and provides APIs for contract opportunities, entity management, federal hierarchy, and location validation services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Procurement
  - Contracts
  - Entity Management
  - Location Services
  - GSA
access: Public
created: '2024-03-29'
modified: '2026-05-02'
x-profiled: 2026-05
specificationVersion: '0.19'
apis:
  - aid: sam.gov:location-services-api
    name: SAM.gov Public Location Services API
    description: The Public Location Services API provides Location Services data (Country, State, City, and ZIP) for validating location data submitted to SAM.gov. Location Services State API supports both United States and Foreign Countries. Requires a valid SAM.gov System Account API key.
    humanURL: https://open.gsa.gov/api/location-public-api/
    tags:
      - Location Services
      - Validation
      - Government
      - GSA
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/location-public-api/
      - type: OpenAPI
        url: openapi/sam-gov-location-services-openapi.yml
  - aid: sam.gov:get-opportunities-api
    name: SAM.gov Get Opportunities Public API
    description: The Get Opportunities Public API provides all published contract opportunity details based on request parameters. Returns solicitation notices, awards, and pre-solicitations from SAM.gov. Rate limited to 1000 requests/day. Requires a SAM.gov API key.
    humanURL: https://open.gsa.gov/api/get-opportunities-public-api/
    tags:
      - Contract Opportunities
      - Procurement
      - Federal Contracts
      - Government
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/get-opportunities-public-api/
      - type: BaseURL
        url: https://api.sam.gov/prod/opportunities/v2/search
  - aid: sam.gov:opportunities-management-api
    name: SAM.gov Opportunity Management API
    description: The Opportunity Management API allows authorized users to programmatically submit, update, and manage contract opportunity notices in SAM.gov. Requires federal government or contractor system account authorization.
    humanURL: https://open.gsa.gov/api/opportunities-api/
    tags:
      - Contract Management
      - Procurement
      - Federal Contracts
      - Government
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/opportunities-api/
  - aid: sam.gov:entity-management-api
    name: SAM.gov Entity Management API
    description: The Entity Management API provides detailed entity (vendor/contractor) information from SAM.gov including registration status, hierarchy, security levels, points of contact, and certifications. Used to verify vendors eligible for federal contracts.
    humanURL: https://open.gsa.gov/api/entity-api/
    tags:
      - Entity Management
      - Vendor Registration
      - Federal Procurement
      - Government
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/entity-api/
  - aid: sam.gov:federal-hierarchy-public-api
    name: SAM.gov Federal Hierarchy Public API
    description: The Federal Hierarchy Public API allows non-federal users to retrieve Federal Organization details down to the office level. Used to look up agency and organizational hierarchy for federal procurement purposes.
    humanURL: https://open.gsa.gov/api/fh-public-api/
    tags:
      - Federal Hierarchy
      - Government Organization
      - Government
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/fh-public-api/
  - aid: sam.gov:contract-awards-api
    name: SAM.gov Contract Awards API
    description: The Contract Awards API provides access to federal contract award information from SAM.gov, including award details, vendor information, award amounts, and performance period data.
    humanURL: https://open.gsa.gov/api/contract-awards/
    tags:
      - Contract Awards
      - Federal Spending
      - Procurement
      - Government
    properties:
      - type: Documentation
        url: https://open.gsa.gov/api/contract-awards/
common:
  - type: Website
    url: https://sam.gov
  - type: Portal
    url: https://open.gsa.gov/api/
  - type: Documentation
    url: https://open.gsa.gov/api/
  - type: APIKey
    url: https://open.gsa.gov/api/get-opportunities-public-api/#getting-started
  - type: GitHub
    url: https://github.com/GSA
  - type: DataCatalog
    url: https://catalog.data.gov
  - type: Status
    url: https://sam.gov/status
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
