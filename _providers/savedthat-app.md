---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Savedthat App Agentic Access
  operation_count: 4
  slug: savedthat-app-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: Save social videos (YouTube, Instagram Reels, TikTok) and search across their transcripts by meaning. Requires Supabase JWT.
  name: SavedThat API
  slug: savedthat-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/savedthat-app/agentic-access/savedthat-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/savedthat-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/savedthat-app/plans/savedthat-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/savedthat-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/savedthat-app/rules/savedthat-app-rules.yml
  title: ''
  type: Spectral
  url: rules/savedthat-app-rules.yml
- group: agent
  href: https://artifacts.apis.io/savedthat-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/savedthat-app/authentication/savedthat-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/savedthat-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/savedthat-app/errors/savedthat-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/savedthat-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/savedthat-app/conformance/savedthat-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/savedthat-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/savedthat-app/llms/savedthat-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/savedthat-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/savedthat-app/mcp/savedthat-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/savedthat-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/savedthat-app/well-known/savedthat-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/savedthat-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/savedthat-app/hosts/savedthat-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/savedthat-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/savedthat-app/vendors/savedthat-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/savedthat-app-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://savedthat.app/login
- group: auth
  href: https://artifacts.apis.io/savedthat-app/security/savedthat-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/savedthat-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://savedthat.app/
- group: docs
  title: ''
  type: Documentation
  url: https://savedthat.app/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://savedthat.app/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://savedthat.app/support
- group: company
  title: ''
  type: Blog
  url: https://savedthat.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://savedthat.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://savedthat.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://savedthat.app/
created: '2026-10-30'
description: SavedThat is a cross-platform app that makes saved videos (YouTube, Instagram Reels, TikTok) searchable by what was actually said. Every saved link is auto-transcribed and indexed with multilingual semantic embeddings + full-text search, so a query like "the bit where they talked about Stripe webhooks" returns the exact video and timestamp.
image: https://savedthat.app/og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at savedthat.app.
  name: savedthat-app MCP Server
  slug: savedthat-app-mcp-yml
modified: '2026-10-30'
name: savedthat-app
nav: Providers
network: true
overview: 'savedthat-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Artificial Intelligence, Search, Transcription, and Productivity.


  The savedthat-app catalog on APIs.io includes 1 Spectral governance ruleset.


  savedthat-app''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Savedthat App Plans Pricing
  plan_count: 4
  slug: savedthat-app-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: savedthat-app API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: savedthat-app-rules
scopes:
- name: Savedthat App Scopes
  scope_count: 0
  slug: savedthat-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.2
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/savedthat-app/savedthat-app-2026-11-03T142820.png
security:
- kind: authentication
  name: Savedthat App Authentication
  slug: savedthat-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Savedthat App Domain Security
  slug: savedthat-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: get-transcript
  slug: savedthat-app-get-transcript
- name: list-videos
  slug: savedthat-app-list-videos
- name: save-video
  slug: savedthat-app-save-video
- name: search-transcripts
  slug: savedthat-app-search-transcripts
slug: savedthat-app
tags:
- Video
- Artificial Intelligence
- Search
- Transcription
- Productivity
website: https://savedthat.app/
---
