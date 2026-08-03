---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Bob's Public API for HR data and workflows — employee data, time off, attendance, tasks, documents/eSign, goals, job catalog, hiring, learning, and workforce planning.
  name: Bob Public API
  slug: bob-public-api
artifact_total: 9
asyncapis:
- description: ''
  name: Hi Bob Webhooks
  slug: hi-bob-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.hibob.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.hibob.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.hibob.com/reference/getting-started-with-bob-api
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.hibob.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/hi-bob-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hi-bob-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hibob.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://community.hibob.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hibob.com/pricing-plans/
- group: start
  title: ''
  type: SignUp
  url: https://app.hibob.com
- group: start
  title: ''
  type: Login
  url: https://app.hibob.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hibob.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hibob.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://hibob.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hi-bob-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hi-bob-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.hibob.com/docs/transition-from-api-access-tokens
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hi-bob-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hi-bob-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hi-bob-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hi-bob-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hi-bob-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hi-bob-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hi-bob-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.hibob.com/privacy/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.hibob.com/privacy/security/
- group: auth
  title: ''
  type: Security
  url: https://www.hibob.com/privacy/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hi-bob-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hi-bob-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/hi-bob-packages.yml
- group: other
  title: ''
  type: Marketplace
  url: https://www.hibob.com/marketplace
created: '2026-07-17'
description: HiBob (bob) is an all-in-one HR platform that connects people management, payroll, benefits, and finance for modern, mid-sized and multinational companies. Bob's Public API gives developers programmatic access to core HR data and workflows — employee profiles and org data, time off and attendance, tasks, documents and eSign, goals, job catalog, hiring/ATS, learning, and workforce planning — over a versioned REST API at https://api.hibob.com/v1. Authentication is token-based via API "service users" (HTTP Basic with a service-user ID and token) with granular category and field permissions, plus OAuth 2.0 (authorization code + refresh) for approved Marketplace partners scoped to endpoint-level permissions. The API offers cursor-based pagination, rate limiting with X-RateLimit-* headers, HMAC-signed Webhooks v2 for event notifications, an official hosted Bob MCP Server for AI tools, and a published llms.txt index of the developer docs.
image: https://images.hibob.com/favicon/bob.svg
layout: provider
mcp_servers:
- description: ''
  name: hi-bob-mcp.yml
  slug: hi-bob-mcpyml
modified: '2026-07-19'
name: Hi Bob
nav: Providers
network: true
overview: 'Hi Bob publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HR, HRIS, Human Resources, and Payroll.


  The Hi Bob catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hi Bob''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 24 more developer resources.'
random_paper: 86
rate_limits:
- limit_count: 1
  name: Hi Bob Rate Limits
  slug: hi-bob-rate-limits
scopes:
- name: Hi Bob Scopes
  scope_count: 27
  slug: hi-bob-scopes
  summary_line: 27 scopes
score:
  band: strong
  composite: 57.6
  delta: 2.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 78.9
  previous_composite: 54.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hi-bob/refs/heads/main/screenshots/hi-bob-2026-07-25T221129.png
security:
- kind: authentication
  name: Hi Bob Authentication
  slug: hi-bob-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Hi Bob Domain Security
  slug: hi-bob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hi Bob Vulnerability Disclosure
  slug: hi-bob-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Hi Bob Trust Center
  slug: hi-bob-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2022, ISO 27018:2019
slug: hi-bob
tags:
- Company
- HR
- HRIS
- Human Resources
- Payroll
- People Analytics
- Time Off
- Workforce Planning
- Employees
- HR Tech
website: https://apidocs.hibob.com/
---
