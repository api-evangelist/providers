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
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aeviamodeler-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aeviamodeler-ai/well-known/aeviamodeler-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aeviamodeler-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aeviamodeler-ai/hosts/aeviamodeler-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aeviamodeler-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aeviamodeler-ai/security/aeviamodeler-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeviamodeler-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aeviamodeler.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aeviamodeler.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeviamodeler.ai/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://aeviamodeler.ai/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: Aevia provides an AI‑powered assistant for life‑cycle assessment (LCA), enabling users to search LCA literature and databases, build product system models, and run impact assessments. The platform integrates with tools like openLCA and generative AI assistants such as Claude and ChatGPT, offering connectors for data import and export. Aevia offers a free Demo plan with usage credits and optional paid plans for expanded features.
layout: provider
modified: '2026-10-31'
name: Aevia
nav: Providers
network: true
overview: Aevia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Life Cycle Assessment, Sustainability, and Environmental.
random_paper: 21
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 10.4
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeviamodeler Ai Domain Security
  slug: aeviamodeler-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aeviamodeler-ai
tags:
- Company
- Artificial Intelligence
- Life Cycle Assessment
- Sustainability
- Environmental
website: https://aeviamodeler.ai/
---
