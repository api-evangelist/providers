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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Syncly Agentic Access
  operation_count: 4
  slug: syncly-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://mcp.syncly.app
  baseurl_source: declared
  description: The Health API from Syncly — 1 operation(s) for health.
  name: Syncly Health API
  slug: syncly-health-api
- baseURL: https://mcp.syncly.app
  baseurl_source: declared
  description: The .well Known API from Syncly — 3 operation(s) for .well known.
  name: Syncly .well Known API
  slug: syncly-well-known-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/syncly-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://syncly.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://syncly-a76215af.mintlify.app/en
- group: docs
  title: ''
  type: Documentation
  url: https://syncly-a76215af.mintlify.app/en
- group: start
  title: ''
  type: GettingStarted
  url: https://syncly-a76215af.mintlify.app/en/quick-start/getting-started
- group: company
  title: ''
  type: Blog
  url: https://syncly.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://syncly.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://creator.syncly.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://syncly.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syncly.app/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/syncly-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syncly-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/syncly-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/syncly-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://syncly.app/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syncly-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/syncly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://syncly.app/security
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/syncly-social-mcp-openapi.json
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/syncly-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/syncly-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/syncly-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/syncly-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/syncly-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/syncly-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/syncly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/syncly-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/syncly-social-mcp-overlay.yaml
created: '2026-07-17'
description: Syncly is an AI-native social and customer intelligence platform (backed by Y Combinator, SoftBank, 500 Global, and Rebel) that unifies customer feedback and social conversations into a single source of truth. It aggregates feedback from tickets, chat, email, surveys, reviews, and social, then uses AI to auto-tag, cluster, and sentiment-score every message into the themes that matter. Its social intelligence surface listens across TikTok, Reels, and Shorts with speech-to-text and vision AI for competitive analysis, creator discovery, and campaign measurement, while "Hey Syncly" lets teams query their data in plain language. Syncly exposes its data to AI assistants through a hosted remote MCP connector (Claude, ChatGPT, Cursor, and more) rather than a public REST API.
image: https://framerusercontent.com/images/eVsReqyksUv6paQaME2J7epX8.png
layout: provider
mcp_servers:
- description: ''
  name: Syncly Social MCP Server
  slug: syncly-social-mcp-server
modified: '2026-08-13'
name: Syncly
nav: Providers
network: true
overview: 'Syncly publishes 2 APIs on the [APIs.io](https://apis.io/) network: Health API and .well Known API. Tagged areas include Company, Social Intelligence, Social Listening, Customer Feedback, and Voice of Customer.


  Syncly''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Syncly Plans Pricing
  plan_count: 3
  slug: syncly-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Syncly Rate Limits
  slug: syncly-rate-limits
scopes:
- name: Syncly Scopes
  scope_count: 2
  slug: syncly-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 37.4
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syncly/refs/heads/main/screenshots/syncly-2026-08-17T082226.png
security:
- kind: authentication
  name: Syncly Authentication
  slug: syncly-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Syncly Domain Security
  slug: syncly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Syncly Vulnerability Disclosure
  slug: syncly-vulnerability-disclosure
  summary_line: contact published
slug: syncly
tags:
- Company
- Social Intelligence
- Social Listening
- Customer Feedback
- Voice of Customer
- Creator Marketing
- Analytics
- Artificial Intelligence
- MCP
website: https://syncly.app
---
