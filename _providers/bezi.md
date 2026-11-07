---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.bezi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bezi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bezi.com/get-started/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bezi.com/get-started/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.bezi.com/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.bezi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bezi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bezi.com/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/bezi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bezi3d
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bezi.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bezi.com/privacy-policy
- group: operate
  href: https://artifacts.apis.io/bezi/changelog/bezi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bezi-changelog.yml
- group: agent
  href: https://artifacts.apis.io/bezi/llms/bezi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bezi-llms.txt
- group: auth
  href: https://artifacts.apis.io/bezi/security/bezi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bezi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bezi/security/bezi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bezi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bezi.com/security
- group: design
  href: https://artifacts.apis.io/bezi/conformance/bezi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bezi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bezi.com/security
created: '2026-07-17'
description: Bezi is an AI agent for Unity game developers that runs directly inside the Unity Editor. It indexes a project's scripts, assets, scenes, packages and documentation in real time to deliver context-aware debugging, code generation, shader creation, scene building and no-code Unity tool automation that follows each project's own conventions. Bezi supports multiple frontier models (Claude Sonnet, GPT, GLM and others), a Skills system for packaging repeatable workflows, MCP connections for external context (Blender, Miro, Notion, Perforce and more), and real-time collaborative team workspaces. The company is SOC 2 Type II certified and backed by Bessemer Venture Partners and Uncork Capital. Bezi ships an in-editor product and desktop/plugin experience rather than a public HTTP API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bezi.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.bezi.com over HTTP.
  name: Bezi MCP Server
  slug: bezi
modified: '2026-07-18'
name: Bezi
nav: Providers
network: true
overview: 'Bezi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Game Development, Unity, and Developer Tools.


  Bezi''s developer surface includes documentation, getting-started guide, quickstart, engineering blog, pricing, signup flow, support, and 12 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 58.3
    operational_transparency: 28.9
  previous_composite: 31.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bezi/bezi-2026-07-25T202847.png
security:
- kind: domain-security
  name: Bezi Domain Security
  slug: bezi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bezi Vulnerability Disclosure
  slug: bezi-vulnerability-disclosure
  summary_line: contact published
slug: bezi
tags:
- Company
- Artificial Intelligence
- Game Development
- Unity
- Developer Tools
- AI Agents
- Coding Assistant
website: https://www.bezi.com/
---
