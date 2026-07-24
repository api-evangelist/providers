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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 78.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 74
  human_in_the_loop: 2
  name: Hooklogic Criteo Agentic Access
  operation_count: 114
  slug: hooklogic-criteo-agentic-access
  summary_line: 114 operations · 74 acting · 2 human-in-the-loop
api_count: 8
apis:
- description: The Accounts API from HookLogic (Criteo) — 12 operation(s) for accounts.
  name: HookLogic (Criteo) Accounts API
  slug: hooklogic-criteo-accounts-api
- description: The Analytics API from HookLogic (Criteo) — 12 operation(s) for analytics.
  name: HookLogic (Criteo) Analytics API
  slug: hooklogic-criteo-analytics-api
- description: The Audience API from HookLogic (Criteo) — 8 operation(s) for audience.
  name: HookLogic (Criteo) Audience API
  slug: hooklogic-criteo-audience-api
- description: The Balance API from HookLogic (Criteo) — 6 operation(s) for balance.
  name: HookLogic (Criteo) Balance API
  slug: hooklogic-criteo-balance-api
- description: The Billing API from HookLogic (Criteo) — 3 operation(s) for billing.
  name: HookLogic (Criteo) Billing API
  slug: hooklogic-criteo-billing-api
- description: The Campaign API from HookLogic (Criteo) — 54 operation(s) for campaign.
  name: HookLogic (Criteo) Campaign API
  slug: hooklogic-criteo-campaign-api
- description: The Catalog API from HookLogic (Criteo) — 2 operation(s) for catalog.
  name: HookLogic (Criteo) Catalog API
  slug: hooklogic-criteo-catalog-api
- description: The Gateway API from HookLogic (Criteo) — 1 operation(s) for gateway.
  name: HookLogic (Criteo) Gateway API
  slug: hooklogic-criteo-gateway-api
artifact_total: 14
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.criteo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.criteo.com/retail-media/docs/welcome-to-criteo
- group: docs
  title: ''
  type: APIReference
  url: https://developers.criteo.com/criteo-apis/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.criteo.com/criteo-apis/docs/connect-to-the-api
- group: operate
  title: ''
  type: Support
  url: https://developers.criteo.com/criteo-apis/docs/escalation-guidelines
- group: company
  title: ''
  type: Blog
  url: https://www.criteo.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/criteo
- group: start
  title: ''
  type: SignUp
  url: https://developers.criteo.com/criteo-apis/docs/create-your-partner-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.criteo.com/criteo-apis/docs/criteo-api-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.criteo.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/realcriteo/workspace/criteo/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/hooklogic-criteo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hooklogic-criteo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hooklogic-criteo-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hooklogic-criteo-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hooklogic-criteo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.criteo.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.criteo.com/criteo-apis/docs/versioning-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hooklogic-criteo-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/hooklogic-criteo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hooklogic-criteo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hooklogic-criteo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hooklogic-criteo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hooklogic-criteo-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hooklogic-criteo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hooklogic-criteo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hooklogic-criteo-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hooklogic-criteo-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hooklogic-criteo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://api.criteo.com/.well-known/security.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hooklogic-criteo-agentic-access.yml
created: '2026-07-17'
description: HookLogic was a retail-media advertising exchange and ad server that let brands buy sponsored-product placements in retailer search results (Walmart, Target, Best Buy). Criteo acquired HookLogic for ~$250M in 2016, and the product line is now delivered as the Criteo Retail Media API — a REST API for retailers, brands, and agencies to programmatically create, launch, monitor, and report on retail-media campaigns. It uses OAuth 2.0 (client-credentials and authorization-code flows), RFC 7807 error bodies, date-based API versioning, and ships officially supported Python, PHP, and Java SDKs.
image: https://avatars.githubusercontent.com/u/1713646?v=4
layout: provider
mcp_servers:
- description: ''
  name: hooklogic-criteo-mcp.yml
  slug: hooklogic-criteo-mcpyml
modified: '2026-07-19'
name: HookLogic (Criteo)
nav: Providers
network: true
overview: 'HookLogic (Criteo) publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, Audience API, and 5 more. Tagged areas include Company, Commerce, Retail Media, Advertising, and E-commerce.


  HookLogic (Criteo)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 0
  name: Hooklogic Criteo Rate Limits
  slug: hooklogic-criteo-rate-limits
score:
  band: developing
  composite: 52.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 49.4
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 52.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Hooklogic Criteo Authentication
  slug: hooklogic-criteo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hooklogic Criteo Domain Security
  slug: hooklogic-criteo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hooklogic Criteo Vulnerability Disclosure
  slug: hooklogic-criteo-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hooklogic-criteo
tags:
- Company
- Commerce
- Retail Media
- Advertising
- E-commerce
- Marketing
- Retail
- APIs
website: https://developers.criteo.com
---
