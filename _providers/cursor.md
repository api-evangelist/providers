---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Cursor Agentic Access
  operation_count: 17
  slug: cursor-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 10
apis:
- description: 'Programmatic access to team data: members, usage metrics, spending, repository blocklists, daily/filtered usage events. Available to Enterprise teams. Uses HTTP Basic auth with API key as username.'
  name: Cursor Admin API
  slug: admin
- description: Usage insights, AI metrics, and model usage stats for Enterprise teams.
  name: Cursor Analytics API
  slug: analytics
- description: Track AI-generated code at the commit level for Enterprise teams.
  name: Cursor AI Code Tracking API
  slug: ai-code-tracking
- description: Create and manage AI coding agents in the cloud. Beta, available across all plans.
  name: Cursor Cloud Agents API
  slug: cloud-agents
- description: Retrieve security and configuration audit events
  name: Cursor Audit Logs API
  slug: cursor-audit-logs-api
- description: Billing groups for cost allocation
  name: Cursor Groups API
  slug: cursor-groups-api
- description: Manage team members
  name: Cursor Members API
  slug: cursor-members-api
- description: Repository indexing blocklist configuration
  name: Cursor Repo Blocklists API
  slug: cursor-repo-blocklists-api
- description: Spending data and per-user spend limits
  name: Cursor Spend API
  slug: cursor-spend-api
- description: Daily usage and granular usage event data
  name: Cursor Usage API
  slug: cursor-usage-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cursor Admin API
  slug: open-cursor-admin-api
- collection_type: open
  name: Cursor Admin Audit Logs API
  slug: open-cursor-audit-logs-api
- collection_type: open
  name: Cursor Admin Audit Logs Groups API
  slug: open-cursor-groups-api
- collection_type: open
  name: Cursor Admin Audit Logs Members API
  slug: open-cursor-members-api
- collection_type: open
  name: Cursor Admin Audit Logs Repo Blocklists API
  slug: open-cursor-repo-blocklists-api
- collection_type: open
  name: Cursor Admin Audit Logs Spend API
  slug: open-cursor-spend-api
- collection_type: open
  name: Cursor Admin Audit Logs Usage API
  slug: open-cursor-usage-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cursor-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cursor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cursor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cursor-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cursor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cursorai
- group: company
  title: ''
  type: Website
  url: https://cursor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cursor.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cursor.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/cursor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cursor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cursor-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://cursor.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://cursor.com/blog
created: '2026-05-08'
description: 'Cursor is an AI-first code editor by Anysphere, forked from VS Code, with deep AI integration: agentic edits, codebase chat, autocomplete, and tab-completion. Offers a hosted plan with model access and team management. Cursor exposes a public Admin API, Analytics API, AI Code Tracking API, Cloud Agents API, and a TypeScript SDK.'
finops:
- name: Cursor Finops
  service_category: AI
  slug: cursor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cursor.png
json_schemas:
- name: Cursor Audit Event
  property_count: 6
  slug: cursor-audit-event
- name: Cursor Daily Usage Record
  property_count: 7
  slug: cursor-daily-usage
- name: Cursor Team Member
  property_count: 5
  slug: cursor-member
jsonld:
- class_count: 25
  name: Cursor Context
  property_count: 0
  slug: cursor-context
layout: provider
modified: '2026-05-19'
name: Cursor
nav: Providers
network: true
overview: 'Cursor publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audit Logs API, Groups API, Members API, and 3 more. Tagged areas include AI, Developer Tools, Code Editor, Agent, and IDE.


  The Cursor catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cursor''s developer surface includes authentication, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Cursor Plans Pricing
  plan_count: 1
  slug: cursor-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Cursor Rate Limits
  slug: cursor-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Cursor API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: cursor-admin-api-rules
- effective_rule_count: 5
  extends: []
  name: Cursor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cursor-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.2
  delta: -1.6
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 45.5
    contract_quality: 60.3
    developer_ergonomics: 14.3
    discoverability: 81.5
    governance: 45.5
    operational_transparency: 7.9
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/screenshots/cursor-2026-06-20T175349.png
security:
- kind: authentication
  name: Cursor Authentication
  slug: cursor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cursor Domain Security
  slug: cursor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cursor Vulnerability Disclosure
  slug: cursor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cursor
tags:
- AI
- Developer Tools
- Code Editor
- Agent
- IDE
- Cloud Agents
website: https://cursor.com/
---
