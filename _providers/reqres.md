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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Reqres Agentic Access
  operation_count: 52
  slug: reqres-agentic-access
  summary_line: 52 operations · 27 acting
api_count: 6
apis:
- baseURL: https://reqres.in/
  baseurl_source: declared
  description: Endpoints designed for AI coding agents. Cursor pagination, deeply nested resources, deliberate error scenarios, deterministic seeded fixtures.
  name: ReqRes Agent Sandbox API
  slug: reqres-agent-sandbox-api
- baseURL: https://reqres.in/
  baseurl_source: declared
  description: The App Users API from ReqRes — 13 operation(s) for app users.
  name: ReqRes App Users API
  slug: reqres-app-users-api
- baseURL: https://reqres.in/
  baseurl_source: declared
  description: The Authentication API from ReqRes — 3 operation(s) for authentication.
  name: ReqRes Authentication API
  slug: reqres-authentication-api
- baseURL: https://reqres.in/
  baseurl_source: declared
  description: The Collections API from ReqRes — 4 operation(s) for collections.
  name: ReqRes Collections API
  slug: reqres-collections-api
- baseURL: https://reqres.in/
  baseurl_source: declared
  description: The Custom Endpoints API from ReqRes — 1 operation(s) for custom endpoints.
  name: ReqRes Custom Endpoints API
  slug: reqres-custom-endpoints-api
- baseURL: https://reqres.in/
  baseurl_source: declared
  description: The Legacy API from ReqRes — 4 operation(s) for legacy.
  name: ReqRes Legacy API
  slug: reqres-legacy-api
artifact_total: 167
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ReqRes Agent Sandbox API
  slug: open-reqres-agent-sandbox-api
- collection_type: open
  name: ReqRes Agent Sandbox App Users API
  slug: open-reqres-app-users-api
- collection_type: open
  name: ReqRes Agent Sandbox Authentication API
  slug: open-reqres-authentication-api
- collection_type: open
  name: ReqRes Agent Sandbox Collections API
  slug: open-reqres-collections-api
- collection_type: open
  name: ReqRes Agent Sandbox Custom Endpoints API
  slug: open-reqres-custom-endpoints-api
- collection_type: open
  name: ReqRes Agent Sandbox Legacy API
  slug: open-reqres-legacy-api
- collection_type: open
  name: ReqRes API
  slug: open-reqres
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reqres-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reqres-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reqres-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://reqres.in/
- group: start
  title: ''
  type: GettingStarted
  url: https://reqres.in/
- group: docs
  title: ''
  type: Documentation
  url: https://reqres.in/docs
- group: start
  title: ''
  type: Signup
  url: https://app.reqres.in/
- group: commercial
  title: ''
  type: Pricing
  url: https://reqres.in/pricing
- group: company
  title: ''
  type: Blog
  url: https://reqres.in/blog
- group: build
  title: Demo App (Source)
  type: GitHubRepository
  url: https://github.com/benhowdle89/reqres-demo-app
- group: build
  title: Waitlist Demo (Source)
  type: GitHubRepository
  url: https://github.com/benhowdle89/reqres-waitlist-demo
- group: build
  title: Ben Howdle (Creator)
  type: GitHubUser
  url: https://github.com/benhowdle89
- group: company
  title: Ben Howdle on LinkedIn
  type: LinkedIn
  url: https://www.linkedin.com/in/ben-howdle
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: other
  title: ''
  type: PublicAPIDevListing
  url: https://publicapi.dev/req-res-api
- group: commercial
  title: ''
  type: Plans
  url: plans/reqres-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reqres-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/reqres-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/reqres-vocabulary.yml
created: '2026-05-28'
description: 'ReqRes (reqres.in) is a hosted REST API originally launched by Ben Howdle as a free no-auth fake-API surface for AJAX prototyping, tutorials, and frontend testing. As of the 2025 relaunch it operates as a freemium SaaS product: every request to /api/* and /app/* now requires an x-api-key header obtained via free signup at app.reqres.in, while the /agent/v1/* Agent Sandbox is open in v1 with IP-based rate limiting. The legacy demo surface (/api/users, /api/login, /api/register, /api/unknown, delayed responses) continues to return the same fixture payloads it always has — what changed is the API-key gate and the addition of persistent collections, app users, custom endpoints, and an agent-targeted sandbox with deliberate failure scenarios. ReqRes remains the default fake-API endpoint cited in countless React, Vue, Angular, and bootcamp tutorials.'
examples:
- key_count: 1
  name: Reqres Agent Health Response Example
  slug: reqres-agent-health-response-example
