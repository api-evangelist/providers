---
aid: telefonica
name: Telefónica
description: Telefónica is one of the world's leading telecommunications companies, operating in Europe and Latin America. Through its Open Gateway initiative, Telefónica exposes standardized network capabilities as APIs following the CAMARA (Cloud and Edge for Mobile Access and Real-time Execution) open standards developed by the GSMA. The Open Gateway APIs enable developers and enterprises to build applications leveraging Telefónica's network infrastructure for authentication, fraud prevention, location services, quality of service, and device management. APIs are available in Spain, Germany, Brazil, and the United Kingdom through the Telefónica Open Gateway sandbox and partner program.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Telecommunications
  - Mobile Network
  - CAMARA
  - Open Gateway
  - Authentication
  - Fraud Prevention
  - Location Services
url: https://raw.githubusercontent.com/api-evangelist/telefonica/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: telefonica:number-verification-api
    name: Telefónica Number Verification API
    description: The Number Verification API enables automatic verification that users are interacting via devices with SIM cards associated with their phone numbers, eliminating the need for credential entry or one-time passwords. Uses carrier network data to verify the mobile number associated with the device's active data connection. Available in Spain, Germany, and Brazil.
    humanURL: https://opengateway.telefonica.com/en/apis/number-verification
    baseURL: https://opengateway.telefonica.com
    tags:
      - Authentication
      - Number Verification
      - Fraud Prevention
      - Mobile Identity
      - SIM
    properties:
      - type: Documentation
        url: https://developers.opengateway.telefonica.com/docs/numberverification
      - type: OpenAPI
        url: openapi/telefonica-number-verification-openapi.yml
      - type: JSONSchema
        url: json-schema/telefonica-device-schema.json
      - type: GitHub
        url: https://github.com/Telefonica/opengateway-developers-website
  - aid: telefonica:sim-swap-api
    name: Telefónica SIM Swap API
    description: The SIM Swap API enables applications to detect recent SIM card swaps on a mobile number, a common indicator of account takeover fraud. Returns whether a SIM swap occurred on the mobile line and when the last swap happened. Based on CAMARA open standards. Available in Spain, Germany, Brazil, and the United Kingdom.
    humanURL: https://opengateway.telefonica.com/en/apis/sim-swap
    baseURL: https://opengateway.telefonica.com
    tags:
      - Authentication
      - Fraud Prevention
      - SIM Swap
      - Mobile Security
    properties:
      - type: Documentation
        url: https://developers.opengateway.telefonica.com/docs/simswap
      - type: OpenAPI
        url: openapi/telefonica-sim-swap-openapi.yml
      - type: JSONSchema
        url: json-schema/telefonica-device-schema.json
      - type: GitHub
        url: https://github.com/Telefonica/opengateway-samples-simswap
  - aid: telefonica:kyc-match-api
    name: Telefónica Know Your Customer Match API
    description: The KYC Match API validates a user's contact information (name, address, phone number, email) against reliable mobile carrier data, enabling quick identity verification without sharing personal data. Used for e-commerce, financial services, and insurance KYC compliance. Available in Spain, Germany, Brazil, and the United Kingdom.
    humanURL: https://opengateway.telefonica.com/en/apis/kyc-match
    baseURL: https://opengateway.telefonica.com
    tags:
      - Authentication
      - Fraud Prevention
      - KYC
      - Identity Verification
      - Financial Services
    properties:
      - type: Documentation
        url: https://opengateway.telefonica.com/en/apis/kyc-match
      - type: OpenAPI
        url: openapi/telefonica-kyc-match-openapi.yml
  - aid: telefonica:location-verification-api
    name: Telefónica Location Verification API
    description: The Location Verification API verifies the geographical location of a SIM-based device, confirming whether the device is present within a requested geographic area. Uses network data rather than GPS to verify location without privacy risks. Available in Spain, Germany, and Brazil.
    humanURL: https://opengateway.telefonica.com/en/apis/location-verification
    baseURL: https://opengateway.telefonica.com
    tags:
      - Location Services
      - Device Location
      - Fraud Prevention
      - Mobile Network
    properties:
      - type: Documentation
        url: https://opengateway.telefonica.com/en/apis/location-verification
      - type: OpenAPI
        url: openapi/telefonica-location-verification-openapi.yml
  - aid: telefonica:quality-on-demand-api
    name: Telefónica Quality on Demand API
    description: The Quality on Demand (QoD) API provides applications with precise control over mobile network connectivity quality, enabling guaranteed bandwidth and low latency for specific application flows. Used for real-time communications, streaming, industrial IoT, and gaming. Available in Spain, Germany, and Brazil.
    humanURL: https://opengateway.telefonica.com/en/apis/quality-on-demand
    baseURL: https://opengateway.telefonica.com
    tags:
      - Quality of Service
      - Mobile Network
      - IoT
      - Network Slicing
      - Communication Quality
    properties:
      - type: Documentation
        url: https://opengateway.telefonica.com/en/apis/quality-on-demand
      - type: OpenAPI
        url: openapi/telefonica-quality-on-demand-openapi.yml
      - type: JSONSchema
        url: json-schema/telefonica-qod-session-schema.json
  - aid: telefonica:device-roaming-status-api
    name: Telefónica Device Roaming Status API
    description: The Device Roaming Status API verifies the roaming status of a SIM-based device securely using carrier network data, without relying on GPS or identity theft risks. Enables fraud detection, access control, and compliance for applications requiring location awareness. Available in Spain and Brazil.
    humanURL: https://opengateway.telefonica.com/en/apis/device-roaming-status
    baseURL: https://opengateway.telefonica.com
    tags:
      - Roaming
      - Device Status
      - Fraud Prevention
      - Mobile Network
    properties:
      - type: Documentation
        url: https://opengateway.telefonica.com/en/apis/device-roaming-status
      - type: OpenAPI
        url: openapi/telefonica-device-roaming-openapi.yml
  - aid: telefonica:scam-signal-api
    name: Telefónica Scam Signal API
    description: The Scam Signal API enables companies to protect their customers from phishing scams and voice fraud by detecting active scam calls in real time using Telefónica's network intelligence. Available in Spain.
    humanURL: https://opengateway.telefonica.com/en/apis/scam-signal
    baseURL: https://opengateway.telefonica.com
    tags:
      - Fraud Prevention
      - Scam Detection
      - Phishing
      - Voice Fraud
      - Security
    properties:
      - type: Documentation
        url: https://opengateway.telefonica.com/en/apis/scam-signal
  - aid: telefonica:age-verification-api
    name: Telefónica Age Verification API
    description: The Age Verification API allows companies to confirm in real time whether a mobile user meets a specified age threshold, using carrier data for privacy-preserving age checks without sharing personal data. Available in the United Kingdom.
    humanURL: https://opengateway.telefonica.com/en/apis/age-verification
    baseURL: https://opengateway.telefonica.com
    tags:
      - Age Verification
      - Compliance
      - E-Commerce
      - Media
      - Privacy
    properties:
      - type: Documentation
        url: https://opengateway.telefonica.com/en/apis/age-verification
  - aid: telefonica:line-tenure-api
    name: Telefónica Line Tenure API
    description: The Line Tenure API indicates how long a mobile number has belonged to its current user, providing a fraud risk signal for identity validation and account security workflows. Available in Spain, Brazil, and the United Kingdom.
    humanURL: https://opengateway.telefonica.com/en/apis/line-tenure
    baseURL: https://opengateway.telefonica.com
    tags:
      - Fraud Prevention
      - Identity Verification
      - Financial Services
      - Mobile Security
    properties:
      - type: Documentation
        url: https://opengateway.telefonica.com/en/apis/line-tenure
  - aid: telefonica:population-density-data-api
    name: Telefónica Population Density Data API
    description: The Population Density Data API provides dynamic real-time data on population density in a specific geographic area and time window, derived from anonymized and aggregated mobile network data. Used for transport planning, event management, and retail analytics. Available in Spain.
    humanURL: https://opengateway.telefonica.com/en/apis/population-density-data
    baseURL: https://opengateway.telefonica.com
    tags:
      - Location Services
      - Population Data
      - Analytics
      - Transport
      - Smart City
    properties:
      - type: Documentation
        url: https://opengateway.telefonica.com/en/apis/population-density-data
