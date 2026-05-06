---
aid: bureau-of-justice-statistics
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-justice-statistics/refs/heads/main/apis.yml
name: Bureau of Justice Statistics
tags:
  - Crime
  - Federal Government
  - Justice
  - Statistics
  - Victimization
  - Recidivism
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-30'
modified: '2026-04-23'
position: Consumer
description: The Bureau of Justice Statistics (BJS) publishes information on crime, criminal offenders, victims of crime, and the operation of justice systems.
apis:
  - aid: bureau-of-justice-statistics:nibrs-national-estimates-api
    name: NIBRS National Estimates API
    tags:
      - Federal Government
      - Crime
      - Statistics
      - NIBRS
    humanURL: https://bjs.ojp.gov/national-incident-based-reporting-system-nibrs-national-estimates-api
    baseURL: https://api.ojp.gov/bjsdataset/v1/
    properties:
      - url: https://bjs.ojp.gov/national-incident-based-reporting-system-nibrs-national-estimates-api
        type: Documentation
      - url: https://catalog.data.gov/dataset?organization=ojp-gov
        type: DataAPI
    description: Provides access to national estimates derived from the FBI's National Incident-Based Reporting System (NIBRS). Includes violent and property incidents, offenses, victimization counts, percentages, and rates. No authentication required.
    features:
      - Violent Incident Data
      - Property Incident Data
      - Offense Data
      - Victimization Rates
      - Filterable by Demographics
      - JSON and CSV Formats
      - Pagination Support
    useCases:
      - Criminal justice policy research
      - Crime trend analysis
      - Academic study of offense patterns
      - Public safety planning
  - aid: bureau-of-justice-statistics:ncvs-api
    name: National Crime Victimization Survey (NCVS) API
    tags:
      - Federal Government
      - Victimization
      - Statistics
    humanURL: https://bjs.ojp.gov/national-crime-victimization-survey-ncvs-api
    baseURL: https://api.ojp.gov/bjsdataset/v1/
    properties:
      - url: https://bjs.ojp.gov/national-crime-victimization-survey-ncvs-api
        type: Documentation
    description: Provides access to victimization data from the National Crime Victimization Survey (NCVS), covering personal and household victimization data along with population estimates. No authentication required.
    features:
      - Personal Victimization Data
      - Household Victimization Data
      - Population Estimates
      - JSON and CSV Formats
      - Filterable by Year
    useCases:
      - Victimization research
      - Policy development
      - Trend analysis over time
      - Comparative household and personal crime studies
  - aid: bureau-of-justice-statistics:bjs-data-analysis-tools
    name: BJS Data Analysis Tools
    tags:
      - Federal Government
      - Statistics
      - Dashboards
    humanURL: https://bjs.ojp.gov/data/data-analysis-tools
    properties:
      - url: https://bjs.ojp.gov/data/data-analysis-tools
        type: Documentation
      - url: https://learcat.bjs.ojp.gov/
        type: Tool
      - url: https://bjs.ojp.gov/recidivism-patterns-explorer
        type: Tool
      - url: https://fccps.bjs.ojp.gov/
        type: Tool
      - url: https://csat.bjs.ojp.gov/
        type: Tool
      - url: https://bjs.ojp.gov/jeet
        type: Tool
      - url: https://ncvs.bjs.ojp.gov/Home
        type: Tool
    description: A suite of interactive web-based data tools providing access to BJS statistical data on crime, corrections, courts, law enforcement, and victimization. Tools include LEARCAT (law enforcement agency crime data), Recidivism Patterns Explorer, Federal Criminal Case Processing Statistics, and NCVS Dashboard.
    features:
      - Law Enforcement Crime Data (LEARCAT)
      - Recidivism Analysis
      - Federal Criminal Case Processing
      - Corrections Statistical Analysis
      - Justice Expenditure Data
      - Parole and Probation Dashboards
    useCases:
      - Criminal justice research
      - Recidivism policy analysis
      - Justice system spending analysis
      - Interactive data exploration
common:
  - type: Website
    url: https://bjs.ojp.gov/
  - type: Portal
    url: https://bjs.ojp.gov/data
  - type: Privacy Policy
    url: https://bjs.ojp.gov/legal/privacy-policy
  - type: Data Collections
    url: https://bjs.ojp.gov/data-collections/search
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=ojp-gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
