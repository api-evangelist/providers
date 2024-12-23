---
aid: weatherbit
url: >-
  https://raw.githubusercontent.com/api-search/weather/main/_apis/weatherbit/apis.md
apis:
  - aid: weatherbit:weatherbit-current-weather-api
    name: Weatherbit Current Weather API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: http://api.weatherbit.io
    humanURL: https://www.weatherbit.io/api/weather-current
    overlays: []
    properties:
      - url: https://www.weatherbit.io/api/weather-current
        type: Documentation
      - url: properties/weatherbit-current-weather-openapi-original.yml
        type: OpenAPI
    description: >-
      This API returns current conditions from our network of sub-hourly
      reporting weather stations, as well as relevant atmospheric meso-analyses
      (For example, the RTMA). Every API request will return the nearest, and
      most recent observation.
  - aid: weatherbit:weatherbit-severe-weather-alerts-api
    name: Weatherbit Severe Weather Alerts API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.weatherbit.io
    humanURL: https://www.weatherbit.io/api/alerts
    overlays: []
    properties:
      - url: https://www.weatherbit.io/api/alerts
        type: Documentation
    description: >+
      This API returns severe weather alerts issued by local meteorological
      agencies. Current supported countries include: The USA via NOAA. European
      Union member nations, the United Kingdom, and Israel via Meteoalarm. As
      well as weather alerts for Canada via Environment Canada, and China via
      the China Meteorological Administration.

  - aid: weatherbit:weatherbit-weather-forecast-api
    name: Weatherbit Weather Forecast API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.weatherbit.io/api/weather-forecast-api
    overlays: []
    properties:
      - url: https://www.weatherbit.io/api/weather-forecast-api
        type: Documentation
    description: >-
      Improve your business applications with accurate forecasts derived from
      the world's best high resolution global, and regional weather models.
      These forecasts incorporate corrections for model biases using state of
      the art machine learning methods. Our temperature forecasts consistently
      outperform those of all competitors, including the US National Weather
      Service! View our live forecast verification page to see how our API has
      performed against the competition over the past 30 days.
  - aid: weatherbit:weatherbit-historical-weather-api
    name: Weatherbit Historical Weather API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.weatherbit.io
    humanURL: https://www.weatherbit.io/api/historical-weather-api
    overlays: []
    properties:
      - url: https://www.weatherbit.io/api/historical-weather-api
        type: Documentation
    description: >-
      The Historical Weather API allows you to quickly retrieve accurate, high
      resolution historical weather data for any location in the world. Our
      curated weather data is backed by over 120,000 weather stations as well as
      high resolution gridded weather datasets such as the ERA-5 re-analysis,
      and global satellite / doppler radar. Data retrieved from our API is
      gap-free (minimal missing data) due to its application of advanced machine
      learning, and statistical backfilling techniques.
  - aid: weatherbit:weatherbit-ag-weather-api
    name: Weatherbit Ag-Weather API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.weatherbit.io/api/agweather-api
    overlays: []
    properties:
      - url: https://www.weatherbit.io/api/agweather-api
        type: Documentation
    description: >-
      Use our service to retrieve derived data specific to the agriculture
      industry. This API utilizes the state of the art GLDAS re-analysis to
      provide global coverage at a spatial resolution of 0.25 degrees.
  - aid: weatherbit:weatherbit-air-quality-api
    name: Weatherbit Air Quality API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://www.weatherbit.io/api/air-quality-api
    overlays: []
    properties:
      - url: https://www.weatherbit.io/api/air-quality-api
        type: Documentation
    description: >
      Enrich your business applications with high quality air quality data
      derived from the world's most advanced global, and regional air quality
      models. As well as thousands of air quality monitoring stations around the
      world.
name: Weatherbit
tags: []
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
common:
  - url: https://www.weatherbit.io/pricing
    type: Plans
  - url: https://www.weatherbit.io/features
    type: Features
  - url: https://help.weatherbit.io/faq/
    type: FAQs
  - url: https://status.weatherbit.io/
    type: Status
  - url: https://blog.weatherbit.io/
    type: Blog
  - url: https://help.weatherbit.io/
    type: Knowledge
  - url: https://www.weatherbit.io/account/create
    type: Sign Up
  - url: https://www.weatherbit.io/account/login
    type: Login
  - url: https://www.weatherbit.io/terms
    type: Terms of Service
  - url: https://www.weatherbit.io/privacy
    type: Privacy Policy
  - url: https://www.weatherbit.io/contact
    type: Contact
created: 2023/11/20
modified: '2024-07-03'
overlays:
  - url: overlays/apis-io-search.yml
    type: APIs.io Search
  - url: overlays/apis-io-search.yml
    type: API Evangelist Ratings
description: >-
  Our mission at Weatherbit.io is pretty simple. It is to provide the highest
  quality weather forecasts, observations, and historical weather data
  possibl-e.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---