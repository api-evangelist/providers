---
access_model:
  confidence: medium
  label: Sales-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.nectarsocial.com/book-a-demo
  - https://beta-api.nectarsocial.com/.well-known/oauth-authorization-server
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 44.8
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: 'Remote Model Context Protocol server exposing Nectar Social''s social content and analytics to AI agents over JSON-RPC 2.0 (Streamable HTTP). OAuth-protected: an anonymous tools/list returns HTTP 401 w'
  name: Nectar Social MCP Server
  slug: nectar-social-mcp-server
- description: The OAuth 2.0 authorization server and platform REST API named by the MCP server's protected-resource metadata. Publishes 18 scopes covering content, analytics, community, inbox, campaigns, competitor
  name: Nectar Social Platform API (Beta)
  slug: nectar-social-platform-api-beta
artifact_total: 11
asyncapis:
- description: ''
  name: Nectar Social Webhooks
  slug: nectar-social-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nectar-social-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nectar-social-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nectar-social-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nectar-social-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nectar-social-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nectar-social-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nectar-social-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nectar-social-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/nectar-social-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nectar-social-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nectar-social-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nectar-social-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nectar-social-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.nectarsocial.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nectar-social-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nectar-social-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nectar-social-well-known.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nectarsocial.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.nectarsocial.com/company/news
- group: company
  title: ''
  type: Website
  url: https://www.nectarsocial.com
created: '2026-07-17'
description: 'Nectar Social is an AI "social operating system" for consumer brands — an AI-powered social teammate that manages online communities, performs real-time social listening and sentiment analysis, tracks influencers, and turns organic social engagement and DM conversations into measurable revenue across community, brand safety, commerce, influencer, social-selling, and analytics use cases. Founded in 2023 by Misbah and Farah Uraizee and based in Bellevue, Washington, the company raised $30M from Menlo Ventures, GV (Google Ventures), and True Ventures. Nectar Social operates a remote Model Context Protocol server at mcp.nectarsocial.com/mcp, protected by a full OAuth 2.1 stack — RFC 9728 protected-resource metadata, an RFC 8414 authorization server at beta-api.nectarsocial.com publishing 18 fine-grained scopes, PKCE S256, dynamic client registration and token revocation. It is an agent-first surface: the MCP server is the only documented way in, and the company publishes no OpenAPI,
  no SDK and no public developer documentation, with docs.nectarsocial.com redirecting into a login-gated single-page application.'
image: https://cdn.prod.website-files.com/6831e07f7427f0c59b8b2a7b/6837117d77fca09e24ab5ba0_Frame%201912056558.png
layout: provider
mcp_servers:
- description: ''
  name: Nectar Social MCP Server
  slug: nectar-social-mcp-server
- description: ''
  name: Nectar Social MCP Server
  slug: nectar-social-mcp-server-2
modified: '2026-08-13'
name: Nectar Social
nav: Providers
network: true
overview: 'Nectar Social publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Social-Media, Community Management, and Social Listening.


  The Nectar Social catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nectar Social''s developer surface includes authentication, engineering blog, and 18 more developer resources.'
plans:
- name: Nectar Social Plans Pricing
  plan_count: 0
  slug: nectar-social-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Nectar Social Rate Limits
  slug: nectar-social-rate-limits
scopes:
- name: Nectar Social Scopes
  scope_count: 18
  slug: nectar-social-scopes
  summary_line: 18 scopes · authorizationCode
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 26.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Nectar Social Authentication
  slug: nectar-social-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nectar Social Domain Security
  slug: nectar-social-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nectar Social Vulnerability Disclosure
  slug: nectar-social-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nectar-social
tags:
- Company
- Artificial Intelligence
- Social-Media
- Community Management
- Social Listening
- Influencer Marketing
- Customer Engagement
- Social Commerce
- MCP
- Agents
- Authentication
website: https://www.nectarsocial.com
---
