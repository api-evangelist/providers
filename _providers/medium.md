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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Medium Agentic Access
  operation_count: 9
  slug: medium-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 6
apis:
- description: Endpoints for initiating the OAuth2 authorization flow by redirecting users to Medium's authorization page.
  name: medium Authorization API
  slug: medium-authorization-api
- description: Operations for uploading images to Medium for use in posts. Supports JPEG, PNG, GIF, and TIFF formats.
  name: medium Images API
  slug: medium-images-api
- description: Operations for creating new posts on a user's profile or within a publication, supporting HTML and Markdown content formats.
  name: medium Posts API
  slug: medium-posts-api
- description: Operations for listing publications a user is associated with and retrieving contributors for a given publication.
  name: medium Publications API
  slug: medium-publications-api
- description: Endpoints for exchanging authorization codes for access tokens and refreshing expired access tokens.
  name: medium Tokens API
  slug: medium-tokens-api
- description: Operations for retrieving authenticated user profile information including username, name, URL, and avatar image.
  name: medium Users API
  slug: medium-users-api
artifact_total: 19
collections:
- collection_type: open
  name: Medium OAuth2 API
  slug: open-medium-oauth2
- collection_type: open
  name: Medium REST API
  slug: open-medium-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/medium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medium-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/medium-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medium-com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/medium-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/medium-post-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/medium-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/medium-publication-schema.json
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/blog
description: Documentation for Medium's OAuth2 API. Contribute to Medium/medium-api-docs development by creating an account on GitHub.
finops:
- name: Medium Finops
  service_category: API
  slug: medium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medium.png
json_schemas:
- name: Medium Post
  property_count: 14
  slug: medium-post
- name: Medium Publication
  property_count: 6
  slug: medium-publication
- name: Medium User
  property_count: 5
  slug: medium-user
jsonld:
- class_count: 0
  name: Medium Context
  property_count: 5
  slug: medium-context
layout: provider
modified: '2026-05-19'
name: medium
nav: Providers
network: true
overview: 'medium publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Images API, Posts API, and 3 more.


  The medium catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  medium''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Medium Plans Pricing
  plan_count: 3
  slug: medium-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Medium Rate Limits
  slug: medium-rate-limits
rules:
- name: medium API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: medium-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.4
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medium/refs/heads/main/screenshots/medium-2026-06-20T185123.png
security:
- kind: authentication
  name: Medium Authentication
  slug: medium-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Medium Domain Security
  slug: medium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: medium
---
