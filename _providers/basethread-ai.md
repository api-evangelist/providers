---
access_model:
  confidence: low
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
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
  href: https://artifacts.apis.io/basethread-ai/plans/basethread-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/basethread-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/basethread-ai/llms/basethread-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basethread-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/basethread-ai/well-known/basethread-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/basethread-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/basethread-ai/hosts/basethread-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basethread-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/basethread-ai/vendors/basethread-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/basethread-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://basethread.ai/security
- group: auth
  href: https://artifacts.apis.io/basethread-ai/security/basethread-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basethread-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://basethread.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://basethread.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://basethread.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://basethread.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://basethread.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://basethread.ai/contact
coverage:
  checked: '2026-11-02'
  detail: The provider's website offers information but does not publish any OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://basethread.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BaseThread provides a shared context platform for AI tools used by teams, enabling saved prompts, clipboard history, and markdown notes across macOS applications. It integrates with major AI assistants like Claude, Cursor, and ChatGPT, allowing automatic read/write of decisions, activity, and tasks. The service offers a free beta with no credit card required and scales with per-seat pricing for larger teams. Features include product integrations, engineering and design solutions, and comprehensive security and privacy controls.
image: https://basethread.ai/og-default.jpg
layout: provider
modified: '2026-11-02'
name: BaseThread
nav: Providers
network: true
overview: 'BaseThread is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Collaboration, Productivity, and Teamware.


  BaseThread''s developer surface includes pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: Basethread Ai Plans Pricing
  plan_count: 3
  slug: basethread-ai-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Basethread Ai Domain Security
  slug: basethread-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: basethread-ai
tags:
- Company
- Artificial Intelligence
- Collaboration
- Productivity
- Teamware
- Software-as-a-Service
website: https://basethread.ai/
---
