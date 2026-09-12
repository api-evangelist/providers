---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Express Gateway Agentic Access
  operation_count: 25
  slug: express-gateway-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 1
apis:
- description: Express Gateway is an API gateway built on Express.js for managing and securing microservices and APIs.
  name: Express Gateway
  slug: express-gateway
- baseURL: http://localhost:9876
  baseurl_source: spec
  description: The Apps API from Express Gateway — 3 operation(s) for apps.
  name: Express Gateway Apps API
  slug: express-gateway-apps-api
- baseURL: http://localhost:9876
  baseurl_source: spec
  description: The Credentials API from Express Gateway — 6 operation(s) for credentials.
  name: Express Gateway Credentials API
  slug: express-gateway-credentials-api
- baseURL: http://localhost:9876
  baseurl_source: spec
  description: The Scopes API from Express Gateway — 2 operation(s) for scopes.
  name: Express Gateway Scopes API
  slug: express-gateway-scopes-api
- baseURL: http://localhost:9876
  baseurl_source: spec
  description: The Users API from Express Gateway — 3 operation(s) for users.
  name: Express Gateway Users API
  slug: express-gateway-users-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Express Gateway Admin Apps API
  slug: open-express-gateway-apps-api
- collection_type: open
  name: Express Gateway Admin Apps Credentials API
  slug: open-express-gateway-credentials-api
- collection_type: open
  name: Express Gateway Admin Apps Scopes API
  slug: open-express-gateway-scopes-api
- collection_type: open
  name: Express Gateway Admin Apps Users API
  slug: open-express-gateway-users-api
- collection_type: open
  name: Express Gateway Admin API
  slug: open-express-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/express-gateway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/express-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/express-gateway-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.express-gateway.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.express-gateway.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ExpressGateway
- group: docs
  title: ''
  type: APIReference
  url: https://www.express-gateway.io/docs/admin/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.express-gateway.io/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://github.com/ExpressGateway/express-gateway/issues
- group: company
  title: ''
  type: Blog
  url: https://www.express-gateway.io/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.express-gateway.io/docs/roadmap/
- group: build
  title: ''
  type: Packages
  url: packages/express-gateway-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/express-gateway-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/express-gateway-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/express-gateway-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/express-gateway-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/express-gateway-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/express-gateway-problem-types.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/express-gateway-scopes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/express-gateway-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/express-gateway-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/express-gateway-admin-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/express-gateway-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/express-gateway-rate-limits.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/express-gateway-mcp.yml
created: '2026-03-27'
description: 'Express Gateway is an open-source (Apache-2.0) microservices and serverless API gateway built on Express.js and Node.js. Operators install it themselves and compose policies — key auth, OAuth 2.0, JWT, CORS, rate limiting, request and response transforms, proxying — into pipelines declared in a single YAML config, fronting their own downstream services. Its own HTTP surface is the Admin API, which manages users, applications, credentials, scopes, schemas, policies, endpoints and pipelines, and which binds by default to localhost:9876 rather than to any host the project runs. The project is dormant: the last release reached npm in April 2021.'
finops:
- name: Express Gateway Finops
  service_category: API
  slug: express-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/express-gateway.png
layout: provider
modified: '2026-09-07'
name: Express Gateway
nav: Providers
network: true
overview: 'Express Gateway publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Credentials API, Scopes API, and 1 more. Tagged areas include API Composition, API Gateway, BFF, Open Source, and Microservices.


  Express Gateway''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, CLI, and 19 more developer resources.'
plans:
- name: Express Gateway Plans Pricing
  plan_count: 0
  slug: express-gateway-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Express Gateway Rate Limits
  slug: express-gateway-rate-limits
scopes:
- name: Express Gateway Scopes
  scope_count: 0
  slug: express-gateway-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 48.3
    developer_ergonomics: 56.5
    discoverability: 59.3
    operational_transparency: 23.7
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/express-gateway/refs/heads/main/screenshots/express-gateway-2026-06-20T180941.png
security:
- kind: authentication
  name: Express Gateway Authentication
  slug: express-gateway-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Express Gateway Domain Security
  slug: express-gateway-domain-security
  summary_line: TLSv1.3 · HSTS
slug: express-gateway
tags:
- API Composition
- API Gateway
- BFF
- Open Source
- Microservices
- Authentication
- Node.js
- Reverse Proxy
website: https://www.express-gateway.io/
---
