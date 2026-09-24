---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: 'Remote MCP server (streamable-http, OAuth 2.1) exposing 14 tools to plan, compare and price AI video/image models, prepare an exact quote, approve a single paid generation, and recover results into a '
  name: MaxVideoAI MCP
  slug: maxvideoai-mcp
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/security/maxvideoai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maxvideoai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maxvideoai.com
- group: docs
  title: ''
  type: Documentation
  url: https://maxvideoai.com/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://maxvideoai.com/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://maxvideoai.com/integrations/claude
- group: start
  title: ''
  type: DeveloperPortal
  url: https://maxvideoai.com/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://maxvideoai.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://maxvideoai.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://maxvideoai.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maxvideoai.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://maxvideoai.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/camgraphe
- group: operate
  title: ''
  type: StatusPage
  url: https://maxvideoai.com/status
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/authentication/maxvideoai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/maxvideoai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/scopes/maxvideoai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/maxvideoai-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/conventions/maxvideoai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/maxvideoai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/conventions/maxvideoai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/maxvideoai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/errors/maxvideoai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/maxvideoai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/lifecycle/maxvideoai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/maxvideoai-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/changelog/maxvideoai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/maxvideoai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/conformance/maxvideoai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/maxvideoai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/well-known/maxvideoai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/maxvideoai-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/llms/maxvideoai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maxvideoai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/packages/maxvideoai-packages.yml
  title: ''
  type: Packages
  url: packages/maxvideoai-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/plans/maxvideoai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/maxvideoai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/maxvideoai/refs/heads/main/rate-limits/maxvideoai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/maxvideoai-rate-limits.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://maxvideoai.com/legal/subprocessors
created: '2026-09-20'
description: MaxVideoAI is a multi-model AI video and image production service delivered entirely through a remote MCP server, so assistants like Claude, ChatGPT and Codex can plan shots, compare current video/image models, estimate project budgets, prepare an exact quote, approve a single paid generation, recover results, and keep media in one private account library. It is pay-as-you-go on prepaid credits with no subscription, uses OAuth 2.1 (PKCE + dynamic client registration) for connection, and deliberately ships no REST API or customer API keys — the MCP tool surface is the product.
image: https://raw.githubusercontent.com/camgraphe/maxvideoai-plugin/main/assets/social/github-social-preview.png
layout: provider
mcp_servers:
- description: ''
  name: MaxVideoAI MCP Server
  slug: maxvideoai-mcp-server
- description: ''
  name: MCP manifest
  slug: mcp-manifest
modified: '2026-09-20'
name: MaxVideoAI
nav: Providers
network: true
overview: 'MaxVideoAI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Video Generation, Image Generation, MCP, and Agent-Native.


  MaxVideoAI''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, authentication, changelog, and 21 more developer resources.'
plans:
- name: Maxvideoai Plans Pricing
  plan_count: 0
  slug: maxvideoai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Maxvideoai Rate Limits
  slug: maxvideoai-rate-limits
scopes:
- name: Maxvideoai Scopes
  scope_count: 4
  slug: maxvideoai-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 70.4
    operational_transparency: 36.8
  previous_composite: 34.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Maxvideoai Authentication
  slug: maxvideoai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Maxvideoai Domain Security
  slug: maxvideoai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maxvideoai
tags:
- Artificial Intelligence
- Video Generation
- Image Generation
- MCP
- Agent-Native
- Text-to-Video
- Image-to-Video
- Creative Production
- Pay As You Go
website: https://maxvideoai.com
---
