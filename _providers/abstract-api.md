---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Abstract Api Agentic Access
  operation_count: 19
  slug: abstract-api-agentic-access
  summary_line: 19 operations
api_count: 14
apis:
- description: User avatar generation operations
  name: Abstract API Avatars API
  slug: abstract-api-avatars-api
- description: Company data enrichment operations
  name: Abstract API Company Enrichment API
  slug: abstract-api-company-enrichment-api
- description: Email validation and reputation operations
  name: Abstract API Email Reputation API
  slug: abstract-api-email-reputation-api
- description: Currency exchange rate operations
  name: Abstract API Exchange Rates API
  slug: abstract-api-exchange-rates-api
- description: IBAN number validation operations
  name: Abstract API IBAN Validation API
  slug: abstract-api-iban-validation-api
- description: Image compression and optimization operations
  name: Abstract API Image Processing API
  slug: abstract-api-image-processing-api
- description: IP address geolocation operations
  name: Abstract API IP Geolocation API
  slug: abstract-api-ip-geolocation-api
- description: Advanced IP address intelligence and security operations
  name: Abstract API IP Intelligence API
  slug: abstract-api-ip-intelligence-api
- description: Phone number validation and intelligence
  name: Abstract API Phone Intelligence API
  slug: abstract-api-phone-intelligence-api
- description: Holiday lookup operations
  name: Abstract API Public Holidays API
  slug: abstract-api-public-holidays-api
- description: Timezone lookup and conversion operations
  name: Abstract API Timezones API
  slug: abstract-api-timezones-api
- description: VAT number validation and rate lookup
  name: Abstract API VAT Validation API
  slug: abstract-api-vat-validation-api
- description: Web content extraction operations
  name: Abstract API Web Scraping API
  slug: abstract-api-web-scraping-api
- description: Website screenshot capture operations
  name: Abstract API Website Screenshot API
  slug: abstract-api-website-screenshot-api
arazzos:
- description: Enrich a company by domain, screenshot its site, and generate a name avatar.
  name: Abstract API Company Enrichment to Screenshot and Avatar
  slug: abstract-api-company-to-screenshot-and-avatar-workflow
- description: Read the live rate, convert an amount, and compare against a historical rate.
  name: Abstract API Live Exchange Rate and Conversion
  slug: abstract-api-currency-live-and-convert-workflow
- description: Validate an email address, then enrich the company behind its domain.
  name: Abstract API Email to Company Enrichment
  slug: abstract-api-email-to-company-enrichment-workflow
- description: Validate an IBAN, then enrich the company it belongs to for a KYB check.
  name: Abstract API IBAN and Company Verification
  slug: abstract-api-iban-and-company-verification-workflow
- description: Geolocate an IP, read its local currency, then convert a price into it.
  name: Abstract API IP Geolocation to Currency Conversion
  slug: abstract-api-ip-geolocation-to-currency-conversion-workflow
- description: Geolocate an IP, get its local time, and list the country's public holidays.
  name: Abstract API IP Geolocation to Timezone and Holidays
  slug: abstract-api-ip-geolocation-to-timezone-holidays-workflow
- description: Screen an IP for VPN/proxy/Tor risk, then geolocate clean traffic.
  name: Abstract API IP Security and Geolocation
  slug: abstract-api-ip-security-and-geolocation-workflow
- description: Validate a phone number, then resolve the local time of its region.
  name: Abstract API Phone Validation to Local Time
  slug: abstract-api-phone-to-timezone-workflow
- description: Capture a website screenshot, scrape its HTML, then optimize an image asset.
  name: Abstract API Screenshot, Scrape, and Image Processing
  slug: abstract-api-screenshot-scrape-and-process-workflow
- description: Validate a VAT number, fetch its country rates, then calculate VAT on an amount.
  name: Abstract API VAT Validation to Rates and Calculation
  slug: abstract-api-vat-validation-to-rates-and-calculation-workflow
artifact_total: 243
collections:
- collection_type: postman
  name: Abstract API - Avatars API
  slug: postman-abstract-api-avatars
- collection_type: postman
  name: Abstract API - Company Enrichment API
  slug: postman-abstract-api-company-enrichment
- collection_type: postman
  name: Abstract API - Email Reputation API
  slug: postman-abstract-api-email-reputation
