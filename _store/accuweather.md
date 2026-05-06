---
aid: accuweather
url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/apis.yml
name: AccuWeather
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Weather
  - Forecasts
  - Meteorology
  - Location Services
  - Air Quality
  - Storms
description: AccuWeather provides the world's most sophisticated weather intelligence to make lives simpler, safer, and better. Their mission is to save lives and protect property through accurate weather forecasting and data. The AccuWeather One Platform API delivers current conditions, forecasts (hourly, daily, minutecast), air quality, storm tracking, lifestyle indices, and imagery to tens of billions of API calls daily.
created: '2023-11-22'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: accuweather:accuweather-api
    name: AccuWeather API
    description: The AccuWeather One Platform API provides comprehensive weather data including current conditions, hourly and daily forecasts, MinuteCast minute-by-minute precipitation, air quality indices, tropical storm tracking, weather alarms, lifestyle indices, and radar/satellite imagery. Covers 3.5 million+ locations globally with 250+ weather data parameters.
    humanURL: https://developer.accuweather.com/
    baseURL: https://dataservice.accuweather.com
    tags:
      - Weather
      - Forecasts
      - Air Quality
      - Storms
      - MinuteCast
      - Location
    properties:
      - type: Documentation
        url: https://developer.accuweather.com/apis
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/openapi/accuweather-openapi-original.yml
      - type: Authentication
        url: https://developer.accuweather.com/
        title: API Key (query parameter)
      - type: Quickstart
        url: https://developer.accuweather.com/
        title: 14-Day Free Trial
common:
  - type: Portal
    url: https://developer.accuweather.com/
  - type: GettingStarted
    url: https://developer.accuweather.com/
  - type: BestPractices
    url: https://developer.accuweather.com/best-practices
  - type: StatusPage
    url: https://status.accuweather.com/
  - type: TermsOfService
    url: https://developer.accuweather.com/legal
  - type: FAQ
    url: https://developer.accuweather.com/faq-page
  - type: Pricing
    url: https://developer.accuweather.com/packages
  - type: PrivacyPolicy
    url: https://www.accuweather.com/en/privacy
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/rules/accuweather-spectral-rules.yml
    title: AccuWeather Spectral Rules
  - type: JSON-LD
    url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/json-ld/accuweather-context.jsonld
    title: AccuWeather JSON-LD Context
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/vocabulary/accuweather-vocabulary.yaml
    title: AccuWeather Vocabulary
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/accuweather/refs/heads/main/capabilities/weather-intelligence.yaml
    title: Weather Intelligence Capability
  - type: Features
    data:
      - name: Global Weather Coverage
        description: Access weather data for 3.5 million+ locations worldwide with hyper-local precision pinpointed to exact latitude and longitude.
      - name: MinuteCast Precipitation Forecasts
        description: Proprietary minute-by-minute precipitation forecasts with start/stop timing for rain, snow, and ice at any location.
      - name: 250+ Weather Data Parameters
        description: Comprehensive data including RealFeel temperature, AccuLumen Brightness Index, 50+ lifestyle indices, and detailed atmospheric data.
      - name: Air Quality Monitoring
        description: Real-time and forecast air quality index (AQI) with pollutant breakdowns including PM2.5, PM10, ozone, NO2, SO2, and CO.
      - name: Tropical Storm Tracking
        description: Active storm tracking with positions, forecast tracks, and historical data for tropical cyclones in all global ocean basins.
      - name: Weather Imagery
        description: Radar and satellite imagery maps in multiple resolutions (480x480, 640x480, 1024x1024) for integration into applications.
  - type: UseCases
    data:
      - name: Consumer Weather Applications
        description: Power mobile and web weather apps with accurate current conditions, forecasts, and location-aware weather data.
      - name: IoT and Smart Home Automation
        description: Trigger IoT device actions based on real-time weather conditions, forecasts, and precipitation alerts.
      - name: Travel and Outdoor Planning
        description: Integrate weather data into travel booking, outdoor activity planning, and event management platforms.
      - name: Emergency Management
        description: Use storm tracking, severe weather alerts, and precipitation forecasts for emergency response and public safety.
      - name: Agriculture and Environmental Monitoring
        description: Access hyper-local weather data and forecasts for precision agriculture, crop management, and environmental monitoring.
  - type: Integrations
    data:
      - name: Apple WeatherKit
        description: AccuWeather data powers weather experiences on Apple platforms alongside native WeatherKit data.
      - name: Samsung SmartThings
        description: Weather-based automation triggers in the Samsung SmartThings IoT ecosystem.
      - name: Salesforce
        description: Weather data integration with Salesforce CRM for weather-aware sales and service workflows.
      - name: Microsoft Azure
        description: Azure Maps integration providing AccuWeather data within the Microsoft cloud ecosystem.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
