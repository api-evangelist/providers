---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provides an MCP gateway with API key authentication as described in the documentation.
  name: MCPifex API
  slug: mcpifex-api-2
- description: 'Amdose API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Amdose API
  slug: mcpifex-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/mcpifex/plans/mcpifex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mcpifex-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mcpifex/rules/mcpifex-rules.yml
  title: ''
  type: Spectral
  url: rules/mcpifex-rules.yml
- group: design
  href: https://artifacts.apis.io/mcpifex/json-ld/mcpifex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mcpifex-context.jsonld
- group: design
  href: https://artifacts.apis.io/mcpifex/vocabulary/mcpifex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mcpifex-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mcpifex/data-model/mcpifex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mcpifex-data-model.yml
- group: auth
  href: https://artifacts.apis.io/mcpifex/authentication/mcpifex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mcpifex-authentication.yml
- group: design
  href: https://artifacts.apis.io/mcpifex/conformance/mcpifex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mcpifex-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mcpifex/llms/mcpifex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mcpifex-llms.txt
- group: other
  href: https://artifacts.apis.io/mcpifex/hosts/mcpifex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcpifex-hosts.yml
- group: other
  href: https://artifacts.apis.io/mcpifex/vendors/mcpifex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mcpifex-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/McpiFex
- group: auth
  href: https://artifacts.apis.io/mcpifex/security/mcpifex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcpifex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcpifex.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.mcpifex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mcpifex.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://mcpifex.com/docs/api-keys-and-authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://mcpifex.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://mcpifex.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://mcpifex.com/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://portal.mcpifex.com/en/auth/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mcpifex.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcpifex.com/privacy.html
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI or other machine‑readable contract was found despite public documentation.
  evidence:
  - status: 0
    url: https://api.mcpifex.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Amdose, operating as MCPifex, provides a hosted MCP server marketplace and gateway that consolidates multiple tool integrations into a single endpoint. It offers a registry of MCP servers with detailed capabilities, pricing plans, and documentation, enabling AI agents to connect to various data sources securely and efficiently. The platform emphasizes scoped keys, easy configuration, and comprehensive monitoring for AI-driven workflows.
image: https://mcpifex.com/og.png
json_schemas:
- name: PostMcpRequest
  property_count: 4
  slug: mcpifex-post-mcp-request
jsonld:
- class_count: 1
  name: Mcpifex Context
  property_count: 4
  slug: mcpifex-context
layout: provider
modified: '2026-10-18'
name: Amdose
nav: Providers
network: true
overview: 'Amdose is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Marketplace, AI Agents, and Integration.


  The Amdose catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amdose''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Mcpifex Plans Pricing
  plan_count: 3
  slug: mcpifex-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Amdose API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: mcpifex-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 18.6
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 40.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mcpifex Authentication
  slug: mcpifex-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mcpifex Domain Security
  slug: mcpifex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mcpifex
tags:
- Company
- MCP
- Marketplace
- AI Agents
- Integration
website: https://mcpifex.com/
---
