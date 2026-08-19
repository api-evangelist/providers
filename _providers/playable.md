---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Public REST API for the Playable gamification platform. Covers campaign types, campaign lifecycle (list, view, update, copy, delete, activate, pause, resume, clear cache), campaign sections and regist
  name: Playable API
  slug: playable-api
- description: 'Hosted Model Context Protocol endpoint served from the Playable web property and advertised through RFC 9728 protected-resource metadata at playable.com/.well-known/oauth-protected-resource. Requires '
  name: Playable MCP Server
  slug: playable-mcp-server
- description: Browser-side JavaScript SDK (`@playable-marketing/campaign-sdk`) that exposes a promise-based `window.sdk` object plus an event stream so a host page can listen to campaign events and read campaign co
  name: Playable Campaign SDK
  slug: playable-campaign-sdk
artifact_total: 13
asyncapis:
- description: ''
  name: Playable Webhooks
  slug: playable-webhooks
collections:
- collection_type: open
  name: Swagger with Laravel
  slug: open-playable-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/playable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://playable.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.playable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.playable.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://api.playable.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.playable.com/en/articles/10384051-developer
- group: operate
  title: ''
  type: Support
  url: https://playable.com/help-center/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.playable.com/en/
- group: company
  title: ''
  type: Blog
  url: https://playable.com/learn/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://playable.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://playable.com/demo/
- group: start
  title: ''
  type: Login
  url: https://app.playable.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://playable.com/terms-and-conditions-v2/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://playable.com/privacy-policy-for-playable-aps/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.playable.com/
- group: auth
  title: ''
  type: Compliance
  url: https://playable.com/iso-gdpr-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/playable-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/playable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/playable-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/playable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/playable-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/playable-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/playable-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/playable-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/playable-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/playable-integration-status-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/playable-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/playable-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/playable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/playable-packages.yml
- group: design
  title: ''
  type: Components
  url: components/playable-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/playable-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/playable-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/playable-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/playable-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/playable-api-overlay.yaml
created: '2026-08-12'
description: Playable (formerly Leadfamly, Playable ApS, Aarhus Denmark and London UK) is a self-service marketing gamification platform used by brands to build, publish and measure interactive campaigns — spin-the-wheel, advent calendars, quizzes, scratch cards, memory and skill games — across web, email, in-app, in-store and retail-media placements. The platform pairs a campaign builder with zero-party data collection, prize and voucher management, ESP/CRM/storage integrations, webhooks and campaign analytics. Programmatic access is delivered through a public REST API at api.playable.com documented with an OpenAPI 3.0 definition and secured with OAuth 2.0 client-credentials scoped per capability, plus a browser-side campaign SDK published to npm. API access is a Premium-plan entitlement; developer apps and credentials are created under Global settings.
image: https://playable.com/wp-content/uploads/2022/09/Logo_Playable_wobble.png
layout: provider
mcp_servers:
- description: ''
  name: playable-mcp.yml
  slug: playable-mcpyml
- description: ''
  name: mcp-oauth-server
  slug: mcp-oauth-server
modified: '2026-08-12'
name: Playable
nav: Providers
network: true
overview: 'Playable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, marketing-gamification, interactive-marketing, campaign-management, and zero-party-data.


  The Playable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Playable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Playable Plans Pricing
  plan_count: 3
  slug: playable-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 1
  name: Playable Rate Limits
  slug: playable-rate-limits
scopes:
- name: Playable Scopes
  scope_count: 37
  slug: playable-scopes
  summary_line: 37 scopes · clientCredentials
score:
  band: strong
  composite: 64.6
  delta: -2.9
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 57.7
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 67.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/playable/refs/heads/main/screenshots/playable-2026-08-17T080409.png
security:
- kind: authentication
  name: Playable Authentication
  slug: playable-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Playable Domain Security
  slug: playable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Playable Trust Center
  slug: playable-trust-center
  summary_line: ISO 27001:2022, ISAE 3000 Type 2, GDPR
slug: playable
tags:
- Company
- marketing-gamification
- interactive-marketing
- campaign-management
- zero-party-data
- lead-generation
- loyalty
- martech
- webhooks
- oauth2
website: https://playable.com/
---
