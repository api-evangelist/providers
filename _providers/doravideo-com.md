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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/doravideo-com/plans/doravideo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doravideo-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/doravideo-com/llms/doravideo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doravideo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/doravideo-com/well-known/doravideo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doravideo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/doravideo-com/hosts/doravideo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doravideo-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://doravideo.com/terms
- group: operate
  title: ''
  type: Support
  url: https://doravideo.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://doravideo.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://doravideo.com/pricing
- group: start
  title: ''
  type: Login
  url: https://doravideo.com/login
- group: company
  title: ''
  type: Blog
  url: https://doravideo.com/blog
- group: auth
  href: https://artifacts.apis.io/doravideo-com/security/doravideo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doravideo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://doravideo.com/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's API host or documentation pages.
  evidence:
  - status: 0
    url: https://api.doravideo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Saga Labs offers Dora, an AI video generation platform that turns text, images, or motion inputs into shareable videos. The service runs on the web, iOS, and integrates with AI assistants like Claude, ChatGPT, and Google Antigravity. It provides multiple AI models for video, image, and audio creation, with subscription plans detailed on its pricing page.
layout: provider
modified: '2026-11-05'
name: Saga Labs
nav: Providers
network: true
overview: 'Saga Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Video, Generation, Platform, and Software-as-a-Service.


  Saga Labs'' developer surface includes support, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Doravideo Com Plans Pricing
  plan_count: 1
  slug: doravideo-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doravideo Com Domain Security
  slug: doravideo-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doravideo-com
tags:
- Artificial Intelligence
- Video
- Generation
- Platform
- Software-as-a-Service
website: https://doravideo.com/
---
