---
aid: the-administration-for-children-and-families
name: The Administration for Children and Families
description: The Administration for Children and Families (ACF) is a division of the U.S. Department of Health and Human Services dedicated to promoting the economic and social well-being of children, families, and communities. ACF administers programs including TANF (cash assistance), CCDF (child care), Head Start, LIHEAP (energy assistance), child welfare, and refugee assistance. ACF collects administrative data via systems including AFCARS (foster care and adoption), NCANDS (child abuse and neglect), NYTD (youth in transition), TANF data reporting, and CCDF data. ACF is pursuing interoperability standards using HL7 FHIR and USCDI+ for human services data exchange. The TANF Data Portal (tanfdata.acf.hhs.gov) provides state agencies with a data submission and analysis interface.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Children
  - Families
  - Federal Government
  - Health And Human Services
  - Human Services
  - Social Safety Net
url: https://raw.githubusercontent.com/api-evangelist/the-administration-for-children-and-families/refs/heads/main/apis.yml
created: '2024-11-20T00:00:00.000Z'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: the-administration-for-children-and-families:tanf-data-portal
    name: TANF Data Portal
    description: The TANF Data Portal (TDP) is a secure, web-based data reporting system for state agencies to submit Temporary Assistance for Needy Families (TANF) program data to ACF. It provides data submission workflows, validation, and reporting capabilities. The system is built on a Django/React stack hosted on Cloud.gov.
    humanURL: https://tanfdata.acf.hhs.gov/
    baseURL: https://tanfdata.acf.hhs.gov/
    tags:
      - Federal Government
      - Human Services
      - TANF
    properties:
      - type: Documentation
        url: https://tanfdata.acf.hhs.gov/
      - type: GitHubRepository
        url: https://github.com/HHS/TANF-app
  - aid: the-administration-for-children-and-families:acf-interoperability
    name: ACF Human Services Interoperability Initiative
    description: ACF's initiative to develop interoperability standards for human services programs using HL7 FHIR and USCDI+ (United States Core Data for Interoperability Plus). Aims to enable data sharing between social services, health, and other human services systems to support integrated care coordination for children and families.
    humanURL: https://acf.gov/about/interoperability
    baseURL: https://acf.gov/
    tags:
      - FHIR
      - Federal Government
      - Human Services
      - Interoperability
    properties:
      - type: Documentation
        url: https://acf.gov/about/interoperability
  - aid: the-administration-for-children-and-families:ndacan
    name: National Data Archive on Child Abuse and Neglect
    description: NDACAN is the central repository for datasets related to child abuse, neglect, and child welfare at Cornell University, funded by ACF. Provides access to AFCARS (foster care/adoption), NCANDS (child abuse and neglect), and NYTD (youth in transition) datasets for research purposes. Includes data codebooks and user guides.
    humanURL: https://www.ndacan.acf.hhs.gov/
    baseURL: https://www.ndacan.acf.hhs.gov/
    tags:
      - Child Welfare
      - Data Archive
      - Federal Government
      - Research
    properties:
      - type: Documentation
        url: https://www.ndacan.acf.hhs.gov/
  - aid: the-administration-for-children-and-families:acf-data-research
    name: ACF Data and Research Portal
    description: ACF's primary data and research portal providing access to program data, statistical reports, and research findings across all ACF program offices. Includes TANF caseload data, CCDF data, Head Start program data, and child welfare statistics.
    humanURL: https://acf.gov/acf-data-research
    baseURL: https://acf.gov/
    tags:
      - Data
      - Federal Government
      - Research
      - Statistics
    properties:
      - type: Documentation
        url: https://acf.gov/acf-data-research
      - type: Dataset
        url: https://catalog.data.gov/organization/hhs-acf
common:
  - type: Website
    url: https://www.acf.hhs.gov/
  - type: Documentation
    url: https://acf.gov/acf-data-research
  - type: Data Portal
    url: https://tanfdata.acf.hhs.gov/
  - type: GitHub Organization
    url: https://github.com/HHS
  - type: Data Catalog
    url: https://catalog.data.gov/organization/hhs-acf
  - type: Interoperability
    url: https://acf.gov/about/interoperability
  - type: JSONSchema
    url: json-schema/acf-child-welfare-schema.json
  - type: JSONSchema
    url: json-schema/acf-tanf-schema.json
  - type: JSON-LD
    url: json-ld/acf-context.jsonld
  - type: Vocabulary
    url: vocabulary/acf-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