- key_count: 3
  name: Reqres Agent Money Example
  slug: reqres-agent-money-example
- key_count: 6
  name: Reqres Agent Pagination Meta Example
  slug: reqres-agent-pagination-meta-example
- key_count: 1
  name: Reqres Agent User Detail Response Example
  slug: reqres-agent-user-detail-response-example
- key_count: 10
  name: Reqres Agent User Example
  slug: reqres-agent-user-example
- key_count: 2
  name: Reqres Agent User List Response Example
  slug: reqres-agent-user-list-response-example
- key_count: 2
  name: Reqres App User Create Request Example
  slug: reqres-app-user-create-request-example
- key_count: 6
  name: Reqres App User Example
  slug: reqres-app-user-example
- key_count: 1
  name: Reqres App User List Response Example
  slug: reqres-app-user-list-response-example
- key_count: 3
  name: Reqres App User Login Request Example
  slug: reqres-app-user-login-request-example
- key_count: 1
  name: Reqres App User Login Response Example
  slug: reqres-app-user-login-response-example
- key_count: 1
  name: Reqres App User Response Example
  slug: reqres-app-user-response-example
- key_count: 1
  name: Reqres App User Session Response Example
  slug: reqres-app-user-session-response-example
- key_count: 1
  name: Reqres App User Total Response Example
  slug: reqres-app-user-total-response-example
- key_count: 3
  name: Reqres App User Update Request Example
  slug: reqres-app-user-update-request-example
- key_count: 1
  name: Reqres App User Verify Request Example
  slug: reqres-app-user-verify-request-example
- key_count: 1
  name: Reqres App User Verify Response Example
  slug: reqres-app-user-verify-response-example
- key_count: 2
  name: Reqres Auth Request Example
  slug: reqres-auth-request-example
- key_count: 5
  name: Reqres Collection Create Request Example
  slug: reqres-collection-create-request-example
- key_count: 9
  name: Reqres Collection Example
  slug: reqres-collection-example
- key_count: 1
  name: Reqres Collection List Response Example
  slug: reqres-collection-list-response-example
- key_count: 1
  name: Reqres Collection Record Create Request Example
  slug: reqres-collection-record-create-request-example
- key_count: 9
  name: Reqres Collection Record Example
  slug: reqres-collection-record-example
- key_count: 2
  name: Reqres Collection Record List Response Example
  slug: reqres-collection-record-list-response-example
- key_count: 1
  name: Reqres Collection Record Response Example
  slug: reqres-collection-record-response-example
- key_count: 1
  name: Reqres Collection Record Update Request Example
  slug: reqres-collection-record-update-request-example
- key_count: 1
  name: Reqres Collection Response Example
  slug: reqres-collection-response-example
- key_count: 4
  name: Reqres Collection Update Request Example
  slug: reqres-collection-update-request-example
- key_count: 0
  name: Reqres Legacy Mutation Request Example
  slug: reqres-legacy-mutation-request-example
- key_count: 3
  name: Reqres Legacy Mutation Response Example
  slug: reqres-legacy-mutation-response-example
- key_count: 5
  name: Reqres Legacy Unknown Example
  slug: reqres-legacy-unknown-example
- key_count: 6
  name: Reqres Legacy Unknown List Response Example
  slug: reqres-legacy-unknown-list-response-example
- key_count: 2
  name: Reqres Legacy Unknown Response Example
  slug: reqres-legacy-unknown-response-example
- key_count: 5
  name: Reqres Legacy User Example
  slug: reqres-legacy-user-example
- key_count: 6
  name: Reqres Legacy User List Response Example
  slug: reqres-legacy-user-list-response-example
- key_count: 2
  name: Reqres Legacy User Response Example
  slug: reqres-legacy-user-response-example
- key_count: 1
  name: Reqres Login Response Example
  slug: reqres-login-response-example
- key_count: 2
  name: Reqres Register Response Example
  slug: reqres-register-response-example
- key_count: 8
  name: Reqres Template Example
  slug: reqres-template-example
- key_count: 2
  name: Reqres Templates Response Example
  slug: reqres-templates-response-example
features:
- description: Stable /api/users, /api/users/{id}, /api/unknown, /api/unknown/{id} fixture data preserved from the original reqres.in launch — the same payloads tutorials have been wired against for years.
  name: Legacy Demo Fixtures
