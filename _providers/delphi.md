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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Delphi Agentic Access
  operation_count: 25
  slug: delphi-agentic-access
  summary_line: 25 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.delphi.ai
  baseurl_source: declared
  description: Store and manage contextual information about users in your audience.
  name: Delphi Audience API
  slug: delphi-audience-api
- baseURL: https://api.delphi.ai
  baseurl_source: declared
  description: Retrieve your clone's public profile information.
  name: Delphi Clone API
  slug: delphi-clone-api
- baseURL: https://api.delphi.ai
  baseurl_source: declared
  description: Create conversations, stream responses, view history, and manage conversation lifecycle.
  name: Delphi Conversations API
  slug: delphi-conversations-api
- baseURL: https://api.delphi.ai
  baseurl_source: declared
  description: Retrieve suggested questions configured for your clone.
  name: Delphi Questions API
  slug: delphi-questions-api
- baseURL: https://api.delphi.ai
  baseurl_source: declared
  description: Search your clone's digital mind for relevant chunks or content.
  name: Delphi Search API
  slug: delphi-search-api
- baseURL: https://api.delphi.ai
  baseurl_source: declared
  description: Create tags and organize your audience.
  name: Delphi Tags API
  slug: delphi-tags-api
- baseURL: https://api.delphi.ai
  baseurl_source: declared
  description: Track consumption metrics and access tiers for your users.
  name: Delphi Usage API
  slug: delphi-usage-api
- baseURL: https://api.delphi.ai
  baseurl_source: declared
  description: Stream voice responses and synthesize speech as real-time PCM audio.
  name: Delphi Voice API
  slug: delphi-voice-api
artifact_total: 27
asyncapis:
- description: ''
  name: Delphi Webhooks
  slug: delphi-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/delphi/plans/delphi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delphi-plans-pricing.yml
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
  href: https://artifacts.apis.io/delphi/authentication/delphi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delphi-authentication.yml
- group: design
  href: https://artifacts.apis.io/delphi/conventions/delphi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delphi-conventions.yml
- group: design
  href: https://artifacts.apis.io/delphi/errors/delphi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/delphi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/delphi/lifecycle/delphi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/delphi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.delphi.ai
- group: operate
  href: https://artifacts.apis.io/delphi/changelog/delphi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/delphi-changelog.yml
- group: design
  href: https://artifacts.apis.io/delphi/conformance/delphi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/delphi-conformance.yml
- group: auth
  href: https://artifacts.apis.io/delphi/security/delphi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delphi-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/delphi/agentic-access/delphi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/delphi-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/delphi/mcp/delphi-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/delphi-mcp.yml
- group: design
  href: https://artifacts.apis.io/delphi/asyncapi/delphi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/delphi-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/delphi/llms/delphi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delphi-llms.txt
- group: design
  href: https://artifacts.apis.io/delphi/data-model/delphi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/delphi-data-model.yml
- group: design
  href: https://artifacts.apis.io/delphi/components/delphi-components.yml
  title: ''
  type: Components
  url: components/delphi-components.yml
- group: other
  href: https://artifacts.apis.io/delphi/overlays/delphi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/delphi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/delphi/skills/_index.yml
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
finops:
- has_sources: true
  method: derived
  name: Delphi Finops
  primary_unit: subscription
  service_category: ''
  slug: delphi-finops
  template: false
image: https://avatars.githubusercontent.com/u/120126721?v=4
layout: provider
modified: '2026-07-18'
name: Delphi
nav: Providers
network: true
overview: 'Delphi publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audience API, Clone API, Conversations API, and 5 more. Tagged areas include Company, Artificial Intelligence, AI Clones, Digital Minds, and Conversational AI.


  The Delphi catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Delphi''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 22 more developer resources.'
plans:
- name: Delphi Plans Pricing
  plan_count: 4
  slug: delphi-plans-pricing
- name: Delphi Price Estimates
  plan_count: 0
  slug: delphi-price-estimates
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: Delphi API Rules
  rule_count: 70
  severity_counts:
    error: 63
    hint: 0
    info: 1
    warn: 6
  slug: delphi-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 22.5
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 47.9
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
screenshot: https://apis.io/screenshots/delphi/delphi-2026-07-25T211653.png
security:
- kind: authentication
  name: Delphi Authentication
  slug: delphi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Delphi Domain Security
  slug: delphi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Converse with a Delphi Digital Mind
  slug: delphi-converse-with-clone
- name: Manage a Delphi audience and its memory
  slug: delphi-manage-audience
- name: Search a Delphi digital mind for RAG
  slug: delphi-search-knowledge
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
- Webhook
website: https://delphi.ai
---
