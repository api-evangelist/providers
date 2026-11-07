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
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Tartu Agentic Access
  operation_count: 1
  slug: university-of-tartu-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: TU Financial Web API providing financial data.
  name: Financial Web API
  slug: financial-web-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/university-of-tartu/agentic-access/university-of-tartu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-tartu-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/university-of-tartu/rules/university-of-tartu-rules.yml
  title: ''
  type: Spectral
  url: rules/university-of-tartu-rules.yml
- group: design
  href: https://artifacts.apis.io/university-of-tartu/json-ld/university-of-tartu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/university-of-tartu-context.jsonld
- group: design
  href: https://artifacts.apis.io/university-of-tartu/vocabulary/university-of-tartu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-tartu-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/university-of-tartu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/university-of-tartu/data-model/university-of-tartu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/university-of-tartu-data-model.yml
- group: design
  href: https://artifacts.apis.io/university-of-tartu/errors/university-of-tartu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/university-of-tartu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/university-of-tartu/conformance/university-of-tartu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-tartu-conformance.yml
- group: other
  href: https://artifacts.apis.io/university-of-tartu/overlays/university-of-tartu-financial-web-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/university-of-tartu-financial-web-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/university-of-tartu/llms/university-of-tartu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/university-of-tartu-llms.txt
- group: agent
  href: https://artifacts.apis.io/university-of-tartu/mcp/university-of-tartu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/university-of-tartu-mcp.yml
- group: other
  href: https://artifacts.apis.io/university-of-tartu/hosts/university-of-tartu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/university-of-tartu-hosts.yml
- group: other
  href: https://artifacts.apis.io/university-of-tartu/vendors/university-of-tartu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/university-of-tartu-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blog.ut.ee/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://ut.ee/en/news/creativity-drives-game-both-research-and-entrepreneurship
- group: other
  title: ''
  type: Leadership
  url: https://cs.ut.ee/en/management
- group: docs
  title: ''
  type: Documentation
  url: https://api.ut.ee/docs/
- group: company
  title: ''
  type: Blog
  url: https://blog.ut.ee/
- group: auth
  href: https://artifacts.apis.io/university-of-tartu/security/university-of-tartu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-tartu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ut.ee
created: '2026-10-29'
description: The University of Tartu is Estonia’s leading research university, founded in 1632. It ranks among the top institutions in the Baltic region, offering a wide range of undergraduate, graduate, and doctoral programs across sciences, humanities, and social sciences. The university emphasizes research, international collaboration, and innovation, contributing significantly to education and knowledge advancement in Europe.
image: https://ut.ee/themes/utheme/assets/img/UT_website_logo_blue_est.svg
jsonld:
- class_count: 2
  name: University Of Tartu Context
  property_count: 15
  slug: university-of-tartu-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.ut.ee.
  name: University of Tartu MCP Server
  slug: university-of-tartu-mcp-yml
modified: '2026-10-29'
name: University of Tartu
nav: Providers
network: true
overview: 'University of Tartu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Higher Education, Research, and Estonia.


  The University of Tartu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Tartu''s developer surface includes documentation, engineering blog, and 18 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: University of Tartu API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: university-of-tartu-rules
scopes:
- name: University Of Tartu Scopes
  scope_count: 0
  slug: university-of-tartu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 12.4
    discoverability: 76.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - estonia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/university-of-tartu/university-of-tartu-2026-11-03T145446.png
security:
- kind: authentication
  name: University Of Tartu Authentication
  slug: university-of-tartu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Tartu Domain Security
  slug: university-of-tartu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-financial-data
  slug: university-of-tartu-get-financial-data
slug: university-of-tartu
tags:
- Company
- Education
- Higher Education
- Research
- Estonia
- University
website: https://ut.ee
---
