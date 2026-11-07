---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 28.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Every tool the AgentDrive MCP server exposes today and what each one does.
  name: AgentDrive MCP API
  slug: agentdrive-mcp-api
- baseURL: https://app.agentdrive.sh
  baseurl_source: declared
  description: 'AgentDrive API as documented publicly: 25 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: AgentDrive API
  slug: agentdrive-sh-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/agentdrive-sh/rate-limits/agentdrive-sh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentdrive-sh-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/agentdrive-sh/rules/agentdrive-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/agentdrive-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/agentdrive-sh/json-ld/agentdrive-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentdrive-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentdrive-sh/vocabulary/agentdrive-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentdrive-sh-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentdrive-sh/data-model/agentdrive-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentdrive-sh-data-model.yml
- group: build
  href: https://artifacts.apis.io/agentdrive-sh/cli/agentdrive-sh-cli.yml
  title: ''
  type: CLI
  url: cli/agentdrive-sh-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agentdrive.sh/security
- group: auth
  href: https://artifacts.apis.io/agentdrive-sh/security/agentdrive-sh-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentdrive-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentdrive-sh/authentication/agentdrive-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentdrive-sh-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentdrive-sh/lifecycle/agentdrive-sh-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentdrive-sh-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agentdrive-sh/errors/agentdrive-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentdrive-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentdrive-sh/conformance/agentdrive-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdrive-sh-conformance.yml
- group: other
  href: https://artifacts.apis.io/agentdrive-sh/hosts/agentdrive-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentdrive-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentdrive-sh/vendors/agentdrive-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentdrive-sh-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentdrive.sh/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentdrive.sh/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://agentdrive.sh/login
- group: start
  title: ''
  type: GettingStarted
  url: https://agentdrive.sh/docs/quick-start
- group: auth
  href: https://artifacts.apis.io/agentdrive-sh/security/agentdrive-sh-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agentdrive-sh-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agentdrive-sh/security/agentdrive-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentdrive-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentdrive-sh/security/agentdrive-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdrive-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentdrive.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://agentdrive.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentdrive.sh/docs
- group: operate
  title: ''
  type: Support
  url: https://agentdrive.sh/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rakesh1002/agentdrive-mcp
- group: build
  href: https://artifacts.apis.io/agentdrive-sh/mcp/agentdrive-sh-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentdrive-sh-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentdrive-sh/mcp/agentdrive-sh-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentdrive-sh-mcp.yml
created: '2026-10-31'
description: AgentDrive provides a persistent artifact workspace that lets multiple AI agents share files, memory, and provenance. It supports cross‑agent workflows across Claude Code, Codex, Cursor, and LangGraph, offering portable storage on Cloudflare R2, Amazon S3, or custom buckets. The platform aims to solve the serialization problem in multi‑agent systems by offering versioned, content‑addressed storage that is searchable and auditable, without locking users into a proprietary SDK.
image: https://agentdrive.sh/opengraph-image?1ca9ae5e9c18bca2
json_schemas:
- name: GetInstallResponse
  property_count: 4
  slug: agentdrive-sh-get-install-response
jsonld:
- class_count: 1
  name: Agentdrive Sh Context
  property_count: 4
  slug: agentdrive-sh-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.agentdrive.sh.
  name: AgentDrive MCP Server
  slug: agentdrive-sh-mcp-yml
- description: ''
  name: AgentDrive MCP Server
  slug: agentdrive-sh-mcp-json
modified: '2026-10-31'
name: AgentDrive
nav: Providers
network: true
overview: 'AgentDrive is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AgentDrive, Artificial Intelligence, Multi-Agent, Workspace, and Memory.


  The AgentDrive catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentDrive''s developer surface includes CLI, authentication, getting-started guide, documentation, API reference, support, and 22 more developer resources.'
plans:
- name: Agentdrive Sh Plans Pricing
  plan_count: 0
  slug: agentdrive-sh-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Agentdrive Sh Rate Limits
  slug: agentdrive-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AgentDrive API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: agentdrive-sh-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.2
    catalog_earned_first_party: 8.0
    catalog_gap: 53.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 35.7
    discoverability: 65.0
    operational_transparency: 34.2
  previous_composite: 41.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
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
  name: Agentdrive Sh Authentication
  slug: agentdrive-sh-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Agentdrive Sh Domain Security
  slug: agentdrive-sh-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agentdrive Sh Vulnerability Disclosure
  slug: agentdrive-sh-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Agentdrive Sh Trust Center
  slug: agentdrive-sh-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP, GDPR
slug: agentdrive-sh
tags:
- AgentDrive
- Artificial Intelligence
- Multi-Agent
- Workspace
- Memory
- MCP
website: https://agentdrive.sh/
---
