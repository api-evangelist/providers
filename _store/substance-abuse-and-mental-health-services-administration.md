---
aid: substance-abuse-and-mental-health-services-administration
url: https://raw.githubusercontent.com/api-evangelist/substance-abuse-and-mental-health-services-administration/refs/heads/main/apis.yml
apis:
  - aid: substance-abuse-and-mental-health-services-administration:samhsa-treatment-locator-api
    name: SAMHSA Behavioral Health Treatment Services Locator API
    tags:
      - Treatment Facilities
      - Behavioral Health
      - Substance Use Disorders
      - Mental Health
      - Open Data
    humanURL: https://findtreatment.gov
    properties:
      - url: https://findtreatment.gov
        type: Documentation
      - url: https://www.samhsa.gov/find-help/national-helpline
        type: National Helpline
      - url: openapi/samhsa-treatment-locator-openapi.yml
        type: OpenAPI
    description: The SAMHSA Treatment Services Locator API provides searchable access to over 14,000 behavioral health treatment facilities across the United States. Search by location, service type, payment options (Medicaid, Medicare, sliding fee, free treatment), and population served. Powers the findtreatment.gov website.
  - aid: substance-abuse-and-mental-health-services-administration:samhsa-data-portal
    name: SAMHSA Data Portal
    tags:
      - Open Data
      - Survey Data
      - NSDUH
      - Statistics
      - Public Health
    humanURL: https://www.datafiles.samhsa.gov
    properties:
      - url: https://www.datafiles.samhsa.gov
        type: Documentation
      - url: https://www.samhsa.gov/data/
        type: Data Portal
      - url: https://pdas.samhsa.gov/sapt
        type: State Data
    description: SAMHSA's data portal provides access to national and state-level behavioral health statistics including the National Survey on Drug Use and Health (NSDUH), Treatment Episode Data Set (TEDS), and National Survey of Substance Abuse Treatment Services (N-SSATS). Data available for download in SAS, SPSS, and Stata formats.
  - aid: substance-abuse-and-mental-health-services-administration:samhsa-mental-health-atlas
    name: SAMHSA Mental Health Client Level Data
    tags:
      - Mental Health
      - Client Data
      - Statistics
      - Open Data
    humanURL: https://www.samhsa.gov/data/report/2020-mental-health-client-level-data-cld
    properties:
      - url: https://www.samhsa.gov/data/report/2020-mental-health-client-level-data-cld
        type: Documentation
    description: Client-Level Data (CLD) from state mental health agencies on clients receiving state-funded mental health services. Provides data on demographics, diagnoses, services received, and outcomes.
name: Substance Abuse and Mental Health Services Administration
tags:
  - Federal Government
  - Public Health
  - Behavioral Health
  - Substance Use Disorders
  - Mental Health
  - Open Data
  - Healthcare
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-02'
position: Consuming
description: The Substance Abuse and Mental Health Services Administration (SAMHSA) is a branch of the U.S. Department of Health and Human Services dedicated to improving the quality and availability of prevention, treatment, and recovery support services for individuals struggling with substance abuse and mental health disorders. SAMHSA provides APIs and open data for the behavioral health treatment services locator, national survey data (NSDUH), treatment episode statistics (TEDS), and state mental health data.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://www.samhsa.gov
    type: Website
  - url: https://findtreatment.gov
    type: Treatment Locator
  - url: https://www.samhsa.gov/data/
    type: Data Portal
  - url: https://www.datafiles.samhsa.gov
    type: Data Files
  - url: https://www.samhsa.gov/find-help/national-helpline
    type: National Helpline
  - url: https://988lifeline.org
    type: 988 Suicide & Crisis Lifeline
  - url: https://www.samhsa.gov/about-us/who-we-are/faq
    type: FAQ
  - url: https://www.samhsa.gov/data/terms-use
    type: Terms of Use
  - url: https://www.samhsa.gov/privacy
    type: Privacy Policy
  - url: https://github.com/samhsa
    type: GitHub Organization
  - url: https://catalog.data.gov/dataset?organization=samhsa-hhs
    type: Data.gov Catalog
  - url: https://api.data.gov/docs/samhsa/
    type: API Reference
  - url: vocabulary/samhsa-vocabulary.yml
    type: Vocabulary
  - url: json-ld/samhsa-context.jsonld
    type: JSON-LD Context
  - url: json-schema/samhsa-treatment-facility-schema.json
    type: JSON Schema
  - url: json-schema/samhsa-nsduh-data-schema.json
    type: JSON Schema
  - url: json-structure/samhsa-treatment-facility-structure.json
    type: JSON Structure
  - url: examples/samhsa-search-treatment-facilities-example.json
    type: Example
---
