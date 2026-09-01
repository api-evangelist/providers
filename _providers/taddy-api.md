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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Taddy Api Agentic Access
  operation_count: 1
  slug: taddy-api-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: GraphQL API for accessing comic book series, issues, and creator data from the Taddy comic book database.
  name: Taddy Comics API
  slug: taddy-comics-api
- description: The GraphQL API from Taddy API — 1 operation(s) for graphql.
  name: Taddy API GraphQL API
  slug: taddy-api-graphql-api
artifact_total: 21
collections:
- collection_type: postman
  name: Taddy Podcast GraphQL API
  slug: postman-taddy-api-graphql-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Taddy Podcast GraphQL API
  slug: open-taddy-api-graphql-api
- collection_type: open
  name: Taddy Podcast API
  slug: open-taddy-podcast
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/taddy-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taddy-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taddy-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taddy-api-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/taddy-developers
- group: start
  title: ''
  type: Portal
  url: https://taddy.org/developers
- group: docs
  title: ''
  type: Documentation
  url: https://taddy.org/developers/podcast-api
- group: start
  title: ''
  type: GettingStarted
  url: https://taddy.org/developers/intro-to-taddy-graphql-api
- group: start
  title: ''
  type: Signup
  url: https://taddy.org/register
- group: company
  title: ''
  type: Website
  url: https://taddy.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://taddy.org/developers#pricing
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/taddyorg
- group: build
  title: ''
  type: Example Project
  url: https://github.com/taddyorg/taddy-api-example-project
- group: other
  title: ''
  type: Dataset Export
  url: https://github.com/taddyorg/podcast-dataset-export
- group: design
  title: ''
  type: Webhooks
  url: https://github.com/taddyorg/webhook-example-taddy
- group: build
  title: ''
  type: n8n Integration
  url: https://github.com/taddyorg/podcast-data-n8n-integration
- group: build
  title: ''
  type: Zapier Integration
  url: https://github.com/taddyorg/podcast-data-zapier-integration
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/json-schema/taddy-podcast-series-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/json-schema/taddy-podcast-episode-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/vocabulary/taddy-api-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://taddy.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://taddy.org/blog
created: '2025-05-02'
description: Taddy provides a GraphQL-based podcast API giving developers access to over 4 million podcasts and 200 million episodes with real-time search, episode transcripts, webhooks, top charts, and comic book data. Taddy simplifies building podcast applications by aggregating and standardizing RSS feed data at scale with daily updates of 1,000 new podcasts and 50,000 new episodes.
examples:
- key_count: 2
  name: Taddy Execute Graphql Query Example
  slug: taddy-execute-graphql-query-example
finops:
- name: Taddy Api Finops
  service_category: API
  slug: taddy-api-finops
graphqls:
- description: GraphQL API providing access to over 4 million podcasts and 200 million episodes. Supports podcast and episode search, transcript retrieval with speaker and timecode data, top charts by country, webho
  name: Taddy API GraphQL API
  slug: taddy-api-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taddy-api.png
json_schemas:
- name: Podcast Episode
  property_count: 25
  slug: taddy-podcast-episode
- name: Podcast Series
  property_count: 25
  slug: taddy-podcast-series
json_structures:
- name: Taddy Podcast Episode Structure
  property_count: 0
  slug: taddy-podcast-episode-structure
- name: Taddy Podcast Series Structure
  property_count: 0
  slug: taddy-podcast-series-structure
jsonld:
- class_count: 4
  name: Taddy Api Context
  property_count: 41
  slug: taddy-api-context
layout: provider
modified: '2026-05-19'
name: Taddy API
nav: Providers
network: true
overview: 'Taddy API publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Audio, Comics, GraphQL, Media, and Podcasts.


  The Taddy API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Taddy API''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Taddy Api Plans Pricing
  plan_count: 3
  slug: taddy-api-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Taddy Api Rate Limits
  slug: taddy-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Taddy API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: taddy-api-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Taddy API API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: taddy-api-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 21.1
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taddy-api/refs/heads/main/screenshots/taddy-api-2026-06-20T194850.png
security:
- kind: authentication
  name: Taddy Api Authentication
  slug: taddy-api-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Taddy Api Domain Security
  slug: taddy-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: taddy-api
tags:
- Audio
- Comics
- GraphQL
- Media
- Podcasts
- Transcripts
- Webhook
website: https://taddy.org/
---
