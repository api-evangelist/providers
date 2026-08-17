---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Jsonplaceholder Agentic Access
  operation_count: 41
  slug: jsonplaceholder-agentic-access
  summary_line: 41 operations · 24 acting
api_count: 6
apis:
- description: 100 sample photo albums owned by users
  name: JSONPlaceholder Albums API
  slug: jsonplaceholder-albums-api
- description: 500 sample comments belonging to posts
  name: JSONPlaceholder Comments API
  slug: jsonplaceholder-comments-api
- description: 5000 sample photos belonging to albums
  name: JSONPlaceholder Photos API
  slug: jsonplaceholder-photos-api
- description: 100 sample blog posts owned by users
  name: JSONPlaceholder Posts API
  slug: jsonplaceholder-posts-api
- description: 200 sample todo items owned by users
  name: JSONPlaceholder Todos API
  slug: jsonplaceholder-todos-api
- description: 10 sample users with profile, address, and company metadata
  name: JSONPlaceholder Users API
  slug: jsonplaceholder-users-api
artifact_total: 65
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: JSONPlaceholder REST Albums API
  slug: open-jsonplaceholder-albums-api
- collection_type: open
  name: JSONPlaceholder REST Albums Comments API
  slug: open-jsonplaceholder-comments-api
- collection_type: open
  name: JSONPlaceholder REST Albums Photos API
  slug: open-jsonplaceholder-photos-api
- collection_type: open
  name: JSONPlaceholder REST Albums Posts API
  slug: open-jsonplaceholder-posts-api
- collection_type: open
  name: JSONPlaceholder REST Albums Todos API
  slug: open-jsonplaceholder-todos-api
- collection_type: open
  name: JSONPlaceholder REST Albums Users API
  slug: open-jsonplaceholder-users-api
- collection_type: open
  name: JSONPlaceholder REST API
  slug: open-jsonplaceholder
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/typicode/jsonplaceholder/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/typicode/jsonplaceholder/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jsonplaceholder-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jsonplaceholder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jsonplaceholder.typicode.com
- group: start
  title: ''
  type: GettingStarted
  url: https://jsonplaceholder.typicode.com/guide/
- group: build
  title: JSONPlaceholder Source
  type: GitHubRepository
  url: https://github.com/typicode/jsonplaceholder
- group: build
  title: json-server (Engine)
  type: GitHubRepository
  url: https://github.com/typicode/json-server
- group: build
  title: lowdb (Storage)
  type: GitHubRepository
  url: https://github.com/typicode/lowdb
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/typicode
- group: company
  title: ''
  type: Blog
  url: https://blog.typicode.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/jsonplaceholder-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jsonplaceholder-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/jsonplaceholder-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/jsonplaceholder-vocabulary.yml
- group: docs
  title: ''
  type: Documentation
  url: https://jsonplaceholder.typicode.com/guide/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/typicode
- group: commercial
  title: ''
  type: Pricing
  url: https://jsonplaceholder.typicode.com
- group: other
  title: ''
  type: X
  url: https://x.com/typicode
- group: commercial
  title: ''
  type: FinOps
  url: finops/jsonplaceholder-finops.yml
created: '2026-05-28'
description: JSONPlaceholder is a free, no-auth fake REST API for prototyping, tutorials, and testing. It exposes six relational resources — posts, comments, albums, photos, todos, and users — over six standard REST routes per resource. All write operations (POST, PUT, PATCH, DELETE) are accepted and respond as if successful, but no changes are persisted. The service is built on the open-source json-server engine (also by typicode) and serves billions of requests per month with no rate limits or authentication.
examples:
- key_count: 3
  name: Create Post Request
  slug: create-post-request
- key_count: 4
  name: Create Post Response
  slug: create-post-response
- key_count: 3
  name: Jsonplaceholder Album Example
  slug: jsonplaceholder-album-example
- key_count: 5
  name: Jsonplaceholder Comment Example
  slug: jsonplaceholder-comment-example
- key_count: 5
  name: Jsonplaceholder Photo Example
  slug: jsonplaceholder-photo-example
- key_count: 4
  name: Jsonplaceholder Post Example
  slug: jsonplaceholder-post-example
- key_count: 4
  name: Jsonplaceholder Todo Example
  slug: jsonplaceholder-todo-example
- key_count: 8
  name: Jsonplaceholder User Example
  slug: jsonplaceholder-user-example
features:
- description: Posts, comments, albums, photos, todos, and users with realistic relationships between them (posts belong to users, comments belong to posts, etc.).
  name: Six Relational Resources
- description: GET, POST, PUT, PATCH, and DELETE methods are accepted on every resource — write operations simulate success without persisting changes.
  name: Full REST Surface
- description: Single-level nested access such as /posts/1/comments, /albums/1/photos, and /users/1/todos for relational queries.
  name: Nested Routes
- description: Basic query-string filtering on any resource field (e.g. /comments?postId=1, /posts?userId=1).
  name: Query Filtering
- description: Open to the public — no API keys, OAuth, or signup required. Use it in tutorials, sandboxes, and frontend demos freely.
  name: No Authentication
