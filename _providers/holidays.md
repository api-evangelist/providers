---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Holidays Agentic Access
  operation_count: 5
  slug: holidays-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: Country metadata, codes, languages, currencies, and subdivisions.
  name: Holiday API Countries API
  slug: holidays-countries-api
- description: Public holidays and observances for countries, states, and provinces.
  name: Holiday API Holidays API
  slug: holidays-holidays-api
- description: Supported languages for retrieving localized holiday names.
  name: Holiday API Languages API
  slug: holidays-languages-api
- description: Working / business day calculations honoring country workweeks and holidays.
  name: Holiday API Workdays API
  slug: holidays-workdays-api
artifact_total: 52
collections:
- collection_type: postman
  name: Holiday Countries API
  slug: postman-holidays-countries-api
- collection_type: postman
  name: Holiday Countries Holidays API
  slug: postman-holidays-holidays-api
- collection_type: postman
  name: Holiday Countries Languages API
  slug: postman-holidays-languages-api
- collection_type: postman
  name: Holiday Countries Workdays API
  slug: postman-holidays-workdays-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/holiday-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/holidays-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/holidays-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://holidayapi.com/
- group: start
  title: ''
  type: Portal
  url: https://holidayapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://holidayapi.com/docs
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/holidays-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/holidays-response-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/holidays-response-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/holidays-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/holidays-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/holidays-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/holidays-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/holidays-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://holidayapi.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://holidayapi.com/signup
- group: start
  title: ''
  type: Login
  url: https://holidayapi.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://holidayapi.com/terms
- group: operate
  title: ''
  type: Contact
  url: https://holidayapi.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/holidayapi
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: Examples
  url: examples/holidays-error-example.json
- group: build
  title: ''
  type: SDKs
  url: https://github.com/holidayapi/holidayapi-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/holidayapi/holidayapi-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/holidayapi/holidayapi-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/holidayapi/holidayapi-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/holidayapi/holidayapi-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/holidayapi/holidayapi-raku
created: '2026-05-28'
description: Holiday API is a commercial reference-data service that delivers verified public holidays, observances, country and language metadata, and workday calculations for 250 countries and 3,680+ state/province subdivisions in 100+ languages. Operated by Gravity Boulevard, LLC, it exposes five JSON endpoints under https://holidayapi.com/v1/ with official client libraries for Go, Node.js, PHP, Python, Ruby, and Raku.
examples:
- key_count: 3
  name: Holidays Error Example
  slug: holidays-error-example
- key_count: 4
  name: Holidays Get Workday Example
  slug: holidays-get-workday-example
- key_count: 3
  name: Holidays Get Workdays Example
  slug: holidays-get-workdays-example
- key_count: 3
  name: Holidays List Countries Example
  slug: holidays-list-countries-example
- key_count: 3
  name: Holidays List Holidays Example
  slug: holidays-list-holidays-example
- key_count: 3
  name: Holidays List Languages Example
  slug: holidays-list-languages-example
features:
- description: Proprietary holiday generation system continuously verifies holidays for 250 countries.
  name: Verified Holiday Data
- description: 3,680 state and province subdivisions on the States & Provinces plan via ISO 3166-2.
  name: Subdivision Coverage
- description: Localized holiday names in over 100 languages via ISO 639-1 codes.
  name: 100+ Languages
- description: Get workdays and count business days between dates honoring country-specific workweeks and holidays.
  name: Workday Calculator
- description: Coverage from year 1 through year 2050+ on paid plans.
  name: Historic and Future Dates
- description: JSON, XML, YAML, CSV, TSV, and PHP serialization.
  name: Multiple Response Formats
- description: Unlimited offline caching during active paid subscription; 24-hour window on free tier.
  name: Offline Storage
- description: All plans share a monthly request quota (1M requests/month) with no per-second or per-minute limits.
  name: No Velocity Throttling
- description: Enterprise-grade infrastructure designed for 99.999% availability.
  name: Five-Nines Uptime
finops:
- name: Holidays Finops
  service_category: Reference Data / Calendar
  slug: holidays-finops
image: https://holidayapi.com/images/calendar.svg
integrations:
- description: Pull holiday data into Google Sheets / Excel via the JSON, CSV, or TSV format options.
  name: Spreadsheets
- description: Feed holiday and workday data into Looker, Tableau, or Metabase for calendar dimensions.
  name: BI Tools
- description: Trigger Zapier or n8n flows on upcoming/previous holidays per country.
  name: Workflow Automation
- description: Sync verified holiday data into Google Calendar, Outlook, or iCal feeds.
  name: Calendar Platforms
json_schemas:
- name: Country
  property_count: 8
  slug: holidays-country
- name: Holiday
  property_count: 8
  slug: holidays-holiday
- name: Language
  property_count: 2
  slug: holidays-language
- name: Response
  property_count: 4
  slug: holidays-response
- name: Workday
  property_count: 2
  slug: holidays-workday
json_structures:
- name: Holidays Country Structure
  property_count: 8
  slug: holidays-country-structure
- name: Holidays Holiday Structure
  property_count: 8
  slug: holidays-holiday-structure
- name: Holidays Language Structure
  property_count: 2
  slug: holidays-language-structure
- name: Holidays Response Structure
  property_count: 4
  slug: holidays-response-structure
- name: Holidays Workday Structure
  property_count: 2
  slug: holidays-workday-structure
jsonld:
- class_count: 16
  name: Holidays Context
  property_count: 17
  slug: holidays-context
layout: provider
modified: '2026-05-29'
name: Holiday API
nav: Providers
network: true
overview: 'Holiday API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Countries API, Holidays API, Languages API, and 1 more. Tagged areas include Calendar, Holidays, Public Holidays, Observances, and Reference Data.


  The Holiday API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Holiday API''s developer surface includes developer portal, documentation, pricing, signup flow, code examples, and 23 more developer resources.'
plans:
- name: Holidays Plans Pricing
  plan_count: 3
  slug: holidays-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 1
  name: Holidays Rate Limits
  slug: holidays-rate-limits
rules:
- name: Holiday API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: holidays-jsonschema-spectral-rules
- name: Holiday API API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 7
  slug: holidays-rules
score:
  band: strong
  composite: 59.1
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 71.3
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/holidays/refs/heads/main/screenshots/holidays-2026-06-20T182809.png
security:
- kind: domain-security
  name: Holidays Domain Security
  slug: holidays-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: holidays
tags:
- Calendar
- Holidays
- Public Holidays
- Observances
- Reference Data
- Countries
- Languages
- Workdays
- Business Days
- Localization
use_cases:
- description: Mark public holidays on calendar UIs and prevent scheduling on non-business days.
  name: Calendar and Scheduling Apps
- description: Compute promised-by dates that honor weekends and country-specific holidays.
  name: Business Day SLA Calculation
- description: Determine paid time off, observed holidays, and country-specific leave eligibility.
  name: HR and Payroll Systems
- description: Time outreach to align with public holidays in target countries and languages.
  name: Localized Marketing Campaigns
- description: Forecast shipping ETAs that respect carrier and destination-country holidays.
  name: E-commerce Fulfillment
- description: Adjust transaction value dates and settlement windows around bank holidays.
  name: Financial Settlement
- description: Coordinate distributed teams across regions with accurate observed-holiday data.
  name: Global Workforce Management
website: https://holidayapi.com/
---
