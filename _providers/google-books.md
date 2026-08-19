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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Books Agentic Access
  operation_count: 8
  slug: google-books-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 3
apis:
- description: The Mylibrary API from Google Books — 3 operation(s) for mylibrary.
  name: Google Books Mylibrary API
  slug: google-books-mylibrary-api
- description: The Users API from Google Books — 3 operation(s) for users.
  name: Google Books Users API
  slug: google-books-users-api
- description: The Volumes API from Google Books — 2 operation(s) for volumes.
  name: Google Books Volumes API
  slug: google-books-volumes-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-books-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-books-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-books-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-books-authentication.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/books.jsonld
created: '2026-03-13'
description: The Google Books API allows you to perform full-text searches and retrieve book information, viewability, and eBook availability. You can search for volumes, access detailed metadata including authors, publishers, and ISBNs, manage personal bookshelves, and determine content accessibility.
finops:
- name: Google Books Finops
  service_category: API
  slug: google-books-finops
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
overview: 'Google Books publishes 3 APIs on the [APIs.io](https://apis.io/) network: Mylibrary API, Users API, and Volumes API. Tagged areas include Books, eBooks, Google, Library, and Publishing.


  The Google Books catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Books'' developer surface includes authentication, getting-started guide, pricing, and 5 more developer resources.'
plans:
- name: Google Books Plans Pricing
  plan_count: 3
  slug: google-books-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Google Books Rate Limits
  slug: google-books-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Books API Rules
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
  band: developing
  composite: 40.6
  delta: -1.4
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 63.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 42.0
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
    score: 61.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-books/refs/heads/main/screenshots/google-books-2026-06-20T182027.png
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
- eBooks
- Google
- Library
- Publishing
- Reading
- Search
---
