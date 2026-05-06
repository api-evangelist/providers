---
aid: us-bureau-of-labor-statistics
name: US Bureau of Labor Statistics
description: The US Bureau of Labor Statistics (BLS) is the principal federal agency responsible for measuring labor market activity, working conditions, price changes, and productivity in the US economy. BLS provides a Public Data API that enables developers to retrieve published historical time series data covering employment, unemployment, inflation, wages, productivity, and occupational statistics across all BLS programs. The API supports both unauthenticated access (v1) and registered access with higher limits (v2), returning data in JSON format for integration into applications, research tools, and economic dashboards.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Labor Statistics
  - Economic Data
  - Open Data
created: '2025-02-09'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/us-bureau-of-labor-statistics/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: us-bureau-of-labor-statistics:bls-public-data-api
    name: BLS Public Data API
    description: The BLS Public Data API allows developers to programmatically retrieve published historical time series data from all BLS surveys. Version 1 is open without registration; Version 2 requires a free API key and provides higher query limits (500 daily, up to 50 series per request, 20 years of data). The API covers Consumer Price Index (CPI), employment and unemployment statistics, wages, productivity, industry employment, and occupational statistics. Data is returned in JSON format.
    humanURL: https://www.bls.gov/developers/home.htm
    baseURL: https://api.bls.gov/publicAPI/v2
    tags:
      - Labor Statistics
      - Employment
      - Unemployment
      - Consumer Price Index
      - Economic Data
      - Time Series
      - Open Data
    properties:
      - type: Documentation
        url: https://www.bls.gov/developers/home.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/us-bureau-of-labor-statistics/refs/heads/main/openapi/bls-public-data-api-openapi.yml
      - type: Registration
        url: https://data.bls.gov/registrationEngine/
      - type: TermsOfService
        url: https://www.bls.gov/developers/termsOfService.htm
      - type: DataAPI
        url: https://api.bls.gov/publicAPI/v2/timeseries/data/
    contact:
      - FN: BLS Data Support
        url: https://www.bls.gov/developers/home.htm
        email: data_staff@bls.gov
features:
  - name: Time Series Data Retrieval
    description: Retrieve historical time series data for one or multiple BLS series IDs
  - name: Multi-Series Requests
    description: Query up to 50 series per request with API v2 registration
  - name: Date Range Filtering
    description: Filter data by start and end year to retrieve specific date ranges
  - name: Statistical Calculations
    description: Request net changes and percent changes alongside raw values (v2)
  - name: Series Catalog
    description: Retrieve metadata and descriptions for series (v2)
  - name: Annual Averages
    description: Include annual average values in time series responses (v2)
  - name: Survey Discovery
    description: List all BLS surveys and their metadata
  - name: Popular Series
    description: Retrieve the 25 most popular BLS series IDs
useCases:
  - name: Economic Research Dashboard
    description: Build dashboards displaying unemployment rate trends, CPI inflation data, and wage growth
  - name: Labor Market Analysis
    description: Analyze employment patterns across industries, occupations, and demographics
  - name: Inflation Monitoring
    description: Track Consumer Price Index changes for economic forecasting and policy analysis
  - name: Occupational Wage Studies
    description: Retrieve occupational employment and wage data for compensation benchmarking
  - name: FOIA Data Applications
    description: Access publicly available BLS survey data for transparency and accountability reporting
solutions:
  - name: Economic Intelligence Platforms
    description: Integrate BLS data into economic intelligence and forecasting platforms
  - name: HR Analytics Tools
    description: Power HR compensation analysis tools with BLS wage and employment data
  - name: Government Data Portals
    description: Enrich government open data portals with BLS statistical datasets
integrations:
  - name: data.gov
    description: BLS datasets are cataloged and accessible through data.gov
    url: https://catalog.data.gov/organization/bls-gov
  - name: api.data.gov
    description: BLS API is accessible via the api.data.gov gateway
    url: https://api.data.gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
