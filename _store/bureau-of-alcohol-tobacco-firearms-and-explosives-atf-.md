---
aid: bureau-of-alcohol-tobacco-firearms-and-explosives-atf-
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-alcohol-tobacco-firearms-and-explosives-atf-/refs/heads/main/apis.yml
name: Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF)
tags:
  - Alcohol
  - Explosives
  - Federal Government
  - Firearms
  - Law Enforcement
  - Public Safety
  - Tobacco
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-04-21'
position: Consumer
description: ATF is a law enforcement agency in the United States Department of Justice that protects communities from violent criminals, criminal organizations, the illegal use and trafficking of firearms, the illegal use and storage of explosives, acts of arson and bombings, acts of terrorism, and the illegal diversion of alcohol and tobacco products. ATF publishes firearms trace data, crime statistics, and regulatory information.
apis:
  - aid: bureau-of-alcohol-tobacco-firearms-and-explosives-atf-:atf-firearms-trace-data
    name: ATF Firearms Trace Data
    tags:
      - Firearms
      - Federal Government
      - Law Enforcement
      - Public Safety
      - Statistics
    humanURL: https://www.atf.gov/firearms/docs/report/2022-firearms-trace-data-report/download
    properties:
      - url: https://www.atf.gov/firearms/firearms-trace-data-2022
        type: Documentation
      - url: https://catalog.data.gov/dataset?organization=atf-gov
        type: DataAPI
    description: ATF publishes annual firearms trace data reports covering the source and age of crime guns traced by law enforcement agencies across the United States. Data includes state-level statistics on firearms trafficking and recovery.
  - aid: bureau-of-alcohol-tobacco-firearms-and-explosives-atf-:atf-federal-firearms-licensee-listing
    name: ATF Federal Firearms Licensee (FFL) Listing
    tags:
      - Federal Firearms Licensees
      - Firearms
      - Federal Government
    humanURL: https://www.atf.gov/firearms/listing-federal-firearms-licensees
    baseURL: https://www.atf.gov/firearms/docs/report/
    properties:
      - url: https://www.atf.gov/firearms/listing-federal-firearms-licensees
        type: Documentation
      - url: https://www.atf.gov/firearms/docs/report/
        type: DataAPI
    description: ATF publishes listings of all active Federal Firearms Licensees (FFLs) by state. The data is available as downloadable files and can be accessed programmatically for compliance verification purposes.
common:
  - type: Website
    url: https://www.atf.gov/
  - type: Privacy Policy
    url: https://www.atf.gov/privacy-policy
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=atf-gov
  - type: Publications
    url: https://www.atf.gov/resource-center/publications
  - type: Statistics
    url: https://www.atf.gov/resource-center/data-statistics
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
