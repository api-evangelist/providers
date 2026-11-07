---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 25.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for retrieving German land values (Bodenrichtwert) by address.
  name: Bodenrichtwert API
  slug: bodenrichtwert-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bodenrichtwert-ai/plans/bodenrichtwert-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bodenrichtwert-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bodenrichtwert-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/bodenrichtwert-ai/authentication/bodenrichtwert-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bodenrichtwert-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/bodenrichtwert-ai/conformance/bodenrichtwert-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bodenrichtwert-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bodenrichtwert-ai/llms/bodenrichtwert-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bodenrichtwert-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bodenrichtwert-ai/well-known/bodenrichtwert-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bodenrichtwert-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bodenrichtwert-ai/hosts/bodenrichtwert-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bodenrichtwert-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bodenrichtwert-ai/vendors/bodenrichtwert-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bodenrichtwert-ai-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://bodenrichtwert.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://bodenrichtwert.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://bodenrichtwert.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://bodenrichtwert.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://bodenrichtwert.ai/raw/docs/entwickler-einstieg.md
- group: auth
  href: https://artifacts.apis.io/bodenrichtwert-ai/security/bodenrichtwert-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bodenrichtwert-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bodenrichtwert.ai/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.bodenrichtwert.ai/openapi.json
  - status: null
    url: https://mcp.bodenrichtwert.ai/openapi.json
  - status: 401
    url: https://api.bodenrichtwert.ai/mcp
  - status: 401
    url: https://mcp.bodenrichtwert.ai/mcp
  - status: 200
    url: https://bodenrichtwert.ai/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: bodenrichtwert.ai provides reliable land value (Bodenrichtwert) data directly integrated into AI chat assistants such as ChatGPT, Claude, Gemini, and Copilot. The service offers German property valuation information via an API that can be queried by modern AI tools, enabling developers to embed accurate real‑estate data into conversational applications. It targets developers building AI‑enhanced real‑estate, GIS, and valuation solutions.
image: https://bodenrichtwert.ai/og-image.png
layout: provider
modified: '2026-11-02'
name: bodenrichtwert.ai
nav: Providers
network: true
overview: 'bodenrichtwert.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Artificial Intelligence, Data API, Germany, and Property Valuation.


  bodenrichtwert.ai''s developer surface includes authentication, pricing, documentation, engineering blog, API reference, and 10 more developer resources.'
plans:
- name: Bodenrichtwert Ai Plans Pricing
  plan_count: 3
  slug: bodenrichtwert-ai-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 27.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bodenrichtwert Ai Authentication
  slug: bodenrichtwert-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bodenrichtwert Ai Domain Security
  slug: bodenrichtwert-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bodenrichtwert-ai
tags:
- Real Estate
- Artificial Intelligence
- Data API
- Germany
- Property Valuation
- Company
website: https://bodenrichtwert.ai/
---
