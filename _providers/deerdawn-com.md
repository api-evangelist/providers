---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Deerdawn Com Agentic Access
  operation_count: 15
  slug: deerdawn-com-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.deerdawn.com
  baseurl_source: declared
  description: The Auth API from DeerDawn — 2 operation(s) for auth.
  name: DeerDawn Auth API
  slug: deerdawn-com-auth-api
- baseURL: https://api.deerdawn.com
  baseurl_source: declared
  description: The Keys API from DeerDawn — 1 operation(s) for keys.
  name: DeerDawn Keys API
  slug: deerdawn-com-keys-api
- baseURL: https://api.deerdawn.com
  baseurl_source: declared
  description: The Session Memory API from DeerDawn — 7 operation(s) for session memory.
  name: DeerDawn Session Memory API
  slug: deerdawn-com-session-memory-api
- baseURL: https://api.deerdawn.com
  baseurl_source: declared
  description: The System API from DeerDawn — 2 operation(s) for system.
  name: DeerDawn System API
  slug: deerdawn-com-system-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/deerdawn-com/agentic-access/deerdawn-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deerdawn-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/deerdawn-com/plans/deerdawn-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deerdawn-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deerdawn-com/rules/deerdawn-com-rules.yml
  title: ''
  type: Spectral
  url: rules/deerdawn-com-rules.yml
- group: design
  href: https://artifacts.apis.io/deerdawn-com/json-ld/deerdawn-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deerdawn-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/deerdawn-com/vocabulary/deerdawn-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deerdawn-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deerdawn-com/data-model/deerdawn-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deerdawn-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/deerdawn-com/cli/deerdawn-com-cli.yml
  title: ''
  type: CLI
  url: cli/deerdawn-com-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://deerdawn.com/security
- group: auth
  href: https://artifacts.apis.io/deerdawn-com/authentication/deerdawn-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deerdawn-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/deerdawn-com/errors/deerdawn-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/deerdawn-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/deerdawn-com/conformance/deerdawn-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deerdawn-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/deerdawn-com/a2a/deerdawn-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deerdawn-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/deerdawn-com/mcp/deerdawn-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deerdawn-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/deerdawn-com/well-known/deerdawn-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deerdawn-com-security.txt
- group: agent
  href: https://artifacts.apis.io/deerdawn-com/well-known/deerdawn-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deerdawn-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/deerdawn-com/hosts/deerdawn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deerdawn-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/deerdawn-com/vendors/deerdawn-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deerdawn-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deerdawn.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://deerdawn.com/signup
- group: auth
  title: ''
  type: Security
  url: https://deerdawn.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deerdawn.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://deerdawn.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://deerdawn.com/docs
- group: company
  title: ''
  type: Blog
  url: https://deerdawn.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://deerdawn.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/deerdawn-com/security/deerdawn-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deerdawn-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/deerdawn-com/security/deerdawn-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deerdawn-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deerdawn-com/security/deerdawn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deerdawn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deerdawn.com/
created: '2026-11-05'
description: DeerDawn provides AI session memory, allowing AI tools to retain context across sessions. It captures project tasks, decisions, and open questions so that models like Claude, ChatGPT, Cursor, and Codex start with full awareness, preventing cold starts. The platform integrates with MCP-compatible AI tools, offering briefings that keep AI aligned with ongoing work.
image: https://deerdawn.com/og-image.png
json_schemas:
- name: ActiveBriefResponse
  property_count: 7
  slug: deerdawn-com-active-brief-response
- name: InjectResponse
  property_count: 1
  slug: deerdawn-com-inject-response
- name: ProjectSummary
  property_count: 4
  slug: deerdawn-com-project-summary
jsonld:
- class_count: 7
  name: Deerdawn Com Context
  property_count: 35
  slug: deerdawn-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.deerdawn.com.
  name: DeerDawn MCP Server
  slug: deerdawn-com-mcp-yml
modified: '2026-11-05'
name: DeerDawn
nav: Providers
network: true
overview: 'DeerDawn publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Keys API, Session Memory API, and 1 more. Tagged areas include Artificial Intelligence, Session Memory, MCP, Productivity, and Platform.


  The DeerDawn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeerDawn''s developer surface includes CLI, authentication, signup flow, pricing, documentation, engineering blog, getting-started guide, and 22 more developer resources.'
plans:
- name: Deerdawn Com Plans Pricing
  plan_count: 3
  slug: deerdawn-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: DeerDawn API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: deerdawn-com-rules
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 52.9
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deerdawn Com Authentication
  slug: deerdawn-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Deerdawn Com Domain Security
  slug: deerdawn-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Deerdawn Com Vulnerability Disclosure
  slug: deerdawn-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Deerdawn Com Trust Center
  slug: deerdawn-com-trust-center
  summary_line: SOC 2, GDPR
slug: deerdawn-com
tags:
- Artificial Intelligence
- Session Memory
- MCP
- Productivity
- Platform
- Company
website: https://deerdawn.com/
---
