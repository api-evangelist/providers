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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Unsplash Agentic Access
  operation_count: 29
  slug: unsplash-agentic-access
  summary_line: 29 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.unsplash.com
  baseurl_source: declared
  description: Photo collection management
  name: Unsplash Collections API
  slug: unsplash-collections-api
- baseURL: https://api.unsplash.com
  baseurl_source: declared
  description: Authenticated user operations
  name: Unsplash Current User API
  slug: unsplash-current-user-api
- baseURL: https://api.unsplash.com
  baseurl_source: declared
  description: Photo browsing and management operations
  name: Unsplash Photos API
  slug: unsplash-photos-api
- baseURL: https://api.unsplash.com
  baseurl_source: declared
  description: Search photos, collections, and users
  name: Unsplash Search API
  slug: unsplash-search-api
- baseURL: https://api.unsplash.com
  baseurl_source: declared
  description: Platform statistics
  name: Unsplash Stats API
  slug: unsplash-stats-api
- baseURL: https://api.unsplash.com
  baseurl_source: declared
  description: Editorial topic operations
  name: Unsplash Topics API
  slug: unsplash-topics-api
- baseURL: https://api.unsplash.com
  baseurl_source: declared
  description: User profile operations
  name: Unsplash Users API
  slug: unsplash-users-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unsplash Collections API
  slug: open-unsplash-collections-api
- collection_type: open
  name: Unsplash Collections Current User API
  slug: open-unsplash-current-user-api
- collection_type: open
  name: Unsplash Collections Photos API
  slug: open-unsplash-photos-api
- collection_type: open
  name: Unsplash Collections Search API
  slug: open-unsplash-search-api
- collection_type: open
  name: Unsplash Collections Stats API
  slug: open-unsplash-stats-api
- collection_type: open
  name: Unsplash Collections Topics API
  slug: open-unsplash-topics-api
- collection_type: open
  name: Unsplash Collections Users API
  slug: open-unsplash-users-api
- collection_type: open
  name: Unsplash API
  slug: open-unsplash
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unsplash-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unsplash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unsplash-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unsplash-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unsplash-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unsplash
- group: company
  title: ''
  type: Website
  url: https://unsplash.com
- group: docs
  title: ''
  type: Documentation
  url: https://unsplash.com/documentation
- group: other
  title: ''
  type: Developers
  url: https://unsplash.com/developers
- group: docs
  title: ''
  type: Guidelines
  url: https://help.unsplash.com/en/articles/2511245-unsplash-api-guidelines
- group: build
  title: ''
  type: GitHub
  url: https://github.com/unsplash
- group: operate
  title: ''
  type: ChangeLog
  url: https://unsplash.com/documentation/changelog
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/vocabulary/unsplash-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/json-ld/unsplash-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://unsplash.com/blog/rss/
created: '2024-11-13'
description: Unsplash is a platform providing the world's largest collection of high-quality, freely usable photographs. The Unsplash API gives developers programmatic access to search, browse, and retrieve photos, collections, topics, and user profiles. Photos are provided under the Unsplash License. Authentication uses Client-ID for public access or OAuth 2.0 for user-delegated operations.
examples:
- key_count: 2
  name: Unsplash Get Random Photo Example
  slug: unsplash-get-random-photo-example
- key_count: 2
  name: Unsplash Search Photos Example
  slug: unsplash-search-photos-example
finops:
- name: Unsplash Finops
  service_category: API
  slug: unsplash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unsplash.png
json_schemas:
- name: Unsplash Photo
  property_count: 20
  slug: unsplash-photo
json_structures:
- name: Unsplash Photo Structure
  property_count: 0
  slug: unsplash-photo-structure
jsonld:
- class_count: 11
  name: Unsplash Context
  property_count: 42
  slug: unsplash-context
layout: provider
modified: '2026-05-19'
name: Unsplash
nav: Providers
network: true
overview: 'Unsplash publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Current User API, Photos API, and 4 more. Tagged areas include Photos, Image, Photography, Stock Photos, and Creative.


  The Unsplash catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Unsplash''s developer surface includes authentication, documentation, GitHub presence, changelog, engineering blog, and 10 more developer resources.'
plans:
- name: Unsplash Plans Pricing
  plan_count: 3
  slug: unsplash-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Unsplash Rate Limits
  slug: unsplash-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Unsplash API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: unsplash-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Unsplash API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: unsplash-rules
scopes:
- name: Unsplash Scopes
  scope_count: 8
  slug: unsplash-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 72.5
    catalog_earned_first_party: 0.0
    catalog_gap: 42.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 72.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 28.9
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unsplash/refs/heads/main/screenshots/unsplash-2026-08-17T082634.png
security:
- kind: authentication
  name: Unsplash Authentication
  slug: unsplash-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Unsplash Domain Security
  slug: unsplash-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unsplash Vulnerability Disclosure
  slug: unsplash-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: unsplash
tags:
- Photos
- Image
- Photography
- Stock Photos
- Creative
- Open-Source
- Media
website: https://unsplash.com
---
