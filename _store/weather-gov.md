---
aid: weather-gov
url: https://example.com/apis/api-web-service.yml
apis:
  - name: API Web Service
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.weather.gov/documentation/services-web-api
    properties:
      - url: openapi/openapi.yml
        name: Weather.gov OpenAPI
        type: OpenAPI
    description: The weather.gov API.
    aid: weather-gov:api-web-service
name: Weather.gov
tags:
  - Weather
image: >-
  https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/api-web-service.png
common: []
created: '2024-07-02T00:00:00.000Z'
modified: '2025-01-04'
description: >-
  Weather.gov is the official website of the National Weather Service, which is
  responsible for providing accurate and timely weather forecasts, warnings, and
  advisories to the public. The website offers a wide range of weather
  information, including current conditions, radar images, satellite imagery,
  and forecasts for cities and regions across the United States. In addition to
  weather forecasts, Weather.gov also provides information on severe weather
  events such as hurricanes, tornadoes, and winter storms, as well as updates on
  ocean and air quality conditions. The website is a valuable resource for
  anyone looking to stay informed about the weather and plan their activities
  accordingly.
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
specificationVersion: '0.16'
type: Contract
position: Consuming
access: 3rd-Party
---