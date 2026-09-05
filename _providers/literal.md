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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
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
random_paper: 14
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 48.9
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 37.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
