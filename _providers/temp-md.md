---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.0
  scored_at: '2026-09-20'
agentic_access:
- acting_count: 33
  human_in_the_loop: 8
  name: Temp Md Agentic Access
  operation_count: 50
  slug: temp-md-agentic-access
  summary_line: 50 operations · 33 acting · 8 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.temp.md
  baseurl_source: declared
  description: Publish agent-made files and applications to one canonical URL, update them atomically, and recover owner credentials without changing the shared link. 23 operations across Publish (multipart create/u
  name: temp.md Public API
  slug: tempmd-public-api
- baseURL: https://api.temp.md/v1
  baseurl_source: declared
  description: 'Versioned (/v1) partner API for products that create and govern previews on behalf of opaque end customers: Organizations and Applications, server-only Application keys, short-lived delegated publish '
  name: temp.md Embedded Preview Platform API
  slug: tempmd-embedded-preview-platform-api
- description: Hosted Streamable HTTP MCP server (serverInfo tempmd-remote 1.0.0, protocol 2025-06-18) exposing eight tools - publish_temp, update_temp, get_temp_status, restore_temp, snapshot_temp, set_comments, li
  name: temp.md MCP Server
  slug: tempmd-mcp-server
- description: 'A2A 1.0 agent ("temp.md Publisher") reachable over JSON-RPC at https://api.temp.md/a2a with three skills - publish-temp, update-temp, inspect-temp - and SendMessage / GetTask / ListTasks / CancelTask '
  name: temp.md A2A Publisher Agent
  slug: tempmd-a2a-publisher-agent
artifact_total: 11
asyncapis:
- description: ''
  name: Temp Md Webhooks
  slug: temp-md-webhooks
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/llms/temp-md-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/temp-md-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://temp.md/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/well-known/temp-md-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/temp-md-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/a2a/temp-md-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/temp-md-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/skills/temp-md-tempmd-skill.md
  title: ''
  type: AgentSkill
  url: skills/temp-md-tempmd-skill.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/mcp/temp-md-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/temp-md-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/packages/temp-md-packages.yml
  title: ''
  type: Packages
  url: packages/temp-md-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/packages/temp-md-packages.yml
  title: ''
  type: SDKs
  url: packages/temp-md-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/cli/temp-md-cli.yml
  title: ''
  type: CLI
  url: cli/temp-md-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/conventions/temp-md-conventions.yml
  title: ''
  type: Conventions
  url: conventions/temp-md-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/conventions/temp-md-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/temp-md-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/errors/temp-md-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/temp-md-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/lifecycle/temp-md-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/temp-md-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/conformance/temp-md-conformance.yml
  title: ''
  type: Conformance
  url: conformance/temp-md-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/plans/temp-md-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/temp-md-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/rate-limits/temp-md-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/temp-md-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/changelog/temp-md-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/temp-md-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/authentication/temp-md-authentication.yml
  title: ''
  type: Authentication
  url: authentication/temp-md-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/security/temp-md-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/temp-md-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/agentic-access/temp-md-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/temp-md-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/temp-md/refs/heads/main/regulatory/temp-md-regulatory-posture.yml
  title: ''
  type: NoticeAndAction
  url: regulatory/temp-md-regulatory-posture.yml
created: '2026-09-19'
description: 'temp.md is an instant web-publishing host built for AI agents: POST an HTML, Markdown, CSV or Mermaid file (or a multi-file bundle) and get a stable public URL like slug.temp.md that can be updated in place, snapshotted, password-protected, commented on and restored after expiry - no account or API key required to publish. The same publishing core is exposed as a REST API (OpenAPI 3.1), a hosted Streamable HTTP MCP server plus a stdio package, an A2A 1.0 agent, a CLI, and an Embedded Preview Platform API for products that publish previews on behalf of their own customers (delegated publish grants, signed webhooks, branded domains, review workflow).'
image: https://temp.md/opengraph-image.png
layout: provider
mcp_servers:
- description: 'temp.md ships the same MCP server two ways: a hosted Streamable HTTP endpoint at https://api.temp.md/mcp that any MCP client can POST to with no credential (anonymous publishing), and a local stdio pa'
  name: temp.md MCP Server
  slug: tempmd-mcp-server
modified: '2026-09-19'
name: temp.md
nav: Providers
network: true
overview: 'temp.md publishes 2 APIs on the [APIs.io](https://apis.io/) network: Public API and Embedded Preview Platform API. Tagged areas include Web Publishing, Static Hosting, AI Agents, MCP, and A2A.


  The temp.md catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  temp.md''s developer surface includes documentation, API reference, getting-started guide, pricing, CLI, changelog, authentication, and 25 more developer resources.'
plans:
- name: Temp Md Plans Pricing
  plan_count: 1
  slug: temp-md-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Temp Md Rate Limits
  slug: temp-md-rate-limits
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 52.1
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 57.4
    developer_ergonomics: 61.9
    discoverability: 75.9
    operational_transparency: 28.9
  previous_composite: 2.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Temp Md Authentication
  slug: temp-md-authentication
  summary_line: http · 7 schemes
- kind: domain-security
  name: Temp Md Domain Security
  slug: temp-md-domain-security
  summary_line: TLSv1.3 · DMARC
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
- agent-native
- Company
website: https://temp.md/
---
