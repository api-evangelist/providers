---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Audio tools API providing free and paid endpoints for audio processing.
  name: Audo API
  slug: audo-api
- baseURL: https://audo.ai
  baseurl_source: declared
  description: 'Audio tools for people and agents: remove noise, enhance voices, transcribe, align a script, cut, remove silence, set loudness, convert, join, swap a video''s audio, change speed and pitch, reverse, mu'
  name: Audo API API
  slug: audo-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/audo-ai/rules/audo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/audo-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/audo-ai/vocabulary/audo-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/audo-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/audo-ai/conventions/audo-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/audo-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/audo-ai/conventions/audo-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/audo-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/audo-ai/conformance/audo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audo-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/audo-ai/vendors/audo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audo-ai-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/audo-ai/plans/audo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/audo-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/audo-ai/errors/audo-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audo-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/audo-ai/llms/audo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audo-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/audo-ai/well-known/audo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audo-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/audo-ai/hosts/audo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audo-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://audo.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://audo.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audo.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/audo-ai
- group: company
  title: ''
  type: Blog
  url: https://audo.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.audo.ai/
- group: auth
  href: https://artifacts.apis.io/audo-ai/security/audo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://audo.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://audo.ai/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://audo.ai/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://audo.ai/developers
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://audo.ai/mcp
  - status: 403
    url: https://app.audo.ai/mcp
  - status: 200
    url: https://audo.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Audo provides AI-powered audio and video enhancement tools, offering noise removal, echo reduction, voice recording, screen recording, transcription, and various editing features. The platform processes over 10 million files since 2021 and offers a free tier with limited usage, as well as pay‑as‑you‑go pricing for higher volumes. It targets developers via an API for integration into apps, as well as end‑users through a web interface. Audo emphasizes privacy, deleting uploaded files after processing, and supports a wide range of audio and video formats up to 10 GB.
image: https://audo.ai/opengraph-image-12o0cb?a196f0b233256eeb
layout: provider
modified: '2026-11-02'
name: Audo
nav: Providers
network: true
overview: 'Audo publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, Artificial Intelligence, Audio, Video, and Tools.


  The Audo catalog on APIs.io includes 1 Spectral governance ruleset.


  Audo''s developer surface includes support, engineering blog, getting-started guide, documentation, API reference, pricing, and 17 more developer resources.'
plans:
- name: Audo Ai Plans Pricing
  plan_count: 6
  slug: audo-ai-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Audo API Rules
  rule_count: 46
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 4
  slug: audo-ai-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 38.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Audo Ai Domain Security
  slug: audo-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: audo-ai
tags:
- Company
- Artificial Intelligence
- Audio
- Video
- Tools
website: https://audo.ai/
---
