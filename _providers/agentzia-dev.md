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
- description: Agentzia provides a Generative Engine Optimization (GEO) platform with a browser‑based MCP for secure credential‑free integration and various tools for AI‑driven product recommendation testing.
  name: Agentzia MCP API
  slug: agentzia-mcp-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/agentzia-dev/plans/agentzia-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentzia-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agentzia-dev/llms/agentzia-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentzia-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentzia-dev/hosts/agentzia-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentzia-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentzia-dev/vendors/agentzia-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentzia-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentzia.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentzia.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentzia.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://www.agentzia.dev/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentzia.dev/docs
- group: auth
  href: https://artifacts.apis.io/agentzia-dev/security/agentzia-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentzia-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentzia.dev/
coverage:
  checked: '2026-11-01'
  detail: Documentation is public HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.agentzia.dev/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agentzia provides a Generative Engine Optimization (GEO) platform that tests how AI agents like ChatGPT, Claude, Gemini, and Grok perceive and recommend products. Users can simulate AI interactions, generate sample reports, and receive actionable insights to improve website content for better AI-driven recommendations. The service includes a browser‑based MCP for secure credential‑free integration, various pricing plans, and extensive documentation covering methodology, data handling, and acceptable use.
image: https://www.agentzia.dev/opengraph-image
layout: provider
modified: '2026-11-01'
name: Morphologic AI Inc.
nav: Providers
network: true
overview: 'Morphologic AI Inc. is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Geo, Product Testing, Generative AI, and Analytics.


  Morphologic AI Inc.''s developer surface includes pricing, documentation, and 9 more developer resources.'
plans:
- name: Agentzia Dev Plans Pricing
  plan_count: 1
  slug: agentzia-dev-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 20.4
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
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
  name: Agentzia Dev Domain Security
  slug: agentzia-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentzia-dev
tags:
- Artificial Intelligence
- Geo
- Product Testing
- Generative AI
- Analytics
- Company
website: https://agentzia.dev/
---
