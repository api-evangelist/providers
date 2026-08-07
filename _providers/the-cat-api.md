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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: The Cat Api Agentic Access
  operation_count: 17
  slug: the-cat-api-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 5
apis:
- description: List, search, and retrieve cat breed information.
  name: The Cat API Breeds API
  slug: the-cat-api-breeds-api
- description: Retrieve available image categories.
  name: The Cat API Categories API
  slug: the-cat-api-categories-api
- description: Manage user favourite cat images.
  name: The Cat API Favourites API
  slug: the-cat-api-favourites-api
- description: Search, upload, retrieve, and delete cat images.
  name: The Cat API Images API
  slug: the-cat-api-images-api
- description: Cast and manage votes on cat images.
  name: The Cat API Votes API
  slug: the-cat-api-votes-api
artifact_total: 21
collections:
- collection_type: open
  name: The Cat API
  slug: open-the-cat-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-cat-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-cat-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-cat-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://thecatapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thecatapi.com/
- group: start
  title: ''
  type: Signup
  url: https://account.thecatapi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thatapicompany
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/the-cat-api/refs/heads/main/openapi/the-cat-api-openapi.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://thecatapi.com/pricing
created: '2025-01-07'
description: An open, free, read and write API all about cats. Access thousands of cat images, vote, favorite, and explore breed information.
examples:
- key_count: 2
  name: The Cat Api Createvote Example
  slug: the-cat-api-createVote-example
- key_count: 2
  name: The Cat Api Listbreeds Example
  slug: the-cat-api-listBreeds-example
- key_count: 2
  name: The Cat Api Searchimages Example
  slug: the-cat-api-searchImages-example
finops:
- name: The Cat Api Finops
  service_category: API
  slug: the-cat-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-cat-api.png
json_schemas:
- name: Cat API Breed
  property_count: 26
  slug: the-cat-api-breed
- name: Cat API Image
  property_count: 6
  slug: the-cat-api-image
json_structures:
- name: The Cat Api Image Search Structure
  property_count: 0
  slug: the-cat-api-image-search-structure
jsonld:
- class_count: 3
  name: The Cat Api Context
  property_count: 21
  slug: the-cat-api-context
layout: provider
modified: '2026-05-19'
name: The Cat API
nav: Providers
network: true
overview: 'The Cat API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Breeds API, Categories API, Favourites API, and 2 more. Tagged areas include Animals, Cats, Images, and Media.


  The The Cat API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Cat API''s developer surface includes authentication, documentation, signup flow, pricing, and 5 more developer resources.'
plans:
- name: The Cat Api Plans Pricing
  plan_count: 3
  slug: the-cat-api-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: The Cat Api Rate Limits
  slug: the-cat-api-rate-limits
rules:
- name: The Cat API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: the-cat-api-jsonschema-spectral-rules
- name: The Cat API API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: the-cat-api-rules
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.2
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-cat-api/refs/heads/main/screenshots/the-cat-api-2026-06-20T195216.png
security:
- kind: authentication
  name: The Cat Api Authentication
  slug: the-cat-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The Cat Api Domain Security
  slug: the-cat-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: the-cat-api
tags:
- Animals
- Cats
- Images
- Media
website: https://thecatapi.com/
---
