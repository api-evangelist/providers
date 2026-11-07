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
    agent_skills: derived
    agentic_access: derived
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Canairecommendmybusiness Com Agentic Access
  operation_count: 2
  slug: canairecommendmybusiness-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Canonical REST door for the AI Recommendation Readiness assessment engine by The Black Friday Agency. Provides readiness score, tier, gap analysis, and roadmap.
  name: AI Recommendation Readiness Assessment API
  slug: ai-recommendation-readiness-assessment-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/canairecommendmybusiness-com/agentic-access/canairecommendmybusiness-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canairecommendmybusiness-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/canairecommendmybusiness-com/rules/canairecommendmybusiness-com-rules.yml
  title: ''
  type: Spectral
  url: rules/canairecommendmybusiness-com-rules.yml
- group: design
  href: https://artifacts.apis.io/canairecommendmybusiness-com/json-ld/canairecommendmybusiness-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canairecommendmybusiness-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/canairecommendmybusiness-com/vocabulary/canairecommendmybusiness-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canairecommendmybusiness-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/canairecommendmybusiness-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/canairecommendmybusiness-com/data-model/canairecommendmybusiness-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canairecommendmybusiness-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/canairecommendmybusiness-com/errors/canairecommendmybusiness-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canairecommendmybusiness-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/canairecommendmybusiness-com/conformance/canairecommendmybusiness-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canairecommendmybusiness-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canairecommendmybusiness-com/mcp/canairecommendmybusiness-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canairecommendmybusiness-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/canairecommendmybusiness-com/hosts/canairecommendmybusiness-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canairecommendmybusiness-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canairecommendmybusiness-com/vendors/canairecommendmybusiness-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canairecommendmybusiness-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/canairecommendmybusiness-com/security/canairecommendmybusiness-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canairecommendmybusiness-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canairecommendmybusiness.com/
created: '2026-11-04'
description: The Black Friday Agency offers a free AI Recommendation Readiness Audit that evaluates whether a business is understandable, verifiable, recommendable, and usable by AI systems. It helps small and midsize businesses improve AI visibility through a plain-English diagnostic covering eight readiness categories.
image: http://localhost:3000/og-image.png
json_schemas:
- name: AssessmentInputs
  property_count: 6
  slug: canairecommendmybusiness-com-assessment-inputs
- name: AssessmentResult
  property_count: 10
  slug: canairecommendmybusiness-com-assessment-result
jsonld:
- class_count: 2
  name: Canairecommendmybusiness Com Context
  property_count: 16
  slug: canairecommendmybusiness-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at canairecommendmybusiness.com.
  name: The Black Friday Agency MCP Server
  slug: canairecommendmybusiness-com-mcp-yml
modified: '2026-11-04'
name: The Black Friday Agency
nav: Providers
network: true
overview: 'The Black Friday Agency is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Recommendation, Business, Audit, Small Business, and Technology.


  The The Black Friday Agency catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: The Black Friday Agency API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: canairecommendmybusiness-com-rules
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 22.7
    developer_ergonomics: 1.8
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
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
  name: Canairecommendmybusiness Com Domain Security
  slug: canairecommendmybusiness-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: canairecommendmybusiness-com-assess-readiness
  slug: canairecommendmybusiness-com-assess-readiness
slug: canairecommendmybusiness-com
tags:
- AI Recommendation
- Business
- Audit
- Small Business
- Technology
website: https://canairecommendmybusiness.com/
---
