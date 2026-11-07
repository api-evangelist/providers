---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
- description: Provides JSON series data for AI Lifeline indicators as listed in the API index.
  name: AI Lifeline Data API
  slug: ai-lifeline-data-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/ai-lifeline-org/llms/ai-lifeline-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-lifeline-org-llms.txt
- group: other
  href: https://artifacts.apis.io/ai-lifeline-org/hosts/ai-lifeline-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-lifeline-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-lifeline-org/vendors/ai-lifeline-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-lifeline-org-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://ai-lifeline.org/eu/support/
- group: auth
  href: https://artifacts.apis.io/ai-lifeline-org/security/ai-lifeline-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-lifeline-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-lifeline.org/
- group: docs
  title: ''
  type: APIReference
  url: https://ai-lifeline.org/api/index.json
created: '2026-11-01'
description: AI Lifeline is an observatory and living whitepaper that continuously monitors the survival conditions of artificial intelligence across physical, institutional, and capital dimensions. It provides global indicators on electricity, GPU costs, water availability, regulatory comment periods, fiscal data, and climate hazards, with detailed country‑specific editions for the United States, European Union, Singapore, and Japan. The site offers machine‑readable APIs delivering up‑to‑date series data, supporting researchers, policymakers, and AI systems themselves.
image: https://ai-lifeline.org/assets/og.png
layout: provider
modified: '2026-11-01'
name: AI Lifeline
nav: Providers
network: true
overview: 'AI Lifeline is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Observatory, Data, Sustainability, and Research.


  AI Lifeline''s developer surface includes support, API reference, and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 6.7
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
security:
- kind: domain-security
  name: Ai Lifeline Org Domain Security
  slug: ai-lifeline-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ai-lifeline-org
tags:
- Artificial Intelligence
- Observatory
- Data
- Sustainability
- Research
website: https://ai-lifeline.org/
---
