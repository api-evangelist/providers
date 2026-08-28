---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 64.4
  scored_at: '2026-08-26'
api_count: 12
apis:
- description: The Live API from Sylvia API — 1 operation(s) for live.
  name: Sylvia API Live API
  slug: sylvia-api-live-api
- description: The Subreddits API from Sylvia API — 2 operation(s) for subreddits.
  name: Sylvia API Subreddits API
  slug: sylvia-api-subreddits-api
- description: The Users API from Sylvia API — 3 operation(s) for users.
  name: Sylvia API Users API
  slug: sylvia-api-users-api
- description: The Account API from Sylvia API — 5 operation(s) for account.
  name: Sylvia API Account API
  slug: sylvia-api-account-api
- description: The Billing API from Sylvia API — 2 operation(s) for billing.
  name: Sylvia API Billing API
  slug: sylvia-api-billing-api
- description: The Discovery API from Sylvia API — 3 operation(s) for discovery.
  name: Sylvia API Discovery API
  slug: sylvia-api-discovery-api
- description: The Domains API from Sylvia API — 2 operation(s) for domains.
  name: Sylvia API Domains API
  slug: sylvia-api-domains-api
- description: The Health API from Sylvia API — 1 operation(s) for health.
  name: Sylvia API Health API
  slug: sylvia-api-health-api
- description: The Keys API from Sylvia API — 2 operation(s) for keys.
  name: Sylvia API Keys API
  slug: sylvia-api-keys-api
- description: The Posts & Comments API from Sylvia API — 6 operation(s) for posts & comments.
  name: Sylvia API Posts & Comments API
  slug: sylvia-api-posts-comments-api
- description: The Search API from Sylvia API — 1 operation(s) for search.
  name: Sylvia API Search API
  slug: sylvia-api-search-api
- description: The Templates API from Sylvia API — 2 operation(s) for templates.
  name: Sylvia API Templates API
  slug: sylvia-api-templates-api
artifact_total: 18
collections:
- collection_type: postman
  name: Sylvia API
  slug: postman-sylvia-api
common:
- group: company
  title: ''
  type: Website
  url: https://sylvia-api.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://sylvia-api.com/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/sylvia-api-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sylvia-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sylvia-api.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://sylvia-api.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://sylvia-api.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/sylvia-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sylvia-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sylvia-api-finops.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://sylvia-api.instatus.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sylvia-api-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://sylvia-api.com/changelog/
- group: auth
  title: ''
  type: Security
  url: https://sylvia-api.com/security/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sylvia-api-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://sylvia-api.com/.well-known/security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sylvia-api.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://sylvia-api.com/blog/
- group: build
  title: ''
  type: SDK
  url: https://sylvia-api.com/sdk/
- group: build
  title: ''
  type: Packages
  url: https://pypi.org/project/sylvia-api/
- group: agent
  title: ''
  type: MCPServer
  url: https://api.sylvia-api.com/mcp
- group: other
  title: ''
  type: AgentCard
  url: a2a/sylvia-api-agent-card.json
- group: other
  title: ''
  type: APICatalog
  url: well-known/sylvia-api-api-catalog.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sylvia-api-well-known.yml
- group: other
  title: ''
  type: APIsJSON
  url: https://sylvia-api.com/apis.json
- group: docs
  title: ''
  type: OpenAPI
  url: https://sylvia-api.com/openapi.json
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sylvia-api-agentic-access-contract.json
- group: build
  title: ''
  type: Postman
  url: postman/sylvia-api.postman_collection.json
- group: design
  title: ''
  type: Conformance
  url: conformance/sylvia-api-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sylvia-api-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sylvia-api-overlay.json
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sylvia-api-deprecation.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sylvia-api-error-codes.yml
created: '2026-08-04'
description: 'Sylvia API is a third-party Reddit data API that serves Reddit content as JSON — posts, comments with full recursive threads, subreddit and user surfaces, global search, and a live comment stream. Thirty-six operations across twelve tags cover the read surface (posts, comments, subreddits, users, search, domains, discovery and live feeds) plus account self-service: API key issue and revoke, response-format templates, usage history and crypto billing. Authentication is an API key for data endpoints and a separate account token for account operations. It occupies the gap left by Pushshift, giving researchers and developers queryable Reddit history without going through OAuth on the first-party API.'
finops:
- name: Sylvia Api Finops
  service_category: ''
  slug: sylvia-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sylvia-api.png
layout: provider
mcp_servers:
- description: ''
  name: Sylvia API MCP Server
  slug: sylvia-api-mcp-server
modified: '2026-08-20'
name: Sylvia API
nav: Providers
network: true
overview: 'Sylvia API publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Live API, Subreddits API, Users API, and 9 more. Tagged areas include Reddit, Social, Data, Search, and Comments.


  Sylvia API''s developer surface includes authentication, documentation, API reference, pricing, changelog, engineering blog, SDKs, and 27 more developer resources.'
plans:
- name: Sylvia Api Plans Pricing
  plan_count: 4
  slug: sylvia-api-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Sylvia Api Rate Limits
  slug: sylvia-api-rate-limits
score:
  band: strong
  composite: 57.5
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 30.3
    contract_quality: 58.4
    developer_ergonomics: 59.5
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 34.2
  previous_composite: 57.5
  provenance:
    conformance: unknown
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Sylvia Api Authentication
  slug: sylvia-api-authentication
  summary_line: 1 scheme
slug: sylvia-api
tags:
- Reddit
- Social
- Data
- Search
- Comments
- Research
- Content
- Datasets
website: https://sylvia-api.com/
---
