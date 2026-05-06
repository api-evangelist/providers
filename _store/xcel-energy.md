---
aid: xcel-energy
name: Xcel Energy
description: 'Xcel Energy is a major U.S. electricity and natural gas utility holding company headquartered in Minneapolis, Minnesota, providing service to approximately 3.7 million electricity customers and 2.1 million natural gas customers across eight Midwestern and Western states: Colorado, Minnesota, Texas, New Mexico, North Dakota, South Dakota, Michigan, and Wisconsin. Xcel Energy operates a developer portal at developer-apim.aws.xcelenergy.com that organizes APIs across customer account management, billing, payments, product and service offerings, and request service. The company provides Green Button Connect My Data APIs based on the ESPI (Energy Services Provider Interface) standard developed by NAESB, enabling authorized third-party applications to access customer energy usage data via OAuth 2.0. Xcel Energy also supports IEEE 2030.5 protocol on newer Itron Gen 5 Riva smart meters for direct local-network access to real-time energy data including solar production. Beyond data APIs, Xcel Energy is a Fortune 500 company investing in clean energy, grid modernization, electric vehicle programs, demand response, and renewable energy interconnection.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Electric Utility
  - Energy
  - Energy Data
  - Green Button
  - Natural Gas
  - Smart Grid
  - Smart Meter
  - Utility
  - ESPI
  - IEEE 2030.5
created: '2024-01-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/xcel-energy/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: xcel-energy:xcel-energy-green-button-api
    name: Xcel Energy Green Button Connect My Data API
    description: Green Button Connect My Data API based on the ESPI (Energy Services Provider Interface) standard developed by NAESB. Enables authorized third-party applications to access customer electricity and natural gas usage data from Xcel Energy smart meters. Supports RESTful access to metered resource data including usage intervals, billing data, and meter readings. Customer authorization is granted via OAuth 2.0 and follows the Green Button Connect specification used by utilities across North America.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer-apim.aws.xcelenergy.com/
    baseURL: https://api.xcelenergy.com
    tags:
      - Energy Data
      - Green Button
      - ESPI
      - Smart Meter
      - Usage Data
      - OAuth 2.0
    properties:
      - type: Documentation
        url: https://developer-apim.aws.xcelenergy.com/
      - type: DeveloperPortal
        url: https://developer-apim.aws.xcelenergy.com/
      - type: Authentication
        url: https://developer-apim.aws.xcelenergy.com/login
      - type: OpenAPI
        url: openapi/xcel-energy-green-button-api.yaml
    contact:
      - type: Support
        url: https://developer-apim.aws.xcelenergy.com/
  - aid: xcel-energy:xcel-energy-smart-meter-api
    name: Xcel Energy Smart Meter IEEE 2030.5 API
    description: IEEE 2030.5 compliant API server built into Itron Gen 5 Riva smart meters deployed by Xcel Energy. Provides real-time and time-delineated energy usage data including solar production information directly from the meter device on the local network. Supports meter reading, usage monitoring, and demand response integration following the Smart Energy Profile 2.0 (IEEE 2030.5) specification.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer-apim.aws.xcelenergy.com/
    tags:
      - IEEE 2030.5
      - Smart Meter
      - Energy Usage
      - Solar
      - Demand Response
      - Local Network
    properties:
      - type: Documentation
        url: https://developer-apim.aws.xcelenergy.com/
      - type: DeveloperPortal
        url: https://developer-apim.aws.xcelenergy.com/
      - type: OpenAPI
        url: openapi/xcel-energy-smart-meter-api.yaml
