---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.9
  scored_at: '2026-09-12'
api_count: 1
apis:
- baseURL: https://api.entergram.com
  baseurl_source: declared
  description: ''
  name: Entergram API
  slug: entergram-api
artifact_total: 10
asyncapis:
- description: ''
  name: Entergram Webhooks
  slug: entergram-webhooks
common:
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
  title: ''
  type: ChangeLog
  url: changelog/entergram-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/entergram-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/entergram-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/entergram-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/entergram-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/entergram-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/entergram-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/entergram-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/entergram-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/entergram-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/entergram-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/entergram-domain-security.yml
created: '2026-09-11'
description: 'Entergram is a CRM built specifically for Telegram. It connects personal Telegram accounts (not bots) into a shared team workspace where sales, support, community and trading teams manage conversations at scale — a multi-account inbox, a CRM table and Kanban pipeline, custom columns and labels, broadcast messaging, and a ticketing system with assignment, SLA and status tracking. Its developer surface has three parts: a workspace-scoped REST API (X-API-Key) covering accounts, contacts, groups, chats, messages, custom fields, tickets, webhooks and resumable events; a hosted Model Context Protocol (MCP) server for personal Telegram accounts (OAuth2 + PKCE) that lets AI agents read chats, manage tickets and update CRM fields; and outbound webhooks for incoming/outgoing message events, plus a Make.com integration.'
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
overview: 'Entergram publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Notifications, Communications, CRM, and Telegram.


  The Entergram catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Entergram''s developer surface includes documentation, API reference, pricing, support, engineering blog, changelog, and 17 more developer resources.'
plans:
- name: Entergram Plans Pricing
  plan_count: 3
  slug: entergram-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Entergram Rate Limits
  slug: entergram-rate-limits
scopes:
- name: Entergram Scopes
  scope_count: 0
  slug: entergram-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 47.0
    discoverability: 75.9
    operational_transparency: 50.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  upsert:
    applies: true
    score: 0.0
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
slug: entergram
tags:
- Messaging
- Notifications
- Communications
- CRM
- Telegram
- Customer Support
- Ticketing
- Sales
- MCP
- Webhooks
website: https://www.entergram.com
---
