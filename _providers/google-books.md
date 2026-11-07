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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Books Agentic Access
  operation_count: 8
  slug: google-books-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- baseURL: https://www.googleapis.com/books/v1
  baseurl_source: declared
  description: The Users API from Google Books — 3 operation(s) for users.
  name: Google Books Users API
  slug: google-books-users-api
- baseURL: https://www.googleapis.com/books/v1
  baseurl_source: declared
  description: The Volumes API from Google Books — 2 operation(s) for volumes.
  name: Google Books Volumes API
  slug: google-books-volumes-api
- baseURL: https://www.googleapis.com/books/v1
  baseurl_source: declared
  description: The My Library API from Google Books — 3 operation(s) for my library.
  name: Google Books My Library API
  slug: google-books-my-library-api
artifact_total: 18
collections:
- collection_type: open
  name: Google Books API
  slug: open-books
- collection_type: open
  name: Google Books Mylibrary API
  slug: open-google-books-mylibrary-api
- collection_type: open
  name: Google Books Mylibrary Users API
  slug: open-google-books-users-api
- collection_type: open
  name: Google Books Mylibrary Volumes API
  slug: open-google-books-volumes-api
common:
- group: commercial
  href: https://artifacts.apis.io/google-books/plans/google-books-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-books-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-books/rate-limits/google-books-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-books-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-books/finops/google-books-finops.yml
  title: ''
  type: FinOps
  url: finops/google-books-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: agent
  href: https://artifacts.apis.io/google-books/agentic-access/google-books-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-books-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-books/security/google-books-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-books-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-books/security/google-books-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-books-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-books/authentication/google-books-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-books-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-books/scopes/google-books-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-books-scopes.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/books/docs/v1/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/books/docs/v1/using
- group: design
  href: https://artifacts.apis.io/google-books/json-ld/books.jsonld
  title: ''
  type: JSONLD
  url: json-ld/books.jsonld
created: '2026-03-13'
description: The Google Books API allows you to perform full-text searches and retrieve book information, viewability, and eBook availability. You can search for volumes, access detailed metadata including authors, publishers, and ISBNs, manage personal bookshelves, and determine content accessibility.
finops:
- has_sources: false
  method: generated
  name: Google Books Finops
  primary_unit: request
  service_category: API
  slug: google-books-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-books.png
json_schemas:
- name: Google Books Volume
  property_count: 7
  slug: books
jsonld:
- class_count: 21
  name: Books Context
  property_count: 1
  slug: books
layout: provider
modified: '2026-05-19'
name: Google Books
nav: Providers
network: true
overview: 'Google Books publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Users API, Volumes API, and My Library API. Tagged areas include Books, Ebooks, Google, Library, and Publishing.


  The Google Books catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Books'' developer surface includes authentication, getting-started guide, pricing, and 9 more developer resources.'
plans:
- name: Google Books Plans Pricing
  plan_count: 3
  slug: google-books-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Google Books Rate Limits
  slug: google-books-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Books — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-books-jsonschema-spectral-rules
scopes:
- name: Google Books Scopes
  scope_count: 1
  slug: google-books-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.7
    catalog_earned_first_party: 0.0
    catalog_gap: 55.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 9.8
    contract_quality: 56.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-books/google-books-2026-06-20T182027.png
security:
- kind: authentication
  name: Google Books Authentication
  slug: google-books-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Google Books Domain Security
  slug: google-books-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Books Vulnerability Disclosure
  slug: google-books-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-books
tags:
- Books
- Ebooks
- Google
- Library
- Publishing
- Reading
- Search
website: https://www.google.com/
---
