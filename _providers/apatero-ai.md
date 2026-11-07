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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Apatero AI platform.
  name: Apatero AI API
  slug: apatero-ai-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/apatero-ai/llms/apatero-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apatero-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/apatero-ai/a2a/apatero-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apatero-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/apatero-ai/well-known/apatero-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apatero-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/apatero-ai/hosts/apatero-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apatero-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/apatero-ai/packages/apatero-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/apatero-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/apatero-ai/packages/apatero-ai-packages.yml
  title: ''
  type: Packages
  url: packages/apatero-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/apatero-ai/security/apatero-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apatero-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apatero.ai/
- group: company
  title: ''
  type: Blog
  url: https://apatero.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.apatero.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.apatero.ai/privacy
coverage:
  checked: '2026-11-01'
  detail: GraphQL endpoint https://api.apatero.ai/graphql returned 403, indicating authentication is required.
  evidence:
  - status: 403
    url: https://api.apatero.ai/graphql
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Apatero is the meta‑layer over the AI generation stack, offering a creator‑grade studio that unifies image, video, audio, 3D and avatar generation across every modern model. Users can generate, edit, and manage AI‑generated media in a single workspace, with tools for prompt engineering, asset management, and collaborative workflows. The platform provides an API and MCP interface for developers to integrate AI generation capabilities into their applications.
image: https://apatero.ai/Favicon.png
layout: provider
modified: '2026-11-01'
name: Apatero
nav: Providers
network: true
overview: 'Apatero is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Image Generation, Video Generation, Audio Generation, and 3D.


  Apatero''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 12.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apatero Ai Domain Security
  slug: apatero-ai-domain-security
  summary_line: TLSv1.3
slug: apatero-ai
tags:
- Artificial Intelligence
- Image Generation
- Video Generation
- Audio Generation
- 3D
- Creator Studio
website: https://apatero.ai/
---
