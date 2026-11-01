---
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: MCP (Machine-Callable Protocol) endpoint providing tools for prompt compression.
  name: SuperCompress MCP
  slug: supercompress-mcp
- baseURL: https://supercompress.dev
  baseurl_source: declared
  description: 'supercompress-dev API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: supercompress-dev API
  slug: supercompress-dev-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/supercompress-dev/rules/supercompress-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/supercompress-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/supercompress-dev/json-ld/supercompress-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/supercompress-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/supercompress-dev/vocabulary/supercompress-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/supercompress-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/supercompress-dev/data-model/supercompress-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/supercompress-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/supercompress-dev/cli/supercompress-dev-cli.yml
  title: ''
  type: CLI
  url: cli/supercompress-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/supercompress-dev/changelog/supercompress-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/supercompress-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/supercompress-dev/authentication/supercompress-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/supercompress-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/supercompress-dev/lifecycle/supercompress-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/supercompress-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/supercompress-dev/errors/supercompress-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/supercompress-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/supercompress-dev/conformance/supercompress-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/supercompress-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/supercompress-dev/llms/supercompress-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/supercompress-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/supercompress-dev/mcp/supercompress-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/supercompress-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/supercompress-dev/well-known/supercompress-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/supercompress-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/supercompress-dev/hosts/supercompress-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/supercompress-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/supercompress-dev/vendors/supercompress-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/supercompress-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/supercompress-dev/packages/supercompress-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/supercompress-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/supercompress-dev/packages/supercompress-dev-packages.yml
  title: ''
  type: Packages
  url: packages/supercompress-dev-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.supercompress.dev/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.supercompress.dev/changelog
- group: auth
  href: https://artifacts.apis.io/supercompress-dev/security/supercompress-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/supercompress-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.supercompress.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supercompress.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.supercompress.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.supercompress.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.supercompress.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Supercompress
- group: commercial
  title: ''
  type: Pricing
  url: https://www.supercompress.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.supercompress.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.supercompress.dev/privacy
created: '2026-10-31'
description: SuperCompress provides a cutting‑edge API that compresses prompts for large language models, reducing token usage and cost by up to 65 %. It enables developers to integrate context compression into chatbots, AI search, RAG pipelines, and agent workflows, offering a free tier of 1 M tokens per month and transparent pricing thereafter. The service runs on a secure, scalable platform and includes detailed documentation, quick‑start guides, and SDKs for easy adoption.
image: https://supercompress.dev/assets/img/og-image-v4.png
json_schemas:
- name: GetCompressResponse
  property_count: 10
  slug: supercompress-dev-get-compress-response
- name: PostApiV1CompressRequest
  property_count: 3
  slug: supercompress-dev-post-api-v1-compress-request
- name: PostApiV1CompressResponse
  property_count: 10
  slug: supercompress-dev-post-api-v1-compress-response
- name: PostCompressRequest
  property_count: 2
  slug: supercompress-dev-post-compress-request
- name: PostCompressResponse
  property_count: 10
  slug: supercompress-dev-post-compress-response
jsonld:
- class_count: 5
  name: Supercompress Dev Context
  property_count: 13
  slug: supercompress-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.supercompress.dev requiring OAuth.
  name: supercompress-dev MCP Server
  slug: supercompress-dev-mcp-yml
modified: '2026-10-31'
name: supercompress-dev
nav: Providers
network: true
overview: 'supercompress-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include LLM, Compression, API, Cost-Reduction, and AI.


  The supercompress-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  supercompress-dev''s developer surface includes CLI, changelog, authentication, sandbox, documentation, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Supercompress Dev Plans Pricing
  plan_count: 0
  slug: supercompress-dev-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Supercompress Dev Rate Limits
  slug: supercompress-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: supercompress-dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: supercompress-dev-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 55.9
    developer_ergonomics: 64.3
    discoverability: 65.0
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Supercompress Dev Authentication
  slug: supercompress-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Supercompress Dev Domain Security
  slug: supercompress-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: supercompress-dev
tags:
- LLM
- Compression
- API
- Cost-Reduction
- AI
- DeveloperTools
website: https://www.supercompress.dev/
---
