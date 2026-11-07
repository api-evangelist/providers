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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.shapes.inc/v1/
  baseurl_source: declared
  description: The Models API from Shapes — 1 operation(s) for models.
  name: Shapes Models API
  slug: shapes-models-api
- baseURL: https://api.shapes.inc/v1/
  baseurl_source: declared
  description: The Shapes API from Shapes — 1 operation(s) for shapes.
  name: Shapes API
  slug: shapes-shapes-api
- baseURL: https://api.shapes.inc/v1/
  baseurl_source: declared
  description: The Chat Completions API from Shapes — 1 operation(s) for chat completions.
  name: Shapes Chat Completions API
  slug: shapes-chat-completions-api
artifact_total: 12
collections:
- collection_type: open
  name: Shapes Chat API
  slug: open-shapes-chat-api
- collection_type: open
  name: Shapes Chat Models API
  slug: open-shapes-models-api
- collection_type: open
  name: Chat Shapes API
  slug: open-shapes-shapes-api
common:
- group: company
  title: ''
  type: Blog
  url: https://shapes.inc/blog
- group: other
  href: https://artifacts.apis.io/shapes/overlays/shapes-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shapes-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://shapes.inc
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shapes.inc
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shapes.inc/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/shapesinc/shapes-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shapes.inc/learninghub
- group: operate
  title: ''
  type: Support
  url: https://talk.shapes.inc/support
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.shapes.inc/premium
- group: start
  title: ''
  type: SignUp
  url: https://shapes.inc/developer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shapesinc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shapes.inc/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shapes.inc/privacy
- group: agent
  href: https://artifacts.apis.io/shapes/llms/shapes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shapes-llms.txt
- group: build
  href: https://artifacts.apis.io/shapes/packages/shapes-packages.yml
  title: ''
  type: Packages
  url: packages/shapes-packages.yml
- group: agent
  href: https://artifacts.apis.io/shapes/mcp/shapes-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/shapes-mcp.yml
- group: agent
  href: https://artifacts.apis.io/shapes/well-known/shapes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shapes-well-known.yml
- group: auth
  href: https://artifacts.apis.io/shapes/authentication/shapes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shapes-authentication.yml
- group: design
  href: https://artifacts.apis.io/shapes/conventions/shapes-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shapes-conventions.yml
- group: design
  href: https://artifacts.apis.io/shapes/conformance/shapes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shapes-conformance.yml
- group: design
  href: https://artifacts.apis.io/shapes/data-model/shapes-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shapes-data-model.yml
- group: design
  href: https://artifacts.apis.io/shapes/lifecycle/shapes-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shapes-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/shapes/lifecycle/shapes-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/shapes-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/shapes/security/shapes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shapes-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/shapes/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Shapes, Inc. is a social AI platform where humans and AI characters ("Shapes") share the same group chats. Shapes are general-purpose social agents with rich personalities, voice, and short-term plus long-term memory that persists across platforms, running on 50+ free text, image, and voice models. Backed by Lightspeed Venture Partners, the company operates the consumer app at shapes.inc and previously offered an OpenAI-compatible developer API (api.shapes.inc) for building Shapes into any application; that developer API was deprecated on 2025-09-25 and the team has said building with Shapes will return. This profile captures the company identity plus the documented API surface, developer tooling, and security posture for the API Evangelist network.
image: https://shapes.inc/og-image-1200x630.png
layout: provider
mcp_servers:
- description: MCP server; 3 tools listed. A candidate, not confirmed as published by the provider.
  name: Shapes MCP Server
  slug: shapes
modified: '2026-10-06'
name: Shapes
nav: Providers
network: true
overview: 'Shapes publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Models API, Chat Completions API, and 1 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Chat, and Social.


  The Shapes catalog on APIs.io includes 1 Spectral governance ruleset.


  Shapes'' developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 18 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Shapes API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: shapes-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 13.2
  previous_composite: 44.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shapes/shapes-2026-08-17T081822.png
security:
- kind: authentication
  name: Shapes Authentication
  slug: shapes-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shapes Domain Security
  slug: shapes-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Chat with a Shape
  slug: shapes-chat-with-a-shape
- name: Look up a public Shape profile
  slug: shapes-lookup-shape-profile
slug: shapes
tags:
- Company
- Artificial Intelligence
- AI Agents
- Chat
- Social
- Conversational AI
- LLM
- Voice
- Developer API
website: https://shapes.inc
---
