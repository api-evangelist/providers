---
access_model:
  confidence: high
  label: Self-serve signup with a 14-day free trial
  onboarding: self-serve
  pricing: paid
  public: true
  source:
  - https://www.lemlist.com/pricing
  - https://app.lemlist.com/create-account
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 84
  human_in_the_loop: 0
  name: Lemlist Agentic Access
  operation_count: 143
  slug: lemlist-agentic-access
  summary_line: 143 operations · 84 acting
api_count: 3
apis:
- description: lemlist's hosted remote Model Context Protocol server. An MCP client POSTs to https://app.lemlist.com/mcp and authenticates with OAuth 2.1 (authorization code + PKCE, dynamic client registration) or a
  name: lemlist MCP Server
  slug: mcp-server
- description: Campaign CRUD and lifecycle - create, update, duplicate, start, pause, validation statutes, stats, reports and asynchronous exports.
  name: lemlist Campaigns API
  slug: lemlist-campaigns-api
- description: Campaign sequences, their steps, and A/B test variants on email steps.
  name: lemlist Sequences API
  slug: lemlist-sequences-api
- description: Leads inside campaigns - create with optional enrichment, update, pause, resume, mark interested, custom variables, CRM import and unsubscribe.
  name: lemlist Leads API
  slug: lemlist-leads-api
- description: Search the lemlist B2B people and company database, list its filters, and manage saved personas.
  name: lemlist People Database API
  slug: lemlist-people-database-api
- description: Asynchronous enrichment - find and verify emails, phone numbers and LinkedIn data, single or in bulk, then poll for the result. Credit-metered.
  name: lemlist Enrich API
  slug: lemlist-enrich-api
- description: The unified reply inbox - conversations, messages, drafts, labels and sending on email, LinkedIn and WhatsApp.
  name: lemlist Inbox API
  slug: lemlist-inbox-api
- description: CRM-side contacts, contact lists, list membership and exports.
  name: lemlist Contacts API
  slug: lemlist-contacts-api
- description: CRM-side companies and company notes.
  name: lemlist Companies API
  slug: lemlist-companies-api
- description: Signal Agents (watch lists) - create and configure watches, list the available signal types and filters, read detected signals, and push external signals.
  name: lemlist Signal Agents API
  slug: lemlist-signal-agents-api
- description: Webhook subscription management - list, create with an optional shared secret, and delete. 76 event types are documented.
  name: lemlist Webhooks API
  slug: lemlist-webhooks-api
- description: Suppression management - unsubscribe and re-subscribe contacts and variables, list and export the suppression set, and the legacy email/domain surface.
  name: lemlist Unsubscribes API
  slug: lemlist-unsubscribes-api
- description: Sending schedules - CRUD and association with campaigns.
  name: lemlist Schedules API
  slug: lemlist-schedules-api
- description: Manual tasks - list, create, update and ignore.
  name: lemlist Tasks API
  slug: lemlist-tasks-api
- description: The activity history feed, and deletion of call recordings and transcripts.
  name: lemlist Activities API
  slug: lemlist-activities-api
- description: Team-level endpoints - team information, senders, remaining credits and CRM users.
  name: lemlist Team API
  slug: lemlist-team-api
- description: User endpoints - user detail and the connected channels available to the authenticated user.
  name: lemlist Users API
  slug: lemlist-users-api
- description: Connect, test and disconnect custom SMTP/IMAP sending accounts.
  name: lemlist Email Accounts API
  slug: lemlist-email-accounts-api
- description: lemwarm mailbox warm-up - start, pause, and read or update warm-up settings per mailbox.
  name: lemlist lemwarm API
  slug: lemlist-lemwarm-api
- description: Threshold alerts on deliverability metrics - create, read, update and delete.
  name: lemlist Deliverability Alerts API
  slug: lemlist-deliverability-alerts-api
- description: The custom field definitions available on leads, contacts and companies.
  name: lemlist Fields API
  slug: lemlist-fields-api
- description: The Stats API from lemlist — 2 operation(s) for stats.
  name: lemlist Stats API
  slug: lemlist-stats-api
