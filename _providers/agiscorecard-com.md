---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agiscorecard Com Agentic Access
  operation_count: 3
  slug: agiscorecard-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://agentready.agiscorecard.com
  baseurl_source: declared
  description: The Badge API from agiscorecard-com — 1 operation(s) for badge.
  name: agiscorecard-com Badge API
  slug: agiscorecard-com-badge-api
- baseURL: https://agentready.agiscorecard.com
  baseurl_source: declared
  description: The Scan API from agiscorecard-com — 1 operation(s) for scan.
  name: agiscorecard-com Scan API
  slug: agiscorecard-com-scan-api
- baseURL: https://agentready.agiscorecard.com
  baseurl_source: declared
  description: The Verify API from agiscorecard-com — 1 operation(s) for verify.
  name: agiscorecard-com Verify API
  slug: agiscorecard-com-verify-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/agiscorecard-com/agentic-access/agiscorecard-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agiscorecard-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agiscorecard-com/rules/agiscorecard-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agiscorecard-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agiscorecard-com/json-ld/agiscorecard-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agiscorecard-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agiscorecard-com/vocabulary/agiscorecard-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agiscorecard-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agiscorecard-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agiscorecard-com/data-model/agiscorecard-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agiscorecard-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agiscorecard-com/errors/agiscorecard-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agiscorecard-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agiscorecard-com/conformance/agiscorecard-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agiscorecard-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agiscorecard-com/llms/agiscorecard-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agiscorecard-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agiscorecard-com/a2a/agiscorecard-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agiscorecard-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/agiscorecard-com/mcp/agiscorecard-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agiscorecard-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agiscorecard-com/mcp/agiscorecard-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agiscorecard-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agiscorecard-com/well-known/agiscorecard-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agiscorecard-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agiscorecard-com/hosts/agiscorecard-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agiscorecard-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agiscorecard-com/vendors/agiscorecard-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agiscorecard-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://agiscorecard.com/changelog
- group: auth
  href: https://artifacts.apis.io/agiscorecard-com/security/agiscorecard-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agiscorecard-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agiscorecard.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agiscorecard.com/privacy
created: '2026-10-29'
description: AGI Scorecard is a platform that aggregates and curates AI interview videos, creator content, and forecasts related to artificial general intelligence (AGI). It provides a searchable database of AI‑related interviews, original video content, and analytical takeaways, helping researchers, enthusiasts, and industry professionals track AI progress, understand emerging trends, and monitor the AGI countdown. The site also offers tools for evaluating AI developments and visualizing prediction evidence.
image: https://agiscorecard.com/og-image.png
json_schemas:
- name: ScanReport
  property_count: 6
  slug: agiscorecard-com-scan-report
- name: VerifyStatus
  property_count: 8
  slug: agiscorecard-com-verify-status
jsonld:
- class_count: 4
  name: Agiscorecard Com Context
  property_count: 20
  slug: agiscorecard-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at agiscorecard.com.
  name: agiscorecard-com MCP Server
  slug: agiscorecard-com-mcp-yml
modified: '2026-10-29'
name: agiscorecard-com
nav: Providers
network: true
overview: 'agiscorecard-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Badge API, Scan API, and Verify API. Tagged areas include Company, AI, AGI, Video, and Research.


  The agiscorecard-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agiscorecard-com''s developer surface includes changelog and 18 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: agiscorecard-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: agiscorecard-com-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 59.7
    developer_ergonomics: 6.4
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agiscorecard Com Domain Security
  slug: agiscorecard-com-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: badge-svg
  slug: agiscorecard-com-badge-svg
- name: scan-site
  slug: agiscorecard-com-scan-site
- name: verify-status
  slug: agiscorecard-com-verify-status
slug: agiscorecard-com
tags:
- Company
- AI
- AGI
- Video
- Research
- Analytics
website: https://agiscorecard.com/
---
