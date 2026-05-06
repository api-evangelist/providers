---
aid: vectren
name: Vectren (CenterPoint Energy)
description: Vectren Corporation was a Fortune 1000 energy holding company headquartered in Evansville (Newburgh), Indiana providing regulated natural gas and electric distribution services to customers in Indiana and Ohio, along with non-regulated infrastructure services and energy efficiency programs. Vectren merged with CenterPoint Energy on February 1, 2019 in a $6 billion transaction, becoming part of the combined company which serves over 7 million metered customers across Arkansas, Indiana, Louisiana, Minnesota, Mississippi, Ohio, Oklahoma, and Texas. Vectren customer-facing portals continue to operate at vectren.com redirecting to CenterPoint Energy services.
url: https://raw.githubusercontent.com/api-evangelist/vectren/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
tags:
  - Electric Utility
  - Energy
  - Natural Gas
  - Regulated Utility
  - Utility
apis:
  - name: CenterPoint Energy Builder Portal
    description: Web portal for builders and developers in Vectren/CenterPoint Energy service territories in Indiana and Ohio. Provides self-service tools for ordering new gas and electric service, checking order status, requesting meters, and managing construction projects. Accessible at builder.vectren.com for legacy Vectren territory customers.
    humanURL: https://builder.vectren.com/web/builder/login/login.jsp
    tags:
      - Builder Services
      - Construction
      - Service Orders
    properties:
      - type: Documentation
        url: https://builder.vectren.com/site-guide
  - name: CenterPoint Energy Customer Account API
    description: Customer self-service portal providing access to account management, bill pay, usage history, and service requests for residential and business customers in the legacy Vectren service territories of Indiana and Ohio. The portal supports energy usage tracking, benchmarking with ENERGY STAR Portfolio Manager, and automated alerts for usage anomalies.
    humanURL: https://midwest.centerpointenergy.com/web/builder/login/login.jsp
    tags:
      - Account Management
      - Bill Pay
      - Customer Portal
      - Energy Usage
    properties:
      - type: Documentation
        url: https://energydataportal.centerpointenergy.com/
  - name: CenterPoint Energy Data Portal
    description: Energy data portal for comparing current and historical energy usage, integrating with ENERGY STAR Portfolio Manager for benchmarking, and accessing customizable energy consumption analytics. Available to residential and business customers in legacy Vectren service territories.
    humanURL: https://energydataportal.centerpointenergy.com/
    tags:
      - Analytics
      - Data
      - Energy Efficiency
      - Energy Usage
    properties:
      - type: Documentation
        url: https://energydataportal.centerpointenergy.com/
common:
  - type: Website
    url: https://www.centerpointenergy.com/en-us/corporate/about-us/vectren-merger
  - type: Portal
    url: https://vectren.com
  - type: BuilderPortal
    url: https://builder.vectren.com/web/builder/login/login.jsp
  - type: Login
    url: https://vectren.com/login
  - type: MergerInfo
    url: https://investors.centerpointenergy.com/news-releases/news-release-details/centerpoint-energy-and-vectren-complete-merger
  - type: Features
    data:
      - name: Natural Gas Distribution
        description: Regulated natural gas distribution serving residential and business customers in Indiana and Ohio.
      - name: Electric Distribution
        description: Regulated electric transmission and distribution in southwestern Indiana.
      - name: Builder and Developer Services
        description: Self-service portal for new service orders, meter requests, and construction project management.
      - name: Energy Efficiency Programs
        description: Programs and incentives for energy efficiency improvements for residential and commercial customers.
      - name: Energy Data Portal
        description: Historical energy usage data and ENERGY STAR Portfolio Manager integration for benchmarking.
      - name: Non-Regulated Services
        description: Infrastructure services and energy efficiency solutions through Vectren's non-regulated subsidiary.
  - type: UseCases
    data:
      - name: New Construction Service
        description: Builders and developers order new gas and electric service connections for residential and commercial construction.
      - name: Account Self-Service
        description: Customers manage accounts, pay bills, track usage, and request service changes online.
      - name: Energy Benchmarking
        description: Commercial building managers benchmark energy performance against ENERGY STAR standards.
      - name: Usage Monitoring
        description: Monitor energy consumption trends to identify efficiency opportunities and anomalies.
  - type: Integrations
    data:
      - name: ENERGY STAR Portfolio Manager
        description: Automated data connection for benchmarking building energy performance.
      - name: CenterPoint Energy
        description: Vectren merged with CenterPoint Energy on February 1, 2019, becoming part of the combined utility.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
