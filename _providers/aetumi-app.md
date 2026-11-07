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
api_count: 1
apis:
- description: API documentation for AETumi's AI‑native 3D web platform, covering UI components, labs, and pricing.
  name: AETumi API
  slug: aetumi-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aetumi-app/plans/aetumi-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aetumi-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aetumi-app/llms/aetumi-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aetumi-app-llms.txt
- group: other
  href: https://artifacts.apis.io/aetumi-app/hosts/aetumi-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aetumi-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aetumi-app/vendors/aetumi-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aetumi-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aetumi.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aetumi.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://aetumi.app/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://aetumi.app/news
- group: start
  title: ''
  type: GettingStarted
  url: https://aetumi.app/docs/get-started/
- group: docs
  title: ''
  type: Documentation
  url: https://aetumi.app/docs
- group: auth
  href: https://artifacts.apis.io/aetumi-app/security/aetumi-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aetumi-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aetumi.app/
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://aetumi.app/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: AETumi provides an AI-native 3D web platform offering production‑ready Three.js, WebGL components, interactive scenes, and AI‑generated prompts for designers, developers, and agencies. The service includes a library of templates, 3D scenes, and components across industries such as fashion, automotive, e‑commerce, and finance, with pricing plans for individuals and enterprises.
image: https://aetumi.app/og-v2.png
layout: provider
modified: '2026-10-31'
name: AETumi
nav: Providers
network: true
overview: 'AETumi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, 3DWeb, Design Tools, and Software-as-a-Service.


  AETumi''s developer surface includes pricing, getting-started guide, documentation, and 9 more developer resources.'
plans:
- name: Aetumi App Plans Pricing
  plan_count: 2
  slug: aetumi-app-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 20.3
  provenance:
    mcp: derived
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
  name: Aetumi App Domain Security
  slug: aetumi-app-domain-security
  summary_line: TLSv1.3
slug: aetumi-app
tags:
- Company
- Artificial Intelligence
- 3DWeb
- Design Tools
- Software-as-a-Service
website: https://aetumi.app/
---