common:
  - url: https://opengateway.telefonica.com/en
    name: Telefónica Open Gateway
    type: Website
    description: Telefónica Open Gateway developer portal.
  - url: https://opengateway.telefonica.com/en/developer-hub
    name: Telefónica Open Gateway Developer Hub
    type: DeveloperPortal
    description: Developer Hub for testing Telefónica Open Gateway APIs in sandbox.
  - url: https://developers.opengateway.telefonica.com/docs/initiative
    name: Open Gateway Initiative Documentation
    type: Documentation
    description: Technical documentation for the Telefónica Open Gateway initiative.
  - url: https://github.com/Telefonica
    name: Telefónica GitHub
    type: GitHub
    description: Telefónica official GitHub organization.
  - url: https://github.com/camaraproject
    name: CAMARA Project GitHub
    type: GitHub
    description: GSMA CAMARA project - open standards for telco network APIs.
  - url: https://opengateway.telefonica.com/en/apis
    name: Telefónica Open Gateway APIs
    type: APIs
    description: Complete list of available Telefónica Open Gateway APIs.
  - url: https://opengateway.telefonica.com/en/developer-hub/join
    name: Join Telefónica Developer Hub
    type: Signup
    description: Registration for the Telefónica Open Gateway Developer Hub.
  - url: https://www.linkedin.com/company/telefonica
    name: Telefónica on LinkedIn
    type: LinkedIn
    description: Telefónica LinkedIn company page.
  - url: https://x.com/Telefonica
    name: Telefónica on X
    type: X
    description: Telefónica on X (formerly Twitter).
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
