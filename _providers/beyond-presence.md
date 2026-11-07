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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.bey.dev
  baseurl_source: declared
  description: The Agents API from Beyond Presence — 2 operation(s) for agents.
  name: Beyond Presence Agents API
  slug: beyond-presence-agents-api
- baseURL: https://api.bey.dev
  baseurl_source: declared
  description: The Authentication API from Beyond Presence — 1 operation(s) for authentication.
  name: Beyond Presence Authentication API
  slug: beyond-presence-authentication-api
- baseURL: https://api.bey.dev
  baseurl_source: declared
  description: The Avatars API from Beyond Presence — 2 operation(s) for avatars.
  name: Beyond Presence Avatars API
  slug: beyond-presence-avatars-api
- baseURL: https://api.bey.dev
  baseurl_source: declared
  description: Retrieve information about the conversations your Managed Agents have had, including their status, participants, and transcripts.
  name: Beyond Presence Agent Conversations API
  slug: beyond-presence-agent-conversations-api
- baseURL: https://api.bey.dev
  baseurl_source: declared
  description: Primitives for embedding a Managed Agent in your own application with advanced cusotmization. **Most integrations do not need these.**
  name: Beyond Presence Agent Integration API
  slug: beyond-presence-agent-integration-api
- baseURL: https://api.bey.dev
  baseurl_source: declared
  description: Manage the knowledge base documents your Managed Agents can draw on during a conversation.
  name: Beyond Presence Agent Knowledge Files API
  slug: beyond-presence-agent-knowledge-files-api
- baseURL: https://api.bey.dev
  baseurl_source: declared
  description: Store credentials for external services, such as an OpenAI-compatible LLM, so Managed Agents can reference them by ID.
  name: Beyond Presence Agents External APIs API
  slug: beyond-presence-agents-external-apis-api
