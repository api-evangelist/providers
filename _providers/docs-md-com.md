---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Docs Md Com Agentic Access
  operation_count: 4
  slug: docs-md-com-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- description: Publish markdown and get a rendered link via the Docs MD API.
  name: Docs MD Share API
  slug: docs-md-share-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/docs-md-com/agentic-access/docs-md-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/docs-md-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/docs-md-com/rate-limits/docs-md-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/docs-md-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/docs-md-com/rules/docs-md-com-rules.yml
  title: ''
  type: Spectral
  url: rules/docs-md-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/docs-md-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/docs-md-com/errors/docs-md-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/docs-md-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/docs-md-com/conformance/docs-md-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docs-md-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docs-md-com/llms/docs-md-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docs-md-com-llms.txt
- group: build
  href: https://artifacts.apis.io/docs-md-com/mcp/docs-md-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/docs-md-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/docs-md-com/mcp/docs-md-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docs-md-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/docs-md-com/hosts/docs-md-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docs-md-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/docs-md-com/vendors/docs-md-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docs-md-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/docs-md-com/security/docs-md-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docs-md-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs-md.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs-md.com/about
- group: docs
  title: ''
  type: APIReference
  url: https://docs-md.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs-md.com/what-is-mcp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs-md.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs-md.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/invisible-hand/docs-md.com
created: '2026-10-30'
description: Docs MD provides a free markdown sharing service tailored for AI‑powered workflows. Users can paste a Markdown file and receive a rendered link that supports Mermaid diagrams, syntax‑highlighted code, and configurable expiry periods (day, week, month, or permanent). The platform also offers an MCP server enabling AI agents like Cursor and Claude Code to programmatically create shares via a REST API, plus a suite of free markdown tools. No signup is required.
image: https://docs-md.com/logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at docs-md.com.
  name: docs-md-com MCP Server
  slug: docs-md-com-mcp-yml
modified: '2026-10-30'
name: docs-md-com
nav: Providers
network: true
overview: 'docs-md-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Markdown, AI, MCP, Sharing, and Free.


  The docs-md-com catalog on APIs.io includes 1 Spectral governance ruleset.


  docs-md-com''s developer surface includes documentation, API reference, getting-started guide, and 16 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 2
  name: Docs Md Com Rate Limits
  slug: docs-md-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: docs-md-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: docs-md-com-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.4
    catalog_earned_first_party: 0.0
    catalog_gap: 54.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 65.5
    contract_quality: 0.0
    developer_ergonomics: 35.0
    discoverability: 65.0
    operational_transparency: 24.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docs Md Com Domain Security
  slug: docs-md-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: delete-share
  slug: docs-md-com-delete-share
- name: read-share
  slug: docs-md-com-read-share
- name: share-markdown
  slug: docs-md-com-share-markdown
- name: update-share
  slug: docs-md-com-update-share
slug: docs-md-com
tags:
- Markdown
- AI
- MCP
- Sharing
- Free
website: https://docs-md.com/
---
