---
aid: bureau-of-safety-and-environmental-enforcement
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-safety-and-environmental-enforcement/refs/heads/main/apis.yml
name: Bureau of Safety and Environmental Enforcement
tags:
  - Enforcement
  - Environment
  - Federal Government
  - Safety
  - Offshore
  - Oil and Gas
  - Wells
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-30'
modified: '2026-04-23'
position: Consumer
description: The Bureau of Safety and Environmental Enforcement (BSEE) works to promote safety, protect the environment, and conserve resources offshore through vigorous regulatory oversight and enforcement.
apis:
  - aid: bureau-of-safety-and-environmental-enforcement:bsee-well-api
    name: BSEE Well API Online Query
    tags:
      - Federal Government
      - Safety
      - Wells
      - Offshore
    humanURL: https://www.data.bsee.gov/well/api/default.aspx
    baseURL: https://www.bsee.gov/Well/API/
    properties:
      - url: https://www.data.bsee.gov/well/api/default.aspx
        type: Documentation
      - url: https://www.data.bsee.gov/
        type: Portal
      - url: https://catalog.data.gov/dataset?organization=bsee-gov
        type: DataAPI
    description: The BSEE Well API provides multiregional offshore well information retrieval across Alaska, Atlantic, Gulf of America, and Pacific regions. Query by API well number, company name, well status, field name, spud date, and other criteria. Returns well records with 18+ data fields.
    features:
      - Multiregional Well Search
      - API Well Number Lookup
      - Company Name Search
      - Well Status Filtering
      - Date Range Queries
      - CSV/XLS Export
      - PDF Export
    useCases:
      - Offshore well permitting research
      - Drilling activity analysis
      - Regulatory compliance verification
      - Environmental monitoring
  - aid: bureau-of-safety-and-environmental-enforcement:bsee-data-center
    name: BSEE Data Center
    tags:
      - Federal Government
      - Safety
      - Offshore
      - Oil and Gas
    humanURL: https://www.data.bsee.gov/
    properties:
      - url: https://www.data.bsee.gov/
        type: Portal
    description: The BSEE Data Center provides online query services and data downloads for offshore oil and gas operations. Data covers company information, leasing, pipelines, wells, production, platforms, and permitting across all OCS regions.
    features:
      - Company and Approval Data
      - Lease and Assignment Records
      - Pipeline Location and Permit Data
      - Well and Borehole Records
      - Production Data by Platform
      - Incident of Non-Compliance Records
      - ArcGIS Interactive Mapping
      - ASCII and Shapefile Downloads
    useCases:
      - Offshore lease research
      - Production monitoring
      - Pipeline safety oversight
      - Regulatory compliance tracking
      - Incident investigation
  - aid: bureau-of-safety-and-environmental-enforcement:tims-eplanning
    name: BSEE eWell Permitting System (TIMS)
    tags:
      - Federal Government
      - Safety
      - Permitting
    humanURL: https://timsweb.bsee.gov/
    properties:
      - url: https://timsweb.bsee.gov/
        type: Portal
    description: The Technical Information Management System (TIMS) / eWell system enables permit submissions and well activity reporting for offshore operations. Operators use this system to submit Applications for Permit to Drill (APD) and report well activities.
    features:
      - Permit Submission
      - Well Activity Reporting
      - Exploration Plan Submissions
      - Development Plan Submissions
    useCases:
      - Drilling permit applications
      - Well activity compliance reporting
      - Regulatory submission workflows
common:
  - type: Website
    url: https://www.bsee.gov/
  - type: Portal
    url: https://www.data.bsee.gov/
  - type: Privacy Policy
    url: https://www.bsee.gov/privacy-policy
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=bsee-gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
