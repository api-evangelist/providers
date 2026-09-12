---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 69.6
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Publora Agentic Access
  operation_count: 36
  slug: publora-agentic-access
  summary_line: 36 operations · 29 acting
api_count: 1
apis:
- baseURL: https://api.publora.com/api/v1
  baseurl_source: declared
  description: REST API and remote MCP server for scheduling and publishing social media posts across ten platforms from one integration, with media uploads, per-platform settings, HMAC-signed webhooks, LinkedIn ana
  name: Publora API
  slug: publora-api
artifact_total: 8
asyncapis:
- description: ''
  name: Publora Webhooks
  slug: publora-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/publora-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/publora-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/publora-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/publora-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/publora-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/publora-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/publora-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/publora-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/publora-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/publora-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.publora.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/publora-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/publora-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/publora-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/publora-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/publora-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/publora-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/publora-openapi-overlay.yaml
- group: commercial
  title: ''
  type: Pricing
  url: https://publora.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://publora.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://publora.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://publora.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://publora.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/publora
- group: company
  title: ''
  type: Website
  url: https://publora.com
created: '2026-09-11'
description: Publora is a social media scheduling and publishing platform with a REST API and a native remote MCP server. One integration publishes and schedules posts across LinkedIn, X (Twitter), Instagram, Threads, TikTok, YouTube, Facebook, Bluesky, Mastodon, and Telegram, with pre-signed media uploads, per-platform settings, HMAC-signed webhooks for post-lifecycle events, LinkedIn analytics and engagement actions, and a workspace/B2B layer for managed users. It uses long-lived API-key authentication, idempotent create/update operations, and exposes 18 MCP tools callable directly by AI agents (keyless tools/list).
image: https://publora.com/publora-preview.png
layout: provider
mcp_servers:
- description: ''
  name: Publora MCP Server
  slug: publora-mcp-server
modified: '2026-09-11'
name: Publora
nav: Providers
network: true
overview: 'Publora publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Publishing, Scheduling, MCP, and Content.


  The Publora catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Publora''s developer surface includes authentication, changelog, sandbox, pricing, signup flow, engineering blog, and 20 more developer resources.'
plans:
- name: Publora Plans Pricing
  plan_count: 3
  slug: publora-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Publora Rate Limits
  slug: publora-rate-limits
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 68.3
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 68.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Publora Authentication
  slug: publora-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Publora Domain Security
  slug: publora-domain-security
  summary_line: TLSv1.3 · DMARC
slug: publora
tags:
- Social Media
- Publishing
- Scheduling
- MCP
- Content
- Social Media Management
- Webhooks
- AI Agents
website: https://publora.com
---
