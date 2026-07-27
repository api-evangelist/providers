---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 45.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dog Api Agentic Access
  operation_count: 24
  slug: dog-api-agentic-access
  summary_line: 24 operations
api_count: 3
apis:
- description: List and look up master breeds and their sub-breeds.
  name: Dog API Breeds API
  slug: dog-api-breeds-api
- description: Fetch random or breed-specific dog images (with optional alt text).
  name: Dog API Images API
  slug: dog-api-images-api
- description: Look up free-text breed information where available.
  name: Dog API Info API
  slug: dog-api-info-api
artifact_total: 40
collections:
- collection_type: open
  name: Dog API
  slug: open-dog-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dog-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dog-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dog.ceo
- group: docs
  title: ''
  type: Documentation
  url: https://dog.ceo/dog-api/documentation
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ElliottLandsborough/dog-ceo-api
- group: commercial
  title: ''
  type: License
  url: https://opensource.org/licenses/MIT
- group: build
  title: MCP Server (Community)
  type: Tools
  url: https://github.com/JithunMethusahan/dog-api-mcp-community
- group: build
  title: p5.js Example
  type: CodeExamples
  url: https://editor.p5js.org/codingtrain/sketches/lQxT7PTKC
- group: build
  title: Vanilla JS Example
  type: CodeExamples
  url: https://codepen.io/elliottlan/pen/MNEWNx
- group: build
  title: jQuery Example
  type: CodeExamples
  url: https://codepen.io/elliottlan/pen/KOXKLG
- group: build
  title: Flutter Example
  type: CodeExamples
  url: https://github.com/LIVELUCKY/dogs
- group: build
  title: Node.js Example
  type: CodeExamples
  url: https://github.com/mrbrunelli/dog-time-decorator
created: '2024-11-14'
description: The internet's biggest collection of open-source dog pictures. Fetching over 20,000 dog images accessible by more than 120 breeds via a free, no-auth REST API returning JSON. Optional alt-text variants pair every image URL with descriptive text for accessibility.
examples:
- key_count: 2
  name: Breed Images
  slug: breed-images
- key_count: 2
  name: Dog Api Alt Image Example
  slug: dog-api-alt-image-example
- key_count: 2
  name: Dog Api Alt Image List Response Example
  slug: dog-api-alt-image-list-response-example
- key_count: 2
  name: Dog Api Breed List Response Example
  slug: dog-api-breed-list-response-example
- key_count: 3
  name: Dog Api Error Response Example
  slug: dog-api-error-response-example
- key_count: 2
  name: Dog Api Image List Response Example
  slug: dog-api-image-list-response-example
- key_count: 2
  name: Dog Api Image Response Example
  slug: dog-api-image-response-example
- key_count: 2
  name: Dog Api String List Response Example
  slug: dog-api-string-list-response-example
- key_count: 2
  name: Dog Api String Response Example
  slug: dog-api-string-response-example
- key_count: 2
  name: List All Breeds
  slug: list-all-breeds
- key_count: 2
  name: Random Image
  slug: random-image
finops:
- name: Dog Api Finops
  service_category: API
  slug: dog-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dog-api.png
json_schemas:
- name: AltImageListResponse
  property_count: 2
  slug: dog-api-alt-image-list-response
- name: AltImage
  property_count: 2
  slug: dog-api-alt-image
- name: BreedListResponse
  property_count: 2
  slug: dog-api-breed-list-response
- name: ErrorResponse
  property_count: 3
  slug: dog-api-error-response
- name: ImageListResponse
  property_count: 2
  slug: dog-api-image-list-response
- name: ImageResponse
  property_count: 2
  slug: dog-api-image-response
- name: StringListResponse
  property_count: 2
  slug: dog-api-string-list-response
- name: StringResponse
  property_count: 2
  slug: dog-api-string-response
json_structures:
- name: Dog Api Alt Image List Response Structure
  property_count: 2
  slug: dog-api-alt-image-list-response-structure
- name: Dog Api Alt Image Structure
  property_count: 2
  slug: dog-api-alt-image-structure
- name: Dog Api Breed List Response Structure
  property_count: 2
  slug: dog-api-breed-list-response-structure
- name: Dog Api Error Response Structure
  property_count: 3
  slug: dog-api-error-response-structure
- name: Dog Api Image List Response Structure
  property_count: 2
  slug: dog-api-image-list-response-structure
- name: Dog Api Image Response Structure
  property_count: 2
  slug: dog-api-image-response-structure
- name: Dog Api String List Response Structure
  property_count: 2
  slug: dog-api-string-list-response-structure
- name: Dog Api String Response Structure
  property_count: 2
  slug: dog-api-string-response-structure
jsonld:
- class_count: 9
  name: Dog Api Context
  property_count: 4
  slug: dog-api-context
- class_count: 10
  name: Dog Api Context
  property_count: 0
  slug: dog-api
layout: provider
modified: '2026-05-30'
name: Dog API
nav: Providers
network: true
overview: 'Dog API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Breeds API, Images API, and Info API. Tagged areas include Dogs, Images, Open Data, and Open Source.


  The Dog API catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Dog API''s developer surface includes documentation, GitHub presence, tooling, code examples, and 8 more developer resources.'
plans:
- name: Dog Api Plans Pricing
  plan_count: 3
  slug: dog-api-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Dog Api Rate Limits
  slug: dog-api-rate-limits
rules:
- name: Dog API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dog-api-jsonschema-spectral-rules
- name: Dog API API Rules
  rule_count: 34
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 19
  slug: dog-api-rules
score:
  band: developing
  composite: 45.2
  delta: 3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.6
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 41.3
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dog-api/refs/heads/main/screenshots/dog-api-2026-06-20T180122.png
security:
- kind: domain-security
  name: Dog Api Domain Security
  slug: dog-api-domain-security
  summary_line: TLSv1.3
slug: dog-api
tags:
- Dogs
- Images
- Open Data
- Open Source
website: https://dog.ceo
---
