---
aid: national-oceanic-and-atmospheric-administration
name: National Oceanic and Atmospheric Administration
description: The National Oceanic and Atmospheric Administration (NOAA) is a federal agency within the U.S. Department of Commerce that focuses on monitoring and predicting changes in the Earth's environment, including climate, weather, oceans, and coasts.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-oceanic-and-atmospheric-administration/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Atmosphere
  - Federal Government
  - Oceans
  - Weather
apis:
  - aid: national-oceanic-and-atmospheric-administration:national-oceanic-and-atmospheric-administration
    name: NOAA CO-OPS Data API
    tags:
      - Oceans
      - Weather
      - Tides
      - Currents
    humanURL: https://api.tidesandcurrents.noaa.gov/api/prod/
    baseURL: https://api.tidesandcurrents.noaa.gov/api/prod
    properties:
      - url: https://api.tidesandcurrents.noaa.gov/api/prod/
        type: Documentation
      - url: https://tidesandcurrents.noaa.gov/web_services_info.html
        type: GettingStarted
      - url: https://raw.githubusercontent.com/api-evangelist/national-oceanic-and-atmospheric-administration/refs/heads/main/openapi/national-oceanic-and-atmospheric-administration-openapi.yml
        type: OpenAPI
    description: The NOAA CO-OPS Data API provides observations and predictions from CO-OPS stations including tides, currents, water levels, meteorological data, and marine forecasts.
common:
  - type: Website
    url: https://www.noaa.gov/
  - type: Portal
    url: https://www.ncdc.noaa.gov/cdo-web/webservices/v2
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
