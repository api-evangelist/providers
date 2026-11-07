---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aige-ws/plans/aige-ws-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aige-ws-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://aige.ws/.well-known/security.txt
- group: agent
  href: https://artifacts.apis.io/aige-ws/llms/aige-ws-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aige-ws-llms.txt
- group: auth
  href: https://artifacts.apis.io/aige-ws/well-known/aige-ws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aige-ws-security.txt
- group: agent
  href: https://artifacts.apis.io/aige-ws/well-known/aige-ws-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aige-ws-well-known.yml
- group: other
  href: https://artifacts.apis.io/aige-ws/hosts/aige-ws-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aige-ws-hosts.yml
- group: other
  href: https://artifacts.apis.io/aige-ws/vendors/aige-ws-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aige-ws-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aige.ws/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aige.ws/legal/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://aige.ws/pricing/
- group: company
  title: ''
  type: Blog
  url: https://aige.ws/blog/
- group: auth
  href: https://artifacts.apis.io/aige-ws/security/aige-ws-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aige-ws-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aige-ws/security/aige-ws-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aige-ws-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aige.ws/
coverage:
  checked: '2026-11-01'
  detail: Provider's developer portal pages are heavily JavaScript rendered, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://aige.ws/developer
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AIGE provides an AI-powered image and video studio that enables creators to generate characters, films, brand designs, and marketing assets from simple text prompts. The platform offers tools for AI image generation, video creation, digital twins, and brand consistency across campaigns, with integrations for Claude, Cursor, and popular creative tools. It includes a marketplace of models, pricing plans, and a developer portal for building custom workflows.
image: https://aige.ws/og-aige.jpg
layout: provider
modified: '2026-11-01'
name: AIGE
nav: Providers
network: true
overview: 'AIGE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Image Generation, Video Generation, Branding, and Platform.


  AIGE''s developer surface includes pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Aige Ws Plans Pricing
  plan_count: 1
  slug: aige-ws-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 18.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aige Ws Domain Security
  slug: aige-ws-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aige Ws Vulnerability Disclosure
  slug: aige-ws-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aige-ws
tags:
- Artificial Intelligence
- Image Generation
- Video Generation
- Branding
- Platform
website: https://aige.ws/
---
