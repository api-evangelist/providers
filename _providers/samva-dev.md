---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 224
  human_in_the_loop: 5
  name: Samva Dev Agentic Access
  operation_count: 376
  slug: samva-dev-agentic-access
  summary_line: 376 operations · 224 acting · 5 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Agents that answer conversations on your mailbox endpoints, with a draft, published versions, and rules for supervision, hours, and staff takeover
  name: samva-dev Agents API
  slug: samva-dev-agents-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Messaging analytics, channel stats, and data export. Every date range is half-open — `after` inclusive, `before` exclusive — and may span at most 366 days. Both bounds are absolute ISO-8601 instants c
  name: samva-dev Analytics API
  slug: samva-dev-analytics-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: API key management, rotation, and usage statistics
  name: samva-dev API Keys API
  slug: samva-dev-api-keys-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Email attachment metadata and secure download URLs
  name: samva-dev Attachments API
  slug: samva-dev-attachments-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Brand themes, logos and footers that templates import with `samva:brand`.
  name: samva-dev Brands API
  slug: samva-dev-brands-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Campaign drafts and scheduled campaign runs
  name: samva-dev Campaigns API
  slug: samva-dev-campaigns-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: A contact's custom and lifecycle event timeline
  name: samva-dev Contact events API
  slug: samva-dev-contact-events-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Segment management — static and dynamic groups with membership operations
  name: samva-dev Contact Groups API
  slug: samva-dev-contact-groups-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Contact CRUD, bulk operations, engagement metrics, and activity timeline
  name: samva-dev Contacts API
  slug: samva-dev-contacts-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Create, update, and list conversations with your contacts.
  name: samva-dev Conversations API
  slug: samva-dev-conversations-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Custom field definitions for contact metadata
  name: samva-dev Custom Fields API
  slug: samva-dev-custom-fields-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Unified email domain for sending, domains, templates, threads, catch-all, blocking, forwarding, and onboarding
  name: samva-dev Email API
  slug: samva-dev-email-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Custom contact event ingestion
  name: samva-dev Events API
  slug: samva-dev-events-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Extension versions installed into the organization, each acting as its own principal
  name: samva-dev Extension installations API
  slug: samva-dev-extension-installations-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Code that receives mailbox events and acts through the mailbox API
  name: samva-dev Extensions API
  slug: samva-dev-extensions-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Reports to Samva about the API itself.
  name: samva-dev Feedback API
  slug: samva-dev-feedback-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Event-triggered, per-contact email flows defined as versioned node graphs
  name: samva-dev Journeys API
  slug: samva-dev-journeys-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: 'Mailboxes: endpoints, threads, messages, drafts, and governed sends'
  name: samva-dev Mailboxes API
  slug: samva-dev-mailboxes-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Media objects and the presigned uploads that fill them
  name: samva-dev Media API
  slug: samva-dev-media-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Send messages and read their delivery state and timeline.
  name: samva-dev Messages API
  slug: samva-dev-messages-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Sub-tenants that confine domains, senders, mailboxes, contacts, templates, and API keys inside an organization
  name: samva-dev Namespaces API
  slug: samva-dev-namespaces-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Custom domains for newsletter archives
  name: samva-dev Newsletter domains API
  slug: samva-dev-newsletter-domains-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Newsletter-owned newsletter Markdown files and their Git workspace
  name: samva-dev Newsletter issues API
  slug: samva-dev-newsletter-issues-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Newsletters, their consent topics, and publishing settings
  name: samva-dev Newsletters API
  slug: samva-dev-newsletters-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Status of accepted asynchronous mutations
  name: samva-dev Operations API
  slug: samva-dev-operations-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Organization management and usage statistics
  name: samva-dev Organizations API
  slug: samva-dev-organizations-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: The Samva API API from samva-dev — 0 operation(s) for samva api.
  name: samva-dev Samva API
  slug: samva-dev-samva-api-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: One-off scheduled message timers
  name: samva-dev Scheduled Messages API
  slug: samva-dev-scheduled-messages-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Recipient-confirmed topic subscriptions
  name: samva-dev Subscriptions API
  slug: samva-dev-subscriptions-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Git-backed email template projects, workspace editing, immutable publications, and delivery defaults
  name: samva-dev Templates API
  slug: samva-dev-templates-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Hosted and embedded double opt-in signup forms for topics
  name: samva-dev Topic forms API
  slug: samva-dev-topic-forms-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Topics and per-channel contact subscriptions
  name: samva-dev Topics API
  slug: samva-dev-topics-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: Customer event webhook management, testing, and delivery logs
  name: samva-dev Webhooks API
  slug: samva-dev-webhooks-api
