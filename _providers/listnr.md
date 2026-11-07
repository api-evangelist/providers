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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Listnr Agentic Access
  operation_count: 6
  slug: listnr-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://bff.listnr.tech/api/tts/v1
  baseurl_source: declared
  description: Discovery and authentication hints
  name: Listnr Agent API
  slug: listnr-agent-api
- baseURL: https://bff.listnr.tech/api/tts/v1
  baseurl_source: declared
  description: Published plan and credit limits
  name: Listnr Billing API
  slug: listnr-billing-api
- baseURL: https://bff.listnr.tech/api/tts/v1
  baseurl_source: declared
  description: Tools and marketing pages
  name: Listnr Catalog API
  slug: listnr-catalog-api
artifact_total: 14
collections:
- collection_type: open
  name: Listnr Text-to-Speech Jobs API
  slug: open-listnr-jobs-api
- collection_type: open
  name: Listnr Jobs Text-to-Speech API
  slug: open-listnr-text-to-speech-api
- collection_type: open
  name: Listnr Text-to-Speech Jobs Voices API
  slug: open-listnr-voices-api
- collection_type: open
  name: Listnr Text-to-Speech API
  slug: open-listnr
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://listnr.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://listnr.ai/blog
- group: agent
  href: https://artifacts.apis.io/listnr/agentic-access/listnr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/listnr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/listnr/security/listnr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/listnr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/listnr/authentication/listnr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/listnr-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/listnr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/team-listnr
- group: company
  title: ''
  type: Website
  url: https://listnr.ai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/team-listnr/text-to-speech-api
- group: start
  title: ''
  type: SignUp
  url: https://voices.listnr.tech
- group: commercial
  href: https://artifacts.apis.io/listnr/plans/listnr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/listnr-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/listnr/rate-limits/listnr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/listnr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/listnr/finops/listnr-finops.yml
  title: ''
  type: FinOps
  url: finops/listnr-finops.yml
created: '2026-07-11'
description: Listnr AI is a text-to-speech and AI voice platform offering 1,000+ ultra-realistic voices across 142+ languages and accents, used for voiceovers, podcasts, and text-to-video. Beyond the web app, Listnr exposes a documented public Text-to-Speech API (base https://bff.listnr.tech/api/tts/v1) that converts SSML text or article URLs into MP3/WAV audio synchronously or asynchronously, lists available voices, and reports async job status. API keys are generated from the Listnr dashboard at voices.listnr.tech and passed via an x-listnr-token header.
finops:
- has_sources: true
  method: generated
  name: Listnr Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: listnr-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listnr.png
layout: provider
modified: '2026-10-06'
name: Listnr
nav: Providers
network: true
overview: 'Listnr publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent API, Billing API, and Catalog API. Tagged areas include Artificial Intelligence, Text-to-Speech, Voice, Speech Synthesis, and Audio.


  The Listnr catalog on APIs.io includes 1 Spectral governance ruleset.


  Listnr''s developer surface includes pricing, engineering blog, authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Listnr Plans Pricing
  plan_count: 5
  slug: listnr-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Listnr Rate Limits
  slug: listnr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Listnr API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: listnr-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 43.4
    contract_governance: 13.6
    contract_quality: 51.5
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 42.9
      total: 7
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/listnr/listnr-2026-07-25T225328.png
security:
- kind: authentication
  name: Listnr Authentication
  slug: listnr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Listnr Domain Security
  slug: listnr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: listnr
tags:
- Artificial Intelligence
- Text-to-Speech
- Voice
- Speech Synthesis
- Audio
- Voiceover
website: https://listnr.ai
---
