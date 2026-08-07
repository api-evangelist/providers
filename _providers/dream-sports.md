---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 154
  human_in_the_loop: 4
  name: Dream Sports Agentic Access
  operation_count: 254
  slug: dream-sports-agentic-access
  summary_line: 254 operations · 154 acting · 4 human-in-the-loop
api_count: 5
apis:
- description: Guardian is Dream Sports' open-source authentication and authorization platform, released through Dream Horizon under the MIT license. It implements OAuth 2.0 (authorization code, implicit, client cre
  name: Guardian Authentication & Authorization API
  slug: guardian-authentication-authorization-api
- description: Checkmate is Dream Sports' open-source test case management application, published through Dream Horizon with a hosted reference instance at checkmate.dreamhorizon.org that also serves the OpenAPI doc
  name: Checkmate Test Management API
  slug: checkmate-test-management-api
- description: Raven is Dream Sports' open-source in-app messaging, nudge and journey platform. The Raven Journey API models journeys, triggers, cohorts, templates, campaigns and analytics; the companion Raven Thund
  name: Raven In-App Messaging & Journeys API
  slug: raven-in-app-messaging-journeys-api
- description: Delivr is Dream Sports' open-source over-the-air mobile update and release platform (React Native, iOS, Android), with a self-hosted OTA server whose OpenAPI covers apps, deployments, releases, rollba
  name: Delivr & DOTA Over-The-Air Update APIs
  slug: delivr-dota-over-the-air-update-apis
- description: First-party Model Context Protocol server (stdio transport) published by Dream Horizon that exposes Odin — Dream Sports' internal developer platform — to agents. It adapts 45 documented tools onto the
  name: Odin MCP Server
  slug: odin-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Dream Sports Webhooks
  slug: dream-sports-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dream-sports-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dream-sports-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dreamsports.group/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dreamhorizon.org/
- group: docs
  title: ''
  type: Documentation
  url: https://dreamhorizon.org/projects
- group: docs
  title: ''
  type: APIReference
  url: https://guardianhq.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://guardianhq.io/docs/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/HrJZCrkeAs
- group: company
  title: ''
  type: Blog
  url: https://blog.dream11engineering.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dream-horizon-org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dreamsports.group/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dreamsports.group/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://github.com/dream-horizon-org/logwise/blob/master/SECURITY.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dream-sports-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dream-sports-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dream-sports-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dream-sports-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/dream-sports-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dream-sports-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dream-sports-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dream-sports-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dream-sports-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dream-sports-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dream-sports-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dream-sports-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dream-sports-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dream-sports-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dream-sports-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dream-sports-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dream-sports-webhooks.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://dream-horizon-org.github.io/odin/docs/roadmap/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Dream Sports is India''s largest sports technology company, founded by Harsh Jain and Bhavit Sheth, whose consumer brands include Dream11 (fantasy sports), FanCode (sports content, streaming and commerce), DreamSetGo (sports travel and experiences), Dream Cricket, Dream Money and DreamStreet, alongside the Dream Sports Foundation. Its public machine-readable API surface is not a consumer product API but two engineering surfaces: the "Login with Dream11" OpenID Connect identity service at auth.dream11.com, which publishes an OIDC discovery document, and Dream Horizon (also branded HorizonOS) — the company''s open-source initiative that releases the platform engineering stack built to run Dream11 at 250M+ users. Dream Horizon publishes real OpenAPI 3.x specifications for Guardian (authentication and authorization), Checkmate (test management), Raven and Raven Thunder (in-app messaging and journeys), Delivr and DOTA (over-the-air mobile updates), protobuf service definitions for
  Odin (its internal developer platform), a first-party stdio MCP server for Odin, an llms.txt, and client SDKs published to npm under the @d11 scope and to LuaRocks under the dream11 namespace.'
image: https://www.dreamsports.group/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: dream-sports-mcp.yml
  slug: dream-sports-mcpyml
modified: '2026-08-04'
name: Dream Sports
nav: Providers
network: true
overview: 'Dream Sports publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Guardian Authentication & Authorization API, Checkmate Test Management API, Raven In-App Messaging & Journeys API, and 1 more. Tagged areas include Company, sports-technology, fantasy-sports, open-source, and developer-tools.


  The Dream Sports catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dream Sports'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 25 more developer resources.'
random_paper: 6
scopes:
- name: Dream Sports Scopes
  scope_count: 7
  slug: dream-sports-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 58.4
    developer_ergonomics: 75.5
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 12.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Dream Sports Authentication
  slug: dream-sports-authentication
  summary_line: apiKey/http/openIdConnect · 6 schemes
- kind: domain-security
  name: Dream Sports Domain Security
  slug: dream-sports-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dream Sports Vulnerability Disclosure
  slug: dream-sports-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: dream-sports
tags:
- Company
- sports-technology
- fantasy-sports
- open-source
- developer-tools
- platform-engineering
- authentication
- openid-connect
- oauth2
- mobile
- react-native
- devops
- observability
- test-management
- ota-updates
- feature-flags
- india
- mcp
- agent-native
website: https://www.dreamsports.group/
---
