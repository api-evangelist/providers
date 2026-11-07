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
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/contendeo-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/contendeo-app/well-known/contendeo-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contendeo-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/contendeo-app/hosts/contendeo-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contendeo-app-hosts.yml
- group: auth
  href: https://artifacts.apis.io/contendeo-app/security/contendeo-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contendeo-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contendeo.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://contendeo.app/demo
- group: commercial
  title: ''
  type: Pricing
  url: https://contendeo.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contendeo.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contendeo.app/privacy
created: '2026-11-04'
description: Contendeo provides AI-powered video comprehension for Claude, turning video URLs into structured context with transcript, vision, OCR, and chart extraction. It supports YouTube, Instagram, Vimeo, Twitter/X, TikTok, and direct MP4 URLs, offering tools like quick_transcribe, deep_analyze, clip_context, and batch_analyze with credit‑based pricing. Users connect via a custom Claude connector and benefit from free cache hits, auto‑refunds on failures, and scalable credit plans.
image: https://contendeo.app/og-card.png
layout: provider
modified: '2026-11-04'
name: Contendeo
nav: Providers
network: true
overview: 'Contendeo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Video, Claude, and Multi-Modal.


  Contendeo''s developer surface includes getting-started guide, pricing, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contendeo App Domain Security
  slug: contendeo-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contendeo-app
tags:
- Artificial Intelligence
- Video
- Claude
- Multi-Modal
website: https://contendeo.app/
---
