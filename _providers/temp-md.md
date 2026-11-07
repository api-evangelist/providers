---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 8
  name: Temp Md Agentic Access
  operation_count: 50
  slug: temp-md-agentic-access
  summary_line: 50 operations · 33 acting · 8 human-in-the-loop
api_count: 2
apis:
- description: Hosted Streamable HTTP MCP server (serverInfo tempmd-remote 1.0.0, protocol 2025-06-18) exposing eight tools - publish_temp, update_temp, get_temp_status, restore_temp, snapshot_temp, set_comments, li
  name: temp.md MCP Server
  slug: tempmd-mcp-server
- description: 'A2A 1.0 agent ("temp.md Publisher") reachable over JSON-RPC at https://api.temp.md/a2a with three skills - publish-temp, update-temp, inspect-temp - and SendMessage / GetTask / ListTasks / CancelTask '
  name: temp.md A2A Publisher Agent
  slug: tempmd-a2a-publisher-agent
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Accounts API from temp.md — 5 operation(s) for accounts.
  name: temp.md Accounts API
  slug: temp-md-accounts-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Agents API from temp.md — 2 operation(s) for agents.
  name: temp.md Agents API
  slug: temp-md-agents-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Applications API from temp.md — 9 operation(s) for applications.
  name: temp.md Applications API
  slug: temp-md-applications-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Comments API from temp.md — 1 operation(s) for comments.
  name: temp.md Comments API
  slug: temp-md-comments-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Health API from temp.md — 1 operation(s) for health.
  name: temp.md Health API
  slug: temp-md-health-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Lifecycle API from temp.md — 5 operation(s) for lifecycle.
  name: temp.md Lifecycle API
  slug: temp-md-lifecycle-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Organizations API from temp.md — 3 operation(s) for organizations.
  name: temp.md Organizations API
  slug: temp-md-organizations-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Previews API from temp.md — 3 operation(s) for previews.
  name: temp.md Previews API
  slug: temp-md-previews-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Publish API from temp.md — 6 operation(s) for publish.
  name: temp.md Publish API
  slug: temp-md-publish-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Publish Grants API from temp.md — 2 operation(s) for publish grants.
  name: temp.md Publish Grants API
  slug: temp-md-publish-grants-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Publish Sessions API from temp.md — 1 operation(s) for publish sessions.
  name: temp.md Publish Sessions API
  slug: temp-md-publish-sessions-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Review Requests API from temp.md — 2 operation(s) for review requests.
  name: temp.md Review Requests API
  slug: temp-md-review-requests-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Safety API from temp.md — 1 operation(s) for safety.
  name: temp.md Safety API
  slug: temp-md-safety-api
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: The Usage API from temp.md — 1 operation(s) for usage.
  name: temp.md Usage API
  slug: temp-md-usage-api
artifact_total: 28
asyncapis:
- description: ''
  name: Temp Md Webhooks
  slug: temp-md-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://temp.md/blog/
- group: other
  href: https://artifacts.apis.io/temp-md/capabilities/temp-md-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/temp-md-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/temp-md/overlays/temp-md-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/temp-md-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://temp.md/
- group: docs
  title: ''
  type: Documentation
  url: https://temp.md/docs
- group: docs
  title: ''
  type: APIReference
  url: https://temp.md/docs#response
- group: start
  title: ''
  type: GettingStarted
  url: https://temp.md/docs#overview
- group: commercial
  title: ''
  type: Pricing
  url: https://temp.md/pricing.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://temp.md/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://temp.md/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tempmd
- group: start
  title: ''
  type: Login
  url: https://temp.md/dashboard
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ship_temp_md
- group: agent
  href: https://artifacts.apis.io/temp-md/llms/temp-md-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/temp-md-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://temp.md/llms.txt
- group: agent
  href: https://artifacts.apis.io/temp-md/well-known/temp-md-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/temp-md-well-known.yml
- group: other
  href: https://artifacts.apis.io/temp-md/a2a/temp-md-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/temp-md-a2a.yml
- group: agent
  href: https://artifacts.apis.io/temp-md/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/temp-md/skills/temp-md-tempmd-skill.md
  title: ''
  type: AgentSkill
  url: skills/temp-md-tempmd-skill.md
- group: agent
  href: https://artifacts.apis.io/temp-md/mcp/temp-md-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/temp-md-mcp.yml
- group: build
  href: https://artifacts.apis.io/temp-md/packages/temp-md-packages.yml
  title: ''
  type: Packages
  url: packages/temp-md-packages.yml
