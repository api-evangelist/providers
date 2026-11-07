---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Arnekellmann De Agentic Access
  operation_count: 3
  slug: arnekellmann-de-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://arnekellmann.de
  baseurl_source: declared
  description: The Documents API from Arne Kellmann — 1 operation(s) for documents.
  name: Arne Kellmann Documents API
  slug: arnekellmann-de-documents-api
- baseURL: https://arnekellmann.de
  baseurl_source: declared
  description: The Sandbox API from Arne Kellmann — 1 operation(s) for sandbox.
  name: Arne Kellmann Sandbox API
  slug: arnekellmann-de-sandbox-api
- baseURL: https://arnekellmann.de
  baseurl_source: declared
  description: The Versioning.md API from Arne Kellmann — 1 operation(s) for versioning.md.
  name: Arne Kellmann Versioning.md API
  slug: arnekellmann-de-versioning-md-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/arnekellmann-de/agentic-access/arnekellmann-de-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arnekellmann-de-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/arnekellmann-de/rate-limits/arnekellmann-de-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arnekellmann-de-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/arnekellmann-de/plans/arnekellmann-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arnekellmann-de-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/rules/arnekellmann-de-rules.yml
  title: ''
  type: Spectral
  url: rules/arnekellmann-de-rules.yml
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/json-ld/arnekellmann-de-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arnekellmann-de-context.jsonld
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/vocabulary/arnekellmann-de-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arnekellmann-de-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arnekellmann-de/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/data-model/arnekellmann-de-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arnekellmann-de-data-model.yml
- group: build
  href: https://artifacts.apis.io/arnekellmann-de/cli/arnekellmann-de-cli.yml
  title: ''
  type: CLI
  url: cli/arnekellmann-de-cli.yml
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/conventions/arnekellmann-de-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/arnekellmann-de-conventions.yml
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/conventions/arnekellmann-de-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arnekellmann-de-conventions.yml
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/lifecycle/arnekellmann-de-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/arnekellmann-de-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/errors/arnekellmann-de-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arnekellmann-de-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arnekellmann-de/conformance/arnekellmann-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arnekellmann-de-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arnekellmann-de/llms/arnekellmann-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arnekellmann-de-llms.txt
- group: build
  href: https://artifacts.apis.io/arnekellmann-de/mcp/arnekellmann-de-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/arnekellmann-de-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/arnekellmann-de/mcp/arnekellmann-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arnekellmann-de-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arnekellmann-de/well-known/arnekellmann-de-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arnekellmann-de-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/arnekellmann-de/well-known/arnekellmann-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arnekellmann-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/arnekellmann-de/hosts/arnekellmann-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arnekellmann-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/arnekellmann-de/vendors/arnekellmann-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arnekellmann-de-vendors.yml
- group: build
  href: https://artifacts.apis.io/arnekellmann-de/packages/arnekellmann-de-packages.yml
  title: ''
  type: SDKs
  url: packages/arnekellmann-de-packages.yml
- group: build
  href: https://artifacts.apis.io/arnekellmann-de/packages/arnekellmann-de-packages.yml
  title: ''
  type: Packages
  url: packages/arnekellmann-de-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://arnekellmann.de/sandbox
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArneFfm
- group: auth
  href: https://artifacts.apis.io/arnekellmann-de/security/arnekellmann-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arnekellmann-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arnekellmann.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arnekellmann.de/developers
- group: docs
  title: ''
  type: APIReference
  url: https://arnekellmann.de/api
- group: company
  title: ''
  type: Blog
  url: https://arnekellmann.de/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://arnekellmann.de/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arnekellmann.de/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arnekellmann.de/privacy
created: '2026-11-01'
description: Arne Kellmann is an AI solution architect who designs and ships production AI systems, covering architecture, retrieval, evaluation, guardrails, and cost control. He works remotely with teams worldwide in English or German, bringing over 15 years of software development and architecture experience. His services include written architecture assessments, production‑ready AI feature implementation, and ongoing guidance to ensure safe and cost‑effective AI deployments.
image: https://arnekellmann.de/og-image.png
jsonld:
- class_count: 1
  name: Arnekellmann De Context
  property_count: 5
  slug: arnekellmann-de-context
layout: provider
mcp_servers:
- description: Remote MCP server at arnekellmann.de.
  name: Arne Kellmann MCP Server
  slug: arnekellmann-de-mcp-yml
modified: '2026-11-02'
name: Arne Kellmann
nav: Providers
network: true
overview: 'Arne Kellmann publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Documents API, Sandbox API, and Versioning.md API. Tagged areas include Artificial Intelligence, Architecture, Consultant, Remote, and Software.


  The Arne Kellmann catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arne Kellmann''s developer surface includes CLI, sandbox, API reference, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Arnekellmann De Plans Pricing
  plan_count: 1
  slug: arnekellmann-de-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Arnekellmann De Rate Limits
  slug: arnekellmann-de-rate-limits
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Arne Kellmann API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: arnekellmann-de-rules
scopes:
- name: Arnekellmann De Scopes
  scope_count: 0
  slug: arnekellmann-de-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 63.8
    catalog_earned_first_party: 16.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 47.5
    developer_ergonomics: 33.8
    discoverability: 65.0
    operational_transparency: 34.2
  previous_composite: 47.4
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arnekellmann De Authentication
  slug: arnekellmann-de-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arnekellmann De Domain Security
  slug: arnekellmann-de-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: assess-architecture-fit
  slug: assess-architecture-fit-SKILL
slug: arnekellmann-de
tags:
- Artificial Intelligence
- Architecture
- Consultant
- Remote
- Software
website: https://arnekellmann.de/
---
