---
access_model:
  confidence: medium
  label: Sales-assisted
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://sessionai.com/request-a-demo
  - https://devguide.zineone.com/docs/integration-onboarding-process
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Public REST API for the Session AI (ZineOne) platform. Documented operations cover sending events into the platform from any channel, retrieving hosted content, calling customer-authored microservices
  name: Session AI Platform REST API
  slug: session-ai-platform-rest-api
- description: 'Remote Model Context Protocol server operated by Session AI at https://sessionai.com/mcp. The endpoint answers with an RFC 9728 OAuth challenge (WWW-Authenticate: Bearer realm="mcp") and publishes pro'
  name: Session AI MCP Server
  slug: session-ai-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Sessionai Webhooks
  slug: sessionai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sessionai.com
- group: company
  title: ''
  type: Blog
  url: https://sessionai.com/blog
- group: operate
  title: ''
  type: Support
  url: https://sessionai.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sessionai.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sessionai.com/terms
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devguide.zineone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zineone.com/
- group: docs
  title: ''
  type: APIReference
  url: https://devguide.zineone.com/docs/rest-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://devguide.zineone.com/docs/introduction-to-html5
- group: start
  title: ''
  type: Login
  url: https://cloud.zineone.com/c3
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sessionai.com/
- group: auth
  title: ''
  type: Compliance
  url: https://sessionai.com/capabilities/privacy-and-fairness
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sessionai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sessionai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sessionai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sessionai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sessionai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sessionai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sessionai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sessionai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sessionai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/sessionai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sessionai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/sessionai-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sessionai-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sessionai-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sessionai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sessionai-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sessionai-domain-security.yml
created: '2026-07-17'
description: Session AI (formerly ZineOne) is an ecommerce AI platform that uses agentic decisioning to optimize promotions and customer experiences in real time. Its Session Marketing Agent predicts in-session visitor intent and behavior, then delivers personalized offers, nudges, and messages to maximize revenue, conversions, and profit margins for retail, travel and hospitality, and telecom brands. The platform integrates via tag managers (Google Tag Manager, Tealium), a CDN-delivered HTML5/JavaScript SDK, Android and iOS SDKs, server-to-server REST calls, and prebuilt plugins/cartridges, advertising sub-50ms decision latency, no PII in scope, and SOC 2 aligned controls. Session AI publishes a public developer guide and REST API reference under its legacy ZineOne domain covering nine documented operations — send events, retrieve content, call microservices, stream and cube queries, CCPA profile opt-in/opt-out, and profile and activity retrieval — authenticated with an apikey header. It
  also operates an OAuth-protected remote MCP server at https://sessionai.com/mcp for agent access.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sessionai.png
layout: provider
mcp_servers:
- description: ''
  name: Session AI
  slug: session-ai
modified: '2026-08-13'
name: Session AI
nav: Providers
network: true
overview: 'Session AI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, E-Commerce, Retail, and Personalization.


  The Session AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Session AI''s developer surface includes engineering blog, support, documentation, API reference, getting-started guide, authentication, sandbox, and 22 more developer resources.'
plans:
- name: Sessionai Plans Pricing
  plan_count: 0
  slug: sessionai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Sessionai Rate Limits
  slug: sessionai-rate-limits
scopes:
- name: Sessionai Scopes
  scope_count: 5
  slug: sessionai-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 40.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sessionai/refs/heads/main/screenshots/sessionai-2026-08-17T081818.png
security:
- kind: authentication
  name: Sessionai Authentication
  slug: sessionai-authentication
  summary_line: apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Sessionai Domain Security
  slug: sessionai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sessionai
tags:
- Company
- Artificial Intelligence
- E-Commerce
- Retail
- Personalization
- Marketing
- Agentic AI
- Decisioning
- Customer Data
- Event
- Real-Time
- MCP
website: https://sessionai.com
---
