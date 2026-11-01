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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Samora Ai Agentic Access
  operation_count: 17
  slug: samora-ai-agentic-access
  summary_line: 17 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.samora.ai
  baseurl_source: declared
  description: Trigger and retrieve individual outbound calls.
  name: Samora AI Calls API
  slug: samora-ai-calls-api
- baseURL: https://api.samora.ai
  baseurl_source: declared
  description: Create and manage outbound calling campaigns and their scheduled recipients.
  name: Samora AI Campaigns API
  slug: samora-ai-campaigns-api
- baseURL: https://api.samora.ai
  baseurl_source: declared
  description: Subscribe to real-time call events.
  name: Samora AI Webhooks API
  slug: samora-ai-webhooks-api
artifact_total: 13
asyncapis:
- description: Real-time call events delivered by Samora AI to a subscriber-provided HTTPS endpoint. Subscriptions are managed via the REST /v2/webhooks operations; each subscription returns a signing secret used to
  name: Samora AI Webhooks
  slug: samora-ai-webhooks-asyncapi
collections:
- collection_type: open
  name: Samora AI Calls API
  slug: open-samora-ai-calls-api
- collection_type: open
  name: Samora AI Calls Campaigns API
  slug: open-samora-ai-campaigns-api
- collection_type: open
  name: Samora AI Calls Webhooks API
  slug: open-samora-ai-webhooks-api
common:
- group: company
  title: ''
  type: Blog
  url: https://samora.ai/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.samora.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.samora.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.samora.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.samora.ai
- group: company
  title: ''
  type: Website
  url: https://samora.ai
- group: start
  title: ''
  type: SignUp
  url: https://app.samora.ai/login
- group: start
  title: ''
  type: Login
  url: https://app.samora.ai/login
- group: operate
  title: ''
  type: Support
  url: https://cal.com/team/samora/quick-chat
- group: docs
  href: https://artifacts.apis.io/samora-ai/openapi/_original/samora-ai-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/samora-ai-openapi.yml
- group: auth
  href: https://artifacts.apis.io/samora-ai/authentication/samora-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/samora-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/samora-ai/agentic-access/samora-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/samora-ai-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/samora-ai/mcp/samora-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/samora-ai-mcp.yml
- group: docs
  href: https://artifacts.apis.io/samora-ai/asyncapi/samora-ai-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/samora-ai-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/samora-ai/asyncapi/samora-ai-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/samora-ai-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/samora-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/samora-ai/conventions/samora-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/samora-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/samora-ai/errors/samora-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/samora-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/samora-ai/lifecycle/samora-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/samora-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/samora-ai/conformance/samora-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/samora-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/samora-ai/data-model/samora-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/samora-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/samora-ai/well-known/samora-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/samora-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/samora-ai/overlays/samora-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/samora-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/samora-ai/llms/samora-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/samora-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/samora-ai/security/samora-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/samora-ai-domain-security.yml
created: '2026-07-17'
description: Samora AI is a Y Combinator (W2026) company building multilingual voice agents that automate high-volume inbound and outbound calling for financial services, recruitment, healthcare, and government. Its agents handle natural conversation across 20+ languages with interruption handling, code-switching, and escalation to human operators, plus omnichannel support (voice, WhatsApp, SMS, email) and CRM integration. Samora exposes a server-to-server REST API to trigger outbound calls, manage outbound calling campaigns and their scheduled recipients, and subscribe to real-time call events through signed webhooks. Authentication is an organization API key sent in the X-API-Key header; the base URL is https://api.samora.ai and the developer documentation is at https://docs.samora.ai.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/samora-ai.png
layout: provider
modified: '2026-10-06'
name: Samora AI
nav: Providers
network: true
overview: 'Samora AI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Calls API, Campaigns API, and Webhooks API. Tagged areas include Company, Voice Agents, Conversational AI, Voice AI, and Telephony.


  The Samora AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Samora AI''s developer surface includes engineering blog, documentation, API reference, getting-started guide, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 22.3
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/samora-ai/samora-ai-2026-09-02T154344.png
security:
- kind: authentication
  name: Samora Ai Authentication
  slug: samora-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Samora Ai Domain Security
  slug: samora-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Place and track an outbound Samora AI voice call
  slug: samora-ai-outbound-call
- name: Run a Samora AI outbound calling campaign
  slug: samora-ai-run-campaign
- name: Subscribe to Samora AI call webhooks
  slug: samora-ai-subscribe-webhooks
slug: samora-ai
tags:
- Company
- Voice Agents
- Conversational AI
- Voice AI
- Telephony
- Customer Communication
- Contact Center
- Campaigns
- Webhook
website: https://samora.ai
---
