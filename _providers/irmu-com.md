---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Irmu Com Agentic Access
  operation_count: 16
  slug: irmu-com-agentic-access
  summary_line: 16 operations · 2 acting
api_count: 1
apis:
- baseURL: https://app.irmu.com/api
  baseurl_source: declared
  description: Searching Booking.com and reading its property pages, through the same crawler.
  name: Irmu Booking API
  slug: irmu-com-booking-api
- baseURL: https://app.irmu.com/api
  baseurl_source: declared
  description: Fetching a page, charging for it, and collecting it if it was slow.
  name: Irmu Crawl API
  slug: irmu-com-crawl-api
- baseURL: https://app.irmu.com/api
  baseurl_source: declared
  description: Reading the AI Overview Google shows for a query, through the same crawler.
  name: Irmu Google API
  slug: irmu-com-google-api
- baseURL: https://app.irmu.com/api
  baseurl_source: declared
  description: Photographing a page instead of reading it, through the same crawler.
  name: Irmu Screenshot API
  slug: irmu-com-screenshot-api
- baseURL: https://app.irmu.com/api
  baseurl_source: declared
  description: Putting a question to ChatGPT through the same crawler.
  name: Irmu Chat GPT API
  slug: irmu-com-chat-gpt-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/irmu-com/agentic-access/irmu-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/irmu-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/irmu-com/plans/irmu-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/irmu-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/irmu-com/rules/irmu-com-rules.yml
  title: ''
  type: Spectral
  url: rules/irmu-com-rules.yml
- group: design
  href: https://artifacts.apis.io/irmu-com/json-ld/irmu-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/irmu-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/irmu-com/vocabulary/irmu-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/irmu-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/irmu-com/data-model/irmu-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/irmu-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/irmu-com/changelog/irmu-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/irmu-com-changelog.yml
- group: operate
  href: https://artifacts.apis.io/irmu-com/lifecycle/irmu-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/irmu-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/irmu-com/lifecycle/irmu-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/irmu-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/irmu-com/errors/irmu-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/irmu-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/irmu-com/conformance/irmu-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/irmu-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/irmu-com/llms/irmu-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/irmu-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/irmu-com/well-known/irmu-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/irmu-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/irmu-com/hosts/irmu-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/irmu-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/irmu-com/vendors/irmu-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/irmu-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://irmu.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://irmu.com/status
- group: auth
  title: ''
  type: Security
  url: https://irmu.com/legal/security
- group: build
  title: ''
  type: SDKs
  url: https://irmu.com/sdks
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://irmu.com/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://irmu.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://irmu.com/api-reference
- group: auth
  href: https://artifacts.apis.io/irmu-com/authentication/irmu-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/irmu-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/irmu-com/security/irmu-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/irmu-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://irmu.com
- group: docs
  title: ''
  type: Documentation
  url: https://irmu.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://irmu.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://irmu.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://irmu.com/docs
created: '2026-11-05'
description: 'Irmu is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://irmu.com/og-image.jpg
json_schemas:
- name: BookingHotelResult
  property_count: 14
  slug: irmu-com-booking-hotel-result
- name: BookingSearchResult
  property_count: 15
  slug: irmu-com-booking-search-result
- name: ChatGptResult
  property_count: 9
  slug: irmu-com-chat-gpt-result
- name: CrawlOutcome
  property_count: 7
  slug: irmu-com-crawl-outcome
- name: CrawlResult
  property_count: 16
  slug: irmu-com-crawl-result
- name: ScreenshotResult
  property_count: 12
  slug: irmu-com-screenshot-result
jsonld:
- class_count: 11
  name: Irmu Com Context
  property_count: 35
  slug: irmu-com-context
layout: provider
modified: '2026-11-05'
name: Irmu
nav: Providers
network: true
overview: 'Irmu publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Booking API, Crawl API, Google API, and 2 more. Tagged areas include Web Scraping, Developer Tools, Automation, Data Extraction, and Company.


  The Irmu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Irmu''s developer surface includes changelog, API reference, authentication, documentation, pricing, engineering blog, getting-started guide, and 22 more developer resources.'
plans:
- name: Irmu Com Plans Pricing
  plan_count: 6
  slug: irmu-com-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Irmu API Rules
  rule_count: 67
  severity_counts:
    error: 57
    hint: 0
    info: 6
    warn: 4
  slug: irmu-com-rules
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 63.9
    developer_ergonomics: 50.0
    discoverability: 57.1
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Irmu Com Authentication
  slug: irmu-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Irmu Com Domain Security
  slug: irmu-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: irmu-com
tags:
- Web Scraping
- Developer Tools
- Automation
- Data Extraction
- Company
website: https://irmu.com
---
