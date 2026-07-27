---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Curse Agentic Access
  operation_count: 46
  slug: curse-agentic-access
  summary_line: 46 operations · 19 acting
api_count: 7
apis:
- description: The Categories API from Curse — 1 operation(s) for categories.
  name: Curse Categories API
  slug: curse-categories-api
- description: The Files API from Curse — 7 operation(s) for files.
  name: Curse Files API
  slug: curse-files-api
- description: The Fingerprints API from Curse — 4 operation(s) for fingerprints.
  name: Curse Fingerprints API
  slug: curse-fingerprints-api
- description: The Games API from Curse — 6 operation(s) for games.
  name: Curse Games API
  slug: curse-games-api
- description: The Minecraft API from Curse — 4 operation(s) for minecraft.
  name: Curse Minecraft API
  slug: curse-minecraft-api
- description: The Mods API from Curse — 19 operation(s) for mods.
  name: Curse Mods API
  slug: curse-mods-api
- description: The Subscriptions API from Curse — 5 operation(s) for subscriptions.
  name: Curse Subscriptions API
  slug: curse-subscriptions-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.fandom.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.curseforge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.curseforge.com/rest-api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.curseforge.com/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.curseforge.com/rest-api/
- group: operate
  title: ''
  type: Support
  url: https://support.curseforge.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.curseforge.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.curseforge.com/
- group: start
  title: ''
  type: SignUp
  url: https://console.curseforge.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.curseforge.com/rest-api/#terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fandom.com/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/curse-core-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/curse-core-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/curse-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curse-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/curse-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/curse-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curse-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curse-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/curse-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/curse-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/curse-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/curse-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/curse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/fandom_bbp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curse-domain-security.yml
created: '2026-07-17'
description: Curse (Curse Inc.) built and operated CurseForge, Gamepedia, and the Curse gaming network; its platform assets are now operated under Fandom / Overwolf. The live developer surface is the CurseForge Core API — a REST API over the CurseForge catalog of game mods, modpacks, and add-ons, covering games, categories, mods, files, fingerprint matching, and Minecraft versions and mod loaders. It is authenticated with an x-api-key header issued from the CurseForge for Studios developer console, with third-party access granted via an approved application.
image: https://www.curseforge.com/images/mods/logos/curseforge.png
layout: provider
mcp_servers:
- description: ''
  name: curse-mcp.yml
  slug: curse-mcpyml
modified: '2026-07-18'
name: Curse
nav: Providers
network: true
overview: 'Curse publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Files API, Fingerprints API, and 4 more. Tagged areas include Company, Gaming, Mods, Minecraft, and Game Content.


  Curse''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 45.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 46.1
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 45.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curse/refs/heads/main/screenshots/curse-2026-07-25T210958.png
security:
- kind: authentication
  name: Curse Authentication
  slug: curse-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Curse Domain Security
  slug: curse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Curse Vulnerability Disclosure
  slug: curse-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: curse
tags:
- Company
- Gaming
- Mods
- Minecraft
- Game Content
- Developer Platform
- Catalog
website: https://www.fandom.com/
---
