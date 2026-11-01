---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Keenable Agentic Access
  operation_count: 4
  slug: keenable-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.keenable.ai
  baseurl_source: declared
  description: The Fetch API from Keenable — 2 operation(s) for fetch.
  name: Keenable Fetch API
  slug: keenable-fetch-api
- baseURL: https://api.keenable.ai
  baseurl_source: declared
  description: The Search API from Keenable — 2 operation(s) for search.
  name: Keenable Search API
  slug: keenable-search-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/keenable/vendors/keenable-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keenable-vendors.yml
- group: agent
  href: https://artifacts.apis.io/keenable/agentic-access/keenable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/keenable-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/keenable/rate-limits/keenable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/keenable-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/keenable/plans/keenable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/keenable-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/keenable/rules/keenable-rules.yml
  title: ''
  type: Spectral
  url: rules/keenable-rules.yml
- group: design
  href: https://artifacts.apis.io/keenable/json-ld/keenable-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/keenable-context.jsonld
- group: design
  href: https://artifacts.apis.io/keenable/vocabulary/keenable-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/keenable-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/keenable/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/keenable/data-model/keenable-data-model.yml
  title: ''
  type: DataModel
  url: data-model/keenable-data-model.yml
- group: build
  href: https://artifacts.apis.io/keenable/cli/keenable-cli.yml
  title: ''
  type: CLI
  url: cli/keenable-cli.yml
- group: operate
  href: https://artifacts.apis.io/keenable/changelog/keenable-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/keenable-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://app.keenable.ai/security.md
- group: auth
  href: https://artifacts.apis.io/keenable/authentication/keenable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keenable-authentication.yml
- group: design
  href: https://artifacts.apis.io/keenable/errors/keenable-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/keenable-problem-types.yml
- group: design
  href: https://artifacts.apis.io/keenable/conformance/keenable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keenable-conformance.yml
- group: agent
  href: https://artifacts.apis.io/keenable/llms/keenable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keenable-llms.txt
- group: other
  href: https://artifacts.apis.io/keenable/a2a/keenable-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/keenable-a2a.yml
- group: build
  href: https://artifacts.apis.io/keenable/mcp/keenable-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/keenable-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/keenable/mcp/keenable-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/keenable-mcp.yml
- group: auth
  href: https://artifacts.apis.io/keenable/well-known/keenable-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/keenable-security.txt
- group: auth
  href: https://artifacts.apis.io/keenable/well-known/keenable-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/keenable-app-security.txt
- group: agent
  href: https://artifacts.apis.io/keenable/well-known/keenable-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/keenable-well-known.yml
- group: other
  href: https://artifacts.apis.io/keenable/hosts/keenable-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keenable-hosts.yml
- group: build
  href: https://artifacts.apis.io/keenable/packages/keenable-packages.yml
  title: ''
  type: SDKs
  url: packages/keenable-packages.yml
- group: build
  href: https://artifacts.apis.io/keenable/packages/keenable-packages.yml
  title: ''
  type: Packages
  url: packages/keenable-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.keenable.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://keenable.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.keenable.ai
- group: start
  title: ''
  type: SignUp
  url: https://keenable.ai/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keenable.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://keenable.ai/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keenableai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.keenable.ai/changelog
- group: company
  title: ''
  type: Blog
  url: https://keenable.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.keenable.ai/index
- group: docs
  title: ''
  type: Documentation
  url: https://docs.keenable.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.keenable.ai/api-reference
- group: auth
  href: https://artifacts.apis.io/keenable/security/keenable-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/keenable-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/keenable/security/keenable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keenable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keenable.ai/
created: '2026-10-24'
description: Keenable provides an independent web‑search API that AI agents and AI labs can integrate to retrieve up‑to‑date web content. The service offers a self‑serve storefront where agents can purchase access at $4 / 1 000 requests for enthusiasts or $1 / 1 000 requests at 100 RPS+ for frontier AI labs, with cloud‑only or on‑premises deployment options. It supports point‑in‑time searches across historical snapshots and handles payment without requiring direct API calls.
image: https://framerusercontent.com/images/BzWtoTW95sFebOcWSEVTOtnpm4.png
json_schemas:
- name: FetchResponse
  property_count: 6
  slug: keenable-fetch-response
- name: SearchRequest
  property_count: 10
  slug: keenable-search-request
- name: SearchResponse
  property_count: 3
  slug: keenable-search-response
jsonld:
- class_count: 6
  name: Keenable Context
  property_count: 22
  slug: keenable-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.keenable.ai.
  name: Keenable MCP Server
  slug: keenable-mcp-yml
modified: '2026-10-24'
name: Keenable
nav: Providers
network: true
overview: 'Keenable publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Fetch API and Search API. Tagged areas include Web Search, API, AI Agents, AI Labs, and Inference Platforms.


  The Keenable catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Keenable''s developer surface includes CLI, changelog, authentication, signup flow, pricing, engineering blog, getting-started guide, and 33 more developer resources.'
plans:
- name: Keenable Plans Pricing
  plan_count: 3
  slug: keenable-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 6
  name: Keenable Rate Limits
  slug: keenable-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Keenable API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: keenable-rules
score:
  band: exemplar
  composite: 66.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 62.3
    developer_ergonomics: 58.9
    discoverability: 65.0
    operational_transparency: 78.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Keenable Authentication
  slug: keenable-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Keenable Domain Security
  slug: keenable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Keenable Vulnerability Disclosure
  slug: keenable-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: keenable-search-web
  slug: keenable-search-web
slug: keenable
tags:
- Web Search
- API
- AI Agents
- AI Labs
- Inference Platforms
website: https://keenable.ai/
---