- baseURL: https://api.bey.dev
  baseurl_source: declared
  description: Attach an avatar to a voice agent you build and run yourself. Prefer using the [LiveKit Plugin](https://docs.bey.dev/integrations/voice-agents/livekit) over calling these endpoints directly.
  name: Beyond Presence Speech-to-Video Sessions API
  slug: beyond-presence-speech-to-video-sessions-api
artifact_total: 32
asyncapis:
- description: ''
  name: Beyond Presence Webhooks
  slug: beyond-presence-webhooks
collections:
- collection_type: postman
  name: Fast Agents API
  slug: postman-beyond-presence-agents-api
- collection_type: postman
  name: Fast Agents Authentication API
  slug: postman-beyond-presence-authentication-api
- collection_type: postman
  name: Fast Agents Avatars API
  slug: postman-beyond-presence-avatars-api
- collection_type: postman
  name: Fast Agents Calls API
  slug: postman-beyond-presence-calls-api
- collection_type: postman
  name: Fast Agents External APIs API
  slug: postman-beyond-presence-external-apis-api
- collection_type: postman
  name: Fast Agents Knowledge Files API
  slug: postman-beyond-presence-knowledge-files-api
- collection_type: postman
  name: Fast Agents Sessions API
  slug: postman-beyond-presence-sessions-api
- collection_type: open
  name: Fast Agents API
  slug: open-beyond-presence-agents-api
- collection_type: open
  name: Fast Agents Authentication API
  slug: open-beyond-presence-authentication-api
- collection_type: open
  name: Fast Agents Avatars API
  slug: open-beyond-presence-avatars-api
- collection_type: open
  name: Fast Agents Calls API
  slug: open-beyond-presence-calls-api
- collection_type: open
  name: Fast Agents External APIs API
  slug: open-beyond-presence-external-apis-api
- collection_type: open
  name: Fast Agents Knowledge Files API
  slug: open-beyond-presence-knowledge-files-api
- collection_type: open
  name: Fast Agents Sessions API
  slug: open-beyond-presence-sessions-api
common:
- group: other
  href: https://artifacts.apis.io/beyond-presence/capabilities/beyond-presence-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/beyond-presence-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/beyond-presence/plans/beyond-presence-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beyond-presence-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://bey.dev
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/beyond-presence/overview
- group: other
  href: https://artifacts.apis.io/beyond-presence/a2a/beyond-presence-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/beyond-presence-a2a.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bey.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bey.dev/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bey.dev/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bey.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://beyondpresence.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://beyondpresence.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.bey.chat/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beyondpresence.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beyondpresence.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/A3JTzk5aWa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bey-dev
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.bey.dev/learn/roadmap
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bey.dev/
- group: operate
  href: https://artifacts.apis.io/beyond-presence/changelog/beyond-presence-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beyond-presence-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bey.dev/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bey.dev/
- group: agent
  href: https://artifacts.apis.io/beyond-presence/llms/beyond-presence-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beyond-presence-llms.txt
- group: build
  href: https://artifacts.apis.io/beyond-presence/packages/beyond-presence-packages.yml
  title: ''
  type: Packages
  url: packages/beyond-presence-packages.yml
- group: build
  href: https://artifacts.apis.io/beyond-presence/packages/beyond-presence-packages.yml
  title: ''
  type: SDKs
  url: packages/beyond-presence-packages.yml
- group: agent
  href: https://artifacts.apis.io/beyond-presence/mcp/beyond-presence-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/beyond-presence-mcp.yml
- group: auth
  href: https://artifacts.apis.io/beyond-presence/authentication/beyond-presence-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beyond-presence-authentication.yml
- group: design
  href: https://artifacts.apis.io/beyond-presence/conventions/beyond-presence-conventions.yml
  title: ''
  type: Conventions
  url: conventions/beyond-presence-conventions.yml
- group: design
  href: https://artifacts.apis.io/beyond-presence/errors/beyond-presence-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beyond-presence-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beyond-presence/lifecycle/beyond-presence-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/beyond-presence-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/beyond-presence/conformance/beyond-presence-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beyond-presence-conformance.yml
- group: design
  href: https://artifacts.apis.io/beyond-presence/data-model/beyond-presence-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beyond-presence-data-model.yml
- group: design
  href: https://artifacts.apis.io/beyond-presence/components/beyond-presence-components.yml
  title: ''
  type: Components
  url: components/beyond-presence-components.yml
- group: auth
  href: https://artifacts.apis.io/beyond-presence/security/beyond-presence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beyond-presence-domain-security.yml
- group: other
  href: https://artifacts.apis.io/beyond-presence/overlays/beyond-presence-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beyond-presence-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/beyond-presence/asyncapi/beyond-presence-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/beyond-presence-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/beyond-presence/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Beyond Presence (brand "bey") is a Europe-based AI company building real-time conversational AI video agents and speech-to-video (S2V) technology. Its platform lets developers deploy hyper-realistic AI video avatars that respond in real time (sub-1.2s latency at up to 1080p) across HR, sales, support, and coaching use cases. Two products are exposed through one REST API at api.bey.dev: a Speech-to-Video API that turns audio streams into lifelike avatars over LiveKit, and a Managed Agents API that runs end-to-end conversational agents with knowledge files, external LLM/API configuration, and webhook events. Official Python and TypeScript SDKs, an OpenAPI spec, and GDPR / SOC 2 Type II compliance are published. Surfaced as an HV Capital portfolio company and enriched from its public developer surface.'
finops:
- has_sources: true
  method: derived
  name: Beyond Presence Finops
  primary_unit: 2k credits/month
  service_category: ''
  slug: beyond-presence-finops
  template: false
image: https://beyondpresence.ai/favicon.ico
layout: provider
modified: '2026-09-16'
name: Beyond Presence
nav: Providers
network: true
overview: 'Beyond Presence publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Authentication API, Avatars API, and 5 more. Tagged areas include Company, Ai Enterprise Software, Artificial Intelligence, Avatars, and Video.


  The Beyond Presence catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Beyond Presence''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 29 more developer resources.'
plans:
- name: Beyond Presence Plans Pricing
  plan_count: 5
  slug: beyond-presence-plans-pricing
- name: Beyond Presence Price Estimates
  plan_count: 0
  slug: beyond-presence-price-estimates
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Beyond Presence API Rules
  rule_count: 59
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 7
  slug: beyond-presence-rules
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 65.0
    developer_ergonomics: 67.3
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 63.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/beyond-presence/beyond-presence-2026-07-25T202842.png
security:
- kind: authentication
  name: Beyond Presence Authentication
  slug: beyond-presence-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Beyond Presence Domain Security
  slug: beyond-presence-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Beyond Presence Trust Center
  slug: beyond-presence-trust-center
  summary_line: SOC 2 Type II, GDPR
skill_count: 2
skills:
- name: Ground an agent with a knowledge file
  slug: beyond-presence-ground-agent-with-knowledge
- name: Create an agent and launch a call
  slug: beyond-presence-launch-agent-call
slug: beyond-presence
tags:
- Company
- Ai Enterprise Software
- Artificial Intelligence
- Avatars
- Video
- Conversational AI
- Agents
- Speech To Video
- Real-Time Communication
- A2A
website: https://bey.dev
---
