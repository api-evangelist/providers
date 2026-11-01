---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Pay-per-call data APIs for AI agents covering company intelligence, news, jobs, app reviews, and Singapore property workflows.
  name: Bounty API
  slug: bounty-api
- description: 'Pay-per-call data APIs for AI agents: company intelligence, news, jobs, app reviews, and Singapore property workflows.'
  name: Bounty API API
  slug: bounty-api-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/bountyapi-com/llms/bountyapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bountyapi-com-llms.txt
- group: commercial
  href: https://artifacts.apis.io/bountyapi-com/plans/bountyapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bountyapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bountyapi-com/rules/bountyapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bountyapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bountyapi-com/json-ld/bountyapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bountyapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bountyapi-com/vocabulary/bountyapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bountyapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bountyapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bountyapi-com/data-model/bountyapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bountyapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bountyapi-com/conventions/bountyapi-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bountyapi-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/bountyapi-com/conventions/bountyapi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bountyapi-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/bountyapi-com/errors/bountyapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bountyapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bountyapi-com/conformance/bountyapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bountyapi-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/bountyapi-com/hosts/bountyapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bountyapi-com-hosts.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://bountyapi.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://bountyapi.com/setup
- group: docs
  title: ''
  type: APIReference
  url: https://bountyapi.com/docs
- group: company
  title: ''
  type: Website
  url: https://bountyapi.com/
- group: auth
  href: https://artifacts.apis.io/bountyapi-com/security/bountyapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bountyapi-com-domain-security.yml
created: '2026-10-30'
description: Bounty API provides pay‑per‑call data APIs for AI agents, offering social intelligence, company intelligence, news, job postings, and app reviews. It operates without API keys or subscriptions, using MCP discovery and x402 payments. Agents can query endpoints like YouTube search, company data, news, jobs, and app reviews with transparent per‑call pricing.
image: https://bountyapi.com/og-image.png
json_schemas:
- name: AffordabilityRequest
  property_count: 9
  slug: bountyapi-com-affordability-request
- name: CompanyIntelResult
  property_count: 22
  slug: bountyapi-com-company-intel-result
- name: InvestCalcRequest
  property_count: 7
  slug: bountyapi-com-invest-calc-request
- name: InvestCalcResult
  property_count: 14
  slug: bountyapi-com-invest-calc-result
- name: PitchRequest
  property_count: 15
  slug: bountyapi-com-pitch-request
- name: PropertyAnalysisRequest
  property_count: 13
  slug: bountyapi-com-property-analysis-request
jsonld:
- class_count: 77
  name: Bountyapi Com Context
  property_count: 270
  slug: bountyapi-com-context
layout: provider
modified: '2026-10-30'
name: bountyapi-com
nav: Providers
network: true
overview: 'bountyapi-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bounty API API, and 1 more. Tagged areas include Company, Data, AI, MCP, and Pay-per-call.


  The bountyapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  bountyapi-com''s developer surface includes pricing, getting-started guide, API reference, and 14 more developer resources.'
plans:
- name: Bountyapi Com Plans Pricing
  plan_count: 15
  slug: bountyapi-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: bountyapi-com API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 3
  slug: bountyapi-com-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 83.5
    catalog_earned_first_party: 0.0
    catalog_gap: 31.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.9
    contract_governance: 79.1
    contract_quality: 50.7
    developer_ergonomics: 25.5
    discoverability: 57.1
    operational_transparency: 0.0
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
- kind: domain-security
  name: Bountyapi Com Domain Security
  slug: bountyapi-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 1
skills:
- name: getting-started
  slug: bountyapi-com-getting_started
slug: bountyapi-com
tags:
- Company
- Data
- AI
- MCP
- Pay-per-call
website: https://bountyapi.com/
---
