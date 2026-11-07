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
  score: 9.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Devplane Dev Agentic Access
  operation_count: 4
  slug: devplane-dev-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Public content API providing marketing pages, FAQs, and comparisons. Read‑only and unauthenticated.
  name: DevPlane Content API
  slug: devplane-content-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/devplane-dev/agentic-access/devplane-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/devplane-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/devplane-dev/rules/devplane-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/devplane-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/devplane-dev/vocabulary/devplane-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/devplane-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/devplane-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/devplane-dev/errors/devplane-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/devplane-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/devplane-dev/conformance/devplane-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/devplane-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/devplane-dev/llms/devplane-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/devplane-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/devplane-dev/mcp/devplane-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/devplane-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/devplane-dev/mcp/devplane-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/devplane-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/devplane-dev/hosts/devplane-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devplane-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/devplane-dev/vendors/devplane-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devplane-dev-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devplane.dev/privacy
- group: auth
  href: https://artifacts.apis.io/devplane-dev/security/devplane-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devplane-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devplane.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://devplane.dev/free
- group: operate
  title: ''
  type: Support
  url: https://devplane.dev/support
- group: operate
  title: ''
  type: FAQ
  url: https://devplane.dev/faq
created: '2026-11-05'
description: DevPlane provides AI development operations, checking AI coding agents' done claims against git remotes, deployments, and live pages across repositories and vendors. It offers free tools, support resources, FAQs, and integrates with developer workflows to ensure AI-generated code meets expectations and compliance.
layout: provider
mcp_servers:
- description: Remote MCP server at devplane.dev.
  name: DevPlane MCP Server
  slug: devplane-dev-mcp-yml
modified: '2026-11-05'
name: DevPlane
nav: Providers
network: true
overview: 'DevPlane is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Development, Platform, and Developer Tools.


  The DevPlane catalog on APIs.io includes 1 Spectral governance ruleset.


  DevPlane''s developer surface includes getting-started guide, support, FAQ, and 14 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: DevPlane API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: devplane-dev-rules
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devplane Dev Domain Security
  slug: devplane-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: content
  slug: devplane-dev-content
slug: devplane-dev
tags:
- Artificial Intelligence
- Development
- Platform
- Developer Tools
website: https://devplane.dev/
---
