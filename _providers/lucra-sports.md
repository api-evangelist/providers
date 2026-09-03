---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: The Health API from Lucra Sports — 1 operation(s) for health.
  name: Lucra Sports Health API
  slug: lucra-sports-health-api
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: The Locations API from Lucra Sports — 1 operation(s) for locations.
  name: Lucra Sports Locations API
  slug: lucra-sports-locations-api
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: The Recreational Games API from Lucra Sports — 5 operation(s) for recreational games.
  name: Lucra Sports Recreational Games API
  slug: lucra-sports-recreational-games-api
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: The States API from Lucra Sports — 1 operation(s) for states.
  name: Lucra Sports States API
  slug: lucra-sports-states-api
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: The TenantTagGroups API from Lucra Sports — 4 operation(s) for tenanttaggroups.
  name: Lucra Sports Tenant Tag Groups API
  slug: lucra-sports-tenanttaggroups-api
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: 'Modular tournament management endpoints. Unlike the legacy API which returns everything in a single call, the v2 API separates concerns into dedicated resources: | Resource | Path | Purpose | |-------'
  name: Lucra Sports Tournaments API
  slug: lucra-sports-tournaments-api
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: 'Drop-in replacement endpoints for the original tournament API operations. Request/response shapes are identical. --- ## Tournament Types ### CASH_FIXED The total prize pool is defined upfront and has '
  name: Lucra Sports Tournaments (Legacy) API
  slug: lucra-sports-tournaments-legacy-api
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: The User Score API from Lucra Sports — 1 operation(s) for user score.
  name: Lucra Sports User Score API
  slug: lucra-sports-user-score-api
- baseURL: https://forge.lucrasports.com
  baseurl_source: declared
  description: 'Manage webhook configurations to receive real-time event notifications via HTTP POST requests. --- ## Available Event Types | Event | Description | |-------|-------------| | `UserSignedUp` | New user '
  name: Lucra Sports Webhooks API
  slug: lucra-sports-webhooks-api
artifact_total: 15
asyncapis:
- description: ''
  name: Lucra Sports Webhooks
  slug: lucra-sports-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lucra-sports-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lucra-sports-forge-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.playlucra.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lucrasports.com/lucra-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lucrasports.com/lucra-sdk/readme
- group: docs
  title: ''
  type: APIReference
  url: https://forge.lucrasports.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lucrasports.com/lucra-sdk/games-you-play-gyp/gyp-sdks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lucra-Sports
- group: operate
  title: ''
  type: Support
  url: https://www.playlucra.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.playlucra.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.playlucra.com/newsroom
- group: start
  title: ''
  type: SignUp
  url: https://www.playlucra.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.playlucra.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.playlucra.com/legal/privacy-policy
- group: other
  title: ''
  type: ResponsibleGaming
  url: https://www.playlucra.com/legal/responsible-gaming
- group: other
  title: ''
  type: CaseStudies
  url: https://www.playlucra.com/case-studies
- group: commercial
  title: ''
  type: Plans
  url: plans/lucra-sports-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lucra-sports-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/lucra-sports-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lucra-sports-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lucra-sports-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lucra-sports-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lucra-sports-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lucra-sports-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lucra-sports-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/lucra-sports-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lucra-sports-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lucra-sports-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/lucra-sports-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lucra-sports-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lucra-sports-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lucra-sports-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lucra-sports-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucra-sports-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucra-sports-domain-security.yml
created: '2026-08-25'
description: 'Lucra (Lucra Sports, Inc.) is a competitive-loyalty and gamification platform that embeds real-money, free-to-play and peer-to-peer contests into third-party consumer apps and websites through a white-label SDK. Partners integrate Games You Play (head-to-head recreational matchups), Sports You Watch (prediction contests), Tournaments, Mini Games and Achievements without building the regulated infrastructure themselves: Lucra acts as merchant of record and operates the KYC, geolocation, age verification, payments, fraud monitoring, prize settlement and responsible-gaming controls behind the experience. The developer surface is a tenant-scoped server-to-server REST API (the Forge gateway) plus iOS, Android, React Native and JavaScript client SDKs, a signed webhook event stream, and a sandbox environment.'
image: https://framerusercontent.com/images/ig8OHgXmBzrkMRo5krWVBCgcrhI.png
layout: provider
mcp_servers:
- description: ''
  name: Lucra Sports MCP Server
  slug: lucra-sports-mcp-server
modified: '2026-08-25'
name: Lucra Sports
nav: Providers
network: true
overview: 'Lucra Sports publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Health API, Locations API, Recreational Games API, and 6 more. Tagged areas include Gaming, Sports, Gamification, Loyalty, and Tournaments.


  The Lucra Sports catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lucra Sports'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 29 more developer resources.'
plans:
- name: Lucra Sports Plans Pricing
  plan_count: 0
  slug: lucra-sports-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Lucra Sports Rate Limits
  slug: lucra-sports-rate-limits
score:
  band: strong
  composite: 57.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.5
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 61.3
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 56.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucra-sports/refs/heads/main/screenshots/lucra-sports-2026-09-02T150330.png
security:
- kind: authentication
  name: Lucra Sports Authentication
  slug: lucra-sports-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lucra Sports Domain Security
  slug: lucra-sports-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lucra-sports
tags:
- Gaming
- Sports
- Gamification
- Loyalty
- Tournaments
- Contests
- Payments
- Wagering
- Embedded Finance
- SDK
- Webhook
- Compliance
website: https://www.playlucra.com/
---