- collection_type: postman
  name: Abstract API - Exchange Rates API
  slug: postman-abstract-api-exchange-rates
- collection_type: postman
  name: Abstract API - IBAN Validation API
  slug: postman-abstract-api-iban-validation
- collection_type: postman
  name: Abstract API - Image Processing API
  slug: postman-abstract-api-image-processing
- collection_type: postman
  name: Abstract API - IP Geolocation API
  slug: postman-abstract-api-ip-geolocation
- collection_type: postman
  name: Abstract API - IP Intelligence API
  slug: postman-abstract-api-ip-intelligence
- collection_type: postman
  name: Abstract API - Phone Intelligence API
  slug: postman-abstract-api-phone-intelligence
- collection_type: postman
  name: Abstract API - Public Holidays API
  slug: postman-abstract-api-public-holidays
- collection_type: postman
  name: Abstract API - Timezone API
  slug: postman-abstract-api-timezones
- collection_type: postman
  name: Abstract API - VAT Validation API
  slug: postman-abstract-api-vat-validation
- collection_type: postman
  name: Abstract API - Web Scraping API
  slug: postman-abstract-api-web-scraping
- collection_type: postman
  name: Abstract API - Website Screenshot API
  slug: postman-abstract-api-website-screenshot
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Abstract API Avatars API
  slug: open-abstract-api-avatars-api
- collection_type: open
  name: Abstract API Avatars Company Enrichment API
  slug: open-abstract-api-company-enrichment-api
- collection_type: open
  name: Abstract API Avatars Email Reputation API
  slug: open-abstract-api-email-reputation-api
- collection_type: open
  name: Abstract API Avatars Exchange Rates API
  slug: open-abstract-api-exchange-rates-api
- collection_type: open
  name: Abstract API Avatars IBAN Validation API
  slug: open-abstract-api-iban-validation-api
- collection_type: open
  name: Abstract API Avatars Image Processing API
  slug: open-abstract-api-image-processing-api
- collection_type: open
  name: Abstract API Avatars IP Geolocation API
  slug: open-abstract-api-ip-geolocation-api
- collection_type: open
  name: Abstract API Avatars IP Intelligence API
  slug: open-abstract-api-ip-intelligence-api
- collection_type: open
  name: Abstract API Avatars Phone Intelligence API
  slug: open-abstract-api-phone-intelligence-api
- collection_type: open
  name: Abstract API Avatars Public Holidays API
  slug: open-abstract-api-public-holidays-api
- collection_type: open
  name: Abstract API Avatars Timezones API
  slug: open-abstract-api-timezones-api
- collection_type: open
  name: Abstract API Avatars VAT Validation API
  slug: open-abstract-api-vat-validation-api
- collection_type: open
  name: Abstract API Avatars Web Scraping API
  slug: open-abstract-api-web-scraping-api
- collection_type: open
  name: Abstract API Avatars Website Screenshot API
  slug: open-abstract-api-website-screenshot-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abstract-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abstract-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abstract-api-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/abstract-api/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-company-to-screenshot-and-avatar-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-currency-live-and-convert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-email-to-company-enrichment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-iban-and-company-verification-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-ip-geolocation-to-currency-conversion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-ip-geolocation-to-timezone-holidays-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-ip-security-and-geolocation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-phone-to-timezone-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-screenshot-scrape-and-process-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abstract-api-vat-validation-to-rates-and-calculation-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abstractapi
- group: company
  title: ''
  type: Website
  url: https://www.abstractapi.com/
- group: start
  title: ''
  type: Portal
  url: https://app.abstractapi.com/
- group: start
  title: ''
  type: Signup
  url: https://app.abstractapi.com/users/signup
- group: start
  title: ''
  type: Login
  url: https://app.abstractapi.com/users/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.abstractapi.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.abstractapi.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abstractapi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.abstractapi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abstractapi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abstractapi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abstractapi.com/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: https://docs.abstractapi.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/abstract-api-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/abstract-api-vocabulary.yaml
created: '2025-02-24'
description: Abstract API is a platform that offers a wide range of API services for developers to easily integrate various functionalities into their applications. Services include IP geolocation, IP intelligence, email validation, phone validation, currency exchange, website screenshots, image processing, web scraping, company enrichment, public holidays, timezone lookup, VAT validation, IBAN validation, and user avatar generation. Abstract API provides a seamless way for developers to access powerful features without having to build them from scratch.
examples:
- key_count: 6
  name: Abstract Api Calculatevat Example
  slug: abstract-api-calculatevat-example
