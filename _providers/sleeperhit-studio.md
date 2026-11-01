---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Programmatic story generation, source‑grounded planning, and durable artifact delivery for AI agents and enterprise integrations.
  name: Sleeper Hit Studio Story API
  slug: sleeper-hit-studio-story-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/sleeperhit-studio/plans/sleeperhit-studio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sleeperhit-studio-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sleeperhit-studio/vocabulary/sleeperhit-studio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sleeperhit-studio-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sleeperhit-studio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/sleeperhit-studio/cli/sleeperhit-studio-cli.yml
  title: ''
  type: CLI
  url: cli/sleeperhit-studio-cli.yml
- group: design
  href: https://artifacts.apis.io/sleeperhit-studio/conventions/sleeperhit-studio-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sleeperhit-studio-conventions.yml
- group: design
  href: https://artifacts.apis.io/sleeperhit-studio/conventions/sleeperhit-studio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sleeperhit-studio-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sleeperhit-studio/security/sleeperhit-studio-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sleeperhit-studio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sleeperhit-studio/authentication/sleeperhit-studio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sleeperhit-studio-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sleeperhit-studio/scopes/sleeperhit-studio-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sleeperhit-studio-scopes.yml
- group: design
  href: https://artifacts.apis.io/sleeperhit-studio/conformance/sleeperhit-studio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sleeperhit-studio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sleeperhit-studio/llms/sleeperhit-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sleeperhit-studio-llms.txt
- group: agent
  href: https://artifacts.apis.io/sleeperhit-studio/mcp/sleeperhit-studio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sleeperhit-studio-mcp.yml
- group: auth
  href: https://artifacts.apis.io/sleeperhit-studio/well-known/sleeperhit-studio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sleeperhit-studio-security.txt
- group: auth
  href: https://artifacts.apis.io/sleeperhit-studio/well-known/sleeperhit-studio-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sleeperhit-studio-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/sleeperhit-studio/well-known/sleeperhit-studio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sleeperhit-studio-well-known.yml
- group: other
  href: https://artifacts.apis.io/sleeperhit-studio/hosts/sleeperhit-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sleeperhit-studio-hosts.yml
- group: other
  href: https://artifacts.apis.io/sleeperhit-studio/vendors/sleeperhit-studio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sleeperhit-studio-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://sleeperhit.studio/signup?intent=business&interval=monthly&plan=development
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sleeperhit.studio/dashboard/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sleeperhit.studio/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sleeperhit.studio/api-reference
- group: auth
  href: https://artifacts.apis.io/sleeperhit-studio/security/sleeperhit-studio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sleeperhit-studio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sleeperhit-studio/security/sleeperhit-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sleeperhit-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sleeperhit.studio/
- group: docs
  title: ''
  type: Documentation
  url: https://sleeperhit.studio/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://sleeperhit.studio/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sleeperhit.studio/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sleeperhit.studio/privacy
- group: operate
  title: ''
  type: Support
  url: https://sleeperhit.studio/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://sleeperhit.studio/mcp
  - status: 401
    url: https://docs.sleeperhit.studio/mcp
  - status: 200
    url: https://sleeperhit.studio/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Sleeper Hit Studio is an enterprise-focused production studio that transforms internal company content into high‑quality audio, video, and interactive episodes. By integrating with tools like Notion, Linear, Slack, and major AI assistants, it automates the creation of podcasts, video shows, and narrative-driven updates for internal communications, product launches, training, and customer storytelling. The platform offers a pay‑as‑you‑go pricing model, customizable credits, and a suite of integrations that let teams generate, edit, and publish episodic content without needing dedicated media expertise.
image: https://sleeperhit.studio/images/hero-theater.png
layout: provider
mcp_servers:
- description: Remote MCP server at sleeperhit.studio.
  name: sleeperhit-studio MCP Server
  slug: sleeperhit-studio-mcp-yml
modified: '2026-10-30'
name: sleeperhit-studio
nav: Providers
network: true
overview: 'sleeperhit-studio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audio, Video, Podcast, and Enterprise.


  sleeperhit-studio''s developer surface includes CLI, authentication, signup flow, getting-started guide, API reference, documentation, pricing, and 22 more developer resources.'
plans:
- name: Sleeperhit Studio Plans Pricing
  plan_count: 1
  slug: sleeperhit-studio-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Sleeperhit Studio Rate Limits
  slug: sleeperhit-studio-rate-limits
scopes:
- name: Sleeperhit Studio Scopes
  scope_count: 0
  slug: sleeperhit-studio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 68.3
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sleeperhit Studio Authentication
  slug: sleeperhit-studio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sleeperhit Studio Domain Security
  slug: sleeperhit-studio-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Sleeperhit Studio Vulnerability Disclosure
  slug: sleeperhit-studio-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: get-background-activity
  slug: sleeperhit-studio-get-background
- name: script-share
  slug: sleeperhit-studio-script-share
slug: sleeperhit-studio
tags:
- Company
- Audio
- Video
- Podcast
- Enterprise
- Automation
website: https://sleeperhit.studio/
---