- description: /api/register, /api/login, and /api/logout return success-shaped tokens without creating real accounts — drop-in for teaching auth patterns without standing up a real identity provider.
  name: Simulated Auth Flows
- description: /api/collections/{slug}/records supports GET/POST/PUT/DELETE with real persistence on paid plans, with custom schemas on the Dev tier and above.
  name: Persistent Collections
- description: /app/* surface lets each app user authenticate independently with a session bearer, so client-side prototypes can model real per-user isolation.
  name: Project-Scoped App Users
- description: /api/custom/{path} executes user-defined endpoints, letting builders shape arbitrary REST surfaces without writing backend code.
  name: Custom Endpoints
- description: /agent/v1/* exposes endpoints designed for AI coding agents — cursor pagination, deeply nested resources, deliberate failure scenarios, and deterministic seeded fixtures.
  name: Agent Sandbox
- description: The Agent Developer plan unlocks 15 failure scenarios on /agent/v1/scenarios so AI agents can be tested against timeouts, rate limits, validation errors, and pagination edge cases.
  name: 15 Deliberate Failure Scenarios
- description: Legacy endpoints accept a ?delay=N query param to simulate slow upstream conditions — useful for spinner/loading-state testing.
  name: Delayed Responses
- description: Served exclusively over HTTPS at reqres.in.
  name: HTTPS Only
- description: All origins are allowed, making ReqRes safe to call directly from browser-based prototypes.
  name: CORS Enabled
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reqres.png
integrations:
- description: Public Postman collections wrap ReqRes endpoints for quick HTTP exploration and learning.
  name: Postman
- description: Frequently used as the default example endpoint in HTTP clients including Hoppscotch and Insomnia.
  name: Hoppscotch
- description: Often paired with MSW so frontend tests can intercept and stub ReqRes traffic deterministically.
  name: MSW (Mock Service Worker)
- description: The /agent/v1/* sandbox is purpose-built for AI coding agents like Claude Code, with deliberate failure scenarios and cursor pagination.
  name: Claude Code / AI Coding Agents
- description: Browser E2E test suites use ReqRes as a stable upstream when writing tests that depend on real network traffic.
  name: Cypress / Playwright
json_schemas:
- name: AgentHealthResponse
  property_count: 1
  slug: reqres-agent-health-response
- name: AgentMoney
  property_count: 3
  slug: reqres-agent-money
- name: AgentPaginationMeta
  property_count: 6
  slug: reqres-agent-pagination-meta
- name: AgentUserDetailResponse
  property_count: 1
  slug: reqres-agent-user-detail-response
- name: AgentUserListResponse
  property_count: 2
  slug: reqres-agent-user-list-response
- name: AgentUser
  property_count: 10
  slug: reqres-agent-user
- name: AppUserCreateRequest
  property_count: 2
  slug: reqres-app-user-create-request
- name: AppUserListResponse
  property_count: 1
  slug: reqres-app-user-list-response
- name: AppUserLoginRequest
  property_count: 3
  slug: reqres-app-user-login-request
- name: AppUserLoginResponse
  property_count: 1
  slug: reqres-app-user-login-response
- name: AppUserResponse
  property_count: 1
  slug: reqres-app-user-response
- name: AppUser
  property_count: 6
  slug: reqres-app-user
- name: AppUserSessionResponse
  property_count: 1
  slug: reqres-app-user-session-response
- name: AppUserTotalResponse
  property_count: 1
  slug: reqres-app-user-total-response
- name: AppUserUpdateRequest
  property_count: 3
  slug: reqres-app-user-update-request
- name: AppUserVerifyRequest
  property_count: 1
  slug: reqres-app-user-verify-request
- name: AppUserVerifyResponse
  property_count: 1
  slug: reqres-app-user-verify-response
- name: AuthRequest
  property_count: 2
  slug: reqres-auth-request
- name: CollectionCreateRequest
  property_count: 5
  slug: reqres-collection-create-request
- name: CollectionListResponse
  property_count: 1
  slug: reqres-collection-list-response
- name: CollectionRecordCreateRequest
  property_count: 1
  slug: reqres-collection-record-create-request
- name: CollectionRecordListResponse
  property_count: 2
  slug: reqres-collection-record-list-response
- name: CollectionRecordResponse
  property_count: 1
  slug: reqres-collection-record-response
- name: CollectionRecord
  property_count: 9
  slug: reqres-collection-record
- name: CollectionRecordUpdateRequest
  property_count: 1
  slug: reqres-collection-record-update-request
- name: CollectionResponse
  property_count: 1
  slug: reqres-collection-response
- name: Collection
  property_count: 9
  slug: reqres-collection
- name: CollectionUpdateRequest
  property_count: 4
  slug: reqres-collection-update-request
- name: LegacyMutationRequest
  property_count: 0
  slug: reqres-legacy-mutation-request
- name: LegacyMutationResponse
  property_count: 3
  slug: reqres-legacy-mutation-response
- name: LegacyUnknownListResponse
  property_count: 6
  slug: reqres-legacy-unknown-list-response
- name: LegacyUnknownResponse
  property_count: 2
  slug: reqres-legacy-unknown-response
- name: LegacyUnknown
  property_count: 5
  slug: reqres-legacy-unknown
- name: LegacyUserListResponse
  property_count: 6
  slug: reqres-legacy-user-list-response
- name: LegacyUserResponse
  property_count: 2
  slug: reqres-legacy-user-response
- name: LegacyUser
  property_count: 5
  slug: reqres-legacy-user
- name: LoginResponse
  property_count: 1
  slug: reqres-login-response
- name: RegisterResponse
  property_count: 2
  slug: reqres-register-response
- name: Template
  property_count: 8
  slug: reqres-template
- name: TemplatesResponse
  property_count: 2
  slug: reqres-templates-response
json_structures:
- name: Reqres Agent Health Response Structure
  property_count: 1
  slug: reqres-agent-health-response-structure
- name: Reqres Agent Money Structure
  property_count: 3
  slug: reqres-agent-money-structure
- name: Reqres Agent Pagination Meta Structure
  property_count: 6
  slug: reqres-agent-pagination-meta-structure
- name: Reqres Agent User Detail Response Structure
  property_count: 1
  slug: reqres-agent-user-detail-response-structure
- name: Reqres Agent User List Response Structure
  property_count: 2
  slug: reqres-agent-user-list-response-structure
- name: Reqres Agent User Structure
  property_count: 10
  slug: reqres-agent-user-structure
- name: Reqres App User Create Request Structure
  property_count: 2
  slug: reqres-app-user-create-request-structure
- name: Reqres App User List Response Structure
  property_count: 1
  slug: reqres-app-user-list-response-structure
- name: Reqres App User Login Request Structure
  property_count: 3
  slug: reqres-app-user-login-request-structure
- name: Reqres App User Login Response Structure
  property_count: 1
  slug: reqres-app-user-login-response-structure
- name: Reqres App User Response Structure
  property_count: 1
  slug: reqres-app-user-response-structure
- name: Reqres App User Session Response Structure
  property_count: 1
  slug: reqres-app-user-session-response-structure
- name: Reqres App User Structure
  property_count: 6
  slug: reqres-app-user-structure
- name: Reqres App User Total Response Structure
  property_count: 1
  slug: reqres-app-user-total-response-structure
- name: Reqres App User Update Request Structure
  property_count: 3
  slug: reqres-app-user-update-request-structure
- name: Reqres App User Verify Request Structure
  property_count: 1
  slug: reqres-app-user-verify-request-structure
- name: Reqres App User Verify Response Structure
  property_count: 1
  slug: reqres-app-user-verify-response-structure
- name: Reqres Auth Request Structure
  property_count: 2
  slug: reqres-auth-request-structure
- name: Reqres Collection Create Request Structure
  property_count: 5
  slug: reqres-collection-create-request-structure
- name: Reqres Collection List Response Structure
  property_count: 1
  slug: reqres-collection-list-response-structure
- name: Reqres Collection Record Create Request Structure
  property_count: 1
  slug: reqres-collection-record-create-request-structure
- name: Reqres Collection Record List Response Structure
  property_count: 2
  slug: reqres-collection-record-list-response-structure
- name: Reqres Collection Record Response Structure
  property_count: 1
  slug: reqres-collection-record-response-structure
- name: Reqres Collection Record Structure
  property_count: 9
  slug: reqres-collection-record-structure
- name: Reqres Collection Record Update Request Structure
  property_count: 1
  slug: reqres-collection-record-update-request-structure
- name: Reqres Collection Response Structure
  property_count: 1
  slug: reqres-collection-response-structure
- name: Reqres Collection Structure
  property_count: 9
  slug: reqres-collection-structure
- name: Reqres Collection Update Request Structure
  property_count: 4
  slug: reqres-collection-update-request-structure
- name: Reqres Legacy Mutation Request Structure
  property_count: 0
  slug: reqres-legacy-mutation-request-structure
- name: Reqres Legacy Mutation Response Structure
  property_count: 3
  slug: reqres-legacy-mutation-response-structure
- name: Reqres Legacy Unknown List Response Structure
  property_count: 6
  slug: reqres-legacy-unknown-list-response-structure
- name: Reqres Legacy Unknown Response Structure
  property_count: 2
  slug: reqres-legacy-unknown-response-structure
- name: Reqres Legacy Unknown Structure
  property_count: 5
  slug: reqres-legacy-unknown-structure
- name: Reqres Legacy User List Response Structure
  property_count: 6
  slug: reqres-legacy-user-list-response-structure
- name: Reqres Legacy User Response Structure
  property_count: 2
  slug: reqres-legacy-user-response-structure
- name: Reqres Legacy User Structure
  property_count: 5
  slug: reqres-legacy-user-structure
- name: Reqres Login Response Structure
  property_count: 1
  slug: reqres-login-response-structure
- name: Reqres Register Response Structure
  property_count: 2
  slug: reqres-register-response-structure
- name: Reqres Template Structure
  property_count: 8
  slug: reqres-template-structure
- name: Reqres Templates Response Structure
  property_count: 2
  slug: reqres-templates-response-structure
jsonld:
- class_count: 40
  name: Reqres Context
  property_count: 75
  slug: reqres-context
layout: provider
modified: '2026-05-29'
name: ReqRes
nav: Providers
network: true
overview: 'ReqRes publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Agent Sandbox API, App Users API, Authentication API, and 3 more. Tagged areas include Development, Testing, Prototyping, Fake API, and REST.


  The ReqRes catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ReqRes'' developer surface includes authentication, getting-started guide, documentation, signup flow, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Reqres Plans Pricing
  plan_count: 7
  slug: reqres-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Reqres Rate Limits
  slug: reqres-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ReqRes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: reqres-jsonschema-spectral-rules
- effective_rule_count: 84
  extends:
  - spectral:oas
  name: ReqRes API Rules
  rule_count: 43
  severity_counts:
    error: 15
    hint: 0
    info: 10
    warn: 18
  slug: reqres-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 20.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 28.8
    contract_quality: 34.6
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reqres/refs/heads/main/screenshots/reqres-2026-06-20T192921.png
security:
- kind: authentication
  name: Reqres Authentication
  slug: reqres-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Reqres Domain Security
  slug: reqres-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reqres
solutions:
- description: From $499/year per team, deploy ReqRes inside your own infrastructure with no external dependencies — useful for regulated environments that can't call a public service.
  name: Self-Hosted Deployment
- description: On the Team plan, issue scoped API keys per engineer with usage tracking, so a single project can attribute spend back to individuals.
  name: Scoped Per-Engineer API Keys
- description: On the Pro plan, configure webhooks that fire on collection data changes, letting ReqRes drive downstream pipelines as a prototyping backend.
  name: Webhook Automations
tags:
- Development
- Testing
- Prototyping
- Fake API
- REST
- Agent Sandbox
use_cases:
- description: The default fake API cited in React, Vue, Angular, and Svelte tutorials when an author needs a real HTTP endpoint without standing up a backend.
  name: Frontend Tutorial Endpoints
- description: Coding bootcamps wire exercises against ReqRes legacy endpoints so students can practice CRUD flows on a stable, free, no-signup surface.
  name: Bootcamp Curriculum
- description: Use the legacy and Collections surfaces to exercise HTTP client libraries (fetch, axios, requests, OkHttp) against a real REST API.
  name: API Client Test Suites
- description: Build a UI against persistent ReqRes collections before standing up a real backend; swap in a real API later by renaming the base URL.
  name: Frontend-First Prototyping
- description: Test AI coding agents against the /agent/v1/* sandbox — cursor pagination, deliberate failures, deterministic seeded fixtures.
  name: AI Agent Testing
- description: Power live sales demos for tools that need to talk to an API without exposing customer data.
  name: Sales Demos
- description: Hands-on workshops where every participant needs a working API endpoint in under a minute.
  name: Workshop Sandboxes
website: https://reqres.in/
---
