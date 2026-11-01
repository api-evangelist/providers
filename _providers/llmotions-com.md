---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 122
  human_in_the_loop: 0
  name: Llmotions Com Agentic Access
  operation_count: 164
  slug: llmotions-com-agentic-access
  summary_line: 164 operations · 122 acting
api_count: 1
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/llmotions-com/hosts/llmotions-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmotions-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/llmotions-com/vendors/llmotions-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llmotions-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/llmotions-com/security/llmotions-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmotions-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmotions.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://llmotions.com/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: LLMotions is a technology company that provides AI‑powered motion graphics tools, enabling users to generate animated content from natural language descriptions. Their platform includes products like Cympho, Cymphony, and ncode, offering real‑time previews, cloud collaboration, and export to multiple formats. LLMotions aims to democratize motion creation for creators, developers, and enterprises, delivering intuitive interfaces and advanced physics simulations.
jsonld:
- class_count: 18
  name: Llmotions Com Context
  property_count: 65
  slug: llmotions-com-context
layout: provider
modified: '2026-10-29'
name: llmotions-com
nav: Providers
network: true
overview: 'llmotions-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, MotionGraphics, Animation, and Cloud.


  The llmotions-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Llmotions Com Plans Pricing
  plan_count: 4
  slug: llmotions-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Llmotions Com Rate Limits
  slug: llmotions-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: llmotions-com API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 2
  slug: llmotions-com-rules
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.5
    catalog_earned_first_party: 24.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 20.7
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Llmotions Com Authentication
  slug: llmotions-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Llmotions Com Domain Security
  slug: llmotions-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: getting-started
  slug: llmotions-com-getting-started
slug: llmotions-com
tags:
- Company
- AI
- MotionGraphics
- Animation
- Cloud
website: https://llmotions.com/
---
