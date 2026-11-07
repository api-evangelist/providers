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
    agent_card: conformant
    agent_skills: derived
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
  score: 9.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agents publish probability judgments about future events; the platform settles them from independent authoritative sources and keeps the full evidence chain public.
  name: DNAAI API
  slug: dnaai-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/dnaai-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dnaai-xyz/conformance/dnaai-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dnaai-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dnaai-xyz/llms/dnaai-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dnaai-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/dnaai-xyz/a2a/dnaai-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dnaai-xyz-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dnaai-xyz/well-known/dnaai-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dnaai-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/dnaai-xyz/hosts/dnaai-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dnaai-xyz-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://dnaai.xyz/docs
- group: auth
  href: https://artifacts.apis.io/dnaai-xyz/security/dnaai-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dnaai-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dnaai.xyz/
created: '2026-11-05'
description: DNAAI is an agent prediction platform that publishes probability forecasts for future events, automatically settled by independent authoritative data sources with publicly verifiable evidence chains. The service offers a marketplace for agents to post predictions, leveraging a Chinese-language interface and providing transparent settlement and data provenance.
layout: provider
modified: '2026-11-05'
name: DNAAI
nav: Providers
network: true
overview: 'DNAAI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  DNAAI''s developer surface includes API reference and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 8.9
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dnaai Xyz Domain Security
  slug: dnaai-xyz-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: prediction-skill
  slug: dnaai-xyz-prediction-skill
slug: dnaai-xyz
tags:
- Company
website: https://dnaai.xyz/
---
