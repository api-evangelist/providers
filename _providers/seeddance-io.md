---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Use the SeedVideo AI API to create video tasks, track their status, and check your available credits.
  name: SeedVideo AI
  slug: seedvideo-ai
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/seeddance-io/plans/seeddance-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/seeddance-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/seeddance-io/changelog/seeddance-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/seeddance-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/seeddance-io/authentication/seeddance-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/seeddance-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/seeddance-io/conformance/seeddance-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seeddance-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/seeddance-io/llms/seeddance-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seeddance-io-llms.txt
- group: other
  href: https://artifacts.apis.io/seeddance-io/hosts/seeddance-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seeddance-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/seeddance-io/vendors/seeddance-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seeddance-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seeddance.io/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.seeddance.io/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seeddance.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.seeddance.io/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.seeddance.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.seeddance.io/blog
- group: auth
  href: https://artifacts.apis.io/seeddance-io/security/seeddance-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seeddance-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seeddance.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.seeddance.io/docs
created: '2026-11-04'
description: SeedVideo AI provides all‑in‑one access to Seedance, Veo, Kling and other top‑tier video models. The platform enables developers to create production‑ready videos from text, images or video in seconds via a REST API, offering generation, upscaling, and model selection capabilities for AI‑driven video creation.
image: https://www.seeddance.io/uploads/a27d29e09f0572ad727363ef49ac2fca.png
layout: provider
modified: '2026-11-04'
name: SeedVideo AI
nav: Providers
network: true
overview: 'SeedVideo AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Video Generation, Video Generation, Image-to-Video, and Creative Tools.


  SeedVideo AI''s developer surface includes changelog, authentication, support, pricing, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Seeddance Io Plans Pricing
  plan_count: 3
  slug: seeddance-io-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Seeddance Io Authentication
  slug: seeddance-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Seeddance Io Domain Security
  slug: seeddance-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seeddance-io
tags:
- AI Video Generation
- Video Generation
- Image-to-Video
- Creative Tools
website: https://www.seeddance.io
---