- key_count: 6
  name: Abstract Api Convertcurrency Example
  slug: abstract-api-convertcurrency-example
- key_count: 6
  name: Abstract Api Converttime Example
  slug: abstract-api-converttime-example
- key_count: 6
  name: Abstract Api Getcompanyenrichment Example
  slug: abstract-api-getcompanyenrichment-example
- key_count: 6
  name: Abstract Api Getcurrenttime Example
  slug: abstract-api-getcurrenttime-example
- key_count: 6
  name: Abstract Api Getemailreputation Example
  slug: abstract-api-getemailreputation-example
- key_count: 6
  name: Abstract Api Gethistoricalexchangerates Example
  slug: abstract-api-gethistoricalexchangerates-example
- key_count: 6
  name: Abstract Api Getipgeolocation Example
  slug: abstract-api-getipgeolocation-example
- key_count: 6
  name: Abstract Api Getipintelligence Example
  slug: abstract-api-getipintelligence-example
- key_count: 6
  name: Abstract Api Getliveexchangerates Example
  slug: abstract-api-getliveexchangerates-example
- key_count: 6
  name: Abstract Api Getphoneintelligence Example
  slug: abstract-api-getphoneintelligence-example
- key_count: 6
  name: Abstract Api Getpublicholidays Example
  slug: abstract-api-getpublicholidays-example
- key_count: 6
  name: Abstract Api Getvatrates Example
  slug: abstract-api-getvatrates-example
- key_count: 6
  name: Abstract Api Processimagebyurl Example
  slug: abstract-api-processimagebyurl-example
- key_count: 6
  name: Abstract Api Scrapewebpage Example
  slug: abstract-api-scrapewebpage-example
- key_count: 6
  name: Abstract Api Validateiban Example
  slug: abstract-api-validateiban-example
- key_count: 6
  name: Abstract Api Validatevatnumber Example
  slug: abstract-api-validatevatnumber-example
- key_count: 11
  name: Company Enrichment Company Enrichment Response Example
  slug: company-enrichment-company-enrichment-response-example
- key_count: 4
  name: Email Reputation Breach Info Example
  slug: email-reputation-breach-info-example
- key_count: 6
  name: Email Reputation Deliverability Example
  slug: email-reputation-deliverability-example
- key_count: 9
  name: Email Reputation Domain Info Example
  slug: email-reputation-domain-info-example
- key_count: 10
  name: Email Reputation Email Quality Example
  slug: email-reputation-email-quality-example
- key_count: 7
  name: Email Reputation Email Reputation Response Example
  slug: email-reputation-email-reputation-response-example
- key_count: 2
  name: Email Reputation Risk Info Example
  slug: email-reputation-risk-info-example
- key_count: 5
  name: Email Reputation Sender Info Example
  slug: email-reputation-sender-info-example
- key_count: 4
  name: Exchange Rates Convert Response Example
  slug: exchange-rates-convert-response-example
- key_count: 3
  name: Exchange Rates Historical Rates Response Example
  slug: exchange-rates-historical-rates-response-example
- key_count: 3
  name: Exchange Rates Live Rates Response Example
  slug: exchange-rates-live-rates-response-example
- key_count: 7
  name: Iban Validation Iban Validation Response Example
  slug: iban-validation-iban-validation-response-example
- key_count: 5
  name: Image Processing Image Processing Response Example
  slug: image-processing-image-processing-response-example
- key_count: 2
  name: Ip Geolocation Currency Info Example
  slug: ip-geolocation-currency-info-example
- key_count: 4
  name: Ip Geolocation Flag Info Example
  slug: ip-geolocation-flag-info-example
- key_count: 20
  name: Ip Geolocation Ip Geolocation Response Example
  slug: ip-geolocation-ip-geolocation-response-example
- key_count: 1
  name: Ip Geolocation Security Info Example
  slug: ip-geolocation-security-info-example
- key_count: 5
  name: Ip Geolocation Timezone Info Example
  slug: ip-geolocation-timezone-info-example
- key_count: 4
  name: Ip Intelligence Asn Info Example
  slug: ip-intelligence-asn-info-example
- key_count: 3
  name: Ip Intelligence Company Basic Example
  slug: ip-intelligence-company-basic-example
