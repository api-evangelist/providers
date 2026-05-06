---
name: Telefono
description: Telefono is a phone number intelligence and validation API platform providing real-time phone number lookup, validation, carrier information, line type detection, and number formatting services for developers. The platform helps businesses verify user phone numbers, detect fraud, improve deliverability of SMS campaigns, and enrich contact data with carrier and geographic information.
image: https://www.telefono.com/logo.png
url: https://www.telefono.com
type: Index
tags:
  - Carrier Lookup
  - Data Enrichment
  - Fraud Prevention
  - Number Intelligence
  - Number Verification
  - Phone Lookup
  - Phone Validation
  - Telecommunications
created: '2024-01-15'
modified: '2026-05-03'
specificationVersion: '0.18'
apis:
  - name: Telefono Phone Validation API
    description: Validate phone numbers in real-time to determine if they are valid, active, and reachable. Returns validity status, number type (mobile, landline, VoIP, toll-free), formatted number in E.164 and national formats, country information, and whether the number is likely a virtual or disposable number.
    image: https://www.telefono.com/api-logo.png
    humanURL: https://developers.telefono.com/validation
    baseURL: https://api.telefono.com/v1/validate
    version: '1.0'
    tags:
      - E.164 Format
      - Number Formatting
      - Number Verification
      - Phone Validation
      - Real-Time Validation
    properties:
      - type: Documentation
        url: https://developers.telefono.com/validation
      - type: OpenAPI
        url: openapi/telefono-validation-openapi.yml
      - type: Authentication
        url: https://developers.telefono.com/authentication
      - type: GettingStarted
        url: https://developers.telefono.com/getting-started
      - type: Pricing
        url: https://www.telefono.com/pricing
      - type: RateLimits
        url: https://developers.telefono.com/rate-limits
    contact:
      - type: Email
        url: mailto:support@telefono.com
      - type: Support
        url: https://www.telefono.com/support
  - name: Telefono Carrier Lookup API
    description: Look up carrier and network information for any phone number worldwide. Returns the current carrier name, network type (GSM, CDMA, UMTS, LTE, 5G), mobile country code (MCC), mobile network code (MNC), and roaming status. Supports real-time HLR (Home Location Register) lookups for accurate portability-aware carrier detection.
    image: https://www.telefono.com/api-logo.png
    humanURL: https://developers.telefono.com/carrier
    baseURL: https://api.telefono.com/v1/carrier
    version: '1.0'
    tags:
      - Carrier Detection
      - Carrier Lookup
      - HLR
      - MCC MNC
      - Network Type
      - Telecommunications
    properties:
      - type: Documentation
        url: https://developers.telefono.com/carrier
      - type: OpenAPI
        url: openapi/telefono-carrier-openapi.yml
      - type: Authentication
        url: https://developers.telefono.com/authentication
      - type: Pricing
        url: https://www.telefono.com/pricing/carrier
    contact:
      - type: Email
        url: mailto:support@telefono.com
  - name: Telefono Number Formatting API
    description: Format phone numbers consistently across different national and international formats. Convert between E.164, national, international, and RFC3966 formats. Supports parsing of phone numbers with country code hints, extracting country codes, and generating click-to-call compatible URIs.
    image: https://www.telefono.com/api-logo.png
    humanURL: https://developers.telefono.com/format
    baseURL: https://api.telefono.com/v1/format
    version: '1.0'
    tags:
      - E.164
      - International Format
      - National Format
      - Number Formatting
      - Phone Parsing
    properties:
      - type: Documentation
        url: https://developers.telefono.com/format
      - type: OpenAPI
        url: openapi/telefono-format-openapi.yml
      - type: Authentication
        url: https://developers.telefono.com/authentication
    contact:
      - type: Email
        url: mailto:support@telefono.com
common:
  - type: Authentication
    url: https://developers.telefono.com/authentication
  - type: Getting Started
    url: https://developers.telefono.com/getting-started
  - type: Rate Limits
    url: https://developers.telefono.com/rate-limits
  - type: Sign Up
    url: https://www.telefono.com/signup
  - type: Pricing
    url: https://www.telefono.com/pricing
  - type: Terms of Service
    url: https://www.telefono.com/terms
  - type: Privacy Policy
    url: https://www.telefono.com/privacy
  - type: Status
    url: https://status.telefono.com
  - type: Support
    url: https://www.telefono.com/support
  - type: GitHub
    url: https://github.com/telefono-api
maintainers:
  - name: Telefono Team
    email: api@telefono.com
---
