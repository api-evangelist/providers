---
aid: national-weather-service
url: >-

  https://raw.githubusercontent.com/api-search/us-federal-government/main/_apis/national-weather-service/apis.md
apis:
  - aid: national-weather-service:national-weather-service-api
    name: National Weather Service API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.weather.gov/documentation/services-web-api
    overlays: []
    properties:
      - url: https://www.weather.gov/documentation/services-web-api
        type: Documentation
    description: |-

      The National Weather Service (NWS) API allows developers access to
      critical forecasts, alerts, and observations, along with other weather
      data. The API was designed with a cache-friendly approach that expires
      content based upon the information life cycle. The API is based upon of
      JSON-LD to promote machine data discovery.
name: National Weather Service
tags:
  - Federal Government
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://example.com
    type: Property
created: 2024/01/01
modified: '2025-01-02'
description: >-
  The National Weather Service (NWS) is a government agency within the National
  Oceanic and Atmospheric Administration (NOAA) that is responsible for
  providing weather forecasts, warnings, and other meteorological information to
  the public, government agencies, and private industries. The NWS operates a
  network of weather stations and radars across the United States to monitor
  weather conditions and issue alerts for severe weather events such as
  hurricanes, tornadoes, and winter storms. In addition to forecasting the
  weather, the NWS also conducts research to improve the accuracy of weather
  predictions and provides climate data for scientific studies and long-term
  planning. Overall, the National Weather Service plays a crucial role in
  keeping people safe and informed during hazardous weather conditions.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.16'
type: Contract
position: Consuming
access: 3rd-Party
---