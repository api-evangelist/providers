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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: GraphQL API for Literal Club that provides access to book data, reading states, shelves, reviews, highlights, reading goals, clubs, and user profiles. Supports both public read operations and authenti
  name: Literal GraphQL API
  slug: literal-graphql-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/literal-domain-security.yml
- group: start
  title: ''
  type: Signup
  url: https://literal.club/
- group: operate
  title: ''
  type: Developer Community
  url: https://literal.club/clubs/dev
- group: operate
  title: ''
  type: Support
  url: mailto:support@literal.club
- group: commercial
  title: ''
  type: TermsOfService
  url: https://literal.club/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://literal.club/pages/privacy
created: '2026-06-13'
description: Literal is a modern social reading and book tracking platform that provides a GraphQL API for managing reading lists, reviews, shelves, reading goals, highlights, and book recommendations. The API enables developers to access user libraries, reading states, book data, author information, and social reading clubs.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: 'Literal exposes a public GraphQL API for searching books, managing reading lists, building widgets, and creating integrations. All data on Literal is accessible through this API. Most read operations '
  name: Literal GraphQL API
  slug: literal-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/literal.png
jsonld:
- class_count: 11
  name: Literal Context
  property_count: 37
  slug: literal-context
layout: provider
modified: '2026-06-13'
name: Literal Club
nav: Providers
network: true
overview: 'Literal Club publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Books, Reading, Social, GraphQL, and Book Tracking.


  The Literal Club catalog on APIs.io includes 1 JSON-LD context.


  Literal Club''s developer surface includes signup flow, support, and 4 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 29
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 56.8
    developer_ergonomics: 4.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 34.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/literal/refs/heads/main/screenshots/literal-2026-06-20T184602.png
security:
- kind: domain-security
  name: Literal Domain Security
  slug: literal-domain-security
  summary_line: TLSv1.3
slug: literal
tags:
- Books
- Reading
- Social
- GraphQL
- Book Tracking
- Reading Lists
- Shelves
- Reviews
- Highlights
- Reading Goals
- Book Clubs
- Recommendations
---
