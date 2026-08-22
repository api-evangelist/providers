---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rottentomatoes Agentic Access
  operation_count: 18
  slug: rottentomatoes-agentic-access
  summary_line: 18 operations
api_count: 5
apis:
- description: The Detailed Info API from Rotten Tomatoes — 6 operation(s) for detailed info.
  name: Rotten Tomatoes Detailed Info API
  slug: rottentomatoes-detailed-info-api
- description: The DVD Lists API from Rotten Tomatoes — 4 operation(s) for dvd lists.
  name: Rotten Tomatoes DVD Lists API
  slug: rottentomatoes-dvd-lists-api
- description: The Movie Lists API from Rotten Tomatoes — 4 operation(s) for movie lists.
  name: Rotten Tomatoes Movie Lists API
  slug: rottentomatoes-movie-lists-api
- description: The Search API from Rotten Tomatoes — 1 operation(s) for search.
  name: Rotten Tomatoes Search API
  slug: rottentomatoes-search-api
- description: The Top Level Lists API from Rotten Tomatoes — 3 operation(s) for top level lists.
  name: Rotten Tomatoes Top Level Lists API
  slug: rottentomatoes-top-level-lists-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rotten Tomatoes Detailed Info API
  slug: open-rottentomatoes-detailed-info-api
- collection_type: open
  name: Rotten Tomatoes Detailed Info DVD Lists API
  slug: open-rottentomatoes-dvd-lists-api
- collection_type: open
  name: Rotten Tomatoes Detailed Info Movie Lists API
  slug: open-rottentomatoes-movie-lists-api
- collection_type: open
  name: Rotten Tomatoes Detailed Info Search API
  slug: open-rottentomatoes-search-api
- collection_type: open
  name: Rotten Tomatoes Detailed Info Top Level Lists API
  slug: open-rottentomatoes-top-level-lists-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rottentomatoes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rottentomatoes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rottentomatoes-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://editorial.rottentomatoes.com/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fandango.com/rotten_tomatoes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.fandango.com/Fandango_Terms_of_Service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.versantprivacy.com/privacy
- group: other
  title: ''
  type: Licensing
  url: https://www.rottentomatoes.com/help_desk/licensing
- group: operate
  title: ''
  type: Contact
  url: https://support.fandango.com/en_us/contact/contact-us-fandango-rkksORSDO?from=RT
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/api-evangelist/rotten-tomatoes/overview
- group: build
  title: ''
  type: GitHub
  url: https://github.com/api-evangelist/rotten-tomatoes
created: '2026-06-13'
description: Rotten Tomatoes is the leading movie and TV review aggregation platform, providing Tomatometer scores, Audience Scores, critic consensus summaries, and review snippets for movies and television shows. The Rotten Tomatoes API enables approved partners to access Tomatometer and Audience scores, critic and audience reviews, box office lists, movie details, cast information, DVD release data, and search capabilities. API access is managed through the Fandango Developer Network and requires an approved application and a paid license agreement starting at $60,000 annually.
examples:
- key_count: 2
  name: Cast
  slug: cast
- key_count: 4
  name: Movie List
  slug: movie-list
- key_count: 13
  name: Movie
  slug: movie
- key_count: 4
  name: Review List
  slug: review-list
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rottentomatoes.png
json_schemas:
- name: Cast
  property_count: 2
  slug: cast
- name: MovieList
  property_count: 4
  slug: movie-list
- name: Movie
  property_count: 13
  slug: movie
- name: Review
  property_count: 6
  slug: review
jsonld:
- class_count: 0
  name: Movie Context
  property_count: 0
  slug: movie
layout: provider
modified: '2026-06-13'
name: Rotten Tomatoes
nav: Providers
network: true
overview: 'Rotten Tomatoes publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Detailed Info API, DVD Lists API, Movie Lists API, and 2 more. Tagged areas include Movies, Television, Reviews, Ratings, and Tomatometer.


  The Rotten Tomatoes catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rotten Tomatoes'' developer surface includes authentication, engineering blog, documentation, GitHub presence, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 11
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Rotten Tomatoes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: rottentomatoes-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.9
  delta: -7.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 47.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rottentomatoes/refs/heads/main/screenshots/rottentomatoes-2026-08-17T081638.png
security:
- kind: authentication
  name: Rottentomatoes Authentication
  slug: rottentomatoes-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rottentomatoes Domain Security
  slug: rottentomatoes-domain-security
  summary_line: DMARC
slug: rottentomatoes
tags:
- Movies
- Television
- Reviews
- Ratings
- Tomatometer
- Audience Score
- Entertainment
- Media
---
