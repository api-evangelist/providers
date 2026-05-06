---
aid: openweather
name: OpenWeather
description: OpenWeather is a data platform that provides accurate and reliable weather information to individuals, businesses, and organizations around the world. They gather real-time data from a network of sensors, satellites, and weather stations to deliver comprehensive weather forecasts, historical weather data, and climate information.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Air Pollution
  - Air Quality
  - Climate
  - Forecasting
  - Weather
created: '2024-11-07'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/openweather/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: openweather:openweather-one-call-api
    name: OpenWeather One Call API
    description: The One Call API provides current weather, minute-by-minute forecast for one hour, hourly forecast for 48 hours, daily forecast for 8 days, and government weather alerts for any geographic coordinates.
    humanURL: https://openweathermap.org/api/one-call-3
    tags:
      - Climate
      - Forecasting
      - Weather
    properties:
      - type: Documentation
        url: https://openweathermap.org/api/one-call-3
      - type: OpenAPI
        url: openapi/openweather-openapi.yml
      - type: Pricing
        url: https://openweathermap.org/price
      - type: SignUp
        url: https://home.openweathermap.org/users/sign_up
  - aid: openweather:openweather-air-pollution-api
    name: OpenWeather Air Pollution API
    description: The Air Pollution API provides current, forecast, and historical air pollution data for any coordinates on the globe. It returns the basic Air Quality Index along with concentrations of CO, NO, NO2, O3, SO2, NH3, PM2.5, and PM10 pollutants.
    humanURL: https://openweathermap.org/api/air-pollution
    tags:
      - Air Pollution
      - Air Quality
      - Weather
    properties:
      - type: Documentation
        url: https://openweathermap.org/api/air-pollution
      - type: Pricing
        url: https://openweathermap.org/price
      - type: SignUp
        url: https://home.openweathermap.org/users/sign_up
common:
  - url: https://openweathermap.org/
    name: OpenWeather
    type: Website
    description: Official OpenWeather website.
  - url: https://openweathermap.org/api
    name: API Catalog
    type: API Portal
    description: Catalog of all OpenWeather APIs and data products.
  - url: https://openweathermap.org/technology
    name: Technology
    type: Documentation
    description: Overview of OpenWeather data sources and processing technology.
  - url: https://openweathermap.org/price
    name: Pricing
    type: Pricing
    description: OpenWeather subscription tiers and pricing.
  - url: https://home.openweathermap.org/users/sign_up
    name: Sign Up
    type: SignUp
    description: Create an OpenWeather account and obtain an API key.
  - url: https://openweather.co.uk/blog
    name: Blog
    type: Blog
    description: OpenWeather blog with product news and weather data insights.
  - url: https://openweathermap.org/faq
    name: FAQ
    type: FAQ
    description: Frequently asked questions about OpenWeather APIs and data.
  - url: https://openweathermap.org/contact-us
    name: Support
    type: Support
    description: Contact and support resources for OpenWeather customers.
  - url: https://openweather.co.uk/privacy-policy
    name: Privacy
    type: Privacy
    description: OpenWeather privacy policy.
  - url: https://openweather.co.uk/terms
    name: Terms of Service
    type: Terms of Service
    description: OpenWeather terms of service.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
