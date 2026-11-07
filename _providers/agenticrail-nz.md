---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Agenticrail Nz Agentic Access
  operation_count: 4
  slug: agenticrail-nz-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.agenticrail.nz
  baseurl_source: declared
  description: Pre-execution gate decisions
  name: AgenticRail Enforcement API
  slug: agenticrail-nz-enforcement-api
- baseURL: https://api.agenticrail.nz
  baseurl_source: declared
  description: Verifiable records of what was enforced
  name: AgenticRail Evidence API
  slug: agenticrail-nz-evidence-api
- baseURL: https://api.agenticrail.nz
  baseurl_source: declared
  description: Health and latency helpers
  name: AgenticRail Operational API
  slug: agenticrail-nz-operational-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/agenticrail-nz/agentic-access/agenticrail-nz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenticrail-nz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agenticrail-nz/rules/agenticrail-nz-rules.yml
  title: ''
  type: Spectral
  url: rules/agenticrail-nz-rules.yml
- group: design
  href: https://artifacts.apis.io/agenticrail-nz/json-ld/agenticrail-nz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agenticrail-nz-context.jsonld
- group: design
  href: https://artifacts.apis.io/agenticrail-nz/vocabulary/agenticrail-nz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenticrail-nz-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agenticrail-nz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agenticrail-nz/data-model/agenticrail-nz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenticrail-nz-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agenticrail.nz/compliance/
- group: design
  href: https://artifacts.apis.io/agenticrail-nz/errors/agenticrail-nz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenticrail-nz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agenticrail-nz/conformance/agenticrail-nz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenticrail-nz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenticrail-nz/llms/agenticrail-nz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenticrail-nz-llms.txt
- group: build
  href: https://artifacts.apis.io/agenticrail-nz/mcp/agenticrail-nz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agenticrail-nz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agenticrail-nz/mcp/agenticrail-nz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenticrail-nz-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agenticrail-nz/well-known/agenticrail-nz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agenticrail-nz-security.txt
- group: agent
  href: https://artifacts.apis.io/agenticrail-nz/well-known/agenticrail-nz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenticrail-nz-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenticrail-nz/hosts/agenticrail-nz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticrail-nz-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticrail-nz/vendors/agenticrail-nz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticrail-nz-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://agenticrail.nz/security/
- group: auth
  href: https://artifacts.apis.io/agenticrail-nz/authentication/agenticrail-nz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenticrail-nz-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agenticrail-nz/security/agenticrail-nz-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agenticrail-nz-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agenticrail-nz/security/agenticrail-nz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agenticrail-nz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agenticrail-nz/security/agenticrail-nz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticrail-nz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticrail.nz/
- group: docs
  title: ''
  type: Documentation
  url: https://agenticrail.nz/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://agenticrail.nz/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://agenticrail.nz/demo/
- group: operate
  title: ''
  type: Support
  url: https://agenticrail.nz/faq/
- group: company
  title: ''
  type: Blog
  url: https://agenticrail.nz/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MSMD-RUA
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenticrail.nz/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenticrail.nz/privacy/
created: '2026-11-01'
description: AgenticRail provides a deterministic sequence enforcement gate for AI agents and automated processes. It prevents out‑of‑order steps, replay attacks, and unauthorized actions by evaluating each step before execution and issuing an Ed25519‑signed receipt. The system supports compliance reporting, cryptographic audit trails, and integrates with existing AI workflows, ensuring transparent and tamper‑evident operation.
image: https://agenticrail.nz/og-image.png
json_schemas:
- name: EvaluateRequest
  property_count: 10
  slug: agenticrail-nz-evaluate-request
- name: EvaluateResponse
  property_count: 23
  slug: agenticrail-nz-evaluate-response
- name: ReportRequest
  property_count: 3
  slug: agenticrail-nz-report-request
- name: Report
  property_count: 16
  slug: agenticrail-nz-report
jsonld:
- class_count: 7
  name: Agenticrail Nz Context
  property_count: 53
  slug: agenticrail-nz-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.agenticrail.nz.
  name: AgenticRail MCP Server
  slug: agenticrail-nz-mcp-yml
modified: '2026-11-01'
name: AgenticRail
nav: Providers
network: true
overview: 'AgenticRail publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Enforcement API, Evidence API, and Operational API. Tagged areas include Artificial Intelligence, Automation, Sequence Enforcement, Cryptographic Receipts, and Compliance.


  The AgenticRail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgenticRail''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AgenticRail API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: agenticrail-nz-rules
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 66.1
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenticrail Nz Authentication
  slug: agenticrail-nz-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agenticrail Nz Domain Security
  slug: agenticrail-nz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Agenticrail Nz Vulnerability Disclosure
  slug: agenticrail-nz-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Agenticrail Nz Trust Center
  slug: agenticrail-nz-trust-center
  summary_line: PCI DSS, GDPR
skill_count: 2
skills:
- name: evaluate-step
  slug: agenticrail-nz-evaluate-step
- name: verify-receipt
  slug: agenticrail-nz-verify-receipt
slug: agenticrail-nz
tags:
- Artificial Intelligence
- Automation
- Sequence Enforcement
- Cryptographic Receipts
- Compliance
website: https://agenticrail.nz/
---
