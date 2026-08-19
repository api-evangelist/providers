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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Delphi Agentic Access
  operation_count: 25
  slug: delphi-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 8
apis:
- description: Store and manage contextual information about users in your audience.
  name: Delphi Audience API
  slug: delphi-audience-api
- description: Retrieve your clone's public profile information.
  name: Delphi Clone API
  slug: delphi-clone-api
- description: Create conversations, stream responses, view history, and manage conversation lifecycle.
  name: Delphi Conversations API
  slug: delphi-conversations-api
- description: Retrieve suggested questions configured for your clone.
  name: Delphi Questions API
  slug: delphi-questions-api
- description: Search your clone's digital mind for relevant chunks or content.
  name: Delphi Search API
  slug: delphi-search-api
- description: Create tags and organize your audience.
  name: Delphi Tags API
  slug: delphi-tags-api
- description: Track consumption metrics and access tiers for your users.
  name: Delphi Usage API
  slug: delphi-usage-api
- description: Stream voice responses and synthesize speech as real-time PCM audio.
  name: Delphi Voice API
  slug: delphi-voice-api
artifact_total: 22
asyncapis:
- description: ''
  name: Delphi Webhooks
  slug: delphi-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Delphi Audience API
  slug: open-delphi-audience-api
- collection_type: open
  name: Delphi Audience Clone API
  slug: open-delphi-clone-api
- collection_type: open
  name: Delphi Audience Conversations API
  slug: open-delphi-conversations-api
- collection_type: open
  name: Delphi Audience Questions API
  slug: open-delphi-questions-api
- collection_type: open
  name: Delphi Audience Search API
  slug: open-delphi-search-api
- collection_type: open
  name: Delphi Audience Tags API
  slug: open-delphi-tags-api
- collection_type: open
  name: Delphi Audience Usage API
  slug: open-delphi-usage-api
- collection_type: open
  name: Delphi Audience Voice API
  slug: open-delphi-voice-api
common:
- group: company
  title: ''
  type: Website
  url: https://delphi.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.delphi.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.delphi.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.delphi.ai/advanced/actions/api-immortal-only
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.delphi.ai/advanced/actions/api-immortal-only
- group: auth
  title: ''
  type: Authentication
  url: authentication/delphi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/delphi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/delphi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/delphi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.delphi.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/delphi-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/delphi-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delphi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/delphi-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/delphi-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/delphi-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/delphi-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/delphi-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/delphi-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/delphi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.delphi.ai
- group: company
  title: ''
  type: Blog
  url: https://delphi.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/delphi-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://delphi.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://delphi.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://delphi.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://delphi.ai/privacy
created: '2026-07-17'
description: 'Delphi is an AI platform for building "Digital Minds" — hyper-realistic AI clones trained exclusively on a person''s own content (podcasts, videos, blogs, long-form writing, live feeds) that match how they speak, write, and think. Audiences can call, text, or video-chat a clone 24/7 for Q&A, coaching, mentorship, and engagement, with omnichannel reach across websites, SMS, Telegram, Slack, and learning platforms like Kajabi and Thinkific. Delphi''s v3 REST API (Immortal plan) lets developers embed a Digital Mind directly in their own app: create conversations, stream text and voice responses, manage the audience and its contextual memory, organize contacts with tags, search the clone''s knowledge base for RAG, track per-user usage, and receive events via signed webhooks. Delphi is backed by Menlo Ventures.'
image: https://avatars.githubusercontent.com/u/120126721?v=4
layout: provider
mcp_servers:
- description: ''
  name: delphi-mcp.yml
  slug: delphi-mcpyml
modified: '2026-07-18'
name: Delphi
nav: Providers
network: true
overview: 'Delphi publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Audience API, Clone API, Conversations API, and 5 more. Tagged areas include Company, Artificial Intelligence, AI Clones, Digital Minds, and Conversational AI.


  The Delphi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Delphi''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 21 more developer resources.'
random_paper: 34
score:
  band: developing
  composite: 40.9
  delta: -0.8
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 23.5
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/delphi/refs/heads/main/screenshots/delphi-2026-07-25T211653.png
security:
- kind: authentication
  name: Delphi Authentication
  slug: delphi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Delphi Domain Security
  slug: delphi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: delphi
tags:
- Company
- Artificial Intelligence
- AI Clones
- Digital Minds
- Conversational AI
- Voice
- Search
- RAG
- Knowledge Base
- Creator Economy
- Webhooks
website: https://delphi.ai
---