- key_count: 3
  name: Ip Intelligence Currency Info Example
  slug: ip-intelligence-currency-info-example
- key_count: 4
  name: Ip Intelligence Flag Info Example
  slug: ip-intelligence-flag-info-example
- key_count: 9
  name: Ip Intelligence Ip Intelligence Response Example
  slug: ip-intelligence-ip-intelligence-response-example
- key_count: 7
  name: Ip Intelligence Ip Security Flags Example
  slug: ip-intelligence-ip-security-flags-example
- key_count: 6
  name: Ip Intelligence Location Info Example
  slug: ip-intelligence-location-info-example
- key_count: 5
  name: Ip Intelligence Timezone Info Example
  slug: ip-intelligence-timezone-info-example
- key_count: 3
  name: Phone Intelligence Phone Country Example
  slug: phone-intelligence-phone-country-example
- key_count: 8
  name: Phone Intelligence Phone Intelligence Response Example
  slug: phone-intelligence-phone-intelligence-response-example
- key_count: 12
  name: Public Holidays Holiday Example
  slug: public-holidays-holiday-example
- key_count: 10
  name: Timezones Convert Time Response Example
  slug: timezones-convert-time-response-example
- key_count: 9
  name: Timezones Current Time Response Example
  slug: timezones-current-time-response-example
- key_count: 7
  name: Vat Validation Vat Calculate Response Example
  slug: vat-validation-vat-calculate-response-example
- key_count: 6
  name: Vat Validation Vat Rates Response Example
  slug: vat-validation-vat-rates-response-example
- key_count: 4
  name: Vat Validation Vat Validation Response Example
  slug: vat-validation-vat-validation-response-example
- key_count: 3
  name: Web Scraping Web Scraping Response Example
  slug: web-scraping-web-scraping-response-example
features:
- description: Each API uses a unique API key passed as a query parameter or Bearer token header
  name: API Key Authentication
- description: Each API offers a free tier with limited monthly requests and 1 request/second rate limit
  name: Free Tier
- description: All APIs follow a simple REST pattern with a single base URL and query parameters
  name: Simple REST API
- description: Data covers global locations with 80+ currencies, 250,000+ cities, and worldwide phone/IP coverage
  name: Global Coverage
- description: All API responses return structured JSON data with consistent error codes
  name: JSON Responses
- description: Each API is independently keyed and priced, allowing granular subscription management
  name: Modular Services
finops:
- name: Abstract Api Finops
  service_category: Data Validation / Enrichment
  slug: abstract-api-finops
image: /assets/icons/abstract-api.png
json_schemas:
- name: ASNInfo
  property_count: 4
  slug: abstract-api-asninfo
- name: BreachInfo
  property_count: 4
  slug: abstract-api-breachinfo
- name: CompanyBasic
  property_count: 3
  slug: abstract-api-companybasic
- name: CompanyEnrichmentResponse
  property_count: 11
  slug: abstract-api-companyenrichmentresponse
- name: ConvertResponse
  property_count: 4
  slug: abstract-api-convertresponse
- name: ConvertTimeResponse
  property_count: 10
  slug: abstract-api-converttimeresponse
- name: CurrencyInfo
  property_count: 2
  slug: abstract-api-currencyinfo
- name: CurrentTimeResponse
  property_count: 9
  slug: abstract-api-currenttimeresponse
- name: Deliverability
  property_count: 6
  slug: abstract-api-deliverability
- name: DomainInfo
  property_count: 9
  slug: abstract-api-domaininfo
- name: EmailQuality
  property_count: 10
  slug: abstract-api-emailquality
- name: EmailReputationResponse
  property_count: 7
  slug: abstract-api-emailreputationresponse
- name: ErrorResponse
  property_count: 2
  slug: abstract-api-errorresponse
- name: FlagInfo
  property_count: 4
  slug: abstract-api-flaginfo
- name: HistoricalRatesResponse
  property_count: 3
  slug: abstract-api-historicalratesresponse
- name: Holiday
  property_count: 12
  slug: abstract-api-holiday
- name: IBANValidationResponse
  property_count: 7
  slug: abstract-api-ibanvalidationresponse
- name: ImageProcessingResponse
  property_count: 5
  slug: abstract-api-imageprocessingresponse
