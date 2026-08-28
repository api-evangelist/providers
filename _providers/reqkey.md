---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API for API key management, usage credits/metering, rate limiting, and traffic analytics. POST/JSON endpoints authenticated with a project root key via Bearer token; single unauthenticated GET /h
  name: ReqKey REST API
  slug: reqkey-rest-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reqkey-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reqkey-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/reqkey-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reqkey-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reqkey-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reqkey-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reqkey-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reqkey-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reqkey-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reqkey-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/reqkey-plans.yml
- group: build
  title: ''
  type: Packages
  url: packages/reqkey-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reqkey-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reqkey-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://www.reqkey.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.reqkey.com/docs/api/keys
- group: start
  title: ''
  type: GettingStarted
  url: https://www.reqkey.com/docs/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://www.reqkey.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.reqkey.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Req-Key
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reqkey.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.reqkey.com/sign-in?mode=signup
- group: start
  title: ''
  type: Login
  url: https://www.reqkey.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reqkey.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reqkey.com/legal/privacy
- group: company
  title: ''
  type: Website
  url: https://www.reqkey.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reqkey
created: '2026-07-26'
description: 'ReqKey is out-of-band API key authentication, usage credits, rate limiting and request analytics as a service for teams that sell or expose an API. It never sits in front of customer traffic: your own middleware makes one call to POST /key/validate per request, which checks the key, deducts a credit from that customer''s pool and records the decision, typically in under 5ms over a reused connection. The defining design choice is that credits and rate limits live on the CONSUMER rather than the key, so issuing a customer fifty keys never multiplies their plan into fifty quotas and disabling a consumer stops all of its keys at once. Validation is Redis-backed and runs in multiple AWS regions with a global sync layer reconciling credit balances. A second endpoint, POST /ingest, correlates full request/response logs to a validation by requestId and feeds an Analytics API over two datasets. Seven first-party SDKs wrap both calls as framework middleware.'
image: https://www.reqkey.com/og-image.png
layout: provider
mcp_servers:
- description: A CANDIDATE tool surface — what an official ReqKey MCP server would expose if ReqKey shipped one. This is an API Evangelist proposal grounded in real, documented endpoints, NOT a server that exists. B
  name: ReqKey MCP Server
  slug: reqkey-mcp-server
modified: '2026-08-09'
name: ReqKey
nav: Providers
network: true
overview: 'ReqKey publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include APIKeys, Authentication, Authorization, Rate Limiting, and Usage Metering.


  ReqKey''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Reqkey Plans
  plan_count: 3
  slug: reqkey-plans
random_paper: 6
rate_limits:
- limit_count: 6
  name: Reqkey Rate Limits
  slug: reqkey-rate-limits
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 38.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Reqkey Authentication
  slug: reqkey-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Reqkey Domain Security
  slug: reqkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Reqkey Vulnerability Disclosure
  slug: reqkey-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: reqkey
tags:
- APIKeys
- Authentication
- Authorization
- Rate Limiting
- Usage Metering
- API Analytics
- API Management
- Developer Tools
- Middleware
- Observability
website: https://www.reqkey.com
---