common:
  - type: DeveloperPortal
    url: https://developer-apim.aws.xcelenergy.com/
  - type: Portal
    url: https://developer-apim.aws.xcelenergy.com/
  - type: SignUp
    url: https://developer-apim.aws.xcelenergy.com/register
  - type: Login
    url: https://developer-apim.aws.xcelenergy.com/login
  - type: TermsOfService
    url: https://developer-apim.aws.xcelenergy.com/terms
  - type: PrivacyPolicy
    url: https://www.xcelenergy.com/privacy_policy
  - type: Support
    url: https://www.xcelenergy.com/contact_us
  - type: LinkedIn
    url: https://www.linkedin.com/company/xcel-energy
  - type: X
    url: https://twitter.com/xcelenergy
  - type: YouTube
    url: https://www.youtube.com/user/XcelEnergyVideo
  - type: Features
    data:
      - name: Green Button Connect My Data
        description: OAuth 2.0 authorized API access to customer electricity and natural gas usage data following the ESPI standard.
      - name: IEEE 2030.5 Smart Meter API
        description: Direct local-network access to real-time energy data including solar production from Itron Gen 5 Riva meters.
      - name: Customer Account Management
        description: API category covering customer account profile, preferences, and service management.
      - name: Billing & Billing Account Management
        description: API category for billing data, statements, and billing account operations.
      - name: Payments & Payment Services
        description: API category for payment processing and payment service operations against customer accounts.
      - name: Product & Service Offerings
        description: API category covering Xcel Energy product and service catalog and program enrollment.
      - name: Request Service & Help
        description: API category for service requests, support workflows, and customer help operations.
      - name: Smart Meter Data
        description: Interval and billing-quality energy usage data captured from Xcel Energy smart meters across electricity and natural gas.
      - name: Demand Response Integration
        description: Programs that allow utilities and third parties to coordinate load reduction events with smart meter and DER endpoints.
      - name: Solar Interconnection Data
        description: Solar production data exposed through smart meter endpoints for customers with on-site photovoltaic systems.
  - type: UseCases
    data:
      - name: Energy Management Applications
        description: Third-party apps that help customers track and reduce electricity and natural gas usage.
      - name: Solar Monitoring
        description: Applications that track on-site solar production and consumption from IEEE 2030.5 smart meters.
      - name: Home Energy Automation
        description: Smart home and HVAC systems that automate energy use based on real-time meter data.
      - name: Sustainability Reporting
        description: Commercial customers reporting carbon and energy data for ESG and sustainability disclosures.
      - name: Building Performance Benchmarking
        description: Whole-building energy benchmarking for ENERGY STAR Portfolio Manager and similar tools.
      - name: Demand Response Programs
        description: Aggregators and DER providers integrating with utility dispatch signals.
      - name: Electric Vehicle Charging Optimization
        description: EV charging applications that schedule charging based on time-of-use rates and grid conditions.
      - name: Research and Policy Analysis
        description: Academic and policy research on energy consumption patterns and decarbonization.
  - type: Integrations
    data:
      - name: Green Button Alliance
        description: Certified Green Button Connect My Data implementation interoperable with the Green Button ecosystem.
      - name: NAESB ESPI
        description: Implements the North American Energy Standards Board Energy Services Provider Interface standard for energy usage data.
      - name: IEEE 2030.5
        description: Smart Energy Profile 2.0 standard implemented on Itron Gen 5 Riva meters for local device APIs.
      - name: Itron
        description: Smart meter deployments use Itron Gen 5 Riva devices that host the IEEE 2030.5 server.
      - name: ENERGY STAR Portfolio Manager
        description: Whole-building benchmarking workflows can consume Green Button data for commercial customers.
      - name: OAuth 2.0
        description: Authorization framework used for customer-consented access to Green Button Connect My Data.
  - type: Solutions
    data:
      - name: Residential Customers
        description: Residential energy usage, billing, and program enrollment across electricity and natural gas service.
      - name: Business Customers
        description: Commercial and industrial customer programs, rates, and aggregated usage data.
      - name: Third-Party Service Providers
        description: Authorized energy management, demand response, and sustainability service providers consuming Green Button data.
      - name: Trade Partners
        description: Contractors, installers, and program partners delivering energy efficiency and renewable installations.
      - name: Researchers and Policy Analysts
        description: Anonymized and customer-authorized data access for academic and policy research.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