- name: IPGeolocationResponse
  property_count: 20
  slug: abstract-api-ipgeolocationresponse
- name: IPIntelligenceResponse
  property_count: 9
  slug: abstract-api-ipintelligenceresponse
- name: IPSecurityFlags
  property_count: 7
  slug: abstract-api-ipsecurityflags
- name: LiveRatesResponse
  property_count: 3
  slug: abstract-api-liveratesresponse
- name: LocationInfo
  property_count: 6
  slug: abstract-api-locationinfo
- name: PhoneCountry
  property_count: 3
  slug: abstract-api-phonecountry
- name: PhoneIntelligenceResponse
  property_count: 8
  slug: abstract-api-phoneintelligenceresponse
- name: RiskInfo
  property_count: 2
  slug: abstract-api-riskinfo
- name: SecurityInfo
  property_count: 1
  slug: abstract-api-securityinfo
- name: SenderInfo
  property_count: 5
  slug: abstract-api-senderinfo
- name: TimezoneInfo
  property_count: 5
  slug: abstract-api-timezoneinfo
- name: VATCalculateResponse
  property_count: 7
  slug: abstract-api-vatcalculateresponse
- name: VATRatesResponse
  property_count: 6
  slug: abstract-api-vatratesresponse
- name: VATValidationResponse
  property_count: 4
  slug: abstract-api-vatvalidationresponse
- name: WebScrapingResponse
  property_count: 3
  slug: abstract-api-webscrapingresponse
- name: CompanyEnrichmentResponse
  property_count: 11
  slug: company-enrichment-company-enrichment-response
- name: BreachInfo
  property_count: 4
  slug: email-reputation-breach-info
- name: Deliverability
  property_count: 6
  slug: email-reputation-deliverability
- name: DomainInfo
  property_count: 9
  slug: email-reputation-domain-info
- name: EmailQuality
  property_count: 10
  slug: email-reputation-email-quality
- name: EmailReputationResponse
  property_count: 7
  slug: email-reputation-email-reputation-response
- name: RiskInfo
  property_count: 2
  slug: email-reputation-risk-info
- name: SenderInfo
  property_count: 5
  slug: email-reputation-sender-info
- name: ConvertResponse
  property_count: 4
  slug: exchange-rates-convert-response
- name: HistoricalRatesResponse
  property_count: 3
  slug: exchange-rates-historical-rates-response
- name: LiveRatesResponse
  property_count: 3
  slug: exchange-rates-live-rates-response
- name: IBANValidationResponse
  property_count: 7
  slug: iban-validation-iban-validation-response
- name: ImageProcessingResponse
  property_count: 5
  slug: image-processing-image-processing-response
- name: CurrencyInfo
  property_count: 2
  slug: ip-geolocation-currency-info
- name: FlagInfo
  property_count: 4
  slug: ip-geolocation-flag-info
- name: IPGeolocationResponse
  property_count: 20
  slug: ip-geolocation-ip-geolocation-response
- name: SecurityInfo
  property_count: 1
  slug: ip-geolocation-security-info
- name: TimezoneInfo
  property_count: 5
  slug: ip-geolocation-timezone-info
- name: ASNInfo
  property_count: 4
  slug: ip-intelligence-asn-info
- name: CompanyBasic
  property_count: 3
  slug: ip-intelligence-company-basic
- name: CurrencyInfo
  property_count: 3
  slug: ip-intelligence-currency-info
- name: FlagInfo
  property_count: 4
  slug: ip-intelligence-flag-info
- name: IPIntelligenceResponse
  property_count: 9
  slug: ip-intelligence-ip-intelligence-response
- name: IPSecurityFlags
  property_count: 7
  slug: ip-intelligence-ip-security-flags
- name: LocationInfo
  property_count: 6
  slug: ip-intelligence-location-info
- name: TimezoneInfo
  property_count: 5
  slug: ip-intelligence-timezone-info
- name: PhoneCountry
  property_count: 3
  slug: phone-intelligence-phone-country
- name: PhoneIntelligenceResponse
  property_count: 8
  slug: phone-intelligence-phone-intelligence-response
- name: Holiday
  property_count: 12
  slug: public-holidays-holiday
- name: ConvertTimeResponse
  property_count: 10
  slug: timezones-convert-time-response
- name: CurrentTimeResponse
  property_count: 9
  slug: timezones-current-time-response
