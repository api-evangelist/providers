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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Checkiday National Holiday Api Agentic Access
  operation_count: 3
  slug: checkiday-national-holiday-api-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://api.apilayer.com/checkiday
  baseurl_source: declared
  description: List, search, and retrieve holidays, observances, and events.
  name: Checkiday - National Holiday and Event API Events API
  slug: checkiday-national-holiday-api-events-api
artifact_total: 24
collections:
- collection_type: postman
  name: Checkiday - National Holiday and Event Events API
  slug: postman-checkiday-national-holiday-api-events-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Checkiday - National Holiday and Event Events API
  slug: open-checkiday-national-holiday-api-events-api
- collection_type: open
  name: Checkiday - National Holiday and Event API
  slug: open-checkiday
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/westy92/holiday-event-api-js/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/westy92/holiday-event-api-js/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/westy92/holiday-event-api-js/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/checkiday---national-holiday-and-event-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/checkiday-national-holiday-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/checkiday-national-holiday-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/checkiday-national-holiday-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://apilayer.com/marketplace/checkiday-api
- group: start
  title: ''
  type: Portal
  url: https://apilayer.com/
- group: other
  title: ''
  type: Marketplace
  url: https://apilayer.com/marketplace
- group: start
  title: ''
  type: Signup
  url: https://apilayer.com/marketplace/checkiday-api#pricing
- group: start
  title: ''
  type: Login
  url: https://apilayer.com/auth/login
- group: commercial
  title: ''
  type: Pricing
  url: https://apilayer.com/marketplace/checkiday-api#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apilayer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apilayer.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://apilayer.com/contact
- group: operate
  title: ''
  type: Contact
  url: https://apilayer.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apilayer.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/westy92
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/westy92/holiday-event-api-js
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: JSONLD
  url: json-ld/checkiday-national-holiday-api-context.jsonld
- group: other
  title: ''
  type: Resources
  url: vocabulary/checkiday-national-holiday-api-vocabulary.yml
- group: other
  title: ''
  type: Resources
  url: rules/checkiday-rules.yml
- group: other
  title: ''
  type: Resources
  url: finops/checkiday-finops.yml
created: '2026-05-28'
description: Industry-leading Holiday and Event API by Checkiday, providing data on more than 5,000 national, international, and bizarre holidays and observances with thousands of descriptions, hashtags, images, founders, alternate names, and multi-year occurrence patterns. Routed through the apilayer marketplace with X-API-Key (apikey) header authentication and official client libraries for JavaScript, TypeScript, Python, C#, PHP, Go, Dart, Rust, and Java/Kotlin. Trusted since 2011 by media organizations including CNN, The New York Times, and USA Today.
examples:
- key_count: 5
  name: Checkiday Get Event Info Example
  slug: checkiday-get-event-info-example
- key_count: 5
  name: Checkiday Get Events Example
  slug: checkiday-get-events-example
- key_count: 5
  name: Checkiday Search Example
  slug: checkiday-search-example
finops:
- name: Checkiday Finops
  service_category: API
  slug: checkiday-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/checkiday-national-holiday-api.png
json_schemas:
- name: Checkiday Event Detail
  property_count: 14
  slug: checkiday-event-detail
- name: Checkiday Event Summary
  property_count: 3
  slug: checkiday-event-summary
- name: Checkiday GetEventInfo Response
  property_count: 2
  slug: checkiday-get-event-info-response
- name: Checkiday GetEvents Response
  property_count: 7
  slug: checkiday-get-events-response
- name: Checkiday Search Response
  property_count: 4
  slug: checkiday-search-response
json_structures:
- name: Checkiday Event Detail Structure
  property_count: 14
  slug: checkiday-event-detail-structure
- name: Checkiday Event Summary Structure
  property_count: 3
  slug: checkiday-event-summary-structure
jsonld:
- class_count: 40
  name: Checkiday National Holiday Api Context
  property_count: 6
  slug: checkiday-national-holiday-api-context
layout: provider
modified: '2026-05-30'
name: Checkiday - National Holiday and Event API
nav: Providers
network: true
overview: 'Checkiday - National Holiday and Event API publishes 1 API on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Calendar, Holidays, Event, Observances, and Dates.


  The Checkiday - National Holiday and Event API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Checkiday - National Holiday and Event API''s developer surface includes authentication, developer portal, signup flow, pricing, support, engineering blog, and 20 more developer resources.'
plans:
- name: Checkiday Plans Pricing
  plan_count: 5
  slug: checkiday-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Checkiday Rate Limits
  slug: checkiday-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Checkiday - National Holiday and Event API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: checkiday-national-holiday-api-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Checkiday - National Holiday and Event API API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 2
  slug: checkiday-rules
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 86.5
    catalog_earned_first_party: 0.0
    catalog_gap: 28.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 13.6
    contract_quality: 73.5
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 57.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/checkiday-national-holiday-api/refs/heads/main/screenshots/checkiday-national-holiday-api-2026-06-20T174241.png
security:
- kind: authentication
  name: Checkiday National Holiday Api Authentication
  slug: checkiday-national-holiday-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Checkiday National Holiday Api Domain Security
  slug: checkiday-national-holiday-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: checkiday-national-holiday-api
tags:
- Calendar
- Holidays
- Event
- Observances
- Dates
- Time
- Public APIs
website: https://apilayer.com/marketplace/checkiday-api
---