- group: build
  href: https://artifacts.apis.io/temp-md/packages/temp-md-packages.yml
  title: ''
  type: SDKs
  url: packages/temp-md-packages.yml
- group: build
  href: https://artifacts.apis.io/temp-md/cli/temp-md-cli.yml
  title: ''
  type: CLI
  url: cli/temp-md-cli.yml
- group: design
  href: https://artifacts.apis.io/temp-md/conventions/temp-md-conventions.yml
  title: ''
  type: Conventions
  url: conventions/temp-md-conventions.yml
- group: design
  href: https://artifacts.apis.io/temp-md/conventions/temp-md-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/temp-md-conventions.yml
- group: design
  href: https://artifacts.apis.io/temp-md/errors/temp-md-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/temp-md-problem-types.yml
- group: design
  href: https://artifacts.apis.io/temp-md/lifecycle/temp-md-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/temp-md-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/temp-md/conformance/temp-md-conformance.yml
  title: ''
  type: Conformance
  url: conformance/temp-md-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/temp-md/plans/temp-md-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/temp-md-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/temp-md/rate-limits/temp-md-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/temp-md-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/temp-md/changelog/temp-md-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/temp-md-changelog.yml
- group: auth
  href: https://artifacts.apis.io/temp-md/authentication/temp-md-authentication.yml
  title: ''
  type: Authentication
  url: authentication/temp-md-authentication.yml
- group: auth
  href: https://artifacts.apis.io/temp-md/security/temp-md-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/temp-md-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/temp-md/agentic-access/temp-md-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/temp-md-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/temp-md/regulatory/temp-md-regulatory-posture.yml
  title: ''
  type: NoticeAndAction
  url: regulatory/temp-md-regulatory-posture.yml
created: '2026-09-19'
description: 'temp.md is an instant web-publishing host built for AI agents: POST an HTML, Markdown, CSV or Mermaid file (or a multi-file bundle) and get a stable public URL like slug.temp.md that can be updated in place, snapshotted, password-protected, commented on and restored after expiry - no account or API key required to publish. The same publishing core is exposed as a REST API (OpenAPI 3.1), a hosted Streamable HTTP MCP server plus a stdio package, an A2A 1.0 agent, a CLI, and an Embedded Preview Platform API for products that publish previews on behalf of their own customers (delegated publish grants, signed webhooks, branded domains, review workflow).'
finops:
- has_sources: true
  method: derived
  name: Temp Md Finops
  primary_unit: ''
  service_category: ''
  slug: temp-md-finops
  template: true
image: https://temp.md/opengraph-image.png
layout: provider
mcp_servers:
- description: 'temp.md ships the same MCP server two ways: a hosted Streamable HTTP endpoint at https://api.temp.md/mcp that any MCP client can POST to with no credential (anonymous publishing), and a local stdio pa'
  name: temp.md MCP Server
  slug: tempmd-remote
modified: '2026-10-06'
name: temp.md
nav: Providers
network: true
overview: 'temp.md publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Agents API, Applications API, and 13 more. Tagged areas include Web Publishing, Static Hosting, AI Agents, MCP, and A2A.


  The temp.md catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  temp.md''s developer surface includes engineering blog, documentation, API reference, getting-started guide, pricing, CLI, changelog, and 28 more developer resources.'
plans:
- name: Temp Md Plans Pricing
  plan_count: 1
  slug: temp-md-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Temp Md Rate Limits
  slug: temp-md-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: temp.md API Rules
  rule_count: 57
  severity_counts:
    error: 43
    hint: 0
    info: 6
    warn: 8
  slug: temp-md-rules
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 55.3
    developer_ergonomics: 50.0
    discoverability: 75.0
    operational_transparency: 26.3
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 14
    mcp: first-party
    skills: first-party
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
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/temp-md/temp-md-2026-10-11T130747.png
security:
- kind: authentication
  name: Temp Md Authentication
  slug: temp-md-authentication
  summary_line: http · 7 schemes
- kind: domain-security
  name: Temp Md Domain Security
  slug: temp-md-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Account-owned publishing and update-token recovery
  slug: temp-md-account-owned-publishing
- name: Publish or update a directory with a resumable publish session
  slug: temp-md-publish-directory-with-sessions
- name: tempmd
  slug: temp-md-tempmd-skill
slug: temp-md
tags:
- Web Publishing
- Static Hosting
- AI Agents
- MCP
- A2A
- Developer Tools
- Preview Infrastructure
- File Sharing
- Agent-Native
- Company
website: https://temp.md/
---