- name: VATCalculateResponse
  property_count: 7
  slug: vat-validation-vat-calculate-response
- name: VATRatesResponse
  property_count: 6
  slug: vat-validation-vat-rates-response
- name: VATValidationResponse
  property_count: 4
  slug: vat-validation-vat-validation-response
- name: WebScrapingResponse
  property_count: 3
  slug: web-scraping-web-scraping-response
json_structures:
- name: Abstract Api Structure
  property_count: 0
  slug: abstract-api-structure
- name: Company Enrichment Company Enrichment Response Structure
  property_count: 11
  slug: company-enrichment-company-enrichment-response-structure
- name: Email Reputation Breach Info Structure
  property_count: 4
  slug: email-reputation-breach-info-structure
- name: Email Reputation Deliverability Structure
  property_count: 6
  slug: email-reputation-deliverability-structure
- name: Email Reputation Domain Info Structure
  property_count: 9
  slug: email-reputation-domain-info-structure
- name: Email Reputation Email Quality Structure
  property_count: 10
  slug: email-reputation-email-quality-structure
- name: Email Reputation Email Reputation Response Structure
  property_count: 7
  slug: email-reputation-email-reputation-response-structure
- name: Email Reputation Risk Info Structure
  property_count: 2
  slug: email-reputation-risk-info-structure
- name: Email Reputation Sender Info Structure
  property_count: 5
  slug: email-reputation-sender-info-structure
- name: Exchange Rates Convert Response Structure
  property_count: 4
  slug: exchange-rates-convert-response-structure
- name: Exchange Rates Historical Rates Response Structure
  property_count: 3
  slug: exchange-rates-historical-rates-response-structure
- name: Exchange Rates Live Rates Response Structure
  property_count: 3
  slug: exchange-rates-live-rates-response-structure
- name: Iban Validation Iban Validation Response Structure
  property_count: 7
  slug: iban-validation-iban-validation-response-structure
- name: Image Processing Image Processing Response Structure
  property_count: 5
  slug: image-processing-image-processing-response-structure
- name: Ip Geolocation Currency Info Structure
  property_count: 2
  slug: ip-geolocation-currency-info-structure
- name: Ip Geolocation Flag Info Structure
  property_count: 4
  slug: ip-geolocation-flag-info-structure
- name: Ip Geolocation Ip Geolocation Response Structure
  property_count: 20
  slug: ip-geolocation-ip-geolocation-response-structure
- name: Ip Geolocation Security Info Structure
  property_count: 1
  slug: ip-geolocation-security-info-structure
- name: Ip Geolocation Timezone Info Structure
  property_count: 5
  slug: ip-geolocation-timezone-info-structure
- name: Ip Intelligence Asn Info Structure
  property_count: 4
  slug: ip-intelligence-asn-info-structure
- name: Ip Intelligence Company Basic Structure
  property_count: 3
  slug: ip-intelligence-company-basic-structure
- name: Ip Intelligence Currency Info Structure
  property_count: 3
  slug: ip-intelligence-currency-info-structure
- name: Ip Intelligence Flag Info Structure
  property_count: 4
  slug: ip-intelligence-flag-info-structure
- name: Ip Intelligence Ip Intelligence Response Structure
  property_count: 9
  slug: ip-intelligence-ip-intelligence-response-structure
- name: Ip Intelligence Ip Security Flags Structure
  property_count: 7
  slug: ip-intelligence-ip-security-flags-structure
- name: Ip Intelligence Location Info Structure
  property_count: 6
  slug: ip-intelligence-location-info-structure
- name: Ip Intelligence Timezone Info Structure
  property_count: 5
  slug: ip-intelligence-timezone-info-structure
- name: Phone Intelligence Phone Country Structure
  property_count: 3
  slug: phone-intelligence-phone-country-structure
- name: Phone Intelligence Phone Intelligence Response Structure
  property_count: 8
  slug: phone-intelligence-phone-intelligence-response-structure
- name: Public Holidays Holiday Structure
  property_count: 12
  slug: public-holidays-holiday-structure
- name: Timezones Convert Time Response Structure
  property_count: 10
  slug: timezones-convert-time-response-structure
- name: Timezones Current Time Response Structure
  property_count: 9
  slug: timezones-current-time-response-structure
