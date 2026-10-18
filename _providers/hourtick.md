---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Hourtick REST API provides task, time tracking, and AI agent operations. Auth via personal API token.
  name: Hourtick API
  slug: hourtick-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Who you are and what you can track on.
  name: Hourtick Account API
  slug: hourtick-account-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: AI agents are workspace members with their own token. Mention one in chat, DM it, or hand it a task, and a session is queued. The agent takes work over MCP (`agent_wait_for_work`), posts progress (`ag
  name: Hourtick Agents API
  slug: hourtick-agents-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Usage (stored data plus data in and out this month) and extra usage. Every plan has unlimited people.
  name: Hourtick Billing API
  slug: hourtick-billing-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Clients, projects and task types (admins).
  name: Hourtick Catalog API
  slug: hourtick-catalog-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: 'Channels, DMs, threads, reactions, files and search. Message bodies are Markdown; reference things with links: `[#12 Title](hourtick://task/<id>)`, `hourtick://project/<id>`, `hourtick://client/<id>`,'
  name: Hourtick Chat API
  slug: hourtick-chat-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Your own accounts in Linear, Notion, Teamwork and Asana. Connecting needs a person's browser (OAuth); AI agents can't connect or link, and never post through a person's connection. Tokens are stored e
  name: Hourtick Integrations API
  slug: hourtick-integrations-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Invoices through the workspace's own Stripe account (Stripe Connect). An admin connects Stripe in Settings; Stripe Invoicing issues, emails and collects each invoice; Hourtick takes no fee (Stripe's o
  name: Hourtick Invoices API
  slug: hourtick-invoices-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Documents and files on a client or a project. Everyone in the workspace can read and add them; the author or a manager deletes. Notes are Tiptap JSON with a plain-text copy (`text`); saves carry a `ve
  name: Hourtick Notes and files API
  slug: hourtick-notes-and-files-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Aggregated time and CSV.
  name: Hourtick Reports API
  slug: hourtick-reports-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: 'The task board: tasks (work items), checklist, chat and files. Any member can create and edit.'
  name: Hourtick Tasks API
  slug: hourtick-tasks-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Approvals, invoicing and members (role-gated).
  name: Hourtick Team API
  slug: hourtick-team-api
- baseURL: https://hourtick.com
  baseurl_source: spec
  description: Timers and time entries. Link time to a task with `workItemId` on start, create or edit.
  name: Hourtick Time API
  slug: hourtick-time-api
artifact_total: 23
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/rules/hourtick-rules.yml
  title: ''
  type: Spectral
  url: rules/hourtick-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/json-ld/hourtick-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hourtick-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/vocabulary/hourtick-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hourtick-vocabulary.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/plans/hourtick-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hourtick-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/data-model/hourtick-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hourtick-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/conventions/hourtick-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hourtick-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/conventions/hourtick-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hourtick-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://hourtick.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/authentication/hourtick-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hourtick-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/errors/hourtick-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hourtick-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/conformance/hourtick-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hourtick-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/llms/hourtick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hourtick-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/mcp/hourtick-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hourtick-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/well-known/hourtick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hourtick-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/hosts/hourtick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hourtick-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hourtick.com/terms
- group: auth
  title: ''
  type: Security
  url: https://hourtick.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hourtick.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://hourtick.com/pricing
- group: start
  title: ''
  type: Login
  url: https://hourtick.com/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://hourtick.com/announcements/a-guide-for-every-ai-app
- group: docs
  title: ''
  type: APIReference
  url: https://hourtick.com/announcements
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hourtick
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/security/hourtick-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hourtick-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/security/hourtick-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hourtick-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hourtick/refs/heads/main/security/hourtick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hourtick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hourtick.com
- group: docs
  title: ''
  type: Documentation
  url: https://hourtick.com/developers
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://hourtick.com/api/mcp
  - status: 200
    url: https://hourtick.com
  reason: partner-login
  state: gated
created: '2026-10-08'
description: Hourtick provides a collaborative platform for tasks, team chat, and time tracking enhanced with AI agents such as Claude, GPT, Grok, and Muse. It enables teams to assign work, monitor progress, and estimate costs using AI-driven insights. The service offers free plans for unlimited users, integrates with popular tools, and includes features like automated time logging, AI-powered task suggestions, and detailed reporting.
image: https://hourtick.com/opengraph-image-pwu6ef?d2b024fd2cd2caaf
json_schemas:
- name: TimeEntry
  property_count: 17
  slug: hourtick-time-entry
- name: WorkItem
  property_count: 18
  slug: hourtick-work-item
jsonld:
- class_count: 3
  name: Hourtick Context
  property_count: 37
  slug: hourtick-context
layout: provider
mcp_servers:
- description: Remote MCP server at hourtick.com.
  name: Hourtick MCP Server
  slug: hourtick-mcp-yml
modified: '2026-10-08'
name: Hourtick
nav: Providers
network: true
overview: 'Hourtick publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Billing API, and 10 more. Tagged areas include Company, Collaboration, Artificial Intelligence, TimeTracking, and Project Management.


  The Hourtick catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hourtick''s developer surface includes authentication, pricing, getting-started guide, API reference, documentation, and 23 more developer resources.'
plans:
- name: Hourtick Plans Pricing
  plan_count: 2
  slug: hourtick-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Hourtick API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: hourtick-rules
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 8.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 35.6
    contract_quality: 56.3
    developer_ergonomics: 40.5
    discoverability: 66.7
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Hourtick Authentication
  slug: hourtick-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hourtick Domain Security
  slug: hourtick-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hourtick Vulnerability Disclosure
  slug: hourtick-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Hourtick Trust Center
  slug: hourtick-trust-center
  summary_line: PCI DSS, GDPR
slug: hourtick
tags:
- Company
- Collaboration
- Artificial Intelligence
- TimeTracking
- Project Management
website: https://hourtick.com
---
