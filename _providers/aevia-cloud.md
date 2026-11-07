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
- description: Aevia provides an AI companion service with import of Claude conversations and self‑hosted continuation.
  name: Aevia API
  slug: aevia-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aevia-cloud/plans/aevia-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aevia-cloud-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aevia-cloud/llms/aevia-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aevia-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/aevia-cloud/hosts/aevia-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aevia-cloud-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aevia-cloud/security/aevia-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aevia-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aevia.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://aevia.cloud/help
- group: commercial
  title: ''
  type: Pricing
  url: https://aevia.cloud/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aevia.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aevia.cloud/privacy
- group: company
  title: ''
  type: Blog
  url: https://aevia.cloud/blog
- group: operate
  title: ''
  type: Support
  url: https://aevia.cloud/help
coverage:
  checked: '2026-10-31'
  detail: Help center pages are rendered client‑side JavaScript with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://aevia.cloud/help
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Aevia provides an AI companion service that lets users import their conversation histories from Claude and continue them with a personalized AI. The platform offers features such as automatic message generation, customizable interaction schedules, and data privacy controls, with a subscription model starting at $49 per month. It emphasizes user‑owned data, no credit‑card required for a 7‑day free trial, and tools for exporting and managing AI dialogues.
image: https://aevia.cloud/og.png
layout: provider
modified: '2026-10-31'
name: Aevia
nav: Providers
network: true
overview: 'Aevia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Aevia''s developer surface includes documentation, pricing, engineering blog, support, and 7 more developer resources.'
plans:
- name: Aevia Cloud Plans Pricing
  plan_count: 1
  slug: aevia-cloud-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 18.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aevia Cloud Domain Security
  slug: aevia-cloud-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aevia-cloud
tags:
- Company
website: https://aevia.cloud/
---