- name: Vat Validation Vat Calculate Response Structure
  property_count: 7
  slug: vat-validation-vat-calculate-response-structure
- name: Vat Validation Vat Rates Response Structure
  property_count: 6
  slug: vat-validation-vat-rates-response-structure
- name: Vat Validation Vat Validation Response Structure
  property_count: 4
  slug: vat-validation-vat-validation-response-structure
- name: Web Scraping Web Scraping Response Structure
  property_count: 3
  slug: web-scraping-web-scraping-response-structure
jsonld:
- class_count: 1
  name: Abstract Api Company Enrichment Context
  property_count: 11
  slug: abstract-api-company-enrichment-context
- class_count: 7
  name: Abstract Api Email Reputation Context
  property_count: 42
  slug: abstract-api-email-reputation-context
- class_count: 3
  name: Abstract Api Exchange Rates Context
  property_count: 8
  slug: abstract-api-exchange-rates-context
- class_count: 1
  name: Abstract Api Iban Validation Context
  property_count: 12
  slug: abstract-api-iban-validation-context
- class_count: 1
  name: Abstract Api Image Processing Context
  property_count: 5
  slug: abstract-api-image-processing-context
- class_count: 5
  name: Abstract Api Ip Geolocation Context
  property_count: 32
  slug: abstract-api-ip-geolocation-context
- class_count: 8
  name: Abstract Api Ip Intelligence Context
  property_count: 35
  slug: abstract-api-ip-intelligence-context
- class_count: 2
  name: Abstract Api Phone Intelligence Context
  property_count: 11
  slug: abstract-api-phone-intelligence-context
- class_count: 1
  name: Abstract Api Public Holidays Context
  property_count: 12
  slug: abstract-api-public-holidays-context
- class_count: 1
  name: Abstract Api Timezones Convert Context
  property_count: 10
  slug: abstract-api-timezones-convert-context
- class_count: 1
  name: Abstract Api Timezones Current Context
  property_count: 9
  slug: abstract-api-timezones-current-context
- class_count: 3
  name: Abstract Api Vat Validation Context
  property_count: 18
  slug: abstract-api-vat-validation-context
- class_count: 1
  name: Abstract Api Web Scraping Context
  property_count: 3
  slug: abstract-api-web-scraping-context
layout: provider
modified: '2026-04-19'
name: Abstract API
nav: Providers
network: true
overview: 'Abstract API publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Avatars API, Company Enrichment API, Email Reputation API, and 11 more. Tagged areas include Avatars, Company Enrichment, Contacts, Currencies, and Email Validation.


  The Abstract API catalog on APIs.io includes 13 JSON-LD contexts and 2 Spectral governance rulesets.


  Abstract API''s developer surface includes authentication, developer portal, signup flow, pricing, engineering blog, documentation, getting-started guide, and 22 more developer resources.'
plans:
- name: Abstract Api Plans Pricing
  plan_count: 5
  slug: abstract-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 6
  name: Abstract Api Rate Limits
  slug: abstract-api-rate-limits
rules:
- name: Abstract API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: abstract-api-jsonschema-spectral-rules
- name: Abstract API API Rules
  rule_count: 40
  severity_counts:
    error: 17
    hint: 0
    info: 6
    warn: 17
  slug: abstract-api-spectral-rules
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 31.2
    developer_ergonomics: 45.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abstract-api/refs/heads/main/screenshots/abstract-api-2026-06-20T163436.png
security:
- kind: authentication
  name: Abstract Api Authentication
  slug: abstract-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Abstract Api Domain Security
  slug: abstract-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abstract-api
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
use_cases:
- description: Validate and filter email lists to improve deliverability and reduce bounce rates
  name: Email List Cleaning
- description: Use IP intelligence, email reputation, and phone intelligence to detect and block fraudulent users
  name: Fraud Detection
- description: Automatically enrich user profiles with geolocation, company, and contact data at signup
  name: User Onboarding Enrichment
- description: Display localized pricing or perform currency conversions in e-commerce and fintech apps
  name: Currency Conversion
- description: Validate VAT numbers and IBAN codes to automate financial compliance workflows
  name: Compliance Automation
- description: Use web scraping API to extract structured data from any website for data pipelines
  name: Content Extraction
- description: Generate placeholder avatars for users without profile photos using the Avatars API
  name: Dynamic User Avatars
website: https://www.abstractapi.com/
---
