---
aid: centers-for-medicare-and-medicaid-services
url: https://raw.githubusercontent.com/api-evangelist/centers-for-medicare-and-medicaid-services/refs/heads/main/apis.yml
name: Centers for Medicare and Medicaid Services
tags:
  - BCDA
  - Blue Button
  - CMS
  - Claims
  - DPC
  - FHIR
  - Federal Government
  - Healthcare
  - Interoperability
  - Marketplace
  - Medicaid
  - Medicare
  - Open Data
  - Provider Data
  - Socrata
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: The Centers for Medicare and Medicaid Services (CMS) is the federal agency that provides health coverage to more than 160 million Americans through Medicare, Medicaid, the Children's Health Insurance Program (CHIP), and the Health Insurance Marketplace. CMS operates one of the largest public API programs in the U.S. government, including the FHIR-based Blue Button 2.0, Beneficiary Claims Data API (BCDA), and Data at the Point of Care (DPC); the data.cms.gov Socrata Open Data API covering Medicare claims, provider, and enrollment datasets; the Medicare Provider Data Catalog (Hospital Compare, Nursing Home Compare); the Healthcare.gov Marketplace API; NPPES and NPI Registry APIs; the QPP Measures API; and Medicaid Transformed Medicaid Statistical Information System (T-MSIS) resources.
apis:
  - aid: centers-for-medicare-and-medicaid-services:cms-blue-button-2
    name: CMS Blue Button 2.0 API
    tags:
      - Blue Button
      - Claims
      - FHIR
      - Medicare
      - OAuth 2.0
      - Patient Access
    humanURL: https://bluebutton.cms.gov/
    baseURL: https://api.bluebutton.cms.gov/v2/fhir/
    properties:
      - url: https://bluebutton.cms.gov/
        type: Website
      - url: https://bluebutton.cms.gov/developers/
        type: Developer
      - url: https://bluebutton.cms.gov/api-documentation/
        type: Documentation
      - url: https://sandbox.bluebutton.cms.gov/
        type: Sandbox
      - url: https://bluebutton.cms.gov/resources/
        type: Resources
    description: Blue Button 2.0 is a standards-based HL7 FHIR R4 API that delivers Medicare Part A, B, and D claims data for over 60 million beneficiaries to registered third-party applications, authorized by the beneficiary through OAuth 2.0. It anchors CMS's Patient Access API program under the 21st Century Cures Act.
  - aid: centers-for-medicare-and-medicaid-services:cms-bcda
    name: CMS Beneficiary Claims Data API (BCDA)
    tags:
      - ACO
      - BCDA
      - Bulk FHIR
      - Claims
      - Medicare
      - Shared Savings
    humanURL: https://bcda.cms.gov/
    baseURL: https://api.bcda.cms.gov/api/v2/
    properties:
      - url: https://bcda.cms.gov/
        type: Website
      - url: https://bcda.cms.gov/guide.html
        type: Documentation
      - url: https://sandbox.bcda.cms.gov/
        type: Sandbox
    description: The Beneficiary Claims Data API (BCDA) is a Bulk FHIR API that delivers Medicare Part A, B, and D claims data to Medicare Shared Savings Program ACOs, ACO REACH participants, and other Alternative Payment Model participants for their attributed and assignable beneficiaries.
  - aid: centers-for-medicare-and-medicaid-services:cms-dpc
    name: CMS Data at the Point of Care (DPC) API
    tags:
      - Bulk FHIR
      - Claims
      - FFS
      - Point of Care
      - Providers
    humanURL: https://dpc.cms.gov/
    baseURL: https://api.dpc.cms.gov/api/v1/
    properties:
      - url: https://dpc.cms.gov/
        type: Website
      - url: https://dpc.cms.gov/docs
        type: Documentation
      - url: https://sandbox.dpc.cms.gov/
        type: Sandbox
      - url: https://dpc.cms.gov/faq
        type: FAQ
    description: Data at the Point of Care is a FHIR Bulk Data API that delivers Original Medicare claims data to fee-for-service providers for the patients currently under their care, enabling clinicians to see a patient's full Medicare history at the point of care.
  - aid: centers-for-medicare-and-medicaid-services:cms-socrata-open-data
    name: CMS Socrata Open Data API (data.cms.gov)
    tags:
      - Datasets
      - Medicare
      - Open Data
      - Provider Data
      - SODA
      - Socrata
    humanURL: https://data.cms.gov/
    baseURL: https://data.cms.gov/data.json
    properties:
      - url: https://data.cms.gov/
        type: Website
      - url: https://data.cms.gov/provider-data/docs
        type: Documentation
      - url: https://developer.cms.gov/data-cms/
        type: Developer
      - url: https://data.cms.gov/data-api
        type: DataAPI
    description: data.cms.gov hosts hundreds of CMS datasets including Medicare Fee-for-Service utilization and payment data, Provider of Services files, Medicare Part B/D Prescriber summaries, Marketplace open enrollment data, and COVID-19 nursing home data, available via the data.cms.gov Data API (JSON) and the CMS Provider Data Catalog Socrata-compatible endpoints.
  - aid: centers-for-medicare-and-medicaid-services:cms-provider-data-catalog
    name: CMS Provider Data Catalog API (Care Compare)
    tags:
      - Care Compare
      - Dialysis Compare
      - Hospital Compare
      - Nursing Home Compare
      - Provider Data
      - Quality
    humanURL: https://data.cms.gov/provider-data/
    baseURL: https://data.cms.gov/provider-data/api/1/
    properties:
      - url: https://data.cms.gov/provider-data/
        type: Website
      - url: https://data.cms.gov/provider-data/docs
        type: Documentation
      - url: https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items
        type: Metastore
    description: The Provider Data Catalog API (formerly Hospital Compare) exposes the Medicare.gov Care Compare datasets including Hospital, Nursing Home, Home Health, Hospice, Physician, Long-Term Care Hospital, Inpatient Rehab, and Dialysis Facility quality measures as DCAT-based datasets with Datastore query endpoints.
  - aid: centers-for-medicare-and-medicaid-services:nppes-npi-registry
    name: NPPES NPI Registry API
    tags:
      - Credentialing
      - NPI
      - NPPES
      - Provider Identifier
      - Provider Registry
    humanURL: https://npiregistry.cms.hhs.gov/
    baseURL: https://npiregistry.cms.hhs.gov/api/
    properties:
      - url: https://npiregistry.cms.hhs.gov/
        type: Website
      - url: https://npiregistry.cms.hhs.gov/api-page
        type: Documentation
      - url: https://npiregistry.cms.hhs.gov/help-api/
        type: Help
    description: The NPPES NPI Registry API provides free public access to look up active National Provider Identifier records for individual and organizational healthcare providers, supporting FHIR-compatible JSON responses used widely in credentialing, directory, and claims validation workflows.
  - aid: centers-for-medicare-and-medicaid-services:healthcare-gov-marketplace
    name: Healthcare.gov Marketplace API
    tags:
      - ACA
      - Exchange
      - Marketplace
      - Plan Finder
      - QHP
    humanURL: https://www.healthcare.gov/developers/
    baseURL: https://marketplace.api.healthcare.gov/api/v1/
    properties:
      - url: https://www.healthcare.gov/developers/
        type: Developer
      - url: https://github.com/CMSgov/marketplace-api-examples
        type: Examples
      - url: https://data.healthcare.gov/
        type: OpenData
    description: The Healthcare.gov Marketplace API and accompanying Open Data Plan Finder exposes Qualified Health Plan (QHP) details, plan attributes, provider networks, and formularies for the Federally-Facilitated Marketplace states, enabling third-party plan comparison and enrollment experiences.
  - aid: centers-for-medicare-and-medicaid-services:qpp-measures-api
    name: CMS Quality Payment Program (QPP) Measures API
    tags:
      - MIPS
      - Measures
      - Quality
      - QPP
      - Value-Based
    humanURL: https://qpp.cms.gov/
    properties:
      - url: https://qpp.cms.gov/
        type: Website
      - url: https://cmsgov.github.io/qpp-measures-data/
        type: Documentation
      - url: https://github.com/CMSgov/qpp-measures-data
        type: SourceCode
    description: The Quality Payment Program Measures Data repository and REST API publish machine-readable specifications of MIPS quality, promoting interoperability, improvement activities, and cost measures for each performance year, supporting vendor QPP submissions and analytics.
  - aid: centers-for-medicare-and-medicaid-services:medicare-coverage-database
    name: Medicare Coverage Database (MCD) API
    tags:
      - Coverage
      - LCD
      - MAC
      - NCD
      - Policy
    humanURL: https://www.cms.gov/medicare-coverage-database/
    properties:
      - url: https://www.cms.gov/medicare-coverage-database/
        type: Website
      - url: https://www.cms.gov/medicare-coverage-database/downloads/downloads.aspx
        type: Downloads
    description: The Medicare Coverage Database publishes National Coverage Determinations (NCDs), Local Coverage Determinations (LCDs), articles, and coding guidance used to determine Medicare coverage and reimbursement policies, distributed via downloadable datasets and JSON/CSV query endpoints.
common:
  - type: Website
    url: https://www.cms.gov/
  - type: Developer
    url: https://developer.cms.gov/
  - type: OpenData
    url: https://data.cms.gov/
  - type: ProviderData
    url: https://data.cms.gov/provider-data/
  - type: BlueButton
    url: https://bluebutton.cms.gov/
  - type: BCDA
    url: https://bcda.cms.gov/
  - type: DPC
    url: https://dpc.cms.gov/
  - type: NPPES
    url: https://npiregistry.cms.hhs.gov/
  - type: Marketplace
    url: https://www.healthcare.gov/developers/
  - type: QPP
    url: https://qpp.cms.gov/
  - type: GitHubOrganization
    url: https://github.com/CMSgov
  - type: Privacy Policy
    url: https://www.cms.gov/privacy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
