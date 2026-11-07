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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI music generation API providing endpoints to create songs from text, lyrics, or ideas.
  name: Aimusicgen API
  slug: aimusicgen-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aimusicgen-app/plans/aimusicgen-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aimusicgen-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aimusicgen-app/llms/aimusicgen-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimusicgen-app-llms.txt
- group: other
  href: https://artifacts.apis.io/aimusicgen-app/hosts/aimusicgen-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimusicgen-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aimusicgen-app/vendors/aimusicgen-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aimusicgen-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimusicgen.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimusicgen.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://aimusicgen.app/pricing
- group: auth
  href: https://artifacts.apis.io/aimusicgen-app/security/aimusicgen-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimusicgen-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aimusicgen.app/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec could be found on the API host.
  evidence:
  - status: 0
    url: https://api.aimusicgen.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Aimusicgen provides a free AI-powered music generation service that transforms text descriptions, lyrics, or ideas into fully produced songs with vocals or instrumentals. Users can select styles, customize arrangements, and download the generated tracks. The platform offers tools such as AI Song Cover, Lyrics Generator, and AI Music Maker, catering to creators, marketers, and developers seeking quick audio content. Aimusicgen operates as a SaaS solution with a free tier and paid plans for higher credit usage.
image: https://aimusicgen.app/og-music.png
layout: provider
modified: '2026-11-01'
name: Aimusicgen
nav: Providers
network: true
overview: 'Aimusicgen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Music, Software-as-a-Service, Generation, and Free.


  Aimusicgen''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Aimusicgen App Plans Pricing
  plan_count: 4
  slug: aimusicgen-app-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aimusicgen App Domain Security
  slug: aimusicgen-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: aimusicgen-app
tags:
- Artificial Intelligence
- Music
- Software-as-a-Service
- Generation
- Free
website: https://aimusicgen.app/
---
