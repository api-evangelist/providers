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
- description: AINPCEngine offers a REST and WebSocket API for AI‑powered NPCs, documented at the developer portal.
  name: AINPCEngine API
  slug: ainpcengine-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/ainpcengine-com/plans/ainpcengine-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ainpcengine-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ainpcengine-com/llms/ainpcengine-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ainpcengine-com-llms.txt
- group: other
  href: https://artifacts.apis.io/ainpcengine-com/hosts/ainpcengine-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ainpcengine-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/ainpcengine-com/packages/ainpcengine-com-packages.yml
  title: ''
  type: SDKs
  url: packages/ainpcengine-com-packages.yml
- group: build
  href: https://artifacts.apis.io/ainpcengine-com/packages/ainpcengine-com-packages.yml
  title: ''
  type: Packages
  url: packages/ainpcengine-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ainpcengine.com/
- group: start
  title: ''
  type: Login
  url: https://ainpcengine.com/auth/login
- group: auth
  href: https://artifacts.apis.io/ainpcengine-com/security/ainpcengine-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ainpcengine-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ainpcengine.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ainpcengine.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://ainpcengine.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ainpcengine.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://ainpcengine.com/docs/quickstart.html
- group: commercial
  title: ''
  type: Pricing
  url: https://ainpcengine.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ainpcengine.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ainpcengine.com/privacy
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://ainpcengine.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AINPCEngine provides AI‑powered non‑player characters (NPCs) for game studios, offering persistent memory, dynamic personalities, and multi‑agent intelligence via a REST and WebSocket API. The platform supports Unity, Unreal, and Godot, delivering drop‑in integration, scalable pricing, and tools such as demos, documentation, and a developer portal. It aims to enhance game immersion with smarter, evolving characters while reducing development costs.
image: https://prodmedia.tyga.host/public/tyga.cloud/landing/ainpcengine.com/ainpcengine-og-image.jpg
layout: provider
modified: '2026-11-01'
name: AINPCEngine
nav: Providers
network: true
overview: 'AINPCEngine is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Gaming, and NPC.


  AINPCEngine''s developer surface includes documentation, API reference, getting-started guide, pricing, and 12 more developer resources.'
plans:
- name: Ainpcengine Com Plans Pricing
  plan_count: 6
  slug: ainpcengine-com-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 31.7
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ainpcengine Com Domain Security
  slug: ainpcengine-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ainpcengine-com
tags:
- Company
- Artificial Intelligence
- Gaming
- NPC
website: https://ainpcengine.com/
---
