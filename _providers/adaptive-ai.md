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
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/adaptive-ai/plans/adaptive-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adaptive-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adaptive-ai/llms/adaptive-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adaptive-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/adaptive-ai/hosts/adaptive-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adaptive-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adaptive-ai/vendors/adaptive-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adaptive-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adaptive.ai/
- group: auth
  href: https://artifacts.apis.io/adaptive-ai/security/adaptive-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adaptive-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adaptive.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://adaptive.ai/about.md
- group: company
  title: ''
  type: Blog
  url: https://adaptive.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adaptive.ai/pricing
- group: build
  title: ''
  type: Integration
  url: https://adaptive.ai/integrations
- group: start
  title: ''
  type: GettingStarted
  url: https://adaptive.ai/start?flow=onboarding
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adaptive.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adaptive.ai/legal/privacy
coverage:
  checked: '2026-10-31'
  detail: No machine‑readable API contract found; attempts to fetch OpenAPI at known paths on api.adaptive.ai all returned 404.
  evidence:
  - status: 404
    url: https://api.adaptive.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Adaptive is an AI agent platform that lets individuals and teams automate workflows, build full applications, and run AI‑powered operations using plain‑language prompts. Users can connect tools like Gmail, Slack, Google Sheets, and Calendar, then describe outcomes to generate and deploy end‑to‑end solutions, from support inbox handling to custom dashboards and content creation.
image: https://static.acflare.com/thumbnail-e89a-0c4b.png
layout: provider
modified: '2026-10-31'
name: Adaptive
nav: Providers
network: true
overview: 'Adaptive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Business Automation, Workflow Automation, Software-as-a-Service, and Integration.


  Adaptive''s developer surface includes documentation, engineering blog, pricing, getting-started guide, and 10 more developer resources.'
plans:
- name: Adaptive Ai Plans Pricing
  plan_count: 3
  slug: adaptive-ai-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 24.1
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
  name: Adaptive Ai Domain Security
  slug: adaptive-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: adaptive-ai
tags:
- AI Agents
- Business Automation
- Workflow Automation
- Software-as-a-Service
- Integration
- Enterprise Security
website: https://adaptive.ai/
---
