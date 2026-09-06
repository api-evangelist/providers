---
access_model:
  confidence: medium
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: D Id Agentic Access
  operation_count: 32
  slug: d-id-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 2
apis:
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: API for translating existing videos into 100+ languages using AI-driven speech translation, voice cloning, and lip-sync technology. Enables brands and content creators to localize video content at sca
  name: D-ID Translations API
  slug: d-id-translations-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: Create and manage AI agent definitions
  name: D-ID Agents API
  slug: d-id-agents-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: Send messages and receive responses in an agent chat
  name: D-ID Chat API
  slug: d-id-chat-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: Retrieve account credit balance
  name: D-ID Credits API
  slug: d-id-credits-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: Manage knowledge bases and documents for RAG
  name: D-ID Knowledge API
  slug: d-id-knowledge-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: Manage real-time streaming sessions for agents
  name: D-ID Sessions API
  slug: d-id-sessions-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: Generate AI talking-head videos (V2 Photo / V3 Pro avatars)
  name: D-ID Talks API
  slug: d-id-talks-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: Translate existing videos into 100+ languages with lip-sync
  name: D-ID Translations API
  slug: d-id-translations-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: Generate V4 Expressive full-HD avatar videos
  name: D-ID Videos V4 API
  slug: d-id-videos-v4-api
- baseURL: https://api.d-id.com
  baseurl_source: declared
  description: List available TTS voices
  name: D-ID Voices API
  slug: d-id-voices-api
artifact_total: 43
collections:
- collection_type: postman
  name: D-ID Agents API
  slug: postman-d-id-agents-api
- collection_type: postman
  name: D-ID Agents Chat API
  slug: postman-d-id-chat-api
- collection_type: postman
  name: D-ID Agents Credits API
  slug: postman-d-id-credits-api
- collection_type: postman
  name: D-ID Agents Knowledge API
  slug: postman-d-id-knowledge-api
- collection_type: postman
  name: D-ID Agents Sessions API
  slug: postman-d-id-sessions-api
- collection_type: postman
  name: D-ID Agents Talks API
  slug: postman-d-id-talks-api
- collection_type: postman
  name: D-ID Agents Translations API
  slug: postman-d-id-translations-api
- collection_type: postman
  name: D-ID Agents Videos V4 API
  slug: postman-d-id-videos-v4-api
- collection_type: postman
  name: D-ID Agents Voices API
  slug: postman-d-id-voices-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: D-ID Agents API
  slug: open-d-id-agents-api
- collection_type: open
  name: D-ID Agents Chat API
  slug: open-d-id-chat-api
- collection_type: open
  name: D-ID Agents Credits API
  slug: open-d-id-credits-api
- collection_type: open
  name: D-ID Agents Knowledge API
  slug: open-d-id-knowledge-api
- collection_type: open
  name: D-ID Agents Sessions API
  slug: open-d-id-sessions-api
- collection_type: open
  name: D-ID Agents Talks API
  slug: open-d-id-talks-api
- collection_type: open
  name: D-ID Agents Translations API
  slug: open-d-id-translations-api
- collection_type: open
  name: D-ID Agents Videos V4 API
  slug: open-d-id-videos-v4-api
- collection_type: open
  name: D-ID Agents Voices API
  slug: open-d-id-voices-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/d-id/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/d-id-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/d-id-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/d-id-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/d-id-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.d-id.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.d-id.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.d-id.com/reference/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/de-id
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deidentification
- group: other
  title: ''
  type: X
  url: https://twitter.com/D_ID_
- group: company
  title: ''
  type: Blog
  url: https://www.d-id.com/blog
- group: company
  title: ''
  type: APICategoryBlog
  url: https://www.d-id.com/blog/category/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.d-id.com/pricing/api/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.d-id.com
- group: commercial
  title: ''
  type: Plans
  url: plans/d-id-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/d-id-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/d-id-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/d-id-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/d-id-context.jsonld
created: '2026-06-12'
description: D-ID is an AI-powered platform for generating talking-head videos and interactive digital human experiences from still photos, text scripts, and audio narration. Developers can access REST APIs to produce pre-rendered talking avatar videos, perform real-time streaming agent conversations via WebRTC, translate videos into 100+ languages with voice cloning and lip-sync, and create custom AI agents backed by LLMs and RAG knowledge bases. The platform has generated over 150 million videos and supports parallel processing of tens of thousands of simultaneous API requests. D-ID serves use cases ranging from enterprise training and customer service to personalized marketing campaigns and language learning applications.
examples:
- key_count: 4
  name: D Id Create Agent Example
  slug: d-id-create-agent-example
- key_count: 4
  name: D Id Create Talk Example
  slug: d-id-create-talk-example
- key_count: 4
  name: D Id Create Translation Example
  slug: d-id-create-translation-example
finops:
- name: D Id Finops
  service_category: ''
  slug: d-id-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/d-id.png
json_schemas:
- name: D-ID Agent
  property_count: 13
  slug: d-id-agent
- name: D-ID Talk
  property_count: 15
  slug: d-id-talk
jsonld:
- class_count: 13
  name: D Id Context
  property_count: 35
  slug: d-id-context
layout: provider
modified: '2026-06-12'
name: D-ID
nav: Providers
network: true
overview: 'D-ID publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Translations API, Agents API, Chat API, and 7 more. Tagged areas include AI Video, Digital Humans, Talking Head, Avatar, and Generative AI.


  The D-ID catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  D-ID''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: D Id Plans Pricing
  plan_count: 5
  slug: d-id-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: D Id Rate Limits
  slug: d-id-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: D-ID API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: d-id-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 93.3
    catalog_earned_first_party: 0.0
    catalog_gap: 21.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 76.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/d-id/refs/heads/main/screenshots/d-id-2026-06-20T175418.png
security:
- kind: authentication
  name: D Id Authentication
  slug: d-id-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: D Id Domain Security
  slug: d-id-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: D Id Trust Center
  slug: d-id-trust-center
  summary_line: GDPR
slug: d-id
tags:
- AI Video
- Digital Humans
- Talking Head
- Avatar
- Generative AI
- Video Generation
- Real-Time Streaming
- Text-to-Video
- Video Translation
- Voice Cloning
website: https://www.d-id.com
---
