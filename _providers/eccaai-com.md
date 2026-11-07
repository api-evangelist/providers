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
  band: agent-aware
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
    error_semantics: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ECCA-AI public API providing multi-engine answer verification, adjudication, proof permalinks, key management, and billing.
  name: ECCA-AI API
  slug: ecca-ai-api
- baseURL: https://eccaai.com
  baseurl_source: declared
  description: ECCA-AI runs a question through several independent AI engines, then adjudicates their answers into one result and shows the reasoning that settled it. This document is derived from the route handlers
  name: ECCA-AI public API API
  slug: ecca-ai-public-api-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/eccaai-com/rules/eccaai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/eccaai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/eccaai-com/json-ld/eccaai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eccaai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/eccaai-com/vocabulary/eccaai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eccaai-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/eccaai-com/conformance/eccaai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eccaai-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/eccaai-com/plans/eccaai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eccaai-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eccaai-com/data-model/eccaai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eccaai-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/eccaai-com/changelog/eccaai-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/eccaai-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/eccaai-com/errors/eccaai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eccaai-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/eccaai-com/llms/eccaai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eccaai-com-llms.txt
- group: build
  href: https://artifacts.apis.io/eccaai-com/mcp/eccaai-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/eccaai-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/eccaai-com/mcp/eccaai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/eccaai-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/eccaai-com/hosts/eccaai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eccaai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/eccaai-com/vendors/eccaai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eccaai-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://eccaai.com/status
- group: start
  title: ''
  type: DeveloperPortal
  url: https://eccaai.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://eccaai.com/changelog
- group: auth
  href: https://artifacts.apis.io/eccaai-com/security/eccaai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eccaai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eccaai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://eccaai.com/method
- group: docs
  title: ''
  type: APIReference
  url: https://eccaai.com/method
- group: operate
  title: ''
  type: Support
  url: https://eccaai.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://eccaai.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eccaai.com/privacy
created: '2026-11-06'
description: ECCA provides a second‑opinion AI platform that aggregates answers from up to six independent AI engines, presenting split results with Socratic proof. Built by a psychology undergraduate after a wrong answer incident, the service aims to prevent single‑source AI hallucinations by letting users compare multiple responses, view reasoning, and see confidence metrics. It offers a studio for querying, a method page explaining its verification pipeline, and transparent changelogs and mistake logs. The platform emphasizes academic reasoning and dialectic evaluation, not medical use.
image: https://eccaai.com/assets/brand/og-default.png?v=7d298b9322b3
json_schemas:
- name: AtomicClaimRecord
  property_count: 10
  slug: eccaai-com-atomic-claim-record
- name: MissCounterResponse
  property_count: 13
  slug: eccaai-com-miss-counter-response
- name: ProofMachineRecord
  property_count: 11
  slug: eccaai-com-proof-machine-record
- name: ProofRecord
  property_count: 14
  slug: eccaai-com-proof-record
- name: SolveRequest
  property_count: 9
  slug: eccaai-com-solve-request
- name: SolveResult
  property_count: 9
  slug: eccaai-com-solve-result
jsonld:
- class_count: 33
  name: Eccaai Com Context
  property_count: 143
  slug: eccaai-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at eccaai.com.
  name: ECCA MCP Server
  slug: eccaai-com-mcp-yml
modified: '2026-11-06'
name: ECCA
nav: Providers
network: true
overview: 'ECCA publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including ECCA-AI public API API, and 1 more. Tagged areas include Company.


  The ECCA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ECCA''s developer surface includes changelog, documentation, API reference, support, pricing, and 18 more developer resources.'
plans:
- name: Eccaai Com Plans Pricing
  plan_count: 3
  slug: eccaai-com-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: ECCA API Rules
  rule_count: 63
  severity_counts:
    error: 48
    hint: 0
    info: 3
    warn: 12
  slug: eccaai-com-rules
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 31.6
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eccaai Com Domain Security
  slug: eccaai-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: eccaai-com
tags:
- Company
website: https://eccaai.com/
---
