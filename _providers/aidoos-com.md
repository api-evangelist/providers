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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/aidoos-com/plans/aidoos-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidoos-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aidoos-com/llms/aidoos-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidoos-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aidoos-com/well-known/aidoos-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aidoos-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aidoos-com/hosts/aidoos-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aidoos-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://aidoos.com/auth/login/
- group: auth
  href: https://artifacts.apis.io/aidoos-com/security/aidoos-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidoos-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aidoos.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://aidoos.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://aidoos.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aidoos.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aidoos.com/privacy/
coverage:
  checked: '2026-11-01'
  detail: The provider's website offers documentation but no machine‑readable API contract such as OpenAPI, GraphQL SDL, or AsyncAPI.
  evidence:
  - status: 200
    url: https://aidoos.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AiDOOS provides outcome-based delivery through Virtual Delivery Centers (VDCs), enabling enterprises to outsource and manage complex projects with a focus on results, flexibility, and scalability. The platform offers tools for building, managing, and optimizing VDCs, along with resources, case studies, and pricing options for various industries.
image: https://aidoos.com/static/ai_new_site/images/aidoos-home-page.jpeg
layout: provider
modified: '2026-11-01'
name: AiDOOS
nav: Providers
network: true
overview: 'AiDOOS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, VirtualDelivery, Outsourcing, Enterprise, and Platform.


  AiDOOS''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Aidoos Com Plans Pricing
  plan_count: 2
  slug: aidoos-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 18.3
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
  name: Aidoos Com Domain Security
  slug: aidoos-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aidoos-com
tags:
- Company
- VirtualDelivery
- Outsourcing
- Enterprise
- Platform
website: https://aidoos.com/
---
