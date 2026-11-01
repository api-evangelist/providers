---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lazyweb Com Agentic Access
  operation_count: 13
  slug: lazyweb-com-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 3
apis:
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Antigravity.md API from lazyweb-com — 1 operation(s) for antigravity.md.
  name: lazyweb-com Antigravity.md API
  slug: lazyweb-com-antigravity-md-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Chatgpt.md API from lazyweb-com — 1 operation(s) for chatgpt.md.
  name: lazyweb-com Chatgpt.md API
  slug: lazyweb-com-chatgpt-md-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Claude.md API from lazyweb-com — 1 operation(s) for claude.md.
  name: lazyweb-com Claude.md API
  slug: lazyweb-com-claude-md-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Codex.md API from lazyweb-com — 1 operation(s) for codex.md.
  name: lazyweb-com Codex.md API
  slug: lazyweb-com-codex-md-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Cursor.md API from lazyweb-com — 1 operation(s) for cursor.md.
  name: lazyweb-com Cursor.md API
  slug: lazyweb-com-cursor-md-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Index.md API from lazyweb-com — 1 operation(s) for index.md.
  name: lazyweb-com Index.md API
  slug: lazyweb-com-index-md-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Install.sh API from lazyweb-com — 1 operation(s) for install.sh.
  name: lazyweb-com Install.sh API
  slug: lazyweb-com-install-sh-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Mcp API from lazyweb-com — 2 operation(s) for mcp.
  name: lazyweb-com MCP API
  slug: lazyweb-com-mcp-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Pricing.md API from lazyweb-com — 1 operation(s) for pricing.md.
  name: lazyweb-com Pricing.md API
  slug: lazyweb-com-pricing-md-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The Use Lazyweb.md API from lazyweb-com — 1 operation(s) for use lazyweb.md.
  name: lazyweb-com Use Lazyweb.md API
  slug: lazyweb-com-use-lazyweb-md-api
- baseURL: https://www.lazyweb.com
  baseurl_source: declared
  description: The .well Known API from lazyweb-com — 2 operation(s) for .well known.
  name: lazyweb-com .well Known API
  slug: lazyweb-com-well-known-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/lazyweb-com/agentic-access/lazyweb-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lazyweb-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/lazyweb-com/plans/lazyweb-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lazyweb-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lazyweb-com/rules/lazyweb-com-rules.yml
  title: ''
  type: Spectral
  url: rules/lazyweb-com-rules.yml
- group: design
  href: https://artifacts.apis.io/lazyweb-com/json-ld/lazyweb-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lazyweb-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/lazyweb-com/vocabulary/lazyweb-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lazyweb-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lazyweb-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lazyweb-com/data-model/lazyweb-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lazyweb-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/lazyweb-com/authentication/lazyweb-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lazyweb-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/lazyweb-com/errors/lazyweb-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lazyweb-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lazyweb-com/conformance/lazyweb-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lazyweb-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lazyweb-com/llms/lazyweb-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lazyweb-com-llms.txt
- group: build
  href: https://artifacts.apis.io/lazyweb-com/mcp/lazyweb-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lazyweb-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lazyweb-com/mcp/lazyweb-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lazyweb-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lazyweb-com/well-known/lazyweb-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lazyweb-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/lazyweb-com/hosts/lazyweb-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lazyweb-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lazyweb-com/vendors/lazyweb-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lazyweb-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lazyweb.com/company/category/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.lazyweb.com/company/category/news
- group: start
  title: ''
  type: Login
  url: https://www.lazyweb.com/inspiration/login
- group: docs
  title: ''
  type: APIReference
  url: https://www.lazyweb.com/openapi.json
- group: auth
  href: https://artifacts.apis.io/lazyweb-com/security/lazyweb-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lazyweb-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lazyweb.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lazyweb.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lazyweb.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lazyweb.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.lazyweb.com/support
created: '2026-10-30'
description: Lazyweb provides an AI‑driven product growth platform that automates experimentation, data‑driven insights, and revenue optimization for SaaS companies. The service offers a free starter tier, integrates with popular tools, and showcases case studies from brands like Duolingo, Dropbox, and Airbnb. It positions itself as a no‑code solution for rapid growth testing and continuous optimization, with a public API for accessing growth metrics and experiment results.
json_schemas:
- name: McpInstallTokenResponse
  property_count: 0
  slug: lazyweb-com-mcp-install-token-response
jsonld:
- class_count: 1
  name: Lazyweb Com Context
  property_count: 3
  slug: lazyweb-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.lazyweb.com.
  name: lazyweb-com MCP Server
  slug: lazyweb-com-mcp-yml
modified: '2026-10-30'
name: lazyweb-com
nav: Providers
network: true
overview: 'lazyweb-com publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Antigravity.md API, Chatgpt.md API, Claude.md API, and 8 more. Tagged areas include Company, SaaS, Growth, AI, and No-code.


  The lazyweb-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  lazyweb-com''s developer surface includes authentication, API reference, pricing, support, and 22 more developer resources.'
plans:
- name: Lazyweb Com Plans Pricing
  plan_count: 3
  slug: lazyweb-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Lazyweb Com Rate Limits
  slug: lazyweb-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: lazyweb-com API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: lazyweb-com-rules
scopes:
- name: Lazyweb Com Scopes
  scope_count: 0
  slug: lazyweb-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 66.2
    catalog_earned_first_party: 12.0
    catalog_gap: 48.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 48.5
    developer_ergonomics: 25.6
    discoverability: 68.3
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lazyweb Com Authentication
  slug: lazyweb-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Lazyweb Com Domain Security
  slug: lazyweb-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 10
skills:
- name: lazyweb-com-create-token-and-call-mcp
  slug: lazyweb-com-create-token-and-call-mcp
- name: lazyweb-growth-backlog
  slug: lazyweb-com-lazyweb-growth-backlog
- name: lazyweb-growth-report
  slug: lazyweb-com-lazyweb-growth-report
- name: lazyweb-growth-score
  slug: lazyweb-com-lazyweb-growth-score
- name: lazyweb-search-experiments
  slug: lazyweb-com-lazyweb-search-experiments
- name: lazyweb-search-flows
  slug: lazyweb-com-lazyweb-search-flows
- name: lazyweb-search-screens
  slug: lazyweb-com-lazyweb-search-screens
- name: lazyweb-update
  slug: lazyweb-com-lazyweb-update
- name: lazyweb
  slug: lazyweb-com-lazyweb
- name: lazyweb-com-search-and-tldr
  slug: lazyweb-com-search-and-tldr
slug: lazyweb-com
tags:
- Company
- SaaS
- Growth
- AI
- No-code
website: https://lazyweb.com/
---
