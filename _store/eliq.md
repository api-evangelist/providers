---
aid: eliq
name: Eliq
description: Eliq provides energy data and analytics APIs for utilities and energy app developers. The platform combines a decade of analytics and machine learning trained on millions of homes to deliver consumption insights, disaggregation, forecasting, peak detection, tariff comparison, and customer segmentation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Utilities
  - Analytics
  - Sustainability
created: '2025-05-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/eliq/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: eliq:auth
    name: Eliq Auth API
    description: The Eliq Auth API authenticates client applications and issues access tokens used to call the Insights, Data Management, and Intelligence APIs. It supports the credential flows required for utility-side integrations.
    humanURL: https://developer.eliq.com/api-reference
    tags:
      - Authentication
      - Energy
    properties:
      - type: Documentation
        url: https://developer.eliq.com/api-reference
      - type: DeveloperPortal
        url: https://developer.eliq.com
  - aid: eliq:data-management
    name: Eliq Data Management API
    description: The Eliq Data Management API ingests and manages customer, location, and meter data inside the Eliq system. Clients use it to provision users and locations, post energy consumption readings, attach metadata such as tariffs and dwelling information, and keep the dataset that powers the Insights API up to date.
    humanURL: https://developer.eliq.com/doc/eliq-apis
    tags:
      - Data Management
      - Energy
      - Utilities
    properties:
      - type: Documentation
        url: https://developer.eliq.com/doc/eliq-apis
  - aid: eliq:insights
    name: Eliq Insights API
    description: The Eliq Insights API delivers analytics and presentation-ready data for end-user energy applications. It exposes consumption aggregates by day, week, month, and year, trends, cost, CO2 footprint, day-ahead pricing, weather, peak power, tariff comparisons, PV disaggregation, forecasting, anomalies, and budget or goal tracking. Device-specific energy insights use NILM disaggregation to attribute consumption to appliances.
    humanURL: https://developer.eliq.com/doc/energy-insights-for-businesses
    tags:
      - Insights
      - Analytics
      - Energy
      - Utilities
      - Disaggregation
    properties:
      - type: Documentation
        url: https://developer.eliq.com/doc/energy-insights-for-businesses
      - type: Documentation
        url: https://developer.eliq.com/doc/device-specific-energy-insights
  - aid: eliq:intelligence
    name: Eliq Intelligence API
    description: The Eliq Intelligence API provides customer-level analytics designed for utility service, operations, and growth teams. It supports customer segmentation, behavioral classification, and personalized recommendations derived from consumption history, weather, tariffs, and disaggregation models. Access to the Intelligence API is granted on request.
    humanURL: https://developer.eliq.com/api-reference
    tags:
      - Intelligence
      - Segmentation
      - Energy
      - Utilities
    properties:
      - type: Documentation
        url: https://developer.eliq.com/api-reference
common:
  - type: Website
    url: https://eliq.com
  - type: DeveloperPortal
    url: https://developer.eliq.com
  - type: Documentation
    url: https://developer.eliq.com/docs
  - type: Documentation
    url: https://eliq.com/api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
