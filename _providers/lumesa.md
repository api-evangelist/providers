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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/lumesa/llms/lumesa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lumesa-llms.txt
- group: other
  href: https://artifacts.apis.io/lumesa/hosts/lumesa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lumesa-hosts.yml
- group: other
  href: https://artifacts.apis.io/lumesa/vendors/lumesa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lumesa-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.lumesa.ai/press
- group: company
  title: ''
  type: Blog
  url: https://www.lumesa.ai/blog
- group: auth
  href: https://artifacts.apis.io/lumesa/security/lumesa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lumesa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lumesa.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.lumesa.ai/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lumesa.ai/tnc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lumesa.ai/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: Landing page redirects via JavaScript, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 200
    url: https://lumesa.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Lumesa provides AI-driven virtual try‑on and fashion imagery solutions for e‑commerce brands. Their platform generates brand‑trained visual models, virtual try‑on experiences, visual analytics, retouching, background‑and‑scene swaps, and ad‑creative assets. Integrated with Shopify, PIM and DAM systems, Lumesa helps brands create infinite AI‑generated fashion visuals, streamline content creation, and enhance shopper engagement across digital channels.
image: https://static.wixstatic.com/media/6fd8ff_2f02f460f31242468d0ed49fadfca0f8%7Emv2.png/v1/fit/w_2500,h_1330,al_c/6fd8ff_2f02f460f31242468d0ed49fadfca0f8%7Emv2.png
layout: provider
modified: '2026-10-29'
name: Lumesa
nav: Providers
network: true
overview: 'Lumesa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, E-Commerce, Virtual Try-On, Fashion Tech, and Image Generation.


  Lumesa''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lumesa/lumesa-2026-11-03T135121.png
security:
- kind: domain-security
  name: Lumesa Domain Security
  slug: lumesa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lumesa
tags:
- Artificial Intelligence
- E-Commerce
- Virtual Try-On
- Fashion Tech
- Image Generation
- Company
website: https://www.lumesa.ai/
---
