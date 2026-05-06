---
aid: abstract-api
url: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/apis.yml
name: Abstract API
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Avatars
  - Company Enrichment
  - Contacts
  - Currencies
  - Email Validation
  - Exchange Rates
  - IBAN Validation
  - Image Processing
  - IP Geolocation
  - IP Intelligence
  - Phone Validation
  - Public Holidays
  - Screenshots
  - Timezones
  - VAT Validation
  - Web Scraping
description: Abstract API is a platform that offers a wide range of API services for developers to easily integrate various functionalities into their applications. Services include IP geolocation, IP intelligence, email validation, phone validation, currency exchange, website screenshots, image processing, web scraping, company enrichment, public holidays, timezone lookup, VAT validation, IBAN validation, and user avatar generation. Abstract API provides a seamless way for developers to access powerful features without having to build them from scratch.
created: '2025-02-24'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: abstract-api:email-reputation
    name: Email Reputation API
    tags:
      - Email Validation
      - Email Reputation
      - Fraud Detection
    humanURL: https://www.abstractapi.com/api/email-verification-validation-api
    baseURL: https://emailreputation.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/email-reputation.md
        type: Documentation
      - url: openapi/abstract-api-email-reputation.yaml
        type: OpenAPI
      - url: json-schema/email-reputation-breach-info-schema.json
        type: JSONSchema
      - url: examples/email-reputation-breach-info-example.json
        type: Example
    description: Validate email addresses for deliverability, detect disposable or risky domains, verify SMTP/MX records, and enrich email data with sender information, breach history, and risk scoring.
  - aid: abstract-api:phone-intelligence
    name: Phone Intelligence API
    tags:
      - Phone Validation
      - Phone Intelligence
      - Fraud Detection
    humanURL: https://www.abstractapi.com/api/phone-validation-api
    baseURL: https://phoneintelligence.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/phone-intelligence.md
        type: Documentation
      - url: openapi/abstract-api-phone-intelligence.yaml
        type: OpenAPI
      - url: json-schema/phone-intelligence-phone-country-schema.json
        type: JSONSchema
      - url: examples/phone-intelligence-phone-country-example.json
        type: Example
    description: Identify carrier, line type, validity, location, and get deep insights including line status, VoIP detection, and risk scoring for any phone number globally.
  - aid: abstract-api:ip-geolocation
    name: IP Geolocation API
    tags:
      - IP Geolocation
      - IP Addresses
      - Geolocation
    humanURL: https://www.abstractapi.com/api/ip-geolocation-api
    baseURL: https://ipgeolocation.abstractapi.com/v1/
    properties:
      - url: https://www.abstractapi.com/api/ip-geolocation-api
        type: Documentation
      - url: openapi/abstract-api-ip-geolocation.yaml
        type: OpenAPI
      - url: json-schema/ip-geolocation-currency-info-schema.json
        type: JSONSchema
      - url: examples/ip-geolocation-currency-info-example.json
        type: Example
    description: Geolocate any IPv4 or IPv6 address to country, region, city, coordinates, timezone, currency, and flag data covering 4 billion+ IP addresses across 250,000+ cities worldwide.
  - aid: abstract-api:ip-intelligence
    name: IP Intelligence API
    tags:
      - IP Intelligence
      - IP Addresses
      - Security
      - Fraud Detection
    humanURL: https://www.abstractapi.com/api/ip-intelligence
    baseURL: https://ip-intelligence.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/ip-intelligence.md
        type: Documentation
      - url: openapi/abstract-api-ip-intelligence.yaml
        type: OpenAPI
      - url: json-schema/ip-intelligence-asn-info-schema.json
        type: JSONSchema
      - url: examples/ip-intelligence-asn-info-example.json
        type: Example
    description: Detect VPNs, proxies, Tor exit nodes, abuse potential, hosting services, relays, and mobile IPs. Also provides ASN, company, location, timezone, flag, and currency data for any IP address.
  - aid: abstract-api:company-enrichment
    name: Company Enrichment API
    tags:
      - Company Enrichment
      - Business Data
      - Data Enrichment
    humanURL: https://www.abstractapi.com/api/company-enrichment
    baseURL: https://companyenrichment.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/company-enrichment.md
        type: Documentation
      - url: openapi/abstract-api-company-enrichment.yaml
        type: OpenAPI
      - url: json-schema/company-enrichment-company-enrichment-response-schema.json
        type: JSONSchema
      - url: examples/company-enrichment-company-enrichment-response-example.json
        type: Example
    description: Retrieve comprehensive details about businesses using their domain or email address, including name, logo, headcount, location, industry, and more.
  - aid: abstract-api:exchange-rates
    name: Exchange Rates API
    tags:
      - Currencies
      - Exchange Rates
      - Finance
    humanURL: https://www.abstractapi.com/api/exchange-rate-api
    baseURL: https://exchange-rates.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/exchange-rates.md
        type: Documentation
      - url: openapi/abstract-api-exchange-rates.yaml
        type: OpenAPI
      - url: json-schema/exchange-rates-convert-response-schema.json
        type: JSONSchema
      - url: examples/exchange-rates-convert-response-example.json
        type: Example
    description: Look up the latest exchange rates for 80+ currencies, convert between currencies, and retrieve historical exchange rate data using ISO 4217 currency codes.
  - aid: abstract-api:public-holidays
    name: Public Holidays API
    tags:
      - Public Holidays
      - Calendar
      - Global Data
    humanURL: https://www.abstractapi.com/api/holidays-api
    baseURL: https://holidays.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/holidays.md
        type: Documentation
      - url: openapi/abstract-api-public-holidays.yaml
        type: OpenAPI
      - url: json-schema/public-holidays-holiday-schema.json
        type: JSONSchema
      - url: examples/public-holidays-holiday-example.json
        type: Example
    description: Get public, local, religious, and other holidays for any country. Supports year and country filtering with comprehensive holiday metadata.
  - aid: abstract-api:timezones
    name: Timezone API
    tags:
      - Timezones
      - Time
      - Date
      - Calendar
    humanURL: https://www.abstractapi.com/api/time-date-timezone-api
    baseURL: https://timezone.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/timezones.md
        type: Documentation
      - url: openapi/abstract-api-timezones.yaml
        type: OpenAPI
      - url: json-schema/timezones-convert-time-response-schema.json
        type: JSONSchema
      - url: examples/timezones-convert-time-response-example.json
        type: Example
    description: Find, convert, and manage time and timezone data across the world. Supports lookup by location or coordinates and returns local time, timezone abbreviation, UTC offset, and DST information.
  - aid: abstract-api:vat-validation
    name: VAT Validation API
    tags:
      - VAT Validation
      - Finance
      - Compliance
      - Tax
    humanURL: https://www.abstractapi.com/api/vat-validation-rates-api
    baseURL: https://vat.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/vat-validation.md
        type: Documentation
      - url: openapi/abstract-api-vat-validation.yaml
        type: OpenAPI
      - url: json-schema/vat-validation-vat-calculate-response-schema.json
        type: JSONSchema
      - url: examples/vat-validation-vat-calculate-response-example.json
        type: Example
    description: Validate VAT numbers, look up current VAT rates by country, and calculate VAT-inclusive or VAT-exclusive prices to stay compliant for domestic and cross-border sales.
  - aid: abstract-api:iban-validation
    name: IBAN Validation API
    tags:
      - IBAN Validation
      - Finance
      - Banking
    humanURL: https://www.abstractapi.com/api/iban-validation
    baseURL: https://ibanvalidation.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/iban-validation.md
        type: Documentation
      - url: openapi/abstract-api-iban-validation.yaml
        type: OpenAPI
      - url: json-schema/iban-validation-iban-validation-response-schema.json
        type: JSONSchema
      - url: examples/iban-validation-iban-validation-response-example.json
        type: Example
    description: Determine the validity and details of International Bank Account Numbers (IBANs), including bank name, account type, and country code.
  - aid: abstract-api:website-screenshot
    name: Website Screenshot API
    tags:
      - Screenshots
      - Web Capture
      - Images
    humanURL: https://www.abstractapi.com/api/website-screenshot-api
    baseURL: https://screenshot.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/screenshot.md
        type: Documentation
      - url: openapi/abstract-api-website-screenshot.yaml
        type: OpenAPI
    description: Capture high-quality screenshots of any website with optional customizations including CSS injection, delay settings, and viewport configuration.
  - aid: abstract-api:image-processing
    name: Image Processing API
    tags:
      - Image Processing
      - Images
      - Optimization
    humanURL: https://www.abstractapi.com/api/image-processing-optimization-api
    baseURL: https://images.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/images.md
        type: Documentation
      - url: openapi/abstract-api-image-processing.yaml
        type: OpenAPI
      - url: json-schema/image-processing-image-processing-response-schema.json
        type: JSONSchema
      - url: examples/image-processing-image-processing-response-example.json
        type: Example
    description: Compress, convert, and optimize images by URL or direct upload. Supports format conversion, quality adjustment, and size reduction.
  - aid: abstract-api:web-scraping
    name: Web Scraping API
    tags:
      - Web Scraping
      - Data Extraction
      - HTML
    humanURL: https://www.abstractapi.com/api/web-scraping-api
    baseURL: https://scrape.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/scrape.md
        type: Documentation
      - url: openapi/abstract-api-web-scraping.yaml
        type: OpenAPI
      - url: json-schema/web-scraping-web-scraping-response-schema.json
        type: JSONSchema
      - url: examples/web-scraping-web-scraping-response-example.json
        type: Example
    description: Extract data from any website by providing the target URL. Handles JavaScript rendering and returns the full HTML content of any web page.
  - aid: abstract-api:avatars
    name: Avatars API
    tags:
      - Avatars
      - Images
      - User Interface
    humanURL: https://www.abstractapi.com/api/user-avatar-api
    baseURL: https://avatars.abstractapi.com/v1/
    properties:
      - url: https://docs.abstractapi.com/api/avatars.md
        type: Documentation
      - url: openapi/abstract-api-avatars.yaml
        type: OpenAPI
    description: Create highly customizable avatar images using a person's name or initials. Supports color, font, and size customization for user profile images.
