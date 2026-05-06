---
aid: centers-for-disease-control-and-prevention
url: https://raw.githubusercontent.com/api-evangelist/centers-for-disease-control-and-prevention/refs/heads/main/apis.yml
name: Centers for Disease Control and Prevention
tags:
  - CDC
  - Environmental Health
  - Epidemiology
  - Federal Government
  - Healthcare
  - Open Data
  - Public Health
  - Socrata
  - Surveillance
  - WONDER
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: The Centers for Disease Control and Prevention (CDC) is the United States' national public health agency, part of the Department of Health and Human Services. CDC operates a broad portfolio of public APIs and open data services including the Socrata-powered data.cdc.gov (Open Data API for hundreds of COVID-19, chronic disease, environmental health, immunization, injury, and mortality datasets), the WONDER online query databases for mortality, natality, and cancer statistics, the PLACES / BRFSS and Environmental Public Health Tracking Network APIs, the Content Syndication platform, and the open.cdc.gov developer portal that indexes these resources for civic technologists and public-health researchers.
apis:
  - aid: centers-for-disease-control-and-prevention:cdc-socrata-open-data-api
    name: CDC Socrata Open Data API (data.cdc.gov)
    tags:
      - Chronic Disease
      - COVID-19
      - Datasets
      - Open Data
      - SODA
      - Socrata
      - Surveillance
    humanURL: https://data.cdc.gov/
    baseURL: https://data.cdc.gov/resource/
    properties:
      - url: https://data.cdc.gov/
        type: Website
      - url: https://dev.socrata.com/
        type: Documentation
      - url: https://dev.socrata.com/docs/endpoints.html
        type: Reference
      - url: https://dev.socrata.com/consumers/getting-started.html
        type: GettingStarted
      - url: https://evergreen.data.socrata.com/signup
        type: SignUp
    description: The CDC Socrata Open Data API (SODA) provides programmatic JSON, CSV, and GeoJSON access to hundreds of data.cdc.gov datasets covering COVID-19 case surveillance, vaccination coverage, excess deaths, flu surveillance, PRAMStat, PLACES small-area estimates, environmental public health tracking, and chronic disease indicators. Supports SoQL filtering, aggregation, pagination, and authenticated app tokens for higher rate limits.
  - aid: centers-for-disease-control-and-prevention:cdc-wonder-api
    name: CDC WONDER API
    tags:
      - Cancer
      - Mortality
      - Natality
      - Query Database
      - Statistics
    humanURL: https://wonder.cdc.gov/
    baseURL: https://wonder.cdc.gov/controller/datarequest/
    properties:
      - url: https://wonder.cdc.gov/
        type: Website
      - url: https://wonder.cdc.gov/wonder/help/WONDER-API.html
        type: Documentation
      - url: https://wonder.cdc.gov/wonder/help/faq.html
        type: FAQ
    description: CDC WONDER (Wide-ranging ONline Data for Epidemiologic Research) is a suite of public-use ad-hoc query databases covering underlying and multiple cause of death, natality, cancer statistics, tuberculosis, STDs, vaccine adverse events, and environmental health indicators. WONDER exposes an XML-based HTTP API that accepts parameter documents and returns aggregate statistics suitable for epidemiologic research.
  - aid: centers-for-disease-control-and-prevention:cdc-places-api
    name: CDC PLACES / 500 Cities API
    tags:
      - BRFSS
      - Census Tract
      - Chronic Disease
      - Health Indicators
      - Small Area Estimation
    humanURL: https://www.cdc.gov/places/
    baseURL: https://chronicdata.cdc.gov/resource/
    properties:
      - url: https://www.cdc.gov/places/
        type: Website
      - url: https://www.cdc.gov/places/methodology/
        type: Methodology
      - url: https://chronicdata.cdc.gov/
        type: OpenData
    description: PLACES (Population Level Analysis and Community Estimates) provides model-based small-area estimates for chronic disease risk factors, health outcomes, and prevention practices for counties, ZCTAs, census tracts, and places across the United States. Data is available via the Socrata chronicdata.cdc.gov portal as JSON, CSV, and GeoJSON endpoints.
  - aid: centers-for-disease-control-and-prevention:cdc-ephtn-api
    name: CDC Environmental Public Health Tracking Network API
    tags:
      - Air Quality
      - Environmental Health
      - Exposure
      - GIS
      - Water Quality
    humanURL: https://ephtracking.cdc.gov/apihelp
    baseURL: https://ephtracking.cdc.gov:443/apigateway/api/v1
    properties:
      - url: https://ephtracking.cdc.gov/
        type: Website
      - url: https://ephtracking.cdc.gov/apihelp
        type: Documentation
      - url: https://ephtracking.cdc.gov/DataExplorer/
        type: Explorer
    description: The Environmental Public Health Tracking Network API provides a REST interface over the National Tracking Network's JSON-formatted data for air quality, water quality, climate and health, childhood lead poisoning, asthma, cancer, and other environmental health indicators at national, state, and county levels.
  - aid: centers-for-disease-control-and-prevention:cdc-content-syndication
    name: CDC Public Health Media Library (Content Syndication)
    tags:
      - Content Syndication
      - Health Content
      - Media
      - Multimedia
    humanURL: https://tools.cdc.gov/medialibrary/
    properties:
      - url: https://tools.cdc.gov/medialibrary/
        type: Website
      - url: https://tools.cdc.gov/api/v2/resources/media
        type: Reference
      - url: https://tools.cdc.gov/api/docs/info.aspx
        type: Documentation
    description: The CDC Public Health Media Library Content Syndication API lets developers and partner sites programmatically retrieve CDC health content (articles, infographics, videos, widgets, images, and microsites) in multiple formats to embed on third-party properties with automatic update propagation.
  - aid: centers-for-disease-control-and-prevention:open-cdc-apis-index
    name: CDC Open Technology API Index
    tags:
      - Developer Portal
      - Directory
      - Open Technology
    humanURL: https://open.cdc.gov/apis.html
    properties:
      - url: https://open.cdc.gov/apis.html
        type: Website
      - url: https://open.cdc.gov/
        type: Portal
      - url: https://github.com/CDCgov
        type: GitHubOrganization
    description: open.cdc.gov is CDC's Open Technology landing site that indexes the agency's public APIs, open-source GitHub repositories, and open data assets, serving as a catalog entry point for developers seeking CDC interfaces across programs and centers.
  - aid: centers-for-disease-control-and-prevention:cdc-tb-nndss-socrata
    name: CDC NNDSS / MMWR Socrata Data
    tags:
      - MMWR
      - NNDSS
      - Notifiable Disease
      - Surveillance
    humanURL: https://data.cdc.gov/browse?category=NNDSS
    properties:
      - url: https://data.cdc.gov/browse?category=NNDSS
        type: Catalog
      - url: https://www.cdc.gov/nndss/
        type: Program
      - url: https://wonder.cdc.gov/nndss/nndss_table_menus.asp
        type: Tables
    description: The National Notifiable Diseases Surveillance System (NNDSS) and Morbidity and Mortality Weekly Report (MMWR) tables are published as Socrata datasets on data.cdc.gov, providing weekly and historical case counts for notifiable conditions accessible via SoQL and bulk download.
common:
  - type: Website
    url: https://www.cdc.gov/
  - type: OpenData
    url: https://data.cdc.gov/
  - type: Portal
    url: https://open.cdc.gov/
  - type: APIs
    url: https://open.cdc.gov/apis.html
  - type: GitHubOrganization
    url: https://github.com/CDCgov
  - type: WONDER
    url: https://wonder.cdc.gov/
  - type: Socrata
    url: https://dev.socrata.com/
  - type: ContentSyndication
    url: https://tools.cdc.gov/medialibrary/
  - type: EPHTN
    url: https://ephtracking.cdc.gov/
  - type: Privacy Policy
    url: https://www.cdc.gov/other/privacy.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
