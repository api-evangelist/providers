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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: The Open Movie Database Agentic Access
  operation_count: 2
  slug: the-open-movie-database-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Retrieve movie, series, and episode details by ID or title.
  name: The Open Movie Database Movies API
  slug: the-open-movie-database-movies-api
- description: Search for movies and series by title.
  name: The Open Movie Database Search API
  slug: the-open-movie-database-search-api
artifact_total: 15
collections:
- collection_type: open
  name: The Open Movie Database API
  slug: open-the-open-movie-database
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-open-movie-database-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-open-movie-database-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-open-movie-database-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omdbapi
- group: company
  title: ''
  type: Website
  url: https://www.omdbapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.omdbapi.com/
- group: start
  title: ''
  type: Signup
  url: https://www.omdbapi.com/apikey.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.omdbapi.com/legal.htm
created: '2025-03-01'
description: The OMDb API is a RESTful web service to obtain movie, series, and episode information. All content and images on the site are contributed and maintained by users. Access movie and TV metadata including title, year, genre, director, cast, plot, ratings, and IMDb data. Search by title or look up by IMDb ID. Requires a free API key obtained at omdbapi.com/apikey.aspx.
examples:
- key_count: 2
  name: The Open Movie Database Get Movie Example
  slug: the-open-movie-database-get-movie-example
finops:
- name: The Open Movie Database Finops
  service_category: API
  slug: the-open-movie-database-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-open-movie-database.png
json_schemas:
- name: OMDb Movie
  property_count: 29
  slug: the-open-movie-database-movie
json_structures:
- name: The Open Movie Database Movie Structure
  property_count: 0
  slug: the-open-movie-database-movie-structure
jsonld:
- class_count: 30
  name: The Open Movie Database Context
  property_count: 7
  slug: the-open-movie-database-context
layout: provider
modified: '2026-05-19'
name: The Open Movie Database
nav: Providers
network: true
overview: 'The Open Movie Database publishes 2 APIs on the [APIs.io](https://apis.io/) network: Movies API and Search API. Tagged areas include Entertainment, Movies, Television, IMDb, and Metadata.


  The The Open Movie Database catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Open Movie Database''s developer surface includes authentication, documentation, signup flow, and 5 more developer resources.'
plans:
- name: The Open Movie Database Plans Pricing
  plan_count: 3
  slug: the-open-movie-database-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: The Open Movie Database Rate Limits
  slug: the-open-movie-database-rate-limits
rules:
- name: The Open Movie Database API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: the-open-movie-database-jsonschema-spectral-rules
- name: The Open Movie Database API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 3
  slug: the-open-movie-database-rules
score:
  band: developing
  composite: 50.6
  delta: -3.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-open-movie-database/refs/heads/main/screenshots/the-open-movie-database-2026-06-20T195233.png
security:
- kind: authentication
  name: The Open Movie Database Authentication
  slug: the-open-movie-database-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The Open Movie Database Domain Security
  slug: the-open-movie-database-domain-security
  summary_line: TLSv1.3 · DMARC
slug: the-open-movie-database
tags:
- Entertainment
- Movies
- Television
- IMDb
- Metadata
website: https://www.omdbapi.com/
---