- description: The service does not publish or enforce documented rate limits and routinely serves about three billion requests per month.
  name: No Rate Limits
- description: All origins are allowed, making the service usable directly from browser-based applications without a proxy.
  name: CORS Enabled
- description: Served exclusively over HTTPS for safe inclusion in modern web tutorials and demos.
  name: HTTPS Only
finops:
- name: Jsonplaceholder Finops
  service_category: ''
  slug: jsonplaceholder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jsonplaceholder.png
integrations:
- description: The open-source engine that powers JSONPlaceholder — runs the same fake REST API locally with a single command.
  name: json-server
- description: The tiny local JSON database that json-server uses for storage; ships from the same typicode org.
  name: lowdb
- description: Public collections wrap JSONPlaceholder for quick HTTP exploration and learning.
  name: Postman
- description: Frequently used as the default example endpoint in HTTP clients including Hoppscotch and Insomnia.
  name: Hoppscotch
- description: Often paired with MSW so frontend tests can intercept and stub JSONPlaceholder traffic deterministically.
  name: MSW (Mock Service Worker)
json_schemas:
- name: Album
  property_count: 3
  slug: jsonplaceholder-album
- name: Comment
  property_count: 5
  slug: jsonplaceholder-comment
- name: Photo
  property_count: 5
  slug: jsonplaceholder-photo
- name: Post
  property_count: 4
  slug: jsonplaceholder-post
- name: Todo
  property_count: 4
  slug: jsonplaceholder-todo
- name: User
  property_count: 8
  slug: jsonplaceholder-user
- name: Post
  property_count: 4
  slug: post
json_structures:
- name: Jsonplaceholder Album Structure
  property_count: 3
  slug: jsonplaceholder-album-structure
- name: Jsonplaceholder Comment Structure
  property_count: 5
  slug: jsonplaceholder-comment-structure
- name: Jsonplaceholder Photo Structure
  property_count: 5
  slug: jsonplaceholder-photo-structure
- name: Jsonplaceholder Post Structure
  property_count: 4
  slug: jsonplaceholder-post-structure
- name: Jsonplaceholder Todo Structure
  property_count: 4
  slug: jsonplaceholder-todo-structure
- name: Jsonplaceholder User Structure
  property_count: 8
  slug: jsonplaceholder-user-structure
jsonld:
- class_count: 1
  name: context Context
  property_count: 4
  slug: context
- class_count: 9
  name: Jsonplaceholder Context
  property_count: 26
  slug: jsonplaceholder-context
layout: provider
modified: '2026-08-08'
name: JSONPlaceholder
nav: Providers
network: true
overview: 'JSONPlaceholder publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Albums API, Comments API, Photos API, and 3 more. Tagged areas include Development, Testing, Prototyping, Fake API, and Open Source.


  The JSONPlaceholder catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  JSONPlaceholder''s developer surface includes getting-started guide, engineering blog, documentation, pricing, and 17 more developer resources.'
plans:
- name: Jsonplaceholder Plans Pricing
  plan_count: 1
  slug: jsonplaceholder-plans-pricing
random_paper: 107
rate_limits:
- limit_count: 2
  name: Jsonplaceholder Rate Limits
  slug: jsonplaceholder-rate-limits
rules:
- name: JSONPlaceholder API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jsonplaceholder-jsonschema-spectral-rules
- name: JSONPlaceholder API Rules
  rule_count: 34
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 18
  slug: jsonplaceholder-rules
score:
  band: thin
  composite: 39.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 29.0
    developer_ergonomics: 21.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jsonplaceholder/refs/heads/main/screenshots/jsonplaceholder-2026-06-20T183819.png
security:
- kind: domain-security
  name: Jsonplaceholder Domain Security
  slug: jsonplaceholder-domain-security
  summary_line: TLSv1.3
slug: jsonplaceholder
solutions:
- description: For teams that need write persistence or offline development, install json-server, point it at a local db.json, and reproduce JSONPlaceholder routes verbatim.
  name: Local Mirror via json-server
- description: typicode operates an additional service (My JSON Server) that turns any GitHub-hosted db.json into a personal hosted fake REST API.
  name: My JSON Server
tags:
- Development
- Testing
- Prototyping
- Fake API
- Open Source
- REST
use_cases:
- description: Wire up React, Vue, Angular, or Svelte tutorials against a real HTTP endpoint without standing up a backend.
  name: Frontend Prototyping
- description: Exercise HTTP client libraries (fetch, axios, requests, OkHttp) against a stable public REST surface.
  name: API Client Testing
- description: Power coding tutorials, bootcamp exercises, and conference workshops that need a deterministic JSON API.
  name: Tutorial and Courseware
- description: Drive iOS and Android sample apps that demonstrate networking, list rendering, and CRUD flows.
  name: Mobile App Demos
- description: Smoke-test API generators, codegen tools, SDK builders, and OpenAPI tooling against a stable real-world API.
  name: Tooling QA
- description: Provide a no-signup HTTP API for hands-on workshops where participants cannot wait for credentials.
  name: Workshop Sandboxes
website: https://jsonplaceholder.typicode.com
---
