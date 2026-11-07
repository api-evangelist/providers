---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Curse Agentic Access
  operation_count: 46
  slug: curse-agentic-access
  summary_line: 46 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.curseforge.com
  baseurl_source: declared
  description: The Categories API from Curse — 1 operation(s) for categories.
  name: Curse Categories API
  slug: curse-categories-api
- baseURL: https://api.curseforge.com
  baseurl_source: declared
  description: The Files API from Curse — 7 operation(s) for files.
  name: Curse Files API
  slug: curse-files-api
- baseURL: https://api.curseforge.com
  baseurl_source: declared
  description: The Games API from Curse — 6 operation(s) for games.
  name: Curse Games API
  slug: curse-games-api
- baseURL: https://api.curseforge.com
  baseurl_source: declared
  description: The Minecraft API from Curse — 4 operation(s) for minecraft.
  name: Curse Minecraft API
  slug: curse-minecraft-api
- baseURL: https://api.curseforge.com
  baseurl_source: declared
  description: The Mods API from Curse — 19 operation(s) for mods.
  name: Curse Mods API
  slug: curse-mods-api
- baseURL: https://api.curseforge.com
  baseurl_source: declared
  description: The Subscriptions API from Curse — 5 operation(s) for subscriptions.
  name: Curse Subscriptions API
  slug: curse-subscriptions-api
- baseURL: https://api.curseforge.com
  baseurl_source: declared
  description: The UserMods API from Curse — 2 operation(s) for usermods.
  name: Curse User Mods API
  slug: curse-usermods-api
artifact_total: 21
collections:
- collection_type: open
  name: CurseForge Core Categories API
  slug: open-curse-categories-api
- collection_type: open
  name: CurseForge Core Categories Files API
  slug: open-curse-files-api
- collection_type: open
  name: CurseForge Core Categories Fingerprints API
  slug: open-curse-fingerprints-api
- collection_type: open
  name: CurseForge Core Categories Games API
  slug: open-curse-games-api
- collection_type: open
  name: CurseForge Core Categories Minecraft API
  slug: open-curse-minecraft-api
- collection_type: open
  name: CurseForge Core Categories Mods API
  slug: open-curse-mods-api
- collection_type: open
  name: CurseForge Core Categories Subscriptions API
  slug: open-curse-subscriptions-api
common:
- group: company
  title: ''
  type: Blog
  url: https://about.fandom.com/newsroom
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
  href: https://artifacts.apis.io/curse/openapi/_original/curse-core-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/curse-core-openapi-original.yml
- group: other
  href: https://artifacts.apis.io/curse/overlays/curse-core-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/curse-core-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/curse/mcp/curse-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/curse-mcp.yml
- group: agent
  href: https://artifacts.apis.io/curse/llms/curse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/curse-llms.txt
- group: agent
  href: https://artifacts.apis.io/curse/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/curse/authentication/curse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curse-authentication.yml
- group: agent
  href: https://artifacts.apis.io/curse/agentic-access/curse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/curse-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/curse/conventions/curse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/curse-conventions.yml
- group: design
  href: https://artifacts.apis.io/curse/errors/curse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/curse-problem-types.yml
- group: design
  href: https://artifacts.apis.io/curse/lifecycle/curse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/curse-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/curse/conformance/curse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curse-conformance.yml
- group: design
  href: https://artifacts.apis.io/curse/data-model/curse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/curse-data-model.yml
- group: build
  href: https://artifacts.apis.io/curse/packages/curse-packages.yml
  title: ''
  type: Packages
  url: packages/curse-packages.yml
- group: agent
  href: https://artifacts.apis.io/curse/well-known/curse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curse-well-known.yml
- group: auth
  href: https://artifacts.apis.io/curse/security/curse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/curse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/fandom_bbp
- group: auth
  href: https://artifacts.apis.io/curse/security/curse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curse-domain-security.yml
created: '2026-07-17'
description: Curse (Curse Inc.) built and operated CurseForge, Gamepedia, and the Curse gaming network; its platform assets are now operated under Fandom / Overwolf. The live developer surface is the CurseForge Core API — a REST API over the CurseForge catalog of game mods, modpacks, and add-ons, covering games, categories, mods, files, fingerprint matching, and Minecraft versions and mod loaders. It is authenticated with an x-api-key header issued from the CurseForge for Studios developer console, with third-party access granted via an approved application.
image: https://www.curseforge.com/images/mods/logos/curseforge.png
layout: provider
modified: '2026-10-06'
name: Curse
nav: Providers
network: true
overview: 'Curse publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Categories API, Files API, Games API, and 4 more. Tagged areas include Company, Gaming, MODS, Minecraft, and Game Content.


  The Curse catalog on APIs.io includes 1 Spectral governance ruleset.


  Curse''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, authentication, and 22 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Curse API Rules
  rule_count: 54
  severity_counts:
    error: 41
    hint: 0
    info: 5
    warn: 8
  slug: curse-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 49.8
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 46.7
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/curse/curse-2026-07-25T210958.png
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
skill_count: 2
skills:
- name: Match installed mods by fingerprint
  slug: curse-match-installed-mods-by-fingerprint
- name: Search and download a CurseForge mod
  slug: curse-search-and-download-mod
slug: curse
tags:
- Company
- Gaming
- MODS
- Minecraft
- Game Content
- Developer Platform
- Catalog
website: https://www.fandom.com/
---
