---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Connected account inventory.
  name: Entergram Accounts API
  slug: entergram-accounts-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Telegram chat creation and group/channel management commands scoped to an explicit connected account.
  name: Entergram Chat Commands API
  slug: entergram-chat-commands-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Actor-scoped chats, linked tickets, and internal chat comments keyed by Telegram chat ID.
  name: Entergram Chats API
  slug: entergram-chats-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Workspace contacts deduplicated across connected accounts, including shared groups and attribution.
  name: Entergram Contacts API
  slug: entergram-contacts-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Workspace chat custom columns, ticket custom columns, selectable options, and workspace-shared chat custom field values.
  name: Entergram Custom Fields API
  slug: entergram-custom-fields-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Metadata-only, cursor-based workspace event stream for resumable integrations.
  name: Entergram Events API
  slug: entergram-events-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Workspace groups derived from shared-contact graph, with invite-link and member metadata when cached.
  name: Entergram Groups API
  slug: entergram-groups-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Actor-owned live Telegram transport view used for current chat discovery before message operations.
  name: Entergram Live Chats API
  slug: entergram-live-chats-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: The Make webhooks API from Entergram — 2 operation(s) for make webhooks.
  name: Entergram Make webhooks API
  slug: entergram-make-webhooks-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Safe workspace member identity, role, permissions, and seat assignment metadata.
  name: Entergram Members API
  slug: entergram-members-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Telegram message history and message write operations scoped to an explicit account and chat.
  name: Entergram Messages API
  slug: entergram-messages-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Authentication and runtime context.
  name: Entergram System API
  slug: entergram-system-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Workspace ticket inventory, ticket detail, comments, and linked chat filters.
  name: Entergram Tickets API
  slug: entergram-tickets-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: API-only webhook endpoint configuration, secret rotation, tests, and sanitized delivery status.
  name: Entergram Webhooks API
  slug: entergram-webhooks-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Workspace metadata and feature access.
  name: Entergram Workspace API
  slug: entergram-workspace-api
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: Shared CRM chat view from frontend DB, deduplicated across workspace accounts and suited for metadata, custom fields, and ticket workflows.
  name: Entergram Workspace Chats API
  slug: entergram-workspace-chats-api
artifact_total: 30
asyncapis:
- description: ''
  name: Entergram Webhooks
  slug: entergram-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/entergram/rate-limits/entergram-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/entergram-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/entergram/capabilities/entergram-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/entergram-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/entergram/mcp/entergram-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/entergram-mcp.yml
- group: other
  href: https://artifacts.apis.io/entergram/overlays/entergram-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/entergram-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/entergram/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.entergram.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.entergram.com/telegram-crm/telegram-crm-api
- group: docs
  title: ''
  type: Documentation
  url: https://api.entergram.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.entergram.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.entergram.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.entergram.com
- group: operate
  title: ''
  type: Support
  url: https://www.entergram.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.entergram.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.entergram.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.entergram.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.entergram.com
- group: operate
  href: https://artifacts.apis.io/entergram/changelog/entergram-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/entergram-changelog.yml
- group: design
  href: https://artifacts.apis.io/entergram/lifecycle/entergram-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/entergram-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/entergram/plans/entergram-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/entergram-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/entergram/llms/entergram-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/entergram-llms.txt
- group: agent
  href: https://artifacts.apis.io/entergram/well-known/entergram-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/entergram-well-known.yml
- group: auth
  href: https://artifacts.apis.io/entergram/well-known/entergram-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/entergram-security.txt
- group: design
  href: https://artifacts.apis.io/entergram/conformance/entergram-conformance.yml
  title: ''
  type: Conformance
  url: conformance/entergram-conformance.yml
- group: auth
  href: https://artifacts.apis.io/entergram/security/entergram-trust-center.yml
  title: ''
  type: Compliance
  url: security/entergram-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/entergram/security/entergram-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/entergram-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/entergram/security/entergram-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/entergram-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/entergram/security/entergram-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/entergram-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/entergram/security/entergram-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/entergram-domain-security.yml
created: '2026-09-11'
description: 'Entergram is a CRM built specifically for Telegram. It connects personal Telegram accounts (not bots) into a shared team workspace where sales, support, community and trading teams manage conversations at scale — a multi-account inbox, a CRM table and Kanban pipeline, custom columns and labels, broadcast messaging, and a ticketing system with assignment, SLA and status tracking. Its developer surface has three parts: a workspace-scoped REST API (X-API-Key) covering accounts, contacts, groups, chats, messages, custom fields, tickets, webhooks and resumable events; a hosted Model Context Protocol (MCP) server for personal Telegram accounts (OAuth2 + PKCE) that lets AI agents read chats, manage tickets and update CRM fields; and outbound webhooks for incoming/outgoing message events, plus a Make.com integration.'
finops:
- has_sources: true
  method: derived
  name: Entergram Finops
  primary_unit: seat
  service_category: ''
  slug: entergram-finops
  template: false
image: https://www.entergram.com/entergram-social-v3.png
layout: provider
mcp_servers:
- description: Hosted Model Context Protocol server for personal Telegram accounts. Connects MCP-compatible AI agents (Claude, ChatGPT, Cursor, Windsurf, Cline, n8n, Make.com) to a shared Entergram Telegram CRM work
  name: Entergram Telegram MCP Server
  slug: entergram-telegram-mcp-server
modified: '2026-09-11'
name: Entergram
nav: Providers
network: true
overview: 'Entergram publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Chat Commands API, Chats API, and 13 more. Tagged areas include Messaging, Notification, Communications, CRM, and Telegram.


  The Entergram catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Entergram''s developer surface includes documentation, API reference, pricing, support, engineering blog, changelog, and 22 more developer resources.'
plans:
- name: Entergram Plans Pricing
  plan_count: 5
  slug: entergram-plans-pricing
- name: Entergram Price Estimates
  plan_count: 0
  slug: entergram-price-estimates
random_paper: 5
rate_limits:
- limit_count: 0
  name: Entergram Rate Limits
  slug: entergram-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Entergram API Rules
  rule_count: 62
  severity_counts:
    error: 46
    hint: 0
    info: 6
    warn: 10
  slug: entergram-rules
scopes:
- name: Entergram Scopes
  scope_count: 19
  slug: entergram-scopes
  summary_line: 19 scopes
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 63.6
    developer_ergonomics: 47.0
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 64.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/entergram/entergram-2026-10-11T104215.png
security:
- kind: authentication
  name: Entergram Authentication
  slug: entergram-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Entergram Domain Security
  slug: entergram-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Entergram Vulnerability Disclosure
  slug: entergram-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Entergram Trust Center
  slug: entergram-trust-center
  summary_line: trust center published
skill_count: 2
skills:
- name: entergram-send-telegram-message
  slug: entergram-send-telegram-message
- name: entergram-triage-chat-to-ticket
  slug: entergram-triage-chat-to-ticket
slug: entergram
tags:
- Messaging
- Notification
- Communications
- CRM
- Telegram
- Customer Service
- Ticketing
- Sales
- MCP
- Webhook
website: https://www.entergram.com
---
