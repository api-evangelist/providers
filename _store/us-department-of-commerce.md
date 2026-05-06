---
aid: us-department-of-commerce
url: https://raw.githubusercontent.com/api-evangelist/us-department-of-commerce/refs/heads/main/apis.yml
apis:
  - aid: us-department-of-commerce:commercegov-api
    name: Commerce.gov API
    tags:
      - Commerce
      - News
      - Blogs
      - Federal Government
    humanURL: https://www.commerce.gov/data-and-reports/developer-resources/commercegov-api
    properties:
      - url: https://www.commerce.gov/data-and-reports/developer-resources/commercegov-api
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-department-of-commerce/refs/heads/main/openapi/commerce-gov-api-openapi.yml
        type: OpenAPI
    description: The Commerce.gov API provides programmatic access to news and blog content published on the Commerce.gov D8 website. Version 2.0 supports news, blogs, and image endpoints with response fields preserved for backward compatibility.
  - aid: us-department-of-commerce:census-bureau-api
    name: US Census Bureau Data API
    tags:
      - Census
      - Demographics
      - Economic Data
      - Federal Government
    humanURL: https://www.census.gov/data/developers/data-sets.html
    properties:
      - url: https://www.census.gov/data/developers/data-sets.html
        type: Documentation
      - url: https://api.census.gov/data.json
        type: OpenData
    description: The Census Bureau's Data API provides access to a broad range of demographic, economic, and geographic datasets including the American Community Survey, Decennial Census, Economic Census, and specialized surveys covering population, housing, income, employment, and trade data.
  - aid: us-department-of-commerce:bea-api
    name: Bureau of Economic Analysis API
    tags:
      - Economic Data
      - GDP
      - National Accounts
      - Federal Government
    humanURL: https://apps.bea.gov/API/signup/
    properties:
      - url: https://apps.bea.gov/API/signup/
        type: Documentation
      - url: https://apps.bea.gov/api/data/
        type: BaseURL
    description: The Bureau of Economic Analysis API provides access to national, regional, and international economic data including GDP, personal income, corporate profits, international trade and investment, and industry accounts.
  - aid: us-department-of-commerce:ita-trade-api
    name: International Trade Administration Trade Data API
    tags:
      - International Trade
      - Exports
      - Trade Leads
      - Federal Government
    humanURL: https://developer.trade.gov/
    properties:
      - url: https://developer.trade.gov/
        type: Documentation
    description: The International Trade Administration Data Services Platform provides authoritative information on U.S. exporting and international trade, aggregating data from multiple federal agencies including the State Department, Treasury, SBA, and others. Datasets include the Consolidated Screening List, Tariff Rates, Trade Leads, and Trade Events.
  - aid: us-department-of-commerce:noaa-api
    name: NOAA Climate and Weather API
    tags:
      - Weather
      - Climate
      - Environment
      - Federal Government
    humanURL: https://www.ncdc.noaa.gov/cdo-web/webservices/v2
    properties:
      - url: https://www.ncdc.noaa.gov/cdo-web/webservices/v2
        type: Documentation
      - url: https://www.ncdc.noaa.gov/cdo-web/api/v2/
        type: BaseURL
    description: The NOAA Climate Data Online Web Services API provides access to climate data including temperature, precipitation, wind, and weather observations from NOAA's National Centers for Environmental Information. Data covers stations worldwide with historical records spanning centuries.
  - aid: us-department-of-commerce:nist-api
    name: NIST Data Discovery API
    tags:
      - Research Data
      - Standards
      - Materials Science
      - Federal Government
    humanURL: https://data.nist.gov/pdr/lps/
    properties:
      - url: https://data.nist.gov/pdr/lps/
        type: Documentation
      - url: https://data.nist.gov/rmm/records
        type: BaseURL
    description: The National Institute of Standards and Technology provides a Data Discovery API giving access to NIST's public data collections and research datasets covering materials science, chemistry, physics, engineering, and measurement standards.
  - aid: us-department-of-commerce:commerce-data-hub-api
    name: Commerce Data Hub Open Data Portal API
    tags:
      - Open Data
      - Commerce
      - Federal Government
    humanURL: https://data.commerce.gov/open-data-portal-odp-api-version-23
    properties:
      - url: https://data.commerce.gov/open-data-portal-odp-api-version-23
        type: Documentation
    description: The Commerce Data Hub Open Data Portal API (version 2.3) provides REST access to the Department of Commerce's open data catalog with rich search capabilities for discovering and accessing Commerce datasets. An API key is required for access.
name: US Department of Commerce
tags:
  - Commerce
  - Federal Government
  - Open Data
  - Trade
  - Economic Data
  - Climate
  - Standards
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: The US Department of Commerce is responsible for promoting economic growth and job creation in the United States. It oversees various programs and initiatives aimed at supporting businesses, industries, and communities across the country. The department works to ensure fair trade practices, protect intellectual property, and promote innovation and entrepreneurship. It also collects and analyzes economic data to inform policy decisions and help businesses make informed decisions. The Commerce Department houses bureaus including the Census Bureau, Bureau of Economic Analysis, International Trade Administration, NOAA, and NIST, each offering public APIs for their respective data domains.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
