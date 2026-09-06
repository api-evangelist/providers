---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.1
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'Hosted Model Context Protocol endpoint served from the Playable web property and advertised through RFC 9728 protected-resource metadata at playable.com/.well-known/oauth-protected-resource. Requires '
  name: Playable MCP Server
  slug: playable-mcp-server
- description: Browser-side JavaScript SDK (`@playable-marketing/campaign-sdk`) that exposes a promise-based `window.sdk` object plus an event stream so a host page can listen to campaign events and read campaign co
  name: Playable Campaign SDK
  slug: playable-campaign-sdk
- baseURL: https://api.playable.com
  baseurl_source: declared
  description: Campaigns
  name: Playable Campaigns API
  slug: playable-campaigns-api
- baseURL: https://api.playable.com
  baseurl_source: declared
  description: The media API from Playable — 1 operation(s) for media.
  name: Playable Media API
  slug: playable-media-api
- baseURL: https://api.playable.com
  baseurl_source: declared
  description: OAuth
  name: Playable OAUTH API
  slug: playable-oauth-api
- baseURL: https://api.playable.com
  baseurl_source: declared
  description: The user API from Playable — 1 operation(s) for user.
  name: Playable User API
  slug: playable-user-api
artifact_total: 16
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
  name: Playable MCP Server
  slug: playable-mcp-server
- description: ''
  name: Playable MCP Server
  slug: playable-mcp-server-2
modified: '2026-08-12'
name: Playable
nav: Providers
network: true
overview: 'Playable publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Media API, OAUTH API, and 1 more. Tagged areas include Company, marketing-gamification, interactive-marketing, Campaign Management, and Zero-Party Data.


  The Playable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Playable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Playable Plans Pricing
  plan_count: 3
  slug: playable-plans-pricing
random_paper: 2
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
  composite: 60.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 58.7
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 60.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Campaign Management
- Zero-Party Data
- Lead Generation
- Loyalty
- MarTech
- Webhook
- Authentication
website: https://playable.com/
---
