---
aid: environmental-protection-agency
name: Environmental Protection Agency
description: The U.S. Environmental Protection Agency (EPA) provides multiple public data APIs covering environmental records, air quality monitoring, UV forecasts, and internal data holdings. These services enable State and local governments, federal agencies, researchers, and the public to access environmental data about air, water, and land.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Environment
  - Federal Government
  - Air Quality
  - Open Data
url: https://raw.githubusercontent.com/api-evangelist/environmental-protection-agency/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
position: Consumer
access: 3rd-Party
apis:
  - aid: environmental-protection-agency:envirofacts
    name: EPA Envirofacts Data Service API
    description: Envirofacts provides a single point of access to U.S. EPA environmental data contained in U.S. EPA databases. The RESTful Data Service API returns output in JSON, CSV, Excel, HTML, JSONP, Parquet, PDF, or XML formats and supports queries across any Envirofacts table.
    humanURL: https://www.epa.gov/enviro/envirofacts-data-service-api
    baseURL: https://data.epa.gov/efservice/
    tags:
      - Environment
      - Open Data
    properties:
      - type: Documentation
        url: https://www.epa.gov/enviro/envirofacts-data-service-api
      - type: Web Services
        url: https://www.epa.gov/enviro/web-services
  - aid: environmental-protection-agency:aqs
    name: EPA Air Quality System API
    description: The EPA Air Quality System (AQS) API provides programmatic access to ambient air pollution data collected by the EPA, state, local, and tribal air pollution control agencies, including hourly sample data, daily/quarterly/annual summaries, monitor information, and quality assurance data. JSON response format with API key authentication.
    humanURL: https://aqs.epa.gov/aqsweb/documents/data_api.html
    baseURL: https://aqs.epa.gov/data/api
    tags:
      - Environment
      - Air Quality
    properties:
      - type: Documentation
        url: https://aqs.epa.gov/aqsweb/documents/data_api.html
      - type: Sign Up
        url: https://aqs.epa.gov/data/api/signup
  - aid: environmental-protection-agency:uv-index
    name: EPA UV Index API
    description: The EPA UV Index API provides hourly and daily ultraviolet radiation forecasts by ZIP code or city/state. Output is available in XML, JSON, Excel, and CSV formats.
    humanURL: https://www.epa.gov/enviro/web-services
    baseURL: https://data.epa.gov/efservice/getEnvirofactsUVHOURLY/
    tags:
      - Environment
      - UV Index
    properties:
      - type: Documentation
        url: https://www.epa.gov/enviro/web-services
  - aid: environmental-protection-agency:echo
    name: EPA ECHO Compliance and Enforcement API
    description: Enforcement and Compliance History Online (ECHO) provides public access to compliance and enforcement information for EPA-regulated facilities nationwide. The ECHO web services API supports facility searches, compliance reports, and enforcement case lookups.
    humanURL: https://echo.epa.gov/tools/web-services
    baseURL: https://echodata.epa.gov/echo/
    tags:
      - Environment
      - Compliance
      - Enforcement
    properties:
      - type: Documentation
        url: https://echo.epa.gov/tools/web-services
common:
  - type: Website
    url: https://www.epa.gov/
  - type: Developer Central
    url: https://www.epa.gov/developers
  - type: Web Services
    url: https://www.epa.gov/enviro/web-services
  - type: Open Data
    url: https://www.data.gov/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
