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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/piestro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://piestro.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/piestro
coverage:
  checked: '2026-08-26'
  detail: Piestro was a pizza-vending-machine hardware maker, not a software vendor, and it ceased operations in January 2025 without shipping a production unit; the only publicly readable surface left is a stale Webflow marketing/crowdfunding site whose entire link graph is Overview/Team/Press/Careers/Invest, with no developer, docs or API page anywhere, and no first-party GitHub org, npm or PyPI package to fall back on.
  evidence:
  - status: 200
    url: https://piestro.webflow.io/
  - status: 404
    url: https://piestro.webflow.io/openapi.json
  - status: 404
    url: https://piestro.webflow.io/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/piestro
  - status: 403
    url: https://piestro.com/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Piestro was a Los Angeles-area food-robotics company that built a fully enclosed, automated pizza-making vending machine — an unattended kiosk that pressed, sauced, topped, baked, cut and boxed an artisanal pizza in roughly three minutes, sold both as direct-to-consumer placements and as a white-label unit for existing pizza brands. Founded by Massimo Noja De Marco and incubated by Wavemaker Labs (since rebranded Vebu Labs), it raised roughly $11.7M from equity-crowdfunding investors, largely via StartEngine, and piloted units with partners including Capriotti''s and 800 Degrees Go. Piestro shut down in January 2025 without shipping a production unit. It is a hardware and food-service company, not a software vendor: it never ran a developer program, and no public API, SDK, webhook, developer portal or machine-readable contract of any kind was ever published. This profile records that absence rather than inventing a surface.'
image: https://cdn.prod.website-files.com/5ed521e4f155f4f157f0a61a/5ed66f0f9264a6758037ab33_Piestro_3_4_Mama_Baby_Button(long%20shadow)-min.png
layout: provider
modified: '2026-08-26'
name: Piestro
nav: Providers
network: true
overview: Piestro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Automation, Food Service, and Restaurant Technology.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Piestro Domain Security
  slug: piestro-domain-security
  summary_line: TLSv1.3
slug: piestro
tags:
- Company
- Robotics
- Automation
- Food Service
- Restaurant Technology
- Vending
- Hardware
- Defunct
website: https://piestro.com/
---
