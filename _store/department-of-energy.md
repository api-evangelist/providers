---
aid: department-of-energy
name: Department of Energy
description: The U.S. Department of Energy (DOE) provides extensive open data and APIs across its national laboratories and program offices. Notable APIs are published by the Energy Information Administration (EIA) for energy statistics, the Office of Scientific and Technical Information (OSTI) for research and publications, the National Renewable Energy Laboratory (NREL, rebranding as NLR) developer network for renewables and alternative fuels, and the Buildings Performance Database (BPD).
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Buildings
  - Electricity
  - Energy
  - Federal Government
  - Open Data
  - Renewables
  - Research
  - Solar
  - Statistics
url: https://raw.githubusercontent.com/api-evangelist/department-of-energy/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: government
position: Producer
access: Public
apis:
  - aid: department-of-energy:eia-api
    name: EIA Open Data API V2
    description: The U.S. Energy Information Administration (EIA) Open Data API v2 is a fully RESTful implementation of EIA's public energy statistics. Routes are arranged in a logical hierarchy across petroleum, natural gas, coal, electricity, nuclear, renewables, total energy, international, and consumption series. Requests require a free api_key obtained from the EIA Open Data portal and return up to 5,000 rows per request as JSON or XML.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.eia.gov/opendata/
    baseURL: https://api.eia.gov/v2
    tags:
      - Coal
      - Electricity
      - Energy Statistics
      - Natural Gas
      - Petroleum
      - Renewables
    properties:
      - type: Documentation
        url: https://www.eia.gov/opendata/documentation.php
      - type: Developer
        url: https://www.eia.gov/developer/
      - type: API Browser
        url: https://www.eia.gov/opendata/browser/
      - type: Sign Up
        url: https://www.eia.gov/opendata/register.php
      - type: Reference PDF
        url: https://www.eia.gov/opendata/documentation/APIv2.1.0.pdf
    contact:
      - FN: EIA Customer Support
        email: InfoCtr@eia.gov
        url: https://www.eia.gov/about/contact/
  - aid: department-of-energy:osti-pages-api
    name: OSTI DOE PAGES API
    description: The DOE PAGES (Public Access Gateway for Energy and Science) REST API provides programmatic access to publications resulting from DOE-funded research, hosted by the Office of Scientific and Technical Information (OSTI). The API supports search and retrieval of bibliographic records and full-text links for journal articles, accepted manuscripts, and technical reports.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.osti.gov/pages/api/v1/docs
    baseURL: https://www.osti.gov/pages/api/v1
    tags:
      - Bibliographic
      - OSTI
      - Publications
      - Research
    properties:
      - type: Documentation
        url: https://www.osti.gov/pages/api/v1/docs
      - type: Reference
        url: https://www.osti.gov/api
    contact:
      - FN: OSTI
        email: osti@osti.gov
        url: https://www.osti.gov/contact
  - aid: department-of-energy:osti-elink-api
    name: OSTI ELINK API
    description: The OSTI ELINK API is the Office of Scientific and Technical Information's submission and retrieval interface for DOE research records. It supports submission of metadata and full text by DOE-funded research organizations, and it powers public retrieval interfaces for OSTI.GOV.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.osti.gov/elink/
    baseURL: https://www.osti.gov/elink
    tags:
      - ELINK
      - Metadata
      - OSTI
      - Submission
    properties:
      - type: Documentation
        url: https://www.osti.gov/elink/
      - type: API
        url: https://www.osti.gov/api
    contact:
      - FN: OSTI ELINK
        email: elink@osti.gov
        url: https://www.osti.gov/contact
  - aid: department-of-energy:nrel-developer-api
    name: NREL/NLR Developer Network APIs
    description: The National Renewable Energy Laboratory (NREL, transitioning to NLR) Developer Network publishes a portfolio of REST APIs covering solar resource and PV simulation, alternative fuels and stations, electricity utilities and rates, transportation, geothermal, and energy economics. All APIs share a common API key model issued through api.data.gov. Existing developer.nrel.gov consumers must migrate to developer.nlr.gov by April 30, 2026.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.nlr.gov/
    baseURL: https://developer.nlr.gov/api
    tags:
      - Alternative Fuels
      - Buildings
      - Electricity
      - Geothermal
      - NREL
      - Renewables
      - Solar
      - Transportation
    properties:
      - type: Documentation
        url: https://developer.nlr.gov/docs/
      - type: Solar APIs
        url: https://developer.nlr.gov/docs/solar/
      - type: Electricity APIs
        url: https://developer.nlr.gov/docs/electricity/
      - type: Sign Up
        url: https://api.data.gov/signup/
      - type: Data Catalog
        url: https://data.nlr.gov/
    contact:
      - FN: NREL Developer Network
        url: https://developer.nlr.gov/contact-us
  - aid: department-of-energy:buildings-performance-database
    name: Buildings Performance Database API
    description: The Buildings Performance Database (BPD) is a DOE repository of anonymized empirical performance records for commercial and residential buildings. The BPD API allows partners to query aggregate distributions and compare cohorts of buildings across attributes such as building type, vintage, climate zone, and energy use intensity.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.energy.gov/eere/buildings/application-programming-interface
    baseURL: https://api.example.com
    tags:
      - BPD
      - Benchmarking
      - Buildings
      - Energy Efficiency
    properties:
      - type: Documentation
        url: https://www.energy.gov/eere/buildings/application-programming-interface
    contact:
      - FN: DOE Building Technologies Office
        url: https://www.energy.gov/eere/buildings
  - aid: department-of-energy:open-data-catalog
    name: Department of Energy Open Data Catalog
    description: The DOE participates in Data.gov by publishing thousands of dataset records under the doe-gov organization. These datasets cover energy consumption, generation, environmental impact, R&D, and more, and are accessible through Data.gov's CKAN-compatible API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://catalog.data.gov/organization/doe-gov
    baseURL: https://catalog.data.gov/api/3
    tags:
      - CKAN
      - Datasets
      - Open Data
    properties:
      - type: Documentation
        url: https://catalog.data.gov/organization/doe-gov
      - type: Open Energy Data
        url: https://www.energy.gov/data/open-energy-data
      - type: CKAN Reference
        url: https://docs.ckan.org/en/2.8/api/
    contact:
      - FN: DOE Open Data
        url: https://www.energy.gov/data/open-energy-data
common:
  - type: Website
    url: https://www.energy.gov
  - type: Open Energy Data
    url: https://www.energy.gov/data/open-energy-data
  - type: Developer Portal
    url: https://api.data.gov/
  - type: EIA
    url: https://www.eia.gov
  - type: OSTI
    url: https://www.osti.gov
  - type: NREL Developer
    url: https://developer.nlr.gov/
  - type: Open Energy Data Initiative
    url: https://data.openei.org/
  - type: Energy Data eXchange
    url: https://edx.netl.doe.gov/
  - type: Data.gov DOE Catalog
    url: https://catalog.data.gov/organization/doe-gov
  - type: News
    url: https://www.energy.gov/news
  - type: Privacy Policy
    url: https://www.energy.gov/privacy
  - type: GitHub Organization
    url: https://github.com/doe-doe
  - type: JSON-LD
    url: json-ld/department-of-energy-context.jsonld
  - type: Vocabulary
    url: vocabulary/department-of-energy-vocabulary.yml
  - type: Capabilities
    url: capabilities/department-of-energy-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
