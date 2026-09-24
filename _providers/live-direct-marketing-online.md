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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 835
  human_in_the_loop: 835
  name: Live Direct Marketing Online Agentic Access
  operation_count: 1500
  slug: live-direct-marketing-online-agentic-access
  summary_line: 1500 operations · 835 acting · 835 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.live-direct-marketing.online
  baseurl_source: declared
  description: 'Multi-tenant B2B outreach automation platform exposed as one Bearer-authenticated HTTPS surface for the web UI, MCP and A2A clients. 1,304 operations across 119 tags: companies, contacts, leads and pi'
  name: LDM v3 API
  slug: ldm-v3-api
- description: Remote Streamable-HTTP MCP server at https://api.live-direct-marketing.online/mcp (protocol 2025-06-18, server ldm-delivery 0.6.1). An anonymous session exposes three bootstrap tools — ldm_health, ldm
  name: LDM MCP Server
  slug: ldm-mcp-server
- description: 'A2A 0.3.0-shaped agent card served at https://api.live-direct-marketing.online/.well-known/agent.json (237 curated skills of 1,270, ?full=1 for all; capabilities streaming + pushNotifications) with a '
  name: LDM.delivery A2A Agent
  slug: ldm-a2a-agent
- description: Outbound HTTPS webhook subscriptions for lead, dialog and task events (lead.created, lead.moved, lead.won, lead.lost, dialog.received, dialog.replied, task.completed, task.failed), signed with X-LDM-S
  name: LDM Webhook Events
  slug: ldm-webhook-events
- baseURL: https://check.live-direct-marketing.online
  baseurl_source: declared
  description: 'Email deliverability test API behind the free Inbox Placement Test at check.live-direct-marketing.online: create a test, send to the returned seed mailboxes across ten providers, poll placement, SPF /'
  name: Inbox Check API
  slug: inbox-check-api
- description: 'Remote Streamable-HTTP MCP server at https://check.live-direct-marketing.online/mcp requiring Authorization: Bearer icp_live_* (anonymous tools/list answers 401 Problem Details). Tools mirror the agen'
  name: Inbox Check MCP Server
  slug: inbox-check-mcp-server
- description: Provider-shaped agent card at https://check.live-direct-marketing.online/.well-known/agent.json listing 21 REST-bound skills with HTTP method, URL and input_schema. The provider states that A2A suppor
  name: Inbox Check A2A Agent Card
  slug: inbox-check-a2a-agent
artifact_total: 18
asyncapis:
- description: ''
  name: Live Direct Marketing Online Webhooks
  slug: live-direct-marketing-online-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/security/live-direct-marketing-online-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/live-direct-marketing-online-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://developers.live-direct-marketing.online/legal/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/security/live-direct-marketing-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/live-direct-marketing-online-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/agentic-access/live-direct-marketing-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/live-direct-marketing-online-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://live-direct-marketing.online/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.live-direct-marketing.online/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.live-direct-marketing.online/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.live-direct-marketing.online/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.live-direct-marketing.online/quickstart
- group: operate
  title: ''
  type: Support
  url: https://live-direct-marketing.online/contact
