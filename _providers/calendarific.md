---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Calendarific Agentic Access
  operation_count: 3
  slug: calendarific-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://calendarific.com/api/v2
  baseurl_source: declared
  description: List supported countries and their ISO codes.
  name: Calendarific Countries API
  slug: calendarific-countries-api
- baseURL: https://calendarific.com/api/v2
  baseurl_source: declared
  description: Retrieve holiday data for any country and year.
  name: Calendarific Holidays API
  slug: calendarific-holidays-api
- baseURL: https://calendarific.com/api/v2
  baseurl_source: declared
  description: List supported languages and their ISO codes.
  name: Calendarific Languages API
  slug: calendarific-languages-api
artifact_total: 48
collections:
- collection_type: postman
  name: Calendarific Holiday Countries API
  slug: postman-calendarific-countries-api
- collection_type: postman
  name: Calendarific Holiday Countries Holidays API
  slug: postman-calendarific-holidays-api
- collection_type: postman
  name: Calendarific Holiday Countries Languages API
  slug: postman-calendarific-languages-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Calendarific Holiday Countries API
  slug: open-calendarific-countries-api
- collection_type: open
  name: Calendarific Holiday Countries Holidays API
  slug: open-calendarific-holidays-api
- collection_type: open
  name: Calendarific Holiday Countries Languages API
  slug: open-calendarific-languages-api
- collection_type: open
  name: Calendarific Holiday API
  slug: open-calendarific
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/calendarific/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/calendarific-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calendarific-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/calendarific-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://calendarific.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://calendarific.com/api-documentation
- group: start
  title: ''
  type: Signup
  url: https://calendarific.com/signup
- group: start
  title: ''
  type: Login
  url: https://calendarific.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://calendarific.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/calendarific-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/calendarific-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calendarific.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calendarific.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://calendarific.com/contact
- group: operate
  title: ''
  type: Contact
  url: https://calendarific.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/calendarific
- group: build
  title: ''
  type: SDKs
  url: https://github.com/calendarific/python-calendarific
- group: build
  title: ''
  type: SDKs
  url: https://github.com/calendarific/node-calendarific
- group: build
  title: ''
  type: SDKs
  url: https://github.com/calendarific/php-calendarific
- group: build
  title: ''
  type: SDKs
  url: https://github.com/calendarific/ruby-calendarific
- group: build
  title: ''
  type: SDKs
  url: https://github.com/calendarific/go-calendarific
- group: build
  title: ''
  type: SDKs
  url: https://github.com/guibranco/calendarific-sdk-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rchaganti/PSCalendarific
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Bounceapp/elixir-calendarific
- group: design
  title: ''
  type: SpectralRules
  url: rules/calendarific-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/calendarific-vocabulary.yml
- group: build
  title: ''
  type: Tools
  url: https://github.com/noalimoy/calendarific-mcp-server
created: '2026-05-28'
description: Worldwide public holidays REST API covering 230+ countries. Calendarific provides national, local, religious, and observance holiday data with localization across many ISO-639 languages. Used for ecommerce scheduling, HR systems, travel planning, payroll, and global operations.
examples:
- key_count: 2
  name: Calendarific List Countries Example
  slug: calendarific-list-countries-example
- key_count: 2
  name: Calendarific List Holidays Example
  slug: calendarific-list-holidays-example
- key_count: 2
  name: Calendarific List Languages Example
  slug: calendarific-list-languages-example
features:
- description: Coverage of national holidays across more than 230 countries.
  name: 230+ Countries
- description: Holiday names and descriptions in many ISO-639 languages (premium).
  name: Multi-Language Localization
- description: Filter by national, local, religious, or observance categories.
  name: Holiday Type Filtering
- description: Filter by ISO-3166-2 state or region codes.
  name: Sub-Region Filtering
- description: Holidays from historical years through 2049.
  name: Historical and Future Data
- description: Download holiday data as flat files in addition to API access.
  name: CSV and XLS Export
- description: Multiple keys per account for environment separation.
  name: Multiple API Keys
finops:
- name: Calendarific Finops
  service_category: ''
  slug: calendarific-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calendarific.png
integrations:
- description: Imported holiday data into Google Calendar via custom calendars.
  name: Google Calendar
- description: Hydrate Outlook calendars with localized holiday events.
  name: Microsoft Outlook
- description: Community Home Assistant sensor uses Calendarific as a data source.
  name: Home Assistant
- description: Community ETL examples using Python, SQLite, and Apache Airflow.
  name: ETL Pipelines
json_schemas:
- name: Country
  property_count: 5
  slug: calendarific-country
- name: Holiday
  property_count: 11
  slug: calendarific-holiday
- name: Language
  property_count: 2
  slug: calendarific-language
json_structures:
- name: Calendarific Country Structure
  property_count: 5
  slug: calendarific-country-structure
- name: Calendarific Holiday Structure
  property_count: 10
  slug: calendarific-holiday-structure
- name: Calendarific Language Structure
  property_count: 2
  slug: calendarific-language-structure
jsonld:
- class_count: 18
  name: Calendarific Context
  property_count: 2
  slug: calendarific-context
layout: provider
modified: '2026-05-29'
name: Calendarific
nav: Providers
network: true
overview: 'Calendarific publishes 3 APIs on the [APIs.io](https://apis.io/) network: Countries API, Holidays API, and Languages API. Tagged areas include Calendar, Public APIs, Holidays, Worldwide, and Localization.


  The Calendarific catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Calendarific''s developer surface includes authentication, signup flow, pricing, support, tooling, and 22 more developer resources.'
plans:
- name: Calendarific Plans Pricing
  plan_count: 4
  slug: calendarific-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Calendarific Rate Limits
  slug: calendarific-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Calendarific API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: calendarific-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Calendarific API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: calendarific-rules
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 79.5
    catalog_earned_first_party: 0.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 28.8
    contract_quality: 70.1
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calendarific/refs/heads/main/screenshots/calendarific-2026-06-20T173842.png
security:
- kind: authentication
  name: Calendarific Authentication
  slug: calendarific-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Calendarific Domain Security
  slug: calendarific-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calendarific
solutions:
- description: REST API for embedding holiday data into apps and services.
  name: Developer API
- description: CSV and XLS bulk exports for analytics and offline use.
  name: Data Downloads
tags:
- Calendar
- Public APIs
- Holidays
- Worldwide
- Localization
use_cases:
- description: Plan promotions, shipping cutoffs, and customer service hours around local holidays.
  name: Ecommerce Scheduling
- description: Populate localized leave calendars and statutory holiday pay.
  name: HR and Payroll
- description: Surface holiday windows that affect bookings, demand, and pricing.
  name: Travel Planning
- description: Plan global team staffing around local public holidays.
  name: Workforce Scheduling
- description: Hydrate enterprise calendars (Google, Outlook) with localized holidays.
  name: Calendar Sync
- description: Identify country-specific trading and settlement closures.
  name: Financial Markets
website: https://calendarific.com/
---
