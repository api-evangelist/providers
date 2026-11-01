---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 'Capanix: the monthly searches, read from search (a month), served as an agent-callable dataset with its source and licence on every answer.'
  name: Capanix API
  slug: capanix-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/capanix-com/rules/capanix-com-rules.yml
  title: ''
  type: Spectral
  url: rules/capanix-com-rules.yml
- group: design
  href: https://artifacts.apis.io/capanix-com/errors/capanix-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/capanix-com-problem-types.yml
- group: commercial
  href: https://artifacts.apis.io/capanix-com/plans/capanix-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/capanix-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/capanix-com/vocabulary/capanix-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/capanix-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/capanix-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://capanix.com/terms
- group: design
  href: https://artifacts.apis.io/capanix-com/conformance/capanix-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/capanix-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/capanix-com/llms/capanix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/capanix-com-llms.txt
- group: build
  href: https://artifacts.apis.io/capanix-com/mcp/capanix-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/capanix-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/capanix-com/mcp/capanix-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/capanix-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/capanix-com/well-known/capanix-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capanix-com-security.txt
- group: auth
  href: https://artifacts.apis.io/capanix-com/well-known/capanix-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/capanix-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/capanix-com/well-known/capanix-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capanix-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/capanix-com/hosts/capanix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capanix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/capanix-com/vendors/capanix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/capanix-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/capanix-com/authentication/capanix-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/capanix-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/capanix-com/security/capanix-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/capanix-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/capanix-com/security/capanix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capanix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capanix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://capanix.com/tools/
- group: start
  title: ''
  type: GettingStarted
  url: https://capanix.com/tools/
- group: operate
  title: ''
  type: Support
  url: https://capanix.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://capanix.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capanix.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capanix.com/privacy/
created: '2026-10-29'
description: Capanix provides free audit preparation worksheets and templates covering ISO, safety, GMP, HR, and other compliance areas. Users can download checklists and internal audit templates to size audits, gather evidence, estimate effort, and track corrective actions. A paid plan offers full audit program management, storing every audit, finding, and corrective action to closure.
image: https://capanix.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at capanix.com.
  name: capanix-com MCP Server
  slug: capanix-com-mcp-yml
modified: '2026-10-29'
name: capanix-com
nav: Providers
network: true
overview: 'capanix-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Audit, ISO, Safety, GMP, and HR.


  The capanix-com catalog on APIs.io includes 1 Spectral governance ruleset.


  capanix-com''s developer surface includes authentication, documentation, getting-started guide, support, pricing, and 20 more developer resources.'
plans:
- name: Capanix Com Plans Pricing
  plan_count: 2
  slug: capanix-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: capanix-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: capanix-com-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 6.0
    developer_ergonomics: 44.5
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Capanix Com Authentication
  slug: capanix-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Capanix Com Domain Security
  slug: capanix-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Capanix Com Vulnerability Disclosure
  slug: capanix-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: capanix-com-dataset
  slug: capanix-com-dataset
slug: capanix-com
tags:
- Audit
- ISO
- Safety
- GMP
- HR
- Templates
website: https://capanix.com/
---
