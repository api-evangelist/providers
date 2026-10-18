---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://prologue.ai/plans
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/prologue/refs/heads/main/plans/prologue-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prologue-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://prologue.ai/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/prologue/refs/heads/main/security/prologue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prologue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prologue.ai/
created: '2026-07-17'
description: Prologue (Prologue AI) is a multimodal creative operating system that lets teams create, edit, and organize AI-generated images, video, audio, and text in a single workspace. Powered by "Prologue Intent" and a best-in-class catalog of third-party generative models, it targets professional creative workflows for agencies and brands ("crafted, not generated"). It was surfaced as an a16z portfolio company and added to the API Evangelist network as a stub for enrichment. As of this pass no public developer API, documentation, or SDK surface was discoverable — the product site is a consumer/pro web application behind bot protection.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prologue.png
layout: provider
modified: '2026-10-06'
name: Prologue
nav: Providers
network: true
overview: 'Prologue is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Generative AI, Creative Tools, and Content Creation.


  Prologue''s developer surface includes pricing, engineering blog, and 3 more developer resources.'
plans:
- name: Prologue Plans Pricing
  plan_count: 6
  slug: prologue-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.6
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/prologue/refs/heads/main/screenshots/prologue-2026-10-11T112827.png
security:
- kind: domain-security
  name: Prologue Domain Security
  slug: prologue-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: prologue
tags:
- Company
- Artificial Intelligence
- Generative AI
- Creative Tools
- Content Creation
- Multi-Modal
- Media
website: https://prologue.ai/
---
