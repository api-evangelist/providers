---
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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Forge is Lucra's unified server-to-server API gateway. It exposes tenant-scoped tournament management (create, update, cancel, complete, leaderboard, rewards, tags), recreational game (Games You Play)
  name: Lucra Forge API
  slug: lucra-sports-forge-api
artifact_total: 7
asyncapis:
- description: ''
  name: Lucra Sports Webhooks
  slug: lucra-sports-webhooks
common:
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
overview: 'Lucra Sports publishes 1 API on the [APIs.io](https://apis.io/) network: Lucra Forge API. Tagged areas include Gaming, Sports, Gamification, Loyalty, and Tournaments.


  The Lucra Sports catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lucra Sports'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 27 more developer resources.'
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
  composite: 57.5
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 16.7
    contract_quality: 56.1
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 47.4
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- SDKs
- Webhooks
- Compliance
website: https://www.playlucra.com/
---
