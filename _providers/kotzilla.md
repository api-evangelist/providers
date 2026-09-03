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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Hosted remote Model Context Protocol server that connects an AI coding assistant to the Kotzilla Platform. Fifteen tools covering app registration, SDK onboarding, telemetry, issue detection and conte
  name: Kotzilla MCP Server
  slug: kotzilla-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://kotzilla.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.kotzilla.io/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.kotzilla.io/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.kotzilla.io/docs/settings/apiUse
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.kotzilla.io/docs/getstartedCustom/overview
- group: operate
  title: ''
  type: Support
  url: https://join.slack.com/t/cloud-inject/shared_invite/zt-28grcrqc7-zHPUy9XCVZ1mNwE_afUZYw
- group: operate
  title: ''
  type: HelpCenter
  url: https://doc.kotzilla.io/docs/discover/help
- group: company
  title: ''
  type: Blog
  url: https://blog.kotzilla.io/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.kotzilla.io/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kotzilla-io
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/InsertKoinIO
- group: commercial
  title: ''
  type: Pricing
  url: https://kotzilla.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.kotzilla.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kotzilla.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kotzilla.io/privacy-policy
- group: commercial
  title: ''
  type: License
  url: https://doc.kotzilla.io/docs/discover/license
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.kotzilla.io/docs/releaseNotes/changelogSDK
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kotzilla-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://doc.kotzilla.io/docs/releaseNotes/versionUpgrades
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kotzilla-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: https://console.kotzilla.io/sandbox-home
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kotzilla-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/kotzilla-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kotzilla-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kotzilla-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kotzilla-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kotzilla-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kotzilla-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kotzilla-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kotzilla-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kotzilla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kotzilla-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kotzilla-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kotzilla-mcp.yml
created: '2026-08-17'
description: 'Kotzilla is a French developer-observability company based in Toulouse, founded by the creators of Koin — the open-source dependency-injection framework for Kotlin, which Kotzilla still maintains. The Kotzilla Platform monitors Android and Kotlin Multiplatform applications by using Koin''s containerization to map runtime telemetry onto application architecture, detecting slow startups, ANRs, crashes, background work and slow rendering, then tracing each issue back to the dependency graph that caused it. The platform has four components: the Koin IDE plugin for IntelliJ and Android Studio, the Kotzilla SDK distributed through Maven Central, the Kotzilla Console, and a hosted remote MCP server that connects AI coding assistants to the platform. Kotzilla publishes no REST or GraphQL API — the MCP server, with fifteen tools behind OAuth 2.0 with PKCE and dynamic client registration, is its only machine-readable, agent-callable surface.'
image: https://storage.googleapis.com/strapi_cms_gcp/kotzilla_light_background_413a1a7089/kotzilla_light_background_413a1a7089.svg
layout: provider
mcp_servers:
- description: ''
  name: Kotzilla MCP Server
  slug: kotzilla-mcp-server
modified: '2026-08-17'
name: Kotzilla
nav: Providers
network: true
overview: 'Kotzilla publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Observability, Monitoring, and Developer Tools.


  Kotzilla''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Kotzilla Plans Pricing
  plan_count: 2
  slug: kotzilla-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Kotzilla Rate Limits
  slug: kotzilla-rate-limits
scopes:
- name: Kotzilla Scopes
  scope_count: 3
  slug: kotzilla-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kotzilla/refs/heads/main/screenshots/kotzilla-2026-09-02T150159.png
security:
- kind: authentication
  name: Kotzilla Authentication
  slug: kotzilla-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Kotzilla Domain Security
  slug: kotzilla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kotzilla
tags:
- Company
- Ai Data
- Observability
- Monitoring
- Developer Tools
- Kotlin
- Android
- Mobile
- Dependency Injection
- Performance
- MCP
- Agents
website: https://kotzilla.io/
---
