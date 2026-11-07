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
  href: https://artifacts.apis.io/bordet-ai/plans/bordet-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bordet-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bordet-ai/llms/bordet-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bordet-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bordet-ai/well-known/bordet-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bordet-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bordet-ai/hosts/bordet-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bordet-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bordet-ai/vendors/bordet-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bordet-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bordet.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bordet.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bordet.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.bordet.ai/blog
- group: auth
  href: https://artifacts.apis.io/bordet-ai/security/bordet-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bordet-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bordet.ai/
coverage:
  checked: '2026-11-03'
  detail: The provider's website offers no public API documentation or machine‑readable contracts.
  evidence:
  - status: 200
    url: https://www.bordet.ai/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Bordet provides a multi‑LLM boardroom platform where multiple AI models such as Claude, GPT, Gemini and Grok collaborate with users in shared rooms. It offers persistent shared memory, an auditable decisions log, and flexible pricing with free starter access and prepaid credit packs. The service emphasizes data privacy, model‑agnostic integration, and team collaboration, targeting AI‑enhanced business workflows.
image: https://www.bordet.ai/opengraph-image?a488e76e6bca0151
layout: provider
modified: '2026-11-02'
name: Bordet
nav: Providers
network: true
overview: 'Bordet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Collaboration, Multi-LLM, Boardroom, and Productivity.


  Bordet''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Bordet Ai Plans Pricing
  plan_count: 5
  slug: bordet-ai-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
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
  name: Bordet Ai Domain Security
  slug: bordet-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bordet-ai
tags:
- Artificial Intelligence
- Collaboration
- Multi-LLM
- Boardroom
- Productivity
- Company
website: https://bordet.ai/
---
