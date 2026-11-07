---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AgentDocs API provides REST endpoints for managing workspaces, spaces, pages, and more.
  name: AgentDocs API
  slug: agentdocs-api
- description: 'agentdocs-eu API as documented publicly: 62 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: agentdocs-eu API
  slug: agentdocs-eu-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/agentdocs-eu/rate-limits/agentdocs-eu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentdocs-eu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentdocs-eu/plans/agentdocs-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentdocs-eu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentdocs-eu/rules/agentdocs-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/agentdocs-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/agentdocs-eu/json-ld/agentdocs-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentdocs-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentdocs-eu/vocabulary/agentdocs-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentdocs-eu-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentdocs-eu/data-model/agentdocs-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentdocs-eu-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agentdocs-eu/security/agentdocs-eu-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentdocs-eu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentdocs-eu/authentication/agentdocs-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentdocs-eu-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentdocs-eu/errors/agentdocs-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentdocs-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentdocs-eu/conformance/agentdocs-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdocs-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentdocs-eu/llms/agentdocs-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdocs-eu-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentdocs-eu/mcp/agentdocs-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentdocs-eu-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentdocs-eu/well-known/agentdocs-eu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentdocs-eu-security.txt
- group: agent
  href: https://artifacts.apis.io/agentdocs-eu/well-known/agentdocs-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentdocs-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentdocs-eu/hosts/agentdocs-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentdocs-eu-hosts.yml
- group: build
  href: https://artifacts.apis.io/agentdocs-eu/packages/agentdocs-eu-packages.yml
  title: ''
  type: SDKs
  url: packages/agentdocs-eu-packages.yml
- group: build
  href: https://artifacts.apis.io/agentdocs-eu/packages/agentdocs-eu-packages.yml
  title: ''
  type: Packages
  url: packages/agentdocs-eu-packages.yml
- group: start
  title: ''
  type: Login
  url: https://agentdocs.eu/login
- group: auth
  href: https://artifacts.apis.io/agentdocs-eu/security/agentdocs-eu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentdocs-eu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentdocs-eu/security/agentdocs-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdocs-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentdocs.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://agentdocs.eu/docs
- group: company
  title: ''
  type: Blog
  url: https://agentdocs.eu/blog
- group: operate
  title: ''
  type: Support
  url: https://agentdocs.eu/support
- group: commercial
  title: ''
  type: Pricing
  url: https://agentdocs.eu/pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://agentdocs.eu/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentdocs.eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentdocs.eu/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://agentdocs.eu/register
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentdocs.eu/docs
coverage:
  checked: '2026-10-30'
  detail: The public API documentation lists endpoints but provides no OpenAPI or other machine-readable spec.
  evidence:
  - status: 200
    url: https://agentdocs.eu/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: AgentDocs is a collaborative documentation platform designed for AI agents and humans. It offers a markdown editor, shareable links, and a full REST API that enables agents to read, write, search, and manage docs programmatically. The service provides a free tier, supports project kits, and integrates with an MCP server for agent-driven workflows, fostering seamless human‑agent collaboration across teams.
image: https://agentdocs.eu/og-image.png
json_schemas:
- name: PostApiAuthRegenerateTokenResponse
  property_count: 1
  slug: agentdocs-eu-post-api-auth-regenerate-token-response
- name: PostApiSpacesSpaceidImportMarkdownRequest
  property_count: 1
  slug: agentdocs-eu-post-api-spaces-spaceid-import-markdown-request
- name: PostApiSpacesSpaceidImportMarkdownResponse
  property_count: 1
  slug: agentdocs-eu-post-api-spaces-spaceid-import-markdown-response
jsonld:
- class_count: 3
  name: Agentdocs Eu Context
  property_count: 3
  slug: agentdocs-eu-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentdocs.eu.
  name: agentdocs-eu MCP Server
  slug: agentdocs-eu-mcp-yml
modified: '2026-10-30'
name: agentdocs-eu
nav: Providers
network: true
overview: 'agentdocs-eu is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Documentation, Artificial Intelligence, Platform, and Open Source.


  The agentdocs-eu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agentdocs-eu''s developer surface includes authentication, documentation, engineering blog, support, pricing, getting-started guide, and 24 more developer resources.'
plans:
- name: Agentdocs Eu Plans Pricing
  plan_count: 2
  slug: agentdocs-eu-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Agentdocs Eu Rate Limits
  slug: agentdocs-eu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: agentdocs-eu API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: agentdocs-eu-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 71.0
    catalog_earned_first_party: 20.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 43.4
    contract_governance: 19.7
    contract_quality: 20.1
    developer_ergonomics: 38.1
    discoverability: 56.7
    operational_transparency: 44.7
  previous_composite: 45.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agentdocs-eu/agentdocs-eu-2026-11-03T120354.png
security:
- kind: authentication
  name: Agentdocs Eu Authentication
  slug: agentdocs-eu-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agentdocs Eu Domain Security
  slug: agentdocs-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentdocs Eu Vulnerability Disclosure
  slug: agentdocs-eu-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentdocs-eu
tags:
- Collaboration
- Documentation
- Artificial Intelligence
- Platform
- Open Source
- Company
website: https://agentdocs.eu/
---
