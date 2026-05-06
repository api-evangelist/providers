---
aid: national-renewable-energy-laboratory
name: National Renewable Energy Laboratory
description: The National Renewable Energy Laboratory (NREL) developer network provides a catalog of public APIs that give developers access to renewable energy, alternative fuel, electricity, building, climate, solar, wind, and transportation data and analysis services produced by NREL.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-renewable-energy-laboratory/refs/heads/main/apis.yml
created: '2025-05-02'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Energy
  - Renewable Energy
  - Federal Government
  - Climate
  - Research
apis:
  - aid: national-renewable-energy-laboratory:nrel-developer-network
    name: NREL Developer Network
    description: The umbrella developer portal for NREL APIs spanning alternative fuel stations, solar resource and PV modeling, utility rates, building energy use, climate, electricity, transportation, wave, and wind data.
    humanURL: https://developer.nrel.gov/
    baseURL: https://developer.nrel.gov/api/
    tags:
      - Energy
      - Renewable Energy
    properties:
      - type: Documentation
        url: https://developer.nrel.gov/docs/
      - type: SignUp
        url: https://developer.nrel.gov/signup/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/national-renewable-energy-laboratory/refs/heads/main/openapi/national-renewable-energy-laboratory-openapi.yml
  - aid: national-renewable-energy-laboratory:alternative-fuel-stations
    name: Alternative Fuel Stations
    description: Locate alternative fuel stations across the United States with filters for fuel type, location, status, and access.
    humanURL: https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/
    baseURL: https://developer.nrel.gov/api/alt-fuel-stations/v1/
    tags:
      - Transportation
      - Alternative Fuel
    properties:
      - type: Documentation
        url: https://developer.nrel.gov/docs/transportation/alt-fuel-stations-v1/
  - aid: national-renewable-energy-laboratory:pvwatts
    name: PVWatts
    description: Estimate the energy production and cost of grid-connected photovoltaic energy systems for any location.
    humanURL: https://developer.nrel.gov/docs/solar/pvwatts/v8/
    baseURL: https://developer.nrel.gov/api/pvwatts/v8/
    tags:
      - Solar
      - Modeling
    properties:
      - type: Documentation
        url: https://developer.nrel.gov/docs/solar/pvwatts/v8/
  - aid: national-renewable-energy-laboratory:utility-rates
    name: Utility Rates
    description: Average commercial, industrial, and residential utility rates by US location.
    humanURL: https://developer.nrel.gov/docs/electricity/utility-rates-v3/
    baseURL: https://developer.nrel.gov/api/utility_rates/v3/
    tags:
      - Electricity
      - Rates
    properties:
      - type: Documentation
        url: https://developer.nrel.gov/docs/electricity/utility-rates-v3/
  - aid: national-renewable-energy-laboratory:solar-resource-data
    name: Solar Resource Data
    description: Average direct normal, global horizontal, and tilt at latitude irradiance for a US location.
    humanURL: https://developer.nrel.gov/docs/solar/solar-resource-v1/
    baseURL: https://developer.nrel.gov/api/solar/solar_resource/v1/
    tags:
      - Solar
      - Climate
    properties:
      - type: Documentation
        url: https://developer.nrel.gov/docs/solar/solar-resource-v1/
common:
  - type: Website
    url: https://www.nrel.gov/
  - type: Portal
    url: https://developer.nrel.gov/
  - type: SignUp
    url: https://developer.nrel.gov/signup/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
