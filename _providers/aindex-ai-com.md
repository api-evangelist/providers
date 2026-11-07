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
    mcp_server: false
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
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/aindex-ai-com/conformance/aindex-ai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aindex-ai-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aindex-ai-com/well-known/aindex-ai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aindex-ai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aindex-ai-com/hosts/aindex-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aindex-ai-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://aindex-ai.com/login
- group: auth
  href: https://artifacts.apis.io/aindex-ai-com/security/aindex-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aindex-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aindex-ai.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://aindex-ai.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: AI Index Network provides infrastructure that connects businesses, sites and e‑commerces to AI engines such as ChatGPT, Gemini, Claude and Perplexity. It ensures these models accurately cite and answer questions about a company’s offerings, lowering token costs by up to 95% while eliminating hallucinations. The platform indexes website content, offers free and paid plans, and continuously refreshes data to keep AI responses up‑to‑date.
layout: provider
modified: '2026-11-01'
name: AI Index Network
nav: Providers
network: true
overview: AI Index Network is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Indexing, Search, LowCost, and NoHallucination.
random_paper: 20
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 8.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aindex Ai Com Domain Security
  slug: aindex-ai-com-domain-security
  summary_line: TLSv1.3
slug: aindex-ai-com
tags:
- Artificial Intelligence
- Indexing
- Search
- LowCost
- NoHallucination
website: https://aindex-ai.com/
---
