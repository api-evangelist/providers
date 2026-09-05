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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.shapes.inc/v1/
  baseurl_source: declared
  description: The Chat API from Shapes — 1 operation(s) for chat.
  name: Shapes Chat API
  slug: shapes-chat-api
- baseURL: https://api.shapes.inc/v1/
  baseurl_source: declared
  description: The Models API from Shapes — 1 operation(s) for models.
  name: Shapes Models API
  slug: shapes-models-api
- baseURL: https://api.shapes.inc/v1/
  baseurl_source: declared
  description: The Shapes API from Shapes — 1 operation(s) for shapes.
  name: Shapes Shapes API
  slug: shapes-shapes-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
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
  title: ''
  type: LLMsTxt
  url: llms/shapes-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/shapes-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shapes-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shapes-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shapes-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shapes-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shapes-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shapes-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shapes-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/shapes-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shapes-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Shapes, Inc. is a social AI platform where humans and AI characters ("Shapes") share the same group chats. Shapes are general-purpose social agents with rich personalities, voice, and short-term plus long-term memory that persists across platforms, running on 50+ free text, image, and voice models. Backed by Lightspeed Venture Partners, the company operates the consumer app at shapes.inc and previously offered an OpenAI-compatible developer API (api.shapes.inc) for building Shapes into any application; that developer API was deprecated on 2025-09-25 and the team has said building with Shapes will return. This profile captures the company identity plus the documented API surface, developer tooling, and security posture for the API Evangelist network.
image: https://shapes.inc/og-image-1200x630.png
layout: provider
mcp_servers:
- description: ''
  name: Shapes MCP Server
  slug: shapes-mcp-server
modified: '2026-07-21'
name: Shapes
nav: Providers
network: true
overview: 'Shapes publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chat API, Models API, and Shapes API. Tagged areas include Company, Artificial Intelligence, AI Agents, Chat, and Social.


  Shapes'' developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 54.2
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 43.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shapes/refs/heads/main/screenshots/shapes-2026-08-17T081822.png
security:
- kind: authentication
  name: Shapes Authentication
  slug: shapes-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shapes Domain Security
  slug: shapes-domain-security
  summary_line: TLSv1.3 · DMARC
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
