---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tenor Agentic Access
  operation_count: 8
  slug: tenor-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://tenor.googleapis.com/v2
  baseurl_source: declared
  description: The Autocomplete API from Tenor — 1 operation(s) for autocomplete.
  name: Tenor Autocomplete API
  slug: tenor-autocomplete-api
- baseURL: https://tenor.googleapis.com/v2
  baseurl_source: declared
  description: The Categories API from Tenor — 1 operation(s) for categories.
  name: Tenor Categories API
  slug: tenor-categories-api
- baseURL: https://tenor.googleapis.com/v2
  baseurl_source: declared
  description: The Featured API from Tenor — 1 operation(s) for featured.
  name: Tenor Featured API
  slug: tenor-featured-api
- baseURL: https://tenor.googleapis.com/v2
  baseurl_source: declared
  description: The Posts API from Tenor — 1 operation(s) for posts.
  name: Tenor Posts API
  slug: tenor-posts-api
- baseURL: https://tenor.googleapis.com/v2
  baseurl_source: declared
  description: The Registershare API from Tenor — 1 operation(s) for registershare.
  name: Tenor Registershare API
  slug: tenor-registershare-api
- baseURL: https://tenor.googleapis.com/v2
  baseurl_source: declared
  description: The Search API from Tenor — 1 operation(s) for search.
  name: Tenor Search API
  slug: tenor-search-api
- baseURL: https://tenor.googleapis.com/v2
  baseurl_source: declared
  description: The Search Suggestions API from Tenor — 1 operation(s) for search suggestions.
  name: Tenor Search Suggestions API
  slug: tenor-search-suggestions-api
- baseURL: https://tenor.googleapis.com/v2
  baseurl_source: declared
  description: The Trending Terms API from Tenor — 1 operation(s) for trending terms.
  name: Tenor Trending Terms API
  slug: tenor-trending-terms-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tenor Autocomplete API
  slug: open-tenor-autocomplete-api
- collection_type: open
  name: Tenor Autocomplete Categories API
  slug: open-tenor-categories-api
- collection_type: open
  name: Tenor Autocomplete Featured API
  slug: open-tenor-featured-api
- collection_type: open
  name: Tenor Autocomplete Posts API
  slug: open-tenor-posts-api
- collection_type: open
  name: Tenor Autocomplete Registershare API
  slug: open-tenor-registershare-api
- collection_type: open
  name: Tenor Autocomplete Search API
  slug: open-tenor-search-api
- collection_type: open
  name: Tenor Autocomplete Search Suggestions API
  slug: open-tenor-search-suggestions-api
- collection_type: open
  name: Tenor Autocomplete Trending Terms API
  slug: open-tenor-trending-terms-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tenor-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tenor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenor-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/tenor
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/tenor/guides/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://console.cloud.google.com/apis/dashboard
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/tenor/answer/10455265
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tenor.com/legal-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: Status
  url: https://status.cloud.google.com/
created: '2026-06-13'
description: 'Tenor is Google''s GIF search engine REST API that enables developers to integrate animated GIF search, trending GIFs, featured content, and category browsing into applications. The API processes over 300 million searches per day across 45+ languages with localized, region-appropriate content. Note: As of January 2026, Google is no longer accepting new API clients; the API is scheduled for sunset on June 30, 2026.'
examples:
- key_count: 1
  name: Categories Response
  slug: categories-response
- key_count: 4
  name: Featured Request
  slug: featured-request
- key_count: 4
  name: Search Request
  slug: search-request
- key_count: 2
  name: Search Response
  slug: search-response
- key_count: 1
  name: Trending Terms Response
  slug: trending-terms-response
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tenor.png
json_schemas:
- name: CategoryObject
  property_count: 3
  slug: CategoryObject
- name: ResponseObject
  property_count: 7
  slug: ResponseObject
- name: SearchResults
  property_count: 2
  slug: SearchResults
- name: SuggestionsResults
  property_count: 1
  slug: SuggestionsResults
jsonld:
- class_count: 0
  name: Tenor Api Context
  property_count: 0
  slug: tenor-api
layout: provider
modified: '2026-06-13'
name: Tenor
nav: Providers
network: true
overview: 'Tenor publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Categories API, Featured API, and 5 more. Tagged areas include GIFs, Animated Images, Search, Media, and Google.


  The Tenor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tenor''s developer surface includes documentation, getting-started guide, authentication, support, status page, and 5 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tenor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tenor-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 64.3
    catalog_earned_first_party: 0.0
    catalog_gap: 50.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 49.0
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tenor/refs/heads/main/screenshots/tenor-2026-06-20T195116.png
security:
- kind: domain-security
  name: Tenor Domain Security
  slug: tenor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tenor Vulnerability Disclosure
  slug: tenor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tenor
tags:
- GIFs
- Animated Images
- Search
- Media
- Google
---
