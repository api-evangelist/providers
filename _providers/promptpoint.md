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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/promptpoint/plans/promptpoint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/promptpoint-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/promptpoint/hosts/promptpoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptpoint-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptpoint/vendors/promptpoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptpoint-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.promptpoint.ai/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://www.promptpoint.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://www.promptpoint.ai/login
- group: auth
  href: https://artifacts.apis.io/promptpoint/security/promptpoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptpoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptpoint.ai/
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found at common API endpoints.
  evidence:
  - status: 0
    url: https://api.promptpoint.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: PromptPoint provides a no‑code platform that enables teams to design, test, and deploy prompt configurations for large language models at speed. Their playground lets users create and organize prompts, run automated tests, and evaluate outputs to ensure high‑quality LLM responses. With features like collaborative prompt engineering, versioning, and integration with hundreds of models, PromptPoint aims to make prompt development predictable and scalable for both technical and non‑technical users. The service offers a free tier, pricing plans for teams, and comprehensive documentation covering getting started, API reference, and best practices.
layout: provider
modified: '2026-10-18'
name: PromptPoint
nav: Providers
network: true
overview: 'PromptPoint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, No-Code, Prompt Engineering, Collaboration, and Platform.


  PromptPoint''s developer surface includes sandbox, pricing, and 6 more developer resources.'
plans:
- name: Promptpoint Plans Pricing
  plan_count: 3
  slug: promptpoint-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 15.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/promptpoint/promptpoint-2026-11-03T141613.png
security:
- kind: domain-security
  name: Promptpoint Domain Security
  slug: promptpoint-domain-security
  summary_line: TLSv1.3 · HSTS
slug: promptpoint
tags:
- Artificial Intelligence
- No-Code
- Prompt Engineering
- Collaboration
- Platform
- Company
website: https://promptpoint.ai/
---
