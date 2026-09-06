---
access_model:
  confidence: high
  label: Self-serve signup, free tier metered on messages sent
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - plans/line-plans-pricing.yml
  - authentication/line-authentication.yml
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 59
  human_in_the_loop: 4
  name: Line Agentic Access
  operation_count: 111
  slug: line-agentic-access
  summary_line: 111 operations · 59 acting · 4 human-in-the-loop
api_count: 9
apis:
- description: End-user authentication and authorization over OAuth 2.0 authorization code grant and OpenID Connect. Authorization runs at access.line.me; token, userinfo, revocation and JWKS endpoints are on api.li
  name: LINE Login v2.1
  slug: line-login-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The channel-access-token API from LINE — 8 operation(s) for channel-access-token.
  name: LINE Channel Access Token API
  slug: line-channel-access-token-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The dummy API from LINE — 1 operation(s) for dummy.
  name: LINE Dummy API
  slug: line-dummy-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The insight API from LINE — 7 operation(s) for insight.
  name: LINE Insight API
  slug: line-insight-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The liff API from LINE — 2 operation(s) for liff.
  name: LINE Liff API
  slug: line-liff-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The line-module API from LINE — 4 operation(s) for line-module.
  name: LINE Line Module API
  slug: line-line-module-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The line-module-attach API from LINE — 1 operation(s) for line-module-attach.
  name: LINE Line Module Attach API
  slug: line-line-module-attach-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The manage-audience API from LINE — 8 operation(s) for manage-audience.
  name: LINE Manage Audience API
  slug: line-manage-audience-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The manage-audience-blob API from LINE — 1 operation(s) for manage-audience-blob.
  name: LINE Manage Audience Blob API
  slug: line-manage-audience-blob-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The messaging-api API from LINE — 61 operation(s) for messaging-api.
  name: LINE Messaging API
  slug: line-messaging-api-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The messaging-api-blob API from LINE — 4 operation(s) for messaging-api-blob.
  name: LINE Messaging API Blob API
  slug: line-messaging-api-blob-api
- baseURL: https://api.line.me
  baseurl_source: declared
  description: The shop API from LINE — 1 operation(s) for shop.
  name: LINE Shop API
  slug: line-shop-api
artifact_total: 29
asyncapis:
- description: 'AsyncAPI description of the webhook event surface published by the LINE Messaging API to bot servers. The Messaging API delivers webhook events as HTTPS POST requests to the configured webhook URL of '
  name: LINE Messaging Webhook Event Surface
  slug: line-messaging-webhook
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LINE Messaging Channel API
  slug: open-line-channel-api
- collection_type: open
  name: LINE Messaging Channel Info API
  slug: open-line-info-api
- collection_type: open
  name: LINE Messaging Channel Message API
  slug: open-line-message-api
- collection_type: open
  name: LINE Messaging Channel Profile API
  slug: open-line-profile-api
- collection_type: open
  name: LINE Messaging API
  slug: open-line
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/line-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-messaging-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-webhook-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-channel-access-token-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-insight-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-manage-audience-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-liff-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-module-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-module-attach-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/line-shop-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/line-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/line-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/line-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/line-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/line-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/line-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/line-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/line-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/line-cli.yml
- group: design
  title: ''
  type: Components
  url: components/line-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/line-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/line-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/line-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/line-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/line-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/line-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/line-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.line-status.info/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/line-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/line-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/line-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/line-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/line-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/line-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/line/line-bot-mcp-server
- group: agent
  title: ''
  type: MCPServer
  url: mcp/line-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/line-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/line-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.line.biz/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linecorp
- group: company
  title: ''
  type: Website
  url: https://line.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.line.biz/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.line.biz/en/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.line.biz/en/reference/messaging-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.line.biz/en/docs/messaging-api/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://developers.line.biz/en/faq/
- group: company
  title: ''
  type: Blog
  url: https://techblog.lycorp.co.jp/en/
- group: docs
  title: ''
  type: OpenAPI Repository
  url: https://github.com/line/line-openapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/line
- group: start
  title: ''
  type: SignUp
  url: https://developers.line.biz/console/
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.line.biz/en/docs/messaging-api/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.line.biz/en/terms-and-policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lycorp.co.jp/en/company/privacypolicy/
created: '2026-05-11'
description: LINE is a Japan-based messaging platform operated by LY Corporation, with over 200 million monthly active users across Japan, Taiwan, Thailand and Indonesia, offering messaging, payments, news and a broad ecosystem of services. The LINE Developers platform exposes public APIs for building chatbots and Official Accounts (Messaging API), issuing and rotating credentials (Channel Access Token API), reading delivery and audience analytics (Insight API), building marketing audiences (Manage Audience API), running web apps inside the LINE client (LIFF), and social login via LINE Login v2.1 over OAuth 2.0 and OpenID Connect. LINE publishes nine first-party OpenAPI documents covering 111 operations at github.com/line/line-openapi and generates all six official server SDKs from them. Server API calls authenticate with a channel access token presented as an HTTP Bearer credential and scoped to a single LINE channel.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/line.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: First-party Model Context Protocol server published by LY Corporation that wraps the LINE Messaging API so an AI agent can drive a LINE Official Account — pushing and broadcasting text and Flex messag
  name: MCP Server manifest
  slug: mcp-server-manifest
modified: '2026-08-13'
name: LINE
nav: Providers
network: true
overview: 'LINE publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Channel Access Token API, Dummy API, Insight API, and 8 more. Tagged areas include Messaging, Chatbots, Social Login, Mini Apps, and Marketing.


  The LINE catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  LINE''s developer surface includes authentication, CLI, sandbox, changelog, documentation, API reference, getting-started guide, and 47 more developer resources.'
plans:
- name: Line Plans Pricing
  plan_count: 3
  slug: line-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 10
  name: Line Rate Limits
  slug: line-rate-limits
rules:
- effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: LINE API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: line-asyncapi-spectral-rules
scopes:
- name: Line Scopes
  scope_count: 0
  slug: line-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 69.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 58.0
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 31.8
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/line/refs/heads/main/screenshots/line-2026-06-20T184539.png
security:
- kind: authentication
  name: Line Authentication
  slug: line-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Line Domain Security
  slug: line-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Line Vulnerability Disclosure
  slug: line-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: line
tags:
- Messaging
- Chatbots
- Social Login
- Mini Apps
- Marketing
- Webhook
- OpenID Connect
- Audience
- Analytics
- Japan
website: https://line.me
---