- baseURL: https://api.samva.dev
  baseurl_source: declared
  description: The organization and credential behind the request.
  name: samva-dev Whoami API
  slug: samva-dev-whoami-api
artifact_total: 55
asyncapis:
- description: ''
  name: Samva Dev Webhooks
  slug: samva-dev-webhooks
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://samva.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://samva.dev/legal/privacy
- group: agent
  href: https://artifacts.apis.io/samva-dev/agentic-access/samva-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/samva-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/samva-dev/plans/samva-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/samva-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/samva-dev/rules/samva-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/samva-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/samva-dev/json-ld/samva-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/samva-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/samva-dev/vocabulary/samva-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/samva-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/samva-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/samva-dev/asyncapi/samva-dev-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/samva-dev-webhooks.yml
- group: design
  href: https://artifacts.apis.io/samva-dev/data-model/samva-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/samva-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/samva-dev/cli/samva-dev-cli.yml
  title: ''
  type: CLI
  url: cli/samva-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/samva-dev/conventions/samva-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/samva-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/samva-dev/conventions/samva-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/samva-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/samva-dev/authentication/samva-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/samva-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/samva-dev/errors/samva-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/samva-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/samva-dev/conformance/samva-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/samva-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/samva-dev/llms/samva-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/samva-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/samva-dev/mcp/samva-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/samva-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/samva-dev/well-known/samva-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/samva-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/samva-dev/hosts/samva-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/samva-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/samva-dev/vendors/samva-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/samva-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.samva.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://samva.dev/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://samva.dev/changelog
- group: auth
  href: https://artifacts.apis.io/samva-dev/security/samva-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/samva-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://samva.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://samva.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://samva.dev/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://samva.dev/docs/developers
- group: operate
  title: ''
  type: Support
  url: https://samva.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://samva.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://samva.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://samva.dev/signup?entry=marketing_page
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/samva-dev/workspace
created: '2026-10-31'
description: Samva provides a developer-friendly Email API platform enabling transactional, inbound, and campaign email sending, along with webhook events and a hosted MCP server for AI agents. It offers a TypeScript SDK, CLI, and REST endpoints, supporting domain verification, template management, and integration with WhatsApp soon. Ideal for SaaS apps, support teams, and businesses needing reliable email communication.
image: https://samva.dev/og/home/index.png
json_schemas:
- name: Contact
  property_count: 16
  slug: samva-dev-contact
- name: Conversation
  property_count: 30
  slug: samva-dev-conversation
- name: EmailDomainVerification
  property_count: 15
  slug: samva-dev-email-domain-verification
- name: MailboxMessage
  property_count: 18
  slug: samva-dev-mailbox-message
- name: Message
  property_count: 23
  slug: samva-dev-message
- name: Template
  property_count: 26
  slug: samva-dev-template
jsonld:
- class_count: 120
  name: Samva Dev Context
  property_count: 178
  slug: samva-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at samva.dev.
  name: samva-dev MCP Server
  slug: samva-dev-mcp-yml
modified: '2026-10-31'
name: samva-dev
nav: Providers
network: true
overview: 'samva-dev publishes 34 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Analytics API, API Keys API, and 31 more. Tagged areas include Company, Email, API, SaaS, and Developer.


  The samva-dev catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  samva-dev''s developer surface includes CLI, authentication, changelog, documentation, API reference, getting-started guide, support, and 27 more developer resources.'
plans:
- name: Samva Dev Plans Pricing
  plan_count: 9
  slug: samva-dev-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 8
  name: Samva Dev Rate Limits
  slug: samva-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: samva-dev API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: samva-dev-rules
scopes:
- name: Samva Dev Scopes
  scope_count: 0
  slug: samva-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 96.6
    catalog_earned_first_party: 0.0
    catalog_gap: 18.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 70.9
    contract_quality: 68.6
    developer_ergonomics: 75.5
    discoverability: 65.0
    operational_transparency: 67.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Samva Dev Authentication
  slug: samva-dev-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Samva Dev Domain Security
  slug: samva-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: samva-dev-create-contact-with-tags
  slug: samva-dev-create-contact-with-tags
- name: samva-dev-create-organization
  slug: samva-dev-create-organization
- name: samva-dev-monitor-and-retry-operations
  slug: samva-dev-monitor-and-retry-operations
- name: samva
  slug: samva-dev-samva
- name: samva-dev-webhook-create-and-test
  slug: samva-dev-webhook-create-and-test
slug: samva-dev
tags:
- Company
- Email
- API
- SaaS
- Developer
website: https://samva.dev/
---
