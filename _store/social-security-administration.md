---
aid: social-security-administration
name: Social Security Administration
description: The Social Security Administration (SSA) is a U.S. federal agency that administers Social Security programs including retirement, disability (SSDI), and survivor benefits. SSA's Developer Support portal provides APIs for locating field offices and resident stations, accessing open data on OASDI beneficiary statistics, and verifying Social Security Numbers through the eCBSV program.
url: https://raw.githubusercontent.com/api-evangelist/social-security-administration/refs/heads/main/apis.yml
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-02'
position: Consuming
tags:
  - Federal Government
  - Social Security
  - Government API
  - Open Data
  - OASDI
  - Disability Benefits
  - Retirement Benefits
specificationVersion: '0.19'
apis:
  - aid: social-security-administration:field-office-address-api
    name: SSA Field Office Address API
    description: Provides location, address, telephone numbers, and office hours for Social Security Administration Field Offices across the United States. Uses the Esri ArcGIS Online platform as a RESTful Feature Service.
    humanURL: https://www.ssa.gov/developer/api/FO_Address_Data_AppDevs.htm
    tags:
      - Field Offices
      - Location Services
      - Government Data
      - Open Data
    properties:
      - type: Documentation
        url: https://www.ssa.gov/developer/api/FO_Address_Data_AppDevs.htm
      - type: OpenAPI
        url: openapi/ssa-field-office-openapi.yml
      - type: ArcGIS Feature Service
        url: https://services6.arcgis.com/zFiipv75rloRP5N4/ArcGIS/rest/services/Office_Points/FeatureServer/1
  - aid: social-security-administration:resident-station-address-api
    name: SSA Resident Station Address API
    description: Provides location, address, telephone numbers, and office hours for Social Security Administration Resident Stations — smaller SSA offices that serve rural communities. Uses the Esri ArcGIS Online platform as a RESTful Feature Service.
    humanURL: https://www.ssa.gov/developer/api/RS_Address_Data_AppDevs.htm
    tags:
      - Resident Stations
      - Location Services
      - Government Data
      - Open Data
    properties:
      - type: Documentation
        url: https://www.ssa.gov/developer/api/RS_Address_Data_AppDevs.htm
      - type: OpenAPI
        url: openapi/ssa-resident-station-openapi.yml
      - type: ArcGIS Feature Service
        url: https://services6.arcgis.com/zFiipv75rloRP5N4/arcgis/rest/services/SSA_Resident_Station_Information/FeatureServer
  - aid: social-security-administration:oasdi-data-api
    name: SSA OASDI Open Data API
    description: Provides statistics on Old Age, Survivors, and Disability Insurance (OASDI) beneficiaries including counts by state, total population data, and benefit payment statistics. Available through SSA's open data portal and Esri Feature Services.
    humanURL: https://www.ssa.gov/data/OASDIBeneficiariesbyState.htm
    tags:
      - OASDI
      - Beneficiary Statistics
      - Open Data
      - Benefits Data
    properties:
      - type: Documentation
        url: https://www.ssa.gov/data/OASDIBeneficiariesbyState.htm
      - type: Open Data Portal
        url: https://www.ssa.gov/data/
  - aid: social-security-administration:ecbsv-api
    name: SSA eCBSV Verification API
    description: The Electronic Consent Based SSN Verification (eCBSV) Service allows financial institutions to verify that a provided Social Security Number, name, and date of birth match SSA records, with consent from the individual. Access is restricted to eligible financial institutions.
    humanURL: https://www.ssa.gov/dataexchange/eCBSV/
    tags:
      - SSN Verification
      - Identity Verification
      - Financial Services
      - Consent Based
    properties:
      - type: Documentation
        url: https://www.ssa.gov/dataexchange/eCBSV/technical_information.html
      - type: CBSV Web Service
        url: https://www.ssa.gov/cbsv/webservice.html
common:
  - type: Website
    url: https://www.ssa.gov/
  - type: Developer Portal
    url: https://www.ssa.gov/developer/
  - type: Open Data Portal
    url: https://www.ssa.gov/data/
  - type: Open Data Inventory
    url: https://www.ssa.gov/data/Open-Data-Inventory-Information.html
  - type: Data.gov Organization
    url: https://catalog.data.gov/organization/ssa-gov
  - type: JSON Schema
    url: json-schema/ssa-field-office-schema.json
  - type: JSON Schema
    url: json-schema/ssa-resident-station-schema.json
  - type: JSON Structure
    url: json-structure/ssa-office-structure.json
  - type: JSON-LD Context
    url: json-ld/ssa-context.jsonld
  - type: Vocabulary
    url: vocabulary/ssa-vocabulary.yml
  - type: Examples
    url: examples/ssa-field-office-query-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