- group: company
  title: ''
  type: Blog
  url: https://live-direct-marketing.online/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/live-direct-marketing
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.live-direct-marketing.online/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developers.live-direct-marketing.online/signup
- group: start
  title: ''
  type: Login
  url: https://app.live-direct-marketing.online/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://live-direct-marketing.online/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://live-direct-marketing.online/policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/101983165/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.live-direct-marketing.online/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/changelog/live-direct-marketing-online-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/live-direct-marketing-online-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/llms/live-direct-marketing-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/live-direct-marketing-online-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/llms/live-direct-marketing-online-developers-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/live-direct-marketing-online-developers-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/llms/live-direct-marketing-online-inbox-check-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/live-direct-marketing-online-inbox-check-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/packages/live-direct-marketing-online-packages.yml
  title: ''
  type: Packages
  url: packages/live-direct-marketing-online-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/packages/live-direct-marketing-online-packages.yml
  title: ''
  type: SDKs
  url: packages/live-direct-marketing-online-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/well-known/live-direct-marketing-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/live-direct-marketing-online-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/well-known/live-direct-marketing-online-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/live-direct-marketing-online-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/a2a/live-direct-marketing-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/live-direct-marketing-online-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/conformance/live-direct-marketing-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/live-direct-marketing-online-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/errors/live-direct-marketing-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/live-direct-marketing-online-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/lifecycle/live-direct-marketing-online-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/live-direct-marketing-online-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/authentication/live-direct-marketing-online-authentication.yml
  title: ''
  type: Authentication
  url: authentication/live-direct-marketing-online-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/scopes/live-direct-marketing-online-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/live-direct-marketing-online-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/conventions/live-direct-marketing-online-conventions.yml
  title: ''
  type: Conventions
  url: conventions/live-direct-marketing-online-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/conventions/live-direct-marketing-online-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/live-direct-marketing-online-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/sandbox/live-direct-marketing-online-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/live-direct-marketing-online-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/plans/live-direct-marketing-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/live-direct-marketing-online-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/rate-limits/live-direct-marketing-online-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/live-direct-marketing-online-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/asyncapi/live-direct-marketing-online-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/live-direct-marketing-online-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/data-model/live-direct-marketing-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/live-direct-marketing-online-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/live-direct-marketing-online/refs/heads/main/regulatory/live-direct-marketing-online-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/live-direct-marketing-online-regulatory-posture.yml
created: '2026-09-19'
description: 'Live Direct Marketing (LDM) is a B2B outreach and CRM platform built to be operated by AI agents: the same Bearer-authenticated HTTPS surface serves the web UI, MCP clients and A2A peers. The LDM v3 API publishes an OpenAPI 3.0 contract with 1,304 operations across 119 tags (companies, contacts, leads, pipelines, campaigns, creatives, mailboxes, deliverability probes, suppression and stop-lists, webhooks, billing, DSAR) and a remote Streamable-HTTP MCP server with an anonymous bootstrap (ldm_terms / ldm_register) that mints a scoped ldm_* key without a human. A second product, Inbox Check, is a free inbox-placement test with its own 196-operation OpenAPI, a remote MCP server and an A2A agent card at check.live-direct-marketing.online. Billing is per confirmed inbox delivery ($0.015 managed / $0.005 BYOC), read from a public pricing endpoint. The operator is a Russian entity (OOO LDM, Yaroslavl); legal documents are drafts pending lawyer review.'
image: https://live-direct-marketing.online/img/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Live Direct Marketing MCP Server
  slug: live-direct-marketing-mcp-server
- description: ''
  name: Remote endpoint (Streamable HTTP)
  slug: remote-endpoint-streamable-http
- description: ''
  name: Remote endpoint (Streamable HTTP)
  slug: remote-endpoint-streamable-http-2
modified: '2026-09-19'
name: Live Direct Marketing
nav: Providers
network: true
overview: 'Live Direct Marketing publishes 2 APIs on the [APIs.io](https://apis.io/) network: LDM v3 API and Inbox Check API. Tagged areas include Company, Email, Email Deliverability, Sales & marketing automation, and CRM.


  The Live Direct Marketing catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Live Direct Marketing''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Live Direct Marketing Online Plans Pricing
  plan_count: 3
  slug: live-direct-marketing-online-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 8
  name: Live Direct Marketing Online Rate Limits
  slug: live-direct-marketing-online-rate-limits
scopes:
- name: Live Direct Marketing Online Scopes
  scope_count: 0
  slug: live-direct-marketing-online-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 49.5
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 71.1
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Live Direct Marketing Online Authentication
  slug: live-direct-marketing-online-authentication
  summary_line: http bearer/apiKey (header)/cookie session · 6 schemes
- kind: domain-security
  name: Live Direct Marketing Online Domain Security
  slug: live-direct-marketing-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Live Direct Marketing Online Vulnerability Disclosure
  slug: live-direct-marketing-online-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: live-direct-marketing-online
tags:
- Company
- Email
- Email Deliverability
- Sales & marketing automation
- CRM
- Lead Management
- Cold Outreach
- Agent-Native
- MCP
- A2A
- Webhook
- B2B
website: https://live-direct-marketing.online/
---