artifact_total: 39
asyncapis:
- description: ''
  name: Lemlist Webhooks
  slug: lemlist-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: lemlist Campaigns API
  slug: open-lemlist-campaigns-api
- collection_type: open
  name: lemlist Campaigns Team API
  slug: open-lemlist-team-api
- collection_type: open
  name: lemlist Campaigns Users API
  slug: open-lemlist-users-api
- collection_type: open
  name: lemlist API
  slug: open-lemlist
common:
- group: company
  title: ''
  type: Website
  url: https://www.lemlist.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lemlist.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lemlist.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lemlist.com/api-reference/getting-started/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lemlist.com/api-reference/getting-started/overview
- group: operate
  title: ''
  type: Support
  url: https://help.lemlist.com
- group: company
  title: ''
  type: Blog
  url: https://www.lemlist.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/l3mpire
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lemlist.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.lemlist.com/create-account
- group: start
  title: ''
  type: Login
  url: https://app.lemlist.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lemlist.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lemlist.com/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lemlist
- group: commercial
  title: ''
  type: Plans
  url: plans/lemlist-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lemlist-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lemlist-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lemlist-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lemlist-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lemlist-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lemlist-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/lemlist-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lemlist-api-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lemlist-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lemlist.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.lemlist.com/api-reference/getting-started/version
- group: design
  title: ''
  type: Conformance
  url: conformance/lemlist-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.lemlist.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/lemlist-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/lemlist
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lemlist-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemlist-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lemlist-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lemlist-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lemlist-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/lemlist-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lemlist-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/lemlist-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lemlist-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lemlist-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lemlist-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.lemlist.com/llms.txt
created: '2026-05-11'
description: lemlist is a sales engagement and cold outreach platform from lempire that helps sales teams build prospect lists, personalize multichannel campaigns across email, LinkedIn, phone, SMS and WhatsApp, and automate follow-ups to book more meetings. It includes a 650M+ record B2B lead database, credit-metered email and phone enrichment, Signal Agents that watch for buying triggers, a unified reply inbox, and lemwarm deliverability warm-up. The developer surface is unusually agent-forward for its category - a 143-operation REST API documented with a published OpenAPI, a hosted remote MCP server at app.lemlist.com/mcp with OAuth 2.1 and dynamic client registration, an official OpenAPI-generated CLI on npm, an llms.txt index, a published Agent Skill, and a 76-event webhook catalog.
examples:
- key_count: 143
  name: Lemlist Examples
  slug: lemlist-examples
graphqls:
- description: '> **Not a lemlist product. Not published by lemlist.**'
  name: lemlist GraphQL Schema
  slug: lemlist-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lemlist.png
layout: provider
mcp_servers:
- description: ''
  name: lemlist MCP Server
  slug: lemlist-mcp-server
modified: '2026-08-13'
name: lemlist
nav: Providers
network: true
overview: 'lemlist publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Sequences API, Leads API, and 18 more. Tagged areas include Email Outreach, Sales Engagement, Cold Email, Sales Automation, and LinkedIn Outreach.


  The lemlist catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  lemlist''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Lemlist Plans Pricing
  plan_count: 3
  slug: lemlist-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Lemlist Rate Limits
  slug: lemlist-rate-limits
scopes:
- name: Lemlist Scopes
  scope_count: 14
  slug: lemlist-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 26
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 60.7
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemlist/refs/heads/main/screenshots/lemlist-2026-06-20T184417.png
security:
- kind: authentication
  name: Lemlist Authentication
  slug: lemlist-authentication
  summary_line: http/apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Lemlist Domain Security
  slug: lemlist-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lemlist Vulnerability Disclosure
  slug: lemlist-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lemlist Trust Center
  slug: lemlist-trust-center
  summary_line: SOC 2 Type 2
slug: lemlist
tags:
- Email Outreach
- Sales Engagement
- Cold Email
- Sales Automation
- LinkedIn Outreach
- Lead Generation
- Data Enrichment
- Deliverability
- CRM
- Multichannel Messaging
- Webhook
- MCP
website: https://www.lemlist.com
---
