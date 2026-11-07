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
  score: 7.4
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/babyname-guide/rules/babyname-guide-rules.yml
  title: ''
  type: Spectral
  url: rules/babyname-guide-rules.yml
- group: design
  href: https://artifacts.apis.io/babyname-guide/vocabulary/babyname-guide-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/babyname-guide-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/babyname-guide/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/babyname-guide/errors/babyname-guide-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/babyname-guide-problem-types.yml
- group: design
  href: https://artifacts.apis.io/babyname-guide/conformance/babyname-guide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/babyname-guide-conformance.yml
- group: agent
  href: https://artifacts.apis.io/babyname-guide/llms/babyname-guide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/babyname-guide-llms.txt
- group: build
  href: https://artifacts.apis.io/babyname-guide/mcp/babyname-guide-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/babyname-guide-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/babyname-guide/mcp/babyname-guide-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/babyname-guide-mcp.yml
- group: other
  href: https://artifacts.apis.io/babyname-guide/hosts/babyname-guide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/babyname-guide-hosts.yml
- group: other
  href: https://artifacts.apis.io/babyname-guide/vendors/babyname-guide-vendors.yml
  title: ''
  type: Vendors
  url: vendors/babyname-guide-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://babyname.guide/llms.txt
- group: auth
  href: https://artifacts.apis.io/babyname-guide/security/babyname-guide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/babyname-guide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://babyname.guide/
- group: docs
  title: ''
  type: Documentation
  url: https://babyname.guide/guides
- group: operate
  title: ''
  type: Support
  url: https://babyname.guide/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://babyname.guide/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://babyname.guide/privacy
- group: start
  title: ''
  type: SignUp
  url: https://babyname.guide/account
coverage:
  checked: '2026-11-02'
  detail: OpenAPI spec at https://babyname.guide/openapi.json belongs to bicycle.guide, not babyname.guide, so no contract found.
  evidence:
  - status: 200
    url: https://babyname.guide/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: 'Naming is one decision you make once, under pressure, with everyone offering an opinion. This is the travel‑guide version: we read the research on how names actually land, the traditions behind them, and what parents wish they had known — honest about where the evidence is thin, and made to leave you confident rather than second‑guessing.'
image: https://babyname.guide/opengraph-image-1oy18k?29435694197f5727
layout: provider
mcp_servers:
- description: Remote MCP server at babyname.guide.
  name: Baby Name Guide MCP Server
  slug: babyname-guide-mcp-yml
modified: '2026-11-02'
name: Baby Name Guide
nav: Providers
network: true
overview: 'Baby Name Guide publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Baby Names, Parenting, guide, Research, and Naming.


  The Baby Name Guide catalog on APIs.io includes 1 Spectral governance ruleset.


  Baby Name Guide''s developer surface includes API reference, documentation, support, signup flow, and 14 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Baby Name Guide API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: babyname-guide-rules
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 17.1
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 20.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Babyname Guide Domain Security
  slug: babyname-guide-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-guides
  slug: babyname-guide-list-guides
slug: babyname-guide
tags:
- Baby Names
- Parenting
- guide
- Research
- Naming
website: https://babyname.guide/
---
