---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Zambo Dev Agentic Access
  operation_count: 35
  slug: zambo-dev-agentic-access
  summary_line: 35 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: Full endpoint catalog
  name: zambo-dev Capabilities API
  slug: zambo-dev-capabilities-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: The Day Pass API from zambo-dev — 1 operation(s) for day pass.
  name: zambo-dev Day Pass API
  slug: zambo-dev-day-pass-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: Agent and capability discovery, routing, traction data
  name: zambo-dev Discovery API
  slug: zambo-dev-discovery-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: Crawl telemetry and discoverability endpoints
  name: zambo-dev GEO API
  slug: zambo-dev-geo-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: The Handover API from zambo-dev — 6 operation(s) for handover.
  name: zambo-dev Handover API
  slug: zambo-dev-handover-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: AI code audit with Provibe Score
  name: zambo-dev Provibe Code API
  slug: zambo-dev-provibecode-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: The Today API from zambo-dev — 3 operation(s) for today.
  name: zambo-dev Today API
  slug: zambo-dev-today-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: Universal routing endpoint - one call, all products
  name: zambo-dev Universal API
  slug: zambo-dev-universal-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: The Zambo API from zambo-dev — 1 operation(s) for zambo.
  name: zambo-dev Zambo API
  slug: zambo-dev-zambo-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: Agent Evolution Engine - swarm wisdom sparks
  name: zambo-dev ZAMBOT API
  slug: zambo-dev-zambot-api
- baseURL: https://zambo.dev
  baseurl_source: declared
  description: Opportunity scanner and builder intelligence
  name: zambo-dev ZAMBRO API
  slug: zambo-dev-zambro-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/zambo-dev/agentic-access/zambo-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zambo-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/zambo-dev/plans/zambo-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zambo-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zambo-dev/rules/zambo-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/zambo-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/zambo-dev/json-ld/zambo-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zambo-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/zambo-dev/vocabulary/zambo-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zambo-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/zambo-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/zambo-dev/data-model/zambo-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zambo-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/zambo-dev/cli/zambo-dev-cli.yml
  title: ''
  type: CLI
  url: cli/zambo-dev-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://zambo.dev/security
- group: design
  href: https://artifacts.apis.io/zambo-dev/lifecycle/zambo-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zambo-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/zambo-dev/errors/zambo-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zambo-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zambo-dev/conformance/zambo-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zambo-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zambo-dev/llms/zambo-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zambo-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/zambo-dev/a2a/zambo-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zambo-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/zambo-dev/mcp/zambo-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zambo-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/zambo-dev/well-known/zambo-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zambo-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/zambo-dev/well-known/zambo-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zambo-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/zambo-dev/hosts/zambo-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zambo-dev-hosts.yml
- group: build
  href: https://artifacts.apis.io/zambo-dev/packages/zambo-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/zambo-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/zambo-dev/packages/zambo-dev-packages.yml
  title: ''
  type: Packages
  url: packages/zambo-dev-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://zambo.dev/status/
- group: auth
  title: ''
  type: Security
  url: https://zambo.dev/security/
- group: company
  title: ''
  type: Newsroom
  url: https://zambo.dev/press/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zambo.dev/developers/
- group: operate
  title: ''
  type: ChangeLog
  url: https://zambo.dev/changelog/
- group: auth
  href: https://artifacts.apis.io/zambo-dev/security/zambo-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zambo-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zambo-dev/security/zambo-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zambo-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zambo-dev/security/zambo-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zambo-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zambo.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://zambo.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://zambo.dev/api
- group: operate
  title: ''
  type: Support
  url: https://zambo.dev/support
- group: company
  title: ''
  type: Blog
  url: https://zambo.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://zambo.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zambo.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zambo.dev/privacy
created: '2026-10-30'
description: Zambo provides a verifiable work layer for AI, offering a hosted MCP server with no API key, 153 live tools, and a verifiable trust layer. Founded by Brennan Zambo, the platform aims to simplify AI tool integration, ensure data provenance, and enable secure, auditable workflows for developers and enterprises alike.
image: https://zambo.dev/images/og-founder.png
jsonld:
- class_count: 1
  name: Zambo Dev Context
  property_count: 7
  slug: zambo-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at zambo.dev.
  name: zambo-dev MCP Server
  slug: zambo-dev-mcp-yml
modified: '2026-10-30'
name: zambo-dev
nav: Providers
network: true
overview: 'zambo-dev publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Capabilities API, Day Pass API, Discovery API, and 8 more. Tagged areas include Company, AI, TrustLayer, MCP, and Platform.


  The zambo-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  zambo-dev''s developer surface includes CLI, changelog, documentation, API reference, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Zambo Dev Plans Pricing
  plan_count: 4
  slug: zambo-dev-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: zambo-dev API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: zambo-dev-rules
score:
  band: strong
  composite: 58.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 59.8
    catalog_earned_first_party: 12.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 49.5
    developer_ergonomics: 66.0
    discoverability: 66.7
    operational_transparency: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zambo Dev Authentication
  slug: zambo-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Zambo Dev Domain Security
  slug: zambo-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zambo Dev Vulnerability Disclosure
  slug: zambo-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Zambo Dev Trust Center
  slug: zambo-dev-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: capability-search
  slug: zambo-dev-capability-search
slug: zambo-dev
tags:
- Company
- AI
- TrustLayer
- MCP
- Platform
website: https://zambo.dev/
---
