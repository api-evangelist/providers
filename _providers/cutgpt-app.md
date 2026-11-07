---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
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
- description: Public developer documentation for cutGPT offering AI chat features.
  name: cutGPT API
  slug: cutgpt-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/cutgpt-app/plans/cutgpt-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cutgpt-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cutgpt-app/llms/cutgpt-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cutgpt-app-llms.txt
- group: other
  href: https://artifacts.apis.io/cutgpt-app/hosts/cutgpt-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cutgpt-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/cutgpt-app/vendors/cutgpt-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cutgpt-app-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cutgpt.app/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://cutgpt.app/guides/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cutgpt.app/tools/category/developer/
- group: auth
  href: https://artifacts.apis.io/cutgpt-app/security/cutgpt-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cutgpt-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cutgpt.app/
coverage:
  checked: '2026-11-04'
  detail: Developer docs are served as JavaScript‑rendered pages with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://cutgpt.app/guides/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: CutGPT is a free AI chat application available on iPhone, Android, and the web. It offers a ChatGPT‑like experience without subscription fees; ads fund the AI models and users can earn rewards redeemable via PayPal. The service provides a limited‑founder‑cut program and aims to democratize access to powerful language models.
image: https://cutgpt.app/static/logo.svg
layout: provider
modified: '2026-11-04'
name: cutGPT
nav: Providers
network: true
overview: 'cutGPT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Chat, Free AI, Advertising‑funded, Rewards program, and Mobile App.


  cutGPT''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Cutgpt App Plans Pricing
  plan_count: 1
  slug: cutgpt-app-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cutgpt App Domain Security
  slug: cutgpt-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cutgpt-app
tags:
- AI Chat
- Free AI
- Advertising‑funded
- Rewards program
- Mobile App
- PayPal payouts
- ChatGPT alternative
website: https://cutgpt.app/
---
