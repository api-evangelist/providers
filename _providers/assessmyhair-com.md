---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Assessmyhair Com Agentic Access
  operation_count: 3
  slug: assessmyhair-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://assessmyhair.com
  baseurl_source: declared
  description: The Assess Hair Needs API from Assess My Hair — 1 operation(s) for assess hair needs.
  name: Assess My Hair Assess Hair Needs API
  slug: assessmyhair-com-assess-hair-needs-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/assessmyhair-com/agentic-access/assessmyhair-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/assessmyhair-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/assessmyhair-com/rules/assessmyhair-com-rules.yml
  title: ''
  type: Spectral
  url: rules/assessmyhair-com-rules.yml
- group: design
  href: https://artifacts.apis.io/assessmyhair-com/json-ld/assessmyhair-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/assessmyhair-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/assessmyhair-com/vocabulary/assessmyhair-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/assessmyhair-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/assessmyhair-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/assessmyhair-com/data-model/assessmyhair-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/assessmyhair-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/assessmyhair-com/errors/assessmyhair-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/assessmyhair-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/assessmyhair-com/conformance/assessmyhair-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/assessmyhair-com-conformance.yml
- group: build
  href: https://artifacts.apis.io/assessmyhair-com/mcp/assessmyhair-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/assessmyhair-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/assessmyhair-com/mcp/assessmyhair-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/assessmyhair-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/assessmyhair-com/hosts/assessmyhair-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assessmyhair-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/assessmyhair-com/vendors/assessmyhair-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assessmyhair-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/assessmyhair-com/security/assessmyhair-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assessmyhair-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assessmyhair.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://assessmyhair.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://assessmyhair.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://assessmyhair.com/docs
created: '2026-11-01'
description: Assess My Hair provides a cosmetic decision engine that offers personalized hair and scalp assessments for coily and 4C hair types. Users complete a short questionnaire in about five minutes without providing an email, receiving a detailed score, a 90‑day care plan, and product recommendations tailored to their hair concerns such as breakage, thinning, dryness, or scalp irritation. The service is powered by Rich Mom Recommends and is intended for cosmetic guidance only, not medical advice.
image: https://assessmyhair.com/assess-hair-hero.jpg
json_schemas:
- name: AssessHairNeedsInput
  property_count: 4
  slug: assessmyhair-com-assess-hair-needs-input
- name: AssessHairNeedsResult
  property_count: 9
  slug: assessmyhair-com-assess-hair-needs-result
jsonld:
- class_count: 2
  name: Assessmyhair Com Context
  property_count: 13
  slug: assessmyhair-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at assessmyhair.com.
  name: Assess My Hair MCP Server
  slug: assessmyhair-com-mcp-yml
modified: '2026-11-02'
name: Assess My Hair
nav: Providers
network: true
overview: 'Assess My Hair publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Assess Hair Needs API. Tagged areas include Hair, Scalp, Beauty, Assessment, and Personalization.


  The Assess My Hair catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Assess My Hair''s developer surface includes documentation, API reference, and 15 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 0
  name: Assessmyhair Com Rate Limits
  slug: assessmyhair-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Assess My Hair API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: assessmyhair-com-rules
scopes:
- name: Assessmyhair Com Scopes
  scope_count: 0
  slug: assessmyhair-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 53.4
    developer_ergonomics: 19.5
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assessmyhair Com Authentication
  slug: assessmyhair-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Assessmyhair Com Domain Security
  slug: assessmyhair-com-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: assess-hair-needs
  slug: assessmyhair-com-assess-hair-needs
slug: assessmyhair-com
tags:
- Hair
- Scalp
- Beauty
- Assessment
- Personalization
- Cosmetics
website: https://assessmyhair.com/
---