common:
  - type: Website
    url: https://www.abstractapi.com/
  - type: Portal
    url: https://app.abstractapi.com/
  - type: SignUp
    url: https://app.abstractapi.com/users/signup
  - type: Login
    url: https://app.abstractapi.com/users/login
  - type: Pricing
    url: https://www.abstractapi.com/pricing
  - type: Blog
    url: https://www.abstractapi.com/blog
  - type: Documentation
    url: https://docs.abstractapi.com/
  - type: GettingStarted
    url: https://docs.abstractapi.com/
  - type: GitHubOrganization
    url: https://github.com/abstractapi
  - type: TermsOfService
    url: https://www.abstractapi.com/legal/terms
  - type: PrivacyPolicy
    url: https://www.abstractapi.com/legal/privacy
  - type: Authentication
    url: https://docs.abstractapi.com/
    data:
      - type: apiKey
        in: query
        name: api_key
        description: Unique API key per service, passed as a query parameter or Bearer token
  - type: Features
    data:
      - name: API Key Authentication
        description: Each API uses a unique API key passed as a query parameter or Bearer token header
      - name: Free Tier
        description: Each API offers a free tier with limited monthly requests and 1 request/second rate limit
      - name: Simple REST API
        description: All APIs follow a simple REST pattern with a single base URL and query parameters
      - name: Global Coverage
        description: Data covers global locations with 80+ currencies, 250,000+ cities, and worldwide phone/IP coverage
      - name: JSON Responses
        description: All API responses return structured JSON data with consistent error codes
      - name: Modular Services
        description: Each API is independently keyed and priced, allowing granular subscription management
  - type: UseCases
    data:
      - name: Email List Cleaning
        description: Validate and filter email lists to improve deliverability and reduce bounce rates
      - name: Fraud Detection
        description: Use IP intelligence, email reputation, and phone intelligence to detect and block fraudulent users
      - name: User Onboarding Enrichment
        description: Automatically enrich user profiles with geolocation, company, and contact data at signup
      - name: Currency Conversion
        description: Display localized pricing or perform currency conversions in e-commerce and fintech apps
      - name: Compliance Automation
        description: Validate VAT numbers and IBAN codes to automate financial compliance workflows
      - name: Content Extraction
        description: Use web scraping API to extract structured data from any website for data pipelines
      - name: Dynamic User Avatars
        description: Generate placeholder avatars for users without profile photos using the Avatars API
  - type: Integrations
    data:
      - name: JavaScript
        description: Official JavaScript SDK for Exchange Rates, Email Validation, IP Geolocation, and Phone Validation
      - name: Python
        description: Official Python SDK for Exchange Rates, Email Validation, IP Geolocation, and Phone Validation
      - name: PHP
        description: Official PHP SDK for Exchange Rates, Email Validation, IP Geolocation, and Phone Validation
  - url: rules/abstract-api-spectral-rules.yml
    type: SpectralRules
  - url: capabilities/fraud-detection.yaml
    type: NaftikoCapability
  - url: capabilities/data-enrichment.yaml
    type: NaftikoCapability
  - url: capabilities/financial-compliance.yaml
    type: NaftikoCapability
  - url: vocabulary/abstract-api-vocabulary.yaml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
